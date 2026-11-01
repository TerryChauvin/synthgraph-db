# PMC9136838 — critique scientifique (journal de décisions)

- Stœchiométrie : La:B = 1,000 (LaMnO3, LaCoO3) et 1:0,501:0,500 (LaMn0.5Ni0.5O3) seulement si LaCl3, CoCl2 et NiCl2 sont anhydres. Avec LaCl3·H2O, La:Mn = 0,93 ; avec LaCl3·7H2O, 0,66. Les masses publiées impliquent donc des sels anhydres : réserve sur l'hygroscopie, pas de problème.
- « Gram scale » classé `probleme` : 87 g de DES + 0,95 g de sels donnent au plus 0,706 g de LaMnO3, à 0,056 g par creuset de 7 g (12,6 creusets). Pour LaCoO3 : 0,615 g ; pour LaMn0,5Ni0,5O3 : 0,533 g. Aucun lot n'atteint le gramme.
- Masses de ChCl et d'acide malonique recalculées pour le rapport 1:1 (87 g → 49,85 + 37,15 g) : elles sont mises dans `calculs`, pas dans les données, pour aider un chimiste qui refait la synthèse.
- « NH3(g) » corrigé en réserve de vocabulaire : la choline n'a pas de N–H ; les produits connus sont la triméthylamine, CH3Cl et le DMAE (brevet US 8 177 962, arXiv 2410.05498). Je n'ai pas classé ce point en `probleme`, car il ne change pas la synthèse, seulement la sécurité.
- Moussage : 0,0284 mol d'acide malonique par creuset → ≈ 1,2 L de CO2 à 230 °C. Calcul fait sur le seul premier CO2 de la décarboxylation, densité du DES supposée ≈ 1,2 (non vérifiée).
- Lacunes de LaCoO3 en `probleme` (deux constats) : (a) V = 335,97 Å3, soit 0,14 % sous une référence (SI Chem. Commun. c8cc09573f, V = 336,44 Å3), donc pas de dilatation globale ; (b) 8,5 h à 900 °C sous air après la combustion de l'organique effacent un état réduit. Valeur de δ à 900 °C sous air non trouvée : argument qualitatif, dit comme tel.
- BM_LaCoO3 en `probleme` : la Fig. 3 est prise « after ball milling » et aucun LaCoO3 non broyé n'est imagé. Le témoin LaMnO3 ne suffit pas (Mn moins réductible). Création de lacunes par le faisceau (Jang 2017, ACS Nano) citée en réserve d'après la fiche ORNL, texte non lu.
- LaMnO3 rhomboédrique R-3c = LaMnO3+δ suroxydé (arXiv 0704.1402 : orthorhombique si δ < 0,1). Réserve, car les auteurs expliquent le volume par le seul Mn3+.
- « Assisted metathesis » : Todd et al. utilisent Li2CO3 → LiCl comme puits ; ici il n'y a pas d'alcalin. Réserve de vocabulaire et de preuve (« conclusively prove »).
- Mn3O4 à 400 °C (Fig. S4) jugé `ok` : il appuie un milieu localement réducteur. Le seuil Mn2O3 → Mn3O4 sous air (≈ 900 °C) vient de mes connaissances générales, sans source lue.
- EIS de IrO2 en `probleme` : 0,985 + 1,860 + 2,820 = 5,67 Ω contre ≈ 4,4 Ω lus sur la Fig. 2c (image du dépôt). Les pérovskites concordent à ±0,25 Ω. R1 = 1,86 Ω pour un oxyde métallique est incohérent ; je suggère une coquille (0,186), sans l'affirmer.
- Témoin IrO2 en `probleme` : 0 cycle d'activation contre 700, et l'activation agit aussi sur la mousse de Ni.
- Doute de l'extracteur sur la stabilité à 100 mA/cm2 : la Fig. 2d montre bien les deux courbes, le texte principal est confirmé et les Méthodes sont incomplètes.
- Godet en WC : contamination Co/W possible, à cause du liant Co courant dans les carbures frittés. Connaissance générale, non sourcée ; réserve seulement.
- Web : 10 recherches. WebFetch et curl bloqués (DNS, proxy 403) : aucun texte intégral lu, tout repose sur les extraits de recherche. Rien n'a été ajouté à fondateurs.md ni à constantes.md (Crossref bloqué).
- DOI non vérifiés : 10.1016/j.molliq.2018.03.076 (lu dans un résultat de recherche), 10.1021/je060038c (lu dans un résultat de recherche), Abbott 2004 (point de fusion du DES à 10 °C) non cité dans le JSON faute de vérification.
