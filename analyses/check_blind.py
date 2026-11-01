#!/usr/bin/env python3
"""Contrôle d'une ré-extraction à l'aveugle : python3 -I analyses/check_blind.py <PMCID>  (lit audits/verification/aveugle/<PMCID>.json, mêmes contrôles que load.py check, sans chargement)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]
os.chdir(ROOT)  # chemins relatifs à la racine du dépôt
import json, sys, pathlib, os
import load
pmcid = sys.argv[1]
path = pathlib.Path("audits/verification/aveugle") / f"{pmcid}.json"
data = json.loads(path.read_text(encoding="utf-8"))
c, order = load.validate(pmcid, data)
for w in c.warnings: print("AVERTISSEMENT", w)
for e in c.errors: print("ERREUR", e)
print(f"{pmcid}: {len(order)} voies ({sum(1 for r in order if r.get('parent'))} branches), {c.n_quotes} citations verifiees, {len(c.errors)} erreurs, {len(c.warnings)} avertissements, {len(data.get('doubts') or [])} doutes")
sys.exit(1 if c.errors else 0)
