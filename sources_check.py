"""Verifie contre Crossref les DOI cites par le critique scientifique (titre et annee).

    python -I sources_check.py PMC1234567        # toutes les sources de l'article
    python -I sources_check.py PMC1234567 5      # les 5 premieres
    python -I sources_check.py --palier 2 10     # 10 sources tirees au hasard dans le palier

Une source dont le DOI n'existe pas, ou dont le titre Crossref ne correspond pas a celui donne
par le critique, est une anomalie bloquante : la critique scientifique de l'article est a refaire.
"""
import json
import random
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402

import os  # noqa: E402
# Crossref « polite pool » : adresse de contact lue dans CROSSREF_MAILTO (jamais écrite dans le dépôt)
UA = {"User-Agent": "synthese-materiaux/1.0" + (f" (mailto:{os.environ['CROSSREF_MAILTO']})" if os.environ.get("CROSSREF_MAILTO") else "")}


def sources(con, where, args):
    seen = {}
    for pmcid, checks, srcs in con.execute(
            "SELECT p.pmcid, pl.checks_json, pl.sources_json FROM plausibility pl JOIN papers p ON p.id=pl.paper_id "
            + where, args):
        for ch in json.loads(checks or "[]"):
            s = ch.get("source")
            if s and s.get("url_or_doi"):
                seen[(pmcid, s["url_or_doi"])] = s
        for s in json.loads(srcs or "[]"):
            if s.get("url_or_doi"):
                seen[(pmcid, s["url_or_doi"])] = s
    return seen


def simplify(title):
    """Titre comparable : sans balises, tirets et espaces typographiques, en minuscules."""
    t = re.sub(r"<[^>]+>", "", title or "")
    t = t.replace("–", "-").replace("—", "-").replace("‐", "-").replace("’", "'")
    # sans espaces : « CsPbX <sub>3</sub> » et « CsPbX3 » doivent se valoir
    # sans parentheses : Crossref ecrit parfois « nickelII » pour « nickel(II) »
    return re.sub(r"[\s()\-\"'“”‘’«»]", "", t.lower())   # ni guillemets : “Green” et "green" doivent se valoir


def check(doi):
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        m = json.load(r)["message"]
    title = " ".join((m.get("title") or [""])[0].split())
    year = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
    return title, year


def lookup(title):
    """DOI probable d'une source donnee sans DOI, par recherche de titre sur Crossref."""
    url = f"https://api.crossref.org/works?rows=1&query.title={urllib.parse.quote(title)}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        items = json.load(r)["message"]["items"]
    if not items:
        return None
    m = items[0]
    # un DOI de materiel supplementaire (.s001) renvoie a l'article lui-meme
    return re.sub(r"\.s\d{3}$", "", m.get("DOI") or "")," ".join((m.get("title") or [""])[0].split()), (m.get("issued", {}).get("date-parts") or [[None]])[0][0]


def main():
    a = sys.argv[1:]
    con = db.connect()
    if a[:1] == ["--palier"]:
        seen = sources(con, "WHERE p.palier=?", (int(a[1]),))
        n = int(a[2]) if len(a) > 2 else 10
        items = random.Random(int(a[1])).sample(list(seen.items()), min(n, len(seen)))
    else:
        seen = sources(con, "WHERE p.pmcid=?", (a[0],))
        items = list(seen.items())[:int(a[1])] if len(a) > 1 else list(seen.items())
    print(f"{len(seen)} sources distinctes, {len(items)} verifiees")
    bad = 0
    for (pmcid, key), s in items:
        doi = key.replace("https://doi.org/", "").replace("doi:", "").strip()
        if not doi.startswith("10."):
            try:
                found = lookup(re.sub(r"\(.*?\)", "", str(s.get("title") or "")))
            except Exception:
                found = None
            if found and simplify(found[1])[:40] == simplify(s.get("title"))[:40]:
                print(f"  DOI?  {pmcid} source sans DOI, titre retrouve sur Crossref : {found[0]} ({found[2]}) | {s.get('title')[:60]}")
            elif key.startswith("http"):
                # page web, fiche ou rapport : hors Crossref, a ouvrir a la main a l'audit ; pas une anomalie
                print(f"  URL   {pmcid} source web sans DOI, a ouvrir a la main : {key} | {str(s.get('title'))[:60]}")
            else:
                bad += 1
                print(f"  ECHEC {pmcid} source sans DOI ni URL et titre introuvable sur Crossref : {key} | {s.get('title')}")
            continue
        if doi.lower().startswith("10.48550/"):
            # DOI arXiv : enregistre chez DataCite, absent de Crossref (404 attendu)
            print(f"  URL   {pmcid} prepublication arXiv, a ouvrir a la main : https://arxiv.org/abs/{doi.split('arXiv.')[-1]} | {str(s.get('title'))[:60]}")
            continue
        try:
            title, year = check(doi)
        except Exception as e:  # DOI inconnu ou reseau
            try:
                # DOI d'une autre agence que Crossref (revues chinoises, DataCite) : existe-t-il sur doi.org ?
                req = urllib.request.Request(f"https://doi.org/api/handles/{urllib.parse.quote(doi)}", headers=UA)
                with urllib.request.urlopen(req, timeout=60) as r:
                    known = json.load(r).get("responseCode") == 1
            except Exception:
                known = False
            if known:
                print(f"  URL   {pmcid} DOI hors Crossref mais connu de doi.org, titre a controler a la main : {doi} | {str(s.get('title'))[:60]}")
                continue
            bad += 1
            print(f"  ECHEC {pmcid} {doi}: {e} | critique : {s.get('title')}")
            continue
        claimed, got = simplify(s.get("title")), simplify(title)
        ok = claimed[:40] in got or got[:40] in claimed
        bad += not ok
        print(f"  {'OK   ' if ok else 'TITRE'} {pmcid} {doi} | Crossref : {title[:70]} ({year}) | critique : {claimed[:60]} ({s.get('year')})")
    print(f"{bad} anomalie(s)")
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main()
