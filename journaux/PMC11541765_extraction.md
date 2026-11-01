# Journal d'extraction PMC11541765 (films minces de ZnO sol-gel, photodégradation du bleu de méthylène)

- Découpage : une voie de base `ZnOTF-3L` (protocole décrit en entier dans « ZnO nanoparticles thin film preparation ») et une branche `ZnOTF-6L`. Seule différence écrite : le nombre de couches (« as 3 and 6 layers coated over the glass substrate surface »), portée par une variation `number_of_layers` à l'étape 5. Base = 3 couches parce qu'elle est citée en premier dans tout l'article.
- Lampe UV, laser 305 nm, stockage d'un an : ce sont des conditions de test du film fini, pas de synthèse. Elles sont des résultats (`outcomes`) et des entrées de `characterizations` de `ZnOTF-6L`, jamais des branches (règle « tests du matériau fini »). Ce sont trois entrées de l'inventaire qui pointent vers la même voie.
- Recuit : « Multiple coats ... dried ... and then ... annealing at 500 °C » ne dit pas si le recuit suit chaque couche. J'ai gardé l'ordre du texte (dépôt, séchage, puis un recuit) et noté le point en doute. Durée, atmosphère, rampe du recuit absentes : dans `not_stated`.
- Atmosphère « open air » : donnée seulement pour le séchage entre couches (étape 6), pas pour le recuit ; je ne l'ai pas étendue au recuit.
- Durée « two hours » (agitation) : écrite en lettres, donc `value_text` (le contrôle exige un chiffre dans la citation pour `value_num`).
- Fournisseurs : recopiés comme écrits (« Oxford » pour l'acétate et la MEA, « Merch » pour le 2-méthoxyéthanol), citation dans `supplier_quote`. Aucune pureté ; aucune quantité de réactif dans tout l'article, d'où `amount` en `not_stated` pour les trois réactifs.
- Rôle de la MEA : l'article ne dit pas « stabilizer ». Choix de chimiste (sol-gel à base d'acétate de zinc), signalé en doute.
- Tableaux 1 et 3 : une rangée = un temps, colonnes dans l'ordre (3L lampe, 6L lampe, 6L laser) lu d'après l'en-tête ; chaque valeur rangée sur son système. La colonne « UV laser » à 1440 min vaut « – » : non extraite.
- Tableau 2 : la colonne « UV lamb » n'est pas étiquetée par le nombre de couches. Ses valeurs à 664 nm sont identiques à celles du Tableau 1 pour 6 couches, donc rattachées à `ZnOTF-6L` (doute consigné). Les 664 nm du Tableau 2 ne sont pas reprises (doublon du Tableau 1).
- Tableau 4 : k écrit « 3.7*10− 4 » avec un espace dans l'exposant, donc `value_text` et non `value_num`. Équation 4 écrite avec un signe positif (C = Co e^{kt}) : contradiction signalée, valeurs non modifiées.
- « Degradation reaches around 75% in only 180 min » contre 60 % (Tableaux 3 et 4) : les deux extraits, doute.
- Laser : résumé 25 µW/cm2, Méthodes 0.25 mW/cm2 ; diamètre du faisceau 5 cm (Méthodes), 60 mm (Discussion), « 6.5 cm2 » (légende Fig. 4). Valeurs des Méthodes dans les conditions de caractérisation.
- XRD sans nombre de couches : rattaché à la voie de base, avec doute.
- Figures lues : Fig. 1, 2, 3 et 6 ; aucune valeur lue sur figure (`from_figure` : 0), tout est dans le texte ou les tableaux. Les gaps de Fig. 3c n'ont pas été relus (texte : 3.19 et 3.21 eV).
- Numérotation : le texte appelle « Fig. 6 » la photoluminescence, les légendes Fig. 7 ; légendes retenues.
- Tableau 5 (DFT) et témoin sans film : aucune voie ; résultats DFT en annotation `tendance_observee`.
- `method_sources` : seul renvoi de méthode utile = CR42 (« explained in detail in previous work »), `protocole_complet`. Non retenus : Scherrer (CR43), densité de puissance (CR44), Gaussian 09 et B3LYP (CR45 à CR49), équations de cinétique (CR37), comparaison à Mondal (CR41).
