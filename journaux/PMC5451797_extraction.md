# Journal d'extraction PMC5451797

- Découpage en trois voies de base, aucune branche : l'article ne balaie aucun paramètre (un seul jeu de conditions par matériau). CQD_solution (CV sur tige de graphite dans l'eau), TiO2_NW (nanowires sur FTO, 6 étapes) et CQDs_TiO2_NW (électrodéposition à −3,0 V, 1 h).
- CQDs_TiO2_NW n'est pas une branche de TiO2_NW : elle ajoute une étape au lieu de changer une valeur. Elle réutilise TiO2_NW et CQD_solution comme réactifs de rôle `intermediate`. TiO2_NW est typée `intermediate` (isolée puis réutilisée, aussi mesurée comme témoin) ; CQD_solution reste `material` (produit-titre de l'article), bien que réutilisée aussi.
- Solution de CQDs comme réactif de l'électrodéposition : « electrodeposition of CQDs onto TiO2 NWs » sans électrolyte écrit. Inscrite en `intermediate`, électrolyte déclaré non cité et mis en doute ; figure S1 (montage) absente du dépôt, signalée en `limite_reproductibilite` (« Annexe absente du dépôt : »).
- Électrodes Ag/AgCl et fil de platine de la voie CQD : en `equipment`, pas en réactifs ; la tige de graphite est le réactif `carbon_source` (consommée à l'anode), sans quantité ni pureté (déclarées non citées).
- Tige 1 / tige 2 et essais 1st–5th de la figure 1a : aucun paramètre ne les distingue dans l'article ; pas de branche, échantillon sans voie dans l'inventaire avec la raison. Aucune valeur n'est donnée par essai.
- Légende de la figure 1 : (b) « UV-Vis » et (c) « PL » sont inversés par rapport à l'image (b = émission, c = absorbance). Le texte écrit « 500 mm » ; conservé tel quel en `value_text`, doute posé. Aucune valeur tirée de la figure.
- Figures ouvertes : 1 et 5. Les valeurs de photocourant (160 et 25 µA cm−2) et du tableau 1 sont dans le texte, donc rien lu sur figure (0 `from_figure`). L'axe de la figure 5a porte « μA cm−1 » : texte retenu (cm−2).
- Tableau 1 : rangée entière citée, colonnes lues par nom d'en-tête (« TiO2 NWs » = 1re valeur, « CQDs/TiO2 NW » = 2e). CPE : 1,89×10−5 (TiO2) et 1,90×10−6 (composite).
- Nettoyage FTO « for 15 min, respectively » : durée de 15 min prise pour l'étape entière, doute posé (15 min par bain ou au total).
- HCl « 12 M » rangé comme pureté (c'est la seule indication de titre donnée) ; fournisseur « Alderich » recopié tel qu'écrit (faute de l'article pour Aldrich).
- Diamètre de 30 nm des TiO2 NWs : lu sur l'image TEM du composite (fig. 3a), rattaché à CQDs_TiO2_NW ; bandes Raman rattachées au composite bien que la légende de la figure 3b couvre aussi TiO2 NWs.
- Chauffage à 500 °C après TiCl4 : action `heat` (« heat treatment »), non `anneal`, pour ne pas affirmer un recuit ; atmosphère et vitesse de chauffe non citées. Le recuit final (« further annealing ») est `anneal`.
- `method_sources` vide : aucun renvoi dans les Méthodes (vérifié dans corpus/refs : 0 marqueur). Le renvoi sur la détection de 1O2 par DMPO est de l'interprétation, non un protocole repris.
- Aucune annotation `comparaison_branches` (pas de branche) ; la comparaison TiO2 contre CQDs/TiO2 est en `tendance_observee`.
