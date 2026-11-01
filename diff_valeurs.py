"""Valeurs numeriques de l'ancienne version (git HEAD) absentes de la nouvelle extraction.

    python -I diff_valeurs.py PMC1234567

Sert apres une mise a niveau ou une correction qui a reecrit le fichier d'un bloc : toute valeur
(nombre + citation) presente avant doit se retrouver apres, sauf retrait voulu.
"""
import json
import subprocess
import sys
from pathlib import Path

GIT = r"C:\Program Files\Git\cmd\git.exe"
if not Path(GIT).exists():
    import shutil
    GIT = shutil.which("git") or "git"


def values(node, out):
    if isinstance(node, dict):
        for k in ("value", "value_num", "amount"):
            if isinstance(node.get(k), (int, float)) and node.get("quote"):
                out.add((float(node[k]), " ".join(node["quote"].split())))
        for v in node.values():
            values(v, out)
    elif isinstance(node, list):
        for v in node:
            values(v, out)
    return out


def main():
    pmcid = sys.argv[1]
    rel = f"extractions/{pmcid}.json"
    # 2e argument : revision de reference (defaut HEAD). Attention : la sauvegarde automatique commite
    # toutes les 10 min, donc HEAD peut deja contenir la reecriture ; donner alors un commit anterieur.
    rev = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
    if Path(rev).is_file():  # 2e argument : copie du JSON au chargement (plus sûr que git quand des sauvegardes automatiques commitent en cours de correction)
        old = Path(rev).read_bytes()
    else:
        old = subprocess.run([GIT, "show", f"{rev}:{rel}"], capture_output=True, cwd=Path(__file__).parent).stdout
    a = values(json.loads(old.decode("utf-8")), set())
    b = values(json.loads((Path(__file__).parent / rel).read_text(encoding="utf-8")), set())
    lost = sorted(a - b)
    print(f"{pmcid}: {len(a)} valeurs avant, {len(b)} apres, {len(lost)} absentes de la nouvelle version")
    for v, q in lost[:40]:
        print(f"  {v:g} | {q[:110]}")


if __name__ == "__main__":
    main()
