# PMC5515720 — critique scientifique (journal)

- Bilan de matière recompté : 9 mL TEOS × 0,933 g/mL / 208,33 = 40,3 mmol → 2,42 g SiO2 ; 1,9 g × 9 % = 0,171 g MWNT → Si:MWNT 6,62:1, identique à l'article. Pas de problème de stœchiométrie.
- Composition 77,5:17:5,5 recalculée : avec 2,42 g de SiO2, le carbone de revêtement vaut ≈ 0,53 g (23 % du C organique apporté), plausible. Les 5,5 % de MWNT tombent exactement sur la valeur de recette (5,47 %) → noté `reserve` : la TG/DTG ne sépare pas C amorphe et MWNT de façon quantitative, la valeur est sans doute calculée.
- `probleme` n°1 : TG « under N2 flow » (Méthodes) contre « oxidization of carbon and MWNT » (Résultats). Un produit pyrolysé à 1100 °C sous Ar ne perd pas son carbone sous N2 entre 550 et 730 °C ; la teneur en SiO2 n'est valable que sous air. Source de méthode : ISO/TS 11308:2020 (page ISO vue dans les résultats de recherche, non ouverte).
- `probleme` n°2 : 475 mAh g−1 à 1000 mA g−1 (résumé) contre 215–220 (texte, Fig. 8 et 10). Rangé sur la voie Cell_SiO2C_Li, là où sont les mesures électrochimiques.
- HRTEM : calcul d = a/√(h²+k²+l²) avec a = 7,13 Å → 4,12 / 2,15 / 2,06 Å = β-cristobalite cubique, que les auteurs ne nomment pas. Les deux petites distances coïncident aussi avec graphite (100) 2,13 Å et (101) 2,03 Å : attribution non discriminante. Laissé en `reserve` (caractérisation, pas synthèse) ; source AIST (structure β-cristobalite, a = 7,126 Å à 300 °C) prise dans l'extrait de recherche.
- DRX 26,1° : Bragg → 3,41 Å = (002) graphite, l'article écrit (200). Erreur d'indexation, `reserve`.
- Raman : explication de ID/IG par des « défauts Si–O » jugée non physique (D et G sont des modes du carbone, Ferrari & Robertson, déjà dans fondateurs.md).
- Mécanisme jugé `a_revoir` : l'hypothèse Pechini de l'extraction place la polyestérification au séchage à 55 °C ; je la place pendant la montée en température (>100 °C), en concurrence avec l'évaporation de l'EG. Pas de source primaire trouvée pour la température de polyestérification (page SINTEF inaccessible, DNS bloqué) ; appui sur Danks 2016 et le brevet Pechini (fondateurs.md), dit dans `sources_not_found`.
- Réduction carbothermique à 1100 °C écartée en chimie générale (seuil ≈ 1500 °C sous P(CO) 1 bar) ; les résultats de recherche donnaient 1400–1700 °C en pratique mais sans titre exploitable, donc non cités.
- Revue Frontiers in Materials (10.3389/fmats.2020.628233) citée pour Li2O/Li4SiO4 irréversibles et Li2Si2O5 réversible : page inaccessible (DNS), auteurs non relevés, DOI non vérifié.
- Voie Cell_SiO2C_Li : verdict `invérifiable` (électrolyte, séparateur, base de normalisation des capacités absents), faisabilité `reproductible_avec_reserves`.
- Témoin SiO2@C : change surtout la présence de MWNT (et 1,7 g d'eau) ; composition non mesurée (≈ 82 % SiO2 attendus) mais écart trop faible pour expliquer les facteurs 1,4–2,2 de capacité → `reserve` seulement.
- compare.py : aucune autre synthèse SiO2@C ou MWNT dans la base.
- Recherches web : 8 recherches + 2 lectures de page échouées (DNS) ; rien ajouté à fondateurs.md ni constantes.md (consigne).
