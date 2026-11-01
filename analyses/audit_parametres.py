#!/usr/bin/env python3
"""Profil de paramètres par méthode de synthèse et couverture des paramètres essentiels.
Usage : python3 -I analyses/audit_parametres.py  → docs/audit_contenu/data/{profil_parametres,homogeneite_methodes,essentiels_methode,reactifs_quantites}.json
Trois états par (voie, paramètre) : cité ; déclaré « non cité » par l'extracteur (manque de l'article) ; absent de la grille (manque de l'extraction)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]
os.chdir(ROOT)  # chemins relatifs à la racine du dépôt
import json, re, sqlite3, collections, itertools, os, sys
from audit_contenu import METHOD_RE

# Paramètres essentiels par méthode (jugement de chimiste ; le même nom que dans parameters/not_stated).
ESS = {
    "hydrothermal": ["temperature", "duration", "volume", "concentration", "fill_fraction", "ph", "heating_rate", "cooling_rate"],
    "solvothermal": ["temperature", "duration", "volume", "concentration", "fill_fraction", "heating_rate", "cooling_rate"],
    "sol-gel": ["temperature", "duration", "molar_ratio", "ph", "stirring_speed", "heating_rate", "atmosphere", "concentration"],
    "precipitation/co-precipitation": ["temperature", "duration", "concentration", "ph", "addition_rate", "stirring_speed", "volume"],
    "hot-injection": ["temperature", "duration", "atmosphere", "volume", "concentration", "cooling_rate", "addition_rate"],
    "microwave": ["temperature", "duration", "power", "volume", "pressure"],
    "sonochemical": ["duration", "power", "frequency", "temperature", "volume"],
    "mechanochemical": ["duration", "speed", "atmosphere", "repetitions"],
    "CVD/ALD/PVD": ["temperature", "duration", "pressure", "gas_flow", "atmosphere", "heating_rate"],
    "film_deposition": ["spin_speed", "duration", "concentration", "temperature", "atmosphere", "thickness"],
    "electrochemical": ["duration", "temperature", "concentration", "potential", "current_density"],
    "solid-state": ["temperature", "duration", "heating_rate", "atmosphere", "repetitions"],
    "combustion/pyrolysis": ["temperature", "duration", "heating_rate", "atmosphere", "gas_flow"],
    "green/bio": ["temperature", "duration", "concentration", "volume", "ph", "stirring_speed"],
    "chemical_reduction": ["temperature", "duration", "concentration", "addition_rate", "stirring_speed", "ph", "volume"],
    "thermal_treatment/activation": ["temperature", "duration", "heating_rate", "atmosphere", "gas_flow"],
    "room_temperature_solution": ["duration", "concentration", "volume", "stirring_speed", "ph", "temperature"],
    "reflux/heating_in_solution": ["temperature", "duration", "concentration", "volume", "stirring_speed", "atmosphere"],
    "ion_exchange/impregnation": ["temperature", "duration", "concentration", "volume", "repetitions", "ph"],
    "polymerization": ["temperature", "duration", "concentration", "atmosphere", "stirring_speed"],
}
GENERIC = ["temperature", "duration", "atmosphere", "stirring_speed", "heating_rate", "concentration", "volume", "ph", "addition_rate", "pressure", "cooling_rate", "repetitions", "centrifuge_speed", "wash_solvent", "power", "gas_flow", "molar_ratio", "fill_fraction", "speed", "spin_speed", "frequency"]

def main():
    c = sqlite3.connect("synthese.db"); q = lambda s, *a: c.execute(s, a).fetchall()
    base = q("select r.id, r.method from synthesis_routes r join papers p on p.id=r.paper_id where p.critic_status='done' and r.parent_route_id is null and r.kind='material'")
    cited, declared = collections.defaultdict(set), collections.defaultdict(set)
    for rid, name in q("select s.route_id, lower(p.name) from parameters p join steps s on s.id=p.step_id"):
        cited[rid].add(re.sub(r"_final|_initial|_max|_min$", "", name))
    for rid, name in q("select route_id, lower(name) from not_stated where scope='step'"):
        declared[rid].add(name)
    amt = collections.defaultdict(lambda: [0, 0, 0])  # precursors: amount given / not_stated / neither
    ns_re = {rid: set() for rid, _ in base}
    for rid, reagent, name in q("select route_id, reagent, name from not_stated where scope='reagent'"):
        if rid in ns_re: ns_re[rid].add((reagent, name))
    meth = {}
    for rid, m in base:
        meth[rid] = next((k for k, rx in METHOD_RE if rx.search(m or "")), "non_classee")
        for name, a, at in q("select name, amount, amount_text from reagents where route_id=? and role='precursor'", rid):
            if a is not None or at: amt[meth[rid]][0] += 1
            elif any(n == "amount" and r == name for r, n in ns_re[rid]): amt[meth[rid]][1] += 1
            else: amt[meth[rid]][2] += 1
    bym = collections.defaultdict(list)
    for rid, _ in base: bym[meth[rid]].append(rid)
    profil, homog, ess_rows = [], [], []
    for m, rids in sorted(bym.items(), key=lambda x: -len(x[1])):
        n = len(rids)
        params = set(GENERIC) | set(ESS.get(m, []))
        for p in sorted(params):
            kc = sum(1 for r in rids if p in cited[r]); kd = sum(1 for r in rids if p not in cited[r] and p in declared[r]); ka = n - kc - kd
            profil.append(dict(methode=m, parametre=p, voies=n, essentiel=p in ESS.get(m, []), pct_cite=round(100 * kc / n, 1), pct_non_cite_declare=round(100 * kd / n, 1), pct_absent_grille=round(100 * ka / n, 1)))
        sets = [frozenset(cited[r]) for r in rids]
        pairs = list(itertools.combinations(sets, 2))[:5000]
        jac = sum(len(a & b) / len(a | b) for a, b in pairs if a | b) / len(pairs) if pairs else None
        typ = collections.Counter(p for s in sets for p in s)
        homog.append(dict(methode=m, voies=n, jaccard_moyen=round(jac, 2) if jac is not None else None, parametres_par_voie=round(sum(len(s) for s in sets) / n, 1), parametres_typiques=", ".join(f"{p} {round(100*k/n)}%" for p, k in typ.most_common(6))))
        if m in ESS:
            E = ESS[m]
            tot = n * len(E)
            kc = sum(1 for r in rids for p in E if p in cited[r]); kd = sum(1 for r in rids for p in E if p not in cited[r] and p in declared[r])
            ess_rows.append(dict(methode=m, voies=n, essentiels=len(E), pct_cite=round(100 * kc / tot, 1), pct_non_cite_declare=round(100 * kd / tot, 1), pct_absent_grille=round(100 * (tot - kc - kd) / tot, 1),
                                 pires=", ".join(f"{p} ({round(100*sum(1 for r in rids if p in cited[r])/n)}% cité, {round(100*sum(1 for r in rids if p not in cited[r] and p not in declared[r])/n)}% hors grille)" for p in sorted(E, key=lambda p: sum(1 for r in rids if p in cited[r]))[:3])))
    react = [dict(methode=m, precurseurs=sum(v), pct_quantite=round(100 * v[0] / sum(v), 1), pct_non_cite_declare=round(100 * v[1] / sum(v), 1), pct_absent_grille=round(100 * v[2] / sum(v), 1)) for m, v in sorted(amt.items(), key=lambda x: -sum(x[1])) if sum(v)]
    out = "docs/audit_contenu/data/"
    for k, v in dict(profil_parametres=profil, homogeneite_methodes=homog, essentiels_methode=ess_rows, reactifs_quantites=react).items():
        json.dump(v, open(out + k + ".json", "w"), ensure_ascii=False, separators=(",", ":"))
    allE = [r for r in ess_rows]
    print("ESSENTIELS par méthode (cité / non cité déclaré / absent de la grille)")
    for r in allE: print(f"  {r['methode']:32s} n={r['voies']:3d}  cité {r['pct_cite']:5.1f}%  déclaré absent {r['pct_non_cite_declare']:5.1f}%  hors grille {r['pct_absent_grille']:5.1f}%  | pires : {r['pires']}")
    print("\nHOMOGÉNÉITÉ (Jaccard moyen des jeux de paramètres entre voies d'une même méthode)")
    for r in homog[:14]: print(f"  {r['methode']:32s} n={r['voies']:3d}  J={r['jaccard_moyen']}  {r['parametres_par_voie']} param/voie  | {r['parametres_typiques']}")
    print("\nQUANTITÉS DES PRÉCURSEURS")
    for r in react[:12]: print(f"  {r['methode']:32s} {r['precurseurs']:4d} précurseurs : quantité {r['pct_quantite']}%  déclarée absente {r['pct_non_cite_declare']}%  hors grille {r['pct_absent_grille']}%")
if __name__ == "__main__": main()
