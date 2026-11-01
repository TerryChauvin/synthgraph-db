"""Respect des grilles de réglages : synthèse (imposée par load.py) et caractérisation (non imposée).

    python3 -I analyses/audit_grilles.py   → audits/audit_grilles.md, docs/audit_contenu/data/audit_grilles.json

A. Grille de synthèse (`load.py`, EXPECTED_STEP / EXPECTED_REAGENT / EXPECTED_ROUTE) :
   - remplissage : chaque case attendue est citée ou déclarée `not_stated` (le contrôle l'impose) ;
   - justesse des `not_stated` : une case déclarée absente alors que la citation de l'étape contient
     la valeur (température, durée, vitesse…) est suspecte ; pureté et fournisseur déclarés absents
     alors qu'une phrase de l'article nomme le réactif avec un fournisseur ou un grade ;
   - couverture : réglages de procédé hors grille (jamais exigés) cités ou non.
B. Grille de caractérisation (aucune n'est imposée) : part des entrées avec appareil et conditions,
   réglages attendus par technique présents dans `conditions`, et présents dans l'article.
"""
import collections
import json
import os
import re
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]
os.chdir(ROOT)
import load  # noqa: E402

SLOT_RE = {
    "temperature": r"\d\s?°\s?C|\d\s?K\b|room temperature|\bRT\b|ambient temperature",
    "duration": r"\d\s?(h|hr|hrs|hours?|min|minutes?|s|sec|days?|d)\b|overnight",
    "heating_rate": r"°\s?C\s?/?\s?min|K\s?/?\s?min|°C min|heating rate|ramp",
    "atmosphere": r"\b(air|N2|nitrogen|Ar|argon|H2|vacuum|O2|oxygen|inert)\b",
    "speed": r"\d\s?(rpm|g\b|×\s?g|x\s?g)",
    "wash_solvent": r"water|ethanol|methanol|acetone|DI\b|deionized|distilled|hexane|toluene|DMF",
    "repetitions": r"(three|two|several|3|2|five|5|four|4)\s*(times|×|x\b)|thrice|twice|repeatedly",
    "ph": r"\bpH\b",
    "yield": r"\byield",
}
SUPPLIER_RE = re.compile(r"Sigma|Aldrich|Merck|Alfa Aesar|Fisher|Acros|TCI|Sinopharm|Macklin|Aladdin|Fluka|Kanto|Wako|Junsei|Daejung|Loba|Himedia|HiMedia|Qualigens|SRL|Riedel|VWR|Strem|Thermo|Panreac|Carlo Erba|Avantor|BDH|Nacalai|Kishida|Samchun|Duksan", re.I)
GRADE_RE = re.compile(r"\d{2}(\.\d+)?\s?%|analytical(ly)? (grade|reagent)|\bAR\b|reagent grade|\bACS\b|HPLC grade|spectroscopic grade|purum|puriss|ultrapure|extra pure|GR grade|\bLR\b", re.I)
OUTSIDE = {  # réglages de procédé non exigés par la grille : (regex nom de paramètre, regex texte de l'étape)
    "vitesse d'agitation": (r"stir|rpm|agitation", r"\d\s?rpm"),
    "refroidissement": (r"cool|quench", r"cool(ed|ing)|quench"),
    "débit de gaz": (r"flow", r"sccm|m?l\s?/\s?min|flow"),
    "pression / vide": (r"pressure|vacuum", r"vacuum|torr|mbar|\bpa\b|bar\b"),
    "taux de remplissage": (r"fill", r"fill"),
    "vitesse d'addition": (r"addition|dropwise|injection", r"dropwise|drop by drop|slowly|ml\s?/\s?(min|h)"),
    "puissance": (r"power|watt", r"\d\s?w\b|watt"),
}
CARAC = {  # technique → réglages attendus (regex dans conditions et dans le texte de l'article)
    "XRD": (r"xrd|x-ray diffraction|diffractom", {"rayonnement": r"cu\s?k|co\s?k|mo\s?k|λ\s?=|wavelength|1\.54", "plage 2θ": r"2\s?θ|2theta|°\s?(to|–|-)\s?\d+\s?°|range", "pas / vitesse": r"step|scan(ning)? (rate|speed)|°\s?/\s?(min|s)"}),
    "BET": (r"\bbet\b|n2 (adsorption|sorption|physisorption)|nitrogen (adsorption|sorption)", {"gaz / température": r"77\s?k|n2|nitrogen|-196", "dégazage": r"degas|outgas|pretreat|evacuat"}),
    "TEM/SEM": (r"\btem\b|\bsem\b|fesem|hrtem|microscop", {"tension": r"\d\s?kv", "nombre de particules": r"\d+\s?(particles|nanoparticles)|counted|n\s?=\s?\d"}),
    "XPS": (r"\bxps\b|photoelectron", {"source": r"al\s?k|mg\s?k|monochromat", "référence C 1s": r"284\.\d|c\s?1s"}),
    "UV-vis / gap": (r"uv|vis|drs|diffuse reflect|tauc|band gap", {"plage": r"\d{3}\s?(–|-|to)\s?\d{3}\s?nm|range", "méthode du gap": r"tauc|kubelka"}),
    "PL": (r"\bpl\b|photolumin|fluoresc", {"excitation": r"excit|λex|λ\s?ex"}),
    "TGA": (r"\btga\b|\btg\b|thermogravim", {"atmosphère": r"air|n2|nitrogen|argon|ar\b", "rampe": r"°\s?c\s?/?\s?min|k\s?/?\s?min|heating rate"}),
    "électrochimie": (r"electrochem|voltamm|\bcv\b|galvanostat|\beis\b|impedance|charge.discharge|capacit", {"électrolyte": r"koh|naoh|h2so4|na2so4|lipf6|electrolyte|\bm\b", "masse active / électrode": r"mass loading|active mass|mg\s?cm|loading", "vitesse de balayage": r"mv\s?s|mv/s|scan rate"}),
    "catalyse / adsorption": (r"catal|degrad|adsorption (test|experiment|capacity)|photocatal|removal", {"masse de catalyseur": r"\d\s?mg|\d\s?g\s?(l|/)|dose|dosage", "concentration": r"mg\s?/?\s?l|ppm|mm\b|mol", "source lumineuse": r"lamp|light|led|xe|uv|visible|irradiat"}),
}


def main():
    c = sqlite3.connect("synthese.db")
    q = lambda s, *a: c.execute(s, a).fetchall()
    pids = {r[0]: r[1] for r in q("SELECT id, pmcid FROM papers WHERE status='extracted' AND format_version>=2")}
    texts = {}

    def text(p):
        if p not in texts:
            f = f"corpus/text/{p}.txt"
            texts[p] = open(f, encoding="utf-8", errors="ignore").read() if os.path.exists(f) else ""
        return texts[p]
    D = {}
    # ---------------- A1 remplissage et A2 not_stated suspects (étapes)
    steps = q("SELECT s.id, r.paper_id, r.id, s.action, s.quote, COALESCE(s.description,'') FROM steps s JOIN synthesis_routes r ON s.route_id=r.id WHERE COALESCE(r.kind,'material')<>'calcul'")
    params = collections.defaultdict(list)
    for sid, name in q("SELECT step_id, name FROM parameters"):
        params[sid].append(name or "")
    ns_step = collections.defaultdict(list)
    for rid, so, name in q("SELECT route_id, step_order, name FROM not_stated WHERE scope='step'"):
        ns_step[(rid, so)].append(name)
    so_of = {r[0]: r[1] for r in q("SELECT id, step_order FROM steps")}
    slot_stats = collections.defaultdict(lambda: dict(attendu=0, cite=0, non_cite=0, suspect=0, exemples=[]))
    for sid, pid, rid, action, quote, desc in steps:
        if pid not in pids:
            continue
        slots = load.expected_slots(action)
        names = params[sid]
        ns = ns_step[(rid, so_of[sid])]
        for slot in slots:
            st = slot_stats[slot]
            st["attendu"] += 1
            if any(slot in n for n in names):
                st["cite"] += 1
            elif slot in ns:
                st["non_cite"] += 1
                pat = SLOT_RE.get(slot)
                if pat and re.search(pat, quote or "", re.I):
                    st["suspect"] += 1
                    if len(st["exemples"]) < 4:
                        st["exemples"].append(f"{pids[pid]} étape {so_of[sid]} ({action}) : « {re.sub(chr(10), ' ', (quote or '')[:150])} »")
    D["grille_synthese_etapes"] = [dict(case=k, **{kk: vv for kk, vv in v.items()}) for k, v in slot_stats.items()]
    # réactifs : pureté / fournisseur déclarés absents alors qu'une phrase nomme le réactif avec un grade ou un fournisseur
    rg = q("SELECT g.id, r.paper_id, g.name, g.purity, g.supplier, g.role FROM reagents g JOIN synthesis_routes r ON g.route_id=r.id")
    ns_rg = collections.defaultdict(set)
    for rid, reagent, name in q("SELECT route_id, reagent, name FROM not_stated WHERE scope='reagent'"):
        ns_rg[reagent].add(name)
    rstats = {k: dict(attendu=0, cite=0, non_cite=0, suspect=0, exemples=[]) for k in ("purity", "supplier")}
    seen = set()
    for gid, pid, name, purity, supplier, role in rg:
        if pid not in pids or (role or "").lower() in load.NO_GRID_ROLES or (role or "").lower() == "intermediate":
            continue
        key = (pid, (name or "").lower())
        if key in seen:
            continue
        seen.add(key)
        t = text(pids[pid])
        nm = re.escape((name or "").split("(")[0].strip()[:25])
        sents = [m.group(0) for m in re.finditer(rf"[^.]*{nm}[^.]*\.", t, re.I)][:12] if nm else []
        for slot, val, rx in (("purity", purity, GRADE_RE), ("supplier", supplier, SUPPLIER_RE)):
            st = rstats[slot]
            st["attendu"] += 1
            if val:
                st["cite"] += 1
                continue
            st["non_cite"] += 1
            hit = next((s for s in sents if rx.search(s)), None)
            if hit:
                st["suspect"] += 1
                if len(st["exemples"]) < 4:
                    st["exemples"].append(f"{pids[pid]} {name} : « {re.sub(chr(10), ' ', hit.strip()[:160])} »")
    D["grille_synthese_reactifs"] = [dict(case=k, **v) for k, v in rstats.items()]
    # A3 hors grille : réglage présent dans la citation d'une étape sans paramètre ni not_stated
    out = {k: dict(etapes_concernees=0, extraits=0, declares=0, absents=0) for k in OUTSIDE}
    for sid, pid, rid, action, quote, desc in steps:
        if pid not in pids:
            continue
        names = " ".join(params[sid]).lower()
        ns = " ".join(ns_step[(rid, so_of[sid])]).lower()
        for k, (pn, tx) in OUTSIDE.items():
            if re.search(tx, quote or "", re.I):
                o = out[k]
                o["etapes_concernees"] += 1
                if re.search(pn, names):
                    o["extraits"] += 1
                elif re.search(pn, ns):
                    o["declares"] += 1
                else:
                    o["absents"] += 1
    D["hors_grille"] = [dict(reglage=k, **v) for k, v in out.items()]
    # ---------------- B grille de caractérisation
    ch = q("SELECT r.paper_id, ch.technique, COALESCE(ch.instrument,''), COALESCE(ch.conditions,'') FROM characterizations ch JOIN synthesis_routes r ON ch.route_id=r.id")
    B = []
    for tech, (trx, settings) in CARAC.items():
        rows = [(pid, i, cnd) for pid, t, i, cnd in ch if pid in pids and re.search(trx, t or "", re.I)]
        if not rows:
            continue
        papers = sorted({pid for pid, _, _ in rows})
        line = dict(technique=tech, entrees=len(rows), publications=len(papers),
                    avec_appareil=round(100.0 * sum(1 for _, i, _ in rows if i.strip()) / len(rows), 1),
                    avec_conditions=round(100.0 * sum(1 for _, _, cnd in rows if cnd.strip()) / len(rows), 1), reglages=[])
        for sname, srx in settings.items():
            in_base = in_text = 0
            for pid in papers:
                cnds = " ".join(cnd for p2, _, cnd in rows if p2 == pid)
                b = bool(re.search(srx, cnds, re.I))
                t = bool(re.search(srx, text(pids[pid]), re.I))
                in_base += b
                in_text += t
            line["reglages"].append(dict(reglage=sname, dans_la_base=round(100.0 * in_base / len(papers), 1), mentionne_dans_l_article=round(100.0 * in_text / len(papers), 1)))
        B.append(line)
    D["grille_caracterisation"] = B
    json.dump(D, open("docs/audit_contenu/data/audit_grilles.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # rapport
    L = ["# Respect des grilles de réglages (synthèse et caractérisation)", "",
         f"{len(pids)} publications au format 2. Script : `analyses/audit_grilles.py`. « Suspect » = case déclarée « non cité » alors que la citation de l'étape (ou une phrase de l'article nommant le réactif) contient un indice de la valeur : à relire, pas une erreur prouvée.", "",
         "## A. Grille de synthèse (imposée par `load.py`)", "", "| Case | Attendues | Citées | Déclarées « non cité » | dont suspectes |", "|---|---|---|---|---|"]
    for r in D["grille_synthese_etapes"] + D["grille_synthese_reactifs"]:
        L.append(f"| {r['case']} | {r['attendu']} | {r['cite']} ({100*r['cite']/max(r['attendu'],1):.0f} %) | {r['non_cite']} | {r['suspect']} ({100*r['suspect']/max(r['non_cite'],1):.0f} %) |")
    L += ["", "Exemples de cases suspectes :", ""]
    for r in D["grille_synthese_etapes"] + D["grille_synthese_reactifs"]:
        L += [f"- {r['case']} : {e}" for e in r["exemples"][:2]]
    L += ["", "### Réglages de procédé hors grille (jamais exigés)", "", "| Réglage | Étapes dont la citation le mentionne | Extrait | Déclaré « non cité » | Ni l'un ni l'autre |", "|---|---|---|---|---|"]
    for r in D["hors_grille"]:
        L.append(f"| {r['reglage']} | {r['etapes_concernees']} | {r['extraits']} | {r['declares']} | {r['absents']} ({100*r['absents']/max(r['etapes_concernees'],1):.0f} %) |")
    L += ["", "## B. Grille de caractérisation (aucune n'est imposée)", "", "| Technique | Entrées | Publications | Avec appareil | Avec conditions |", "|---|---|---|---|---|"]
    for r in B:
        L.append(f"| {r['technique']} | {r['entrees']} | {r['publications']} | {r['avec_appareil']} % | {r['avec_conditions']} % |")
    L += ["", "Réglages attendus, par publication : présents dans les conditions extraites, et mentionnés quelque part dans l'article (borne haute de ce qui est extractible).", "", "| Technique | Réglage | Dans la base | Mentionné dans l'article |", "|---|---|---|---|"]
    for r in B:
        for s in r["reglages"]:
            L.append(f"| {r['technique']} | {s['reglage']} | {s['dans_la_base']} % | {s['mentionne_dans_l_article']} % |")
    open("audits/audit_grilles.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
