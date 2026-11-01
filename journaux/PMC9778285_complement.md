# PMC9778285 — complément (journal de décisions)

Sonde : 7 points. Une seule vraie lacune de contenu ; le reste était déjà couvert ou hors sujet.

Points écartés
- Rampe de chauffe (« 10 degrees/min ») : appartient à la TGA/DTA (Méthodes 4.2), déjà dans `characterizations.conditions` de TGA/DTA sur MW_gel et SG_gel. Les `heating_rate` de la calcination à 300/500/650 °C restent `not_stated` : l'article ne donne aucune rampe de four.
- Débit de gaz (« flowing air atmosphere of 80 mL/min ») et atmosphère : mesure TGA, déjà dans les conditions TGA. Ne vaut pas pour la calcination, dont l'atmosphère reste `not_stated` (non cité, recherche faite dans tout le fichier).
- Vide (« high vacuum mode ») : condition MEB, déjà dans les conditions SEM de toutes les voies. Rien à mettre dans une étape de synthèse.
- Raman : seule occurrence = résultat de Zargar et al. (littérature, film épais recuit à 550 °C), aucune mesure Raman des auteurs. Rien ajouté.
- Catalyse / adsorption : faux positif (« physically absorbed water » dans l'analyse thermique). Pas de test catalytique ni d'adsorption dans l'article.
- EDS « résultat absent » : le texte ne donne qu'une confirmation qualitative de V (déjà extraite). Fig. 5 ouverte : spectre avec pics Zn K/L, O K, C K et un petit pic V K, sans tableau de teneurs ni pourcentages ; aucune valeur lisible, rien ajouté en résultat.

Ajouts
- MW@650, caractérisation EDX : `conditions` renseigné (poudre sur ruban carbone double face, sans revêtement, 10 et 20 kV, mode haut vide), tirées des Méthodes 4.2 qui décrivent le SEM-EDX commun. Le champ était null ; instrument déjà présent.
- Cases `not_stated` ajoutées après recherche dans tout le texte, légendes et annexes comprises (aucune annexe dans ce fichier) : `repetitions` sur la voie de base MW_gel (aucun nombre de lots ni de répétitions) ; `cooling_mode` sur l'étape micro-ondes de MW_gel (rien sur le refroidissement après 10 min à 60 °C) ; `vessel` sur les étapes de calcination de MW@500 et SG@500 (creuset ou nacelle non cités ; les creusets Al2O3 cités sont ceux de la TGA).
- Non ajoutés car sans objet ou déjà couverts : pH (sol–gel éthanolique, pas de mesure de pH dans l'article), lavage, centrifugation, purification (aucune de ces opérations), `drying_mode` (déjà couvert par `oven_type`), `fill_fraction` et volume d'autoclave (pas d'autoclave).

Aucune valeur, citation, étape, voie ni annotation existante modifiée ni retirée ; aucune case `not_stated` retirée (aucune contredite par le texte). Les doutes existants (SG_gel hérité de MW_gel, 10/20 kV contre 30 kV, tailles MEB) sont inchangés.
