# PMC8401075 — critique scientifique (journal de décisions)

- DRX (Fig. 6 ouverte) : pic fort à ~32,2°, pic faible à ~66,5–67° (pas 64,4° comme dans le texte), aucun pic à 38,1°. Rapport des d ≈ 1,98 = paire (200)/(400) d'un réseau NaCl, pas Ag(111)/(220) (1,633). Classé `probleme` : la phase métallique n'est pas démontrée par la DRX.
- AgCl préféré à Ag2O : Ag2O donnerait (111) à 32,8° et (222) à 68,9°, ainsi que (200) à 38,1° ; AgCl (32,24/67,46°) colle mieux, et l'EDX montre Cl. NaCl (31,70/66,23°) reste possible (Na et K en EDX, goutte séchée sur verre) : les deux sont cités, sans trancher.
- Calcul AgCl/Ag : la teneur en Cl du fruit est une hypothèse (0,2 % sur matière sèche), signalée comme telle dans `calculs` et dans `sources_not_found` ; le point solide est le seuil Ksp (≈ 0,2 µM).
- Cinétique : A(1 h)/A(4 h) = 0,44 (Fig. 2a) → `probleme` de cohérence entre Méthodes et Résultats ; l'échantillon à 1 jour (A 1,47 > 1,40) montre que la stabilité porte sur le mélange non lavé.
- Absorbance plasmon : ε de Paramelle 2014 (tableau 1 lu : 20 nm → 4,18 × 10^9 ; 10 nm → 5,56 × 10^8) → A attendue ≈ 15–16 pour 0,9 mM : dilution non écrite ou conversion ≈ 9 %. Laissé en `reserve` (la dilution peut simplement manquer).
- 4-NP : 25 mM dans le mélange → A ≈ 450 contre 1,1 sur la Fig. 14a (≈ 62 µM). Probable erreur d'unité (0,05 mM ?), non affirmée. ε = 18 000 M−1 cm−1 pris dans une citation secondaire (Das 2012) ; la recherche d'une source primaire (NBS 1967) n'a rien donné d'utilisable.
- Fig. 14d contre 14e (figure ouverte) : à 1 et 3 min (1 mL), 14d donne −ln 0,01 et 0,26 et 14e 0,12 et 0,43 ; à 5 min (2 mL), 3,9 (14d), 2,8 (14c), 3,0 (14e). Période d'induction de 2–3 min dans 14b/14d effacée par l'ajustement passant par l'origine → `probleme`. Gu et al. 2014 (cité dans PMC9316932, DOI relevé) sert de source pour l'analyse cinétique et l'induction.
- Stokes : la paire (249,05 nm ; 8884,15 cm−1) se résout exactement en 419,4 → 668,4 nm : la bande d'émission à ~668 nm de la Fig. 8b, et non celle à 470 nm. Les coordonnées CIE (0,21 ; 0,54) sont vertes ; la Fig. 8d place le point vers (0,16 ; 0,22). `probleme` (PL), avec Brouwer 2011 (fondateurs) pour l'absorbance à l'excitation.
- Rendement quantique recalculé : 0,056 %, l'arithmétique des auteurs est juste ; seul le mot « moderate » et le choix 330/360 nm posent problème.
- IC50 recalculée par interpolation (≈ 61 µg/mL) : cohérente, rien à signaler, sinon la dose de 1 mg/mL contre l'IC50 dans les essais qualitatifs.
- IR : les bandes 2078/2088 (eau) et 1382 cm−1 (nitrate) sont réattribuées par chimie générale, sans recherche web ; laissé en `reserve`.
- « 60 °C … boil » : `reserve` et non `probleme`, car le doute porte sur la consigne de plaque et ne rend pas la voie impossible.
- Comparaison avec la base : `compare.py silver` → PMC3998862 (Ag(111) à 38,52°), PMC10493855 (d111 2,39 Å), PMC4043712 (plateau à 4,5 h).
- Recherches web : 4 recherches et 2 lectures de page. L'article Trametes (PMC4237688) est cité par son URL PMC (DOI non relevé). Rien n'a été ajouté à fondateurs.md ni à constantes.md (Crossref est bloqué).
