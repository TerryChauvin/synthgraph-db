"""Fiche de synthese lisible : chaque etape, ses parametres, et les cases « non cite ».

    python -I fiche.py PMC1234567          # -> fiches/PMC1234567.md (toutes les voies de l'article)
    python -I fiche.py                     # toutes les publications extraites
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402

NC = "**non cité**"


def val(num, text, unit):
    v = f"{num:g}" if num is not None else (text or "")
    return f"{v} {unit or ''}".strip()


def fiche(con, paper):
    q = lambda sql, *a: con.execute(sql, a).fetchall()
    out = [f"# {paper['title']}", "",
           f"{paper['authors'] or ''} — *{paper['journal'] or ''}*, {paper['year'] or ''}. "
           f"[{paper['pmcid']}]({paper['url']})" + (f" · doi:{paper['doi']}" if paper["doi"] else ""), "",
           "Chaque valeur vient de l'article et porte sa citation. « non cité » = information cherchée et "
           "absente de l'article (ou seulement implicite) : à déterminer par le chimiste.", ""]
    routes = q("SELECT r.*, m.name AS mname, m.formula, m.phase, m.morphology FROM synthesis_routes r"
               " LEFT JOIN materials m ON m.id=r.material_id WHERE r.paper_id=? ORDER BY r.id", paper["id"])
    labels = {r["id"]: r["branch_label"] for r in routes}
    # ce qu'un chimiste doit savoir avant le protocole : limites et dangers, toutes voies confondues
    warn = q("SELECT type, text, route_id FROM annotations WHERE paper_id=? AND (type='limite_reproductibilite'"
             " OR type LIKE 'securite_%') ORDER BY type LIKE 'securite_%', id", paper["id"])
    if warn:
        out += ["## Avant de refaire", ""]
        out += [f"- **{'Sécurité' if a['type'].startswith('securite') else 'Limite'}"
                + (f" ({labels.get(a['route_id'])})" if a["route_id"] else "") + ".** " + a["text"] for a in warn]
        out.append("")
    for a in q("SELECT type, text FROM annotations WHERE paper_id=? AND route_id IS NULL AND type != "
               "'limite_reproductibilite' AND type NOT LIKE 'securite_%' ORDER BY id", paper["id"]):
        out += [f"**{a['type'].replace('_', ' ').capitalize()}.** {a['text']}", ""]
    for r in routes:
        gaps = q("SELECT * FROM not_stated WHERE route_id=?", r["id"])
        out += [f"## Voie « {r['branch_label']} »", "",
                f"- Matériau : {r['mname']}" + (f" ({r['formula']})" if r["formula"] else "")
                + (f", {r['phase']}" if r["phase"] else "") + (f", {r['morphology']}" if r["morphology"] else ""),
                f"- Méthode : {r['method'] or '—'}",
                f"- Complétude : {r['completeness_score']}"
                + ("" if r["succeeded"] is None else (" · produit visé obtenu" if r["succeeded"] else " · **échec rapporté**"))]
        if r["yield_value"] is not None:
            out.append(f"- Rendement : {r['yield_value']:g} {r['yield_unit'] or ''}")
        elif any(g["scope"] == "route" and g["name"] == "yield" for g in gaps):
            out.append(f"- Rendement : {NC}")
        variations = q("SELECT * FROM route_variations WHERE route_id=?", r["id"])
        if r["parent_route_id"]:
            out += ["", f"**Identique à la voie « {labels.get(r['parent_route_id'])} », sauf :**", ""]
            for v in variations:
                where = f" (étape {v['step_order']})" if v["step_order"] else ""
                out.append(f"- {v['parameter']}{where} : **{val(v['value_num'], v['value_text'], v['unit'])}** "
                           f"au lieu de {v['parent_value'] or '?'} — « {v['quote']} »")
        reagents = q("SELECT * FROM reagents WHERE route_id=? ORDER BY id", r["id"])
        if reagents:
            out += ["", "### Réactifs", "", "| Réactif | Formule | Rôle | Quantité | Pureté | Fournisseur |", "|---|---|---|---|---|---|"]
            for g in reagents:
                ns = {x["name"] for x in gaps if x["scope"] == "reagent" and x["reagent"] == g["name"]}
                cell = lambda v, key: (str(v) if v else (NC if key in ns else "—"))
                amount = val(g["amount"], g["amount_text"], g["unit"])
                out.append(f"| {g['name']} | {g['formula'] or '—'} | {g['role'] or '—'} | {cell(amount, 'amount')} | "
                           f"{cell(g['purity'], 'purity')} | {cell(g['supplier'], 'supplier')} |")
        steps = q("SELECT * FROM steps WHERE route_id=? ORDER BY step_order", r["id"])
        if steps:
            out += ["", "### Étapes", ""]
        for s in steps:
            out.append(f"{s['step_order']}. **{s['action']}** — {s['description'] or ''}  ")
            out.append(f"   « {s['quote']} »")
            for p in q("SELECT * FROM parameters WHERE step_id=? ORDER BY id", s["id"]):
                out.append(f"   - {p['name']} : **{val(p['value_num'], p['value_text'], p['unit'])}**"
                           + (f" (figure)" if "from_figure" in p.keys() and p["from_figure"] else ""))
            for g in gaps:
                if g["scope"] == "step" and g["step_order"] == s["step_order"]:
                    out.append(f"   - {g['name']} : {NC}")
            for e in q("SELECT * FROM equipment WHERE step_id=?", s["id"]):
                out.append(f"   - matériel : {e['type']} {e['detail'] or ''}")
        outcomes = q("SELECT * FROM outcomes WHERE route_id=? ORDER BY id", r["id"])
        if outcomes:
            out += ["", "### Résultats", ""]
            out += [f"- {o['property']} : {val(o['value_num'], o['value_text'], o['unit'])}" for o in outcomes]
        for a in q("SELECT type, text FROM annotations WHERE route_id=? AND type != 'limite_reproductibilite'"
                   " AND type NOT LIKE 'securite_%' ORDER BY id", r["id"]):
            out += ["", f"*{a['type'].replace('_', ' ').capitalize()}.* {a['text']}"]
        out.append("")
    return "\n".join(out)


def main():
    con = db.connect()
    target = db.ROOT / "fiches"
    target.mkdir(exist_ok=True)
    where, args = ("WHERE pmcid=?", (sys.argv[1],)) if len(sys.argv) > 1 else ("WHERE status='extracted'", ())
    n = 0
    for paper in con.execute(f"SELECT * FROM papers {where} ORDER BY seq", args).fetchall():
        (target / f"{paper['pmcid']}.md").write_text(fiche(con, paper), encoding="utf-8")
        n += 1
    print(f"{n} fiches ecrites dans {target}")


if __name__ == "__main__":
    main()
