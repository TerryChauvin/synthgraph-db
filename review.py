"""Vue compacte d'une extraction pour la relecture : une ligne par valeur, avec sa citation.

    python -I review.py PMC1234567            # tout
    python -I review.py PMC1234567 doubts     # seulement le decoupage en voies et les doutes
    python -I review.py PMC1234567 science    # tout, sans les citations (critique scientifique : moitie moins de texte)
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402


def val(o, num="value_num", text="value_text"):
    v = o.get(num) if o.get(num) is not None else o.get(text)
    return f"{v} {o.get('unit') or ''}".strip()


def main():
    pmcid = sys.argv[1]
    brief = len(sys.argv) > 2 and sys.argv[2] == "doubts"
    # mode science : les citations sont retirees des lignes affichees (le critique scientifique n'en a pas besoin)
    out = (lambda s: print(re.sub(r"( \+)? « .*? »", "", s))) if sys.argv[2:3] == ["science"] else print
    d = json.loads((db.EXTRACT_DIR / f"{pmcid}.json").read_text(encoding="utf-8"))
    n = 0
    for r in d["routes"]:
        m = r.get("material") or {}
        out(f"\n=== {r['label']}  parent={r.get('parent')}  [{r.get('method')}]  "
              f"{m.get('name')} / {m.get('formula')} / {m.get('family')} / {m.get('phase')} / {m.get('morphology')}"
              f"  succeeded={r.get('succeeded')}")
        out(f"    « {r.get('quote')} »")
        for v in r.get("variations") or []:
            n += 1
            out(f"  VAR {v['parameter']} (etape {v.get('step_order')}) = {val(v)}  [parent: {v.get('parent_value')}]  « {v['quote']} »")
        if brief:
            out(f"  ({len(r.get('reagents') or [])} reactifs, {len(r.get('steps') or [])} etapes, "
                  f"{len(r.get('outcomes') or [])} resultats)")
            continue
        for g in r.get("reagents") or []:
            n += 1
            extra = " ".join(str(x) for x in (g.get("purity"), g.get("supplier")) if x)
            out(f"  REACTIF {g['name']} [{g.get('formula')}] {g.get('role')}: "
                  f"{val(g, 'amount', 'amount_text')} {extra} « {g['quote']} »"
                  + (f" + « {g['supplier_quote']} »" if g.get("supplier_quote") else ""))
        for s in r.get("steps") or []:
            out(f"  {s['order']}. {s['action']}: {s.get('description')} « {s['quote']} »")
            for p in s.get("parameters") or []:
                n += 1
                q = "" if p["quote"] in s["quote"] else f" « {p['quote']} »"
                out(f"       {p['name']} = {val(p)}{q}")
            for e in s.get("equipment") or []:
                q = "" if e["quote"] in s["quote"] else f" « {e['quote']} »"
                out(f"       [materiel] {e['type']} {e.get('detail') or ''}{q}")
        if r.get("yield"):
            out(f"  RENDEMENT {r['yield'].get('value')} {r['yield'].get('unit')} « {r['yield'].get('quote')} »")
        for c in r.get("characterizations") or []:
            out(f"  CARAC {c['technique']}: {c.get('result')} « {c['quote']} »")
        for o in r.get("outcomes") or []:
            n += 1
            out(f"  RESULTAT {o['property']} = {val(o)} « {o['quote']} »")
        out(f"  MANQUE {r.get('missing_fields')}")
    if not brief:
        print()
        for a in d.get("annotations") or []:
            out(f"ANNOT {a['type']} ({a.get('route')}): {a['text']}")
    print()
    for x in d.get("doubts") or []:
        out(f"DOUTE [{x.get('where')}] {x['issue']}")
    out(f"\n{n} valeurs")


if __name__ == "__main__":
    main()
