# PMC9418622 — critique scientifique (journal de décisions)

- Voies jugées : les trois voies de base (MAPbBr3-1L, MAPbBrI_x0.9, White_2759K) et deux branches qui changent la chimie : MAPbI3 (autres précurseurs) et MAPbBr3-6L (4 éq. d'octylamine par Pb, phase possiblement différente). Les autres branches sont traitées dans les constats des voies de base.
- Probleme 1 (MAPbI3) : 755 nm = 1,642 eV contre gap publié 1,51 eV, et 1,51 eV < gap du massif (1,57 eV, Noh 2013) pour des cristaux de 19,9 nm. Émission au-dessus du bord d'absorption = gap de Tauc erroné.
- Probleme 2 (MAPbBrI_x0.9) : même calcul E = 1239,84/λ ; x = 0,9 et 0,8 donnent une émission 0,09 et 0,13 eV au-dessus du gap du tableau 2. Classé `probleme` (pas `reserve`) car l'écart dépasse largement l'incertitude de lecture.
- 1L : écart de 24 meV dans le même sens, laissé en `reserve` (dans l'incertitude d'un gap pris au pic d'absorption).
- Composition réelle : Vegard entre 5,930 et 6,304 Å donne x_eff ≈ x + 0,1 pour toute la série, et la formule de Noh donne des gaps attendus 0,07–0,18 eV plus bas que publiés. Deux indices indépendants dans le même sens → `reserve` « plus riche en Br que nominal ». J'ai vérifié que les solutions mères ont presque la même concentration (I/Br = 1,06 à volume égal), donc l'écart ne vient pas d'un mélange en volume.
- Phases lamellaires pour les forts taux de ligand : hypothèse préférée au « confinement de nanocristaux cubiques » des auteurs pour 6L (408 nm, sans MET) ; classée `reserve` et non `probleme` faute de valeurs chiffrées n → λ lues dans Sichert 2015 (seul le résumé a été obtenu). Les épaisseurs 1,73–2,34 nm valent 3–4 couches d'octaèdres (a = 0,593 nm).
- Probleme 3 (White_2759K) : le résumé parle de « blending … nanocrystals », les Méthodes d'une combinaison numérique de spectres. Un mélange réel subirait l'échange d'anions Br/I entre nanocristaux (Nedelcu 2015, de fondateurs.md) et la réabsorption : l'IRC de 93,95 n'est pas une propriété démontrée.
- IRC plausible en simulation : Ohno 2005 (NIST, DOI 10.1117/1.2130694) trouvé par recherche web ; Ra ≈ 90 dès trois bandes. Laissé en `reserve` (IRC indulgent pour les raies étroites).
- CCT recalculées par McCamy à partir des (x, y) arrondis : 2–4 % d'écart, cohérent. Formule utilisée de mémoire (signalé dans sources_not_found).
- Rapport 9 mL de DMF/GBL pour 5 mL de toluène (36 % d'antisolvant) : inverse de la LARP de Zhang 2015 ; `reserve`, avec la formulation fautive « 8.5 of mL ».
- Excès MA/Pb = 1,64 (Br) et 1,51 (I) : non expliqué ; `reserve`.
- Bragg vérifié : (100) 14,93°, (200) 30,12° pour a = 5,930 Å ; (004)/(220) de MAPbI3 → a = 8,88 Å, c = 12,67 Å, pseudo-cubique 6,30 Å = 6,304 du tableau 2.
- Recherches web : 7 recherches + 2 lectures de page. Sources trouvées hors fondateurs.md : Noh 2013, Hoke 2015, Sichert 2015, Zhang 2015, Ohno 2005, PMC11477630. Rien ajouté à fondateurs.md ni constantes.md (Crossref bloqué, consigne de l'orchestrateur).
- Densité de l'octylamine (0,782 g/mL) prise de mémoire (fiche fournisseur), non revérifiée : n'influe que sur les rapports octylamine/Pb.
