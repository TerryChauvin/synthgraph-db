# Journal critique de fidélité PMC6600758

- Ma liste d'échantillons avant ouverture de l'extraction : MS/CN (Na2MoO4·2H2O 1,0 g + thiourée 3,0 g, 550 °C, 1 h, N2, 10 °C/min), MS (même procédure, 600 °C 2 h), CN (thiourée seule, 550 °C 1 h), puis électrodes (3 matériaux, une recette) et pile bouton 2032. Identique à `sample_inventory` ; les électrodes après 200 cycles et le Tableau 2 de la littérature y sont bien traités hors voies.
- Aucun [[id]] de bibliographie dans les sections 2.1 à 2.3 (corpus/refs) : `method_sources` vide accepté, pas de constat.
- Lavage de CN : « as mentioned above for the preparation of MS/CN » vaut renvoi au lavage de MS/CN (2 × eau, 1 × éthanol). L'extracteur hérite ce lavage pour MS mais déclare `repetitions` non cité pour CN : incohérence, constat `non_cite_a_tort` en `probable` car l'article reste elliptique.
- Fournisseur du Ketjen black et du PAA : « All the chemicals were purchased from Sigma-Aldrich » ouvre la section de synthèse du matériau, pas celle de l'électrode ; je n'ai pas signalé un `non_cite_a_tort` (non-constat, noté dans reproducibility_gaps).
- Figures ouvertes : Fig. 5 (a, b), Fig. 6 (b, d), Fig. 1. Lectures de l'extracteur correctes : 720/880 (MS/CN) et 500/820 (MS) en régime ; CN ~100 ; parts pseudocapacitives 54/65/65/78/84 %, écart < 2 points ; b = 0,55 à ~1,9 V. Aucun constat de valeur.
- Fig. 1B : 3456 cm-1 pour MS/CN et 3173 cm-1 pour CN, soit 283 cm-1 d'écart : l'attribution du pic 3456 au composite est confirmée.
- Fig. 1C : repères 70,3 % et 63,8 % (déjà dans les doutes). Ils redonnent à peu près 78 % et 71 % de MoS2 via MoS2/MoO3, cohérent avec le texte ; pas de constat sur la valeur, mais note de reproductibilité.
- MS « sans g-C3N4 » : le texte dit que la TGA de MS montre une étape de décomposition de g-C3N4 et l'IR un résidu organique ; l'annotation affirme l'inverse. Constat `deduit` en `probable` (interprétation de l'extracteur, pas du texte).
- XPS de MS/CN, CV, pics IR de MS : omissions de résultats, toutes `manquant`. XPS et IR de MS en `sure` (texte explicite) ; CV et plateaux en `probable` (choix de couverture, pas une erreur de valeur).
- `cell_type` déclaré non cité pour Coin_cell alors que « 2032 coin cell » est écrit : `mineur`.
- Contradiction du texte sur Rct (smaller « in both conditions » puis « MS is much lower ») : le doute existe mais pas l'annotation `limite_reproductibilite` ; constat `mineur`.
- Stœchiométrie de l'annotation mécanisme : 3,0 g de thiourée = 39,4 mmol, 1,0 g de Na2MoO4·2H2O = 4,13 mmol : exacte.
- Écarté : MS sans étapes propres (héritage via « following the procedure ») et voie Electrode unique pour trois matériaux ; ces choix sont conformes à l'article.
