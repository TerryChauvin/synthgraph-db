# Journal de la passe de complément — PMC13257848

Une seule voie (ZIF-8@TPPa) ; Text S1 (ZIF-8) et Text S3 (caractérisation) sont absents du dépôt, aucune section Supporting Information dans le fichier texte. Figures non ouvertes : aucune condition de mesure n'y est nécessaire.

Points de la sonde écartés
- agitation (rpm) : les trois occurrences de « 200 rpm » décrivent les essais d'adsorption (3.4), déjà dans `conditions` de ces caractérisations. La synthèse n'a qu'un « vigorously shaken for 10 s » sans vitesse : `stirring_speed` reste en `not_stated` à l'étape 5.
- centrifugation : « centrifuge tube » est un récipient d'essai d'adsorption, pas une séparation du produit. `separation_method` reste non cité à l'étape 7 ; aucun paramètre de centrifugation ajouté.
- répétitions : « triplicate » figurait déjà dans les `conditions` de la cinétique, des isothermes et de la thermodynamique ; ce sont des répétitions de mesure, pas de lots de synthèse. Ajout de `repetitions` (lots) en `not_stated` de la voie après recherche de « batch », « repeated », « triplicate » dans tout le texte : aucun nombre de lots pour la synthèse.
- XRD, TEM/SEM, XPS, EDS : rien dans le texte (rayonnement, plage, tension, appareil). Le seul renvoi est « Detailed information is provided in Text S3 », annexe absente. `instrument` et `conditions` laissés vides plutôt que remplis d'un texte « non cité », et un doute les consigne.

Ajouts
- BET : `conditions` renseigné avec le gaz N2 (seule condition écrite) ; température de mesure, dégazage et appareil signalés non cités.
- Résultats : distribution EDS (qualitative, pas de pourcentages atomiques), bandes FT-IR du composite, énergies N 1s du composite (valeurs en `value_text`, citations exactes du texte).
- `not_stated` : `power` et `frequency` aux étapes 1 et 3 (sonication, après recherche de « sonicat », « W », « kHz » : rien) ; `drying_mode` à l'étape 8 (« desiccated at 60 °C for 24 h » ne dit ni étuve ni vide) ; `repetitions` pour la voie.
- Pas touché : `sonication_power` déjà présent (nom hors vocabulaire, conservé, doublon voulu avec `power`).

Non fait : les positions XRD et les énergies XPS de ZIF-8 et de TPPa seuls ne sont pas ajoutées comme résultats de la voie, car elles décrivent d'autres échantillons (sans voie).
