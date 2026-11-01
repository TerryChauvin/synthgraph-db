# PMC13057244 — critique scientifique (journal de décisions)

- Recalcul du Tableau 1 : Li/TM = 0,928 exact, mais Li = 6,210 ± 0,966 % donne Li/TM entre 0,78 et 1,07. Le déficit de 7,2 % n'est pas significatif : classé `probleme` (c'est la base de tout le plan factoriel).
- Même tableau : Ni:Mn:Co = 0,65:0,20:0,15 ; Co mesuré 8,38 % contre 12,16 % attendu pour 622, écart > 3 incertitudes. `probleme` (formule visée non démontrée). La chimie 622 des cellules LG de la Kona n'est confirmée que par une source secondaire (Electric Revs 2018).
- Somme des métaux 62,1 % contre 66,8 % attendus pour l'oxyde : ~7 % de la poudre « high purity » n'est pas de l'oxyde (liant, carbone, Al). Gardé en calcul, pas en constat séparé.
- Constat central tiré du Tableau 2 seul (pas besoin du seuil de 1,2) : I003/I104 passe de 2,05 (usagé) à 1,18/0,82/1,29 après régénération, contre 2,09 pour le commercial. La régénération augmente le mélange cationique selon le descripteur des auteurs : `probleme`. Ohzuku 1993 cité comme origine du descripteur, DOI non trouvé ; le seuil de 1,2 n'a pas été confirmé en recherche, donc non utilisé.
- Capacité nulle de la poudre usagée incompatible avec 93 % de Li et I003/I104 = 2,05 : la cause est ailleurs (surface, résidus). D'où le `probleme` « pas de témoin recuit seul » sur M1 (contrôle 5).
- « reduction of the OH- ions » : c'est une oxydation (4 OH− → O2 + 2 H2O + 4 e−). `probleme` de vocabulaire (contrôle 4) ; l'annotation mecanisme_analyse de l'extraction est juste.
- Tableau S1 contre texte (M1/M2 1 h/2 h inversés) : repris en `probleme` car l'optimum annoncé en dépend ; déjà signalé par l'extracteur.
- M8 : choisi « highest lithium composition » puis dit « Li deficient » ; et la poudre usagée (déficitaire) a le plus petit volume. Explication du volume de M8 non soutenue : `probleme`.
- Volume de M2 : 100,31 Å3 recalculé contre 100,81 annoncé (a nécessaire 2,867, arrondi 2,87) : `reserve`, une des trois valeurs est fausse. M1 et commercial compatibles à l'arrondi.
- Diffusivité : avec l'aire géométrique (1,131 cm2) et CLi = 0,0485 mol/cm3 (masse volumique 4,7 g/cm3, valeur usuelle non sourcée), D ≈ 9e-16 cm2/s contre 4,8e-12 : non recalculable, A et CLi absents. M2 cohérent avec σ (3,5e-13), M8 décalé d'un facteur ~2. `reserve`.
- Chute ohmique M2 : 0,63 mA × 1600 Ω ≈ 1 V à 1 C → capacité nulle cohérente (lecture Rct sur figure). Classé `ok`.
- Boîte à gants « 0,01 mg/L » ≈ 7,6 ppm O2 et 13,6 ppm H2O si littéral : `reserve`.
- Échange Li+/H+ au lavage et au délaminage aqueux (Oswald et al. 2024, titre et DOI confirmés en recherche) proposé comme mécanisme alternatif à la « surface reconstruction » pour M2.
- Sécurité ajoutée : LiOH + Al résiduel → H2 dans le réacteur fermé avec l'O2 dégagé (CAMEO, lithium hydroxide solution).
- Shi et al. 2018 (ACS Energy Lett.) : référence confirmée par une revue citante, mais pages de l'éditeur et OSTI injoignables ; DOI 10.1021/acsenergylett.8b00833 donné de mémoire, non vérifié. Seul le schéma « hydrothermal LiOH + recuit court sur NCM111/523 » lui est attribué.
- NIST WebBook injoignable (DNS) : pressions de vapeur 0,618 et 2,320 MPa prises sur une table IAPWS secondaire (Pressbooks). Solubilité de LiOH prise sur Wikipedia (secondaire, renvoie à PubChem CID 3939).
- 9 recherches web, 3 lectures de page (toutes en échec DNS). Rien ajouté à fondateurs.md ni à constantes.md (consigne : Crossref bloqué).
