# PMC9099495 — critique scientifique (Opus)

- Rapport TiCl4/alcool : 5 mL × 1,726 / 189,68 = 45,5 mmol ; 50 mL × 0,789 / 46,07 = 856 mmol, soit 1/18,8 contre 1/10 dans le résumé. Le 1/10 est le rapport des volumes 5/50. Classé `probleme`, parce que pour TiPr400 on ne sait pas lequel suivre (50 mL donnent 1/14,7 ; 1/10 demande 34 mL).
- « Ti(OEt)4 » des Méthodes : classé `probleme` (mécanisme). Sans base, l'alcoolyse reste partielle, et Ti(OEt)4 pur est un liquide, donc pas le « solide TiEt ». Sources : Wikipedia (préparation avec Et3N, Téb 150–152 °C sous 10 mmHg ; source secondaire) et l'extrait du brevet US 4 789 752 (Ti:Cl ≈ 1:2,1 sans base). Je n'ai pas trouvé de source primaire de Bradley lisible : c'est noté dans `sources_not_found`.
- Le brevet n'a été lu que par l'extrait du moteur de recherche (fetch du PDF USPTO tombé en délai dépassé). Statut `reserve`, en appui seulement.
- TiPr400, mécanisme : `probleme`. L'ATG des auteurs (35 % pour TiPr contre 50 % pour TiEt) contredit leur explication, selon laquelle une chaîne plus longue dégagerait plus de gaz. Une perte de 35 % est proche de Ti(OH)4 → TiO2 (31,1 %) : TiPr était déjà hydrolysé et en partie cristallisé.
- Eau d'hydrolyse : avec 0,2 % d'eau supposée dans l'éthanol absolu (teneur non donnée par l'article, hypothèse dite dans `calculs`), h ≈ 0,1. L'humidité de l'air est donc la vraie source d'eau ; `reserve` et point à vérifier.
- P25 : k initial ≈ 0,022 min−1 (20 % en 10 min) contre k ajusté de 0,0024 min−1. Classé `probleme`, car la supériorité sur P25 dépend de la fenêtre d'ajustement. La source retenue est PMC6780102 (Nanomaterials 2019) : P25 y est le plus actif sous UV et le paracétamol y suit un ordre zéro. Je cite Yang, Yu, Ray 2008 (Water Res.) sans l'utiliser : ce papier n'a été vu que dans des listes de références, pas lu.
- Hypothèse « intermédiaires aromatiques absorbant près de 243 nm » : laissée qualitative, sans longueur d'onde chiffrée, car aucune source n'a été lue.
- Fig. 7 (C/C0/SBET) : la normalisation est fausse dans son principe, mais k/(m·S) donne 6,2 et 6,7·10−5 min−1 m−2 pour TiEt400 et TiPr400. La conclusion entre ces deux solides tient donc : `reserve` et non `probleme`.
- Bande IR « centrée sur 400 cm−1 » avec une plage de 4000–450 cm−1 : `probleme` mineur (contrôle 7 de PLAUSIBILITE), sans conséquence sur la synthèse.
- 4V/S : 12,8 et 15,3 nm contre 10,2 et 10,3 nm dans la Table 1, mais 7,8 contre 7,7 nm pour P25. La méthode du logiciel n'est donc pas 4V/S(BET) ; probablement BJH, non dit. `reserve`.
- Bragg avec 1,5418 Å : les 11 distances recalculées concordent à ±0,01 Å. Aucune critique.
- Thermochimie : NIST WebBook donne ΔrH° = −205 kJ/mol pour l'alcoolyse complète (HCl dissous, Bradley et Hillyer 1966). Je l'utilise comme ordre de grandeur de l'exotherme, pas comme valeur exacte de la réaction partielle.
- Référence Zhu et al. 2000 (DOI 10.1023/A:1004882120249, pris dans les références de l'article) : introuvable par la recherche web et non vérifiable (Crossref bloqué). Le protocole d'origine n'a donc pas été comparé.
- Verdicts : TiEt400 `coherente` (procédé connu, produit plausible), TiPr400 `douteuse` (aucune quantité donnée, et explication contredite par les données).
- Le WebFetch natif échoue (DNS) ; Parallel_Search a servi aux lectures. Rien n'a été ajouté à fondateurs.md ni à constantes.md (consigne : Crossref bloqué).
