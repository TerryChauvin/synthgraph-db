"""Acces commun a la base et au corpus."""
import html
import re
import sqlite3
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import os
ROOT = Path(__file__).resolve().parent
# architecture v2 : base et dossier d'extractions séparés (SYNTHESE_DB=synthese_v2.db SYNTHESE_EXTRACT_DIR=extractions_v2)
DB_PATH = ROOT / os.environ.get("SYNTHESE_DB", "synthese.db")
XML_DIR = ROOT / "corpus" / "xml"
TEXT_DIR = ROOT / "corpus" / "text"
PDF_DIR = ROOT / "corpus" / "pdf"
EXTRACT_DIR = ROOT / os.environ.get("SYNTHESE_EXTRACT_DIR", "extractions")
AUDIT_DIR = ROOT / "audits"
PALIER_SIZE = 50

_WS = re.compile(r"\s+")
_TAG = re.compile(r"<[^>]+>")

# la console Windows (cp1252) ne sait pas afficher les caracteres des articles
for _s in (sys.stdout, sys.stderr):
    _s.reconfigure(encoding="utf-8", errors="replace")


def strip_tags(s):
    return _TAG.sub("", html.unescape(s)) if s else s


def connect():
    for d in (XML_DIR, TEXT_DIR, PDF_DIR, EXTRACT_DIR, AUDIT_DIR):
        d.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH, timeout=60)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript((ROOT / "schema.sql").read_text(encoding="utf-8"))
    # colonnes ajoutees apres la creation de la base
    if "supplier_quote" not in [r[1] for r in con.execute("PRAGMA table_info(reagents)")]:
        con.execute("ALTER TABLE reagents ADD COLUMN supplier_quote TEXT")
    if "format_version" not in [r[1] for r in con.execute("PRAGMA table_info(papers)")]:
        # 1 = extraction d'origine ; 2 = grille de reproductibilite remplie (cases « non cite »)
        con.execute("ALTER TABLE papers ADD COLUMN format_version INTEGER NOT NULL DEFAULT 1")
    # format 2 : conditions de mesure, nature de la voie, valeurs lues sur figure
    for table, column, decl in (
            ("characterizations", "instrument", "TEXT"), ("characterizations", "conditions", "TEXT"),
            ("synthesis_routes", "kind", "TEXT NOT NULL DEFAULT 'material'"),
            ("parameters", "from_figure", "TEXT"), ("outcomes", "from_figure", "TEXT"),
            ("route_variations", "from_figure", "TEXT"),
            ("papers", "si_status", "TEXT"), ("papers", "si_files", "INTEGER"),
            ("papers", "critic_status", "TEXT NOT NULL DEFAULT 'none'"),
            ("characterizations", "char_key", "TEXT"), ("outcomes", "measured_by", "INTEGER"),
            ("outcomes", "measured_status", "TEXT")):
        if column not in [r[1] for r in con.execute(f"PRAGMA table_info({table})")]:
            con.execute(f"ALTER TABLE {table} ADD COLUMN {column} {decl}")
    if "param_score" not in [r[1] for r in con.execute("PRAGMA table_info(papers)")]:
        con.execute("ALTER TABLE papers ADD COLUMN param_score REAL")
    # vocabulaire canonique (canon.py) : name_canon, property_canon, property_group, table vocabulaire
    import canon
    canon.ensure_columns(con)
    return con


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def norm(s):
    """Normalisation appliquee a l'identique au texte des articles et aux citations."""
    return _WS.sub(" ", unicodedata.normalize("NFC", s)).strip()


def load_text(pmcid):
    """Texte normalise de l'article : une ligne par paragraphe, sans double espace,
    donc remplacer les sauts de ligne par des espaces conserve les positions."""
    raw = (TEXT_DIR / f"{pmcid}.txt").read_text(encoding="utf-8")
    return raw.replace("\n", " "), raw


def section_at(raw, pos):
    """Titre de section ('## ...') precedant la position pos."""
    i = raw.rfind("\n## ", 0, pos + 1)
    if i < 0:
        return None
    return raw[i + 4: raw.find("\n", i + 1)].strip()
