"""Recharge toutes les extractions deja chargees (apres une evolution de load.py ou du schema).

    python -I reload_all.py

Les rangs, paliers, niveaux de relecture et doutes tranches sont conserves.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402
from load import insert, validate  # noqa: E402


def main():
    con = db.connect()
    bad = 0
    for r in con.execute("SELECT pmcid FROM papers WHERE status='extracted' ORDER BY seq").fetchall():
        data = json.loads((db.EXTRACT_DIR / f"{r['pmcid']}.json").read_text(encoding="utf-8"))
        c, order = validate(r["pmcid"], data)
        if c.errors:
            bad += 1
            print(f"{r['pmcid']}: {len(c.errors)} erreurs, non recharge -> {c.errors[:2]}")
            continue
        insert(con, r["pmcid"], data, order, c)
    print(f"recharge termine, {bad} en erreur")
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main()
