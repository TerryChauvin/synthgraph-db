# Journal du critique de fidélité, PMC3833402

- Liste d'échantillons faite avant l'extraction : le complexe [Cd(detu)2(OOCCH3)2]·H2O (2.2), les nanoparticules CdS-HDA (2.4), plus le ligand libre (IR) et le CdS massif (comparaison). Même liste que `sample_inventory` : aucun échantillon manquant. L'article ne teste qu'une condition de thermolyse, donc aucune branche attendue.
- Quantités vérifiées une à une contre 2.2 et 2.4 : 2 mmol / 0,533 g Cd(OAc)2·2H2O, 4 mmol / 0,529 g detu, 50 + 50 mL éthanol, reflux 6 h, 0,5 g complexe, 10 mL TOP, 6 g HDA, 150 °C, chute de 20–30 °C, 1 h, refroidissement à 70 °C. Toutes exactes. Conversions masse/mmol refaites (266,5 et 132,2 g/mol) : cohérentes.
- Formule et analyse élémentaire : C 168,15/512,96 = 32,78 % retrouvé ; la formule C14H32CdN4O5S2 est cohérente avec 2 detu + 2 acétate + H2O.
- Cases `not_stated` (31 comptées) toutes vérifiées contre le texte : aucune n'est à tort. Le doublon `speed` / `centrifuge_speed` à l'étape 6 est sans conséquence et n'est pas signalé.
- `method_sources` vide : les renvois de 2.2 et 2.4 n'existent pas ; B16/B17 (SAINT, SMART, SHELX), B20/B21 (liaisons thioamide) et B22 (résidu CdS) ne sont pas des méthodes. Pas de constat.
- Aucune valeur `from_figure`. J'ai ouvert les figures 3 à 7 quand même : l'ATG montre un résidu d'environ 28–29 %, cohérent avec CdS ; l'absorption montre un épaulement vers 425–430 nm, la PL sature près de 565 nm (texte 559 nm, non corrigé : le texte fait foi) ; le DRX porte deux astérisques non expliqués (~41,5° et ~48°) et le TEM montre des bâtonnets en plus de particules sphériques.
- Constat 1 (`deduit`, probable) : « d'où une injection à 150 °C » est un lien causal inventé par l'annotateur ; le texte dit seulement que la synthèse est à 150 °C, et la décomposition se termine à 233 °C, donc l'argument ne tient pas. Probable et non sûr car c'est une annotation (interprétation).
- Constat 2 (`attribution`, probable) : l'inférence « décomposition en phase liquide après fusion » porte sur le solide en ATG/ATD, voie du complexe, pas sur la thermolyse dans HDA.
- Constat 3 (`manquant`, sûr) : pics DTG 61 et 186 °C et résidu 3,68 mg contre 3,65 mg absents de la caractérisation comme des résultats ; sûr car ils sont textuels et absents du JSON.
- Écarté comme non-constat : l'hexagonal / cubique. L'extracteur a recopié « hexagonal » et posé un doute ; c'est la bonne conduite. Je demande seulement une annotation limite_reproductibilite (constat 7, mineur), avec les astérisques de la figure 5.
- Écarté : la différence 111,59 contre 115,59° (texte contre Table 2) : déjà en doutes, donnée de structure sans extraction.
- Écarté : EDX annoncé en 2.5 sans résultat dans l'article ni dans les figures : ce n'est pas une omission de l'extracteur, noté en lacune de reproductibilité.
- Recristallisation (conclusion) contre évaporation directe (2.2) : contradiction interne de l'article ; probable seulement, mise en `mineur`.
