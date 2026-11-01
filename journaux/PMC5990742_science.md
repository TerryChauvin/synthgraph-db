# PMC5990742 — critique scientifique (journal de décisions)

- Teneur « x % MoS2 » : 0,05 g de molybdate ≈ 0,283 mmol Mo ≈ 45 mg MoS2 ; rapporté au g-C3N4 maximal théorique (1,61 g, carbone limitant) cela fait déjà 2,7 %, et ≈ 9 % au rendement réel de la thiourée (11 %, Alwin 2020, sous air). Le nom est donc la masse de molybdate sur la masse de thiourée → `probleme` (bilan) sur les trois composites.
- Rendement sous argon à 500 °C : aucune source trouvée ; j'ai donné une fourchette 0,2–0,44 g en hypothèse, en le disant (sources_not_found).
- Mo/N XPS (2,4 %) comparé au Mo/N en volume calculé (0,4 % au rendement maximal, 1,5 % à 11 %) : l'argument va dans le sens d'un faible rendement, mais l'XPS sonde la surface ; je l'ai gardé comme appui, pas comme preuve.
- Photocourant : Résultats « lower photocurrent » contre Conclusion « increased photocurrent » ; et un photocourant plus faible n'est pas une preuve de séparation des charges → `probleme` (cohérence entre sections et preuve discriminante).
- Sécurité : l'article se dit « avoiding harmful reactants » ; la thiourée est CLP H351/H361d et sa pyrolyse dégage NH3, CS2 et HCN (Madarász & Pokol 2007) → `probleme` sécurité, pour que l'orchestrateur en fasse une annotation.
- Mécanisme : l'hypothèse de l'extraction (sulfuration par H2S) contredit Madarász & Pokol 2007 (pas d'H2S détecté par TG-FTIR ni TG-MS, gaz principaux NH3 + CS2) → `a_revoir`, sulfuration par CS2/HNCS proposée. DOI de cet article non trouvé ; référencé par sa notice real.mtak.hu.
- XPS : 232,2 − 229,4 = 2,8 eV contre ≈ 3,1–3,15 eV pour Mo 3d (3,14 eV fixé dans arXiv:2106.07366, source secondaire faute de mieux) → `reserve`, possibilité de Mo(VI) résiduel ; Mo─N à 228,6 eV jugé non discriminant.
- HRTEM 0,67 nm : 2H-MoS2 d(002) = c/2 ≈ 0,615 nm ; le (100) du g-C3N4 à 13° donne 0,680 nm par Bragg → `reserve` plutôt que `probleme` (la cartographie Mo/S soutient quand même la présence de MoS2).
- « Mo et S proches de 2:1 » : en réalité S/Mo = 1,79 ; inversion de vocabulaire, `reserve`.
- k et C/C0 : exp(−2k) reproduit la figure pour g-C3N4 et 1,25 %, mais pas pour 0,5 % (0,16 contre 0,24) ni pour 2,5 % (0,10 contre 0,17) ; écart supérieur à la précision de lecture → `reserve` sur les branches.
- Témoin g-C3N4 sans dissolution, évaporation ni broyage : la hausse de SSA peut venir en partie de la mise en forme → `reserve`, témoin proposé.
- Hystérésis sur le g-C3N4 dit « sans mésopores » : `reserve`, avec Thommes 2015 (fondateurs.md).
- Source Huu et al. 2021 (Sci. Rep., thiourée + molybdate de sodium à 500 °C sous N2) retenue comme confirmation de faisabilité ; texte complet non ouvert (NCBI injoignable), appui pris sur le résumé.
- CS2 : page CAMEO non ouverte ; auto-inflammation ≈ 100 °C relevée dans REMPEC et une FDS (secondaires) : valeur donnée comme ordre de grandeur.
- 11 recherches web (une de plus que la dizaine prévue, pour le DOI de Madarász, sans succès).
