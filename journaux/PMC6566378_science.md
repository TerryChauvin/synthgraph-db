# PMC6566378 — critique scientifique (Opus)

- Recette identifiée comme celle de Dong et al. 2018 (Nano Lett., 10.1021/acs.nanolett.8b00861) : 0,25 g Cs2CO3 / 0,8 g OA / 7 g ODE et 75 mg PbBr2 + ZnBr2 + 0,4 mL injectés, retrouvés mot pour mot dans les Méthodes de PMC11921029 (2024) qui cite Dong. Le texte de Dong lui-même n'a pas pu être lu (notice PubMed seulement).
- Mécanisme : préféré l'équilibre thermodynamique de Dong (taille fixée par Br/Pb et T) à l'hypothèse cinétique de `mecanisme_analyse` (nucléation abondante, croissance arrêtée par un temps court) ; d'où `a_revoir`. Appuis : notice Dong, thèse U. South Carolina 2025 (Br/Pb 10–25 → 3–7 nm), recette de Rossi 2020 (arXiv 2002.08589, 4 nm à 80 °C, Br/Pb ≈ 9,8).
- Br/Pb calculé de 2 (0 mg ZnBr2) à ≈ 28 (600 mg) : la masse de ZnBr2 est un paramètre de taille, donc l'absence de valeur par taille rend 4,5 nm (même 120 °C que 4,3 nm) non reproductible → `probleme` sur la branche 4,5 nm.
- Point de l'orchestrateur, plages 190–80 / 140–190 / 80–120 °C contre 88–140 °C : `probleme` rattaché à la branche 5,0 nm (130 °C hors des deux régimes de purification), `reserve` sur la voie de base (120 °C est couvert). Origine probable : protocole général de la méthode source, non confirmé.
- Point de l'orchestrateur, dE/dt à 5,0 nm : recalcul des 8 lignes ; 7 reproduites à l'arrondi, 5,0 nm donne 0,275 contre 0,24 ± 0,01 (3,5 σ) ; la valeur recalculée suit mieux la tendance → `probleme` sur la branche 5,0 nm.
- Nouveau `probleme` : lot triplé (3 × 11 mL + 1,2 mL ≈ 34 mL) dans le ballon de 25 mL des Méthodes, rattaché à la branche 2,6 nm (vaut aussi pour 3,0 et 3,5 nm).
- Nouveau `probleme` : DDT + hexane « vacuum-dried 1 h at 100 °C » : l'hexane (Téb 68,7 °C) part ; dose de DDT de 0,12 ou 0,42 mmol selon l'hypothèse (facteur 3,5). Antoine de l'hexane (NIST) cité de mémoire, signalé dans `sources_not_found`.
- Test DDT jugé peu discriminant (`reserve`) : ΔE de 4,3 nm ≈ 2 100 cm−1, zone où ni l'OA (C=O 1 710 cm−1) ni le DDT n'absorbent fortement ; aucun IR/RMN de l'échange. Référence de principe : Pandey & Guyot-Sionnest 2008 (confirmée par recherche, DOI non vérifié sur Crossref).
- Phase non mesurée (pas de DRX) : `reserve` avec Cottingham 2016 et Palazon 2017 (fondateurs.md) ; Cs4PbBr6 jugé peu probable car milieu riche en Pb.
- Comparaison base : PMC11012633 (150 °C, Br/Pb 6, 5,7 nm, 485 nm) et PMC10148794 (170 °C, ≈ 5,5 nm) cohérents avec 6,2 nm à 140 °C.
- Recherches : 3 WebSearch + 1 recherche Parallel ; lectures : 2 réussies (arXiv 2002.08589 via Parallel, PMC11921029), 2 échouées (WebFetch par.nsf.gov et arxiv.org : DNS ; curl : 403 du proxy).
- DOI non vérifiés sur Crossref (bloqué) : 10.1021/acs.nanolett.8b00861, 10.1126/science.1159832. Rien ajouté à fondateurs.md ni constantes.md.
