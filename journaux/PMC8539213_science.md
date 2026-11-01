# PMC8539213 — critique scientifique (Opus)

- Verdict « cohérente » pour les quatre voies : le protocole sol-gel citrate tient chimiquement ; les `probleme` portent sur des résultats (EDX, test catalytique), pas sur la voie de synthèse elle-même.
- EDX `probleme` : Ce0.18Zr0.14La0.2Pr0.2Y0.18O2 → somme des cations 0,90, donc O/M = 2,22 avec O fixé à 2 ; impossible (O/M ≤ 2 ; attendu 1,70–1,80 par électroneutralité). Renormalisé aux cations, Zr = 0,156 (−22 %).
- Zr déficitaire : piste chiffrée du nitrate de zirconyle hydraté pesé sur la masse anhydre (x = 6 → 0,136) ; présentée comme hypothèse (`reserve`), pas comme preuve.
- Recouvrement Zr Lβ1 2124,4 eV / Au Mα1 2122,9 eV (grille d'or) relu dans la Table 1-3 du X-Ray Data Booklet : la raison « molar mass » donnée par les auteurs est fausse.
- Paramètre de maille : modèle de sphères dures avec les rayons de Shannon que l'article cite, plutôt que l'équation de Kim, dont je n'ai pas pu relire les coefficients (recherche infructueuse). L'ordre mesuré contredit l'ordre prévu (CZEYG, au plus petit rayon, a le 2e plus grand a) : `reserve`.
- Fluorite à 40–60 % de cations trivalents : jugée plausible mais métastable, d'après Djenadic 2017 / Sarkar 2017 et la prépublication arXiv:2512.03881 (bixbyite à l'équilibre pour 20 % de Ce, ordre local invisible en DRX). Auteurs de l'arXiv non relevés.
- Carbonates : La2O2CO3 se décompose vers 770–800 °C (article PMC7603085) ; un résidu possible à 600 °C est signalé en `reserve` (aucune ATG ni IR dans l'article).
- Rapport citrate/métal : indéterminé, de 1 à 48 selon le volume pris (47,6 mmol de CA par 100 mL) ; je n'ai pas supposé de volume.
- pH 5 : 1,66 équivalent de NH3 par citrate, calculé avec les pKa de la fiche Sigma (3,13 / 4,76 / 6,40) plutôt qu'avec le pKa unique de 2,79 donné par PubChem.
- Catalyse, bilan redox `probleme` : sous N2, ≥ 0,81 mmol d'électrons à retirer pour 81 % de benzile, contre ≤ 0,02 mmol de Ce4+ et Pr4+ dans le catalyseur. Aucun oxydant déclaré, et aucune source trouvée sur l'oxydant de ce couplage.
- Vanilline/pipéronal `probleme` : le nom du produit (bis-benzo[1,3]dioxolyl) est celui de la dicétone du pipéronal ; l'erreur vient de l'article, ce n'est pas une erreur de recopie.
- « Benzoic acid transformed totally into chalcone » `probleme` : impossible sans méthylcétone (chalcone C15H12O).
- Corrélation acidité–conversion recalculée (r = 0,997) : la linéarité est réelle, mais la TPD de NH3 ne distingue pas Lewis de Brønsted, et par m2 c'est CZEYG le plus acide : `reserve`.
- Base : aucun HEO ni cérine-zircone comparable (compare.py sur 5 mots-clés) ; seule comparaison faible avec PMC9844074 (CeO2 calciné à 600 °C, 26 m2/g).
- 8 appels web (7 recherches, 1 lecture de page) ; aucun DOI vérifié sur Crossref (bloqué) ; rien ajouté à fondateurs.md ni à constantes.md.
