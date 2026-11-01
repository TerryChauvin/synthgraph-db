#!/usr/bin/env python3
"""Contrôles de vérification de la base (points 2 à 7 de l'audit de contenu) :
2. branches sans résultat propre ; 3. stœchiométrie nominale des précurseurs contre la formule du produit ;
4. complétude contre verdict de la critique scientifique ; 5. variation d'une branche → effet mesuré ;
6. synonymes de noms de paramètres ; 7. couverture des conversions SI.
Usage : python3 -I analyses/audit_verification.py → docs/audit_contenu/data/verif_*.json. Ne modifie pas la base."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path[:0] = [HERE, ROOT]
os.chdir(ROOT)  # chemins relatifs à la racine du dépôt
import collections, json, math, os, re, sqlite3, statistics, sys
from audit_contenu import canon_prop, norm_unit, METHOD_RE

MASSES = {"H": 1.008, "He": 4.003, "Li": 6.94, "Be": 9.012, "B": 10.81, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.18, "Na": 22.99, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06, "Cl": 35.45, "Ar": 39.95, "K": 39.098, "Ca": 40.078, "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38, "Ga": 69.723, "Ge": 72.63, "As": 74.922, "Se": 78.971, "Br": 79.904, "Kr": 83.798, "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224, "Nb": 92.906, "Mo": 95.95, "Ru": 101.07, "Rh": 102.906, "Pd": 106.42, "Ag": 107.868, "Cd": 112.414, "In": 114.818, "Sn": 118.71, "Sb": 121.76, "Te": 127.6, "I": 126.904, "Cs": 132.905, "Ba": 137.327, "La": 138.905, "Ce": 140.116, "Pr": 140.908, "Nd": 144.242, "Sm": 150.36, "Eu": 151.964, "Gd": 157.25, "Tb": 158.925, "Dy": 162.5, "Ho": 164.93, "Er": 167.259, "Tm": 168.934, "Yb": 173.045, "Lu": 174.967, "Hf": 178.49, "Ta": 180.948, "W": 183.84, "Re": 186.207, "Os": 190.23, "Ir": 192.217, "Pt": 195.084, "Au": 196.967, "Hg": 200.592, "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Th": 232.038, "U": 238.029}
NONMETAL = {"H", "O", "C", "N"}
TOK = re.compile(r"([A-Z][a-z]?)(\d*\.?\d*)|(\()|(\))(\d*\.?\d*)")


def parse_formula(f):
    """Composition élémentaire d'une formule simple (parenthèses, hydrates '·xH2O'). None si non lisible."""
    if not f:
        return None
    f = f.replace("−", "-").replace("–", "-").split("@")[0].strip()
    if re.search(r"[a-z]{3,}|\s|/|\[|=|%", f):
        return None
    parts = re.split(r"[·•.]", f)
    total = collections.Counter()
    for part in parts:
        m = re.match(r"^(\d*\.?\d*)(.*)$", part)
        mult = float(m.group(1)) if m.group(1) else 1.0
        s = m.group(2)
        stack = [collections.Counter()]
        pos = 0
        while pos < len(s):
            t = TOK.match(s, pos)
            if not t:
                return None
            pos = t.end()
            if t.group(1):
                el, n = t.group(1), float(t.group(2)) if t.group(2) else 1.0
                if el not in MASSES:
                    return None
                stack[-1][el] += n
            elif t.group(3):
                stack.append(collections.Counter())
            elif t.group(4):
                if len(stack) < 2:
                    return None
                inner = stack.pop()
                n = float(t.group(5)) if t.group(5) else 1.0
                for k, v in inner.items():
                    stack[-1][k] += v * n
        if len(stack) != 1 or not stack[0]:
            return None
        for k, v in stack[0].items():
            total[k] += v * mult
    return total if total else None


def molar_mass(comp):
    return sum(MASSES[k] * v for k, v in comp.items())


def moles(amount, unit, comp):
    u = (unit or "").strip().lower().replace("μ", "µ")
    if amount is None:
        return None
    if u in ("mol",):
        return amount
    if u in ("mmol",):
        return amount / 1e3
    if u in ("µmol", "umol"):
        return amount / 1e6
    if comp and u in ("g", "mg", "kg"):
        m = molar_mass(comp)
        return amount / m * {"g": 1, "mg": 1e-3, "kg": 1e3}[u]
    return None


def num(s):
    if s is None:
        return None
    m = re.search(r"-?\d+(?:[.,]\d+)?", str(s))
    return float(m.group().replace(",", ".")) if m else None


def spearman(x, y):
    n = len(x)
    if n < 3:
        return None
    rx = {v: i for i, v in enumerate(sorted(x))}
    ry = {v: i for i, v in enumerate(sorted(y))}
    a = [rx[v] for v in x]
    b = [ry[v] for v in y]
    ma, mb = sum(a) / n, sum(b) / n
    num_ = sum((p - ma) * (q - mb) for p, q in zip(a, b))
    den = math.sqrt(sum((p - ma) ** 2 for p in a) * sum((q - mb) ** 2 for q in b))
    return num_ / den if den else None


from canon import PARAM_RULES, canon_param  # noqa: E402  (vocabulaire canonique commun)
