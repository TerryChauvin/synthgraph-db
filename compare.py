"""Voies deja extraites pour un materiau donne, pour comparer une synthese aux autres.

    python -I compare.py "ZnO"
    python -I compare.py "hydroxyapatite"
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402


def main():
    key = f"%{sys.argv[1]}%"
    con = db.connect()
    # mot entier, casse respectee pour une formule : « Ag » ne doit ramener ni « fragment » ni « AgCl »
    word = re.compile(rf"(?<![A-Za-z0-9]){re.escape(sys.argv[1])}(?![A-Za-z0-9])",
                      0 if re.search(r"[A-Z]", sys.argv[1]) else re.I)
    rows = [r for r in con.execute(
        "SELECT p.pmcid, r.id, r.branch_label, r.method, m.name, m.formula, m.phase, r.succeeded"
        " FROM synthesis_routes r JOIN papers p ON p.id=r.paper_id LEFT JOIN materials m ON m.id=r.material_id"
        " WHERE (m.name LIKE ? OR m.formula LIKE ?) AND r.parent_route_id IS NULL ORDER BY p.pmcid", (key, key))
        if word.search(r["formula"] or "") or word.search(r["name"] or "")]
    print(f"{len(rows)} voies de base pour « {sys.argv[1]} »\n")
    for r in rows:
        params = con.execute(
            "SELECT s.step_order, s.action, pa.name, pa.value_num, pa.value_text, pa.unit FROM parameters pa"
            " JOIN steps s ON s.id=pa.step_id WHERE s.route_id=? AND (pa.name LIKE '%temperature%' OR pa.name LIKE"
            " '%duration%' OR pa.name='ph' OR pa.name='atmosphere') ORDER BY s.step_order", (r["id"],)).fetchall()
        cond = "; ".join(f"{p['action']}:{p['name']}={p['value_num'] if p['value_num'] is not None else p['value_text']}"
                         f"{p['unit'] or ''}" for p in params)
        outs = con.execute("SELECT property, value_num, value_text, unit FROM outcomes WHERE route_id=? LIMIT 4",
                           (r["id"],)).fetchall()
        res = "; ".join(f"{o['property']}={o['value_num'] if o['value_num'] is not None else o['value_text']}{o['unit'] or ''}"
                        for o in outs)
        nb = con.execute("SELECT COUNT(*) FROM synthesis_routes WHERE parent_route_id=?", (r["id"],)).fetchone()[0]
        print(f"{r['pmcid']} « {r['branch_label']} » ({nb} branches) — {r['name']} [{r['formula']}] {r['phase'] or ''}")
        print(f"   méthode : {r['method']}")
        print(f"   conditions : {cond}")
        print(f"   résultats : {res}\n")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:   # sortie tronquee par un `| Select-Object -First n`
        pass
