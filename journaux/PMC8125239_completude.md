# Journal du test de complétude — PMC8125239

- Extraction d'origine déjà très complète : 13 branches, tableaux 1 à 3 et valeurs de figures 2 à 4 et 11 à 15 en `outcomes`, XPS par échantillon. Seule lacune structurelle : l'essai catalytique du matériau fini, décrit dans les doutes mais pas en données.
- Choix : l'essai UV-CWPO est rangé en entrée `characterizations` de la voie de base (pas en voie `device`, pas de synthèse) ; l'eau brute (DCO 1510 etc.) est une entrée séparée car c'est une caractérisation de la matrice, pas une condition de réglage.
- Les cinq méthodes d'analyse (DCO, COT, UV254, DBO5, respirométrie) ont chacune une entrée unique avec appareil et conditions, comme demandé pour les étalonnages.
- Pression de vapeur saturante de 0,2 MPa : gardée dans les conditions de l'essai (phrase des auteurs expliquant le choix de 0,5 MPa), pas en `outcomes`. Texte de l'entrée : la citation d'appui ne couvre que la première phrase de la méthode, les autres éléments viennent de la même section 2.3 et des légendes.
- Valeurs nominales XPS (795.5, 780, 779, 781, 528.5, 531) : déjà couvertes par les énergies A/B de chaque échantillon ; non ajoutées. Valeurs de texte de la BET (2.685, 13.073, ...) : le tableau 1 est retenu, écart déjà en doubts.
- `comparisons` : trois valeurs de l'introduction ajoutées (LaFeO3/TCE, LaNiO3/RB5 ×2). Elles décrivent d'autres systèmes ; un doubt le dit. Les renvois B13 et B14 sont ceux de la liste de références (Hsu 2019 ; Palas 2018).
- Conditions de mesure absentes de l'article (dégazage BET, pas XRD, taille de cristallite) : mises en `doubts`, jamais en `not_stated`.
- Aucune figure rouverte : tous les résultats chiffrés des figures 5 à 10, 16 et 17 sont écrits dans le texte ou les tableaux.
- `not_stated` ajoutés à la voie de base : `repetitions` (nombre de lots de synthèse) et `scale` ; cherchés par mot-clé dans tout le fichier, aucune mention.
- Rien n'a été modifié ni retiré ; `load.py check` : 0 erreur (1 avertissement d'origine, voie LaCoO3 sans réactif, déjà expliquée dans un doubt).
