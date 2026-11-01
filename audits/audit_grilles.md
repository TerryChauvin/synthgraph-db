# Respect des grilles de réglages (synthèse et caractérisation)

500 publications au format 2. Script : `analyses/audit_grilles.py`. « Suspect » = case déclarée « non cité » alors que la citation de l'étape (ou une phrase de l'article nommant le réactif) contient un indice de la valeur : à relire, pas une erreur prouvée.

## A. Grille de synthèse (imposée par `load.py`)

| Case | Attendues | Citées | Déclarées « non cité » | dont suspectes |
|---|---|---|---|---|
| wash_solvent | 710 | 663 (93 %) | 47 | 0 (0 %) |
| repetitions | 710 | 358 (50 %) | 352 | 3 (1 %) |
| temperature | 2647 | 2114 (80 %) | 533 | 52 (10 %) |
| duration | 4521 | 3156 (70 %) | 1365 | 158 (12 %) |
| speed | 452 | 272 (60 %) | 180 | 0 (0 %) |
| atmosphere | 493 | 208 (42 %) | 285 | 6 (2 %) |
| heating_rate | 493 | 110 (22 %) | 383 | 0 (0 %) |
| ph | 112 | 109 (97 %) | 3 | 1 (33 %) |
| purity | 4474 | 1866 (42 %) | 2608 | 265 (10 %) |
| supplier | 4474 | 2406 (54 %) | 2068 | 86 (4 %) |

Exemples de cases suspectes :

- repetitions : PMC9929317 étape 6 (wash) : « The paste was centrifuged at 3500 rpm for 10 min, three times, and then washed with doubly distilled water. »
- repetitions : PMC9929317 étape 6 (wash) : « In addition, the precipitate obtained was centrifuged at 3500 rpm for 10 min, three times, and then washed with doubly distilled water (DDW). »
- temperature : PMC3833323 étape 4 (dry) : « The mycelia were freeze-dried and stored at 4°C in air-tight containers prior to use. »
- temperature : PMC6702676 étape 5 (calcine) : « The ZnSe@N-C was synthesized by precursor solution directly dried at 80°C overnight and calcined at the same way with Se powder. »
- duration : PMC4639899 étape 8 (anneal) : « The PMMA on 2D materials was removed by acetone and thermal annealing under forming gas at 450 °C. »
- duration : PMC4639899 étape 7 (anneal) : « The PMMA on 2D materials was removed by acetone and thermal annealing under forming gas at 450 °C. »
- atmosphere : PMC8155954 étape 3 (sinter) : « The precursors were pre-sintered at 500 °C for 6 h to decompose impurities and they were then calcined at different temperatures (750 °C (NCM750), 800 »
- atmosphere : PMC9689030 étape 9 (anneal) : « The samples were then dried in ambient air for 100 °C for 10 min before being annealed at 400 °C for 15 min. »
- ph : PMC10674298 étape 4 (adjust_ph) : « The uniform mixture of ethylene glycol, citric acid, and the precursors of the cations of interest was brought to a suitable pH by slowly adding ammon »
- purity : PMC5438438 2-methylimidazole : « ## Experimental section ## Materials Horseradish peroxidase (HRP) (reagent grade), Candida antarctica lipase (CALB), 2-methylimidazole, phosphate buffer saline  »
- purity : PMC5438438 Candida antarctica lipase B : « ## Experimental section ## Materials Horseradish peroxidase (HRP) (reagent grade), Candida antarctica lipase (CALB), 2-methylimidazole, phosphate buffer saline  »
- supplier : PMC5309769 toluene : « ## CdSe NCs CdSe NCs dispersed in toluene were purchased from Sigma-Aldrich Co. »
- supplier : PMC11231976 deionized water : « The nitrate precursor was formulated by dissolving cobalt nitrate hexahydrate [Co(NO3)2·6H2O, Thermo Scientific] and lithium nitrate [LiNO3, Thermo Scientific]  »

### Réglages de procédé hors grille (jamais exigés)

| Réglage | Étapes dont la citation le mentionne | Extrait | Déclaré « non cité » | Ni l'un ni l'autre |
|---|---|---|---|---|
| vitesse d'agitation | 531 | 75 | 9 | 447 (84 %) |
| refroidissement | 437 | 41 | 166 | 230 (53 %) |
| débit de gaz | 133 | 44 | 38 | 51 (38 %) |
| pression / vide | 487 | 73 | 207 | 207 (43 %) |
| taux de remplissage | 76 | 2 | 2 | 72 (95 %) |
| vitesse d'addition | 349 | 191 | 51 | 107 (31 %) |
| puissance | 55 | 43 | 0 | 12 (22 %) |

## B. Grille de caractérisation (aucune n'est imposée)

| Technique | Entrées | Publications | Avec appareil | Avec conditions |
|---|---|---|---|---|
| XRD | 1509 | 418 | 90.3 % | 82.5 % |
| BET | 404 | 161 | 90.3 % | 83.2 % |
| TEM/SEM | 1582 | 478 | 88.7 % | 53.2 % |
| XPS | 455 | 183 | 79.3 % | 52.5 % |
| UV-vis / gap | 628 | 256 | 91.6 % | 74.7 % |
| PL | 379 | 131 | 84.7 % | 85.0 % |
| TGA | 248 | 125 | 87.1 % | 83.1 % |
| électrochimie | 301 | 103 | 84.7 % | 98.3 % |
| catalyse / adsorption | 348 | 117 | 70.1 % | 96.0 % |

Réglages attendus, par publication : présents dans les conditions extraites, et mentionnés quelque part dans l'article (borne haute de ce qui est extractible).

| Technique | Réglage | Dans la base | Mentionné dans l'article |
|---|---|---|---|
| XRD | rayonnement | 68.7 % | 86.8 % |
| XRD | plage 2θ | 45.5 % | 96.9 % |
| XRD | pas / vitesse | 27.3 % | 80.1 % |
| BET | gaz / température | 53.4 % | 98.8 % |
| BET | dégazage | 31.7 % | 44.7 % |
| TEM/SEM | tension | 38.1 % | 53.8 % |
| TEM/SEM | nombre de particules | 2.7 % | 47.5 % |
| XPS | source | 30.6 % | 70.5 % |
| XPS | référence C 1s | 17.5 % | 68.3 % |
| UV-vis / gap | plage | 26.2 % | 96.1 % |
| UV-vis / gap | méthode du gap | 7.4 % | 27.0 % |
| PL | excitation | 73.3 % | 95.4 % |
| TGA | atmosphère | 71.2 % | 100.0 % |
| TGA | rampe | 71.2 % | 76.0 % |
| électrochimie | électrolyte | 33.0 % | 99.0 % |
| électrochimie | masse active / électrode | 1.0 % | 43.7 % |
| électrochimie | vitesse de balayage | 50.5 % | 66.0 % |
| catalyse / adsorption | masse de catalyseur | 63.2 % | 87.2 % |
| catalyse / adsorption | concentration | 61.5 % | 100.0 % |
| catalyse / adsorption | source lumineuse | 49.6 % | 100.0 % |
