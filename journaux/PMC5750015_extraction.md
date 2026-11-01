# Journal d'extraction PMC5750015

- Découpage : une voie de base (Water-based, schéma 1 du texte) et deux branches (DMF-based, THF-based) ; un seul paramètre change, le solvant de la solution de CNTH (« CNTH was dissolved in distilled water (figure 1, scheme 1), THF (scheme 2) and DMF (scheme 3) »). Phrase « All other reaction parameters ... were kept the same » : héritage complet accepté.
- Voie de base = eau, bien que son produit soit surtout du β-CPF : c'est le premier schéma de l'article et le protocole est décrit pour les trois ; choix de convention, noté dans le résumé.
- succeeded : Water-based false (phase majoritaire différente de HA, visée par Ca/P = 1,67), DMF-based true (HA majoritaire, β-CPF très minoritaire), THF-based true. Les auteurs ne parlent pas d'échec : doute écrit.
- Numérotation des schémas : le texte dit THF = schéma 2 et DMF = schéma 3, la figure 1 (lue) l'inverse. Les voies portent le nom du solvant, donc aucun effet sur les données ; doute écrit.
- Tableau 2 : colonnes lues dans l'ordre eau, DMF, THF (en-tête « water-based | DMF-based | THF-based »), pas dans l'ordre THF, DMF du texte. Chaque rangée est recopiée entière en citation et attribuée par le nom de la colonne.
- Crystallite size de l'eau (19,4 nm, k = 0,89) : probablement la phase β-CPF (pic 201), mais l'article ne le dit pas ; valeur gardée, doute écrit.
- Ammoniaque : « The pH of aqueous solutions was adjusted » ne dit pas quelle solution ; la figure 1 place NH4OH du côté CNTH, d'où l'étape 3 avant l'addition de DAHP. Dans les mélanges, « NH4OH was added into 5 ml of water and then diluted with the organic solvent » devient un réactif d'eau (5 mL) et une variation à nom explicite dans chaque branche : le contrôle émet un avertissement (nom absent du parent), expliqué en doute.
- pH « 10–12 » : plage, donc value_text et pas de valeur numérique.
- Température : 40 ± 2 °C citée par la phrase du résumé « All reactions were carried out at 40 ± 2°C for 4 h » (la tolérance n'entre pas dans value_num, qui vaut 40).
- Agitation pendant les 4 h : le texte ne la donne que pendant l'addition ; la figure 1 dit 250 r.p.m. pour les 4 h mais n'est pas citable, donc stirring_speed déclaré non cité à l'étape 6.
- Atmosphère de calcination et vitesse de refroidissement : non citées (recherche « atmosphere », « air » : seul « air oven » pour le séchage).
- Volumes de solvant : seulement la concentration 0,5 M ; amount_text plutôt qu'une quantité déduite (200 mL ou 120 mL non calculés).
- Pureté : « Reagent-grade » appliqué aux cinq produits listés par la phrase Materials (Merck, « used as received ») ; eau « Triple distilled water was used for all experiments » pour les eaux de dissolution, fournisseur non cité.
- Tableau 1 (pics DRX de référence HA et β-CPF d'après les fiches PDF) non extrait : données de référence, pas des résultats d'échantillon.
- Raman DMF-1 et DMF-2 : deux points d'analyse du même échantillon, pas deux voies (inventaire avec route DMF-based).
- Figures : seule la figure 1 lue (schéma) ; figures 2 à 6 (spectres, images) sans valeur utile absente du texte ; aucune valeur lue sur figure.
- method_sources : réfs C36 et C37 (sol–gel « reported earlier ... with minor variations »), protocole_adapte, route null car commun aux trois voies ; aucune autre source de méthode (Scherrer, additivité de la constante diélectrique exclus).
