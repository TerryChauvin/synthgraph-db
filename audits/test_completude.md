# Test de complétude (20 publications, 28/10/2026)

Question de l'utilisateur : l'extraction contient-elle toutes les informations pertinentes de l'article (propriétés du matériau, paramètres de synthèse, réglages qui ont mené à chaque mesure) ? Consigne : `PROMPT_TEST_COMPLETUDE.md` (lecture intégrale de l'article, ajout seulement, relevé de tri de chaque nombre absent). Périmètre validé par l'utilisateur : résultats, conditions de mesure, valeurs de référence, statistiques, littérature (table `comparisons`), calculs (voies `kind: calcul`).

## Tirage

Trois strates sur les 480 publications hors pilote, tirage au hasard dans chacune (`audits/test_completude/tirage.json`) : S1, au moins 15 valeurs absentes estimées (102 publications, 7 tirées) ; S2, au moins 3 alertes « conditions de mesure absentes » de la sonde (170, 6 tirées) ; S3, témoins sous les deux seuils (208, 7 tirées).

## Résultats

| Strate | Publications | Résultats ajoutés (médiane) | Conditions de mesure (médiane) | Valeurs de littérature (médiane) | Paramètres de synthèse (total) | Jetons (médiane) |
|---|---|---|---|---|---|---|
| S1 valeurs | 7 | 28 | 13 | 9 | 55 | 165 k |
| S2 conditions | 6 | 12 | 5 | 5 | 11 | 162 k |
| S3 témoins | 7 | 19 | 4 | 8 | 7 | 160 k |
| **Total** | **20** | **557** | **178** | **341** | **73** | **3,46 M** |

Plus 165 entrées de caractérisation, 53 cases `not_stated`, 5 voies de calcul (DFT, TD-DFT, modèle à trois niveaux), 15 champs existants complétés (`null` rempli ou chaîne de conditions allongée), aucun élément retiré.

Couverture des nombres de l'article (`analyses/couverture_valeurs.py`) sur ces 20 publications : tableaux 83,3 % → 99,9 % ; nombres avec unité du texte 84,8 % → 98,8 %.

**Jugement des agents** : 20 sur 20 « oui sauf ». La synthèse (réactifs, quantités, étapes, branches) était complète dans toutes ; manquaient, selon les publications : les conditions de mesure et des essais (biologiques, catalytiques, électrochimiques, pompe-sonde), les résultats secondaires (positions de pics, tableaux d'annexe, ajustements de modèles, mesures sur dispositifs), les valeurs de la littérature et les calculs. Un seul manque de fond touchant le cœur d'un article : PMC12043898, dont les calculs DFT qui fondent la conclusion n'étaient pas extraits.

## Fidélité des ajouts (critique sur 4 publications, une par strate et la plus grosse)

| Publication | Ajouts contrôlés | Faux | Douteux |
|---|---|---|---|
| PMC9227472 (S1) | 56 | 0 | 6 |
| PMC12043898 (S1) | 415 | 26 | 40 |
| PMC10131834 (S2) | 77 | 0 | 1 |
| PMC10324055 (S3) | 82 | 0 | 7 |
| **Total** | **630** | **26 (4,1 %)** | **54 (8,6 %)** |

25 des 26 faux viennent d'une seule cause : l'agent de PMC12043898 a extrait des valeurs du fichier de réponses aux relecteurs (annexe MOESM4, « Peer Review File »), qui n'est pas l'article publié. Les 11 ajouts dont la citation n'existe que dans ce fichier ont été retirés ; les autres signalés ont une citation présente aussi dans l'article ou son annexe publiée. Hors cette cause, corrigée dans la consigne en cours de test : **1 faux sur 630 (0,2 %)** (une case `not_stated` contredite par le texte). Les douteux sont surtout des attributions à toute une série d'une phrase générale, des valeurs que l'article contredit lui-même, et des cases `not_stated` discutables.

Autres corrections faites pendant le test : échelle de sensibilité d'un test antimicrobien (seuil de la littérature) déplacée des résultats vers les conditions de mesure (PMC9227472) ; voies `calcul` exemptées de la grille de reproductibilité dans `load.py` (sinon impossibles à créer).

## Défauts de consigne relevés (à corriger avant toute généralisation)

1. **Fichiers de relecture par les pairs** pris comme source : à exclure explicitement (fait en cours de test).
2. **Conditions de mesure ajoutées en fin de chaîne `conditions` existante, sans citation propre** (PMC5302706, PMC6443225) : `load.py` ne vérifie pas ces chaînes contre le texte. Règle : une condition ajoutée = une entrée avec sa citation.
3. **Valeurs d'étalonnage éclatées** (42 temps de rétention GC-MS en 42 entrées, PMC9054543) : une entrée par technique.
4. **Conditions de mesure absentes déclarées en `not_stated`** avec des noms ad hoc : elles vont en doute, la grille `not_stated` est celle de la synthèse.
5. **Pas de lien entre un résultat et la mesure qui l'a produit** : les réglages sont rangés par voie et par technique, pas par valeur. Voir `audits/audit_grilles.md`.

## Conclusions

- **La sélection par la mesure ne sert pas** : les témoins (S3) reçoivent autant d'ajouts que les publications sélectionnées. Les manques sont répartis sur toute la base, pas concentrés.
- **La synthèse est complète** ; ce qui manque, ce sont les propriétés secondaires, les réglages de mesure, la littérature et les calculs.
- **Une passe de complétion sur toute la base est justifiée** si l'objectif est l'exhaustivité (propriétés + paramètres de synthèse + réglages de mesure), après correction des cinq défauts ci-dessus, avec une critique des ajouts sur une publication sur cinq. Coût mesuré : 160–175 k jetons par publication (jusqu'à 395 k pour une publication avec annexes et calculs lourds), soit ≈ 80 M pour 480 publications, plus ≈ 15 M de critiques.

## Fichiers

`PROMPT_TEST_COMPLETUDE.md` ; `audits/test_completude/` (`tirage.json`, `<PMCID>_listes.md`, `<PMCID>_tri.md`, `<PMCID>_ajouts.md`, `<PMCID>_critique.md`) ; `journaux/<PMCID>_completude.md` ; `audits/jetons.csv` (passes `test_completude`, `critique_ajouts`).
