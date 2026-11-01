# PMC10169762 — critique scientifique (Opus)

- Fig. 4 (DRX) : graduations repérées par pixels (10° à x ≈ 74, 20° à x ≈ 166) ; le pic fort est à x ≈ 101–103, soit ≈ 12,9° et non 11,78° comme dans le texte. Classé `reserve` et non `probleme` : la figure est une image et la longueur d'onde n'est pas déclarée.
- Fig. 5 (ATG) : courbe lue par pixels (31,4 % à 800 °C, 28,8 % à 990 °C). Le rapport 0,917 correspond à Co3O4 → CoO (0,934 théorique) : le résidu est bien un oxyde de Co, d'où ≈ 23 % de Co (3,9 mmol/g). C'est la seule teneur en Co fiable de l'article ; elle sert de base aux calculs de NH3/Co et de charge de catalyseur.
- ICP 0,065 mol/g → `probleme` : 3,8 fois plus que le cobalt pur. Aucune réinterprétation de l'unité (mmol/g, g/g) ne colle avec l'ATG ; je n'en ai retenu aucune.
- NH3-TPD → `probleme` : 5,0 mmol/g sur 2,5 m2/g, soit ≈ 1200 NH3/nm2 contre ≈ 7,6 pour une monocouche (aire de NH3 tirée de la masse volumique du liquide). La Fig. 8 montre en plus un signal nul sous ≈ 400 °C, puis une montée au moment où l'ATG perd de la masse. J'en conclus à une décomposition prise pour une désorption, comme les auteurs l'admettent eux-mêmes au-delà de 475 °C.
- BET/BJH → `probleme` (Thommes 2015, tiré de fondateurs.md) : la Fig. 7 est en rayon r_p, monotone, sans pic à 1,66 nm. Avec 4V/S ≈ 19 nm (V lu sur la Fig. 6 ≈ 7,7 cm3/g) et une sphère équivalente de 1,2–1,6 µm (masse volumique supposée 1,5–2,0 g/cm3), la surface mesurée est celle des microsphères du MEB.
- Identité MOF → `probleme` : pas de structure ; Fig. 1 avec Co à 2 voisins et ponts NH déprotonés. Source retenue pour le mode N,S du pyrimidine-2-thiolate sur Co : structure Acta Cryst. E 2009 (PMC2970082). Auteurs non relevés dans l'extrait : je ne les ai pas inventés.
- IR S–H : `reserve` et non `probleme`. La forme thione domine (Stoyanov 1990 ; le NIST nomme le ligand pyrimidinethione) ; l'argument des auteurs n'est pas faux, il n'est simplement pas discriminant.
- Témoins du Tableau 2 recalculés en Co : 50 mg de sel (0,17 mmol) contre 50 mg de MOF (0,20 mmol), donc comparables. Ce qui pose question, c'est l'inactivité du Co(II) dissous face à la thèse de l'acidité de Lewis. Les NH2 basiques sont l'alternative que je propose ; non sourcée, d'où `basis` = chimie_generale.
- Tableau 4 : séries en masse à 100 °C contre optimum à 110 °C, donc deux variables à la fois (contrôle 5).
- « Co-P-MOF » dans le paragraphe IR : c'est la réf. 14 de l'article (Synth. Met. 2020, même groupe), ce qui confirme un reste de texte réutilisé.
- Pression dans l'autoclave : eau à 6,18 bar (NIST, page lue). Pression du DMF à 160 °C estimée par Clausius-Clapeyron (ΔvapH ≈ 47 kJ/mol supposée) faute de source ; indiqué dans sources_not_found.
- Source Co3O4 → CoO : document Kuwata et al. (douanes japonaises, 940 °C), sans année sur la page. J'ai écarté la fiche BenchChem, qui n'est pas une source primaire.
- Classement CLP du DMF et des sels de Co donné de mémoire, avec la mention « à vérifier sur ECHA » ; aucune recherche faite là-dessus.
- 9 appels web (8 recherches, 1 lecture NIST). Crossref bloqué : DOI non vérifiés 10.1139/v90-227 et 10.1039/D5DD00200A.
