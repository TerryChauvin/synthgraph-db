"""Sonde des manques d'extraction (point 1 du plan du 28/10/2026).

Pour chaque publication close, cherche dans les sections expérimentales de corpus/text/<PMCID>.txt des
termes qui annoncent un paramètre de procédé ou une condition de mesure, et vérifie si l'extraction porte
quelque chose sous ce nom (paramètre, action d'étape, équipement, case `not_stated`, technique avec
`conditions`, propriété). Un terme présent sans rien d'extrait = un manque possible, à relire.

    python3 -I analyses/sonde_manques.py            # toutes les publications closes → JSON + rapport
    python3 -I analyses/sonde_manques.py PMC1234567 # liste à relire pour une publication (Markdown)

Sorties : docs/audit_contenu/data/sonde_manques.json (résumé + détail par publication, positions dans le
texte) et audits/sonde_manques.md (tableau de synthèse, publications les plus touchées).
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

OUT_JSON = "docs/audit_contenu/data/sonde_manques.json"
OUT_MD = "audits/sonde_manques.md"
EXP = re.compile(r"^## .*(experiment|method|synthes|preparation|materials and|procedure|fabrication|growth|supporting information)", re.I)

# (libellé, regex dans le texte, regex sur les noms extraits : paramètres, actions, équipements, not_stated)
PARAM_PROBES = [
    ("rampe de chauffe", r"°c ?/ ?min|°c min|k ?/ ?min|°c per min|heating rate", r"ramp|heating_rate|\brate"),
    ("refroidissement", r"cool(ed|ing)\b.{0,30}(naturally|slowly|to room|at a rate|in air|furnace)|quench|furnace.cool", r"cool|quench"),
    ("débit de gaz", r"\bsccm\b|m?l ?/ ?min|l/min|flow rate", r"flow"),
    ("agitation (rpm)", r"\brpm\b", r"stir|rpm|agitation|rotation|speed"),
    ("puissance (W)", r"\b\d+ ?w\b|\bwatt|\bkw\b", r"power|watt"),
    ("pH", r"\bph\b", r"\bph"),
    ("lavage (n fois)", r"washed .{0,40}(times|thrice|twice)|washed (three|several|two)", r"wash|rins|cycle|repeat|times"),
    ("centrifugation", r"centrifug", r"centrifug|rpm|speed"),
    ("séchage", r"\bdried\b|\bdrying\b|\bdry\b", r"\bdry|desicc|lyophil|freeze"),
    ("vieillissement / repos", r"\baged\b|\bag(e)?ing\b|left (to )?stand|allowed to stand", r"\bag(e|ing)|rest|stand"),
    ("ultrasons", r"sonicat|ultrasonic", r"sonic|ultrason"),
    ("vide", r"vacuum", r"vacuum|pressure"),
    ("atmosphère", r"\b(argon|nitrogen|n2|ar|air|h2|forming gas)\b.{0,15}(atmosphere|flow)|under (ar|argon|n2|nitrogen|air|vacuum)", r"atmos|gas"),
    ("taux de remplissage", r"fill(ed|ing)? .{0,20}\d+ ?%|\d+ ?% ?(filled|filling|of the (autoclave|volume))", r"fill"),
    ("rendement (chiffré)", r"yield of \d|\d+(\.\d+)? ?% yield|isolated yield|yield(ed)? (about |ca\. |~)?\d+(\.\d+)? ?(g|mg|%)", r"yield"),
    ("répétitions", r"repeated (three|3|several|twice)|in triplicate|three (independent|separate|different) (batches|syntheses|samples)|batch-to-batch", r"repeat|replic|batch|triplic"),
    ("échelle / lot", r"gram-scale|scale-?up|large-?scale|\d+(\.\d+)? ?g of (product|powder|sample)", r"scale|batch|yield"),
    ("vitesse d'addition", r"dropwise|drop-wise|added slowly|\bml ?/ ?min|\bml ?/ ?h\b|syringe pump", r"addition|dropwise|injection|rate"),
    ("purification (dialyse, colonne, tamis)", r"dialys|column chromatograph|sieve|mesh|filtered through", r"dialys|chromat|sieve|filter"),
]
# (libellé, regex dans le texte entier, regex technique/propriété)
CARAC_PROBES = [
    ("XRD", r"\bxrd\b|x-ray diffraction", r"xrd|diffract|phase|crystal|lattice|scherrer"),
    ("BET", r"\bbet\b|brunauer", r"bet|surface_area|pore"),
    ("TEM/SEM", r"\btem\b|\bsem\b|electron microscop", r"tem|sem|microscop|size|morpholog"),
    ("XPS", r"\bxps\b", r"xps|oxidation|binding"),
    ("Raman", r"\braman\b", r"raman"),
    ("TGA", r"\btga\b|thermogravimetr", r"tga|thermogravim|weight_loss|thermal|mass_loss"),
    ("UV-vis / band gap", r"uv-vis|uv–vis|band ?gap|tauc", r"uv|band|gap|absorb"),
    ("PL", r"photoluminescence|\bpl\b", r"\bpl\b|photolum|emission|quantum_yield"),
    ("ICP/EDS composition", r"\bicp\b|\beds\b|\bedx\b|elemental analysis", r"icp|eds|edx|composition|content|ratio|element"),
    ("DLS / zêta", r"\bdls\b|zeta potential|hydrodynamic", r"dls|zeta|hydrodynamic"),
    ("magnétisme", r"\bvsm\b|squid|magnetization|coerciv", r"magnet|coerciv|saturation"),
    ("électrochimie", r"cyclic voltammetry|\bcv\b|galvanostatic|\beis\b|capacit", r"capacit|electro|current|voltage|overpotential|cycl|impedance|conductiv|\bcv\b|\beis\b"),
    ("catalyse / adsorption", r"degradation|conversion|selectivity|adsorption capacity|removal", r"degrad|convers|select|adsorpt|removal|rate|efficiency|yield|catal"),
]


def sections(txt):
    """[(début, fin)] des sections expérimentales ; tout le texte si aucun titre ne correspond."""
    pos = [m.start() for m in re.finditer(r"(?m)^(?=## )", txt)] + [len(txt)]
    spans = [(a, b) for a, b in zip(pos, pos[1:]) if EXP.match(txt[a:b])]
    return spans or [(0, len(txt))]


def names_by_paper(c):
    N = collections.defaultdict(set)
    q = """SELECT p.pmcid, x FROM (
     SELECT r.paper_id pid, lower(pa.name) x FROM parameters pa JOIN steps s ON pa.step_id=s.id JOIN synthesis_routes r ON s.route_id=r.id
     UNION ALL SELECT r.paper_id, lower(s.action) FROM steps s JOIN synthesis_routes r ON s.route_id=r.id
     UNION ALL SELECT r.paper_id, lower(e.type) FROM equipment e JOIN steps s ON e.step_id=s.id JOIN synthesis_routes r ON s.route_id=r.id
     UNION ALL SELECT r.paper_id, 'ns:'||lower(n.name) FROM not_stated n JOIN synthesis_routes r ON n.route_id=r.id
    ) t JOIN papers p ON p.id=t.pid"""
    for pid, x in c.execute(q):
        N[pid].add(x or "")
    T, Tc, O = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
    for pid, t, cond in c.execute("SELECT p.pmcid, lower(ch.technique), ch.conditions FROM characterizations ch JOIN synthesis_routes r ON ch.route_id=r.id JOIN papers p ON p.id=r.paper_id"):
        T[pid].add(t or "")
        if cond and cond.strip():
            Tc[pid].add(t or "")
    for pid, t in c.execute("SELECT p.pmcid, lower(o.property) FROM outcomes o JOIN synthesis_routes r ON o.route_id=r.id JOIN papers p ON p.id=r.paper_id"):
        O[pid].add(t or "")
    return N, T, Tc, O


def snippet(txt, a, b, w=90):
    return re.sub(r"\s+", " ", txt[max(0, a - w):b + w]).strip()


def probe_paper(pmcid, txt, N, T, Tc, O):
    hits = []
    spans = sections(txt)
    for lab, tr, pr in PARAM_PROBES:
        t, p = re.compile(tr, re.I), re.compile(pr, re.I)
        ms = [m for a, b in spans for m in t.finditer(txt, a, b)]
        if not ms:
            continue
        cited = any(p.search(n) for n in N[pmcid] if not n.startswith("ns:"))
        if cited:
            continue
        state = "not_stated" if any(p.search(n) for n in N[pmcid] if n.startswith("ns:")) else "absent"
        hits.append(dict(sonde=lab, etat=state, n=len(ms), positions=[m.start() for m in ms[:5]], extraits=[snippet(txt, m.start(), m.end()) for m in ms[:3]]))
    for lab, tr, pr in CARAC_PROBES:
        t, p = re.compile(tr, re.I), re.compile(pr, re.I)
        ms = list(t.finditer(txt))
        if not ms:
            continue
        has_cond = any(p.search(n) for n in Tc[pmcid])
        has_out = any(p.search(n) for n in O[pmcid])
        if has_cond and has_out:
            continue
        state = ("conditions absentes" if not has_cond else "") + (" ; " if not has_cond and not has_out else "") + ("résultat absent" if not has_out else "")
        hits.append(dict(sonde="mesure : " + lab, etat=state, n=len(ms), positions=[m.start() for m in ms[:5]], extraits=[snippet(txt, m.start(), m.end(), 70) for m in ms[:2]]))
    return hits


def run_all(c):
    N, T, Tc, O = names_by_paper(c)
    pm = [r[0] for r in c.execute("SELECT pmcid FROM papers WHERE status='extracted' ORDER BY seq")]
    papers, count = {}, collections.defaultdict(lambda: [0, 0, 0])  # sonde → [articles, absent, not_stated]
    for x in pm:
        f = f"corpus/text/{x}.txt"
        if not os.path.exists(f):
            continue
        txt = open(f, encoding="utf-8", errors="ignore").read()
        hits = probe_paper(x, txt, N, T, Tc, O)
        papers[x] = dict(manques=len(hits), sondes=hits)
        for h in hits:
            count[h["sonde"]][1] += 1
            if h["etat"] == "not_stated":
                count[h["sonde"]][2] += 1
    # articles mentionnant chaque sonde (dénominateur)
    for lab, tr, _ in PARAM_PROBES:
        t = re.compile(tr, re.I)
        for x in papers:
            txt = open(f"corpus/text/{x}.txt", encoding="utf-8", errors="ignore").read()
            if any(t.search(txt, a, b) for a, b in sections(txt)):
                count[lab][0] += 1
    for lab, tr, _ in CARAC_PROBES:
        t = re.compile(tr, re.I)
        for x in papers:
            if t.search(open(f"corpus/text/{x}.txt", encoding="utf-8", errors="ignore").read()):
                count["mesure : " + lab][0] += 1
    summary = [dict(sonde=k, articles=v[0], manques=v[1], pct=round(100.0 * v[1] / max(v[0], 1), 1), dont_not_stated=v[2])
               for k, v in count.items()]
    summary.sort(key=lambda r: -r["pct"])
    return dict(publications=len(papers), resume=summary, par_publication=papers)


def md_paper(pmcid, d):
    L = [f"# Sonde des manques — {pmcid}", "", f"{d['manques']} points à relire (terme présent dans l'article, rien d'extrait sous ce nom).", ""]
    for h in d["sondes"]:
        L.append(f"## {h['sonde']} — {h['etat']} ({h['n']} occurrence(s), positions {', '.join(map(str, h['positions']))})")
        L += [f"- « {e} »" for e in h["extraits"]] + [""]
    return "\n".join(L)


def main():
    c = sqlite3.connect("synthese.db")
    if len(sys.argv) > 1:
        x = sys.argv[1]
        if os.path.exists(OUT_JSON):
            d = json.load(open(OUT_JSON, encoding="utf-8"))["par_publication"].get(x)
        else:
            d = None
        if d is None:
            N, T, Tc, O = names_by_paper(c)
            txt = open(f"corpus/text/{x}.txt", encoding="utf-8", errors="ignore").read()
            hits = probe_paper(x, txt, N, T, Tc, O)
            d = dict(manques=len(hits), sondes=hits)
        print(md_paper(x, d))
        return
    D = run_all(c)
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    json.dump(D, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    P = D["par_publication"]
    dist = collections.Counter(v["manques"] for v in P.values())
    L = ["# Sonde des manques d'extraction", "",
         f"{D['publications']} publications closes. Un « manque » = terme présent dans les sections expérimentales (ou, pour les mesures, dans tout l'article)",
         "sans paramètre, action, équipement ni case `not_stated` correspondant ; pour les mesures, technique sans `conditions` ou sans résultat lié.",
         "Script : `analyses/sonde_manques.py` ; détail par publication : `python3 -I analyses/sonde_manques.py <PMCID>`.", "",
         "| Sonde | Articles concernés | Manques | % | dont déclarés `not_stated` |", "|---|---|---|---|---|"]
    L += [f"| {r['sonde']} | {r['articles']} | {r['manques']} | {r['pct']} | {r['dont_not_stated']} |" for r in D["resume"]]
    L += ["", "## Répartition par publication", "", "| Manques par publication | Publications |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in sorted(dist.items())]
    top = sorted(P.items(), key=lambda kv: -kv[1]["manques"])[:30]
    L += ["", "## Publications les plus touchées", "", "| PMCID | Manques | Sondes |", "|---|---|---|"]
    L += [f"| {x} | {v['manques']} | {', '.join(h['sonde'] for h in v['sondes'])} |" for x, v in top]
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"ok: {D['publications']} publications, {sum(v['manques'] for v in P.values())} manques → {OUT_JSON}, {OUT_MD}")


if __name__ == "__main__":
    main()
