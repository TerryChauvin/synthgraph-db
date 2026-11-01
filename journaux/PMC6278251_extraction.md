# Journal d'extraction PMC6278251

- Voie de base : 7ZnHAp (xZn = 0,07), parce que le seul protocole écrit contient le nitrate de zinc ; HAp (xZn = 0) est une branche avec la variation « zinc nitrate hexahydrate = absent » (citation : « with various Zn/(Zn + Ca) ion ratios (xZn = 0 and xZn = 0.07) »).
- HAp reçoit ses propres étapes (copie des 7 étapes, étape 1 sans zinc), conformément à la règle « sans X n'hérite pas des étapes de X » ; le texte ne dit pas explicitement que HAp a les mêmes durées et températures, d'où le doute.
- Température de l'étape 5 : 100 °C et 48 h (Méthodes) retenus contre « at room temperature » de la Conclusion ; contradiction consignée en doute.
- Formule du nitrate de zinc : « Zn(NO3)6·6H2O » dans les Méthodes (coquille), formule corrigée en Zn(NO3)2·6H2O dans le champ `formula` seulement, la citation reste celle de l'article.
- Aucune quantité de réactif, pureté, fournisseur dans l'article ni annexe : tout en `not_stated` après recherche de « purity, supplier, Sigma, Merck, purchased ».
- Lavage : « five times » en `value_text` (le nombre 5 n'est pas écrit dans la citation).
- Pas d'étape de séchage ni de calcination : l'article parle de gels puis de « powders » pour XRD ; consigné en doute et en limite de reproductibilité, aucune étape inventée.
- Ca 2p (350,94 et 347,27 eV) : phrase écrite pour « HAp and 7ZnHAp », puis 7ZnHAp décalé vers le bas ; valeurs rattachées à HAp uniquement.
- P 2p : rangées attribuées par le nom d'échantillon écrit dans la phrase (HAp 134,13/133,18 ; 7ZnHAp 133,78/132,91).
- Tableau 3 : chaque rangée contient deux blocs (HAp à gauche, 7ZnHAp à droite, séparés par le second « E = ») ; une valeur 1468.3 apparaît trois fois dans le bloc 7ZnHAp, signalé comme probable erreur de recopie.
- Tableau 2 : légende (E = 2 GPa, R = 4,98 nm) en conflit avec le texte (E = 10 et 6 GPa, R = 13 et 9,7 nm) ; valeurs du tableau extraites, paramètres de légende non repris.
- Rayons de nanoparticule (13 et 9,7 nm) : paramètres d'entrée du modèle FEM, rangés en outcomes `nanoparticle_radius_FEM_input` et non comme taille mesurée.
- Vitesses expérimentales (1454,17 ± 1,06 et 1476,02 ± 0,15 m/s) : `value_num` + `value_text` avec l'incertitude ; « ZnHAp » lu comme 7ZnHAp.
- Durée d'agitation de la suspension pour les ultrasons : 15 min (Résultats) contre 30 min (Méthodes) ; 30 min mises en condition de caractérisation, doute noté.
- Figures : 12 figures présentes, ouvertes (1, 9) ; aucune valeur lue sur figure car tout résultat chiffré est dans le texte ou les tableaux (figures 8 à 11 reprennent les tableaux 2 et 3).
- method_sources : B57 (voie sol-gel adaptée) en protocole_adapte ; B58 et B59 (rapport 1,67) et B35 en « autre » ; MAUD, COMSOL, MATLAB non retenus (outils d'analyse).
- Famille du matériau : `ceramique` (bioceramique) plutôt que `oxyde`.
