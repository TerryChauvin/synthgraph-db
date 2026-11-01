"""relabel.py PMCID ancien=nouveau ... : renomme des voies dans critiques/<PMCID>_science.json
apres un renommage decide par l'orchestrateur (les libelles d'origine du critique restent dans 'label_critique')."""
import json, sys
from pathlib import Path
p = Path(__file__).resolve().parent / "critiques" / f"{sys.argv[1]}_science.json"
m = dict(a.split("=", 1) for a in sys.argv[2:])
d = json.load(open(p, encoding="utf-8"))
for r in d["routes"]:
    print(repr(r["label"]), "->", repr(m.get(r["label"], r["label"])))
    if r["label"] in m:
        r["label_critique"], r["label"] = r["label"], m[r["label"]]
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
