#!/usr/bin/env python3
"""Visuels de la page d'accueil GitHub : schéma du pipeline, chiffres clés, modèle de données, exemple dessiné
d'une voie et de ses branches. Chaque visuel existe en français et en anglais, en thème clair et sombre
(README : <picture> avec prefers-color-scheme). Appelé par analyses/build_site.py ; utilisable seul.

Les chiffres viennent de docs/audit_contenu/data/summary.json, des constantes de palier de build_site.py
(rapports audits/palier_NNN_relecture.md) et, pour l'exemple, de extractions/PMC6199062.json (lecture seule).
Sans dépendance. Sorties : docs/img/accueil/<visuel>_<fr|en>_<light|dark>.svg"""
import os, json, html

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT = "docs/img/accueil/"
EXAMPLE = "PMC6199062"

THEMES = {
    "light": dict(bg="#ffffff", card="#f6f8fa", line="#d1d9e0", tx="#1f2328", mut="#59636e",
                  agent="#17707f", opus="#b26a00", script="#6e7781", data="#3f7d4e", warn="#a8412f",
                  agent_bg="#e3f1f3", opus_bg="#fbefdc", script_bg="#eef1f4", data_bg="#e6f2e9", warn_bg="#f8e7e3"),
    "dark": dict(bg="#0d1117", card="#161b22", line="#30363d", tx="#e6edf3", mut="#9198a1",
                 agent="#45b3c4", opus="#e0a43c", script="#9aa5b1", data="#6cc184", warn="#e98a74",
                 agent_bg="#11303a", opus_bg="#3a2a10", script_bg="#21262d", data_bg="#16321f", warn_bg="#3d1f19"),
}
FONT = "font-family:'Source Sans 3',system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"


def esc(s): return html.escape(str(s), quote=False)


def nb(x, lg, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", " ").replace(".", ",") if lg == 0 else s


def svg(w, h, label, body, th):
    c = THEMES[th]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}">'
            f'<style>text{{{FONT};fill:{c["tx"]}}}.m{{fill:{c["mut"]}}}</style>'
            f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0L10,5L0,10z" fill="{c["mut"]}"/></marker></defs>'
            f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="{c["card"]}" stroke="{c["line"]}"/>{body}</svg>')


def box(x, y, w, h, kind, c, rx=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{c[kind + "_bg"]}" stroke="{c[kind]}" stroke-width="1.5"/>'


def txt(x, y, s, size=13, weight=400, cls="", anchor="start", fill=None):
    f = f' fill="{fill}"' if fill else ""
    k = f' class="{cls}"' if cls else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"{k}{f}>{esc(s)}</text>'


def arrow(x1, y1, x2, y2, c, dash=False):
    d = ' stroke-dasharray="4 3"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c["mut"]}" stroke-width="1.6"{d} marker-end="url(#a)"/>'


# ------------------------------------------------------------------ 1. pipeline
def pipeline(lg, th, S):
    c = THEMES[th]; T = lambda fr, en: (fr, en)[lg]
    W, H = 880, 372
    o = [txt(24, 34, T("Chaque publication passe par six étapes ; aucun agent ne contrôle son propre travail",
                       "Every paper goes through six stages; no agent checks its own work"), 16, 600)]
    # (colonne, ligne, type, titre, sous-titre)
    nodes = [
        (0, 1, "data", T("Article", "Paper"), T("accès libre, CC", "open access, CC"), T("+ annexes, figures", "+ SI, figures")),
        (1, 1, "agent", T("1 Extraction", "1 Extraction"), T("agent Sonnet", "Sonnet agent"), T("+ ce qui manque", "+ what is missing")),
        (2, 1, "script", T("2 Contrôle", "2 Check"), T("load.py", "load.py"), T("citation exacte", "verbatim quote")),
        (3, 0, "agent", T("3 Fidélité", "3 Fidelity"), T("2ᵉ lecteur", "2nd reader"), T("article d'abord", "paper read first")),
        (3, 2, "opus", T("4 Science", "4 Science"), T("Opus + web", "Opus + web"), T("stœchiométrie…", "stoichiometry…")),
        (4, 1, "agent", T("5 Correction", "5 Correction"), T("agent séparé", "separate agent"), T("corrigé / rejeté", "fixed / rejected")),
        (5, 1, "script", T("6 Audit", "6 Batch audit"), T("tous les 50", "every 50 papers"), T("relecture à la main", "hand re-reading")),
        (6, 1, "data", T("Base", "Database"), "SQLite", T("valeur + citation", "value + quote")),
    ]
    bw, bh, gap, x0, y0, dy = 108, 66, 14, 24, 58, 82
    pos = {}
    for col, row, kind, t1, t2, t3 in nodes:
        x = x0 + col * (bw + gap); y = y0 + row * dy; pos[(col, row)] = (x, y)
        o.append(box(x, y, bw, bh, kind, c))
        o.append(txt(x + bw / 2, y + 22, t1, 14, 700, anchor="middle", fill=c[kind]))
        o.append(txt(x + bw / 2, y + 40, t2, 12, anchor="middle"))
        o.append(txt(x + bw / 2, y + 56, t3, 11, cls="m", anchor="middle"))
    mid = lambda col, row: pos[(col, row)][1] + bh / 2
    for a, b in ((0, 1), (1, 2), (4, 5), (5, 6)):
        o.append(arrow(x0 + a * (bw + gap) + bw, mid(a, 1), x0 + b * (bw + gap) - 2, mid(b, 1), c))
    # fourche vers les deux critiques, puis jonction
    xs, xc, xe = x0 + 2 * (bw + gap) + bw, x0 + 3 * (bw + gap), x0 + 4 * (bw + gap)
    for row in (0, 2):
        o.append(f'<path d="M{xs},{mid(2,1)} C{xs+12},{mid(2,1)} {xc-12},{mid(3,row)} {xc-2},{mid(3,row)}" fill="none" stroke="{c["mut"]}" stroke-width="1.6" marker-end="url(#a)"/>')
        o.append(f'<path d="M{xc+bw},{mid(3,row)} C{xc+bw+12},{mid(3,row)} {xe-12},{mid(4,1)} {xe-2},{mid(4,1)}" fill="none" stroke="{c["mut"]}" stroke-width="1.6" marker-end="url(#a)"/>')
    o.append(txt(xc + bw / 2, y0 + dy + bh / 2 + 4, T("en parallèle", "in parallel"), 11, cls="m", anchor="middle"))
    # boucle d'amélioration du protocole
    xa = pos[(5, 1)][0] + bw / 2; xr = pos[(1, 1)][0] + bw / 2; yb = y0 + 2 * dy + bh + 22
    o.append(f'<path d="M{xa},{y0+dy+bh} L{xa},{yb} L{xr},{yb} L{xr},{y0+dy+bh+4}" fill="none" stroke="{c["warn"]}" stroke-width="1.4" stroke-dasharray="5 4" marker-end="url(#a)"/>')
    o.append(f'<rect x="{(xa+xr)/2-150}" y="{yb-10}" width="300" height="20" fill="{c["card"]}"/>')
    o.append(txt((xa + xr) / 2, yb + 4, T("une erreur vue deux fois devient une règle écrite", "a mistake seen twice becomes a written rule"), 12, 600, anchor="middle", fill=c["warn"]))
    # légende
    ly = H - 18; lx = 24
    for kind, l in (("agent", T("agent de langage (Sonnet)", "language agent (Sonnet)")), ("opus", T("agent Opus", "Opus agent")),
                    ("script", T("script de contrôle", "checking script")), ("data", T("données", "data"))):
        o.append(f'<rect x="{lx}" y="{ly-10}" width="12" height="12" rx="3" fill="{c[kind+"_bg"]}" stroke="{c[kind]}" stroke-width="1.5"/>')
        o.append(txt(lx + 18, ly, l, 12, cls="m")); lx += 30 + 7 * len(l)
    return svg(W, H, T("Pipeline multi-agent : article, extraction, contrôle, deux critiques, correction, audit, base",
                       "Multi-agent pipeline: paper, extraction, quote check, two critiques, correction, audit, database"), "".join(o), th)


# ------------------------------------------------------------------ 2. chiffres clés
def kpis(lg, th, S, K):
    c = THEMES[th]; T = lambda fr, en: (fr, en)[lg]
    A = json.load(open(os.path.join(ROOT, "docs/audit_contenu/data/chiffres_accueil.json"), encoding="utf-8"))
    pc = lambda v: T(f"{v:.0f} %", f"{v:.0f}%")
    bas, haut = round(A["usd_bas"]), round(A["usd_haut"])
    # (valeur, titre, sous-titre, couleur, colonnes occupées)
    tiles = [
        (nb(A["publications"], lg), T("publications étudiées", "papers studied"), T("10 paliers audités de 50", "10 audited batches of 50"), "data", 1),
        (nb(A["voies"], lg), T("voies de synthèse extraites", "synthesis routes extracted"), T(f"{nb(S['voies_base'], lg)} de base + {nb(S['branches'], lg)} branches", f"{nb(S['voies_base'], lg)} base + {nb(S['branches'], lg)} branches"), "data", 1),
        (nb(A["materiaux_distincts"], lg), T("matériaux différents", "distinct materials"), T(f"couples composition-phase, sur {nb(A['compositions_distinctes'], lg)} compositions", f"composition-phase pairs, {nb(A['compositions_distinctes'], lg)} compositions"), "data", 1),
        (nb(A["methodes"], lg), T("méthodes de synthèse", "synthesis methods"), T("classes distinctes (+ non classées)", "distinct classes (+ unclassified)"), "data", 1),
        (pc(A["pct_parametres_communs_methode"]), T("paramètres communs", "shared parameters"), T("2 voies, même méthode", "2 routes, same method"), "agent", 1),
        (pc(A["pct_proprietes_communes_famille"]), T("propriétés communes", "shared properties"), T("2 voies, même famille", "2 routes, same family"), "agent", 1),
        (T(f"{bas} – {haut} $", f"${bas}–{haut}"), T(f"prix API de l'extraction ({nb(A['jetons'] / 1e6, lg)} M jetons)", f"API price of the extraction ({nb(A['jetons'] / 1e6, lg)} M tokens)"),
         T(f"{nb(A['agents'], lg)} agents Sonnet / Opus 5.5 ; bas : tout en cache, haut : tout en entrée", f"{nb(A['agents'], lg)} Sonnet / Opus 5.5 agents; low: all cached, high: all fresh input"), "opus", 2),
    ]
    W, cols, tw, th_, gx, gy, x0, y0 = 880, 4, 200, 92, 12, 12, 24, 20
    H = y0 * 2 + 2 * th_ + gy
    o = []; slot = 0
    for v, l1, l2, kind, span in tiles:
        x = x0 + (slot % cols) * (tw + gx); y = y0 + (slot // cols) * (th_ + gy); w = tw * span + gx * (span - 1); slot += span
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{th_}" rx="8" fill="{c["bg"]}" stroke="{c["line"]}"/>')
        o.append(f'<rect x="{x}" y="{y+12}" width="4" height="{th_-24}" rx="2" fill="{c[kind]}"/>')
        o.append(txt(x + 18, y + 38, v, 28, 700, fill=c[kind]))
        o.append(txt(x + 18, y + 60, l1, 14, 600))
        o.append(txt(x + 18, y + 78, l2, 11.5, cls="m"))
    return svg(W, H, T("Chiffres clés de la base", "Key figures of the database"), "".join(o), th)


# ------------------------------------------------------------------ 3. modèle de données
def modele(lg, th):
    c = THEMES[th]; T = lambda fr, en: (fr, en)[lg]
    W, H = 880, 350
    o = [txt(24, 34, T("Modèle de données : voie de base, branches qui changent une variation, une citation par valeur",
                       "Data model: a base route, branches that change one variation, every value with its quote"), 16, 600)]

    def ent(x, y, w, h, kind, title, lines, quote=True):
        r = [box(x, y, w, h, kind, c), txt(x + 12, y + 22, title, 14, 700, fill=c[kind])]
        for i, l in enumerate(lines): r.append(txt(x + 12, y + 42 + i * 17, l, 12, cls="m"))
        if quote:
            r.append(f'<rect x="{x+w-30}" y="{y+8}" width="22" height="18" rx="4" fill="{c["bg"]}" stroke="{c["script"]}"/>')
            r.append(txt(x + w - 19, y + 23, "❝", 14, 700, anchor="middle", fill=c["script"]))
        return "".join(r)

    o.append(ent(24, 60, 150, 76, "data", "Publication", ["PMCID, DOI", T("licence CC, URL", "CC licence, URL")], quote=False))
    o.append(ent(214, 60, 190, 94, "agent", T("Voie de base", "Base route"), [T("matériau, formule, famille", "material, formula, family"), T("méthode, rendement", "method, yield"), T("type : matériau, dispositif…", "kind: material, device…")]))
    o.append(ent(214, 222, 190, 94, "opus", T("Branche", "Branch"), [T("variante testée par l'auteur", "variant tested by the author"), T("variation : 150 → 180 °C", "variation: 150 → 180 °C"), T("échecs gardés (succeeded)", "failures kept (succeeded)")]))
    o.append(arrow(174, 98, 212, 98, c))
    o.append(f'<path d="M309,222 L309,156" fill="none" stroke="{c["opus"]}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#a)"/>')
    o.append(txt(318, 194, T("hérite de", "inherits"), 12, 600, fill=c["opus"]))
    o.append(txt(318, 209, T("tout le reste", "everything else"), 11, cls="m"))
    # entités rattachées à la voie (bus vertical), paramètres rattachés aux étapes
    for (t, ls, kind, q), (x, y) in zip([
            (T("Étapes", "Steps"), [T("ordre, action, équipement", "order, action, equipment")], "agent", True),
            (T("Réactifs", "Reagents"), [T("rôle, quantité, pureté", "role, amount, purity")], "agent", True),
            (T("Résultats", "Outcomes"), [T("propriété, valeur, conditions", "property, value, conditions"), T("lu dans le texte ou sur figure", "from text or read off a figure")], "agent", True),
            (T("Paramètres", "Parameters"), [T("valeur, unité, valeur SI", "value, unit, SI value"), "T, t, pH, rampe…" if lg == 0 else "T, t, pH, ramp…"], "agent", True),
            (T("Non dit", "Not stated"), [T("par étape et par réactif :", "per step and reagent:"), T("vitesse de chauffe, pression…", "heating rate, pressure…")], "warn", False),
            (T("Annotations", "Annotations"), [T("limites de reproductibilité,", "reproducibility limits,"), T("séparées des données", "kept apart from data")], "script", False)],
            [(452, 60), (452, 152), (452, 244), (662, 60), (662, 152), (662, 244)]):
        o.append(ent(x, y, 190, 76, kind, t, ls, quote=q))
    o.append(f'<path d="M404,98 L428,98 M428,98 L428,282" fill="none" stroke="{c["mut"]}" stroke-width="1.6"/>')
    for y in (98, 190, 282): o.append(arrow(428, y, 450, y, c))
    o.append(arrow(642, 98, 660, 98, c))
    o.append(f'<path d="M547,136 L547,144 L652,144 L652,190 L660,190" fill="none" stroke="{c["warn"]}" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#a)"/>')
    o.append(f'<path d="M404,140 L416,140 L416,330 L757,330 L757,322" fill="none" stroke="{c["script"]}" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#a)"/>')
    o.append(f'<rect x="24" y="168" width="164" height="160" rx="8" fill="{c["bg"]}" stroke="{c["script"]}" stroke-dasharray="4 3"/>')
    o.append(txt(36, 192, T("❝ = citation exacte", "❝ = verbatim quote"), 13, 700, fill=c["script"]))
    for i, l in enumerate(T(["retrouvée telle quelle", "dans le texte ;", "le nombre doit figurer", "dans la citation ;", "conversion SI à part,", "jamais à la place", "de l'auteur."],
                            ["found word for word", "in the source text;", "the number must appear", "inside the quote;", "SI conversion stored", "apart, never in place", "of the author's value."])):
        o.append(txt(36, 214 + i * 16, l, 12, cls="m"))
    return svg(W, H, T("Modèle de données de la base", "Database data model"), "".join(o), th)


# ------------------------------------------------------------------ 4. exemple dessiné
def _example():
    d = json.load(open(os.path.join(ROOT, "extractions", EXAMPLE + ".json"), encoding="utf-8"))
    routes = {r["label"]: r for r in d["routes"]}
    base = next(r for r in d["routes"] if r.get("is_baseline") and not r.get("parent"))
    kids = [r for r in d["routes"] if r.get("parent") == base["label"]]
    out = lambda r, p: next((o for o in r.get("outcomes", []) if o["property"] == p), None)
    ns = sum(len(s.get("not_stated", [])) for s in base["steps"]) + sum(len(x.get("not_stated", [])) for x in base.get("reagents", []))
    return d, base, kids, out, ns


def _pv(p):
    v = p.get("value_num"); return (f"{v:g} {p.get('unit') or ''}".strip() if v is not None else (p.get("value_text") or ""))


def exemple(lg, th):
    c = THEMES[th]; T = lambda fr, en: (fr, en)[lg]
    d, base, kids, out, ns = _example()
    W, H = 880, 420
    o = [txt(24, 34, T(f"Exemple : {EXAMPLE}, Sb₂S₃ hydrothermal, série en température (une voie de base, deux branches)",
                       f"Example: {EXAMPLE}, hydrothermal Sb₂S₃, temperature series (one base route, two branches)"), 16, 600)]
    # protocole de la voie de base, lu dans le JSON
    o.append(box(24, 54, 330, 280, "agent", c))
    o.append(txt(38, 78, T(f"Voie de base · {base['label']}", f"Base route · {base['label']}"), 14, 700, fill=c["agent"]))
    act = {"dissolve": ("dissoudre", "dissolve"), "add": ("ajouter", "add"), "heat": ("autoclave", "autoclave"), "wash": ("laver", "wash"), "dry": ("sécher", "dry")}
    rg = base.get("reagents", [])
    y = 102
    for s in base["steps"]:
        vals = ", ".join(_pv(p) for p in s["parameters"] if p.get("value_num") is not None or len(p.get("value_text") or "") <= 16)
        extra = ""
        if s["order"] == 1 and rg: extra = f"{rg[0]['amount']:g} {rg[0]['unit']} L-cysteine"
        if s["order"] == 2 and len(rg) > 2: extra = f"{rg[2]['amount']:g} {rg[2]['unit']} SbCl₃"
        o.append(f'<circle cx="46" cy="{y-4}" r="9" fill="{c["agent"]}"/>' + txt(46, y + 0.5, s["order"], 11, 700, anchor="middle", fill=c["card"]))
        o.append(txt(62, y, act.get(s["action"], (s["action"],) * 2)[lg], 13, 700))
        o.append(txt(140, y, " · ".join(x for x in (extra, vals) if x), 12, cls="m"))
        y += 28
    q = base["steps"][2]["quote"]
    o.append(f'<rect x="36" y="{y-6}" width="306" height="44" rx="6" fill="{c["bg"]}" stroke="{c["script"]}" stroke-dasharray="4 3"/>')
    o.append(txt(46, y + 12, "❝ …" + q[q.find("maintained"):] + "”", 11.5, fill=c["script"]))
    o.append(txt(46, y + 29, T("citation exacte de l'article, contrôlée par load.py", "verbatim quote from the paper, checked by load.py"), 11, cls="m"))
    o.append(txt(38, 322, T(f"{ns} cases « non dites » (vitesse de chauffe, pH…)", f"{ns} \"not stated\" cells (heating rate, pH…)"), 12, 600, fill=c["warn"]))
    # trois échantillons : 120, 150, 180 °C
    samples = sorted([base] + kids, key=lambda r: (r.get("variations") or [{"value_num": 150}])[0]["value_num"])
    cap = "LIB_discharge_capacity_200mAg-1_after_50_cycles"; cap2 = "LIB_discharge_capacity_500mAg-1_after_100_cycles"
    vmax = max(out(r, cap)["value_num"] for r in samples)
    x0, cw = 376, 158
    for i, r in enumerate(samples):
        x = x0 + i * (cw + 8); isb = r is base
        t = (r.get("variations") or [{"value_num": 150, "unit": "°C"}])[0]
        kind = "agent" if isb else ("warn" if r.get("succeeded") is False else "opus")
        o.append(box(x, 54, cw, 280, kind, c))
        o.append(txt(x + 12, 78, f"{t['value_num']:g} °C", 20, 700, fill=c[kind]))
        o.append(txt(x + 12, 96, T("voie de base", "base route") if isb else T("branche : T changée", "branch: T changed"), 12, cls="m"))
        ph = out(r, "phase")["value_text"]; mo = (out(r, "morphology") or {}).get("value_text") or r["material"].get("morphology") or ""
        imp = "Sb8O11Cl2" in ph
        o.append(txt(x + 12, 122, T("phase", "phase"), 11, cls="m"))
        o.append(txt(x + 12, 138, "Sb₂S₃ + Sb₈O₁₁Cl₂" if imp else T("Sb₂S₃ pur", "pure Sb₂S₃"), 13, 600, fill=c["warn"] if imp else None))
        o.append(txt(x + 12, 160, T("morphologie", "morphology"), 11, cls="m"))
        words = mo.split(); lines = [""]
        for w_ in words:
            if len(lines[-1]) + len(w_) > 22: lines.append("")
            lines[-1] = (lines[-1] + " " + w_).strip()
        for j, l in enumerate(lines[:3]): o.append(txt(x + 12, 176 + j * 15, l, 12))
        for k, (prop, lab) in enumerate(((cap, T("Li-ion, 200 mA/g, 50 cycles", "Li-ion, 200 mA/g, 50 cycles")), (cap2, T("Li-ion, 500 mA/g, 100 cycles", "Li-ion, 500 mA/g, 100 cycles")))):
            v = out(r, prop)["value_num"]; yy = 236 + k * 46
            o.append(txt(x + 12, yy, lab, 11, cls="m"))
            o.append(f'<rect x="{x+12}" y="{yy+6}" width="{(cw-70)*v/vmax:.1f}" height="12" rx="3" fill="{c[kind]}"/>')
            o.append(txt(x + 18 + (cw - 70) * v / vmax, yy + 17, f"{v:g}", 12, 700))
        o.append(txt(x + 12, 326, "mAh g⁻¹", 11, cls="m"))
    o.append(txt(24, 362, T("Lecture : à 120 °C, impureté d'oxychlorure (succeeded = false) ; à 150 °C, sphères creuses et meilleure tenue en cyclage.",
                            "Reading: at 120 °C an oxychloride impurity appears (succeeded = false); 150 °C gives hollow spheres and the best cycling."), 12))
    o.append(txt(24, 382, T("Chaque nombre est lu dans extractions/PMC6199062.json, avec sa citation ; l'article donne aussi l'électrode et les piles (voies « dispositif »).",
                            "Every number here is read from extractions/PMC6199062.json, with its quote; the paper also yields electrode and cell (\"device\") routes."), 12, cls="m"))
    o.append(txt(24, 402, T("Requête : SELECT * FROM v_route_complete WHERE pmcid = 'PMC6199062' ORDER BY branch_label, step_order;",
                            "Query: SELECT * FROM v_route_complete WHERE pmcid = 'PMC6199062' ORDER BY branch_label, step_order;"), 11.5, cls="m"))
    return svg(W, H, T("Exemple d'une voie et de ses branches : Sb2S3 à 120, 150 et 180 °C", "Example of a route and its branches: Sb2S3 at 120, 150 and 180 °C"), "".join(o), th)



# ------------------------------------------------------------------ 5. pipeline détaillé (consignes et règles strictes)
def pipeline_detail(lg, th):
    c = THEMES[th]; T = lambda fr, en: (fr, en)[lg]
    rows = [
        ("agent", T("1 Extraction", "1 Extraction"), T("Sonnet, sans web", "Sonnet, no web"),
         [T("inventaire de tous les échantillons avant d'écrire", "inventory of every sample before writing"),
          T("voie de base + une branche par variante comparée", "base route + one branch per compared variant"),
          T("grille v1 : chaque case extraite ou déclarée", "v1 grid: every slot extracted or declared")],
         [T("chaque valeur a sa citation mot pour mot", "every value has its verbatim quote"),
          T("rien de déduit, converti ou hérité sans texte", "nothing inferred, converted or inherited unstated"),
          T("dans le doute : doute écrit, lecture littérale", "when unsure: write a doubt, literal reading")]),
        ("script", T("2 Contrôle", "2 Automatic check"), "load.py",
         [T("citations, structure, grille, plages physiques", "quotes, structure, grid, physical ranges"),
          T("relancé par l'orchestrateur, jamais cru sur parole", "rerun by the orchestrator, never taken on trust")],
         [T("citation absente du texte → refus", "quote not in the text → rejected"),
          T("nombre absent de sa citation → refus", "number missing from its quote → rejected"),
          T("case ni remplie ni déclarée → refus", "slot neither filled nor declared → rejected")]),
        ("opus", T("3 Relecture", "3 Review"), T("orchestrateur Opus", "Opus orchestrator"),
         [T("chaque doute tranché en relisant le passage", "every doubt settled by re-reading the passage"),
          T("1 publication sur 5 relue valeur par valeur", "1 paper in 5 re-read value by value")],
         [T("tirage par hachage du PMCID (non choisi)", "drawn by PMCID hash (not chosen)"),
          T("erreurs > 5 % → lot relu + règle ajoutée", "errors > 5% → batch re-read + new rule")]),
        ("agent", T("4a Fidélité", "4a Fidelity"), T("Sonnet, sans web", "Sonnet, no web"),
         [T("lit l'article AVANT l'extraction", "reads the paper BEFORE the extraction"),
          T("cherche : faux, attribution, manquant, déduit", "looks for: wrong, attribution, missing, inferred")],
         [T("constat sans passage exact de l'article → refusé", "finding without an exact passage → rejected"),
          T("ne modifie rien", "changes nothing")]),
        ("opus", T("4b Science", "4b Science"), T("Opus + web", "Opus + web"),
         [T("stœchiométrie, redox, thermique, solubilité", "stoichiometry, redox, thermal, solubility"),
          T("comparaison aux méthodes fondatrices", "comparison with founding methods")],
         [T("calculs posés pour être recomptés", "calculations laid out to be recounted"),
          T("source avec DOI, sinon déclarée introuvable", "source with DOI, or declared not found")]),
        ("agent", T("5 Correction", "5 Correction"), T("Sonnet", "Sonnet"),
         [T("applique les décisions écrites de l'orchestrateur", "applies the orchestrator's written decisions"),
          T("par script, sur le seul JSON de l'article", "by script, on the paper's JSON only")],
         [T("le texte tranche, jamais la majorité", "the text decides, never the majority"),
          T("aucune valeur perdue (contrôle par diff)", "no value lost (checked by diff)"),
          T("erreur de l'article → annotation, pas correction", "paper's error → annotation, not a fix")]),
        ("script", T("6 Audit", "6 Batch audit"), T("tous les 50 articles", "every 50 papers"),
         [T("recontrôle de toutes les citations à leur position", "every quote re-checked at its position"),
          T("30 valeurs et 5 stœchiométries relues, sources", "30 values and 5 stoichiometries re-read, sources")],
         [T("palier suivant seulement à 0 anomalie bloquante", "next batch only at 0 blocking finding"),
          T("anomalie acceptée = explication écrite", "accepted finding = written explanation")]),
    ]
    W = 880; x1, x2, x3 = 24, 196, 532; top = 84; rh = 66
    H = top + len(rows) * rh + 44
    o = [txt(24, 32, T("Le pipeline en détail : ce qu'on demande à chaque étape, et ce qui bloque", "The pipeline in detail: what each stage is asked to do, and what blocks"), 16, 600),
         txt(x2, 66, T("Consigne", "Instruction"), 13, 700, cls="m"), txt(x3, 66, T("Règle stricte (vérifiée)", "Strict rule (checked)"), 13, 700, cls="m")]
    for i, (kind, t1, t2, cons, rule) in enumerate(rows):
        y = top + i * rh
        o.append(box(x1, y, 160, rh - 10, kind, c))
        o.append(txt(x1 + 12, y + 24, t1, 14, 700, fill=c[kind])); o.append(txt(x1 + 12, y + 42, t2, 12, cls="m"))
        o.append(f'<rect x="{x2}" y="{y}" width="{x3 - x2 - 12}" height="{rh - 10}" rx="6" fill="{c["bg"]}" stroke="{c["line"]}"/>')
        o.append(f'<rect x="{x3}" y="{y}" width="{W - 24 - x3}" height="{rh - 10}" rx="6" fill="{c["warn_bg"]}" stroke="{c["line"]}"/>')
        for j, l in enumerate(cons): o.append(txt(x2 + 10, y + 18 + j * 16, "· " + l, 12))
        for j, l in enumerate(rule): o.append(txt(x3 + 10, y + 18 + j * 16, "✓ " + l, 12, fill=c["tx"]))
        if i < len(rows) - 1: o.append(arrow(x1 + 80, y + rh - 10, x1 + 80, y + rh - 1, c))
    o.append(txt(24, H - 16, T("Chaque agent tient un journal de ses choix ; une erreur vue deux fois devient une règle écrite dans les consignes.",
                               "Each agent keeps a log of its choices; a mistake seen twice becomes a written rule in the instructions."), 12, cls="m"))
    return svg(W, H, T("Pipeline détaillé : consignes et règles de vérification par étape", "Detailed pipeline: instructions and checking rules per stage"), "".join(o), th)

# ------------------------------------------------------------------ écriture
def build(S, K):
    """S : summary.json ; K : dict(quotes, relues, fausses, blind). Renvoie la liste des fichiers écrits."""
    os.makedirs(os.path.join(ROOT, OUT), exist_ok=True); files = []
    for lg, code in enumerate(("fr", "en")):
        for th in THEMES:
            for name, s in (("pipeline", pipeline(lg, th, S)), ("chiffres", kpis(lg, th, S, K)), ("modele", modele(lg, th)), ("exemple", exemple(lg, th)), ("pipeline_detail", pipeline_detail(lg, th))):
                f = f"{OUT}{name}_{code}_{th}.svg"; open(os.path.join(ROOT, f), "w", encoding="utf-8").write(s); files.append(f)
    return files


if __name__ == "__main__":
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_site", os.path.join(HERE, "build_site.py")); bs = importlib.util.module_from_spec(spec); spec.loader.exec_module(bs)
    print(len(build(bs.S, bs.KPI)), "visuels écrits dans", OUT)
