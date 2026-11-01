# Journal d'extraction PMC9061421

- Une seule voie de base (N-CDs) : l'article ne balaie aucun paramètre de synthèse. Pas de branche. La seule série (QY à 0,01, 0,1 et 1 mg mL−1) est une dilution du matériau fini pour la mesure, donc des résultats de la voie et non des branches.
- Détection du Cr(VI), restauration à l'acide ascorbique, eau de rivière (Table 2) et germes de haricot mungo : tests du matériau fini, rangés en `outcomes` ou laissés sans voie dans `sample_inventory` avec raison (règle « tests du matériau fini »). Aucune voie `device` : rien n'est fabriqué à partir du matériau.
- Température de l'étape 2 : l'article donne 80 °C puis 228 °C comme profil mesuré par capteur (« the temperature sharply increased from 80 °C to 228 °C »), pas comme consigne. Case `temperature` déclarée non citée, 228 °C gardé en `outcomes` (microwave_reaction_temperature_final) et doute écrit. Un paramètre `temperature_final` sur l'étape aurait rempli la case à tort.
- Durée « three minutes » : sans chiffre dans la phrase de méthode, donc `value_text`. De même « ten minutes » pour la centrifugation (vitesse 10 000 rpm en `value_num` 10000 : forme « 10 000 » acceptée par le contrôle).
- Pureté « analytical grade » : phrase générale en fin de section Materials, valable pour tous les réactifs. Pour la citer avec la phrase d'achat chez Aladdin dans un seul `supplier_quote`, j'ai pris le passage contigu de « MA, urea… » à « …without further purification » (le contrôle exige une sous-chaîne continue).
- Lyophilisation : action `dry` pour que la grille impose température et durée, déclarées non citées (aucune valeur dans l'article).
- Dialyse : seule la coupure 1000 Da et 24 h sont données ; milieu, volume, renouvellements en `not_stated`.
- Rendement 58,5 % : base (masse totale des précurseurs ou carbone) non précisée, `yield_basis` en `not_stated`.
- QY : ordre « respectively » 0,01 / 0,1 / 1 mg mL−1 ↔ 23,02 / 38,88 / 10,36 %, confirmé par « 0.1 mg mL−1 was the optimal concentration ».
- Figures : Fig. 5 lue (F0–F de Cr(VI), Ag+, Cu2+, Fe3+, 2 chiffres significatifs, `from_figure`) ; Fig. 2 ouverte, rien de plus que le texte. Autres figures (3, 4, 6, 7, 8) : courbes ou images dont les valeurs clés sont déjà écrites dans le texte, non lues.
- Annexe : le fichier SI ne contient que les légendes des Fig. S1–S4 (pas les données) ; annotation « Annexe absente du dépôt » écrite.
- Contradiction notée : « 0,1 g mL−1 » (Multicolor bioimaging) contre 0,1 mg mL−1 en légende de la Fig. 8 ; aucune valeur extraite, doute écrit.
- `method_sources` vide : aucun renvoi bibliographique de méthode dans les sections Experimental (les renvois sont dans l'introduction et le tableau de comparaison).
