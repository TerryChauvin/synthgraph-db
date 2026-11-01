#!/usr/bin/env python3
"""Vitrine du dépôt : graphiques SVG (docs/img/), page à onglets FR/EN pour GitHub Pages (docs/index.html)
et blocs « Analyse » des README. Tout vient des jeux de données de docs/audit_contenu/data/ (produits par
analyses/audit_contenu.py, audit_parametres.py, audit_verification.py, compare_blind.py) : relancer après toute mise à jour.

Usage : python3 -I analyses/build_site.py
Sorties : docs/img/<graphique>_<fr|en>.svg ; docs/index.html ; blocs entre <!-- SITE:... --> dans README.md et README.fr.md.
Sans dépendance (SVG écrit à la main). Le texte est écrit une fois, rendu en HTML et en Markdown."""
import os, sys, json, re, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
os.chdir(ROOT)
DATA = "docs/audit_contenu/data/"
IMG = "docs/img/"
GH = "https://github.com/TerryChauvin/synthgraph-multi-agent-cloud"
PAGES = "https://terrychauvin.github.io/synthgraph-multi-agent-cloud/"

L = lambda k: json.load(open(DATA + k + ".json"))
S = L("summary")[0]

# ------------------------------------------------------------------ constantes de lecture (rapports de palier)
# palier : (citations vérifiées, valeurs relues à la main, fausses, médiane de constats de fidélité, constats « faux », constats)
PALIERS = [(8712, 1307, 10, 10, 29, 526), (8796, 776, 0, 8, 7, 403), (10050, 981, 0, 8.5, 5, 435), (9920, 529, 0, 8, 7, 406), (9581, 1112, 0, 8, 4, 428),
           (9680, 1887, 0, 8, 3, 419), (9238, 1032, 2, 8, 9, 421), (9859, 1181, 1, 9, 11, 437), (9719, 1258, 0, 8.5, 4, 424), (9498, 1222, 3, 9, 11, 446)]
QUOTES = sum(p[0] for p in PALIERS); RELUES = sum(p[1] for p in PALIERS); FAUSSES = sum(p[2] for p in PALIERS)
KPI = dict(quotes=QUOTES, relues=RELUES, fausses=FAUSSES, blind=[r for r in L("verif_reextraction") if r["pmcid"] == "TOTAL"][0]["precision_params"])

# titres courts des cartes de la grille d'accueil
SHORT = {"Types de synthèse (classement par mots-clés de la méthode)": "Types de synthèse", "Synthesis types (keyword classification of the method)": "Synthesis types",
         "Mécanisme de formation : auteurs contre critique scientifique": "Mécanisme : auteurs / critique", "Formation mechanism: authors vs. science reviewer": "Mechanism: authors vs. reviewer",
         "Base contre plages de référence relevées sur le web": "Base contre la littérature", "Database vs. reference ranges found on the web": "Database vs. literature ranges",
         "Voies de base de matériau par famille": "Voies de base par famille", "Propriétés attendues les moins renseignées": "Propriétés attendues manquantes",
         "Branches sans résultat ni caractérisation": "Branches sans résultat", "Branches with no outcome or characterization": "Branches with no outcome",
         "Motifs des limites de reproductibilité": "Limites de reproductibilité", "Reasons for reproducibility limits": "Reproducibility limits",
         "Ré-extraction à l'aveugle de 20 publications": "Ré-extraction à l'aveugle (20)", "Blind re-extraction of 20 papers": "Blind re-extraction (20 papers)"}

# ------------------------------------------------------------------ libellés
FAM = {"composite": ("composite", "composite"), "oxyde": ("oxyde", "oxide"), "perovskite": ("pérovskite", "perovskite"), "MOF": ("MOF", "MOF"), "nanoparticule_metallique": ("nanoparticule métallique", "metal nanoparticle"),
       "chalcogenure": ("chalcogénure", "chalcogenide"), "autre": ("autre", "other"), "quantum_dot": ("quantum dot", "quantum dot"), "zeolithe": ("zéolithe", "zeolite"), "carbone": ("carbone", "carbon"),
       "ceramique": ("céramique", "ceramic"), "batterie": ("batterie", "battery"), "silice_mesoporeuse": ("silice mésoporeuse", "mesoporous silica"), "materiau_2D": ("matériau 2D", "2D material"),
       "nitrure": ("nitrure", "nitride"), "carbure": ("carbure", "carbide"), "phosphure": ("phosphure", "phosphide")}
METH = {"hydrothermal": ("hydrothermal", "hydrothermal"), "precipitation/co-precipitation": ("précipitation", "precipitation"), "sol-gel": ("sol-gel", "sol-gel"), "solvothermal": ("solvothermal", "solvothermal"),
        "non_classee": ("non classée", "unclassified"), "green/bio": ("voie verte / bio", "green / bio"), "film_deposition": ("dépôt de film", "film deposition"), "chemical_reduction": ("réduction chimique", "chemical reduction"),
        "room_temperature_solution": ("solution à T ambiante", "room-temperature solution"), "hot-injection": ("injection à chaud", "hot injection"), "ion_exchange/impregnation": ("échange ionique / imprégnation", "ion exchange / impregnation"),
        "reflux/heating_in_solution": ("reflux / chauffage", "reflux / heating"), "thermal_treatment/activation": ("traitement thermique", "thermal treatment"), "mechanochemical": ("mécanochimie", "mechanochemistry"),
        "sonochemical": ("sonochimie", "sonochemistry"), "CVD/ALD/PVD": ("CVD / ALD / PVD", "CVD / ALD / PVD"), "microwave": ("micro-ondes", "microwave"), "combustion/pyrolysis": ("combustion / pyrolyse", "combustion / pyrolysis"),
        "physical_mixing": ("mélange physique", "physical mixing"), "polymerization": ("polymérisation", "polymerization"), "solid-state": ("réaction solide-solide", "solid-state"), "loading/surface_modification": ("chargement / greffage", "loading / grafting")}
PROP = {"BET_surface_area": ("surface BET", "BET surface area"), "phase": ("phase cristalline", "crystalline phase"), "pore_volume_total": ("volume poreux", "pore volume"), "yield": ("rendement", "yield"), "decomposition_temperature": ("T de décomposition", "decomposition T"),
        "band_gap": ("band gap", "band gap"), "quantum_yield": ("rendement quantique", "quantum yield"), "FWHM": ("largeur à mi-hauteur", "FWHM"), "crystallite_size": ("taille de cristallite", "crystallite size"), "absorption_peak": ("pic d'absorption", "absorption peak"),
        "morphology": ("morphologie", "morphology"), "coulombic_efficiency": ("efficacité coulombique", "coulombic efficiency"), "capacity_retention": ("rétention de capacité", "capacity retention"), "density": ("densité", "density"),
        "hardness": ("dureté", "hardness"), "particle_size": ("taille de particule", "particle size"), "thickness_layers": ("épaisseur / couches", "thickness / layers"), "raman_band": ("bande Raman", "Raman band"), "d_spacing": ("distance interréticulaire", "d-spacing"),
        "xrd_peak_position": ("position des pics DRX", "XRD peak position"), "elemental_composition": ("composition élémentaire", "elemental composition"), "specific_capacity": ("capacité spécifique", "specific capacity"), "raman_ID_IG": ("rapport Raman ID/IG", "Raman ID/IG")}
MOTIF = {"incoherence_interne": ("incohérence interne de l'article", "internal inconsistency in the paper"), "preuve_non_discriminante": ("preuve non discriminante", "non-discriminating evidence"), "interpretation_contestee": ("interprétation contestée", "interpretation contested"),
         "bilan_matiere_stoechiometrie": ("bilan de matière / stœchiométrie", "mass balance / stoichiometry"), "annexe_absente": ("annexe absente du dépôt", "supplement not in repository"), "conditions_manquantes": ("conditions manquantes", "missing conditions"),
         "quantites_manquantes": ("quantités manquantes", "missing amounts"), "unite_ou_lecture_ambigue": ("unité ou lecture ambiguë", "ambiguous unit or reading"), "calcul_du_critique": ("recalcul du critique", "reviewer's recalculation"),
         "valeur_hors_plage": ("valeur hors plage", "out-of-range value"), "produit_non_decrit": ("produit non décrit", "product not described"), "non_reproductible_tel_quel": ("non reproductible tel quel", "not reproducible as written"), "securite": ("sécurité", "safety")}
VERD = {"conforme": ("conforme", "within range"), "plus_large": ("plus large", "wider"), "plus_bas": ("plus bas", "lower"), "plus_haut": ("plus haut", "higher"), "non_trouve": ("pas de référence", "no reference")}
ACC = {"accord": ("accord", "agreement"), "nuance": ("nuance", "nuanced"), "desaccord": ("désaccord", "disagreement")}
lab = lambda d, k, i: d[k][i] if k in d else str(k).replace("_", " ")

# ------------------------------------------------------------------ mise en forme des nombres
def n(x, lg, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", " ") if lg == 0 else s
def p(x, lg, dec=1):
    s = f"{x:.{dec}f}"
    return (s.replace(".", ",") + " %") if lg == 0 else s + "%"

# ------------------------------------------------------------------ SVG
FG, MUT = "#1d2a30", "#5b6b73"
STYLE = ("<style>.bg{fill:#f3f6f7;stroke:#d5dde0}.tx{fill:#1d2a30}.mut{fill:#5b6b73}.gl{stroke:#d5dde0}.c1{fill:#17707f}.c2{fill:#c27c0e}.c3{fill:#a8412f}.c4{fill:#3f7d4e}.c5{fill:#9fb3bb}"
         "text{font-family:'Source Sans 3',system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;font-size:13px}.t{font-size:15px;font-weight:600}</style>")

# variante sombre (README GitHub : <picture> + prefers-color-scheme)
STYLE_DARK = (STYLE.replace("#f3f6f7", "#161b22").replace("#d5dde0", "#30363d").replace("#1d2a30", "#e6edf3").replace("#5b6b73", "#9198a1")
              .replace("#17707f", "#3a9fb0").replace("#c27c0e", "#d18f1f").replace("#a8412f", "#c9583f").replace("#3f7d4e", "#4f9a62").replace("#9fb3bb", "#5d7079"))

def esc(s): return html.escape(str(s), quote=False)

def frame(w, h, title, sub, body, standalone):
    head = f'<text class="tx t" x="16" y="26">{esc(title)}</text>' + (f'<text class="mut" x="16" y="44" font-size="12">{esc(sub)}</text>' if sub else "")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(title)}">'
            f'{STYLE if standalone else ""}<rect class="bg" x=".5" y=".5" width="{w-1}" height="{h-1}" rx="6"/>{head}{body}</svg>')

def trunc(s, k): return s if len(s) <= k else s[:k - 1] + "…"

def bars(items, title, sub, standalone, w=760, labw=230, fmt=None, vmax=None):
    """items : (libellé, valeur, classe)"""
    top = 58 if sub else 44; rh = 24; h = top + len(items) * rh + 12
    vmax = vmax or max(v for _, v, _ in items) or 1
    sc = (w - labw - 80) / vmax; out = []
    for i, (l, v, c) in enumerate(items):
        y = top + i * rh
        out.append(f'<text class="tx" x="{labw-8}" y="{y+15}" text-anchor="end">{esc(trunc(l, int(labw / 7.6)))}</text><rect class="{c}" x="{labw}" y="{y+3}" width="{max(1.5, v*sc):.1f}" height="{rh-8}" rx="2"/>'
                   f'<text class="mut" x="{labw+max(1.5, v*sc)+6:.1f}" y="{y+15}">{esc(fmt(v) if fmt else v)}</text>')
    return frame(w, h, title, sub, "".join(out), standalone)

def stacked(items, series, title, sub, standalone, w=760, labw=230):
    """items : (libellé, [valeurs]) ; séries : [(nom, classe)] ; barres normalisées à 100 %"""
    out = []; x = 16; ly = 52 if sub else 38
    for nm, c in series:
        if x + 22 + 7 * len(nm) > w: x = 16; ly += 18
        out.append(f'<rect class="{c}" x="{x}" y="{ly}" width="10" height="10" rx="2"/><text class="tx" x="{x+15}" y="{ly+9}">{esc(nm)}</text>'); x += 22 + 7 * len(nm)
    top = ly + 24; rh = 24; h = top + len(items) * rh + 12
    bw = w - labw - 24
    for i, (l, vals) in enumerate(items):
        y = top + i * rh; tot = sum(vals) or 1; acc = 0
        out.append(f'<text class="tx" x="{labw-8}" y="{y+15}" text-anchor="end">{esc(trunc(l, int(labw / 7.6)))}</text>')
        for (nm, c), v in zip(series, vals):
            wv = bw * v / tot
            if wv > 0.4: out.append(f'<rect class="{c}" x="{labw+acc:.1f}" y="{y+3}" width="{wv-1:.1f}" height="{rh-8}"><title>{esc(l)} · {esc(nm)} : {v:g}</title></rect>')
            if wv > 30: out.append(f'<text x="{labw+acc+wv/2:.1f}" y="{y+15}" text-anchor="middle" fill="#fff" font-size="11">{100*v/tot:.0f}</text>')
            acc += wv
    return frame(w, h, title, sub, "".join(out), standalone)

# ------------------------------------------------------------------ graphiques
def charts(lg, standalone, small=False):
    """small : cartes de 440 px pour la grille de la page d'accueil (8 lignes au plus, sans sous-titre)."""
    global bars, stacked
    if small:
        _b, _s = bars, stacked
        def bars(items, title, sub, standalone, w=760, labw=230, fmt=None, vmax=None):
            return _b(items[:8], SHORT.get(title, title), None, standalone, w=440, labw=min(labw, 175), fmt=fmt, vmax=vmax)
        def stacked(items, series, title, sub, standalone, w=760, labw=230):
            return _s(items[:8], series, SHORT.get(title, title), None, standalone, w=440, labw=min(labw, 150))
        try: return charts(lg, standalone)
        finally: bars, stacked = _b, _s
    fam = [(lab(FAM, r["famille"], lg), r["voies_base"], "c1") for r in sorted(L("by_family"), key=lambda r: -r["voies_base"])]
    meth = [(lab(METH, r["methode"], lg), r["voies"], "c5" if r["methode"] == "non_classee" else "c1") for r in L("methodes")[:14]]
    ess = sorted(L("essentiels_methode"), key=lambda r: -r["voies"])[:10]
    gaps = sorted([r for r in L("proprietes_attendues") if r["voies"] >= 15], key=lambda r: r["couverture_pct"])[:14]
    br = sorted([r for r in L("verif_branches") if r["famille"] != "toutes"], key=lambda r: -r["pct_mortes"])[:9]
    tot_br = [r for r in L("verif_branches") if r["famille"] == "toutes"][0]
    acc = {}
    for r in L("mecanismes_accord"): acc.setdefault(r["famille"], {})[r["accord"]] = r["voies"]
    accf = sorted(acc.items(), key=lambda kv: -sum(kv[1].values()))[:8]
    mot = [r for r in L("limites_motifs") if r["motif"] != "autre"][:10]
    ref = {}
    for r in L("references_externes"): ref[r["verdict"]] = ref.get(r["verdict"], 0) + 1
    bl = [r for r in L("verif_reextraction") if r["pmcid"] == "TOTAL"][0]
    T = lambda fr, en: (fr, en)[lg]
    out = {}
    out["familles"] = bars(fam, T("Voies de base de matériau par famille", "Base routes per material family"), T("747 voies de base, 17 familles attribuées par l'extracteur", "747 base routes, 17 families assigned by the extractor"), standalone)
    out["methodes"] = bars(meth, T("Types de synthèse (classement par mots-clés de la méthode)", "Synthesis types (keyword classification of the method)"), T("14 premières classes sur 29", "top 14 of 29 classes"), standalone)
    out["essentiels"] = stacked([(lab(METH, r["methode"], lg), [r["pct_cite"], r["pct_non_cite_declare"], r["pct_absent_grille"]]) for r in ess],
                                [(T("cité", "cited"), "c4"), (T("déclaré absent de l'article", "declared absent in the paper"), "c2"), (T("jamais cherché (hors grille)", "never looked for (outside grid)"), "c3")],
                                T("Paramètres essentiels par méthode", "Essential parameters per method"), T("part des cases voie × paramètre essentiel, en %", "share of route × essential-parameter cells, %"), standalone)
    out["trous"] = bars([(f"{lab(FAM, r['famille'], lg)} · {lab(PROP, r['propriete'], lg)}", r["couverture_pct"], "c2") for r in gaps],
                        T("Propriétés attendues les moins renseignées", "Least-reported expected properties"), T("part des voies de la famille qui rapportent la propriété, en %", "share of the family's routes that report the property, %"), standalone, labw=290, vmax=100, fmt=lambda v: f"{v:.0f}%")
    out["branches"] = bars([(T("toutes familles", "all families"), tot_br["pct_mortes"], "c5")] + [(lab(FAM, r["famille"], lg), r["pct_mortes"], "c3") for r in br],
                           T("Branches sans résultat ni caractérisation", "Branches with no outcome or characterization"), T(f"{n(tot_br['branches'], lg)} branches (variantes testées), part « mortes » en %", f"{n(tot_br['branches'], lg)} branches (tested variants), share \"dead\", %"), standalone, fmt=lambda v: f"{v:.1f}%")
    out["mecanismes"] = stacked([(lab(FAM, f, lg), [d.get("accord", 0), d.get("nuance", 0), d.get("desaccord", 0)]) for f, d in accf],
                                [(lab(ACC, "accord", lg), "c4"), (lab(ACC, "nuance", lg), "c5"), (lab(ACC, "desaccord", lg), "c3")],
                                T("Mécanisme de formation : auteurs contre critique scientifique", "Formation mechanism: authors vs. science reviewer"), T(f"{sum(sum(d.values()) for d in acc.values())} voies comparées, 8 familles principales, en %", f"{sum(sum(d.values()) for d in acc.values())} routes compared, 8 main families, %"), standalone)
    out["limites"] = bars([(lab(MOTIF, r["motif"], lg), r["limites"], "c1") for r in mot], T("Motifs des limites de reproductibilité", "Reasons for reproducibility limits"), T(f"{n(S['limites_reproductibilite'], lg)} annotations, premier motif reconnu dans le texte", f"{n(S['limites_reproductibilite'], lg)} annotations, first reason recognised in the text"), standalone, labw=260)
    out["references"] = bars([(lab(VERD, k, lg), ref.get(k, 0), {"conforme": "c4", "non_trouve": "c5"}.get(k, "c2")) for k in ("conforme", "plus_large", "plus_bas", "plus_haut", "non_trouve")],
                             T("Base contre plages de référence relevées sur le web", "Database vs. reference ranges found on the web"), T(f"{sum(ref.values())} couples matériau-propriété (28 matériaux fréquents)", f"{sum(ref.values())} material-property pairs (28 frequent materials)"), standalone, labw=170)
    out["aveugle"] = bars([(T("paramètres : précision", "parameters: precision"), bl["precision_params"], "c4"), (T("résultats : précision", "outcomes: precision"), bl["precision_resultats"], "c4"),
                           (T("réactifs : rappel", "reagents: recall"), bl["rappel_reactifs"], "c1"), (T("paramètres : rappel", "parameters: recall"), bl["rappel_params"], "c1"), (T("résultats : rappel", "outcomes: recall"), bl["rappel_resultats"], "c1")],
                          T("Ré-extraction à l'aveugle de 20 publications", "Blind re-extraction of 20 papers"), T("précision = valeurs de l'aveugle présentes en base ; rappel = valeurs de la base retrouvées", "precision = blind values present in the database; recall = database values found"), standalone, labw=190, vmax=100, fmt=lambda v: f"{v:.1f}%")
    return out

# ------------------------------------------------------------------ contenu (une source, deux rendus)
def content(lg):
    """Blocs : (type, ...) ; types : h2 h3 p ul ol kpis chart table code note. Markdown léger dans les textes (** ` [](])."""
    ex = L("essentiels_methode"); ov = S
    st = L("verif_stoechiometrie_resume")[0]; si = L("verif_si_resume")[0]; sy = L("verif_param_synonymes_resume")[0]; va = L("verif_variation_resume")[0]
    bl = [r for r in L("verif_reextraction") if r["pmcid"] == "TOTAL"][0]; tot_br = [r for r in L("verif_branches") if r["famille"] == "toutes"][0]
    acc = {}
    for r in L("mecanismes_accord"): acc[r["accord"]] = acc.get(r["accord"], 0) + r["voies"]
    ref = {}
    for r in L("references_externes"): ref[r["verdict"]] = ref.get(r["verdict"], 0) + 1
    fond = sorted(L("mecanismes_fondateurs"), key=lambda r: -r["manquant"])[:3]
    meth0 = L("methodes")[0]; hyd = ex[0]
    N = lambda x: n(x, lg); P = lambda x, d=1: p(x, lg, d)
    T = lambda fr, en: (fr, en)[lg]
    rep = f"{GH}/blob/main/audits/"
    pal_rows = [[str(i + 1), N(q), N(rl), str(fa), (str(med).replace(".", ",") if lg == 0 else str(med)), f"{fk} / {N(c)}"] for i, (q, rl, fa, med, fk, c) in enumerate(PALIERS)]
    pres = [
        ("p", T("**Une base vérifiable de protocoles de synthèse de matériaux, extraits de 500 articles en accès libre par un pipeline multi-agent. Chaque valeur porte la citation mot pour mot qui la fonde.**",
                "**A verifiable database of materials synthesis protocols, extracted from 500 open-access papers by a multi-agent pipeline. Every value carries the verbatim quote that supports it.**")),
        ("kpis", [(N(ov["publications"]), T("publications closes", "papers closed")), (N(ov["voies"]), T("voies de synthèse", "synthesis routes")), (N(ov["parametres"]), T("paramètres cités", "cited parameters")),
                  (N(ov["resultats"]), T("résultats mesurés", "measured outcomes")), (N(QUOTES), T("citations vérifiées, 100 % retrouvées", "quotes checked, 100% found")), (N(ov["annotations"]), T("annotations (interprétation)", "annotations (interpretation)"))]),
        ("h2", T("Pourquoi cette base", "Why this exists")),
        ("p", T("La littérature de synthèse est abondante mais peu réutilisable : les conditions sont dispersées entre Méthodes, Résultats, tableaux, légendes et annexes ; les séries d'échantillons tiennent en une phrase (« la même procédure a été répétée à 150 et 180 °C ») ; les manques, comme une atmosphère de recuit non précisée, ne sont jamais signalés.",
                "The synthesis literature is huge but hard to reuse. Conditions are scattered across Methods, Results, tables, captions and supplementary files. Sample series are described in one sentence (\"the same procedure was repeated at 150 and 180 °C\"). Missing information, such as an unstated annealing atmosphere, is never flagged.")),
        ("p", T("Pour chaque article, la base répond à deux questions : **que dit exactement l'article** de chaque réactif, étape, paramètre et résultat, pour chaque variante comparée par les auteurs ? **Qu'omet-il**, et qu'est-ce qui est incohérent ou douteux pour un lecteur formé ? L'objectif : qu'un chimiste puisse **refaire un matériau à partir de la base seule** et voir **comment chaque variation de synthèse change le résultat**.",
                "For each paper the database answers two questions: **what exactly does the paper say** about every reagent, step, parameter and result, for every variant the authors compared? **What does it leave out**, and what is inconsistent or doubtful for a trained reader? The goal: a chemist can **reproduce a material from the database alone** and see **how each synthesis variation changes the outcome**.")),
        ("h2", T("Comment un article devient une donnée", "How a paper becomes data")),
        ("ol", [T("**Extraction.** Un agent lecteur transforme l'article (texte, légendes, tableaux d'annexe, figures) en voies, étapes, paramètres et résultats, chacun avec sa citation ; ce que l'article ne dit pas est enregistré (`not_stated`).",
                  "**Extraction.** A reader agent turns the paper (text, captions, supplementary tables, figures) into routes, steps, parameters and results, each with its quote; what the paper does not state is recorded (`not_stated`)."),
                T("**Contrôle automatique et chargement.** `load.py` vérifie que chaque citation existe mot pour mot dans la source, ainsi que les unités, la chimie et la structure ; rien ne se charge avec une erreur.",
                  "**Automatic checks and loading.** `load.py` verifies that every quote exists verbatim in the source, plus units, chemistry and structure; nothing loads with an error."),
                T("**Critique de fidélité.** Un second lecteur, indépendant, compare l'extraction à l'article et liste ce qui manque, est mal attribué ou n'est pas soutenu.",
                  "**Fidelity critique.** A second, independent reader compares the extraction with the paper and lists what is missing, misattributed or unsupported."),
                T("**Critique scientifique.** Un agent de raisonnement chimique recalcule la stœchiométrie, juge la plausibilité à partir de la littérature et propose des mécanismes ; les problèmes venant de l'article deviennent des limites de reproductibilité, jamais des corrections de données.",
                  "**Science critique.** A chemistry-reasoning agent recomputes stoichiometry, judges plausibility against the literature and proposes mechanisms; problems that come from the paper become reproducibility limits, never data edits."),
                T("**Corrections et audit.** Un agent applique les décisions constat par constat ; tous les 50 articles, un audit recontrôle chaque citation, relit des valeurs à la main et compare les synthèses d'un même matériau.",
                  "**Corrections and audit.** A correction agent applies decisions finding by finding; every 50 papers an audit re-checks every quote, re-reads values by hand and cross-compares syntheses of the same material.")]),
        ("h2", T("Principes", "Ground rules")),
        ("ul", [T("**La citation fait foi.** Aucune valeur sans citation exacte ; rien d'inventé, déduit ou converti à la place des auteurs.", "**The quote is the proof.** No value without an exact quote; nothing invented, inferred or converted on the authors' behalf."),
                T("**L'absence est une donnée.** Ce que l'article ne dit pas est enregistré explicitement : une voie n'est jamais « complète » en silence.", "**Absence is data.** What the paper does not state is recorded explicitly, so a route is never silently complete."),
                T("**Toute comparaison compte.** Toutes les variantes comparées par les auteurs sont des branches, échecs compris.", "**Every comparison counts.** All variants compared by the authors are captured as branches, including failures."),
                T("**Les erreurs des auteurs sont gardées, pas corrigées.** Elles sont signalées comme limites de reproductibilité.", "**Author errors are kept, not fixed.** They are flagged as reproducibility limits."),
                T("**L'interprétation est séparée des données**, et une erreur vue deux fois devient une règle écrite du protocole.", "**Interpretation is separate from data**, and a mistake seen twice becomes a written rule of the protocol.")]),
        ("h2", T("Qualité mesurée", "Measured quality")),
        ("p", T(f"Sur les dix paliers de 50 publications : **100 % des {N(QUOTES)} citations** contrôlées sont retrouvées mot pour mot ; {N(RELUES)} valeurs relues à la main, {FAUSSES} fausses (soit {P(100*FAUSSES/RELUES, 2)}), dont 10 dans les 10 publications de calibration, devenues des règles du protocole ; aucune anomalie bloquante ouverte.",
                f"Over the ten batches of 50 papers: **100% of {N(QUOTES)} quotes** checked are found verbatim; {N(RELUES)} values re-read by hand, {FAUSSES} wrong ({P(100*FAUSSES/RELUES, 2)}), 10 of them in the 10 calibration papers, which became protocol rules; no blocking anomaly left open.")),
        ("table", [T("Palier", "Batch"), T("Citations vérifiées", "Quotes verified"), T("Valeurs relues", "Values re-read"), T("Fausses", "Wrong"), T("Médiane de constats / article", "Median findings / paper"), T("Constats « faux » / total", "\"Wrong\" findings / total")], pal_rows),
        ("note", T("**Portée.** La base garantit la fidélité à la source et rend explicite ce qui manque pour reproduire ; elle ne garantit pas qu'un protocole publié fonctionne. La plupart des verdicts « douteux » viennent des articles eux-mêmes (une teneur en cobalt plus lourde que le cobalt pur, un « laser HeNe à 532 nm »), gardés tels quels et signalés.",
                   "**Scope.** The database guarantees faithfulness to the source and makes explicit what is missing to reproduce a synthesis. It does not guarantee that a published protocol works. Most \"doubtful\" verdicts come from the papers themselves (a cobalt content heavier than pure cobalt, a \"HeNe laser at 532 nm\"), kept as written and flagged.")),
        ("h2", T("Utiliser la base", "Using the database")),
        ("p", T("`synthese.db` est un fichier SQLite ordinaire (DB Browser, DBeaver, Python). Protocole complet d'une branche, avec ses citations :", "`synthese.db` is a plain SQLite file (DB Browser, DBeaver, Python). Full protocol of one branch, with quotes:")),
        ("code", "SELECT step_order, action, parameter, value_num, value_text, unit, quote\nFROM v_route_complete\nWHERE pmcid = 'PMC0000000' AND branch_label = 'ZnO-180'\nORDER BY step_order;"),
        ("h2", T("Plan du dépôt", "Repository map")),
        ("table", [T("Chemin", "Path"), T("Contenu", "Content")], [["`synthese.db`", T("la base", "the database")], ["`extractions/`", T("un JSON par article, source de vérité de la base", "one JSON per paper, the source of truth of the database")],
                                                               ["`critiques/`, `journaux/`", T("critiques de fidélité et scientifique, journaux de décision des agents", "fidelity and science critiques, agents' decision logs")],
                                                               ["`audits/`", T("rapports de palier, audits de contenu et de vérification (`audits/verification/aveugle/` : ré-extractions indépendantes), coûts en jetons", "batch reports, content and verification audits (`audits/verification/aveugle/`: independent re-extractions), token costs")],
                                                               ["`analyses/`", T("scripts des audits de contenu et de vérification, générateur de cette vitrine", "content and verification audit scripts, generator of this showcase")],
                                                               ["`docs/`", T("page publique, graphiques, données des analyses", "public page, charts, analysis datasets")],
                                                               ["`RUNBOOK.md`, `CRITIQUE.md`, `PLAUSIBILITE.md`", T("protocoles donnés aux agents", "protocols given to the agents")], ["`load.py`, `audit.py`, `critic_load.py`", T("contrôles automatiques et chargement", "automatic checks and loading")]]),
    ]
    ana = [
        ("p", T(f"Deux audits de contenu (28 octobre 2026) examinent ce que contiennent réellement les 500 publications et si l'extraction est fiable. Tout est reproductible : `python3 -I analyses/audit_contenu.py`, `audit_parametres.py`, `audit_verification.py`, `compare_blind.py`, puis `build_site.py` pour cette page.",
                f"Two content audits (28 October 2026) examine what the 500 papers actually contain and whether the extraction can be trusted. Everything is reproducible: `python3 -I analyses/audit_contenu.py`, `audit_parametres.py`, `audit_verification.py`, `compare_blind.py`, then `build_site.py` for this page.")),
        ("kpis", [(N(ov["voies_base_materiau"]), T("voies de base d'un matériau", "material base routes")), (str(ov["methodes"]), T("classes de méthode", "method classes")), (N(ov["proprietes_canoniques"]), T("propriétés canoniques (sur 16 577 noms)", "canonical properties (from 16,577 names)")),
                  (P(ov["pct_voies_avec_limite"], 0), T("des voies de base avec une limite", "of base routes with a limit")), (N(ov["mecanismes_compares"]), T("mécanismes comparés", "mechanisms compared")), ("20", T("publications ré-extraites à l'aveugle", "papers re-extracted blind"))]),
        ("h2", T("1. Ce que contient la base", "1. What the database contains")),
        ("chart", "familles"), ("chart", "methodes"),
        ("ul", [T(f"**{meth0['methode'].replace('_', ' ')} domine** ({P(meth0['part_pct'])} des voies de base), puis précipitation, sol-gel et solvothermal. Deux classements indépendants (mots-clés de la méthode, enchaînement des étapes) concordent à **{P(ov['concordance_pct'])}**.",
                  f"**Hydrothermal dominates** ({P(meth0['part_pct'])} of base routes), then precipitation, sol-gel and solvothermal. Two independent classifications (method keywords, step sequence) agree on **{P(ov['concordance_pct'])}**."),
                T(f"Les 16 577 noms de propriétés libres sont ramenés à **{ov['proprietes_canoniques']} propriétés canoniques** par une table d'expressions régulières ; **{P(ov['part_autre'])} des valeurs** restent non classées (noms trop spécifiques). Avant toute exploitation statistique, une liste fermée de noms est à fixer.",
                  f"The 16,577 free property names are mapped to **{ov['proprietes_canoniques']} canonical properties** by a regex table; **{P(ov['part_autre'])} of values** stay unclassified (names too specific). A closed vocabulary is needed before any statistical use.")]),
        ("h2", T("2. Paramètres communs et paramètres essentiels", "2. Common and essential parameters")),
        ("chart", "essentiels"),
        ("ul", [T("**Température et durée sont les seuls paramètres universels** (90 à 100 % des voies des méthodes principales). Au-delà, deux voies d'une même méthode ne partagent que 25 à 45 % de leurs types de paramètres (similarité de Jaccard de 0,19 à 0,43).",
                  "**Temperature and duration are the only universal parameters** (90–100% of routes of the main methods). Beyond that, two routes of the same method share only 25–45% of their parameter types (Jaccard similarity 0.19–0.43)."),
                T(f"**Les articles sont la première source de manque.** Pour les méthodes en autoclave, {P(hyd['pct_non_cite_declare'], 0)} des paramètres essentiels ne sont pas donnés par l'article (et l'extracteur l'a écrit) ; le taux de remplissage est cité dans 1 à 5 % des voies, les rampes de chauffe et de refroidissement dans moins de 12 %.",
                  f"**Papers are the first source of gaps.** For autoclave methods, {P(hyd['pct_non_cite_declare'], 0)} of essential parameters are not given by the paper (and the extractor said so); fill fraction is cited in 1–5% of routes, heating and cooling rates in under 12%."),
                T("**L'extraction a ses angles morts** : vitesse de refroidissement, débit de gaz, répétitions de cycles, puissance, taux de remplissage ne figurent pas dans la grille de reproductibilité, donc ne sont ni cités ni déclarés absents.",
                  "**The extraction has blind spots**: cooling rate, gas flow, cycle repeats, power and fill fraction are not in the reproducibility grid, so they are neither cited nor declared absent."),
                T("Les quantités de précurseurs, elles, sont données pour 87 % (hydrothermal) à 97 % (voies vertes) d'entre eux, et déclarées absentes quand elles manquent : aucun manque silencieux.",
                  "Precursor amounts, by contrast, are given for 87% (hydrothermal) to 97% (green routes) of precursors and declared absent when missing: no silent gaps.")]),
        ("h2", T("3. Trous de couverture", "3. Coverage gaps")),
        ("chart", "trous"),
        ("ul", [T(f"**{ov['trous_famille_methode']} cases famille × méthode sur 175** comptent moins de 5 voies : hors hydrothermal et sol-gel, chaque méthode n'est représentée que par une poignée de voies par famille (électrochimie : 4 voies en tout).",
                  f"**{ov['trous_famille_methode']} family × method cells out of 175** hold fewer than 5 routes: beyond hydrothermal and sol-gel, each method is represented by a handful of routes per family (electrochemistry: 4 routes in total)."),
                T(f"**{ov['proprietes_attendues_trous']} couples famille-propriété attendus** sont couverts à moins de 30 % : band gap et rendement quantique des pérovskites, surface BET des carbones, rétention de capacité des batteries, densité et dureté des céramiques.",
                  f"**{ov['proprietes_attendues_trous']} expected family-property pairs** are covered below 30%: band gap and quantum yield of perovskites, BET area of carbons, capacity retention of batteries, density and hardness of ceramics."),
                T("Familles trop peu représentées : carbures (3 voies), phosphures (1), nitrures (17), matériaux 2D (18). Absentes ou noyées dans « autre » : polymères, verres, alliages, COF, électrolytes solides, thermoélectriques.",
                  "Under-represented families: carbides (3 routes), phosphides (1), nitrides (17), 2D materials (18). Missing or buried in \"other\": polymers, glasses, alloys, COFs, solid electrolytes, thermoelectrics.")]),
        ("h2", T("4. Qualité des données", "4. Data quality")),
        ("chart", "branches"),
        ("ul", [T(f"**Branches** : {P(tot_br['pct_mortes'])} sans résultat ni caractérisation, mais {P(24.0, 0)} chez les MOF (séries de conditions dont l'article ne rapporte qu'un résultat global).", f"**Branches**: {P(tot_br['pct_mortes'])} with neither outcome nor characterization, but {P(24.0, 0)} among MOFs (condition series for which the paper reports a single global result)."),
                T(f"**Stœchiométrie nominale** : sur {st['controlables']} voies contrôlables, {st['≤10 %']} concordent à moins de 10 % avec la formule du produit ; les écarts importants sont des excès voulus ou des précurseurs apportés par une voie intermédiaire, pas des erreurs.",
                  f"**Nominal stoichiometry**: of {st['controlables']} checkable routes, {st['≤10 %']} match the product formula within 10%; large gaps are intended excesses or precursors supplied by an intermediate route, not errors."),
                T(f"**{ov['hors_plage']} valeurs hors plage physique**, toutes recopiées de l'article (rendements quantiques de 112 à 241 % pour des points de carbone, mesurés par rapport à un étalon).", f"**{ov['hors_plage']} out-of-range values**, all copied from the papers (quantum yields of 112–241% for carbon dots, measured against a standard)."),
                T(f"**Normalisation** : {sy['noms_distincts']} noms de paramètres pour {sy['groupes']} types ; {P(si['pct'], 0)} des paramètres numériques ont une valeur SI (température, durée, rampe à 99 % ; jamais les volumes, concentrations, vitesses : limite de `load.py`).",
                  f"**Normalization**: {sy['noms_distincts']} parameter names for {sy['groupes']} types; {P(si['pct'], 0)} of numeric parameters have an SI value (temperature, duration, ramp at 99%; never volumes, concentrations, speeds: a `load.py` limit)."),
                T(f"**Variation → effet** : {P(va['pct'], 0)} des {N(va['variations_numeriques'])} variations numériques ont une propriété mesurée des deux côtés ; {va['series_3_points']} séries de 3 points ou plus, dont {P(va['pct_monotones'], 0)} monotones. Un changement de température déplace les propriétés de taille et de texture de 40 à 50 % en médiane, un changement de réactif les propriétés optiques de moins de 10 %.",
                  f"**Variation → effect**: {P(va['pct'], 0)} of {N(va['variations_numeriques'])} numeric variations have a property measured on both sides; {va['series_3_points']} series of 3+ points, {P(va['pct_monotones'], 0)} monotonic. A temperature change shifts size and texture properties by 40–50% (median), a reagent change shifts optical properties by under 10%.")]),
        ("h2", T("5. Limites de reproductibilité et mécanismes", "5. Reproducibility limits and mechanisms")),
        ("chart", "limites"), ("chart", "mecanismes"),
        ("ul", [T(f"**{P(ov['pct_voies_avec_limite'], 0)} des voies de base** portent au moins une limite ; la première cause est l'incohérence interne de l'article (21 %), devant les preuves non discriminantes (10 %), les interprétations contestées (10 %) et les bilans de matière impossibles (9,5 %).",
                  f"**{P(ov['pct_voies_avec_limite'], 0)} of base routes** carry at least one limit; the first cause is internal inconsistency in the paper (21%), ahead of non-discriminating evidence (10%), contested interpretation (10%) and impossible mass balances (9.5%)."),
                T(f"Sur {ov['mecanismes_compares']} voies, le mécanisme des auteurs et celui du critique scientifique sont en **accord pour {acc.get('accord', 0)}**, en **nuance pour {acc.get('nuance', 0)}** (dont 106 articles qui ne décrivent aucun mécanisme) et en **désaccord pour {acc.get('desaccord', 0)}** ; **{ov['mecanismes_incompatibles']}** mécanismes sont contredits par les conditions extraites (réduction sans réducteur, AgCl précipité avant toute réduction…).",
                  f"Over {ov['mecanismes_compares']} routes, the authors' mechanism and the science reviewer's are in **agreement for {acc.get('accord', 0)}**, **nuanced for {acc.get('nuance', 0)}** (including 106 papers that describe no mechanism) and in **disagreement for {acc.get('desaccord', 0)}**; **{ov['mecanismes_incompatibles']}** mechanisms are contradicted by the extracted conditions (reduction without a reductant, AgCl precipitating before any reduction…)."),
                T("Travaux fondateurs le plus souvent absents alors qu'ils fondent la méthode : " + ", ".join(f"{r['fondateur']} ({r['manquant']})" for r in fond) + ".", "Foundational works most often missing though they ground the method: " + ", ".join(f"{r['fondateur']} ({r['manquant']})" for r in fond) + ".")]),
        ("h2", T("6. Comparaison à la littérature", "6. Comparison with the literature")),
        ("chart", "references"),
        ("ul", [T(f"Sur {sum(ref.values())} couples matériau-propriété, {ref.get('conforme', 0)} sont dans la plage publiée. Écarts nets : band gap du SnS (médiane 2,81 eV contre 1,07–1,40 eV massif), photoluminescence du CdS (580 nm contre 490–505 nm : émission de pièges), silices « mésoporeuses » (BET 274 contre 400–1 137 m²/g), volume microporeux du ZIF-8 (0,15 contre 0,52–0,62 cm³/g).",
                  f"Of {sum(ref.values())} material-property pairs, {ref.get('conforme', 0)} fall within the published range. Clear deviations: SnS band gap (median 2.81 eV vs. 1.07–1.40 eV bulk), CdS photoluminescence (580 nm vs. 490–505 nm: trap emission), \"mesoporous\" silicas (BET 274 vs. 400–1,137 m²/g), ZIF-8 micropore volume (0.15 vs. 0.52–0.62 cm³/g)."),
                T("Les bases structurées (CoRE MOF, IZA, Materials Project) ne sont pas joignables depuis l'environnement d'exécution ; les plages viennent du web, avec l'URL réellement consultée.", "Structured databases (CoRE MOF, IZA, Materials Project) are not reachable from the execution environment; ranges come from the web, with the URL actually consulted.")]),
        ("h2", T("7. Vérification par ré-extraction à l'aveugle", "7. Verification by blind re-extraction")),
        ("chart", "aveugle"),
        ("ul", [T(f"20 publications tirées au sort ont été ré-extraites par un agent qui n'a vu ni l'extraction en base ni les critiques : {bl['voies_appariees']} voies sur {bl['voies_base']} appariées. **{P(bl['precision_params'])} des paramètres et {P(bl['precision_resultats'])} des résultats** trouvés à l'aveugle sont dans la base, avec **0 conflit** sur les valeurs univoques.",
                  f"20 randomly drawn papers were re-extracted by an agent that saw neither the database extraction nor the critiques: {bl['voies_appariees']} of {bl['voies_base']} routes matched. **{P(bl['precision_params'])} of parameters and {P(bl['precision_resultats'])} of outcomes** found blind are in the database, with **0 conflict** on unambiguous values."),
                T("Le rappel plus bas (68 % des paramètres, 57 % des résultats) mesure l'apport des critiques : la base contient environ 30 % de paramètres et 40 % de résultats de plus qu'une extraction seule. Les désaccords restants sont des attributions d'une valeur à un autre échantillon ou à une autre voie.",
                  "The lower recall (68% of parameters, 57% of outcomes) measures what the critiques add: the database holds about 30% more parameters and 40% more outcomes than a single extraction. Remaining disagreements are attributions of a value to another sample or route.")]),
        ("h2", T("Rapports complets", "Full reports")),
        ("ul", [f"[audits/audit_contenu.md]({rep}audit_contenu.md) — " + T("types de synthèse, propriétés, conditions, trous, qualité, mécanismes, références", "synthesis types, properties, conditions, gaps, quality, mechanisms, references"),
                f"[audits/audit_verification.md]({rep}audit_verification.md) — " + T("paramètres par méthode et sept contrôles de vérification", "parameters per method and seven verification checks"),
                f"[audits/palier_010_relecture.md]({rep}palier_010_relecture.md) — " + T("dernier audit de palier", "latest batch audit")]),
    ]
    return pres, ana

# ------------------------------------------------------------------ rendus
def inline_md(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s); s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)

def picture(light, dark, alt, width=None):
    w = f' width="{width}"' if width else ""
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{dark}">'
            f'<img src="{light}" alt="{html.escape(alt)}"{w}></picture>')

def render_md(blocks, lg, svgs, base="###", prefix="docs/img/", fold=False):
    """fold : chaque section h2 devient un bloc <details> repliable (README, sous la grille d'accueil)."""
    out = []; opened = False
    for b in blocks:
        t = b[0]
        if t == "h2" and fold and re.match(r"\d", b[1]):
            if opened: out.append("</details>\n")
            out.append(f"<details><summary><b>{inline_md(b[1])}</b></summary>\n"); opened = True
        elif t == "h2":
            if opened: out.append("</details>\n"); opened = False
            out.append(f"\n{base} {b[1]}\n")
        elif t == "p": out.append(b[1] + "\n")
        elif t == "note": out.append("> " + b[1] + "\n")
        elif t == "ul": out.append("\n".join(f"- {x}" for x in b[1]) + "\n")
        elif t == "ol": out.append("\n".join(f"{i+1}. {x}" for i, x in enumerate(b[1])) + "\n")
        elif t == "kpis": out.append("| " + " | ".join(f"**{v}**" for v, _ in b[1]) + " |\n|" + "---|" * len(b[1]) + "\n| " + " | ".join(l for _, l in b[1]) + " |\n")
        elif t == "table": out.append("| " + " | ".join(b[1]) + " |\n|" + "---|" * len(b[1]) + "\n" + "\n".join("| " + " | ".join(r) + " |" for r in b[2]) + "\n")
        elif t == "code": out.append("```sql\n" + b[1] + "\n```\n")
        elif t == "chart":
            f = f'{prefix}{b[1]}_{("fr","en")[lg]}'
            out.append('<p align="center">' + picture(f + ".svg", f + "_dark.svg", re.search(r'aria-label="(.*?)"', svgs[b[1]]).group(1), 760) + "</p>\n")
    if opened: out.append("</details>\n")
    return "\n".join(out)

def render_html(blocks, lg, svgs):
    out = []; ul = None
    for b in blocks:
        t = b[0]
        if t == "h2": out.append(f"<h2>{inline_md(b[1])}</h2>")
        elif t == "p": out.append(f"<p>{inline_md(b[1])}</p>")
        elif t == "note": out.append(f'<p class="note">{inline_md(b[1])}</p>')
        elif t == "ul": out.append("<ul>" + "".join(f"<li>{inline_md(x)}</li>" for x in b[1]) + "</ul>")
        elif t == "ol": out.append("<ol>" + "".join(f"<li>{inline_md(x)}</li>" for x in b[1]) + "</ol>")
        elif t == "kpis": out.append('<div class="kpis">' + "".join(f'<div><b>{v}</b><span>{inline_md(l)}</span></div>' for v, l in b[1]) + "</div>")
        elif t == "table": out.append('<div class="tw"><table><thead><tr>' + "".join(f"<th>{inline_md(h)}</th>" for h in b[1]) + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in r) + "</tr>" for r in b[2]) + "</tbody></table></div>")
        elif t == "code": out.append(f"<pre><code>{html.escape(b[1])}</code></pre>")
        elif t == "chart": out.append(f'<figure class="ch">{svgs[b[1]]}</figure>')
    return "\n".join(out)

PAGE = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Base de voies de synthèse de matériaux</title>
<meta name="description" content="Base vérifiable de 5 338 voies de synthèse extraites de 500 articles en accès libre / A verifiable database of 5,338 synthesis routes from 500 open-access papers">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600&family=Source+Serif+4:wght@400;600&display=swap" rel="stylesheet">
<script>document.documentElement.classList.add('js')</script>
<style>
:root{--bg:#f6f8f9;--fg:#1d2a30;--mut:#5b6b73;--line:#d5dde0;--panel:#fff;--c1:#17707f;--c2:#c27c0e;--c3:#a8412f;--c4:#3f7d4e;--c5:#9fb3bb;--bgs:#f3f6f7;--code:#eef2f3}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#11181b;--fg:#e4edf0;--mut:#9db0b8;--line:#2b3a40;--panel:#182125;--c1:#4fb3c4;--c2:#e0a23a;--c3:#d9735f;--c4:#6fb583;--c5:#5d747d;--bgs:#1a2428;--code:#1f2b30}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 'Source Sans 3',system-ui,-apple-system,'Segoe UI',sans-serif}
.wrap{max-width:1040px;margin:0 auto;padding:0 max(16px,env(safe-area-inset-left)) 56px}
header{padding:32px 0 8px;display:flex;flex-wrap:wrap;gap:16px;align-items:flex-end;justify-content:space-between}
h1{font:600 clamp(26px,4vw,38px)/1.15 'Source Serif 4',Georgia,serif;margin:0;letter-spacing:-.01em;max-width:30ch}
.sub{color:var(--mut);margin:6px 0 0;max-width:62ch}
.lang{display:flex;border:1px solid var(--line);border-radius:6px;overflow:hidden}
.lang button{font:inherit;color:var(--fg);background:var(--panel);border:0;padding:6px 14px;cursor:pointer}
.lang button[aria-pressed=true]{background:var(--c1);color:#fff}
.tabs{display:flex;gap:4px;border-bottom:1px solid var(--line);margin:18px 0 22px;flex-wrap:wrap}
.tabs button{font:inherit;color:var(--mut);background:none;border:0;border-bottom:3px solid transparent;padding:10px 16px;cursor:pointer;margin-bottom:-1px}
.tabs button[aria-selected=true]{color:var(--fg);border-bottom-color:var(--c1);font-weight:600}
button:focus-visible{outline:2px solid var(--c1);outline-offset:2px}
.js [data-panel][hidden],.js .tabs[hidden]{display:none}
h2{font:600 22px/1.25 'Source Serif 4',Georgia,serif;margin:34px 0 10px}
p,li{max-width:74ch}li{margin:5px 0}
a{color:var(--c1)}code{background:var(--code);padding:1px 5px;border-radius:3px;font-size:.92em}
pre{background:var(--code);padding:14px 16px;border-radius:6px;overflow:auto}pre code{background:none;padding:0}
.note{border-left:3px solid var(--c2);padding:4px 0 4px 14px;color:var(--mut)}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:20px 0}
.kpis div{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:12px 14px;display:flex;flex-direction:column}
.kpis b{font:600 26px/1.1 'Source Serif 4',Georgia,serif;font-variant-numeric:tabular-nums;color:var(--c1)}
.kpis span{color:var(--mut);font-size:14px;margin-top:4px}
.tw{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14.5px;font-variant-numeric:tabular-nums}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{color:var(--mut);font-weight:600;white-space:nowrap}
figure.ch{margin:14px 0;overflow-x:auto}figure.ch svg{width:100%;height:auto;min-width:560px;display:block}
.ch .bg{fill:var(--bgs);stroke:var(--line)}.ch .tx{fill:var(--fg)}.ch .mut{fill:var(--mut)}.ch .c1{fill:var(--c1)}.ch .c2{fill:var(--c2)}.ch .c3{fill:var(--c3)}.ch .c4{fill:var(--c4)}.ch .c5{fill:var(--c5)}
.ch text{font-family:'Source Sans 3',system-ui,sans-serif;font-size:13px}.ch .t{font-size:15px;font-weight:600}
footer{margin-top:44px;padding-top:16px;border-top:1px solid var(--line);color:var(--mut);font-size:14px}
</style></head><body><div class="wrap">
<header><div><h1 data-l="fr">Base de voies de synthèse de matériaux</h1><h1 data-l="en" hidden>Materials Synthesis Routes Database</h1>
<p class="sub" data-l="fr">500 articles en accès libre, 5 338 voies, chaque valeur reliée à sa citation exacte.</p><p class="sub" data-l="en" hidden>500 open-access papers, 5,338 routes, every value tied to its exact quote.</p></div>
<div class="lang" role="group" aria-label="Langue / Language"><button type="button" data-lang="fr" aria-pressed="true">Français</button><button type="button" data-lang="en" aria-pressed="false">English</button></div></header>
<nav class="tabs" data-l="fr" role="tablist"><button type="button" role="tab" data-sec="presentation" aria-selected="true">Présentation</button><button type="button" role="tab" data-sec="analysis" aria-selected="false">Analyse</button></nav>
<nav class="tabs" data-l="en" role="tablist" hidden><button type="button" role="tab" data-sec="presentation" aria-selected="true">Presentation</button><button type="button" role="tab" data-sec="analysis" aria-selected="false">Analysis</button></nav>
@@PANELS@@
<footer><span data-l="fr">Code, données et rapports : <a href="@@GH@@">dépôt GitHub</a> · méthodologie complète : <a href="@@GH@@/blob/main/README.fr.md">README.fr.md</a> · page générée par <code>analyses/build_site.py</code>.</span><span data-l="en" hidden>Code, data and reports: <a href="@@GH@@">GitHub repository</a> · full methodology (French): <a href="@@GH@@/blob/main/README.fr.md">README.fr.md</a> · page generated by <code>analyses/build_site.py</code>.</span></footer>
</div>
<script>
(function(){
 var lang='fr',sec='presentation';
 function show(l,s,push){lang=l;sec=s;
  document.documentElement.lang=l;
  document.querySelectorAll('[data-l]').forEach(function(e){e.hidden=e.dataset.l!==l});
  document.querySelectorAll('.lang button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.lang===l)});
  document.querySelectorAll('.tabs[data-l="'+l+'"] button').forEach(function(b){b.setAttribute('aria-selected',b.dataset.sec===s)});
  document.querySelectorAll('[data-panel]').forEach(function(p){p.hidden=!(p.dataset.panel===l+'-'+s)});
  if(push)history.replaceState(null,'','#'+l+'-'+s)}
 var h=location.hash.slice(1).split('-');
 if(h.length===2&&/^(fr|en)$/.test(h[0])&&/^(presentation|analysis)$/.test(h[1])){lang=h[0];sec=h[1]}
 else if(!/^fr/i.test(navigator.language||'fr'))lang='en';
 document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){show(b.dataset.lang,sec,true)})});
 document.querySelectorAll('.tabs button').forEach(function(b){b.addEventListener('click',function(){show(lang,b.dataset.sec,true)})});
 window.addEventListener('hashchange',function(){var x=location.hash.slice(1).split('-');if(x.length===2&&/^(fr|en)$/.test(x[0]))show(x[0],x[1],false)});
 show(lang,sec,false)})();
</script></body></html>
"""

# ------------------------------------------------------------------ bloc visuel de la page d'accueil (README)
ACC_DIR = "docs/img/accueil/"
CARDS = ["familles", "methodes", "essentiels", "trous", "branches", "mecanismes", "limites", "references", "aveugle"]

def captions(lg):
    T = lambda fr, en: (fr, en)[lg]
    return {"familles": T(f"{n(S['voies_base_materiau'], lg)} voies de base de matériau, {S['familles']} familles", f"{n(S['voies_base_materiau'], lg)} material base routes, {S['familles']} families"),
            "methodes": T(f"8 premières classes sur {S['methodes']} (mots-clés de la méthode)", f"top 8 of {S['methodes']} classes (method keywords)"),
            "essentiels": T("vert : cité · orange : l'article se tait · rouge : hors grille", "green: cited · amber: paper silent · red: outside the grid"),
            "trous": T("part des voies de la famille qui rapportent la propriété", "share of the family's routes reporting the property"),
            "branches": T("variantes testées sans résultat ni caractérisation, en %", "tested variants with no outcome or characterization, %"),
            "mecanismes": T(f"{S['mecanismes_compares']} voies : mécanisme des auteurs jugé par le critique", f"{S['mecanismes_compares']} routes: authors' mechanism judged by the reviewer"),
            "limites": T(f"{p(S['pct_voies_avec_limite'], lg, 0)} des voies de base portent au moins une limite", f"{p(S['pct_voies_avec_limite'], lg, 0)} of base routes carry at least one limit"),
            "references": T(f"{S['references_conformes']} couples sur {S['references_comparees']} dans la plage publiée", f"{S['references_conformes']} of {S['references_comparees']} pairs within the published range"),
            "aveugle": T("20 publications ré-extraites sans voir la base", "20 papers re-extracted without seeing the database")}

def visual_md(lg, code, small):
    T = lambda fr, en: (fr, en)[lg]
    a = lambda name: picture(f"{ACC_DIR}{name}_{code}_light.svg", f"{ACC_DIR}{name}_{code}_dark.svg", re.search(r'aria-label="(.*?)"', open(f"{ACC_DIR}{name}_{code}_light.svg", encoding="utf-8").read()).group(1), "100%")
    cap = captions(lg); cells = []
    for k in CARDS:
        alt = re.search(r'aria-label="(.*?)"', small[k]).group(1)
        cells.append(f'<td width="50%" valign="top">{picture(f"{ACC_DIR}carte_{k}_{code}.svg", f"{ACC_DIR}carte_{k}_{code}_dark.svg", alt, "100%")}<br><sub>{html.escape(cap[k])}</sub></td>')
    more = T("Chiffres détaillés, méthode et limites : sections repliables ci-dessous, rapports <code>audits/audit_contenu.md</code> et <code>audits/audit_verification.md</code>.",
             "Detailed figures, method and limits: collapsible sections below, reports <code>audits/audit_contenu.md</code> and <code>audits/audit_verification.md</code>.")
    cells.append(f'<td width="50%" valign="middle"><sub>{more}</sub></td>')
    grid = "<table>\n" + "\n".join("<tr>" + "".join(cells[i:i + 2]) + "</tr>" for i in range(0, len(cells), 2)) + "\n</table>"
    return "\n".join([
        f'<p align="center">{a("pipeline")}</p>', "", f'<p align="center">{a("chiffres")}</p>', "",
        "<sub>" + T("Matériaux : couples (composition, phase) distincts, hors voies « dispositif ». Paramètres et propriétés communs : similarité de Jaccard moyenne entre deux voies de base de la même méthode (ou famille), sur le vocabulaire canonique. Prix : historique complet de <code>audits/jetons.csv</code> (chaque agent), au tarif API catalogue ; le journal ne sépare pas entrée, sortie et cache, d'où la fourchette ; l'orchestrateur et la ré-extraction à l'aveugle ne sont pas comptés. Calcul : <code>analyses/chiffres_accueil.py</code>.",
                    "Materials: distinct (composition, phase) pairs, device routes excluded. Shared parameters and properties: mean Jaccard similarity between two base routes of the same method (or family), on the canonical vocabulary. Price: full history of <code>audits/jetons.csv</code> (every agent) at list API rates; the log does not split input, output and cache, hence the range; the orchestrator and the blind re-extraction are not counted. Computed by <code>analyses/chiffres_accueil.py</code>.") + "</sub>", "",
        "## " + T("Le modèle de données", "The data model"), "",
        T("Une **voie de base** décrit un protocole complet ; chaque **branche** est une variante testée par les auteurs et ne porte que ce qui change. Chaque valeur est accompagnée de sa citation exacte, et ce que l'article ne dit pas est noté.",
          "A **base route** holds a full protocol; each **branch** is a variant tested by the authors and stores only what changes. Every value comes with its verbatim quote, and what the paper leaves out is recorded."), "",
        f'<p align="center">{a("modele")}</p>', "",
        "## " + T("Un exemple", "An example"), "",
        f'<p align="center">{a("exemple")}</p>', "",
        "## " + T("Ce que contient la base, en un coup d'œil", "The database at a glance"), "", grid, ""])

def main():
    os.makedirs(IMG, exist_ok=True)
    import build_visuels
    build_visuels.build(S, KPI)
    panels = []; md = {}; smalls = {}
    for lg, code in enumerate(("fr", "en")):
        svg_file = charts(lg, True); svg_inline = charts(lg, False)
        for k, v in svg_file.items(): open(f"{IMG}{k}_{code}.svg", "w", encoding="utf-8").write(v)
        pres, ana = content(lg)
        panels.append(f'<main data-panel="{code}-presentation" id="{code}-presentation">{render_html(pres, lg, svg_inline)}</main>')
        panels.append(f'<main data-panel="{code}-analysis" id="{code}-analysis" hidden>{render_html(ana, lg, svg_inline)}</main>')
        md[code] = render_md(ana, lg, svg_file, base="###", fold=True)
        for k, v in svg_file.items(): open(f"{IMG}{k}_{code}_dark.svg", "w", encoding="utf-8").write(v.replace(STYLE, STYLE_DARK))
        small = charts(lg, True, small=True); os.makedirs(ACC_DIR, exist_ok=True)
        for k, v in small.items():
            open(f"{ACC_DIR}carte_{k}_{code}.svg", "w", encoding="utf-8").write(v)
            open(f"{ACC_DIR}carte_{k}_{code}_dark.svg", "w", encoding="utf-8").write(v.replace(STYLE, STYLE_DARK))
        smalls[code] = small
    open("docs/index.html", "w", encoding="utf-8").write(PAGE.replace("@@PANELS@@", "\n".join(panels)).replace("@@GH@@", GH))
    open("docs/.nojekyll", "w").write("")
    # blocs de README
    for f, code, intro in (("README.md", "en", ""), ("README.fr.md", "fr", "")):
        s = open(f, encoding="utf-8").read()
        title = "7. What the database contains: results" if code == "en" else "7. Ce que contient la base : les résultats"
        block = f'<!-- SITE:analysis:begin -->\n<a id="analysis"></a>\n\n## {title}\n\n' + md[code] + '\n<!-- SITE:analysis:end -->'
        if "<!-- SITE:analysis:begin -->" in s: s = re.sub(r"<!-- SITE:analysis:begin -->[\s\S]*?<!-- SITE:analysis:end -->", lambda m: block, s)
        else: print(f"! marqueur SITE:analysis absent de {f} : bloc non inséré")
        vis = "<!-- SITE:visual:begin -->\n" + visual_md(("fr", "en").index(code), code, smalls[code]) + "\n<!-- SITE:visual:end -->"
        if "<!-- SITE:visual:begin -->" in s: s = re.sub(r"<!-- SITE:visual:begin -->[\s\S]*?<!-- SITE:visual:end -->", lambda m: vis, s)
        else: print(f"! marqueur SITE:visual absent de {f} : bloc non inséré")
        open(f, "w", encoding="utf-8").write(s)
    print("ok:", len(os.listdir(IMG)), "graphiques,", os.path.getsize("docs/index.html") // 1024, "Ko de page")

if __name__ == "__main__":
    main()
