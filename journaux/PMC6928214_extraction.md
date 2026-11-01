# Journal d'extraction PMC6928214

- Voie de base = S,Se-CQDs : seul protocole décrit en entier (Methods, « Preparation of S,Se-CQDs »). Les trois témoins CQDs, S-CQDs, Se-CQDs sont des branches : la dernière phrase du paragraphe dit qu'ils sont faits « according to the above method ».
- Attribution des réactifs aux témoins : la phrase « citric acid (5 g) or citric acid (5 g) and mercaptoethylamine (0.8 g) or citric acid (5 g) and sodium selenite (0.06 g) … respectively » est lue dans l'ordre des échantillons de la phrase précédente (CQDs, S-CQDs, Se-CQDs). Chaque branche porte donc une ou deux variations « absent » sur les réactifs du parent.
- Héritage des étapes : accepté pour les trois témoins (« according to the above method »). Le volume d'eau (40 mL) n'est pas répété pour les témoins : signalé en doute, pas recopié comme valeur propre.
- Fournisseurs : citrate (Sinopharm) et sélénite (Nanjing) ont leur propre phrase ; la mercaptoéthylamine est citée avec DTNB et XTT dans une phrase unique (Macleans), recopiée entière en `supplier_quote`. Pureté non donnée : déclarée non citée. Le fournisseur de l'eau « pure water » n'est pas donné.
- Étape 6 : lyophilisation notée `freeze_dry` (hors grille « dry ») ; température, durée et pression déclarées non citées, car l'article dit seulement « finally freeze-dry ».
- Séparation (étape 4) et dialyse (étape 5) séparées : « separation supernatant » n'a ni méthode ni outil ; la dialyse donne 2 jours, 200 Da, eau changée toutes les 5 h (paramètre `water_change_interval`).
- Tests antioxydants, MTT, poisson-zèbre, imagerie : traités comme tests du matériau fini. Pas de voies ; leurs conditions vont dans `characterizations` de la voie de base (concentrations, volumes, longueurs d'onde), leurs résultats dans `outcomes`.
- Fig. 5 : ordonnées étiquetées « % » mais graduées de 0 à 1. Valeurs lues en fraction sans conversion, unité écrite explicitement (« fraction (axe 0–1 étiqueté %) »). 40 % du résumé (200 μg/mL) contre ≈ 0,33 lu en Fig. 5e à 200 μg/mL : contradiction gardée en doute, les deux valeurs conservées.
- ·OH : texte 15 % pour S,Se-CQDs, figure ≈ 0,17–0,18. Les deux enregistrées, écart attribué à la lecture graphique.
- Fig. 7 : la légende inverse survie et rythme cardiaque par rapport au texte et à la figure ; ordre de la figure retenu. Axe « Heart Rate (%) » douteux, valeurs ≈ 145 laissées telles quelles. Seuls S-CQDs et S,Se-CQDs sont testés sur le poisson-zèbre (légende), le texte ne parle que de S,Se-CQDs.
- Fig. 6 : trois matériaux indiscernables à 400 μg/mL ; Se-CQDs absent de cette figure. Valeurs ≈ 105 % (HeLa) et ≈ 96 % (MDA-MB-231) lues pour CQDs, S-CQDs et S,Se-CQDs.
- Figures lues : 1, 5, 6, 7. Les figures 2, 3, 4 et 8 portent des spectres ou des images dont les valeurs sont dans le texte ; non relues. La légende de la Fig. 2 parle de « CQDs » alors que le texte parle de S-CQDs et S,Se-CQDs : texte préféré.
- Échantillons sans voie : Vc (témoin positif de la Fig. 5, non décrit) et les témoins de mesure (eau, 0 μg/mL).
- method_sources : seuls MTT (CR30) et poisson-zèbre (CR31) sont retenus ; Fenton, DTNB et XTT (CR23, CR26, CR28, CR29) soutiennent la chimie des tests, dont les quantités sont données dans les Méthodes.
- Aucune annexe n'est citée par l'article ; aucune « annexe absente » à déclarer.
