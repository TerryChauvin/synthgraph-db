"""Recherche et telechargement d'articles open access sur Europe PMC.

    python -I fetch.py --per-family 12        # ajoute jusqu'a 12 nouveaux articles par famille
    python -I fetch.py --family MOF --per-family 30
    python -I fetch.py --pdfs                 # PDF des articles retenus (apres sections.py)
"""
import argparse
import http.client
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402

API = "https://www.ebi.ac.uk/europepmc/webservices/rest"
# le second groupe impose un vrai protocole de laboratoire dans le texte integral
FILTER = (' AND ("was dissolved" OR "were dissolved" OR autoclave OR calcined OR "tube furnace"'
          ' OR "was stirred" OR annealed)'
          " AND OPEN_ACCESS:y AND IN_EPMC:y AND HAS_FT:y NOT PUB_TYPE:review")
S3 = "https://pmc-oa-opendata.s3.amazonaws.com"
UA = {"User-Agent": "synthese-materiaux/1.0 (base de donnees de recherche; usage personnel)"}
DELAY = 0.4


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            err = e
        except (urllib.error.URLError, TimeoutError, ConnectionError, http.client.HTTPException,
                ssl.SSLError) as e:
            err = e    # HTTPException : telechargement tronque ; SSLError : erreur TLS passagere
        time.sleep(2 ** i)
    raise RuntimeError(f"echec apres {tries} essais: {url} ({err})")


def fetch_pdf(con, pmcid):
    """Telecharge le PDF de l'article ; un echec n'est pas bloquant (le XML fait foi)."""
    # depot officiel PMC Open Access sur S3 : un prefixe '<PMCID>.<version>/' par article
    try:
        keys, token = [], None
        while True:
            params = {"list-type": 2, "prefix": f"{pmcid}."}
            if token:
                params["continuation-token"] = token
            listing = get(f"{S3}/?{urllib.parse.urlencode(params)}", tries=2).decode("utf-8")
            keys += re.findall(r"<Key>([^<]+\.pdf)</Key>", listing, re.I)
            m = re.search(r"<NextContinuationToken>([^<]+)</NextContinuationToken>", listing)
            if not m:
                break
            token = m.group(1)
        # l'article lui-meme, pas les annexes : derniere version, nom le plus court
        main = [k for k in keys if not re.search(r"supp|moesm|esm|_si_|appendix", k, re.I)] or keys
        if not main:
            return False
        version = max(k.split("/")[0] for k in main)
        key = min((k for k in main if k.startswith(version + "/")), key=len)
        data = get(f"{S3}/{urllib.parse.quote(key)}", tries=2)
    except RuntimeError:
        return False
    if not data or not data.startswith(b"%PDF"):
        return False
    (db.PDF_DIR / f"{pmcid}.pdf").write_bytes(data)
    con.execute("UPDATE papers SET pdf_path=? WHERE pmcid=?", (f"corpus/pdf/{pmcid}.pdf", pmcid))
    con.commit()
    return True


def backfill_pdfs(con):
    rows = con.execute("SELECT pmcid FROM papers WHERE pdf_path IS NULL AND status != 'rejected'").fetchall()
    ok = 0
    for r in rows:
        time.sleep(DELAY)
        ok += fetch_pdf(con, r["pmcid"])
    print(f"pdf telecharges: {ok}/{len(rows)}")


def read_queries(only=None):
    out = []
    for line in (db.ROOT / "queries.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        family, query = line.split("\t", 1)
        if only is None or family == only:
            out.append((family, query))
    return out


def search(query, cursor):
    params = {"query": query + FILTER, "format": "json", "pageSize": 100,
              "resultType": "core", "cursorMark": cursor, "sort": "CITED desc"}
    data = json.loads(get(f"{API}/search?{urllib.parse.urlencode(params)}"))
    return data.get("resultList", {}).get("result", []), data.get("nextCursorMark")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-family", type=int, default=12)
    ap.add_argument("--family")
    ap.add_argument("--pdfs", action="store_true",
                    help="telecharge seulement les PDF manquants des articles deja retenus")
    args = ap.parse_args()

    con = db.connect()
    if args.pdfs:
        return backfill_pdfs(con)
    known = {r["pmcid"] for r in con.execute("SELECT pmcid FROM papers")}
    total = 0
    for family, query in read_queries(args.family):
        added, cursor, pages = 0, "*", 0
        while added < args.per_family and cursor and pages < 15:
            results, nxt = search(query, cursor)
            pages += 1
            if not results:
                break
            for r in results:
                pmcid, lic = r.get("pmcid"), (r.get("license") or "").lower()
                if not pmcid or pmcid in known or not lic.startswith("cc"):
                    continue
                known.add(pmcid)
                time.sleep(DELAY)
                try:
                    xml = get(f"{API}/{pmcid}/fullTextXML", tries=2)
                except RuntimeError:
                    continue    # erreur serveur sur cet article : on passe au suivant
                if not xml or b"<body" not in xml:
                    continue
                (db.XML_DIR / f"{pmcid}.xml").write_bytes(xml)
                journal = (r.get("journalInfo") or {}).get("journal", {}).get("title")
                con.execute(
                    "INSERT INTO papers (pmcid, doi, title, authors, journal, year, license, url,"
                    " family_query, status, fetched_at) VALUES (?,?,?,?,?,?,?,?,?, 'fetched', ?)",
                    (pmcid, r.get("doi"), db.strip_tags(r.get("title")), r.get("authorString"), journal,
                     int(r["pubYear"]) if r.get("pubYear") else None, lic,
                     f"https://europepmc.org/article/PMC/{pmcid}", family, db.now()))
                con.commit()
                added += 1
                if added >= args.per_family:
                    break
            cursor = nxt if nxt != cursor else None
            time.sleep(DELAY)
        print(f"{family}: +{added}")
        total += added
    print(f"total telecharge: {total}")


if __name__ == "__main__":
    main()
