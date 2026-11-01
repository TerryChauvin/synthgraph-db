# PMC11382057 — critique scientifique (journal de décisions)

- Conductivités (Tableau 1, SG) : avec σ = L/(R·S), L = 0,1 cm et S = 0,785 cm², 265 Ω donne 4,8 × 10−4 et non 1,04 × 10−3 S cm−1. Le rapport article/recalcul vaut 1,67, 2,05, 2,16 et 1,97 selon l'échantillon, donc ce n'est pas une constante unique (une aire d'Au plus petite pour toutes les pastilles aurait donné le même facteur). Classé `probleme` sur la voie de base, les branches 0,2 et 0,3 et la cellule Au ; doute de l'extracteur confirmé.
- « χ² = 3,26 » : 10,2/3,13 = 3,26 exactement, donc c'est le GOF ; χ² = 10,6. Classé `probleme` (grandeur dérivée mal nommée qui fait passer un ajustement moyen pour « satisfaisant »).
- Densité théorique : recalculée à 5,21 g cm−3 avec la maille de l'article et Z = 8 ; 96/91 % deviennent 94/89 %. Classé `reserve` seulement : l'écart MW/SG demeure.
- « 0.4 mol% » : classé `probleme` parce qu'un chimiste qui lirait le résumé doperait à une teneur environ dix fois trop faible ; le Tableau 1 (Li:La:Zr:Ga = 5,8:3:2:0,4) lève l'ambiguïté.
- « Poudre nanostructurée » : diamètre BET 6/(ρS) = 1,4 μm (MW) contre 1,7 μm (SG). Classé `probleme` : l'écart de d50 (0,80 contre 14,28 μm) vient de l'agglomération, et la thèse « nano → densification » ne tient que pour le précurseur.
- Sécurité : séchage à 250 °C d'un précipité imbibé de diéthylène glycol, au-dessus de l'auto-inflammation (229 °C, CAMEO ; 444 °F) et du début de décomposition (240 °C, fiche MEGlobal). Classé `probleme` parce que l'article ne dit rien. Le vase micro-ondes nitrates + glycol à 250 °C n'est qu'en `reserve` (vase conçu pour ça, mais remplissage non donné).
- Centrifugation : le surnageant écarté peut emporter Li (et Ga) ; aucune ICP. Classé `reserve` (hypothèse chimique, non démontrée), repris dans le témoin SG qui, lui, garde tout le Li.
- Témoin SG : change le solvant, la source de Li, le pH (NH3), le chauffage et la séparation. Gardé en `reserve` et non `probleme`, puisque les auteurs le présentent comme une comparaison de méthodes et non comme un témoin à une seule variable.
- x = 0,4 optimal et La2Zr2O7 à 0,45 : la solubilité du Ga va jusqu'à ≈ 0,72 (revue ACS AEM 2024) et Wagner 2016 garde le cubique de 0,10 à 0,60. J'attribue la pyrochlore à une perte de Li plutôt qu'à un excès de Ga (`reserve`).
- Al du creuset : la DRX ne porte que sur les poudres calcinées, alors que σ est mesurée sur des pastilles frittées en alumine (Geiger 2011). `reserve`, preuve non discriminante.
- Cellule Li : la baisse de Rb de 76 à 46 Ω (−40 %) sur une céramique est suspecte ; j'ai retenu la source MDPI Batteries 2018 (baisse de la résistance de la cellule associée à une pénétration de Li). `reserve` faute de preuve directe.
- Pression 3000 psi = 20,7 MPa : `reserve` parce que la phrase peut désigner le manomètre de la presse.
- Sources : 5 recherches web (11 requêtes). Les auteurs de la revue ACS AEM 2024, de l'article MDPI 2018 et de PMC9382651 ne sont pas relevés ; aucun DOI vérifié sur Crossref (bloqué). La limite d'emploi du PTFE (≈ 260 °C) est donnée de mémoire.
- compare.py « LLZO » ne trouve que cette publication : pas de comparaison possible dans la base.
