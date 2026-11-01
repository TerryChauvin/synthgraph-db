#!/usr/bin/env python3
"""Chiffres clés de la page d'accueil (demande de l'utilisateur du 28/10/2026).

Usage : python3 -I analyses/chiffres_accueil.py → docs/audit_contenu/data/chiffres_accueil.json
Base ouverte en lecture seule. Définitions :
- publications : papiers extraits (status 'extracted') ;
- voies : toutes les voies de ces publications (base + branches, tous types) ;
- matériaux différents : couples (composition, phase) distincts sur les voies non « dispositif » ;
  composition = formule sans espaces, sinon nom en minuscules ; phase en minuscules (vide si non dite) ;
- méthodes : classes de méthode (mots-clés de audit_contenu.METHOD_RULES) hors « non classée » ;
- paramètres communs : similarité de Jaccard moyenne des ensembles de paramètres canoniques entre deux
  voies de base de la même méthode, moyenne pondérée par le nombre de voies (méthodes à ≥ 5 voies) ;
- propriétés communes : idem avec les propriétés canoniques entre deux voies de base de la même famille ;
- coût : historique complet de audits/jetons.csv (chaque agent, sans moyenne), au tarif API catalogue.
  Le CSV ne sépare pas entrée / sortie / cache : on donne une fourchette (tout en lecture de cache →
  tout en entrée non cachée). Non comptés : l'orchestrateur et ce qui n'a pas été consigné (voir « manques »)."""
import os, sys, csv, json, sqlite3, itertools, collections, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); os.chdir(ROOT)
from audit_contenu import METHOD_RE

# tarifs API par million de jetons (référence Anthropic, cache du 2026-10-06) : entrée, sortie, lecture de cache
PRIX = {"sonnet": dict(modele="Claude Sonnet 5.5", entree=2.0, sortie=10.0, cache=0.20),
        "opus": dict(modele="Claude Opus 5.5", entree=4.0, sortie=20.0, cache=0.20)}


def jaccard(groups, min_n=5):
    tot, w, det = 0.0, 0, []
    for k, sets in sorted(groups.items(), key=lambda x: -len(x[1])):
        sets = [s for s in sets if s]
        if len(sets) < min_n: continue
        pairs = list(itertools.combinations(sets, 2))[:20000]
        j = sum(len(a & b) / len(a | b) for a, b in pairs) / len(pairs)
        det.append(dict(groupe=k, voies=len(sets), jaccard=round(j, 3)))
        tot += j * len(sets); w += len(sets)
    return round(100 * tot / w, 1), det


def main():
    c = sqlite3.connect(f"file:{os.path.join(ROOT, 'synthese.db')}?mode=ro", uri=True); q = lambda s, *a: c.execute(s, a).fetchall()
    pubs = q("select count(*) from papers where status='extracted'")[0][0]
    voies = q("select count(*) from synthesis_routes r join papers p on p.id=r.paper_id where p.status='extracted'")[0][0]
    mats = set(); comps = set()
    for f, nm, ph in q("select m.formula, m.name, m.phase from synthesis_routes r join papers p on p.id=r.paper_id join materials m on m.id=r.material_id "
                       "where p.status='extracted' and coalesce(r.kind,'material')!='device'"):
        comp = re.sub(r"\s+", "", f) if f and f.strip() else (nm or "").strip().lower()
        if not comp: continue
        comps.add(comp); mats.add((comp, (ph or "").strip().lower()))
    base = q("select r.id, r.method, m.family from synthesis_routes r join papers p on p.id=r.paper_id left join materials m on m.id=r.material_id "
             "where p.status='extracted' and r.parent_route_id is null and coalesce(r.kind,'material')='material'")
    meth = {rid: next((k for k, rx in METHOD_RE if rx.search(m or "")), "non_classee") for rid, m, _ in base}
    fam = {rid: f or "autre" for rid, _, f in base}
    par = collections.defaultdict(set); pro = collections.defaultdict(set)
    for rid, n in q("select s.route_id, p.name_canon from parameters p join steps s on s.id=p.step_id where p.name_canon is not null"): par[rid].add(n)
    for rid, n in q("select route_id, property_canon from outcomes where property_canon is not null and property_canon not in ('autre','other')"): pro[rid].add(n)
    gm = collections.defaultdict(list); gf = collections.defaultdict(list)
    for rid in meth:
        if meth[rid] != "non_classee": gm[meth[rid]].append(frozenset(par[rid]))
        if fam[rid] != "autre": gf[fam[rid]].append(frozenset(pro[rid]))
    pct_par, det_par = jaccard(gm); pct_pro, det_pro = jaccard(gf)
    # coût : chaque ligne du journal, au tarif de son modèle
    rows = list(csv.DictReader(open("audits/jetons.csv", encoding="utf-8-sig")))
    passes = collections.defaultdict(lambda: dict(agents=0, jetons=0))
    for r in rows:
        k = (re.sub(r"(_lot\d|\d[a-z])$", "", r["passe"]).replace("critique_scientifique", "critique_science"), r["modele"])
        passes[k]["agents"] += 1; passes[k]["jetons"] += int(r["jetons"] or 0)
    cout = []
    for (ps, mo), v in sorted(passes.items(), key=lambda x: -x[1]["jetons"]):
        P = PRIX[mo]; m = v["jetons"] / 1e6
        cout.append(dict(passe=ps, modele=P["modele"], agents=v["agents"], jetons=v["jetons"], usd_bas=round(m * P["cache"], 2), usd_haut=round(m * P["entree"], 2)))
    out = dict(publications=pubs, voies=voies, materiaux_distincts=len(mats), compositions_distinctes=len(comps),
               methodes=len({m for m in meth.values() if m != "non_classee"}), voies_base_materiau=len(base),
               pct_parametres_communs_methode=pct_par, pct_proprietes_communes_famille=pct_pro,
               agents=len(rows), jetons=sum(x["jetons"] for x in cout),
               usd_bas=round(sum(x["usd_bas"] for x in cout), 2), usd_haut=round(sum(x["usd_haut"] for x in cout), 2),
               tarifs=PRIX, cout_par_passe=cout, detail_parametres=det_par, detail_proprietes=det_pro,
               publications_sans_extraction_consignee=pubs - len({r["﻿publication" if "﻿publication" in r else "publication"] for r in rows if r["passe"] == "extraction"}),
               manques=["jetons de l'orchestrateur (session principale) non consignés",
                        "extractions et mises à niveau des premières publications du palier 1 non consignées",
                        "ré-extraction à l'aveugle de 20 publications (2,85 M jetons selon CLAUDE.md) absente du journal"])
    json.dump(out, open("docs/audit_contenu/data/chiffres_accueil.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print({k: v for k, v in out.items() if not isinstance(v, (list, dict))})


if __name__ == "__main__":
    main()
