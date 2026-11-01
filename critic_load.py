"""Valide et charge les critiques (fidelite et science) d'un article.

    python -I critic_load.py PMC1234567

Verifie que chaque `article_says` est une sous-chaine du texte, que chaque appui `litterature`
a une source, puis remplit les tables `critiques` et `plausibility`.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402

CRIT_DIR = db.ROOT / "critiques"
SEVERITIES = {"faux", "attribution", "manquant", "non_cite_a_tort", "deduit", "mineur"}
VERDICTS = {"conforme", "corrections_mineures", "corrections_majeures", "a_refaire"}
SCI_VERDICTS = {"coherente", "douteuse", "incoherente", "invérifiable", "inverifiable"}


def ensure_tables(con):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS critiques (
        id INTEGER PRIMARY KEY, paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
        kind TEXT NOT NULL, verdict TEXT, severity TEXT, location TEXT, extracted TEXT, article_says TEXT,
        fix TEXT, confidence TEXT, status TEXT NOT NULL DEFAULT 'ouvert', resolution TEXT, created_at TEXT);
    CREATE TABLE IF NOT EXISTS plausibility (
        id INTEGER PRIMARY KEY, paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
        route_id INTEGER, branch_label TEXT,   -- route_id sans cle etrangere : relie par branch_label (load.py)
        verdict TEXT, feasibility TEXT, mechanism_assessment TEXT, mechanism_proposed TEXT,
        checks_json TEXT, sources_json TEXT, to_verify_json TEXT, created_at TEXT);
    CREATE TABLE IF NOT EXISTS plausibility_paper (
        paper_id INTEGER PRIMARY KEY REFERENCES papers(id) ON DELETE CASCADE,
        summary TEXT, author_errors_json TEXT, comparison TEXT, sources_not_found_json TEXT, created_at TEXT);
    """)
    # migration : l'ancienne table perdait ses lignes a chaque rechargement d'extraction (cascade sur route_id)
    sql = con.execute("SELECT sql FROM sqlite_master WHERE name='plausibility'").fetchone()[0]
    if "REFERENCES synthesis_routes" in sql:
        con.executescript("""
        CREATE TABLE plausibility_new (
            id INTEGER PRIMARY KEY, paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
            route_id INTEGER, branch_label TEXT, verdict TEXT, feasibility TEXT, mechanism_assessment TEXT,
            mechanism_proposed TEXT, checks_json TEXT, sources_json TEXT, to_verify_json TEXT, created_at TEXT);
        INSERT INTO plausibility_new SELECT * FROM plausibility;
        DROP TABLE plausibility; ALTER TABLE plausibility_new RENAME TO plausibility;""")


def main():
    pmcid = sys.argv[1]
    con = db.connect()
    ensure_tables(con)
    paper = con.execute("SELECT id FROM papers WHERE pmcid=?", (pmcid,)).fetchone()
    flat, _ = db.load_text(pmcid)
    errors = []
    pid = paper["id"]

    fid = CRIT_DIR / f"{pmcid}.json"
    if fid.exists():
        d = json.loads(fid.read_text(encoding="utf-8"))
        if d.get("verdict") not in VERDICTS:
            errors.append(f"verdict inconnu: {d.get('verdict')!r}")
        for i, f in enumerate(d.get("findings") or []):
            if f.get("severity") not in SEVERITIES:
                errors.append(f"findings[{i}]: severity inconnue {f.get('severity')!r}")
            says = db.norm(f.get("article_says") or "")
            if not says or says not in flat:
                errors.append(f"findings[{i}] ({f.get('where')}): article_says absent du texte: {says[:80]!r}")
        if not errors:
            # un rechargement ne doit pas effacer les decisions deja prises par l'orchestrateur
            kept = {(r["location"], r["article_says"]): (r["status"], r["resolution"]) for r in con.execute(
                "SELECT location, article_says, status, resolution FROM critiques WHERE paper_id=? AND kind='fidelite'"
                " AND status != 'ouvert'", (pid,))}
            con.execute("DELETE FROM critiques WHERE paper_id=? AND kind='fidelite'", (pid,))
            for f in d.get("findings") or []:
                says = db.norm(f["article_says"])
                status, resolution = kept.get((f.get("where"), says), ("ouvert", None))
                con.execute("INSERT INTO critiques (paper_id, kind, verdict, severity, location, extracted,"
                            " article_says, fix, confidence, status, resolution, created_at)"
                            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                            (pid, "fidelite", d["verdict"], f["severity"], f.get("where"), str(f.get("extracted")),
                             says, f.get("fix"), f.get("confidence"), status, resolution, db.now()))
            if not d.get("findings"):
                con.execute("INSERT INTO critiques (paper_id, kind, verdict, status, created_at) VALUES (?,?,?,?,?)",
                            (pid, "fidelite", d["verdict"], "accepte", db.now()))
            print(f"fidelite: verdict {d['verdict']}, {len(d.get('findings') or [])} constats")

    fsci = CRIT_DIR / f"{pmcid}_science.json"
    if fsci.exists():
        d = json.loads(fsci.read_text(encoding="utf-8"))
        labels = {r["branch_label"]: r["id"] for r in con.execute(
            "SELECT id, branch_label FROM synthesis_routes WHERE paper_id=?", (pid,))}
        for i, r in enumerate(d.get("routes") or []):
            # route_removed : pose par l'orchestrateur quand la voie jugee a ete supprimee apres la critique
            if r.get("label") not in labels and not r.get("route_removed"):
                errors.append(f"routes[{i}]: label inconnu {r.get('label')!r}")
            if r.get("verdict") not in SCI_VERDICTS:
                errors.append(f"routes[{i}]: verdict inconnu {r.get('verdict')!r}")
            for j, c in enumerate(r.get("checks") or []):
                if c.get("basis") == "litterature" and not (c.get("source") or {}).get("url_or_doi"):
                    errors.append(f"routes[{i}].checks[{j}]: appui 'litterature' sans source (url_or_doi)")
        if not errors:
            con.execute("DELETE FROM plausibility WHERE paper_id=?", (pid,))
            for r in d.get("routes") or []:
                m = r.get("mechanism") or {}
                con.execute("INSERT INTO plausibility (paper_id, route_id, branch_label, verdict, feasibility,"
                            " mechanism_assessment, mechanism_proposed, checks_json, sources_json, to_verify_json,"
                            " created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                            (pid, labels.get(r["label"]), r["label"], r["verdict"], r.get("feasibility"),
                             m.get("assessment"), m.get("proposed"),
                             json.dumps(r.get("checks") or [], ensure_ascii=False),
                             json.dumps(m.get("sources") or [], ensure_ascii=False),
                             json.dumps(r.get("what_to_verify_before_repeating") or [], ensure_ascii=False), db.now()))
            a = d.get("article_level") or {}
            con.execute("INSERT OR REPLACE INTO plausibility_paper VALUES (?,?,?,?,?,?)",
                        (pid, a.get("summary"), json.dumps(a.get("author_errors_suspected") or [], ensure_ascii=False),
                         a.get("comparison_with_database"), json.dumps(d.get("sources_not_found") or [], ensure_ascii=False),
                         db.now()))
            n_pb = sum(1 for r in d.get("routes") or [] for c in r.get("checks") or [] if c.get("status") == "probleme")
            print(f"science: {len(d.get('routes') or [])} voies evaluees, {n_pb} problemes")
    for e in errors:
        print("ERREUR", e)
    if errors:
        raise SystemExit(1)
    con.commit()


if __name__ == "__main__":
    main()
