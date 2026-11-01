# Critique de fidélité des ajouts — PMC8474143

Lecture : sections S1 (méthodes), S2–S5 (annexes) et corps de l'article ; vérification du rattachement aux étapes dans `extractions/PMC8474143.json` (lecture ciblée des étapes et de `not_stated`, pas de relecture entière).

| catégorie | voie | élément | verdict | raison |
|---|---|---|---|---|
| paramètre | QDs-TES | étape 1, atmosphere = argon | juste | « in an argon atmosphere » mot pour mot, bonne étape |
| paramètre | QDs-TES | étape 5, drying_mode = vacuum | juste | « transferred to vacuum … 24 hours », séchage du xérogel |
| not_stated | QDs-TES | wash_volume (étape 4, purification à l'éthanol) | juste | volume d'éthanol de lavage jamais donné |
| not_stated | QDs-TES | gas_flow, cooling_mode, vessel (étape 6, pré-recuit 600 °C) | juste | débit, refroidissement, four absents du texte et des annexes |
| not_stated | QDs-TES | gas_flow, cooling_mode, vessel (étape 7, recuit T2) | juste | idem ; seule l'atmosphère Ar/H2 est donnée |
| not_stated | QDs-TES | power, frequency (étape 13, ultrasons 5 min) | juste | « ultrasonic for 5 min », ni puissance ni fréquence |
| not_stated | QDs-TES | gas_flow, cooling_mode (étape 14, hydrosilylation) | juste | seule « argon-filled Schlenk line » ; débit non donné |
| not_stated | QDs-HSQ | repetitions (niveau voie) | douteux | l'étape 5 de la même voie porte « three times » (extractions au toluène) ; ambigu, à lever si le sens est « lots répétés » |
| not_stated | QDs-HSQ | gas_flow, cooling_mode, vessel (étape 1, recuit 1200 °C) | juste | non donnés |
| not_stated | QDs-HSQ | stirring_speed (une étape d'agitation magnétique) | juste | « magnetic stirring » sans vitesse |
| not_stated | QDs-HSQ | power, frequency (étape 7, sonication) | juste | « sonicated for 5 min » sans puissance |
| not_stated | QDs-HSQ | gas_flow, cooling_mode (étape 8, Schlenk) | juste | non donnés |
| not_stated | QDs-SiO | repetitions (niveau voie) | douteux | même ambiguïté : « for three times » est déjà à l'étape 5 |
| not_stated | QDs-SiO | gas_flow, cooling_mode, vessel (étape 1, recuit 920 °C) | juste | non donnés |
| not_stated | QDs-SiO | stirring_speed (agitation magnétique) | juste | pas de vitesse |
| not_stated | QDs-SiO | power, frequency (étape 7) | juste | sonication 5 min, sans puissance |
| not_stated | QDs-SiO | gas_flow, cooling_mode (étape 8) | juste | non donnés |
| not_stated | QDs-TES/OSTE | repetitions (niveau voie) | douteux | l'annexe S5 donne 7 lots de QDs-TES (Table S9), mais pas pour le composite : sens à préciser |
| not_stated | QDs-TES/OSTE | power, frequency (ultrasons, étape 1) | juste | « ultrasonication » sans valeur |
| not_stated | QDs-TES/OSTE | stirring_speed (mélange « thoroughly », étape 2) | juste | aucune vitesse |
| caractérisation | QDs-HSQ | UV-vis absorption et PL (même absorption et pic PL pour les trois) | juste | phrase du corps, valable pour les trois voies |
| caractérisation | QDs-HSQ | PLQY toluène ~35 % | juste | « ∼35 % » et « 35 ± 4 % in toluene » (Table 1) |
| caractérisation | QDs-HSQ | décroissance PL 216 ± 2 µs, β 0,90 ± 0,01, 878 nm | juste | Fig. S7b, valeurs exactes |
| caractérisation | QDs-HSQ | TGA, perte 220–350 °C (réseau cage) | juste | légende S3 ; la TGA porte sur le précurseur HSQ |
| caractérisation | QDs-SiO | UV-vis absorption et PL | juste | idem HSQ |
| caractérisation | QDs-SiO | PLQY toluène ~15 % | juste | « only ∼15 % even after recipe optimization » |
| caractérisation | QDs-SiO | décroissance PL 136 ± 10 µs, β 0,86 ± 0,08, 878 nm | juste | Fig. S7a |
| caractérisation | QDs-SiO | TGA, quasi pas de perte 30–900 °C sous N2 | juste | légende S3 mot pour mot |
| condition de mesure | QDs-HSQ | TEM : JEM-2100F 200 kV, dépôt sur SiN ~15 nm | douteux | valeur juste (Méthodes) mais citation = phrase de résultat, pas le protocole |
| condition de mesure | QDs-HSQ | UV-vis : Lambda 750, toluène | douteux | valeur juste, citation = phrase de résultat |
| condition de mesure | QDs-HSQ | PLQY : sphère maison 6 pouces, EQ-99, SP2150i, CCD, 440 nm, erreur ~10 % | juste | Méthodes S1 ; citation de la table suffisante |
| condition de mesure | QDs-HSQ | décroissance PL : Shamrock 500, APD, laser 405 nm, 15 W cm-2, 100–500 µs, 0,3–2 kHz, objectif 10x | juste | Méthodes µ-PL ; « room temperature » seulement déduit de la largeur homogène « at room temperature » |
| condition de mesure | QDs-HSQ | TGA : TGA/DSC1, ~10 mg, alumine, 10 °C/min, N2 50 mL/min, 25 (Méthodes) ou 30 (légende) à 900 °C | juste | les deux sources citées |
| condition de mesure | QDs-SiO | TEM | douteux | même défaut de citation que HSQ |
| condition de mesure | QDs-SiO | UV-vis | douteux | même défaut de citation |
| condition de mesure | QDs-SiO | PLQY | juste | idem HSQ |
| condition de mesure | QDs-SiO | décroissance PL | juste | idem HSQ |
| condition de mesure | QDs-SiO | TGA | juste | idem HSQ |
| résultat | QDs-TES | XRD pics Si 28, 48, 55 ° | juste | « all three annealed powders » |
| résultat | QDs-TES | bande SiO2 amorphe 21 ° (référence) | juste | patrons de référence = poudres pré-recuites |
| résultat | QDs-TES | taille TEM 4–5 nm | juste | « all three precursors » |
| résultat | QDs-HSQ | XRD 28, 48, 55 ° | juste | idem |
| résultat | QDs-HSQ | bande 21 ° | juste | idem |
| résultat | QDs-HSQ | taille TEM 4–5 nm | juste | idem |
| résultat | QDs-SiO | XRD 28, 48, 55 ° | juste | idem |
| résultat | QDs-SiO | bande 21 ° | juste | idem |
| résultat | QDs-SiO | taille TEM 4–5 nm | juste | idem (moins uniforme, dit ailleurs) |
| résultat | QDs-SiO | bosses du SiO pré-recuit 28, 50 ° | juste | citation exacte, propre à SiO |
| modifié/retiré | QDs-HSQ, QDs-SiO | TEM sans conditions remplacé par TEM avec conditions | juste | simple enrichissement du même élément, même citation |

## Manques restants

- Conditions de la décroissance PL non reprises : intervalle spectral détecté ~6 nm, largeur homogène supposée ~200 meV, ajustement en exponentielle étirée (traitement qui fixe τ et β).
- Aucune condition pour les spectres d'émission PL (excitation, spectromètre) : l'article ne la décrit pas explicitement ; à déclarer `not_stated` pour UV-vis/PL.
- QDs-TES/OSTE : conditions de PLQY sans « erreur relative ~10 % » ni sphère complète (CCD, monochromateur) ; durée de cure UV (30 s) à vérifier dans l'étape 4 (le paramètre `duration` y est vide).
- Ensemble PLQY dans OSTE pour HSQ (50 ± 5 %) et SiO (25 ± 3 %) : portés par les voies OSTE correspondantes, mais leurs `outcomes` n'ont pas de nom exploitable ; non vérifié plus loin.
- Pas de mention du caractère « précurseur » de la TGA (HSQ, SiO, xérogel TES) dans les conditions : risque de lecture comme TGA des QDs.

## Bilan

- Ajouts contrôlés : tous les 65 éléments listés (2 paramètres, 33 not_stated regroupés par étape, 8 caractérisations, 10 conditions, 10 résultats, 2 modifications) en 49 lignes de tableau.
- Faux : 0.
- Douteux : 7 (trois « repetitions » de niveau voie en conflit ou ambigus avec les étapes ; quatre citations de conditions TEM/UV-vis qui sont des phrases de résultat).
