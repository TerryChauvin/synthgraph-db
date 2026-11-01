"""Complete le texte de chaque article avec ce que la conversion de base laisse de cote.

    python -I enrich.py                 # tous les articles ayant un texte (idempotent)
    python -I enrich.py PMC1234567      # un seul article
    python -I enrich.py figs PMC1234567 # telecharge les figures dans corpus/fig/<PMCID>/

Ajoute A LA FIN de corpus/text/<PMCID>.txt (les positions des citations deja enregistrees
ne bougent donc pas) :
  ## Figure captions             legendes des figures
  ## Table footnotes             notes de bas de tableau
  ## Supporting Information — <fichier>    texte des annexes (PDF, DOCX, TXT) du depot PMC Open Access
et ecrit corpus/refs/<PMCID>.txt : le texte avec les renvois bibliographiques marques [[id]]
suivi de la liste des references, pour retrouver les publications sources d'une methode.

Les fichiers telecharges sont des donnees non fiables : ils sont lus, jamais executes.
"""
import io
import json
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402
import sections  # noqa: E402
from fetch import S3, get  # noqa: E402

SI_DIR = db.ROOT / "corpus" / "si"
REF_DIR = db.ROOT / "corpus" / "refs"
FIG_DIR = db.ROOT / "corpus" / "fig"
SI_EXT = (".pdf", ".docx", ".txt", ".csv")
SI_MAX_BYTES = 40 * 1024 * 1024
MARK_CAPTIONS, MARK_FOOT, MARK_SI = "## Figure captions", "## Table footnotes", "## Supporting Information — "


def parse(pmcid):
    data = (db.XML_DIR / f"{pmcid}.xml").read_bytes()
    if b"<!ENTITY" in data:
        return None
    root = ET.fromstring(data)
    for e in root.iter():
        e.tag = sections.local(e.tag)
    return root


def flat_all(el):
    """Texte complet d'un element (y compris ce que sections.flat ignore)."""
    return db.norm("".join(el.itertext()))


def captions_and_footnotes(root):
    caps, foots = [], []
    for fig in root.iter("fig"):
        label, cap = fig.find("label"), fig.find("caption")
        line = " ".join(x for x in (flat_all(label) if label is not None else "",
                                    flat_all(cap) if cap is not None else "") if x)
        if line and line not in caps:
            caps.append(line)
    for tw in root.iter("table-wrap"):
        label = tw.find("label")
        for foot in tw.iter("table-wrap-foot"):
            txt = flat_all(foot)
            if txt:
                line = f"{flat_all(label) if label is not None else 'Table'} — {txt}"
                if line not in foots:
                    foots.append(line)
    return caps, foots


def s3_keys(pmcid):
    keys, token = [], None
    while True:
        params = {"list-type": 2, "prefix": f"{pmcid}."}
        if token:
            params["continuation-token"] = token
        listing = get(f"{S3}/?{urllib.parse.urlencode(params)}", tries=3).decode("utf-8")
        keys += re.findall(r"<Key>([^<]+)</Key>.*?<Size>(\d+)</Size>", listing, re.S)
        m = re.search(r"<NextContinuationToken>([^<]+)</NextContinuationToken>", listing)
        if not m:
            break
        token = m.group(1)
    if not keys:
        return []
    version = max(k.split("/")[0] for k, _ in keys)
    return [(k, int(size)) for k, size in keys if k.startswith(version + "/")]


def text_of(name, data):
    """Texte d'une annexe ; None si le format n'est pas lisible."""
    low = name.lower()
    try:
        if low.endswith(".pdf"):
            import pymupdf as fitz  # PyMuPDF
            with fitz.open(stream=data, filetype="pdf") as doc:
                return "\n".join(page.get_text() for page in doc)
        if low.endswith(".docx"):
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                xml = z.read("word/document.xml").decode("utf-8", "replace")
            xml = re.sub(r"</w:p>|</w:tr>", "\n", xml)
            xml = re.sub(r"</w:tc>", " | ", xml)
            return re.sub(r"<[^>]+>", "", xml).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        if low.endswith((".txt", ".csv")):
            return data.decode("utf-8", "replace")
    except Exception as e:  # annexe illisible : on la signale, on ne bloque pas
        print(f"  annexe illisible {name}: {type(e).__name__}")
    return None


def supplementary(pmcid, keys):
    """[(nom, lignes)] pour chaque annexe textuelle du depot."""
    main = {f"{pmcid}.{ext}" for ext in ("pdf", "txt", "xml", "json")}
    out = []
    for key, size in keys:
        name = key.split("/", 1)[1]
        if re.sub(r"\.\d+\.", ".", name) in main or re.match(rf"{pmcid}\.\d+\.(pdf|txt|xml|json)$", name):
            continue
        if not name.lower().endswith(SI_EXT) or size > SI_MAX_BYTES:
            continue
        local = SI_DIR / pmcid / Path(name).name
        if local.exists():
            data = local.read_bytes()
        else:
            time.sleep(0.2)
            data = get(f"{S3}/{urllib.parse.quote(key)}", tries=3)
            local.parent.mkdir(parents=True, exist_ok=True)
            local.write_bytes(data)
        txt = text_of(name, data)
        if txt:
            lines = [db.norm(l) for l in txt.splitlines()]
            lines = [l for l in lines if l and not l.startswith(("## ", "# "))]
            if lines:
                out.append((Path(name).name, lines))
    return out


def references(pmcid, root):
    """Texte avec renvois [[id]] + liste des references -> corpus/refs/<PMCID>.txt et .json."""
    sections.MARK_REFS = True
    try:
        lines = []
        body = root.find("body")
        if body is not None:
            sections.walk_body(body, lines)
    finally:
        sections.MARK_REFS = False
    refs = {}
    for ref in root.iter("ref"):
        rid = ref.get("id")
        if not rid:
            continue
        cit = next((c for c in ref if sections.local(c.tag) in ("element-citation", "mixed-citation", "citation")), ref)
        ids = {p.get("pub-id-type"): flat_all(p) for p in cit.iter("pub-id")}
        names = [flat_all(n) for n in cit.iter("name")][:6]
        year = cit.find(".//year")
        title, source = cit.find(".//article-title"), cit.find(".//source")
        refs[rid] = {"authors": "; ".join(names), "title": flat_all(title) if title is not None else None,
                     "journal": flat_all(source) if source is not None else None,
                     "year": flat_all(year) if year is not None else None,
                     "doi": ids.get("doi"), "pmid": ids.get("pmid"), "pmcid": ids.get("pmcid") or ids.get("pmc"),
                     "raw": db.norm(" ".join(t.strip() for t in cit.itertext() if t.strip()))[:400]}
    REF_DIR.mkdir(parents=True, exist_ok=True)
    listing = [f"[[{rid}]] {r['raw']}" + (f" doi:{r['doi']}" if r["doi"] else "") for rid, r in refs.items()]
    (REF_DIR / f"{pmcid}.txt").write_text(
        "\n".join([db.norm(l) for l in lines if db.norm(l)] + ["## References"] + listing), encoding="utf-8")
    (REF_DIR / f"{pmcid}.json").write_text(json.dumps(refs, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(refs)


def enrich(con, pmcid, with_si=True):
    path = db.TEXT_DIR / f"{pmcid}.txt"
    root = parse(pmcid)
    if root is None or not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    add = []
    caps, foots = captions_and_footnotes(root)
    if caps and MARK_CAPTIONS not in text:
        add += [MARK_CAPTIONS] + caps
    if foots and MARK_FOOT not in text:
        add += [MARK_FOOT] + foots
    n_si = text.count(MARK_SI)
    status = None
    if with_si and MARK_SI not in text:
        try:
            files = supplementary(pmcid, s3_keys(pmcid))
            for name, lines in files:
                add += [f"{MARK_SI}{name}"] + lines
            n_si, status = len(files), ("ok" if files else "absent")
        except RuntimeError as e:
            status = "erreur_reseau"
            print(f"  {pmcid}: annexes non recuperees ({e})")
    if add:
        path.write_text(text.rstrip("\n") + "\n" + "\n".join(db.norm(l) for l in add if db.norm(l)), encoding="utf-8")
    n_refs = references(pmcid, root)
    if status:
        con.execute("UPDATE papers SET si_status=?, si_files=?, text_chars=? WHERE pmcid=?",
                    (status, n_si, len(path.read_text(encoding="utf-8")), pmcid))
        con.commit()
    return len(caps), len(foots), n_si, n_refs


def figures(pmcid):
    out = FIG_DIR / pmcid
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for key, size in s3_keys(pmcid):
        if key.lower().endswith((".jpg", ".jpeg", ".png", ".gif")) and size < 15 * 1024 * 1024:
            target = out / Path(key).name
            if not target.exists():
                target.write_bytes(get(f"{S3}/{urllib.parse.quote(key)}", tries=3))
            n += 1
    print(f"{pmcid}: {n} figures dans {out}")


def main():
    args = sys.argv[1:]
    if args[:1] == ["figs"]:
        return [figures(p) for p in args[1:]]
    if args[:1] == ["refs"]:
        # regenere seulement corpus/refs/ (hors ligne) pour tous les articles ayant un texte
        n = bad = 0
        for xml in sorted(db.XML_DIR.glob("*.xml")):
            pmcid = xml.stem
            if (db.TEXT_DIR / f"{pmcid}.txt").exists():
                root = parse(pmcid)
                if root is not None:
                    references(pmcid, root)
                    n += 1
                    body = (REF_DIR / f"{pmcid}.txt").read_text(encoding="utf-8").split("## References")[0]
                    bad += "[[" not in body
        print(f"references regenerees: {n} ; sans aucun renvoi marque dans le corps: {bad}")
        return
    con = db.connect()
    cols = [r[1] for r in con.execute("PRAGMA table_info(papers)")]
    if "si_status" not in cols:
        con.execute("ALTER TABLE papers ADD COLUMN si_status TEXT")   # ok | absent | erreur_reseau
        con.execute("ALTER TABLE papers ADD COLUMN si_files INTEGER")
    todo = args or [r["pmcid"] for r in con.execute(
        "SELECT pmcid FROM papers WHERE status IN ('queued','in_progress','extracted') ORDER BY (status='extracted') DESC, id")]
    tot = [0, 0, 0]
    for i, pmcid in enumerate(todo):
        try:
            r = enrich(con, pmcid)
        except ET.ParseError:
            r = None
        if r:
            tot = [tot[0] + (r[0] > 0), tot[1] + (r[1] > 0), tot[2] + (r[2] > 0)]
        if len(todo) < 5 or (i + 1) % 25 == 0:
            print(f"{i + 1}/{len(todo)} {pmcid}: {r}", flush=True)
    print(f"termine: {len(todo)} articles, legendes {tot[0]}, notes de tableau {tot[1]}, annexes {tot[2]}", flush=True)


if __name__ == "__main__":
    main()
