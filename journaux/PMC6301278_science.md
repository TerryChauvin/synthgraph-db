# PMC6301278 — critique scientifique (journal de décisions)

- DRX (point demandé par l'orchestrateur) : Bragg recalculé avec Cu Kα1 = 1,54056 Å (longueur d'onde non déclarée ; D8 Advance supposé au cuivre). Les pics 31,99 / 45,5 / 54,85 / 57,52 / 67,24° donnent d = 2,795 / 1,992 / 1,672 / 1,601 / 1,391 Å, soit a = 5,55 Å en indexant (200)/(220)/(311)/(222)/(400) d'AgCl : accord à 0,3 %. Aucun pic à moins de 1,2° d'un pic d'Ag cfc (38,11 / 44,30 / 64,44 / 77,40°). Classé `probleme` : la phase mesurée est AgCl.
- La figure 5 a été ouverte : pas de pic à 38,1° (fond bombé entre 36 et 44°), indices « (142) » (parité mélangée, interdite en cfc) et « (220) » à 67°. Ces constats renforcent le classement.
- EDX (figure 4 ouverte) : pic Cl Kα (2,622 keV) de même hauteur que Ag Lα (2,984 keV), d'après le X-Ray Data Booklet. Explication « chlore des lames de verre » rejetée (verre sodocalcique sans chlore). « Absorption optique plasmon à 3 keV » signalé comme erreur de vocabulaire.
- Bilan chlore : 0,10 mmol d'Ag → 3,5 mg de Cl suffisent, soit 0,1 % de ≈ 3,3 g d'extrait ; Ksp 1,8e-10 → 1,8e-7 M de Cl- suffisent pour précipiter. Pas de valeur mesurée de chlorure pour R. stricta : recherche non faite (budget), dit dans `sources_not_found`.
- Masse d'extrait : 10 g × 6/18 = 3,3 g (borne haute, volume de solution ignoré ; ≈ 2,1 g si la solution fait ≈ 28 mL). Donnée sous forme de fourchette.
- Sources retenues pour AgCl : Sharifi-Rad & Pohl 2020 (Nanomaterials, pics 27,9/32,4/46,2/54,8/57,6/67,5°, JCPDS 31-1238) et Okaiyeto et al. 2019 (Molecules, Ag/AgCl, Cl- venant de l'extrait). Lues sur leurs pages PMC (PMC7221712, PMC6930575) ; DOI non vérifiés sur Crossref (bloqué).
- Une source trouvée (Sharifi-Rad & Pohl) attribue une « LSPR à 460 nm » à AgCl pur, ce qui est discutable : je ne la cite que pour les positions DRX.
- Positions de référence de l'Ag : NBS Monograph 25-13 (38,112/44,295/64,437/77,390°), préféré à un article de synthèse verte.
- Colonne « écart-type » des annexes recalculée : c'est exactement |a − b|/√2 entre les deux colonnes de la rangée (sans/avec xylitol, ou 24 h/48 h), vérifié sur toutes les rangées de s001, s004 et s003. Pas de réplicats → `probleme` pour les conclusions antibactériennes.
- Incohérence entre figures 7, 8 et 9 (16 contre 26 mm pour le même échantillon ; témoin 20–37 mm ; cefixime ou cefipime) classée `probleme` (contrôle n° 6).
- UV–Vis : laissé en `reserve` et non en `probleme`. Une petite fraction d'Ag0 peut exister sous le seuil de détection DRX ; mais absorbance > 2, extrait déjà coloré avant réaction et bande à 380 nm trop basse pour un plasmon d'Ag.
- Xylitol : 9 mg contre 2–3 g d'extrait ; rôle de stabilisant jugé peu plausible (`reserve`), l'article ne donnant qu'une image MEB par condition.
- Scherrer : largeur ≈ 0,4° lue sur la figure pour le pic à 45,7° → ≈ 21 nm, cohérent avec 20 nm, mais c'est une cristallite d'AgCl. Lecture approximative signalée.
- Mécanisme retenu : précipitation immédiate d'AgCl par les chlorures de l'extrait, puis réduction partielle et lente (AgCl/Ag à +0,22 V) → Ag/AgCl dominé par AgCl. Préféré à la réduction directe Ag+ → Ag0 des auteurs.
- Série AgNP_ser_* jugée `invérifiable` / `non_reproductible` : conditions absentes ; la dose d'extrait n'est estimée qu'en supposant la même solution de 10 g/18 mL.
- 5 recherches web (4 recherches et 1 lecture de deux pages PMC) ; rien n'est ajouté à fondateurs.md ni à constantes.md (consigne).
