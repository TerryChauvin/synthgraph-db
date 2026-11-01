"""Différence entre l'extraction en dépôt (git HEAD) et l'extraction de travail, pour la passe de complément.

    python3 -I analyses/delta_complement.py PMC1234567           # Markdown : ajouts, par catégorie, avec citation
    python3 -I analyses/delta_complement.py PMC1234567 --json    # comptes seulement

Vérifie aussi qu'aucun élément existant n'a été modifié ni retiré (règle de la passe : ajouter seulement) ;
toute modification est listée sous « MODIFIÉ / RETIRÉ » et compte comme une anomalie.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
os.chdir(ROOT)


def key_param(p):
    return (p.get("name"), p.get("value_num"), p.get("value_text"), p.get("unit"))


def items(d):
    """Dictionnaire catégorie → {clé: description} de tous les éléments d'une extraction."""
    I = {k: {} for k in ("parametres", "not_stated", "equipements", "caracterisations", "conditions_mesure", "resultats", "reactifs", "etapes", "voies")}
    for r in d.get("routes") or []:
        L = r.get("label")
        I["voies"][L] = dict(material=r.get("material"), method=r.get("method"), parent=r.get("parent"))
        for n in r.get("not_stated") or []:
            I["not_stated"][(L, "voie", n)] = n
        for g in r.get("reagents") or []:
            k = (L, g.get("name"), g.get("amount"), g.get("unit"), g.get("role"))
            I["reactifs"][k] = f"{g.get('name')} {g.get('amount') or ''} {g.get('unit') or ''} ({g.get('role')})"
            for n in g.get("not_stated") or []:
                I["not_stated"][(L, f"réactif {g.get('name')}", n)] = n
        for s in r.get("steps") or []:
            o = s.get("order")
            I["etapes"][(L, o)] = f"{s.get('action')} — {(s.get('description') or '')[:80]}"
            for p in s.get("parameters") or []:
                I["parametres"][(L, o) + key_param(p)] = f"étape {o} ({s.get('action')}) · {p.get('name')} = {p.get('value_num') if p.get('value_num') is not None else p.get('value_text')} {p.get('unit') or ''} — « {p.get('quote', '')[:140]} »"
            for e in s.get("equipment") or []:
                I["equipements"][(L, o, e.get("type"), e.get("detail"))] = f"étape {o} · {e.get('type')} {e.get('detail') or ''} — « {e.get('quote', '')[:100]} »"
            for n in s.get("not_stated") or []:
                I["not_stated"][(L, f"étape {o}", n)] = n
        for c in r.get("characterizations") or []:
            I["caracterisations"][(L, c.get("technique"), c.get("result"))] = f"{c.get('technique')} : {(c.get('result') or '')[:80]}"
            if c.get("conditions") or c.get("instrument"):
                I["conditions_mesure"][(L, c.get("technique"), c.get("instrument"), c.get("conditions"))] = f"{c.get('technique')} · {c.get('instrument') or ''} · {c.get('conditions') or ''} — « {c.get('quote', '')[:100]} »"
        for o in r.get("outcomes") or []:
            I["resultats"][(L, o.get("property"), o.get("value_num"), o.get("value_text"), o.get("unit"))] = f"{o.get('property')} = {o.get('value_num') if o.get('value_num') is not None else (o.get('value_text') or '')[:60]} {o.get('unit') or ''} — « {o.get('quote', '')[:120]} »"
    return I


def main():
    pmcid = sys.argv[1]
    path = f"extractions/{pmcid}.json"
    # --base <commit> : comparer à cette version au lieu de HEAD ; --auto : avant-dernier commit touchant le fichier
    ref = "HEAD"
    if "--base" in sys.argv:
        ref = sys.argv[sys.argv.index("--base") + 1]
    elif "--auto" in sys.argv:
        ref = subprocess.run(["git", "log", "--format=%H", "-n", "2", "--", path], capture_output=True, text=True).stdout.split()[1]
    old = json.loads(subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True, check=True).stdout)
    new = json.load(open(path, encoding="utf-8"))
    A, B = items(old), items(new)
    added = {k: {x: v for x, v in B[k].items() if x not in A[k]} for k in A}
    removed = {k: {x: v for x, v in A[k].items() if x not in B[k]} for k in A}
    counts = {k: len(v) for k, v in added.items()}
    counts["retires_ou_modifies"] = sum(len(v) for v in removed.values())
    counts["doutes_ajoutes"] = max(0, len(new.get("doubts") or []) - len(old.get("doubts") or []))
    counts["annotations_ajoutees"] = max(0, len(new.get("annotations") or []) - len(old.get("annotations") or []))
    if "--json" in sys.argv:
        print(json.dumps(counts, ensure_ascii=False))
        return
    print(f"# Complément — {pmcid}\n")
    print("| " + " | ".join(counts) + " |\n|" + "---|" * len(counts) + "\n| " + " | ".join(map(str, counts.values())) + " |\n")
    for k, v in added.items():
        if v:
            print(f"## {k} ajoutés ({len(v)})\n")
            for x, desc in v.items():
                print(f"- [{x[0]}] {desc}")
            print()
    rem = [(k, x, v) for k, d in removed.items() for x, v in d.items()]
    if rem:
        print(f"## MODIFIÉ / RETIRÉ ({len(rem)}) — anomalie\n")
        for k, x, v in rem:
            print(f"- {k} [{x[0]}] {v}")


if __name__ == "__main__":
    main()
