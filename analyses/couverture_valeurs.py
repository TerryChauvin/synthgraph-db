"""Couverture des valeurs chiffrées : mesure indépendante de la sonde, sans agent.

Pour chaque publication close, relève dans corpus/text/<PMCID>.txt
  - les nombres des tableaux (blocs `[TABLE]`, cellules numériques) ;
  - les nombres suivis d'une unité dans le corps (hors Introduction, Conclusions, références) ;
et cherche chacun parmi les nombres de extractions/<PMCID>.json (tous les champs sauf les citations).
Un nombre absent de l'extraction = valeur possiblement manquée (ou hors périmètre : littérature, DFT,
échantillon commercial) ; le taux sert à classer les publications, pas à compter des erreurs.

    python3 -I analyses/couverture_valeurs.py                 # toutes → JSON + rapport
    python3 -I analyses/couverture_valeurs.py PMC1234567      # détail : nombres non couverts avec contexte
    python3 -I analyses/couverture_valeurs.py PMC1234567 --base <commit>   # extraction d'un commit donné

Sorties : docs/audit_contenu/data/couverture_valeurs.json, audits/couverture_valeurs.md
"""
import json
import os
import re
import sqlite3
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]
os.chdir(ROOT)

NUM = r"[-−–]?\d+(?:[.,]\d+)?"
UNITS = (r"°\s?C|K\b|h\b|hrs?\b|hours?\b|min\b|minutes?\b|s\b|nm\b|µm|μm|mm\b|cm\b|m2|m²|cm3|cm−1|cm-1|mL\b|ml\b|µL|μL|L\b|"
         r"mg\b|µg|μg|g\b|kg\b|mmol|µmol|μmol|mol\b|M\b|mM\b|µM|μM|wt\s?%|at\s?%|vol\s?%|%|eV\b|meV|mV\b|V\b|mA\b|A\s?g|F\s?g|"
         r"mAh|Wh|W\b|kW|kV\b|rpm\b|ppm\b|ppb\b|Pa\b|kPa|MPa|GPa|bar\b|mbar|Torr|°|Hz\b|kHz|MHz|GHz|S\s?cm|S/cm|Ω|ohm|emu|Oe\b|mT\b|T\b|"
         r"mg\s?/\s?L|mg\s?L|g\s?/\s?L|sccm|ml\s?/\s?min|mL\s?/\s?min|K\s?/\s?min|°C\s?/\s?min|nm/s|Å")
NUM_UNIT = re.compile(rf"(?<![\w.])({NUM})\s?(?:±\s?{NUM}\s?)?(?:{UNITS})")
CELL_NUM = re.compile(rf"^\s*\(?({NUM})\)?\s*(?:±\s*{NUM})?\s*(?:\(\s*{NUM}\s*\))?\s*%?\s*$")
SKIP_SEC = re.compile(r"^## .*(introduction|conclusion|reference|acknowledg|author contribution|funding|conflict|data availability|abbreviation)", re.I)
EXP_SEC = re.compile(r"^## .*(experiment|method|synthes|preparation|materials and|procedure|fabrication)", re.I)


def norm(x):
    try:
        v = float(str(x).replace(",", ".").replace("−", "-").replace("–", "-"))
    except ValueError:
        return None
    return f"{abs(v):.6g}"


def json_numbers(d):
    """Nombres portés par l'extraction (valeurs, textes de valeur, conditions), citations exclues."""
    out = set()

    def walk(o, key=""):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("quote", "supplier_quote", "issue", "text"):  # citations, doutes et annotations
                    continue
                walk(v, k)
        elif isinstance(o, list):
            for v in o:
                walk(v, key)
        elif isinstance(o, (int, float)) and not isinstance(o, bool):
            out.add(norm(o))
        elif isinstance(o, str):
            for m in re.finditer(NUM, o):
                out.add(norm(m.group(0)))
    walk(d)
    out.discard(None)
    return out


def text_numbers(txt):
    """(tableaux, corps_resultats, corps_experimental) : listes de (nombre normalisé, position)."""
    tables, res, exp = [], [], []
    lines = txt.split("\n")
    pos, in_table, sec, sec_exp, skip = 0, False, "", False, False
    for ln in lines:
        if ln.startswith("## "):
            sec, skip, sec_exp, in_table = ln, bool(SKIP_SEC.match(ln)), bool(EXP_SEC.match(ln)), False
            if ln.startswith("## Figure captions") or ln.startswith("## Table footnotes"):
                skip = False
        elif ln.startswith("[TABLE]"):
            in_table = True
        elif in_table and " | " not in ln:
            in_table = False
        if in_table and " | " in ln:
            cells = ln.split(" | ")
            off = pos
            for i, c in enumerate(cells):
                m = CELL_NUM.match(c)
                if i > 0 and m:  # première colonne = étiquette d'échantillon
                    n = norm(m.group(1))
                    if n is not None:
                        tables.append((n, off))
                off += len(c) + 3
        elif not skip and not in_table and not ln.startswith("[TABLE]"):
            for m in NUM_UNIT.finditer(ln):
                n = norm(m.group(1))
                if n is None:
                    continue
                (exp if sec_exp else res).append((n, pos + m.start()))
        pos += len(ln) + 1
    return tables, res, exp


def cover(pmcid, d=None):
    txt = open(f"corpus/text/{pmcid}.txt", encoding="utf-8", errors="ignore").read()
    if d is None:
        d = json.load(open(f"extractions/{pmcid}.json", encoding="utf-8"))
    J = json_numbers(d)
    T, R, E = text_numbers(txt)
    def part(L):
        miss = [(n, p) for n, p in L if n not in J]
        return dict(total=len(L), manquants=len(miss), pct=round(100.0 * (len(L) - len(miss)) / len(L), 1) if L else None), miss
    t, tm = part(T)
    r, rm = part(R)
    e, em = part(E)
    return dict(tableaux=t, resultats_texte=r, experimental=e), dict(tableaux=tm, resultats_texte=rm, experimental=em), txt


def main():
    if len(sys.argv) > 1:
        x = sys.argv[1]
        d = None
        if "--base" in sys.argv:
            ref = sys.argv[sys.argv.index("--base") + 1]
            d = json.loads(subprocess.run(["git", "show", f"{ref}:extractions/{x}.json"], capture_output=True, text=True, check=True).stdout)
        c, miss, txt = cover(x, d)
        print(json.dumps(c, ensure_ascii=False))
        for k, L in miss.items():
            print(f"\n## {k} : {len(L)} non couverts")
            for n, p in (L if "--all" in sys.argv else L[:60]):
                print(f"- {n} : « {re.sub(chr(10), ' ', txt[max(0, p - 70):p + 40])} »")
        return
    c = sqlite3.connect("synthese.db")
    rows = []
    for (x,) in c.execute("SELECT pmcid FROM papers WHERE status='extracted' ORDER BY seq"):
        if not os.path.exists(f"extractions/{x}.json"):
            continue
        cv, _, _ = cover(x)
        rows.append(dict(pmcid=x, **{f"{k}_{m}": v[m] for k, v in cv.items() for m in ("total", "manquants", "pct")}))
    json.dump(rows, open("docs/audit_contenu/data/couverture_valeurs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    def agg(k):
        tot = sum(r[f"{k}_total"] for r in rows)
        mi = sum(r[f"{k}_manquants"] for r in rows)
        return tot, mi, round(100.0 * (tot - mi) / max(tot, 1), 1)
    L = ["# Couverture des valeurs chiffrées", "", f"{len(rows)} publications. Script : `analyses/couverture_valeurs.py`.", "",
         "| Source | Nombres dans l'article | Absents de l'extraction | Couverture |", "|---|---|---|---|"]
    for k, lab in (("tableaux", "cellules numériques des tableaux"), ("resultats_texte", "nombres avec unité, corps hors expérimental"), ("experimental", "nombres avec unité, sections expérimentales")):
        t, m, p = agg(k)
        L.append(f"| {lab} | {t} | {m} | {p} % |")
    open("audits/couverture_valeurs.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
