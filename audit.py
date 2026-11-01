"""Audit de palier (toutes les 50 publications).

    python -I audit.py 1          # audite le palier 1 (publications 1 a 50)

Ecrit audits/palier_NNN.md, remplit audit_findings et exporte synthese_dump.sql.
Les controles automatiques ne remplacent pas la relecture : le rapport liste un
echantillon que l'orchestrateur doit verifier a la main, puis consigner dans
audits/palier_NNN_relecture.md (le palier n'est valide qu'avec ce fichier).
"""
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402
from load import ANNOT_REQUIRED, number_forms, to_si  # noqa: E402
from state import needs_full_review  # noqa: E402

ELEMENTS = set("""H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn
Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu
Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Th U""".split())
ELEMENT_NAMES = {
    "lithium": "Li", "boron": "B", "boric": "B", "borohydride": "B", "sodium": "Na", "magnesium": "Mg",
    "alumin": "Al", "silic": "Si", "silane": "Si", "teos": "Si", "phosph": "P", "sulf": "S", "sulph": "S",
    "thio": "S", "cystein": "S", "cystine": "S", "glutathione": "S", "methionine": "S", "chlor": "Cl", "potassium": "K", "calcium": "Ca", "scandium": "Sc", "titan": "Ti",
    "vanad": "V", "chrom": "Cr", "mangan": "Mn", "iron": "Fe", "ferr": "Fe", "cobalt": "Co",
    "nickel": "Ni", "copper": "Cu", "cupr": "Cu", "zinc": "Zn", "gallium": "Ga", "german": "Ge",
    "arsen": "As", "selen": "Se", "brom": "Br", "rubidium": "Rb", "strontium": "Sr", "yttrium": "Y",
    "zircon": "Zr", "niob": "Nb", "molybd": "Mo", "ruthen": "Ru", "rhod": "Rh", "pallad": "Pd",
    "silver": "Ag", "cadmium": "Cd", "indium": "In", "tin ": "Sn", "stann": "Sn", "antimon": "Sb",
    "tellur": "Te", "iod": "I", "cesium": "Cs", "caesium": "Cs", "barium": "Ba", "lanthan": "La",
    "cerium": "Ce", "ceric": "Ce", "cerous": "Ce", "neodym": "Nd", "samarium": "Sm", "europ": "Eu",
    "gadolin": "Gd", "terbium": "Tb", "erbium": "Er", "ytterb": "Yb", "hafn": "Hf", "tantal": "Ta",
    "tungst": "W", "platin": "Pt", "gold": "Au", "aur": "Au", "lead": "Pb", "plumb": "Pb",
    "bismuth": "Bi", "fluor": "F", "methylammonium": "N", "formamidinium": "N",
}
C_WORDS = re.compile(r"carbon|graphit|graphene|glucose|sucrose|citr|acet|urea|melamine|oxal|"
                     r"ethanol|methanol|glycol|polymer|ctab|pvp|amine|imidazol|terephthal|acid|"
                     r"oleic|oleyl|octadecene|dmf|formamid|benzene|toluene|alkoxide|propoxide|"
                     r"butoxide|ethoxide|methyl|ethyl|carbide", re.I)
N_WORDS = re.compile(r"nitrat|ammoni|urea|melamine|amine|nitrogen|\bN2\b|NH3|imidazol|dmf|formamid|"
                     r"hydrazine|azide|nitride|cyan|pyridine|nitric", re.I)
SOLVENT_BP = {"water": 100, "h2o": 100, "ethanol": 78, "methanol": 65, "acetone": 56,
              "isopropanol": 82, "2-propanol": 82, "dmf": 153, "dimethylformamide": 153,
              "ethylene glycol": 197, "toluene": 111, "hexane": 69, "acetonitrile": 82,
              "dmso": 189, "chloroform": 61, "octadecene": 315, "oleylamine": 350, "glycerol": 290}
PRESSURIZED = re.compile(r"autoclave|sealed|reflux|solvothermal|hydrothermal|microwave|teflon|"
                         r"pressure|bomb|parr|condenser|closed", re.I)
WET_ACTION = re.compile(r"react|heat|stir|age|mix|dissolv|precipit|grow|crystalli", re.I)
THERMAL_ACTION = re.compile(r"calcin|sinter|anneal|pyroly|carboniz", re.I)
NON_OXIDE = re.compile(r"sulfide|sulphide|selenide|telluride|nitride|carbide|phosphide|MXene", re.I)
QUOTED = ("synthesis_routes", "route_variations", "reagents", "steps", "parameters", "equipment",
          "characterizations", "outcomes", "annotations")


def elements_of(formula):
    # cations organiques des perovskites hybrides : FA = formamidinium, MA = methylammonium
    f, extra = formula or "", set()
    if re.search(r"FA|MA(?![a-z])", f):
        f, extra = re.sub(r"FA|MA(?![a-z])", "", f), {"C", "N", "H"}
    return {t for t in re.findall(r"[A-Z][a-z]?", f) if t in ELEMENTS} | extra


def reagent_elements(g):
    els = elements_of(g["formula"])
    name = (g["name"] or "").lower() + " "
    els |= {el for word, el in ELEMENT_NAMES.items() if word in name}
    els |= elements_of(" ".join(t for t in re.findall(r"[A-Z][A-Za-z0-9()·.]*\d[A-Za-z0-9()·.]*",
                                                      g["name"] or "")))
    text = f"{g['name']} {g['formula'] or ''}"
    if C_WORDS.search(text):
        els.add("C")
    if N_WORDS.search(text):
        els.add("N")
    return els


class Audit:
    def __init__(self, con, palier):
        self.con, self.palier, self.findings = con, palier, []
        self.papers = con.execute(
            "SELECT * FROM papers WHERE status='extracted' AND palier=? ORDER BY seq", (palier,)).fetchall()
        self.ids = [p["id"] for p in self.papers]
        self.pm = {p["id"]: p["pmcid"] for p in self.papers}
        self.texts = {p["id"]: db.load_text(p["pmcid"])[0] for p in self.papers}
        self.routes = self.q("SELECT * FROM synthesis_routes WHERE paper_id IN ({ids}) ORDER BY id")
        self.by_id = {r["id"]: r for r in self.routes}

    def q(self, sql, *args):
        return self.con.execute(sql.replace("{ids}", ",".join(map(str, self.ids)) or "NULL"), args).fetchall()

    def add(self, check, severity, paper_id, target, desc, route_id=None):
        self.findings.append((check, severity, paper_id, route_id, target, desc))

    def inherited(self, route, table):
        """Lignes de `table` de l'ancetre le plus proche qui en possede."""
        r = route
        while r is not None:
            rows = self.con.execute(f"SELECT * FROM {table} WHERE route_id=?", (r["id"],)).fetchall()
            if rows:
                return rows
            r = self.by_id.get(r["parent_route_id"])
        return []

    def all_reagents(self, route):
        """Reactifs de la voie et de tous ses ancetres (ceux d'une branche s'ajoutent)."""
        rows, r = [], route
        while r is not None:
            rows += self.con.execute("SELECT * FROM reagents WHERE route_id=?", (r["id"],)).fetchall()
            r = self.by_id.get(r["parent_route_id"])
        return rows

    # ---- citations -------------------------------------------------------
    def citations(self):
        n = 0
        joins = {
            "synthesis_routes": "t.paper_id", "annotations": "t.paper_id",
            "route_variations": "(SELECT paper_id FROM synthesis_routes WHERE id=t.route_id)",
            "reagents": "(SELECT paper_id FROM synthesis_routes WHERE id=t.route_id)",
            "steps": "(SELECT paper_id FROM synthesis_routes WHERE id=t.route_id)",
            "characterizations": "(SELECT paper_id FROM synthesis_routes WHERE id=t.route_id)",
            "outcomes": "(SELECT paper_id FROM synthesis_routes WHERE id=t.route_id)",
            "parameters": "(SELECT r.paper_id FROM steps s JOIN synthesis_routes r ON r.id=s.route_id WHERE s.id=t.step_id)",
            "equipment": "(SELECT r.paper_id FROM steps s JOIN synthesis_routes r ON r.id=s.route_id WHERE s.id=t.step_id)",
        }
        for table in QUOTED:
            for row in self.q(f"SELECT t.*, {joins[table]} AS pid FROM {table} t WHERE {joins[table]} IN ({{ids}})"):
                if row["quote"] is None:
                    continue
                n += 1
                flat, target = self.texts[row["pid"]], f"{table}#{row['id']}"
                if flat[row["char_start"] or 0: row["char_end"] or 0] != row["quote"]:
                    sev = "bloquant" if flat.find(row["quote"]) < 0 else "avertissement"
                    self.add("citation", sev, row["pid"], target,
                             "citation absente du texte de l'article" if sev == "bloquant"
                             else "position de la citation incoherente (recharger l'extraction)")
                for col in ("value_num", "amount"):
                    # valeur lue sur figure : la citation est la legende, meme regle que load.py
                    if col in row.keys() and row[col] is not None and \
                            not ("from_figure" in row.keys() and row["from_figure"]) and \
                            not any(f in row["quote"] for f in number_forms(row[col])):
                        self.add("citation", "bloquant", row["pid"], target,
                                 f"la valeur {row[col]} n'apparait pas dans sa citation")
        return n

    # ---- physique --------------------------------------------------------
    def physique(self):
        rows = self.q(
            "SELECT pa.*, s.action, s.description, s.quote AS step_quote, s.id AS sid, s.route_id, s.step_order,"
            " r.paper_id FROM parameters pa JOIN steps s ON s.id=pa.step_id"
            " JOIN synthesis_routes r ON r.id=s.route_id WHERE r.paper_id IN ({ids})")
        for p in rows:
            # cible stable d'un rechargement a l'autre (les identifiants de ligne changent)
            name, v = p["name"], p["value_num"]
            target = f"voie {self.by_id[p['route_id']]['branch_label']!r} etape {p['step_order']} {p['name']}"
            if v is None:
                continue
            si, _ = to_si(name, v, p["unit"])
            if p["value_si"] is not None and si is not None and abs(si - p["value_si"]) > 1e-6 * max(1, abs(si)):
                self.add("physique", "bloquant", p["paper_id"], target, "valeur SI incoherente avec la valeur d'origine", p["route_id"])
            convertible = "temperature" in name or "duration" in name or name == "pressure" \
                or name in ("heating_rate", "cooling_rate", "ramp_rate")
            if convertible and si is None:
                self.add("physique", "avertissement", p["paper_id"], target,
                         f"unite non reconnue, pas de conversion SI: {p['unit']!r}", p["route_id"])
                continue
            if "temperature" in name and si is not None:
                celsius = si - 273.15
                # un recuit de film (perovskite, polymere) peut etre tres doux ; une calcination non
                low = 40 if "anneal" in p["action"].lower() else 100
                if THERMAL_ACTION.search(p["action"]) and not low <= celsius <= 2500:
                    self.add("physique", "avertissement", p["paper_id"], target,
                             f"temperature inhabituelle pour '{p['action']}': {celsius:.0f} °C", p["route_id"])
                # au-dela de 350 °C ce n'est plus une etape en phase liquide (pyrolyse, four) :
                # la comparaison au point d'ebullition du solvant n'a pas de sens
                if WET_ACTION.search(p["action"]) and not THERMAL_ACTION.search(p["action"]) and celsius <= 350:
                    ctx = f"{p['action']} {p['description'] or ''} {p['step_quote']}"
                    ctx += " ".join(e["type"] + " " + (e["detail"] or "") for e in self.con.execute(
                        "SELECT * FROM equipment WHERE step_id=?", (p["sid"],)))
                    solvents = [g for g in self.all_reagents(self.by_id[p["route_id"]])
                                if (g["role"] or "").lower() in ("solvent", "solvant")]
                    bps = [bp for g in solvents for k, bp in SOLVENT_BP.items() if k in g["name"].lower()]
                    if bps and celsius > max(bps) + 10 and not PRESSURIZED.search(ctx):
                        self.add("physique", "avertissement", p["paper_id"], target,
                                 f"{celsius:.0f} °C au-dessus du point d'ebullition du solvant "
                                 f"({max(bps)} °C) sans autoclave, reflux ni enceinte fermee mentionnes",
                                 p["route_id"])
            if "duration" in name and si is not None and si > 30 * 86400:
                self.add("physique", "avertissement", p["paper_id"], target, f"duree superieure a 30 jours: {v} {p['unit']}", p["route_id"])
            if ("rate" in name or "ramp" in name) and si is not None and si > 100:
                self.add("physique", "avertissement", p["paper_id"], target, f"vitesse de chauffe invraisemblable: {v} {p['unit']}", p["route_id"])
            if "speed" in name and (p["unit"] or "").lower() == "rpm" and v > 150000:
                self.add("physique", "avertissement", p["paper_id"], target, f"vitesse de rotation invraisemblable: {v} rpm", p["route_id"])
            if name == "ph" and not 0 <= v <= 14:
                self.add("physique", "bloquant", p["paper_id"], target, f"pH hors de 0-14: {v}", p["route_id"])

    # ---- chimie ----------------------------------------------------------
    def chimie(self):
        for r in self.routes:
            mat = self.con.execute("SELECT * FROM materials WHERE id=?", (r["material_id"],)).fetchone()
            target = f"route {r['branch_label']!r}"
            reagents = self.all_reagents(r)
            if not mat or not mat["formula"]:
                self.add("chimie", "info", r["paper_id"], target, "formule du materiau absente : bilan d'elements impossible", r["id"])
            elif reagents:
                available = set().union(*(reagent_elements(g) for g in reagents)) | {"O", "H"}
                # un element introduit par une variation (dopant, substitution) compte aussi
                for v in self.con.execute("SELECT * FROM route_variations WHERE route_id=?", (r["id"],)):
                    fake = {"name": f"{v['parameter']} {v['value_text'] or ''}", "formula": v["value_text"]}
                    available |= reagent_elements(fake)
                missing = elements_of(mat["formula"]) - available
                if missing:
                    self.add("chimie", "avertissement", r["paper_id"], target,
                             f"elements du produit {mat['formula']} sans source parmi les reactifs: "
                             f"{sorted(missing)}", r["id"])
            if mat and NON_OXIDE.search(f"{mat['name']} {mat['formula'] or ''}"):
                for s in self.inherited(r, "steps"):
                    if not THERMAL_ACTION.search(s["action"]):
                        continue
                    ps = self.con.execute("SELECT * FROM parameters WHERE step_id=?", (s["id"],)).fetchall()
                    air = any(p["name"] == "atmosphere" and re.search(r"\bair\b|oxygen|\bO2\b", p["value_text"] or "", re.I) for p in ps)
                    hot = any("temperature" in p["name"] and (p["value_si"] or 0) > 673 for p in ps)
                    if air and hot:
                        self.add("chimie", "avertissement", r["paper_id"], target,
                                 f"materiau non-oxyde traite sous air au-dela de 400 °C (etape {s['step_order']}) : "
                                 "risque d'oxydation, verifier l'atmosphere dans l'article", r["id"])

    # ---- coherence -------------------------------------------------------
    def coherence(self):
        for p in self.papers:
            types = {a["type"] for a in self.con.execute(
                "SELECT type FROM annotations WHERE paper_id=? AND route_id IS NULL", (p["id"],))}
            for t in ANNOT_REQUIRED:
                if t not in types:
                    self.add("coherence", "bloquant", p["id"], p["pmcid"], f"annotation obligatoire absente: {t}")
            if p["review_level"] == "none":
                self.add("coherence", "bloquant", p["id"], p["pmcid"], "extraction jamais controlee par l'orchestrateur")
            elif p["review_level"] != "full" and needs_full_review(p["pmcid"], p["seq"]):
                self.add("coherence", "bloquant", p["id"], p["pmcid"], "relecture integrale due (calibrage ou echantillon 1/5) non faite")
            for d in self.con.execute("SELECT * FROM doubts WHERE paper_id=? AND status='open'", (p["id"],)):
                self.add("coherence", "bloquant", p["id"], f"doubts#{d['id']}", f"doute non tranche: {d['issue']}")
        signatures = defaultdict(list)
        for r in self.routes:
            target = f"route {r['branch_label']!r}"
            variations = self.con.execute("SELECT * FROM route_variations WHERE route_id=?", (r["id"],)).fetchall()
            if r["parent_route_id"] is None:
                if not self.con.execute("SELECT 1 FROM reagents WHERE route_id=?", (r["id"],)).fetchone():
                    self.add("coherence", "avertissement", r["paper_id"], target, "voie de base sans reactif", r["id"])
            else:
                if not variations:
                    self.add("coherence", "bloquant", r["paper_id"], target, "branche sans variation declaree", r["id"])
                parent = self.by_id.get(r["parent_route_id"])
                names = {pa["name"] for s in self.inherited(parent, "steps") for pa in self.con.execute(
                    "SELECT name FROM parameters WHERE step_id=?", (s["id"],))}
                names |= {g["name"] for g in self.all_reagents(parent)}
                for v in variations:
                    if v["parameter"] not in names:
                        self.add("coherence", "info", r["paper_id"], target,
                                 f"variation '{v['parameter']}' sans equivalent dans le protocole parent "
                                 "(nouveau parametre, ou nom different du parent)", r["id"])
                sig = tuple(sorted((v["parameter"], v["step_order"], v["value_num"], v["value_text"]) for v in variations))
                signatures[(r["parent_route_id"], sig)].append(r["branch_label"])
            has_out = self.con.execute("SELECT 1 FROM outcomes WHERE route_id=?", (r["id"],)).fetchone()
            if not has_out and r["succeeded"] is None:
                self.add("coherence", "info", r["paper_id"], target, "aucun resultat rapporte pour cette voie", r["id"])
            if (r["completeness_score"] or 0) < 0.5:
                self.add("coherence", "info", r["paper_id"], target,
                         f"protocole incomplet (score {r['completeness_score']}), manque: {r['missing_fields']}", r["id"])
        for (parent, sig), labels in signatures.items():
            if len(labels) > 1 and sig:
                r = next(x for x in self.routes if x["branch_label"] == labels[0] and x["parent_route_id"] == parent)
                self.add("coherence", "avertissement", r["paper_id"], f"routes {labels}", "branches identiques (memes variations)")

    # ---- sortie ----------------------------------------------------------
    def save(self):
        con = self.con
        accepted = {(r["check_type"], r["target"], r["description"]) for r in con.execute(
            "SELECT * FROM audit_findings WHERE palier=? AND status='accepte'", (self.palier,))}
        con.execute("DELETE FROM audit_findings WHERE palier=? AND status != 'accepte'", (self.palier,))
        for check, sev, pid, rid, target, desc in self.findings:
            if (check, target, desc) not in accepted:
                con.execute("INSERT INTO audit_findings (palier, check_type, severity, paper_id, route_id,"
                            " target, description, created_at) VALUES (?,?,?,?,?,?,?,?)",
                            (self.palier, check, sev, pid, rid, target, desc, db.now()))
        con.commit()

    def sample(self, n=30):
        rows = self.q(
            "SELECT p.pmcid, r.branch_label, s.step_order, pa.name, pa.value_num, pa.value_text, pa.unit, pa.quote"
            " FROM parameters pa JOIN steps s ON s.id=pa.step_id JOIN synthesis_routes r ON r.id=s.route_id"
            " JOIN papers p ON p.id=r.paper_id WHERE p.id IN ({ids}) ORDER BY pa.id")
        rows += self.q(
            "SELECT p.pmcid, r.branch_label, v.step_order, v.parameter AS name, v.value_num, v.value_text, v.unit, v.quote"
            " FROM route_variations v JOIN synthesis_routes r ON r.id=v.route_id"
            " JOIN papers p ON p.id=r.paper_id WHERE p.id IN ({ids}) ORDER BY v.id")
        return random.Random(self.palier).sample(rows, min(n, len(rows)))


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    palier = int(sys.argv[1])
    con = db.connect()
    a = Audit(con, palier)
    if not a.papers:
        raise SystemExit(f"aucune publication extraite dans le palier {palier}")
    n_quotes = a.citations()
    a.physique()
    a.chimie()
    a.coherence()
    a.save()

    open_f = con.execute("SELECT * FROM audit_findings WHERE palier=? AND status='ouvert' ORDER BY"
                         " CASE severity WHEN 'bloquant' THEN 0 WHEN 'avertissement' THEN 1 ELSE 2 END,"
                         " check_type, paper_id", (palier,)).fetchall()
    counts = Counter((f["check_type"], f["severity"]) for f in open_f)
    n_branch = sum(1 for r in a.routes if r["parent_route_id"])
    fam = Counter(r[0] for r in a.q(
        "SELECT m.family FROM synthesis_routes r LEFT JOIN materials m ON m.id=r.material_id WHERE r.paper_id IN ({ids})"))
    meth = Counter(r["method"] for r in a.routes)
    bad_quotes = sum(1 for f in open_f if f["check_type"] == "citation" and f["severity"] == "bloquant")
    L = [f"# Audit du palier {palier}", "",
         f"Genere le {db.now()} — publications n°{a.papers[0]['seq']} a n°{a.papers[-1]['seq']} "
         f"({len(a.papers)} sur {db.PALIER_SIZE}).", "",
         "## Volume", "",
         f"- Voies : {len(a.routes)} ({len(a.routes) - n_branch} de base, {n_branch} branches)",
         f"- Citations verifiees : {n_quotes} — exactes : {n_quotes - bad_quotes} "
         f"({100 * (n_quotes - bad_quotes) / max(1, n_quotes):.1f} %)",
         f"- Completude moyenne : {sum(r['completeness_score'] or 0 for r in a.routes) / max(1, len(a.routes)):.2f}",
         f"- Familles : {dict(fam.most_common())}",
         f"- Methodes : {dict(meth.most_common(12))}", "",
         "## Anomalies ouvertes", "",
         "| Controle | Bloquant | Avertissement | Info |", "|---|---|---|---|"]
    for check in ("citation", "physique", "chimie", "coherence"):
        L.append(f"| {check} | {counts[(check, 'bloquant')]} | {counts[(check, 'avertissement')]} | {counts[(check, 'info')]} |")
    L += ["", "| id | Gravite | Controle | Article | Cible | Description |", "|---|---|---|---|---|---|"]
    for f in open_f:
        if f["severity"] != "info":
            L.append(f"| {f['id']} | {f['severity']} | {f['check_type']} | {a.pm.get(f['paper_id'], '')} | "
                     f"{f['target']} | {f['description'].replace('|', '/')} |")
    L += ["", f"Anomalies de niveau info : {sum(1 for f in open_f if f['severity'] == 'info')} "
              "(table audit_findings).", "",
          "## Echantillon a relire a la main", "",
          "Pour chaque ligne : la citation soutient-elle bien cette valeur, pour cette etape et cette "
          "branche ? Consigner le resultat dans "
          f"`audits/palier_{palier:03d}_relecture.md`, avec le controle de stoechiometrie de 5 voies.", "",
          "| Article | Voie | Etape | Parametre | Valeur | Citation |", "|---|---|---|---|---|---|"]
    for s in a.sample():
        val = s["value_num"] if s["value_num"] is not None else s["value_text"]
        L.append(f"| {s['pmcid']} | {s['branch_label']} | {s['step_order'] or ''} | {s['name']} | "
                 f"{val} {s['unit'] or ''} | {s['quote'].replace('|', '/')} |")
    out = db.AUDIT_DIR / f"palier_{palier:03d}.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    (db.ROOT / "synthese_dump.sql").write_text("\n".join(con.iterdump()) + "\n", encoding="utf-8")
    blocking = sum(1 for f in open_f if f["severity"] == "bloquant")
    print(f"palier {palier}: {len(a.papers)} publications, {len(a.routes)} voies, {n_quotes} citations, "
          f"{blocking} bloquants, {sum(1 for f in open_f if f['severity'] == 'avertissement')} avertissements")
    print(f"rapport: {out}")
    raise SystemExit(1 if blocking else 0)


if __name__ == "__main__":
    main()
