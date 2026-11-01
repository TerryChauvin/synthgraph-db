# PMC10368083 — critique scientifique (journal de décisions)

- Bilan de la fonctionnalisation : UiO-66-NH2 idéal = 1754 g/mol, donc 3,42 mmol NH2/g et 1,71 mmol NH2 dans 0,5 g. Avec 2,00 mmol de HCHO et d'H3PO3, on n'a que 1,17 équivalent par NH2 au lieu de 2 pour N(CH2PO3H2)2 : jugé `probleme` (formule inatteignable). Pas d'erreur de l'extracteur : 0,06 g et 0,164 g font bien 2 mmol chacun.
- Défauts du réseau : un UiO-66-NH2 modulé à l'acide acétique a moins de 6 ligands par cluster, donc un peu moins de NH2 ; la conclusion ne change pas (même avec 5 ligands il faudrait 2,85 mmol).
- Greffage covalent non démontré (`probleme`) : je m'appuie sur la phrase des auteurs « presence of phosphorus acid peaks » dans la DRX du catalyseur (fig. 6 vue : raies supplémentaires et bosse amorphe vers 15–25°) et sur l'absence de test de filtration à chaud, alors que H3PO3 libre (5 mol %) donne 70 %. Alternative retenue : H3PO3 adsorbé ou coordiné aux Zr.
- Stabilité : 1,17 P par Zr. Source Bůžek 2021 (les phosphates dégradent UiO-66), mise en `reserve` seulement : leurs essais portent sur des tampons phosphate aqueux et non sur H3PO3 dans l'éthanol.
- XPS P 2p : écart de 2,1 eV entre « 2p3/2 » et « 2p1/2 » contre 0,86–0,87 eV (Thermo Fisher, HarwellXPS) ; rapport d'aires de la fig. 9c loin de 2:1. Jugé `probleme` (erreur de physique, pas d'interprétation). Zr 3d (2,4 eV) contrôlé et correct.
- XPS N 1s 399,6 eV « N–C–P » : même position que l'amine libre de UiO-66-NH2 (Wang 2022, N–H à 399,04 eV) ; `reserve` car non discriminant mais pas faux.
- C 1s : ordre C–N sous C=C inhabituel, calibration probablement décalée de ~1 eV ; `reserve`, je n'ai pas cherché de source (contrôle de manuel).
- p-TSA : 0,017 g = 4,5–4,9 mol % de 2 mmol, pas 10 mol % ; `reserve` (une des deux valeurs est fausse, impossible de dire laquelle).
- Formaldéhyde : 0,06 g = 2 mmol seulement si paraformaldéhyde (liste des produits) ; avec du formol à 37 % ce serait 0,74 mmol. Mis en `reserve`, pas en problème.
- Données des produits (A7 copiée de A6, B6 à 8 pics 13C dont 79,1 et 70,4 ppm) : jugé `probleme` dans la voie du catalyseur, car l'étendue annoncée en dépend ; l'extracteur l'avait déjà signalé en doute.
- Mécanisme catalytique (H2 ou H2O2 libéré) : H2O2 impossible sous argon ; Evdokimov 2006 (Org. Lett.) montre l'oxydation des 1,4-DHP par l'adduit de Knoevenagel, alternative retenue en `reserve`. Le commentaire de Salehzadeh (RSC Adv. 2017) sur l'« oxydation anomérique » a été vu seulement dans une liste de références : non cité, faute de vérification.
- Moedritzer–Irani : DOI 10.1021/jo01343a067 pris dans deux sources secondaires concordantes (Wikipedia ATMP, brevet US 7 662 991) ; les conditions classiques (HCl concentré, 2–3 mol par mole d'amine) viennent du brevet.
- Rendement plus faible au reflux qu'à 25 °C : hypothèse de perte de NH3 (décomposition de NH4OAc), donnée comme plausible et non vérifiée.
- 9 appels web (8 recherches et 1 lecture de PubMed). DOI non vérifiés sur Crossref (bloqué) : 10.1021/jo01343a067, 10.1039/D0QI00973C, 10.1021/cm102601v, 10.3389/fchem.2022.962383, 10.1021/ol052994+. Rien n'a été ajouté à fondateurs.md ni à constantes.md.
