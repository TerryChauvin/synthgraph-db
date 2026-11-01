# PMC11736836 — critique scientifique (journal de décisions)

- **Eau du sol (probleme, TiO2_sol)** : 0,49 mol HNO3 à 65 % m/m apportent 0,49 × (63,01/0,65 − 63,01)/18,015 = 0,92 mol H2O par Ti, plus que le 0,82 déclaré. Le 0,82 ne peut donc pas être l'eau totale ; seule lecture possible : eau ultrapure ajoutée, d'où h réel ≈ 1,74 (≤ 1,9 avec 0,2 % d'eau dans l'éthanol). Classé `probleme` (paramètre clé du sol, doublé, non dit par l'article) plutôt que `reserve`.
- **Mécanisme de l'extraction mis à `a_revoir`** : « l'acide ralentit l'hydrolyse » est inexact pour Ti (hydrolyse très rapide ; l'acide freine la condensation par protonation des Ti–OH et répulsion des oligomères chargés) et h = 0,82 est à remplacer par ≈ 1,7. Source : Livage, Henry, Sanchez 1988.
- **Porosités Lorentz–Lorenz** recalculées exactement avec n_bulk = 2,400 (16,7 ; 15,8 ; 9,9 ; 11,8 ; 10,3 %). Avec l'indice de films d'anatase à 633 nm (2,48–2,49, Möls et al. 2019, pris à 2,485) : 19,2 ; 18,4 ; 12,7 ; 14,6 ; 13,1 %. Mis en `reserve` : valeurs absolues conventionnelles, comparaisons internes valables. Source de 2,400 introuvable dans l'article (noté dans sources_not_found).
- **Phase des films** : la poudre comme témoin change plusieurs variables (contrôle 5) ; la hausse de la température de cristallisation des films très minces ne s'appuie que sur une thèse (Unisa 2021, auteur non relevé), source secondaire faible : `reserve` seulement.
- **XPS O 1s 531,3 eV « lacunes »** : `reserve` avec Idriss 2021 (Surface Science 712, 121894, DOI vérifié via ADS/OpenAlex, pas Crossref).
- **O/Ti avant décapage** : 2,07 inclut l'oxygène lié aux 17,8 % at de carbone de contamination ; seul le 1,98 après décapage est probant.
- **Incohérence texte/tableau** : EP sur Si = 52 nm dans le texte, 50 nm au tableau 3 (déjà noté en doute par l'extracteur) ; gardé en `reserve` mineure.
- **DLS** : PDI 0,098 → FWHM gaussienne ≈ 2,0 nm, contre 2,7 nm déclaré : même ordre, pas de constat. Viscosité du milieu (≈ 12,5 % molaire de butanol parmi les alcools) non donnée : `reserve`.
- **60 °C** : sous l'ébullition de l'éthanol, mais pression de vapeur ≈ 0,46 atm (Antoine, valeur de mémoire non vérifiée en ligne) : évaporation si récipient ouvert → `reserve`.
- **Sécurité HNO3 + éthanol** : CAMEO (« ignites upon contact with alcohols ») ; risque surtout à l'addition de l'acide concentré (≈ 14,3 mol/L), faible dans le sol final (0,24 mol/L).
- **Four** : « drying oven » à 450 °C avec contrôleur Nabertherm B170 = vraisemblablement un four à moufle ; non vérifié en ligne, signalé dans un `ok`.
- **Série ReaxFF et pression capillaire** (179,5 et 569 atm, recalcul exact) : hors périmètre sur consigne, non jugées.
- Recherches web : 8 recherches + 1 lecture de page. Densités : Sigma-Aldrich 244112 (Ti(OBu)4 1,00 g/mL, 340,32 g/mol), table ChemLin (HNO3 65 % : 1,3913 kg/L à 20 °C). Rien ajouté à fondateurs.md ni à constantes.md (Crossref bloqué).
- Comparaison base : PMC5521283 (film anatase 400 °C, n = 1,98), PMC5873029 (anatase 500 °C).
