#!/usr/bin/env python3
"""Audit de contenu de synthese.db : types de synthèse, propriétés, conditions, trous, qualité, limites.

Usage : python3 -I analyses/audit_contenu.py [--out docs/audit_contenu/data]
Produit un fichier JSON par jeu de données (lignes = objets) et summary.json.
Les sorties des agents (mécanismes, références web) sont lues dans docs/audit_contenu/sources/ si présentes.
Ne modifie jamais la base.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]
os.chdir(ROOT)  # chemins relatifs à la racine du dépôt
import argparse, collections, datetime, json, os, re, sqlite3, statistics

# ---------------------------------------------------------------- taxonomies
# Propriétés : (canonique, groupe, regex) ; première règle qui matche, sur le nom en minuscules.
from canon import PROP_RULES, PROP_RE, canon_prop  # noqa: E402  (vocabulaire canonique commun)

# Méthodes (texte libre de la voie) : (classe, regex) par priorité décroissante.
METHOD_RULES = [
    ("hydrothermal", r"hydrotherm"),
    ("solvothermal", r"solvotherm|ionotherm"),
    ("hot-injection", r"hot[- ]injection|injection"),
    ("microwave", r"microwave|micro-onde"),
    ("sonochemical", r"sonochem|ultrason|sonicat"),
    ("mechanochemical", r"mechanochem|ball[- ]mill|broyage|grind|milling"),
    ("CVD/ALD/PVD", r"\bcvd\b|\bald\b|\bpvd\b|sputter|vapou?r deposition|evaporation"),
    ("electrochemical", r"electrodep|électrodép|anodi|electrochem|électrochim|electrolys"),
    ("film_deposition", r"spin[- ]coat|dip[- ]coat|drop[- ]cast|spray|electrospin|électrofil|doctor[- ]blade|screen[- ]print|printing|coating|dépôt"),
    ("sol-gel", r"sol[- –]gel|sol gel|stöber|stober|hydrolysis"),
    ("combustion/pyrolysis", r"combustion|pyroly|carboniz|carbonis|thermal decomposition|thermolysis"),
    ("solid-state", r"solid[- ]state|état solide|ceramic method|solid state"),
    ("green/bio", r"green|extract|plant|biosynth|bacteri|fung|leaf|biogenic|biological"),
    ("precipitation/co-precipitation", r"precipit|précipit"),
    ("reflux/heating_in_solution", r"reflux|heating|thermal|oil bath|water bath"),
    ("ion_exchange/impregnation", r"ion[- ]exchange|impregn|imprégn|échange"),
    ("polymerization", r"polymeri|crosslink|réticul|gelation|gélification"),
    ("self-assembly", r"self[- ]assembl|layer[- ]by[- ]layer|auto-assembl|lbl"),
    ("micellar/emulsion", r"micell|emulsion|microemulsion"),
    ("chemical_reduction", r"reduction|réduction|reducing|borohydride|citrate"),
    ("etching/exfoliation", r"etch|exfoliat|delamin|intercalat"),
    ("gelation/crosslinking", r"gelation|gélification|dripping|cross-?link|ionotrop"),
    ("loading/surface_modification", r"adsorption|loading|encapsul|conjugat|immobili|functionali|grafting|coating of|decorat|anchor|association"),
    ("physical_mixing", r"physical mix|mixing|blend|mélange"),
    ("thermal_treatment/activation", r"calcin|anneal|recuit|sinter|activation|condensation thermique|thermal condensation|traitement thermique|heat treatment"),
    ("melt/laser/physical", r"melt|laser|ablation|arc|plasma"),
    ("room_temperature_solution", r"room temperature|température ambiante|ambient|aqueous|solution|stirring"),
    ("non_decrite", r"not described|non décrit|non décrite|not reported|non détaillé"),
]
METHOD_RE = [(c, re.compile(r, re.I)) for c, r in METHOD_RULES]
METHOD_MODIFIERS = [("template", r"templat|gabarit|micelle|surfactant|sacrificial"), ("calcination", r"calcin|anneal|recuit|sinter")]

# Équivalences mot-clé ↔ signature d'étapes, pour la concordance.
EQUIV = {
    "hydrothermal": {"hydro/solvothermal"}, "solvothermal": {"hydro/solvothermal"},
    "hot-injection": {"hot-injection", "solution_heated"}, "microwave": {"microwave", "hydro/solvothermal", "solution_heated"},
    "sonochemical": {"sonochemical", "solution_RT"}, "mechanochemical": {"mechanochemical", "solid-state"},
    "CVD/ALD/PVD": {"vapour_deposition", "film_deposition"}, "electrochemical": {"electrochemical"},
    "film_deposition": {"film_deposition"}, "sol-gel": {"solution+calcination", "solution_heated", "solution_RT"},
    "combustion/pyrolysis": {"solution+calcination", "pyrolysis", "solid-state"}, "solid-state": {"solid-state", "pyrolysis"},
    "green/bio": {"solution_RT", "solution_heated"}, "precipitation/co-precipitation": {"solution_RT", "solution_heated", "solution+calcination"},
    "reflux/heating_in_solution": {"solution_heated", "solution+calcination"}, "ion_exchange/impregnation": {"solution_RT", "solution_heated", "solution+calcination"},
    "polymerization": {"solution_RT", "solution_heated"}, "self-assembly": {"solution_RT", "film_deposition"},
    "room_temperature_solution": {"solution_RT"}, "thermal_treatment/activation": {"solution+calcination", "solid-state", "pyrolysis"},
    "micellar/emulsion": {"solution_RT", "solution_heated"}, "chemical_reduction": {"solution_RT", "solution_heated"}, "etching/exfoliation": {"solution_RT", "solution_heated", "sonochemical"},
    "gelation/crosslinking": {"solution_RT", "solution_heated"}, "loading/surface_modification": {"solution_RT", "solution_heated"}, "physical_mixing": {"solution_RT", "mechanochemical"},
    "melt/laser/physical": {"autre", "solid-state", "vapour_deposition"},
}

SOLVENT_RULES = [("water", r"water|aqueous|h2o|eau"), ("ethanol", r"ethanol|éthanol|etoh"), ("methanol", r"methanol|méthanol|meoh"),
    ("isopropanol", r"isopropanol|2-propanol|ipa\b"), ("DMF", r"dimethylformamide|\bdmf\b"), ("DMSO", r"dimethyl sulfoxide|dimethylsulfoxide|\bdmso\b"),
    ("NMP", r"pyrrolid|\bnmp\b"), ("toluene", r"toluene|toluène"), ("hexane/alkanes", r"hexane|heptane|octane|cyclohexane"),
    ("octadecene", r"octadecene|\bode\b"), ("ethylene_glycol/polyols", r"ethylene glycol|glycerol|diethylene|polyol|propanediol|butanediol"),
    ("acetone", r"acetone|acétone"), ("chloroform/DCM", r"chloroform|dichloromethane|\bdcm\b"), ("acetonitrile", r"acetonitrile"),
    ("THF", r"tetrahydrofuran|\bthf\b"), ("chlorobenzene/DCB", r"chlorobenzene|dichlorobenzene"), ("ethyl_acetate", r"ethyl acetate"),
    ("ionic_liquid/deep_eutectic", r"ionic liquid|imidazolium|eutectic"), ("oleylamine/oleic", r"oleylamine|oleic"),
    ("acid_medium", r"acid|acide|hcl|hno3|h2so4"), ("alkoxyethanol", r"methoxyethanol|ethoxyethanol")]
SOLVENT_RE = [(c, re.compile(r, re.I)) for c, r in SOLVENT_RULES]

ATMOS_RULES = [("inerte", r"argon|\bar\b|nitrogen|\bn2\b|inert|glove|helium|schlenk"), ("vide", r"vacuum|vide|evacuated"),
    ("reductrice", r"\bh2\b|hydrogen|forming gas|nh3|ammonia"), ("oxydante", r"\bo2\b|oxygen|ozone|plasma"),
    ("air", r"\bair\b|ambient|atmospher|open"), ("gaz_reactif", r"h2s|ch4|acetylene|c2h2|co2|sulfur|chlorine")]
ATMOS_RE = [(c, re.compile(r, re.I)) for c, r in ATMOS_RULES]

LIMITE_RULES = [
    ("incoherence_interne", r"incoh[ée]ren|incompatible|contredi|contradict|diverge|ne concorde|écart entre|(texte|résumé|conclusion)[^.]{0,40}(figure|tableau|légende|méthodes)|(figure|tableau|légende)[^.]{0,40}texte|deux valeurs|selon (la|le) (section|figure|tableau)"),
    ("non_reproductible_tel_quel", r"(non|pas|im)[- ]?(re)?productible|ne peut (pas )?(être )?(refait|reproduit)|irréalisable|impossible à (refaire|préparer|reproduire)|ne se refait pas|ne peut pas être (préparé|suivi)"),
    ("bilan_matiere_stoechiometrie", r"st[oœ]chiom|bilan de mati|bilan massique|équivalent|en (large )?excès|rapport molaire|solubilit|mmol"),
    ("preuve_non_discriminante", r"discriminant|ne prouve|non prouv|non démontr|pas démontr|ne démontre|ne permet pas de (conclure|distinguer|trancher|savoir)|(aucun|sans|pas de) témoin|non (mesur|vérifi)|pas mesur"),
    ("valeur_hors_plage", r"hors (du )?(domaine|plage)|physiquement|impossible|au-dessus (de la|du) (solubilit|théorique|maximum)|dépasse|supérieur[e]? (à|au) (la |le )?(théor|maximum|limite)|invraisembl"),
    ("conditions_manquantes", r"(temp[ée]rature|dur[ée]e|atmosph|pression|vitesse|rampe|agitation|\bph\b|puissance|fr[ée]quence|centrifug|séchage|lavage)[^.]{0,80}(non (donn|indiqu|précis|cit|écrit|dit)|absent|manqu|pas (donn|indiqu|précis|dit))|(non|pas) (donn|indiqu|précis)[ée]e?s?[^.]{0,40}(temp[ée]rature|dur[ée]e|atmosph)"),
    ("quantites_manquantes", r"(quantit|masse|volume|concentration|rendement|échelle|fournisseur|puret)[^.]{0,80}(non (donn|indiqu|précis|cit|dit)|absent|manqu|pas (donn|indiqu|précis|dit))|aucune quantit|sans quantit"),
    ("unite_ou_lecture_ambigue", r"unit[ée]|ambigu|facteur \d|coquille|erreur (de recopie|typographique)|probable erreur|lu[es]? sur (la |une |l.)?(figure|image|courbe)|lecture (de|sur) figure|approximati|arrondi"),
    ("produit_non_decrit", r"commercial|non décrit|pas décrit|non détaill|(préparation|protocole|synthèse)[^.]{0,30}(n.est pas|non) (décri|donn)|travail antérieur|référence \[|cité d.un autre|d.après (la )?réf|renvoi"),
    ("annexe_absente", r"annexe|supporting|\bsi\b|figures? s\d|tableau s\d"),
    ("securite", r"sécurit|toxi|danger|explos|inflamm|ph3|\bhf\b|cyanure|corros"),
    ("interpretation_contestee", r"interpr[ée]t|conclusion|affirm|revendiqu|surinterpr|non soutenu|pas soutenu|attribu[ée]e? (à|au)|hypothèse|présenté comme|contrairement|alors que"),
    ("calcul_du_critique", r"calcul|≈|surestim|sous-estim|intégrale|facteur|recalcul|d.après [A-Z][a-z]+ et al"),
    ("figures_lues", r"figures? lues?|lu[es]? sur|histogramme|bandeau|lecture"),
    ("heritage_entre_voies", r"hérit|même procédure|même protocole|par renvoi|séries"),
]
LIMITE_RE = [(c, re.compile(r, re.I)) for c, r in LIMITE_RULES]

# Propriétés qu'un chimiste attend par famille (canoniques).
EXPECTED = {
    "MOF": ["phase", "BET_surface_area", "pore_volume_total", "yield", "crystallite_size", "decomposition_temperature"],
    "zeolithe": ["phase", "BET_surface_area", "crystallinity", "particle_size", "elemental_composition", "micropore_volume"],
    "perovskite": ["phase", "band_gap", "PL_emission_peak", "quantum_yield", "particle_size", "FWHM"],
    "quantum_dot": ["particle_size", "PL_emission_peak", "quantum_yield", "FWHM", "absorption_peak", "band_gap"],
    "nanoparticule_metallique": ["particle_size", "absorption_peak", "morphology", "zeta_potential", "phase", "hydrodynamic_size"],
    "oxyde": ["phase", "crystallite_size", "band_gap", "BET_surface_area", "morphology", "particle_size"],
    "chalcogenure": ["phase", "band_gap", "particle_size", "crystallite_size", "morphology", "absorption_peak"],
    "carbone": ["BET_surface_area", "raman_ID_IG", "morphology", "elemental_composition", "pore_volume_total", "quantum_yield"],
    "batterie": ["specific_capacity", "capacity_retention", "coulombic_efficiency", "phase", "particle_size", "morphology"],
    "ceramique": ["phase", "density", "crystallite_size", "hardness", "particle_size", "morphology"],
    "materiau_2D": ["thickness_layers", "phase", "raman_band", "morphology", "d_spacing", "band_gap"],
    "silice_mesoporeuse": ["BET_surface_area", "pore_diameter", "pore_volume_total", "particle_size", "morphology", "xrd_peak_position"],
    "composite": ["phase", "morphology", "BET_surface_area", "elemental_composition", "particle_size", "band_gap"],
    "nitrure": ["phase", "band_gap", "BET_surface_area", "morphology", "crystallite_size", "elemental_composition"],
    "carbure": ["phase", "crystallite_size", "morphology", "particle_size", "elemental_composition", "BET_surface_area"],
    "phosphure": ["phase", "particle_size", "morphology", "crystallite_size", "band_gap", "elemental_composition"],
    "autre": ["phase", "morphology", "particle_size", "yield", "elemental_composition", "BET_surface_area"],
}

ELEM_RE = re.compile(r"(?<![a-z])(He|Li|Be|Ne|Na|Mg|Al|Si|Cl|Ar|Ca|Sc|Ti|Cr|Mn|Fe|Co|Ni|Cu|Zn|Ga|Ge|As|Se|Br|Kr|Rb|Sr|Zr|Nb|Mo|Tc|Ru|Rh|Pd|Ag|Cd|In|Sn|Sb|Te|Xe|Cs|Ba|La|Ce|Pr|Nd|Pm|Sm|Eu|Gd|Tb|Dy|Ho|Er|Tm|Yb|Lu|Hf|Ta|Re|Os|Ir|Pt|Au|Hg|Tl|Pb|Bi|Th|U|B|C|N|O|F|P|S|K|V|Y|I|W|H)(?![a-z])")




def canon_from(rules, text, default):
    if not text:
        return default
    for c, r in rules:
        if r.search(text):
            return c
    return "autre"


def norm_unit(u):
    if not u:
        return ""
    u = u.replace("−", "-").replace("–", "-").replace("⁻", "-").replace("²", "2").replace("³", "3").replace("℃", "°C").replace("μ", "µ")
    u = re.sub(r"[·∙⋅.\s]+", "", u)
    u = re.sub(r"-(g|L|mL|cm2|m2|kg|h|s|min)-1$", r"/\1", u)
    u = re.sub(r"(?<=[A-Za-zµ])(g|L|mL|cm2|m2|kg)-1$", r"/\1", u)
    u = re.sub(r"^(m2|cm3|cm2|mAh|mmol|mg|µmol|mL|ml|mol|g|mA|F|W|S|mg)g-1$", r"\1/g", u)
    return u


def to_hours(v, u):
    u = (u or "").lower()
    if v is None:
        return None
    if u.startswith("h"):
        return v
    if u.startswith("min"):
        return v / 60
    if u in ("s", "sec", "seconds", "second"):
        return v / 3600
    if u.startswith("d"):
        return v * 24
    if u.startswith("week"):
        return v * 168
    return None


def to_celsius(v, u):
    if v is None:
        return None
    if u == "K":
        return v - 273.15
    return v


def pct(a, b):
    return round(100.0 * a / b, 1) if b else None


def quantiles(xs):
    xs = sorted(xs)
    if not xs:
        return (None, None, None)
    n = len(xs)
    def q(p):
        return xs[min(n - 1, int(p * n))]
    return (q(0.1), statistics.median(xs), q(0.9))


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="synthese.db")
    ap.add_argument("--out", default="docs/audit_contenu/data")
    ap.add_argument("--sources", default="docs/audit_contenu/sources")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    c = sqlite3.connect(a.db)
    q = lambda s, *p: c.execute(s, p).fetchall()
    D = {}

    papers = {r[0]: dict(id=r[0], pmcid=r[1], year=r[2], journal=r[3], family_query=r[4], title=r[5], doi=r[6])
              for r in q("select id,pmcid,year,journal,family_query,title,doi from papers where critic_status='done'")}
    P = tuple(papers)
    PIN = "(" + ",".join(map(str, P)) + ")"
    routes = {}
    for r in q(f"select r.id,r.paper_id,r.parent_route_id,r.branch_label,r.kind,r.method,r.completeness_score,r.succeeded,r.yield_value,r.yield_unit,m.family,m.name,m.formula from synthesis_routes r left join materials m on m.id=r.material_id where r.paper_id in {PIN}"):
        routes[r[0]] = dict(id=r[0], paper_id=r[1], parent=r[2], label=r[3], kind=r[4], method=r[5] or "", completeness=r[6], succeeded=r[7], yield_value=r[8], yield_unit=r[9], family=r[10] or "autre", material=r[11], formula=r[12])
    children = collections.defaultdict(list)
    for r in routes.values():
        if r["parent"]:
            children[r["parent"]].append(r["id"])

    def tree(rid):
        out = [rid]
        for ch in children.get(rid, []):
            out += tree(ch)
        return out

    def ancestors(rid):
        out = [rid]
        while routes[rid]["parent"]:
            rid = routes[rid]["parent"]
            out.append(rid)
        return out

    steps = collections.defaultdict(list)
    for sid, rid, order, action in q("select id,route_id,step_order,action from steps"):
        if rid in routes:
            steps[rid].append((order, sid, action or ""))
    for rid in steps:
        steps[rid].sort()
    params = collections.defaultdict(list)
    for sid, name, vn, vt, unit in q("select step_id,name,value_num,value_text,unit from parameters"):
        params[sid].append((name or "", vn, vt, unit))
    equip = collections.defaultdict(list)
    for sid, t in q("select step_id,type from equipment"):
        equip[sid].append((t or "").lower())
    reagents = collections.defaultdict(list)
    for rid, name, formula, role, amount, unit, atext in q("select route_id,name,formula,role,amount,unit,amount_text from reagents"):
        if rid in routes:
            reagents[rid].append(dict(name=name or "", formula=formula or "", role=role or "", amount=amount, unit=unit, atext=atext))
    outcomes = collections.defaultdict(list)
    for rid, prop, vn, vt, unit, quote, fig in q("select route_id,property,value_num,value_text,unit,quote,from_figure from outcomes"):
        if rid in routes:
            cp, grp = canon_prop(prop)
            outcomes[rid].append(dict(raw=prop or "", canon=cp, group=grp, vn=vn, vt=vt, unit=unit, nunit=norm_unit(unit), quote=quote or "", fig=fig))
    annots = collections.defaultdict(list)
    paper_annots = collections.defaultdict(list)
    for pid, rid, typ, text in q(f"select paper_id,route_id,type,text from annotations where paper_id in {PIN}"):
        (annots[rid] if rid else paper_annots[pid]).append((typ, text or ""))
    not_stated = collections.defaultdict(list)
    for rid, scope, name in q("select route_id,scope,name from not_stated"):
        if rid in routes:
            not_stated[rid].append((scope, name))
    plaus = {r[0]: (r[1], r[2]) for r in q("select route_id,verdict,feasibility from plausibility")}

    base = [r for r in routes.values() if r["parent"] is None and r["kind"] == "material"]
    base_ids = {r["id"] for r in base}

    # ------------------------------------------------ vue d'ensemble
    nroutes = len(routes)
    D["overview"] = [dict(
        publications=len(papers), voies=nroutes, voies_base=sum(1 for r in routes.values() if r["parent"] is None), branches=sum(1 for r in routes.values() if r["parent"]),
        voies_materiau=sum(1 for r in routes.values() if r["kind"] == "material"), voies_intermediaire=sum(1 for r in routes.values() if r["kind"] == "intermediate"),
        voies_post_traitement=sum(1 for r in routes.values() if r["kind"] == "post_treatment"), voies_dispositif=sum(1 for r in routes.values() if r["kind"] == "device"),
        voies_base_materiau=len(base), etapes=sum(len(v) for v in steps.values()), reactifs=sum(len(v) for v in reagents.values()),
        parametres=sum(len(params[s[1]]) for v in steps.values() for s in v), resultats=sum(len(v) for v in outcomes.values()),
        resultats_numeriques=sum(1 for v in outcomes.values() for o in v if o["vn"] is not None), resultats_lus_sur_figure=sum(1 for v in outcomes.values() for o in v if o["fig"]),
        noms_de_proprietes_bruts=len({o["raw"] for v in outcomes.values() for o in v}), proprietes_canoniques=len({o["canon"] for v in outcomes.values() for o in v}),
        caracterisations=q(f"select count(*) from characterizations where route_id in (select id from synthesis_routes where paper_id in {PIN})")[0][0],
        annotations=sum(len(v) for v in annots.values()) + sum(len(v) for v in paper_annots.values()),
        limites_reproductibilite=sum(1 for v in list(annots.values()) + list(paper_annots.values()) for t, _ in v if t == "limite_reproductibilite"),
        doutes=q(f"select count(*) from doubts where paper_id in {PIN}")[0][0], doutes_ouverts=q(f"select count(*) from doubts where paper_id in {PIN} and status='open'")[0][0],
        constats_fidelite=q(f"select count(*) from critiques where paper_id in {PIN}")[0][0], constats_faux=q(f"select count(*) from critiques where paper_id in {PIN} and severity='faux'")[0][0],
        jugements_scientifiques=len(plaus), cases_non_citees=sum(len(v) for v in not_stated.values()),
        citations_verifiees=q(f"select count(*) from outcomes where route_id in (select id from synthesis_routes where paper_id in {PIN}) and quote is not null and quote!=''")[0][0],
        genere_le=datetime.date.today().isoformat())]

    D["by_year"] = [dict(annee=y, publications=n) for y, n in sorted(collections.Counter(p["year"] for p in papers.values()).items()) if y]
    jc = collections.Counter((p["journal"] or "?").split(" (")[0] for p in papers.values())
    D["by_journal"] = [dict(revue=j, publications=n) for j, n in jc.most_common(20)]
    D["by_family_query"] = [dict(famille_requete=f, publications=n) for f, n in collections.Counter(p["family_query"] for p in papers.values()).most_common()]

    # per-route tree props, conditions
    def route_props(rid):
        s = set()
        for t in tree(rid):
            for o in outcomes[t]:
                s.add(o["canon"])
        return s

    def route_conditions(rid):
        ids = ancestors(rid)
        tmax, tstep, dur, nsteps, atm, autoclave, ph, stir, hr, conc, ratio, vol, press = None, None, 0.0, 0, [], False, None, None, None, 0, 0, None, None
        for r2 in ids:
            for order, sid, action in steps[r2]:
                nsteps += 1
                for t in equip[sid]:
                    if re.search(r"autoclave|teflon|bomb|pressure vessel|sealed tube", t):
                        autoclave = True
                for name, vn, vt, unit in params[sid]:
                    n = name.lower()
                    if n.startswith("temperature") and vn is not None:
                        v = to_celsius(vn, unit)
                        if v is not None and -200 < v < 4000 and (tmax is None or v > tmax):
                            tmax, tstep = v, action
                    elif n == "duration":
                        h = to_hours(vn, unit)
                        if h is not None:
                            dur += h
                    elif n == "atmosphere":
                        atm.append(vt or "")
                    elif n == "ph" and vn is not None:
                        ph = vn
                    elif n == "stirring_speed" and vn is not None:
                        stir = max(stir or 0, vn)
                    elif n == "heating_rate" and vn is not None:
                        hr = max(hr or 0, vn)
                    elif n == "concentration":
                        conc += 1
                    elif n == "molar_ratio":
                        ratio += 1
                    elif n == "volume" and vn is not None and unit:
                        u = unit.lower()
                        ml = vn if u in ("ml", "mL".lower()) else vn * 1000 if u == "l" else vn / 1000 if u in ("µl", "ul", "μl") else None
                        if ml is not None:
                            vol = max(vol or 0, ml)
                    elif n == "pressure" and vn is not None:
                        press = vn
                    if re.search(r"autoclave|teflon", (vt or ""), re.I):
                        autoclave = True
        atmc = sorted({canon_from(ATMOS_RE, x, "autre") for x in atm}) or ["non_cite"]
        atm1 = "inerte" if "inerte" in atmc else "vide" if "vide" in atmc else "reductrice" if "reductrice" in atmc else "oxydante" if "oxydante" in atmc else "gaz_reactif" if "gaz_reactif" in atmc else "air" if "air" in atmc else atmc[0]
        solv = [canon_from(SOLVENT_RE, g["name"], "autre") for r2 in ids for g in reagents[r2] if g["role"] == "solvent"]
        solv1 = solv[0] if solv else "aucun_solvant_declare"
        return dict(t_max_C=round(tmax, 1) if tmax is not None else None, etape_t_max=tstep, duree_totale_h=round(dur, 2) if dur else None, n_etapes=nsteps,
                    atmosphere=atm1, atmospheres=",".join(atmc), autoclave=autoclave, ph=ph, agitation_rpm=stir, rampe_C_min=hr, n_concentrations=conc, n_rapports_molaires=ratio, volume_max_mL=vol, pression=press, solvant=solv1, solvants=",".join(sorted(set(solv))))

    def signature(rid):
        ids = ancestors(rid)
        acts = [a for r2 in ids for _, _, a in steps[r2]]
        eq = [t for r2 in ids for _, sid, _ in steps[r2] for t in equip[sid]]
        txt = " ".join(acts) + " " + " ".join(eq)
        cond = route_conditions(rid)
        A = set(acts)
        if cond["autoclave"] or "hydrothermal" in A:
            return "hydro/solvothermal"
        if any(re.search(r"microwave", t) for t in eq):
            return "microwave"
        if A & {"electrodeposit", "anodize", "electrolyze", "charge", "discharge"} or any("potentiostat" in t or "electrochemical" in t for t in eq):
            return "electrochemical"
        if any(re.search(r"cvd|ald|pvd|sputter|evaporator|furnace tube.*flow", t) for t in eq) or A & {"sublime"} or ("deposit" in A and cond["t_max_C"] and cond["t_max_C"] >= 300 and not (A & {"dissolve", "add"})):
            return "vapour_deposition"
        if A & {"spin_coat", "drop_cast", "dip", "coat", "electrospin", "cast", "print", "spin"} or ("deposit" in A and A & {"dissolve", "add", "mix"} and not (A & {"calcine", "anneal", "sinter"} and len(A & {"dissolve", "add"}) == 0)) and "deposit" in A:
            return "film_deposition"
        if A & {"grind", "mill"} and not (A & {"dissolve", "add", "stir", "mix"} - {"mix"}) and not A & {"calcine", "sinter", "anneal"}:
            return "mechanochemical"
        if A & {"grind", "mill", "press", "sieve", "pelletize"} and A & {"calcine", "sinter", "anneal", "heat"} and not A & {"dissolve", "add", "stir"}:
            return "solid-state"
        if A & {"pyrolyze", "carbonize", "combust", "ignite"} or (A & {"calcine", "anneal", "heat"} and cond["t_max_C"] and cond["t_max_C"] >= 500 and A & {"dry"} and len(A & {"dissolve", "add", "stir", "mix"}) <= 1):
            return "pyrolysis"
        if "inject" in A and cond["t_max_C"] and cond["t_max_C"] >= 120:
            return "hot-injection"
        if A & {"calcine", "anneal", "sinter"} and A & {"dissolve", "add", "stir", "mix", "react"}:
            return "solution+calcination"
        if "sonicate" in A and not (A & {"heat", "reflux", "react"}) and (cond["t_max_C"] is None or cond["t_max_C"] <= 60):
            return "sonochemical"
        if A & {"dissolve", "add", "stir", "mix", "react", "reflux", "age", "precipitate"}:
            if cond["t_max_C"] is not None and cond["t_max_C"] > 60:
                return "solution_heated"
            return "solution_RT"
        return "autre"

    # ------------------------------------------------ synthèses
    rows_cond = []
    for r in base:
        rid = r["id"]
        m = r["method"]
        kw = next((c for c, rx in METHOD_RE if rx.search(m)), "non_classee")
        mods = [c for c, rx in METHOD_MODIFIERS if re.search(rx, m, re.I)]
        sig = signature(rid)
        cond = route_conditions(rid)
        props = route_props(rid)
        lim = sum(1 for t in tree(rid) for typ, _ in annots[t] if typ == "limite_reproductibilite")
        pv = plaus.get(rid, (None, None))
        y = r["yield_value"] if r["yield_unit"] in ("%", None) else None
        rows_cond.append(dict(route_id=rid, pmcid=papers[r["paper_id"]]["pmcid"], voie=r["label"], famille=r["family"], materiau=(r["material"] or "")[:60], formule=(r["formula"] or "")[:40],
                              methode_mot_cle=kw, modificateurs=",".join(mods), methode_signature=sig, concordance=sig in EQUIV.get(kw, set()),
                              **cond, n_branches=len(tree(rid)) - 1, n_resultats=sum(len(outcomes[t]) for t in tree(rid)), n_proprietes=len(props),
                              completude=round(r["completeness"], 2) if r["completeness"] is not None else None, n_non_cite=len(not_stated[rid]), n_limites=lim,
                              verdict_science=pv[0], faisabilite=pv[1], rendement_pct=y, annee=papers[r["paper_id"]]["year"]))
    D["voies"] = rows_cond
    D["methodes"] = [dict(methode=k, voies=n, part_pct=pct(n, len(base))) for k, n in collections.Counter(r["methode_mot_cle"] for r in rows_cond).most_common()]
    D["signatures"] = [dict(signature=k, voies=n, part_pct=pct(n, len(base))) for k, n in collections.Counter(r["methode_signature"] for r in rows_cond).most_common()]
    D["famille_methode"] = [dict(famille=f, methode=m, voies=n, trou=n < 5) for (f, m), n in sorted(collections.Counter((r["famille"], r["methode_mot_cle"]) for r in rows_cond).items())]
    D["concordance"] = [dict(methode=m, signature=s, voies=n, concordant=s in EQUIV.get(m, set())) for (m, s), n in sorted(collections.Counter((r["methode_mot_cle"], r["methode_signature"]) for r in rows_cond).items(), key=lambda x: -x[1])]
    D["kinds"] = [dict(kind=k, voies=n) for k, n in collections.Counter(r["kind"] for r in routes.values()).most_common()]
    fam_rows = []
    for f, n in collections.Counter(r["family"] for r in base).most_common():
        rs = [r for r in rows_cond if r["famille"] == f]
        allr = [r for r in routes.values() if r["family"] == f]
        pids = {routes[x["route_id"]]["paper_id"] for x in rs}
        comp = [x["completude"] for x in rs if x["completude"] is not None]
        fam_rows.append(dict(famille=f, publications=len(pids), voies_base=n, voies_toutes=len(allr), branches=sum(x["n_branches"] for x in rs), resultats=sum(x["n_resultats"] for x in rs),
                             completude_moyenne=round(statistics.mean(comp), 2) if comp else None, pct_voies_avec_limite=pct(sum(1 for x in rs if x["n_limites"]), n),
                             pct_douteuses=pct(sum(1 for x in rs if x["verdict_science"] in ("douteuse", "incoherente")), sum(1 for x in rs if x["verdict_science"])),
                             t_max_mediane=statistics.median([x["t_max_C"] for x in rs if x["t_max_C"] is not None]) if any(x["t_max_C"] is not None for x in rs) else None,
                             methode_principale=collections.Counter(x["methode_mot_cle"] for x in rs).most_common(1)[0][0]))
    D["by_family"] = fam_rows

    # ------------------------------------------------ propriétés
    allo = [(rid, o) for rid, v in outcomes.items() for o in v]
    prop_rows = []
    syn_rows = []
    grp_of = {}
    for cp, lst in collections.defaultdict(list, {k: [x for x in allo if x[1]["canon"] == k] for k in {o["canon"] for _, o in allo}}).items():
        raws = collections.Counter(o["raw"] for _, o in lst)
        units = collections.Counter(o["nunit"] for _, o in lst if o["vn"] is not None)
        mu, mun = units.most_common(1)[0] if units else ("", 0)
        grp_of[cp] = lst[0][1]["group"]
        prop_rows.append(dict(propriete=cp, groupe=lst[0][1]["group"], valeurs=len(lst), numeriques=sum(1 for _, o in lst if o["vn"] is not None), voies=len({rid for rid, _ in lst}),
                              publications=len({routes[rid]["paper_id"] for rid, _ in lst}), noms_bruts=len(raws), exemples_noms=", ".join(k for k, _ in raws.most_common(4)),
                              unite_principale=mu, pct_unite_principale=pct(mun, sum(units.values())), n_unites=len(units), familles=len({routes[rid]["family"] for rid, _ in lst})))
        for raw, n in raws.most_common():
            syn_rows.append(dict(propriete=cp, nom_brut=raw, valeurs=n))
    prop_rows.sort(key=lambda x: -x["valeurs"])
    D["proprietes"] = prop_rows
    D["synonymes"] = syn_rows
    D["groupes_proprietes"] = [dict(groupe=g, valeurs=n, proprietes=len({o["canon"] for _, o in allo if o["group"] == g})) for g, n in collections.Counter(o["group"] for _, o in allo).most_common()]
    fp = []
    byfp = collections.defaultdict(list)
    for rid, o in allo:
        if o["vn"] is not None:
            byfp[(routes[rid]["family"], o["canon"], o["nunit"])].append(o["vn"])
    for (f, cp, u), xs in byfp.items():
        if len(xs) >= 3:
            p10, med, p90 = quantiles(xs)
            fp.append(dict(famille=f, propriete=cp, groupe=grp_of[cp], unite=u, n=len(xs), min=min(xs), p10=p10, mediane=med, p90=p90, max=max(xs)))
    fp.sort(key=lambda x: (-x["n"]))
    D["famille_propriete"] = fp

    # ------------------------------------------------ conditions agrégées
    cond_rows = []
    for f in {r["famille"] for r in rows_cond} | {"toutes"}:
        rs = [r for r in rows_cond if f == "toutes" or r["famille"] == f]
        for metric, key in [("t_max_C", "t_max_C"), ("duree_totale_h", "duree_totale_h"), ("n_etapes", "n_etapes"), ("ph", "ph"), ("agitation_rpm", "agitation_rpm"), ("rampe_C_min", "rampe_C_min"), ("volume_max_mL", "volume_max_mL")]:
            xs = [r[key] for r in rs if r[key] is not None]
            if len(xs) >= 3:
                p10, med, p90 = quantiles(xs)
                cond_rows.append(dict(famille=f, metrique=metric, n=len(xs), couverture_pct=pct(len(xs), len(rs)), min=min(xs), p10=p10, mediane=med, p90=p90, max=max(xs)))
    D["conditions_famille"] = cond_rows
    D["atmospheres"] = [dict(famille=f, atmosphere=a, voies=n) for (f, a), n in sorted(collections.Counter((r["famille"], r["atmosphere"]) for r in rows_cond).items())]
    D["solvants"] = [dict(famille=f, solvant=s, voies=n) for (f, s), n in sorted(collections.Counter((r["famille"], r["solvant"]) for r in rows_cond).items())]
    D["methode_tmax"] = [dict(methode=m, n=len(xs), p10=quantiles(xs)[0], mediane=quantiles(xs)[1], p90=quantiles(xs)[2]) for m, xs in {m: [r["t_max_C"] for r in rows_cond if r["methode_mot_cle"] == m and r["t_max_C"] is not None] for m in {r["methode_mot_cle"] for r in rows_cond}}.items() if len(xs) >= 3]
    BINS = {"t_max_C": [(-300, 50, "<50"), (50, 100, "50–100"), (100, 150, "100–150"), (150, 200, "150–200"), (200, 300, "200–300"), (300, 500, "300–500"), (500, 800, "500–800"), (800, 1000, "800–1000"), (1000, 5000, ">1000")],
            "duree_totale_h": [(0, 1, "<1 h"), (1, 6, "1–6 h"), (6, 24, "6–24 h"), (24, 72, "1–3 j"), (72, 168, "3–7 j"), (168, 1e9, ">7 j")],
            "ph": [(-5, 2, "<2"), (2, 4, "2–4"), (4, 6, "4–6"), (6, 8, "6–8"), (8, 10, "8–10"), (10, 12, "10–12"), (12, 20, ">12")]}
    rng = []
    for f in {r["famille"] for r in rows_cond}:
        for metric, bins in BINS.items():
            xs = [r[metric] for r in rows_cond if r["famille"] == f and r[metric] is not None]
            for lo, hi, lab in bins:
                rng.append(dict(famille=f, metrique=metric, intervalle=lab, ordre=bins.index((lo, hi, lab)), voies=sum(1 for x in xs if lo <= x < hi), total=len(xs)))
    D["plages_conditions"] = rng

    # ------------------------------------------------ trous
    exp_rows = []
    for f, props in EXPECTED.items():
        rs = [r for r in base if r["family"] == f]
        if not rs:
            continue
        for p in props:
            have = sum(1 for r in rs if p in route_props(r["id"]))
            exp_rows.append(dict(famille=f, propriete=p, voies=len(rs), voies_avec=have, couverture_pct=pct(have, len(rs)), trou=pct(have, len(rs)) < 30))
    D["proprietes_attendues"] = exp_rows
    elem = collections.Counter()
    elem_f = collections.Counter()
    for r in base:
        s = set()
        for t in ancestors(r["id"]):
            for g in reagents[t]:
                if g["role"] in ("precursor", "dopant", "active_material", "intermediate"):
                    s |= set(ELEM_RE.findall(g["formula"] or ""))
        s |= set(ELEM_RE.findall(r["formula"] or ""))
        for e in s:
            elem[e] += 1
            elem_f[(e, r["family"])] += 1
    D["elements"] = [dict(element=e, voies=n, part_pct=pct(n, len(base))) for e, n in elem.most_common()]
    D["elements_famille"] = [dict(element=e, famille=f, voies=n) for (e, f), n in elem_f.most_common()]
    prec = collections.Counter()
    for r in base:
        for t in ancestors(r["id"]):
            for g in reagents[t]:
                if g["role"] == "precursor":
                    prec[re.sub(r"\s*\(.*?\)", "", g["name"]).strip().lower()[:50]] += 1
    D["precurseurs"] = [dict(precurseur=k, voies=n) for k, n in prec.most_common(60)]

    # ------------------------------------------------ qualité
    D["unites"] = [dict(propriete=cp, unite=u or "(sans unité)", valeurs=n) for (cp, u), n in sorted(collections.Counter((o["canon"], o["nunit"]) for _, o in allo if o["vn"] is not None).items(), key=lambda x: (x[0][0], -x[1]))]
    OUT_RULES = {"band_gap": ("eV", 0.05, 12, "band gap hors 0,05–12 eV"), "BET_surface_area": ("m2/g", 0.1, 8000, "surface BET hors 0,1–8 000 m2/g"), "quantum_yield": ("%", 0, 100.0001, "rendement quantique hors 0–100 %"),
                 "yield": ("%", 0, 100.0001, "rendement hors 0–100 %"), "particle_size": ("nm", 0.3, 100000, "taille hors 0,3 nm–100 µm"), "crystallite_size": ("nm", 0.5, 5000, "cristallite hors 0,5–5 000 nm"),
                 "pore_diameter": ("nm", 0.2, 1000, "pore hors 0,2–1 000 nm"), "zeta_potential": ("mV", -200, 200, "zêta hors ±200 mV"), "lattice_parameter_a": ("Å", 2, 100, "paramètre a hors 2–100 Å"), "lattice_parameter_c": ("Å", 2, 100, "paramètre c hors 2–100 Å"),
                 "PCE": ("%", 0, 50, "PCE hors 0–50 %"), "Voc": ("V", 0, 3, "Voc hors 0–3 V"), "fill_factor": ("%", 0, 100.0001, "FF hors 0–100 %"), "PL_emission_peak": ("nm", 200, 2500, "émission hors 200–2 500 nm"), "pore_volume_total": ("cm3/g", 0, 5, "volume poreux hors 0–5 cm3/g"), "coulombic_efficiency": ("%", 0, 100.5, "efficacité coulombique > 100 %")}
    outl = []
    for rid, o in allo:
        if o["vn"] is None or o["canon"] not in OUT_RULES:
            continue
        u, lo, hi, rule = OUT_RULES[o["canon"]]
        nu = o["nunit"]
        if nu != norm_unit(u) and not (o["canon"] in ("quantum_yield", "yield", "fill_factor", "coulombic_efficiency") and nu == ""):
            continue
        v = o["vn"]
        if o["canon"] in ("quantum_yield", "yield", "fill_factor", "coulombic_efficiency") and nu == "" and v <= 1.0001:
            continue
        if not (lo <= v <= hi):
            outl.append(dict(pmcid=papers[routes[rid]["paper_id"]]["pmcid"], voie=routes[rid]["label"], famille=routes[rid]["family"], propriete=o["canon"], nom_brut=o["raw"], valeur=v, unite=o["unit"] or "", regle=rule, citation=o["quote"][:160]))
    PAR_RULES = [("temperature", lambda v, u: to_celsius(v, u) is not None and not (-273 <= to_celsius(v, u) <= 3500), "température hors −273–3 500 °C"), ("ph", lambda v, u: not (0 <= v <= 14), "pH hors 0–14"),
                 ("duration", lambda v, u: v < 0, "durée négative"), ("heating_rate", lambda v, u: v > 1000, "rampe > 1 000 °C/min"), ("stirring_speed", lambda v, u: v > 30000, "agitation > 30 000 rpm"), ("centrifuge_speed", lambda v, u: (u or "").lower() == "rpm" and v > 100000, "centrifugation > 100 000 rpm")]
    for rid in routes:
        for order, sid, action in steps[rid]:
            for name, vn, vt, unit in params[sid]:
                if vn is None:
                    continue
                for pn, test, rule in PAR_RULES:
                    if name.lower().startswith(pn) and test(vn, unit):
                        outl.append(dict(pmcid=papers[routes[rid]["paper_id"]]["pmcid"], voie=routes[rid]["label"], famille=routes[rid]["family"], propriete="param:" + name, nom_brut=action, valeur=vn, unite=unit or "", regle=rule, citation=""))
    D["hors_plage"] = outl
    comp_bins = [(0, 0.4, "<0,4"), (0.4, 0.6, "0,4–0,6"), (0.6, 0.8, "0,6–0,8"), (0.8, 1.01, "≥0,8")]
    D["completude"] = [dict(famille=f, intervalle=lab, ordre=i, voies=sum(1 for r in rows_cond if r["famille"] == f and r["completude"] is not None and lo <= r["completude"] < hi)) for f in {r["famille"] for r in rows_cond} for i, (lo, hi, lab) in enumerate(comp_bins)]
    nsc = collections.Counter((s, n) for v in not_stated.values() for s, n in v)
    nroutes_grid = len([r for r in routes.values() if not_stated[r["id"]]])
    D["non_cite"] = [dict(portee=s, champ=n, occurrences=k, pct_voies=pct(len({rid for rid, v in not_stated.items() if (s, n) in v}), nroutes)) for (s, n), k in nsc.most_common(40)]
    # doublons
    keymat = collections.defaultdict(set)
    for r in base:
        key = (r["formula"] or "").replace(" ", "") or (r["material"] or "").split("(")[0].strip()
        if key:
            keymat[(key, r["family"])].add(r["id"])
    dup = []
    dupp = []
    for (key, f), rids in keymat.items():
        pids = {routes[x]["paper_id"] for x in rids}
        if len(pids) < 2:
            continue
        dup.append(dict(materiau=key, famille=f, publications=len(pids), voies_base=len(rids)))
        vals = collections.defaultdict(list)
        for x in rids:
            for t in tree(x):
                for o in outcomes[t]:
                    if o["vn"] is not None and o["canon"] in ("BET_surface_area", "band_gap", "particle_size", "crystallite_size", "quantum_yield", "PL_emission_peak", "pore_volume_total", "specific_capacity", "PCE"):
                        vals[(o["canon"], o["nunit"])].append((o["vn"], papers[routes[t]["paper_id"]]["pmcid"]))
        for (cp, u), xs in vals.items():
            if len({p for _, p in xs}) >= 2:
                v = [a for a, _ in xs]
                dupp.append(dict(materiau=key, famille=f, propriete=cp, unite=u, publications=len({p for _, p in xs}), n=len(v), min=min(v), mediane=statistics.median(v), max=max(v), rapport_max_min=round(max(v) / min(v), 1) if min(v) > 0 else None))
    dup.sort(key=lambda x: -x["publications"])
    dupp.sort(key=lambda x: -(x["rapport_max_min"] or 0))
    D["doublons"] = dup
    D["doublons_proprietes"] = dupp
    D["verdicts_science"] = [dict(famille=f, verdict=v, voies=n) for (f, v), n in sorted(collections.Counter((routes[rid]["family"], (pv[0] or "").replace("invérifiable", "inverifiable")) for rid, pv in plaus.items() if rid in routes).items())]
    D["faisabilite"] = [dict(faisabilite=v, voies=n) for v, n in collections.Counter(pv[1] for pv in plaus.values()).most_common()]
    D["critiques_fidelite"] = [dict(severite=s, statut=st, constats=n) for s, st, n in q(f"select severity,status,count(*) from critiques where paper_id in {PIN} group by 1,2 order by 3 desc")]

    # ------------------------------------------------ limites
    lim_rows = []
    for f in {r["family"] for r in routes.values()}:
        rs = [r for r in routes.values() if r["family"] == f]
        withl = sum(1 for r in rs if any(t == "limite_reproductibilite" for t, _ in annots[r["id"]]))
        lim_rows.append(dict(famille=f, voies=len(rs), voies_avec_limite=withl, pct=pct(withl, len(rs)), limites=sum(1 for r in rs for t, _ in annots[r["id"]] if t == "limite_reproductibilite")))
    lim_rows.sort(key=lambda x: -(x["pct"] or 0))
    D["limites_famille"] = lim_rows
    motifs = collections.Counter()
    motifs_f = collections.Counter()
    ex = {}
    texts = [(routes[rid]["family"], t) for rid, v in annots.items() for typ, t in v if typ == "limite_reproductibilite"] + [("(article)", t) for v in paper_annots.values() for typ, t in v if typ == "limite_reproductibilite"]
    for f, t in texts:
        cls = [c for c, r in LIMITE_RE if r.search(t)] or ["autre"]
        motifs[cls[0]] += 1
        motifs_f[(f, cls[0])] += 1
        ex.setdefault(cls[0], t[:200])
    D["limites_motifs"] = [dict(motif=m, limites=n, part_pct=pct(n, len(texts)), exemple=ex[m]) for m, n in motifs.most_common()]
    D["limites_motifs_famille"] = [dict(famille=f, motif=m, limites=n) for (f, m), n in motifs_f.most_common()]
    D["limites_methode"] = [dict(methode=m, voies=len(xs), pct_avec_limite=pct(sum(1 for x in xs if x["n_limites"]), len(xs)), limites_par_voie=round(sum(x["n_limites"] for x in xs) / len(xs), 2)) for m, xs in {m: [r for r in rows_cond if r["methode_mot_cle"] == m] for m in {r["methode_mot_cle"] for r in rows_cond}}.items() if len(xs) >= 5]

    # ------------------------------------------------ publications
    prow = []
    for pid, p in papers.items():
        rs = [r for r in routes.values() if r["paper_id"] == pid]
        bs = [r for r in rs if r["parent"] is None and r["kind"] == "material"]
        comp = [r["completeness"] for r in bs if r["completeness"] is not None]
        fam = collections.Counter(r["family"] for r in bs).most_common(1)
        prow.append(dict(pmcid=p["pmcid"], titre=(p["title"] or "")[:110], annee=p["year"], revue=(p["journal"] or "").split(" (")[0][:40], famille_requete=p["family_query"], famille=fam[0][0] if fam else "", voies=len(rs), voies_base=len(bs),
                         resultats=sum(len(outcomes[r["id"]]) for r in rs), completude=round(statistics.mean(comp), 2) if comp else None, limites=sum(1 for r in rs for t, _ in annots[r["id"]] if t == "limite_reproductibilite") + sum(1 for t, _ in paper_annots[pid] if t == "limite_reproductibilite"),
                         constats=q("select count(*) from critiques where paper_id=?", pid)[0][0], faux=q("select count(*) from critiques where paper_id=? and severity='faux'", pid)[0][0], doi=p["doi"] or ""))
    prow.sort(key=lambda x: x["pmcid"])
    D["publications"] = prow

    # ------------------------------------------------ sources externes (agents)
    mech = []
    for fn in ("mech_A_out.json", "mech_B_out.json", "mech_out.json"):
        fp_ = os.path.join(a.sources, fn)
        if os.path.exists(fp_):
            mech += json.load(open(fp_))
    if mech:
        fam_of = {}
        for m in mech:
            rid = m.get("route_id")
            m["famille"] = routes[rid]["family"] if rid in routes else "?"
            m["voie"] = routes[rid]["label"] if rid in routes else ""
            m["methode"] = next((x["methode_mot_cle"] for x in rows_cond if x["route_id"] in ancestors(rid)), "") if rid in routes else ""
        D["mecanismes"] = [dict(pmcid=m.get("pmcid"), voie=m["voie"], famille=m["famille"], methode=m["methode"], type_auteurs=m.get("type_auteurs"), type_critique=m.get("type_critique"), accord=m.get("accord"), motif=m.get("motif", ""), incompatibilite=bool(m.get("incompatibilite_conditions")), incompatibilite_motif=m.get("incompatibilite_motif", ""), fondateurs=", ".join(m.get("fondateurs") or []), fondateur_manquant=m.get("fondateur_manquant", "")) for m in mech]
        D["mecanismes_accord"] = [dict(famille=f, accord=ac, voies=n) for (f, ac), n in sorted(collections.Counter((m["famille"], m.get("accord")) for m in mech).items())]
        tc = collections.Counter()
        for m in mech:
            tc[(m["famille"], "auteurs", m.get("type_auteurs"))] += 1
            tc[(m["famille"], "critique", m.get("type_critique"))] += 1
        D["mecanismes_types"] = [dict(famille=f, source=s, type=t, voies=n) for (f, s, t), n in sorted(tc.items())]
        normf = lambda x: re.sub(r"\s*\(.*?\)\s*", " ", x or "").replace("et al.", "et al.").strip(" ,;")
        for m in mech:
            m["fondateurs"] = sorted({normf(x) for x in (m.get("fondateurs") or []) if normf(x)})
            m["fondateur_manquant"] = normf(m.get("fondateur_manquant"))
        fc = collections.Counter(x for m in mech for x in m["fondateurs"])
        fm = collections.Counter(m["fondateur_manquant"] for m in mech if m["fondateur_manquant"])
        D["mecanismes_fondateurs"] = [dict(fondateur=k, invoque=fc.get(k, 0), manquant=fm.get(k, 0)) for k in sorted(set(fc) | set(fm), key=lambda k: -(fc.get(k, 0) + fm.get(k, 0)))]
    refp = os.path.join(a.sources, "ref_out.json")
    if os.path.exists(refp):
        D["references_externes"] = json.load(open(refp))

    # ------------------------------------------------ résumé
    S = D["overview"][0].copy()
    S["part_autre"] = pct(sum(1 for _, o in allo if o["canon"] == "autre"), len(allo))
    S.update(dict(familles=len(fam_rows), methodes=len(D["methodes"]), voies_methode_non_classee=next((m["voies"] for m in D["methodes"] if m["methode"] == "non_classee"), 0),
                  concordance_pct=pct(sum(1 for r in rows_cond if r["concordance"]), len(rows_cond)), trous_famille_methode=sum(1 for r in D["famille_methode"] if r["trou"]),
                  proprietes_attendues_trous=sum(1 for r in exp_rows if r["trou"]), hors_plage=len(outl), doublons_materiaux=len(dup), unites_variantes=sum(1 for p in prop_rows if p["n_unites"] > 1 and p["numeriques"] >= 10),
                  pct_voies_avec_limite=pct(sum(1 for r in rows_cond if r["n_limites"]), len(rows_cond)), t_max_couverture_pct=pct(sum(1 for r in rows_cond if r["t_max_C"] is not None), len(rows_cond)),
                  mecanismes_compares=len(mech), mecanismes_desaccord=sum(1 for m in mech if m.get("accord") == "desaccord"), mecanismes_incompatibles=sum(1 for m in mech if m.get("incompatibilite_conditions")),
                  references_comparees=len(D.get("references_externes", [])), references_conformes=sum(1 for r in D.get("references_externes", []) if r.get("verdict") == "conforme")))
    D["summary"] = [S]
    for k, v in D.items():
        json.dump(v, open(os.path.join(a.out, k + ".json"), "w"), ensure_ascii=False, separators=(",", ":"))
    bundle(D, os.path.join(os.path.dirname(a.out.rstrip("/")), "dash"))
    print(json.dumps(S, ensure_ascii=False, indent=1))
    print({k: len(v) for k, v in D.items()})


def bundle(D, out):
    """Jeux de données regroupés pour le tableau de bord (moins de fichiers, colonnes homogènes)."""
    os.makedirs(out, exist_ok=True)
    B = {}
    B["resume"] = D["summary"]
    rep = []
    def add(table, rows, cle, n, pct=None, extra=None):
        for r in rows:
            rep.append(dict(table=table, cle=str(r[cle]), n=r[n], pct=r.get(pct) if pct else None, extra=(r.get(extra) if extra else None)))
    add("annee", D["by_year"], "annee", "publications"); add("revue", D["by_journal"], "revue", "publications"); add("famille_requete", D["by_family_query"], "famille_requete", "publications")
    add("kind", D["kinds"], "kind", "voies"); add("methode", D["methodes"], "methode", "voies", "part_pct"); add("signature", D["signatures"], "signature", "voies", "part_pct")
    add("groupe_propriete", D["groupes_proprietes"], "groupe", "valeurs", None, "proprietes"); add("faisabilite", D["faisabilite"], "faisabilite", "voies")
    for r in D["critiques_fidelite"]:
        rep.append(dict(table="critique_fidelite", cle=f"{r['severite']} / {r['statut']}", n=r["constats"], pct=None, extra=None))
    add("limite_motif", D["limites_motifs"], "motif", "limites", "part_pct", "exemple"); add("element", D["elements"], "element", "voies", "part_pct"); add("precurseur", D["precurseurs"], "precurseur", "voies")
    if "mecanismes_fondateurs" in D:
        for r in D["mecanismes_fondateurs"]:
            rep.append(dict(table="fondateur", cle=r["fondateur"], n=r["invoque"], pct=None, extra=r["manquant"]))
    B["repartition"] = rep
    B["familles"] = D["by_family"]
    cr = []
    def cross(table, rows, a_, b_, n, c=None, flag=None, ordre=None, total=None):
        for r in rows:
            cr.append(dict(table=table, a=str(r[a_]), b=str(r[b_]), c=str(r[c]) if c else "", n=r[n], flag=bool(r[flag]) if flag else None, ordre=r.get(ordre) if ordre else None, total=r.get(total) if total else None))
    cross("famille_methode", D["famille_methode"], "famille", "methode", "voies", flag="trou"); cross("concordance", D["concordance"], "methode", "signature", "voies", flag="concordant")
    cross("atmosphere", D["atmospheres"], "famille", "atmosphere", "voies"); cross("solvant", D["solvants"], "famille", "solvant", "voies"); cross("element_famille", D["elements_famille"], "element", "famille", "voies")
    cross("limite_motif_famille", D["limites_motifs_famille"], "famille", "motif", "limites"); cross("verdict_science", D["verdicts_science"], "famille", "verdict", "voies")
    cross("completude", D["completude"], "famille", "intervalle", "voies", ordre="ordre"); cross("plage_condition", D["plages_conditions"], "famille", "intervalle", "voies", c="metrique", ordre="ordre", total="total")
    cross("doublon", D["doublons"], "materiau", "famille", "publications", c="voies_base")
    if "mecanismes_accord" in D:
        cross("mecanisme_accord", D["mecanismes_accord"], "famille", "accord", "voies"); cross("mecanisme_type", D["mecanismes_types"], "famille", "type", "voies", c="source")
    B["croisements"] = cr
    B["voies"] = D["voies"]; B["publications"] = D["publications"]; B["proprietes"] = D["proprietes"]
    B["synonymes"] = [s for s in D["synonymes"] if s["valeurs"] >= 2 or s["propriete"] != "autre"][:6000]
    B["famille_propriete"] = D["famille_propriete"]
    B["conditions"] = [dict(table="famille", groupe=r["famille"], **{k: r[k] for k in ("metrique", "n", "couverture_pct", "min", "p10", "mediane", "p90", "max")}) for r in D["conditions_famille"]] + \
                      [dict(table="methode", groupe=r["methode"], metrique="t_max_C", n=r["n"], couverture_pct=None, min=None, p10=r["p10"], mediane=r["mediane"], p90=r["p90"], max=None) for r in D["methode_tmax"]]
    B["attendues"] = D["proprietes_attendues"]; B["unites"] = D["unites"]; B["hors_plage"] = D["hors_plage"]; B["non_cite"] = D["non_cite"]; B["doublons"] = D["doublons_proprietes"]
    B["limites"] = [dict(table="famille", groupe=r["famille"], voies=r["voies"], pct=r["pct"], limites=r["limites"], limites_par_voie=round(r["limites"] / r["voies"], 2) if r["voies"] else None) for r in D["limites_famille"]] + \
                   [dict(table="methode", groupe=r["methode"], voies=r["voies"], pct=r["pct_avec_limite"], limites=None, limites_par_voie=r["limites_par_voie"]) for r in D["limites_methode"]]
    if "mecanismes" in D:
        B["mecanismes"] = D["mecanismes"]
    if "references_externes" in D:
        B["references"] = D["references_externes"]
    for k, v in B.items():
        json.dump(v, open(os.path.join(out, k + ".json"), "w"), ensure_ascii=False, separators=(",", ":"))
    print("dash:", {k: len(v) for k, v in B.items()})


if __name__ == "__main__":
    main()
