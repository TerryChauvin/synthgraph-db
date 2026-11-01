"""Validation et chargement d'une extraction (extractions/<PMCID>.json) dans la base.

    python -I load.py check PMC1234567     # validation seule, rien n'est ecrit
    python -I load.py load  PMC1234567     # validation puis insertion (remplace l'existant)

Toute citation doit etre une sous-chaine exacte du texte normalise de l'article
(corpus/text/<PMCID>.txt), aux espaces pres. Une seule erreur bloque le chargement.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402
import canon  # noqa: E402

ANNOT_TYPES = {"resume", "objectif_etude", "pourquoi_ces_donnees", "comparaison_branches",
               "tendance_observee", "conclusion_auteurs", "limite_reproductibilite",
               # format 2 : *_auteurs = ce que dit l'article (citation obligatoire) ;
               # *_analyse = explication de Claude, non sourcee (pas de citation)
               "mecanisme_auteurs", "mecanisme_analyse", "securite_auteurs", "securite_analyse"}
ROUTE_KINDS = {"material", "intermediate", "device", "post_treatment", "calcul"}
ANNOT_REQUIRED = ("resume", "objectif_etude", "pourquoi_ces_donnees")
NAME_RE = re.compile(r"^[a-z][a-z0-9_]*$")
WORKUP = re.compile(r"wash|dry|filter|centrifug|calcin|anneal|sinter|rinse|collect|evaporat|quench", re.I)

# Grille de reproductibilite : informations attendues selon l'action de l'etape. Chaque case doit
# etre remplie (parametre dont le nom contient la cle) ou declaree dans `not_stated`.
EXPECTED_STEP = [
    (re.compile(r"calcin|anneal|sinter|pyroly|carboniz", re.I), ["temperature", "duration", "atmosphere", "heating_rate"]),
    (re.compile(r"heat|react|reflux|age|hydrothermal|solvothermal|microwave", re.I), ["temperature", "duration"]),
    (re.compile(r"\bdry|dried|drying", re.I), ["temperature", "duration"]),
    (re.compile(r"stir|mix|sonicat|dispers", re.I), ["duration"]),
    (re.compile(r"centrifug", re.I), ["speed", "duration"]),
    (re.compile(r"wash|rinse", re.I), ["wash_solvent", "repetitions"]),
    (re.compile(r"adjust_ph", re.I), ["ph"]),
]
EXPECTED_REAGENT = ["amount", "purity", "supplier"]       # reactifs qui entrent dans le produit ou la reaction
NO_GRID_ROLES = {"wash", "gas", "substrate"}
EXPECTED_ROUTE = ["yield"]


def expected_slots(action):
    for pattern, slots in EXPECTED_STEP:
        if pattern.search(action or ""):
            return slots
    return []


TEMP_UNITS = {"°c": lambda v: v + 273.15, "c": lambda v: v + 273.15, "k": lambda v: v,
              "°f": lambda v: (v - 32) * 5 / 9 + 273.15}
TIME_UNITS = {"s": 1, "sec": 1, "min": 60, "h": 3600, "hr": 3600, "hours": 3600, "hour": 3600,
              "d": 86400, "day": 86400, "days": 86400, "week": 604800, "weeks": 604800}
PRESSURE_UNITS = {"pa": 1, "kpa": 1e3, "mpa": 1e6, "gpa": 1e9, "bar": 1e5, "mbar": 100,
                  "atm": 101325, "torr": 133.322, "mtorr": 0.133322, "psi": 6894.76}
RATE_UNITS = {"°c/min": 1 / 60, "k/min": 1 / 60, "°c min-1": 1 / 60, "°c min−1": 1 / 60,
              "°c/h": 1 / 3600, "k/h": 1 / 3600, "°c/s": 1, "k/s": 1}


def to_si(name, value, unit):
    """Valeur normalisee quand la conversion est sans ambiguite, sinon (None, None)."""
    if value is None or not unit:
        return None, None
    u = unit.strip().lower().replace("º", "°").replace("˚", "°")
    # « °C min−1 », « °C·min–1 », « K min-1 » -> « °c/min »
    u = re.sub(r"[\s·.]*(min|h|s)\s*[−–-]\s*1$", r"/\1", u).replace(" ", "") if re.search(r"[/−–-]", u) else u
    u = {"minutes": "min", "minute": "min", "mins": "min", "hr": "h", "hrs": "h", "hours": "h",
         "seconds": "s", "second": "s", "mtorr": "mtorr"}.get(u, u)
    if name in ("heating_rate", "cooling_rate", "ramp_rate") or "ramp" in name:
        return (value * RATE_UNITS[u], "K/s") if u in RATE_UNITS else (None, None)
    if "temperature" in name:
        return (TEMP_UNITS[u](value), "K") if u in TEMP_UNITS else (None, None)
    if "duration" in name:
        return (value * TIME_UNITS[u], "s") if u in TIME_UNITS else (None, None)
    if "pressure" in name:
        return (value * PRESSURE_UNITS[u], "Pa") if u in PRESSURE_UNITS else (None, None)
    return None, None


def number_forms(v):
    forms = set()
    if float(v).is_integer():
        i = int(v)
        forms |= {str(i), f"{i:,}", f"{i:,}".replace(",", " "), f"{i:,}".replace(",", " "),
                  f"{i}.0"}
    s = repr(float(v))
    forms |= {s, s.replace(".", ","), s.replace("-", "−"), f"{float(v):,}"}
    if s.startswith("0."):
        forms.add(s[1:])
    forms |= {f.replace("-", "−") for f in list(forms)}
    forms |= {f.replace("-", "–") for f in list(forms) if f.startswith("-")}  # signe moins typographié en tiret demi-cadratin (2026-10-13)
    # notation scientifique écrite « 1.73 × 10−4 » (2026-10-13) : la mantisse et l'exposant doivent être dans la citation
    if v and (abs(float(v)) < 1e-3 or abs(float(v)) >= 1e5):
        m, e = f"{float(v):e}".split("e")
        m = m.rstrip("0").rstrip(".")
        e = int(e)
        mf = float(m)
        mants = {m} | {f"{mf:.{k}f}" for k in (1, 2, 3)}
        for ms in mants | {x.replace(".", ",") for x in mants}:
            for sep in (" × ", "×", " x ", "x", " ⋅ ", "·"):
                for es in {str(e), str(e).replace("-", "−"), str(e).replace("-", "–")}:
                    forms.add(f"{ms}{sep}10{es}")
                    forms.add(f"{ms}{sep}10^{es}")
    return forms


class Checker:
    def __init__(self, pmcid):
        self.pmcid = pmcid
        self.flat, self.raw = db.load_text(pmcid)
        self.errors, self.warnings = [], []
        self.n_quotes = 0

    def err(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")

    def quote(self, where, obj, required=True):
        """Verifie obj['quote'] et renvoie (quote, section, debut, fin)."""
        q = obj.get("quote")
        if not q or not isinstance(q, str) or not q.strip():
            if required:
                self.err(where, "citation manquante")
            return None, None, None, None
        q = db.norm(q)
        if len(q) < 8:
            self.err(where, f"citation trop courte pour etre tracable: {q!r}")
        pos = self.flat.find(q)
        self.n_quotes += 1
        if pos < 0:
            hint = ""
            for n in (40, 25, 15):
                p = self.flat.find(q[:n])
                if p >= 0:
                    hint = f" | texte de l'article a cet endroit: {self.flat[p:p + len(q) + 30]!r}"
                    break
            self.err(where, f"citation introuvable dans l'article: {q!r}{hint}")
            return q, None, None, None
        return q, db.section_at(self.raw, pos), pos, pos + len(q)

    def number(self, where, obj, key="value_num"):
        v = obj.get(key)
        if v is None:
            return None
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            self.err(where, f"{key} doit etre un nombre (sinon utiliser value_text): {v!r}")
            return None
        q = db.norm(obj.get("quote") or "")
        # valeur lue sur une figure : la citation est la legende, le nombre n'y figure pas
        if q and not obj.get("from_figure") and not any(f in q for f in number_forms(v)):
            self.err(where, f"la valeur {v} n'apparait pas dans sa citation {q!r} "
                            "(ne rien deduire ni convertir : recopier la valeur ecrite, "
                            "ou utiliser value_text)")
        return float(v)


def validate(pmcid, data):
    c = Checker(pmcid)
    if data.get("pmcid") != pmcid:
        c.err("pmcid", f"attendu {pmcid}, trouve {data.get('pmcid')!r}")
    routes = data.get("routes")
    if not isinstance(routes, list) or not routes:
        c.err("routes", "aucune voie de synthese")
        return c, []
    labels = [r.get("label") for r in routes]
    if len(set(labels)) != len(labels) or not all(isinstance(l, str) and l for l in labels):
        c.err("routes", f"labels absents ou en double: {labels}")
        return c, []
    by_label = {r["label"]: r for r in routes}

    # arbre : parents existants, pas de cycle, ordre parents d'abord
    order, seen = [], set()
    for r in routes:
        chain, cur = [], r
        while cur is not None and cur["label"] not in seen:
            if cur["label"] in [x["label"] for x in chain]:
                c.err(f"route {r['label']}", "cycle dans les parents")
                return c, []
            chain.append(cur)
            p = cur.get("parent")
            if p is not None and p not in by_label:
                c.err(f"route {cur['label']}", f"parent inconnu: {p!r}")
                return c, []
            cur = by_label.get(p) if p else None
        for x in reversed(chain):
            seen.add(x["label"])
            order.append(x)

    def source(r, key):
        while r is not None and not r.get(key):
            r = by_label.get(r.get("parent")) if r.get("parent") else None
        return r

    for r in order:
        w = f"route {r['label']}"
        c.quote(w, r)
        mat = r.get("material") or {}
        if not mat.get("name"):
            c.err(w, "material.name manquant")
        if not r.get("method") and not r.get("parent"):
            c.err(w, "method manquant")
        y = r.get("yield")
        if y:
            c.quote(f"{w} yield", y)
            c.number(f"{w} yield", y, "value")
        steps = r.get("steps") or []
        if not r.get("parent"):
            if not steps:
                c.err(w, "une voie sans parent doit decrire ses etapes")
            if not r.get("reagents"):
                c.warn(w, "aucun reactif")
        else:
            if not r.get("variations"):
                c.err(w, "une branche doit declarer au moins une variation par rapport a son parent")
        if [s.get("order") for s in steps] != list(range(1, len(steps) + 1)):
            c.err(w, "les etapes doivent etre numerotees 1, 2, 3... sans trou")

        # grille de reproductibilite (format 2) : chaque information attendue est soit extraite,
        # soit declaree « non cite » apres recherche dans l'article ; jamais oubliee
        # une voie de calcul (DFT, simulation) n'a ni rendement, ni reactifs, ni etapes de laboratoire
        if (data.get("format") or 1) >= 2 and r.get("kind") != "calcul":
            hint = "donner la valeur avec sa citation, ou l'ajouter a not_stated si l'article ne la donne pas"
            if not r.get("parent") and not r.get("yield") and "yield" not in (r.get("not_stated") or []):
                c.err(w, f"grille : rendement (yield) ni extrait ni declare non cite ({hint})")
            for g in r.get("reagents") or []:
                if (g.get("role") or "").lower() in NO_GRID_ROLES:
                    continue
                ns = g.get("not_stated") or []
                have = {"amount": g.get("amount") is not None or bool(g.get("amount_text")),
                        "purity": bool(g.get("purity")), "supplier": bool(g.get("supplier"))}
                # role intermediate : produit prepare par les auteurs (autre voie de l'article), ni purete ni fournisseur
                made_here = (g.get("role") or "").lower() == "intermediate"
                for slot in EXPECTED_REAGENT:
                    if not have[slot] and slot not in ns and not (made_here and slot != "amount"):
                        c.err(f"{w} reagent {g.get('name')!r}", f"grille : {slot} ni extrait ni declare non cite ({hint})")
                    if have[slot] and slot in ns:
                        c.err(f"{w} reagent {g.get('name')!r}", f"grille : {slot} a la fois extrait et declare non cite")
            for s in steps:
                names = [p.get("name") or "" for p in s.get("parameters") or []]
                ns = s.get("not_stated") or []
                slots = action_slots(s.get("action")) if (data.get("format") or 1) >= 3 else expected_slots(s.get("action"))
                for slot in slots:
                    found = any(slot in n for n in names)
                    if not found and slot not in ns:
                        c.err(f"{w} step {s.get('order')} ({s.get('action')})",
                              f"grille : {slot} ni extrait ni declare non cite ({hint})")
                    if found and slot in ns:
                        c.err(f"{w} step {s.get('order')} ({s.get('action')})",
                              f"grille : {slot} a la fois extrait et declare non cite")

        for i, g in enumerate(r.get("reagents") or []):
            wg = f"{w} reagent[{i}] {g.get('name')!r}"
            if not g.get("name"):
                c.err(wg, "name manquant")
            c.quote(wg, g)
            c.number(wg, g, "amount")
            if g.get("amount") is not None and not g.get("unit"):
                c.err(wg, "quantite sans unite")
            sq = c.quote(f"{wg} supplier_quote", {"quote": g.get("supplier_quote")}, required=False)[0] or ""
            for key in ("purity", "supplier"):
                if g.get(key) and db.norm(str(g[key])) not in db.norm(g.get("quote") or "") + " " + sq:
                    c.err(wg, f"{key} {g[key]!r} absent de quote et de supplier_quote : recopier la valeur "
                              "telle qu'ecrite et citer la phrase qui la donne dans supplier_quote")

        for s in steps:
            ws = f"{w} step {s.get('order')}"
            if not s.get("action"):
                c.err(ws, "action manquante")
            c.quote(ws, s)
            for j, p in enumerate(s.get("parameters") or []):
                wp = f"{ws} param[{j}] {p.get('name')!r}"
                name = p.get("name") or ""
                if not NAME_RE.match(name):
                    c.err(wp, "name doit etre en snake_case anglais (temperature, duration, ph...)")
                c.quote(wp, p)
                v = c.number(wp, p)
                if v is None and not p.get("value_text"):
                    c.err(wp, "ni value_num ni value_text")
                if v is not None:
                    if ("temperature" in name or "duration" in name or name in ("heating_rate", "cooling_rate")) \
                            and not p.get("unit"):
                        c.err(wp, "unite manquante")
                    if name == "ph" and not 0 <= v <= 14:
                        c.err(wp, f"pH hors de 0-14: {v}")
                    if "duration" in name and v <= 0:
                        c.err(wp, f"duree non positive: {v}")
                    si, _ = to_si(name, v, p.get("unit"))
                    if "temperature" in name and si is not None and not 0 < si < 4300:
                        c.err(wp, f"temperature physiquement impossible: {v} {p.get('unit')}")
            for j, e in enumerate(s.get("equipment") or []):
                we = f"{ws} equipment[{j}]"
                if not e.get("type"):
                    c.err(we, "type manquant")
                c.quote(we, e)

        src = source(by_label.get(r.get("parent")) if r.get("parent") else None, "steps")
        src_steps = (src or {}).get("steps") or []
        src_reag, anc = [], by_label.get(r.get("parent")) if r.get("parent") else None
        while anc is not None:
            src_reag += anc.get("reagents") or []
            anc = by_label.get(anc.get("parent")) if anc.get("parent") else None
        for i, v in enumerate(r.get("variations") or []):
            wv = f"{w} variation[{i}] {v.get('parameter')!r}"
            if not v.get("parameter"):
                c.err(wv, "parameter manquant")
            c.quote(wv, v)
            num = c.number(wv, v)
            if num is None and not v.get("value_text"):
                c.err(wv, "ni value_num ni value_text")
            so = v.get("step_order")
            names = {p.get("name") for s in src_steps for p in (s.get("parameters") or [])
                     if so is None or s.get("order") == so}
            names |= {g.get("name") for g in src_reag}
            if so is not None and so not in [s.get("order") for s in src_steps]:
                c.err(wv, f"step_order {so} n'existe pas dans le protocole herite")
            elif v.get("parameter") not in names:
                c.warn(wv, "ne correspond a aucun parametre ni reactif du protocole herite "
                           f"(noms disponibles: {sorted(n for n in names if n)}) ; "
                           "reprendre le meme nom si c'est le meme parametre")

        for key, field in (("characterizations", "technique"), ("outcomes", "property")):
            for i, o in enumerate(r.get(key) or []):
                wo = f"{w} {key}[{i}] {o.get(field)!r}"
                if not o.get(field):
                    c.err(wo, f"{field} manquant")
                c.quote(wo, o)
                if key == "outcomes":
                    v = c.number(wo, o)
                    if v is None and not o.get("value_text"):
                        c.err(wo, "ni value_num ni value_text")
        if not r.get("outcomes") and r.get("succeeded") is None:
            c.warn(w, "ni resultat (outcomes) ni indication de succes/echec")

    annots = data.get("annotations") or []
    types = [a.get("type") for a in annots if not a.get("route")]
    for t in ANNOT_REQUIRED:
        if t not in types:
            c.err("annotations", f"annotation d'article obligatoire absente: {t}")
    if any(r.get("parent") for r in routes) and \
            "comparaison_branches" not in [a.get("type") for a in annots]:
        c.err("annotations", "des branches existent : annotation comparaison_branches obligatoire")
    if (data.get("format") or 1) >= 2:
        all_types = [a.get("type") or "" for a in annots]
        for family in ("mecanisme", "securite"):
            if not any(t.startswith(family) for t in all_types):
                c.err("annotations", f"format 2 : au moins une annotation {family}_auteurs ou {family}_analyse")
        if "method_sources" not in data:
            c.err("method_sources", "format 2 : cle obligatoire (liste vide si l'article ne renvoie a aucune "
                                    "publication pour sa methode)")
        for r in routes:
            if r.get("kind") and r["kind"] not in ROUTE_KINDS:
                c.err(f"route {r['label']}", f"kind inconnu (autorises: {sorted(ROUTE_KINDS)})")
        ref_file = db.ROOT / "corpus" / "refs" / f"{pmcid}.json"
        known = json.loads(ref_file.read_text(encoding="utf-8")) if ref_file.exists() else None
        for i, m in enumerate(data.get("method_sources") or []):
            wm = f"method_sources[{i}] {m.get('ref_id')!r}"
            c.quote(wm, m)
            if m.get("route") and m["route"] not in by_label:
                c.err(wm, f"route inconnue: {m['route']!r}")
            if known is not None and m.get("ref_id") not in known:
                c.err(wm, "ref_id absent de corpus/refs/<PMCID>.json (recopier l'identifiant entre [[ ]])")
        for i, m in enumerate(data.get("comparisons") or []):
            wm = f"comparisons[{i}] {m.get('material')!r}"
            c.quote(wm, m)
            if not m.get("material") or not m.get("property"):
                c.err(wm, "material et property obligatoires")
            if m.get("value_num") is None and not m.get("value_text"):
                c.err(wm, "value_num ou value_text obligatoire")
            if m.get("route") and m["route"] not in by_label:
                c.err(wm, f"route inconnue: {m['route']!r}")
            if m.get("ref_id") and known is not None and m["ref_id"] not in known:
                c.err(wm, "ref_id absent de corpus/refs/<PMCID>.json")
    for i, a in enumerate(annots):
        wa = f"annotation[{i}] {a.get('type')!r}"
        if a.get("type") not in ANNOT_TYPES:
            c.err(wa, f"type inconnu (autorises: {sorted(ANNOT_TYPES)})")
        sourced = (a.get("type") or "").startswith(("mecanisme_", "securite_"))
        if sourced and a["type"].endswith("_auteurs") and not a.get("quote"):
            c.err(wa, "une annotation *_auteurs rapporte ce que dit l'article : citation obligatoire")
        if sourced and a["type"].endswith("_analyse") and a.get("quote"):
            c.err(wa, "une annotation *_analyse est une explication de Claude : pas de citation "
                      "(ce que disent les auteurs va dans *_auteurs)")
        if not a.get("text") or len(a["text"]) < 40:
            c.err(wa, "texte absent ou trop court")
        if a.get("route") and a["route"] not in by_label:
            c.err(wa, f"route inconnue: {a['route']!r}")
        c.quote(wa, a, required=False)
    # inventaire des echantillons (RUNBOOK, depuis le palier 2) : chaque echantillon a sa voie ou une raison
    for i, s in enumerate(data.get("sample_inventory") or []):
        ws = f"sample_inventory[{i}] {s.get('sample')!r}"
        if s.get("route") and s["route"] not in by_label:
            c.err(ws, f"route inconnue: {s['route']!r}")
        if not s.get("route") and not s.get("why"):
            c.err(ws, "echantillon sans voie : donner la raison dans 'why'")
    for i, d in enumerate(data.get("doubts") or []):
        if not d.get("issue"):
            c.err(f"doubts[{i}]", "issue manquant")
    if (data.get("format") or 1) >= 3:
        validate_v3(c, data, order, by_label)
    return c, order


# ---------------------------------------------------------------- format 3 (architecture v2, 28/10/2026)
_VOCAB = None


def vocab_index():
    global _VOCAB
    if _VOCAB is None:
        import vocab
        _VOCAB = vocab.index_noms()
    return _VOCAB


def vocab_name(typ, name, prefix_ok=False):
    """Nom officiel (ou ajout en attente) correspondant à `name`, None sinon ; avec prefix_ok, « nom_precision » est admis."""
    import vocab
    idx, _ = vocab_index()
    n = vocab.norm(name)
    if n in idx[typ]:
        return idx[typ][n]
    if prefix_ok:
        parts = n.split("_")
        for k in range(len(parts) - 1, 0, -1):
            base = "_".join(parts[:k])
            if base in idx[typ]:
                return idx[typ][base]
    return None


def action_slots(action):
    name = vocab_name("action", action or "")
    if name is None:
        return []
    return vocab_index()[1][("action", name)].get("cases") or []


SUSPECT = {  # motif d'une valeur présente dans la citation d'une étape alors que la case est déclarée « non cité »
    "temperature": r"\d\s?°\s?C|\d\s?K\b|room temperature",
    "duration": r"\d\s?(h|hr|hrs|hours?|min|minutes?|days?)\b|overnight",
    "heating_rate": r"°\s?C\s?/?\s?min|K\s?/?\s?min",
    "atmosphere": r"\b(air|N2|nitrogen|argon|Ar|vacuum|H2)\b",
    "centrifuge_speed": r"\d\s?(rpm|×\s?g)",
    "stirring_speed": r"\d\s?rpm",
    "repetitions": r"(three|two|several|thrice|twice|\d)\s*(times|×)|thrice|twice",
    "ph": r"\bpH\b",
    "power": r"\d\s?W\b",
    "fill_fraction": r"\d\s?%\s?(of|fill)|filled",
    "cooling": r"cool(ed|ing)",
}


GENERIQUE = re.compile(r"^(other|others|autre|misc|miscellaneous|unknown|generic|various)(_|$)", re.I)


def validate_v3(c, data, order, by_label):
    """Contrôles de l'architecture v2 : noms du vocabulaire, grille par technique, réglages structurés,
    lien résultat → mesure, « non cité » suspects (avertissements)."""
    import re as _re
    hint_v = "nom absent du vocabulaire : `python3 -I vocab.py cherche <PMCID> \"…\"` puis, si rien ne convient, `vocab.py ajoute`"
    _, entries = vocab_index()
    char_ids = {}   # id -> (route label, technique officielle)
    interdit = "nom générique interdit (other, autre…) : choisir un nom de la liste (`vocab.py cherche`) ou en ajouter un avec sa définition (`vocab.py ajoute`)"
    for r in order:
        noms = [("méthode", m) for m in r.get("methods") or []]
        noms += [("action", s.get("action")) for s in r.get("steps") or []]
        noms += [("paramètre", p.get("name")) for s in r.get("steps") or [] for p in s.get("parameters") or []]
        noms += [("technique", ch.get("technique")) for ch in r.get("characterizations") or []]
        noms += [("réglage", st.get("name")) for ch in r.get("characterizations") or [] for st in ch.get("settings") or []]
        noms += [("propriété", o.get("property")) for o in r.get("outcomes") or []]
        for typ, n in noms:
            if n and GENERIQUE.match(str(n)):
                c.err(f"route {r['label']}", f"{typ} {n!r} : {interdit}")
    for r in order:
        w = f"route {r['label']}"
        if not r.get("parent") and r.get("kind") != "calcul":
            ms = r.get("methods")
            if not ms:
                c.err(w, "format 3 : `methods` obligatoire pour une voie de base (liste de méthodes du vocabulaire)")
            for m in ms or []:
                if vocab_name("methode", m) is None:
                    c.err(w, f"méthode {m!r} : {hint_v}")
        for s in r.get("steps") or []:
            ws = f"{w} step {s.get('order')}"
            if vocab_name("action", s.get("action") or "") is None:
                c.err(ws, f"action {s.get('action')!r} : {hint_v}")
            for p in s.get("parameters") or []:
                if vocab_name("parametre", p.get("name") or "", prefix_ok=True) is None:
                    c.err(f"{ws} param {p.get('name')!r}", hint_v)
            q = s.get("quote") or ""
            for slot in s.get("not_stated") or []:
                pat = SUSPECT.get(slot)
                if pat and _re.search(pat, q, _re.I):
                    c.warn(ws, f"« non cité » suspect : {slot} déclaré absent alors que la citation de l'étape contient un motif de cette case")
        for i, ch in enumerate(r.get("characterizations") or []):
            wc = f"{w} characterizations[{i}] {ch.get('technique')!r}"
            cid = ch.get("id")
            if not cid:
                c.err(wc, "format 3 : `id` obligatoire (identifiant unique de la mesure, repris par outcomes[].measured_by)")
            elif cid in char_ids:
                c.err(wc, f"id {cid!r} en double")
            tech = vocab_name("technique", ch.get("technique") or "")
            if tech is None:
                c.err(wc, f"technique : {hint_v}")
            if cid:
                char_ids[cid] = (r["label"], tech)
            if ch.get("conditions"):
                c.warn(wc, "format 3 : `conditions` en texte libre déconseillé, utiliser `settings` (un réglage par entrée, avec citation)")
            names = []
            for j, st in enumerate(ch.get("settings") or []):
                wst = f"{wc} settings[{j}] {st.get('name')!r}"
                if vocab_name("reglage", st.get("name") or "") is None:
                    c.err(wst, hint_v)
                names.append(vocab_name("reglage", st.get("name") or "") or st.get("name"))
                c.quote(wst, st)
                v = c.number(wst, st)
                if v is None and not st.get("value_text"):
                    c.err(wst, "ni value_num ni value_text")
            ns = ch.get("not_stated") or []
            if tech:
                for reg in entries[("technique", tech)].get("reglages") or []:
                    if reg not in names and reg not in ns:
                        c.err(wc, f"grille de mesure : réglage {reg} ni extrait (settings) ni déclaré non cité (not_stated)")
                    if reg in names and reg in ns:
                        c.err(wc, f"grille de mesure : réglage {reg} à la fois extrait et déclaré non cité")
    for r in order:
        w = f"route {r['label']}"
        anc, lab = set(), r["label"]
        while lab:
            anc.add(lab)
            lab = by_label[lab].get("parent")
        for i, o in enumerate(r.get("outcomes") or []):
            wo = f"{w} outcomes[{i}] {o.get('property')!r}"
            prop = vocab_name("propriete", o.get("property") or "", prefix_ok=True)
            if prop is None:
                c.err(wo, f"propriété : {hint_v}")
                continue

            techs = entries[("propriete", prop)].get("techniques") or []
            mb = o.get("measured_by")
            if not techs:
                continue
            if not mb:
                c.err(wo, "format 3 : `measured_by` obligatoire (id de la mesure dans cette voie ou une voie parente, "
                          "ou \"not_stated\" si l'article ne dit pas comment la valeur a été mesurée)")
            elif mb != "not_stated":
                if mb not in char_ids:
                    c.err(wo, f"measured_by {mb!r} : aucune caractérisation avec cet id")
                elif char_ids[mb][0] not in anc:
                    c.err(wo, f"measured_by {mb!r} : mesure d'une autre voie ({char_ids[mb][0]}), ni cette voie ni un parent")
                elif char_ids[mb][1] and char_ids[mb][1] not in techs:
                    c.warn(wo, f"measured_by {mb!r} : technique {char_ids[mb][1]} inhabituelle pour {prop} (attendu : {', '.join(techs)})")


def completeness(route, by_label):
    """Part des informations necessaires a la reproduction qui sont presentes (0-1)."""
    def inherited(key):
        r = route
        while r is not None and not r.get(key):
            r = by_label.get(r.get("parent")) if r.get("parent") else None
        return (r or {}).get(key) or []

    # les reactifs propres a une branche (additif, dopant) s'ajoutent a ceux de ses ancetres
    reagents, r = [], route
    while r is not None:
        reagents += r.get("reagents") or []
        r = by_label.get(r.get("parent")) if r.get("parent") else None
    steps = inherited("steps")
    params = [p for s in steps for p in (s.get("parameters") or [])]
    precursors = [g for g in reagents if (g.get("role") or "").lower() not in ("solvent", "solvant")]
    checks = [
        bool(precursors) and all(g.get("amount") is not None or g.get("amount_text") for g in precursors),
        any((g.get("role") or "").lower() in ("solvent", "solvant") for g in reagents),
        any("temperature" in (p.get("name") or "") for p in params),
        any("duration" in (p.get("name") or "") for p in params),
        any(WORKUP.search(s.get("action") or "") for s in steps),
        bool((route.get("material") or {}).get("formula")),
        bool(route.get("outcomes") or route.get("characterizations")),
        len(steps) >= 3,
    ]
    return round(sum(checks) / len(checks), 3)


def material_id(con, m):
    vals = (m.get("name"), m.get("formula"), m.get("phase"), m.get("morphology"))
    row = con.execute("SELECT id FROM materials WHERE name IS ? AND formula IS ? AND phase IS ?"
                      " AND morphology IS ?", vals).fetchone()
    if row:
        if m.get("family"):
            con.execute("UPDATE materials SET family = COALESCE(family, ?) WHERE id = ?",
                        (m["family"], row["id"]))
        return row["id"]
    return con.execute("INSERT INTO materials (name, formula, phase, morphology, family)"
                       " VALUES (?,?,?,?,?)", vals + (m.get("family"),)).lastrowid


def insert(con, pmcid, data, order, c):
    paper = con.execute("SELECT * FROM papers WHERE pmcid = ?", (pmcid,)).fetchone()
    if paper is None:
        raise SystemExit(f"{pmcid} absent de la table papers")
    pid = paper["id"]
    # un rechargement ne doit pas rouvrir les doutes deja tranches
    solved = {d["issue"]: d["resolution"] for d in con.execute(
        "SELECT issue, resolution FROM doubts WHERE paper_id=? AND status='resolved'", (pid,))}
    for t in ("synthesis_routes", "annotations", "doubts", "method_sources", "comparisons"):
        con.execute(f"DELETE FROM {t} WHERE paper_id = ?", (pid,))
    by_label = {r["label"]: r for r in order}
    ids = {}
    char_db = {}   # id de mesure (format 3) -> characterizations.id

    def q(obj, required=True):
        return c.quote("", obj, required)

    for r in order:
        quote = q(r)
        y = r.get("yield") or {}
        ids[r["label"]] = rid = con.execute(
            "INSERT INTO synthesis_routes (paper_id, material_id, parent_route_id, branch_label,"
            " is_baseline, method, scale, yield_value, yield_unit, yield_quote, succeeded,"
            " missing_fields, completeness_score, quote, section, char_start, char_end)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (pid, material_id(con, r.get("material") or {}), ids.get(r.get("parent")), r["label"],
             int(bool(r.get("is_baseline", not r.get("parent")))),
             r.get("method") or by_label.get(r.get("parent"), {}).get("method"), r.get("scale"),
             y.get("value"), y.get("unit"), db.norm(y["quote"]) if y.get("quote") else None,
             None if r.get("succeeded") is None else int(bool(r["succeeded"])),
             json.dumps(r.get("missing_fields") or [], ensure_ascii=False),
             completeness(r, by_label)) + quote).lastrowid
        con.execute("UPDATE synthesis_routes SET kind=? WHERE id=?", (r.get("kind") or "material", rid))
        gaps = [("route", None, None, n) for n in r.get("not_stated") or []]
        gaps += [("reagent", None, g["name"], n) for g in r.get("reagents") or [] for n in g.get("not_stated") or []]
        gaps += [("step", s["order"], None, n) for s in r.get("steps") or [] for n in s.get("not_stated") or []]
        con.executemany("INSERT INTO not_stated (route_id, scope, step_order, reagent, name) VALUES (?,?,?,?,?)",
                        [(rid,) + g for g in gaps])
        for v in r.get("variations") or []:
            con.execute(
                "INSERT INTO route_variations (route_id, parameter, step_order, value_num, value_text,"
                " unit, parent_value, from_figure, quote, section, char_start, char_end)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (rid, v["parameter"], v.get("step_order"), v.get("value_num"), v.get("value_text"),
                 v.get("unit"), None if v.get("parent_value") is None else str(v["parent_value"]),
                 v.get("from_figure")) + q(v))
        for g in r.get("reagents") or []:
            con.execute(
                "INSERT INTO reagents (route_id, name, formula, role, amount, unit, amount_text, purity,"
                " supplier, supplier_quote, quote, section, char_start, char_end)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (rid, g["name"], g.get("formula"), g.get("role"), g.get("amount"), g.get("unit"),
                 g.get("amount_text"), g.get("purity"), g.get("supplier"),
                 db.norm(g["supplier_quote"]) if g.get("supplier_quote") else None) + q(g))
        for s in r.get("steps") or []:
            sid = con.execute(
                "INSERT INTO steps (route_id, step_order, action, description, quote, section,"
                " char_start, char_end) VALUES (?,?,?,?,?,?,?,?)",
                (rid, s["order"], s["action"], s.get("description")) + q(s)).lastrowid
            for p in s.get("parameters") or []:
                si, usi = to_si(p["name"], p.get("value_num"), p.get("unit"))
                con.execute(
                    "INSERT INTO parameters (step_id, name, value_num, value_text, unit, value_si,"
                    " unit_si, from_figure, quote, section, char_start, char_end) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (sid, p["name"], p.get("value_num"), p.get("value_text"), p.get("unit"), si, usi,
                     p.get("from_figure")) + q(p))
            for e in s.get("equipment") or []:
                con.execute(
                    "INSERT INTO equipment (step_id, type, detail, quote, section, char_start, char_end)"
                    " VALUES (?,?,?,?,?,?,?)", (sid, e["type"], e.get("detail")) + q(e))
        for m in r.get("methods") or []:
            con.execute("INSERT INTO route_methods (route_id, method) VALUES (?,?)", (rid, m))
        for o in r.get("characterizations") or []:
            chid = con.execute(
                "INSERT INTO characterizations (route_id, technique, result, instrument, conditions, quote,"
                " section, char_start, char_end) VALUES (?,?,?,?,?,?,?,?,?)",
                (rid, o["technique"], o.get("result"), o.get("instrument"), o.get("conditions")) + q(o)).lastrowid
            if o.get("id"):
                char_db[o["id"]] = chid
                con.execute("UPDATE characterizations SET char_key=? WHERE id=?", (o["id"], chid))
            for st in o.get("settings") or []:
                con.execute(
                    "INSERT INTO char_settings (characterization_id, name, value_num, value_text, unit, from_figure,"
                    " quote, section, char_start, char_end) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (chid, st["name"], st.get("value_num"), st.get("value_text"), st.get("unit"),
                     st.get("from_figure")) + q(st))
            con.executemany("INSERT INTO not_stated (route_id, scope, step_order, reagent, name) VALUES (?,?,?,?,?)",
                            [(rid, "characterization", None, o.get("id") or o["technique"], n) for n in o.get("not_stated") or []])
        for o in r.get("outcomes") or []:
            mb = o.get("measured_by")
            con.execute(
                "INSERT INTO outcomes (route_id, property, value_num, value_text, unit, from_figure, quote,"
                " section, char_start, char_end, measured_by, measured_status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (rid, o["property"], o.get("value_num"), o.get("value_text"), o.get("unit"),
                 o.get("from_figure")) + q(o) + (char_db.get(mb), "non_cite" if mb == "not_stated" else ("lie" if mb else None)))
    for a in data.get("annotations") or []:
        con.execute(
            "INSERT INTO annotations (paper_id, route_id, type, text, source, quote, section, char_start,"
            " char_end) VALUES (?,?,?,?,?,?,?,?,?)",
            (pid, ids.get(a.get("route")), a["type"], a["text"],
             "auteurs" if a["type"] in ("mecanisme_auteurs", "securite_auteurs") else "claude")
            + q(a, required=False))
    ref_file = db.ROOT / "corpus" / "refs" / f"{pmcid}.json"
    refs = json.loads(ref_file.read_text(encoding="utf-8")) if ref_file.exists() else {}
    for m in data.get("method_sources") or []:
        ref = refs.get(m.get("ref_id"), {})
        con.execute(
            "INSERT INTO method_sources (paper_id, route_id, ref_id, role, authors, title, journal, year, doi,"
            " pmid, source_pmcid, quote, section, char_start, char_end) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (pid, ids.get(m.get("route")), m["ref_id"], m.get("role"), ref.get("authors"),
             ref.get("title") or ref.get("raw"), ref.get("journal"), ref.get("year"), ref.get("doi"),
             ref.get("pmid"), ref.get("pmcid")) + q(m))
    for m in data.get("comparisons") or []:
        con.execute(
            "INSERT INTO comparisons (paper_id, route_id, material, property, value_num, value_text, unit, conditions,"
            " ref_id, quote, section, char_start, char_end) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (pid, ids.get(m.get("route")), m["material"], m["property"], m.get("value_num"), m.get("value_text"),
             m.get("unit"), m.get("conditions"), m.get("ref_id")) + q(m))
    for d in data.get("doubts") or []:
        con.execute("INSERT INTO doubts (paper_id, location, issue, resolution, status) VALUES (?,?,?,?,?)",
                    (pid, d.get("where"), d["issue"], solved.get(d["issue"]),
                     "resolved" if d["issue"] in solved else "open"))
    # les verdicts du critique scientifique suivent la voie par son label a travers les rechargements
    if con.execute("SELECT 1 FROM sqlite_master WHERE name='plausibility'").fetchone():
        con.execute("UPDATE plausibility SET route_id=(SELECT id FROM synthesis_routes r WHERE r.paper_id=? "
                    "AND r.branch_label=plausibility.branch_label) WHERE paper_id=?", (pid, pid))
    seq = paper["seq"]
    if seq is None:
        seq = con.execute("SELECT COALESCE(MAX(seq), 0) + 1 FROM papers").fetchone()[0]
    con.execute("UPDATE papers SET status='extracted', seq=?, palier=?, extracted_at=?, format_version=? WHERE id=?",
                (seq, (seq - 1) // db.PALIER_SIZE + 1, db.now(), data.get("format") or 1, pid))
    canon.apply_paper(con, pid)   # noms canoniques (canon.py), colonnes séparées des noms bruts
    con.commit()
    return seq


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("check", "load"):
        raise SystemExit(__doc__)
    mode, pmcid = sys.argv[1], sys.argv[2]
    path = db.EXTRACT_DIR / f"{pmcid}.json"   # SYNTHESE_EXTRACT_DIR pour la v2 (extractions_v2/)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise SystemExit(f"ERREUR lecture {path.name}: {e}")
    c, order = validate(pmcid, data)
    for w in c.warnings:
        print("AVERTISSEMENT", w)
    for e in c.errors:
        print("ERREUR", e)
    n_branch = sum(1 for r in order if r.get("parent"))
    print(f"{pmcid}: {len(order)} voies ({n_branch} branches), {c.n_quotes} citations verifiees, "
          f"{len(c.errors)} erreurs, {len(c.warnings)} avertissements, "
          f"{len(data.get('doubts') or [])} doutes")
    if c.errors:
        raise SystemExit(1)
    if mode == "load":
        seq = insert(db.connect(), pmcid, data, order, c)
        print(f"charge (publication n°{seq})")


if __name__ == "__main__":
    main()
