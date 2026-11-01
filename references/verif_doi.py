"""Verifie sur Crossref chaque DOI de references/fondateurs.md (titre et annee).

    python -I references/verif_doi.py

Un DOI inconnu de Crossref est imprime ECHEC : retirer ou corriger la ligne avant de garder le fichier.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sources_check import check  # noqa: E402

text = (Path(__file__).with_name("fondateurs.md")).read_text(encoding="utf-8")
bad = 0
for line in text.splitlines():
    m = re.search(r"\b(10\.\d{4,9}/[^\s—]+?)(?=\s—|\s*$)", line)
    if not m:
        continue
    doi = m.group(1).rstrip(".,;)")
    year = re.search(r"\b(19|20)\d{2}\b", line.split(doi)[0])
    try:
        title, got = check(doi)
    except Exception as e:
        bad += 1
        print(f"ECHEC {doi}: {e}")
        continue
    flag = "" if not year or str(got) == year.group(0) else f"  (annee du fichier {year.group(0)})"
    print(f"OK    {doi} | {title[:80]} ({got}){flag}")
print(f"{bad} DOI en echec")
raise SystemExit(1 if bad else 0)
