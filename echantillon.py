"""Fiche de verification humaine : tire des valeurs au hasard et les presente avec leur
citation, le passage de l'article autour, et les liens vers l'article et le PDF local.

    python -I echantillon.py            # 40 valeurs au hasard -> audits/verification/echantillon.html
    python -I echantillon.py 100 7      # 100 valeurs, graine 7 (meme graine = meme tirage)
"""
import html
import random
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db  # noqa: E402

QUERIES = {
    "parametre": "SELECT p.pmcid, p.title, p.year, p.journal, p.url, r.branch_label, s.step_order, s.action,"
                 " x.name, x.value_num, x.value_text, x.unit, x.quote, x.char_start, x.char_end"
                 " FROM parameters x JOIN steps s ON s.id=x.step_id JOIN synthesis_routes r ON r.id=s.route_id"
                 " JOIN papers p ON p.id=r.paper_id",
    "reactif": "SELECT p.pmcid, p.title, p.year, p.journal, p.url, r.branch_label, NULL, x.role,"
               " x.name, x.amount, x.amount_text, x.unit, x.quote, x.char_start, x.char_end"
               " FROM reagents x JOIN synthesis_routes r ON r.id=x.route_id JOIN papers p ON p.id=r.paper_id"
               " WHERE x.amount IS NOT NULL OR x.amount_text IS NOT NULL",
    "variation": "SELECT p.pmcid, p.title, p.year, p.journal, p.url, r.branch_label, x.step_order,"
                 " 'par rapport au parent : ' || COALESCE(x.parent_value, '?'),"
                 " x.parameter, x.value_num, x.value_text, x.unit, x.quote, x.char_start, x.char_end"
                 " FROM route_variations x JOIN synthesis_routes r ON r.id=x.route_id JOIN papers p ON p.id=r.paper_id",
    "resultat": "SELECT p.pmcid, p.title, p.year, p.journal, p.url, r.branch_label, NULL, 'resultat mesure',"
                " x.property, x.value_num, x.value_text, x.unit, x.quote, x.char_start, x.char_end"
                " FROM outcomes x JOIN synthesis_routes r ON r.id=x.route_id JOIN papers p ON p.id=r.paper_id",
}
CSS = """body{font:15px/1.5 system-ui,sans-serif;max-width:960px;margin:2em auto;padding:0 1em;color:#222}
.c{border:1px solid #ccc;border-radius:8px;padding:1em;margin:1em 0}
.v{font-size:1.25em;font-weight:600}.m{color:#555;font-size:.9em}
.ctx{background:#f6f6f6;padding:.7em;border-radius:6px;margin:.6em 0}mark{background:#ffe27a}
label{margin-right:1.2em}#bilan{position:sticky;top:0;background:#fff;padding:.6em 0;border-bottom:1px solid #ccc}"""
JS = """const K='verif-'+document.title;let S=JSON.parse(localStorage.getItem(K)||'{}');
function maj(){let n={ok:0,faux:0,doute:0};for(const v of Object.values(S))n[v]++;
document.getElementById('bilan').textContent=`Vérifiées : ${n.ok+n.faux+n.doute} / ${document.querySelectorAll('.c').length}`+
` — correctes ${n.ok}, fausses ${n.faux}, douteuses ${n.doute}`;}
document.querySelectorAll('input[type=radio]').forEach(i=>{if(S[i.name]===i.value)i.checked=true;
i.onchange=()=>{S[i.name]=i.value;localStorage.setItem(K,JSON.stringify(S));maj();};});maj();"""


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else random.randrange(10 ** 6)
    con = db.connect()
    rows = [(kind,) + tuple(r) for kind, q in QUERIES.items() for r in con.execute(q)]
    picks = random.Random(seed).sample(rows, min(n, len(rows)))
    out = [f"<!doctype html><meta charset=utf-8><title>Vérification graine {seed}</title><style>{CSS}</style>",
           f"<h1>Vérification de {len(picks)} valeurs tirées au hasard</h1>",
           f"<p class=m>Tirage parmi {len(rows)} valeurs de la base, graine {seed}. Pour chaque fiche : la valeur "
           "est-elle bien celle de l'article, pour ce matériau et cette étape ? Le passage surligné est la citation "
           "enregistrée ; les liens ouvrent l'article en ligne et le PDF local.</p><div id=bilan></div>"]
    for i, (kind, pmcid, title, year, journal, url, label, step, ctx, name, num, text, unit, quote, a, b) in enumerate(picks):
        flat = db.load_text(pmcid)[0]
        around = (html.escape(flat[max(0, a - 350):a]) + "<mark>" + html.escape(flat[a:b]) + "</mark>"
                  + html.escape(flat[b:b + 350])) if a is not None else html.escape(quote)
        value = f"{num:g}" if num is not None else (text or "")
        frag = urllib.parse.quote(" ".join(quote.split()[:8]))
        pdf = f"../corpus/pdf/{pmcid}.pdf"
        out.append(
            f"<div class=c><div class=m>{i + 1}. {kind} — {html.escape(title or '')} ({html.escape(journal or '')}, {year})</div>"
            f"<div class=m>Voie « {html.escape(label)} »" + (f", étape {step}" if step else "")
            + (f" — {html.escape(str(ctx))}" if ctx else "") + "</div>"
            f"<div class=v>{html.escape(name)} = {html.escape(value)} {html.escape(unit or '')}</div>"
            f"<div class=ctx>…{around}…</div>"
            f"<a href='{url}#:~:text={frag}' target=_blank>Article en ligne ({pmcid})</a> · "
            f"<a href='{pdf}' target=_blank>PDF local</a><br>"
            + "".join(f"<label><input type=radio name=v{i} value={v}> {t}</label>"
                      for v, t in (("ok", "correcte"), ("faux", "fausse"), ("doute", "douteuse"))) + "</div>")
    out.append(f"<script>{JS}</script>")
    target = db.ROOT / "audits" / "verification"
    target.mkdir(exist_ok=True)
    path = target / "echantillon.html"
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"{len(picks)} valeurs -> {path} (graine {seed})")


if __name__ == "__main__":
    main()
