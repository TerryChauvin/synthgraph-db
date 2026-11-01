# Relecture du palier 3 (publications 101 à 150)

Session cloud du 2026-10-13 au 2026-10-14. Paliers 3 et 4 traités ensemble, sur 100 publications, à la demande de l'utilisateur.

## Bilan

- 50 publications closes : 556 voies (128 de base, 428 branches), 10 050 citations vérifiées, toutes exactes. Complétude moyenne 0,77.
- `audit.py 3` : 0 bloquant et 0 avertissement ouvert après traitement. 28 avertissements ont été acceptés (voir plus bas).
- Le pipeline est le même qu'au palier 2 : extraction → contrôle et chargement → critique de fidélité et critique scientifique → correction → clôture.
- 8 relectures intégrales : 0 valeur fausse sur 981 valeurs contrôlées.
- Échantillon de 30 valeurs : 0 erreur, 1 imprécision.
- Coût : 0,605 M jetons par publication (médiane), contre 0,63 M au palier 2.

## Relectures intégrales

| Publication | Valeurs contrôlées | Fausses | Remarque |
|---|---|---|---|
| PMC11602897 | 152 | 0 | |
| PMC10350639 | 148 | 0 | |
| PMC4531889 | 56 | 0 | |
| PMC9605960 | 242 | 0 | 169 cellules de tableau contrôlées par script ; les résultats du Run-9 sont vérifiés contre le texte |
| PMC6562340 | 60 | 0 | |
| PMC10964133 | 76 | 0 | Tableau S1 aplati par l'extraction, ordre des rangées vérifié |
| PMC8600520 | 96 | 0 | |
| PMC10037322 | 151 | 0 | |

## Critiques : constats et comparaison avec les paliers 1 et 2

| | Palier 1 | Palier 2 | Palier 3 |
|---|---|---|---|
| Constats de fidélité | 526 | 403 | 435 |
| Médiane par publication | 10 | 8 | 8,5 (de 5 à 15) |
| Constats « faux » | 29 | 7 | 5 |

Répartition des 435 constats par type :
- `mineur` : 189
- `manquant` : 152
- `deduit` : 40
- `attribution` : 26
- `non_cite_a_tort` : 23
- `faux` : 5

Sur les 435 constats, 417 ont été corrigés et 18 rejetés. Les rejets sont motivés par le texte, dans quatre cas :
- un renvoi de contexte, qui n'est pas une source de méthode ;
- une contradiction interne de l'article : la valeur littérale est gardée, avec un doute et une limite ;
- un héritage justifié par une phrase générale des Méthodes ;
- un test du matériau fini, rangé en résultat et non en branche.

Les 5 constats « faux » :
- **PMC7786535, deux constats :**
  - une annotation de mécanisme donnait une plage de température non écrite ;
  - une entrée de `method_sources` était mal classée (Ojha et al., renvoi pour un ajustement de courbe).
- **PMC8309541 :** une réponse de capteur lue sur la Fig. 6 portait une étiquette trompeuse (« first_cycle_peak »).
- **PMC7279382 :** une revue de contexte avait été prise pour la source de méthode de l'électrode BiNPs@Ti3C2Tx.
- **PMC10964133 :** le rapport 2-méthylimidazole/Zn de l'annotation ZIF-8 était donné comme ≈ 16. Le calcul juste est 8 (1,12 mmol contre 0,14 mmol), et l'annotation est corrigée.

Comme au palier 2, aucune valeur numérique recopiée du texte n'était fausse. Les « faux » sont des annotations, des classements de sources ou une étiquette de lecture de figure.

Critique scientifique : 305 jugements de voie (112 cohérentes, 168 douteuses, 12 invérifiables, 13 incohérentes) et 263 contrôles au statut `probleme`. Les problèmes venant de l'article sont devenus des annotations `limite_reproductibilite`, et aucune valeur n'a été changée sur la foi de cette critique.

## Avertissements de l'audit acceptés (28)

- **12 sur PMC9076075 :** Cs est apporté par l'intermédiaire Cs-oléate (voie séparée), qui n'a pas de formule propre.
- **8 sur PMC4214824 :** Ti, Ni et Au viennent de cibles ou de multicouches métalliques déposées physiquement.
- **PMC6548969 :** Cs, Pb et Br viennent des nanocristaux CsPbBr3 préformés.
- **PMC9036687 :** Ca vient d'une source naturelle (coquilles).
- **PMC10883016, deux avertissements :** Ca et P viennent d'os, source biologique ; le séchage à 110 °C porte sur un solide déjà sans solvant.
- **PMC9078598, deux avertissements :** recuit à 300 °C d'un film déjà séché, l'éthanol est parti.
- **PMC6376056 :** séchage du capteur à 150 °C, sans récipient fermé.
- **PMC7692729 :** l'unité « °C∙min−1 » est écrite avec un point médian, recopiée telle quelle, sans conversion SI.

## Échantillon de 30 valeurs du rapport d'audit

30 lignes relues. Dans les 30 cas, la citation soutient la valeur pour la bonne étape et la bonne voie. Pour les lignes de tableau, la colonne et la rangée ont été vérifiées contre l'en-tête.

0 erreur, 1 imprécision : PMC9218112, « 2 mL vials ». C'est la contenance du flacon, pas un volume de réactif. Le nom du paramètre le dit, mais un lecteur pressé peut s'y tromper.

## Stœchiométrie et cohérence chimique (5 voies)

| Voie | Contrôle | Verdict |
|---|---|---|
| PMC10350639 AZ1 (ZSM-5 amorphe) | TEOS 27 mL → 0,121 mol de SiO2 (7,26 g) ; Al(OH)3 0,3275 g → 2,10 mmol d'Al2O3 (0,214 g). SiO2/Al2O3 ≈ 34 en masse, ≈ 58 en moles | l'article annonce 6,2. L'écart est déjà annoté en limite |
| PMC10964133 ZIF-8 | 0,56 M × 2 mL de 2-MeIm = 1,12 mmol, 70 mM × 2 mL d'acétate de Zn = 0,14 mmol → 8:1 | excès de ligand courant pour ZIF-8 ; annotation corrigée (16 → 8) |
| PMC10037322 CsPbIBr2 | CsI 600 mg = 2,31 mmol, PbBr2 800 mg = 2,18 mmol → Cs:Pb = 1,06, I:Br = 1:1,9 ; ≈ 1,1 M dans 2 mL de DMSO | conforme à CsPbIBr2 |
| PMC6562340 g-C3N4 | mélamine 3 g, 520 °C, 4 h | conditions standard de polycondensation ; rendement non donné |
| PMC8600520 Ag-12.0 | AgNO3 à 12 % en masse sur 0,5 g de polymère (chitosane + PEO), 70 °C, 2 h | réduction par le chitosane plausible à l'air ; la base du pourcentage n'est pas précisée par l'article (doute présent) |

## Contrôle croisé (`compare.py`)

- **g-C3N4 :** la mélamine à 520–550 °C donne des surfaces et des pics (002) cohérents d'une publication à l'autre.
- **MCM-41 :** les SBET de 739 à 996 m²/g sont cohérents. La valeur basse est un MCM-41 chargé en ZnO.
- **CsPbBr3 :** les émissions de 526 à 530 nm et les tailles d'environ 8 nm concordent. Les boîtes de 2,6 nm à 454 nm (PMC5122874) s'expliquent par un fort confinement.

Rien d'aberrant au-delà de ce qui est déjà annoté.

## Sources du critique scientifique

Crossref est bloqué depuis le cloud. Les 123 DOI du palier sont listés dans `palier_003_doi_a_verifier.txt`, à vérifier depuis le PC (`python -I sources_check.py --palier 3 10`, puis la liste complète).

Trois sources ont été contrôlées par recherche web :
- **10.1016/j.tca.2005.04.010 :** Ehrhardt et al. 2005, décomposition thermique du nitrate de cobalt (citée pour PMC10350639). Elle existe et dit ce qui lui est attribué.
- **10.1016/j.polymdegradstab.2007.03.023 :** Rahaman et al. 2007, revue du traitement thermique du PAN (citée pour PMC6702676). Conforme.
- **10.1021/la200547k :** non retrouvée par la recherche. Elle reste à vérifier sur Crossref avant d'en conclure quoi que ce soit.

## Règles et outils modifiés pendant le palier

- **RUNBOOK.md :**
  - rôles `quencher` et `stabilizer` ;
  - règle de la branche « sans X » : aucun héritage d'une condition que l'article ne justifie pas.
- **Journal de décisions :** chaque agent écrit `journaux/<PMCID>_<passe>.md` (consignes dans RUNBOOK, CRITIQUE, PLAUSIBILITE et PROMPT_CORRECTION). Ce journal remplace l'archivage des transcriptions.
- `load.py` et `audit.py` n'ont pas été modifiés.

## Coût en jetons (agents seuls, hors orchestrateur)

| Passe | Médiane par publication |
|---|---|
| Extraction (Sonnet) | 160 k |
| Critique de fidélité (Sonnet) | 139 k |
| Critique scientifique (Opus) | 166 k |
| Correction (Sonnet) | 134 k |
| **Total par publication** | **0,605 M** (moyenne 0,611 M ; 30,6 M pour le palier) |

## Ce qui n'a pas été vérifié

- Les DOI sur Crossref : liste à passer depuis le PC.
- Les pages sources elles-mêmes : la plupart des éditeurs sont injoignables depuis le proxy du cloud.
- Les valeurs lues sur figure (876 résultats `from_figure` sur le palier) : seules celles contestées par la critique ont été relues sur l'image.
