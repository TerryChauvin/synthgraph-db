"""File d'attente, verrou et etat d'avancement.

    python -I state.py status                 # resume + ecrit STATE.json
    python -I state.py next 4                 # reserve 4 articles (reprend d'abord les 'in_progress')
    python -I state.py reject PMC123 "raison" # ecarte un article (hors sujet, protocole absent...)
    python -I state.py review PMC123 full 2 85   # relecture integrale : 2 valeurs corrigees sur 85
    python -I state.py review PMC123 doubts      # seuls les doutes ont ete relus
    python -I state.py doubt 17 "resolution"  # clot un doute
    python -I state.py doubts PMC123          # liste les doutes de l'article
    python -I state.py doubts PMC123 "resolution"   # clot tous ses doutes ouverts d'un coup
    python -I state.py finding 12 corrige "note"   # statut d'une anomalie d'audit (corrige|accepte)
    python -I state.py critic PMC123 done "bilan"   # seconde lecture critique traitee (ou: pending)
    python -I state.py critiques PMC123             # liste les constats du critique de fidelite
    python -I state.py critiques PMC123 12 corrige "note"   # statut d'un constat (corrige|accepte|rejete)
    python -I state.py critiques PMC123 all accepte "note"  # tous les constats encore ouverts
    python -I state.py lock | touch | unlock   # touch : prolonge le verrou pendant une longue execution
"""
import hashlib
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402

LOCK = db.ROOT / "run.lock"
LOCK_STALE_S = 75 * 60
TARGET_PAPERS = 500   # cible fixee par l'utilisateur : 500 publications extraites (et non 500 voies)
CALIBRATION = 10      # les N premieres publications sont relues integralement
SAMPLE_MOD = 5        # ensuite 1 publication sur 5


def needs_full_review(pmcid, seq):
    """Tirage stable d'une execution a l'autre (depend seulement du PMCID)."""
    if seq is not None and seq <= CALIBRATION:
        return True
    return int(hashlib.sha1(pmcid.encode()).hexdigest(), 16) % SAMPLE_MOD == 0


def status(con):
    one = lambda sql: con.execute(sql).fetchone()[0]
    by_status = dict(con.execute("SELECT status, COUNT(*) FROM papers GROUP BY status").fetchall())
    extracted = by_status.get("extracted", 0)
    palier = extracted // db.PALIER_SIZE + 1
    # palier valide = rapport d'audit + relecture manuelle consignee + plus aucun bloquant ouvert
    blocked = {r[0] for r in con.execute(
        "SELECT DISTINCT palier FROM audit_findings WHERE status='ouvert' AND severity='bloquant'")}
    audited = [n for n in (int(p.stem.split("_")[1]) for p in db.AUDIT_DIR.glob("palier_*_relecture.md"))
               if n not in blocked and (db.AUDIT_DIR / f"palier_{n:03d}.md").exists()]
    pending = [r[0] for r in con.execute(
        "SELECT pmcid FROM papers WHERE status='extracted' AND review_level='none' ORDER BY seq")]
    full_due = [r["pmcid"] for r in con.execute(
        "SELECT pmcid, seq FROM papers WHERE status='extracted' AND review_level != 'full' ORDER BY seq")
        if needs_full_review(r["pmcid"], r["seq"])]
    sample = con.execute(
        "SELECT COALESCE(SUM(review_errors),0), COALESCE(SUM(review_values),0) FROM papers"
        " WHERE review_level='full' AND seq > ?", (CALIBRATION,)).fetchone()
    routes = one("SELECT COUNT(*) FROM synthesis_routes")
    st = {
        "updated": db.now(),
        "target_papers": TARGET_PAPERS,
        "routes_total": routes,
        "routes_base": one("SELECT COUNT(*) FROM synthesis_routes WHERE parent_route_id IS NULL"),
        "routes_branches": one("SELECT COUNT(*) FROM synthesis_routes WHERE parent_route_id IS NOT NULL"),
        "parameters": one("SELECT COUNT(*) FROM parameters"),
        "papers": by_status,
        "papers_extracted": extracted,
        "current_palier": palier,
        "paliers_complets": extracted // db.PALIER_SIZE,
        "paliers_audites": sorted(audited),
        "audit_du": [p for p in range(1, extracted // db.PALIER_SIZE + 1) if p not in audited],
        "open_doubts": one("SELECT COUNT(*) FROM doubts WHERE status='open'"),
        "open_blocking_findings": one(
            "SELECT COUNT(*) FROM audit_findings WHERE status='ouvert' AND severity='bloquant'"),
        "review_pending": pending,
        "critic_pending": [r[0] for r in con.execute(
            "SELECT pmcid FROM papers WHERE status='extracted' AND critic_status='none' ORDER BY seq")],
        "format1_to_upgrade": [r[0] for r in con.execute(
            "SELECT pmcid FROM papers WHERE status='extracted' AND format_version < 2 ORDER BY seq")],
        "full_review_due": full_due,
        "sample_error_rate": round(sample[0] / sample[1], 4) if sample[1] else None,
        "queue_by_family": dict(con.execute(
            "SELECT family_query, COUNT(*) FROM papers WHERE status='queued' GROUP BY 1").fetchall()),
        "done": extracted >= TARGET_PAPERS and extracted % db.PALIER_SIZE == 0
                and not [p for p in range(1, extracted // db.PALIER_SIZE + 1) if p not in audited],
    }
    (db.ROOT / "STATE.json").write_text(json.dumps(st, indent=2, ensure_ascii=False), encoding="utf-8")
    return st


def next_papers(con, n):
    rows = [r["pmcid"] for r in con.execute(
        "SELECT pmcid FROM papers WHERE status='in_progress' ORDER BY id LIMIT ?", (n,))]
    while len(rows) < n:
        # famille la moins representee parmi les articles deja pris, puis l'article le plus
        # « parametrique » (plus de branches par publication)
        r = con.execute(
            "SELECT q.pmcid FROM papers q WHERE q.status='queued' ORDER BY"
            " (SELECT COUNT(*) FROM papers d WHERE d.family_query = q.family_query"
            "  AND d.status IN ('extracted','in_progress')), q.param_score DESC, q.id LIMIT 1").fetchone()
        if r is None:
            break
        con.execute("UPDATE papers SET status='in_progress' WHERE pmcid=?", (r["pmcid"],))
        rows.append(r["pmcid"])
    con.commit()
    return rows


def main():
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    con = db.connect()
    cmd = a[0]
    if cmd == "status":
        print(json.dumps(status(con), indent=2, ensure_ascii=False))
    elif cmd == "next":
        for pmcid in next_papers(con, int(a[1]) if len(a) > 1 else 1):
            r = con.execute("SELECT * FROM papers WHERE pmcid=?", (pmcid,)).fetchone()
            print(f"{pmcid}\t{r['family_query']}\t{r['text_chars']}\t{r['title']}")
    elif cmd == "reject":
        con.execute("UPDATE papers SET status='rejected', reject_reason=? WHERE pmcid=?", (a[2], a[1]))
        con.execute("DELETE FROM synthesis_routes WHERE paper_id=(SELECT id FROM papers WHERE pmcid=?)", (a[1],))
        con.commit()
    elif cmd == "review":
        errs, vals = (int(a[3]), int(a[4])) if a[2] == "full" else (None, None)
        con.execute("UPDATE papers SET review_level=?, review_errors=?, review_values=? WHERE pmcid=?",
                    (a[2], errs, vals, a[1]))
        con.commit()
    elif cmd == "doubt":
        con.execute("UPDATE doubts SET status='resolved', resolution=? WHERE id=?", (a[2], int(a[1])))
        con.commit()
    elif cmd == "doubts":
        pid = con.execute("SELECT id FROM papers WHERE pmcid=?", (a[1],)).fetchone()["id"]
        if len(a) > 2:
            con.execute("UPDATE doubts SET status='resolved', resolution=? WHERE paper_id=? AND status='open'",
                        (a[2], pid))
            con.commit()
        for d in con.execute("SELECT * FROM doubts WHERE paper_id=?", (pid,)):
            print(f"{d['id']}\t{d['status']}\t{d['location']}\t{d['issue']}")
    elif cmd == "critic":
        # critic PMC123 done "<bilan>"  |  critic PMC123 pending
        con.execute("UPDATE papers SET critic_status=? WHERE pmcid=?", (a[2], a[1]))
        if len(a) > 3:
            con.execute("INSERT INTO doubts (paper_id, location, issue, resolution, status) VALUES "
                        "((SELECT id FROM papers WHERE pmcid=?), 'critique', ?, ?, 'resolved')",
                        (a[1], "Seconde lecture critique", a[3]))
        con.commit()
    elif cmd == "critiques":
        # critiques PMC123                      -> liste les constats de fidelite
        # critiques PMC123 <id|all> <corrige|accepte|rejete> "resolution"
        pid = con.execute("SELECT id FROM papers WHERE pmcid=?", (a[1],)).fetchone()["id"]
        if len(a) > 4:
            where = "" if a[2] == "all" else " AND id=%d" % int(a[2])
            con.execute("UPDATE critiques SET status=?, resolution=? WHERE paper_id=? AND kind='fidelite'"
                        " AND status='ouvert'" + where if a[2] == "all" else
                        "UPDATE critiques SET status=?, resolution=? WHERE paper_id=? AND kind='fidelite'" + where,
                        (a[3], a[4], pid))
            con.commit()
        for r in con.execute("SELECT * FROM critiques WHERE paper_id=? AND kind='fidelite' ORDER BY id", (pid,)):
            print(f"{r['id']}\t{r['status']}\t{r['severity']}\t{r['confidence']}\t{r['location']}\n"
                  f"\textrait : {r['extracted']}\n\tarticle : {r['article_says']}\n\tcorrection proposee : {r['fix']}")
    elif cmd == "finding":
        con.execute("UPDATE audit_findings SET status=?, note=? WHERE id=?",
                    (a[2], a[3] if len(a) > 3 else None, int(a[1])))
        con.commit()
    elif cmd == "lock":
        if LOCK.exists() and time.time() - LOCK.stat().st_mtime < LOCK_STALE_S:
            print("OCCUPE: une autre execution est en cours")
            raise SystemExit(2)
        LOCK.write_text(db.now(), encoding="utf-8")
        print("verrou pris")
    elif cmd == "touch":
        LOCK.write_text(db.now(), encoding="utf-8")
    elif cmd == "unlock":
        LOCK.unlink(missing_ok=True)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
