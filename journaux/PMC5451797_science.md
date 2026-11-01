# PMC5451797 — critique scientifique (journal de décisions)

- Durée des 3500 cycles recalculée : 12 V parcourus par cycle à 0,5 V/s → 24 s, soit ≈ 23,3 h ; donnée absente de l'article, mise en `calculs` pour que la correction puisse la signaler comme annotation (pas comme valeur extraite).
- Frange 0,223 nm « graphite (101) » : avec a = 2,464 Å et c = 6,711 Å, d(101) = 0,203 nm et d(100) = 0,213 nm ; 0,223 nm tombe entre rutile (200) 0,230 et (111) 0,219 nm → `probleme`. Paramètres de maille pris de mémoire (valeurs de manuel), signalés comme à confirmer sur la COD ; la conclusion tient même à ±1 %.
- 0,325 nm (rutile 110) et 0,323 nm (graphite 002 des CQDs) sont indiscernables : le HRTEM ne prouve pas la présence des CQDs sur les fils ; dit dans le même constat.
- Témoin manquant (polarisation à −3 V sans CQDs) classé `probleme` : deux sources indépendantes montrent qu'une forte polarisation cathodique réduit le FTO en Sn (Sanz-Navarro 2023, Sn à −2,0 V) et augmente le photocourant (Xie et al. 2015, notice INIS seulement, journal et DOI non relevés).
- Contradiction figure 2 / figure S4 (CQDs générateurs puis piégeurs de •OH) classée `probleme` sur CQD_solution : c'est une incohérence interne de l'article, pas une question de littérature ; « peroxydase » jugé impropre (au mieux catalase-like, et non mesuré).
- DMPO comme sonde de 1O2 : `reserve` seulement (interprétation), source Ueda et al. 2003 (Photochem. Photobiol.) ; TEMP cité comme piège spécifique d'après des extraits de recherche, sans source enregistrée.
- « Première fois » contredit par Ming et al. 2012 (Dalton Trans., 10.1039/c2dt30985h, électrolyse de graphite dans l'eau pure) ; laissé en `reserve` car cela ne change pas la faisabilité, au contraire cela la soutient.
- Fuite de KCl de la référence Ag/AgCl dans l'eau à 18 MΩ·cm : hypothèse de chimie générale, non sourcée ; l'article indique lui-même une référence en KCl 3 M pour la mesure du photocourant.
- Recette TiO2 : seule une annexe anonyme (DocsLib) donne une recette presque identique (6 ml 2-butanone, 6 ml HCl, 0,5 ml TBT, 200 °C, 40 min) ; gardée en source secondaire, signalée dans `sources_not_found` faute d'auteurs et de DOI.
- Comparaison avec Liu et Aydil 2009 : HCl/Ti ≈ 41 ici contre ≈ 122 chez eux ; écart noté sans en faire un problème (milieu toujours très acide).
- TiCl4 0,5 M jugé élevé (bains de post-traitement usuels ≈ 0,04 M) sans source cherchée : `reserve` en chimie générale.
- Masses volumiques (TBT 1,00 ; HCl 37 % 1,18 g/ml) et pression de vapeur de l'eau à 200 °C (≈ 15,5 bar) prises de mémoire, signalées comme non revérifiées ; recherche NIST sur la 2-butanone sans valeur exploitable dans l'extrait.
- Revue « CQDs as ROS-generator and -scavenger » (Dyes Pigm. 2022) trouvée sans auteurs ni DOI : non citée.
- Comparaison base : seule PMC7153708 (nanofils de TiO2 sur FTO, 0,4 mA/cm2) est comparable ; conditions de mesure différentes, donc `reserve`.
- 8 recherches web au total ; Crossref non utilisé (bloqué) ; rien ajouté à fondateurs.md ni constantes.md.
