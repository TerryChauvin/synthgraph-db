# PMC9061730 — critique scientifique (journal de décisions)

- **Énergies DSC (probleme, voie rGO|CuNP)** : borne calculée avec ΔfH°(AP) = −295,77 kJ/mol (NIST WebBook, lu) : NH4ClO4 → HCl + 1,5 H2O(g) + 0,5 N2 + 1,25 O2 donne 1,36 kJ/g ; avec Cl2 1,60 kJ/g ; même avec H2O liquide ≤ 2,35 kJ/g ; +0,33 kJ/g pour 1 % de carbone brûlé. 3559 et 2851 J/g (Fig. 6, étiquettes) dépassent la borne. Rangé sur la voie rGO|CuNP (celle qui porte la conclusion « 3,5 fois ») et repris dans `author_errors_suspected` pour toutes les voies.
- **Cu(0) non prouvé (probleme, CuNP)** : 0,212 nm est plus proche de Cu2O(200) (2,135 Å, a = 4,270 Å) que de Cu(111) (2,087 Å, a = 3,615 Å) ; EDS sans information de degré d'oxydation ; pas de DRX/XPS. Sources : PMC4726356 (Cu{111} 0,208 nm) et ACS Omega 2026 (Cu2O(200) 0,21 nm).
- **Bande à 390 nm (probleme, CuNP)** : plasmon de Cu attendu à 570–580 nm (PMC3852993) ; 242 nm au pH 1 attribué à l'acide ascorbique non dissocié (chimie générale, λmax ≈ 245 nm, non sourcé en ligne).
- **Redox CuCl → Cu à pH 1 (reserve, pas probleme)** : calcul de Nernst défavorable d'environ 0,1–0,15 V, mais l'E°' de l'ascorbate (+0,06 V à pH 7) est une valeur de consensus non relue en source primaire et Xiong 2011 obtient du cuivre par cette voie ; d'où une simple réserve, mécanisme « a_revoir » avec intermédiaire CuCl (PMC10171199).
- **Composite non lavé (probleme)** : 12,3 mmol d'AA (2,17 g) pour 127 mg de Cu ; séché tel quel ≈ 5 % de Cu, alors que les auteurs supposent ≈ 50 % (« double amount of copper »). Le pic de fusion de l'acide ascorbique dans leurs DSC appuie la présence de résidu.
- **Témoin taille 6 → 2 nm (probleme)** : AA/Cu passe de 2,0 à 6,15 et un traitement à pH 10 s'ajoute ; Xiong 2011 donne déjà < 2 nm sans support (résumé lu seulement).
- **rGO « colonnes à 3 Å »** : laissé en réserve ; 3 Å n'est pas une distance du plan de graphène, plutôt l'empilement (0,335 nm).
- **rGO 65 °C / 1 h** : comparé à Fernández-Merino (95 °C, pH 9–10, NH4OH) via la revue PMC9505528 ; réduction jugée partielle, cohérente avec le pic à 360–370 °C.
- **GO** : protocole identique à Marcano (fondateurs.md) ; seuil Mn2O7 55 °C pris dans Dreyer 2010 (fondateurs.md), sans recherche web.
- **Sécurité perchlorate d'ammine de cuivre** : mise en chimie générale, sans source consultée (risque si la solution ammoniacale de Cu touche l'AP humide).
- Hypothèses non écrites par l'article et signalées comme telles : acides concentrés (98 %, 85 %), GO à 30–40 % d'O.
- Recherches : 7 recherches web + 2 lectures de page (NIST AP, page Marcano ACS ; cette dernière n'a rendu que le résumé). Crossref bloqué : aucun ajout à fondateurs.md ni à constantes.md.
- Validité JSON non vérifiée par script (Bash refusé en cours de session) : fichier écrit à la main, à contrôler avec critic_load.py.
