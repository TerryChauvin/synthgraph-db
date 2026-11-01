# PMC9080687 — critique scientifique

- Problème « IPCE/Jsc » (Cl_normal_65C_4.5h) : IPCE max 17 % contre Jsc 16,1 mA cm−2 ; avec le rapport Jsc/IPCE_max de la cellule à l'urée (20,9/0,77 = 27,1), le témoin ne peut dépasser ≈ 4,6 mA cm−2. Argument interne retenu faute d'avoir lu la table de Rühle 2016 (Jsc de Shockley–Queisser).
- Verdict « incoherente » réservé à cette branche : c'est la seule contradiction chiffrée impossible physiquement ; les autres écarts (25/30 wt%, Ag/Al, 70/75 °C, 10/20 min) sont des contradictions de rédaction, mises en réserve.
- Problème « surface active » (I_normal_100C_10min) : 0,01 cm2 et 10 mm2 (= 0,1 cm2) dans le même paragraphe du SI ; classé problème car Jsc et PCE en dépendent directement.
- Problème « rapport MAI:PbCl2 absent » : le 3:1 usuel (Dualeh 2014) est supposé pour les calculs de concentration (≈ 0,42 M de Pb à 25 wt%, ≈ 0,54 M à 30 wt%) ; c'est une hypothèse, notée comme telle.
- Problème « unité de l'additif » posé deux fois (Cl_urea1_65C_4.5h et I_urea1_85C_10min) : trois lectures calculées (vol% de la solution à 25 wt%, wt% des solides, mol%) donnent 1 à 10 mol% d'urée par Pb. La lecture vol% (≈ 3,5 mol% pour MAPbI3) est la plus proche des 4 mol% de Lee et al. 2017, mais rien dans l'article ne la confirme.
- Cl_urea1_90C : brunissement en 10 s contre 2,5 h sans additif (facteur ≈ 900) ; mécanisme « a_revoir » plutôt que « probleme », car l'observation est visuelle et l'article ne prétend pas à une conversion complète en 10 s.
- I_thiourea0.5_65C_20min : grains de 895 nm mais PCE 8,8 % ; mis en réserve comme contradiction de l'interprétation des auteurs (taille de grains « key factor »), pas comme erreur de donnée.
- « 10−7 Pa » : converti en 10−9 mbar ; jugé confusion d'unité probable (réserve), pas impossible en soi.
- TRPL : durées de 2 à 44 ns contre 200–750 ns chez Lee et al. 2017 ; le substrat de mesure n'est pas dit, donc réserve et non problème.
- Sources : Lee et al. Chem 2017 (urée, 4 mol%), Dualeh et al. AFM 2014 (MAI/PbCl2 1:3, recuit), Jeon et al. Nat. Mater. 2014 (antisolvant, adduit DMSO) trouvées par recherche ; DOI non vérifiés sur Crossref (bloqué). Account ACS 10.1021/acs.accounts.5b00440 : titre et DOI vus sur une page de reprise, auteurs non confirmés, signalé dans la source.
- Écartées : article PCCP 2016 (10.1039/C6CP06347K) sur la sublimation du MACl, titre et auteurs non obtenus (pubs.rsc.org et PMC injoignables par WebFetch).
- Températures de fusion de l'urée (133 °C) et de la thiourée (≈ 176–178 °C) données de mémoire (PubChem) sans lecture de la page : à confirmer si un constat en dépend (aucun problème n'en dépend).
- Rien ajouté à fondateurs.md ni à constantes.md (consigne : Crossref bloqué).
