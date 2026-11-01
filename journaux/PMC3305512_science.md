# PMC3305512 — critique scientifique (journal de décisions)

- Aucune quantité dans l'article (« stoichiometric mixtures ») : le bloc `calculs` de la voie de base porte les masses pour 10 mmol, recalculées à partir de la formule, en prenant Fe(NO3)3·9H2O. Avec la masse molaire du « Fe(NO3)2·9H2O » écrit, il manquerait 15 % du fer.
- Combustion jugée `probleme` : pas de combustible. Le calcul de Jain donne φ ≈ 0,14 avec 5 gouttes d'éthanol (hypothèse 0,25 mL), avant même l'évaporation (Téb 78 °C). La revue Varma 2016 sert de référence au principe redox nitrate/combustible. Aucune source trouvée pour une combustion de nitrates sans combustible.
- L'ordre « 200 °C 24 h puis combustion » est jugé `probleme` : Fe(NO3)3·9H2O se décompose vers 125 °C (fiche Fisher). La source est une fiche fournisseur, faute d'avoir pu joindre PubChem.
- CuCl est classé `reserve` et non `probleme` : il est insoluble dans l'eau (≈ 5 L pour 0,3 g) mais se dissout par oxydation par Fe3+ (0,77 V contre 0,15 V). Le protocole reste donc faisable.
- Éq. 3 : recalculée avec ro = 1,38 Å (valeur écrite, 8,865 Å) puis avec 1,26 Å (8,360 Å, conforme au tableau). Conclusion : les auteurs ont calculé avec 1,26 Å. L'accord ath ≈ aexp peut être circulaire, puisque l'Éq. 3 redonne a quand rA et rB viennent des Éq. 5 et 6 avec μ = 0,375. Mais les rA et rB du tableau ne sortent pas des Éq. 5 et 6 (0,550 et 0,830 Å) : classé `reserve`.
- Densité X : l'Éq. 7 donne 5,360 à 5,377 g/cm³, en hausse avec Zn, contre 5,503 à 5,465 au tableau, en baisse. Classé `probleme`, confirmé par PMC11556383 (a = 8,388 Å, Dx = 5,35, conforme à l'Éq. 7). Le constat est répété sur chaque branche, car l'écart varie avec x.
- Distribution cationique (Éq. 4) classée `probleme` : Cu est absent, le fer total vaut 2 + δ, les sites ne sont pas conservés, et le Fe2+ est attribué à un « frittage » qui n'a pas eu lieu (600 °C sous air).
- Rayons ioniques : les tables de Shannon 1976 (DOI non vérifié sur Crossref) contredisent « Zn2+ 0.84 / Ni3+ 0.74 Å ». La tendance est réexpliquée par Zn2+(IV) 0,60 Å à la place de Fe3+(IV) 0,49 Å.
- Fig. 11 lue : ε' ≈ 0,8 pour x = 0 et ≈ 1 pour x = 0,2 à 1 MHz. Classé `probleme` (ε' < 1 impossible pour un diélectrique passif), sans source web : argument de physique générale (ε' ≥ n²).
- Tableau 3 : f = 1/(2πRC) ≈ 0,004 Hz, hors de la plage 42 Hz–5 MHz, quelle que soit l'unité de R (KΩ au tableau, ×10⁶ KΩ sur l'axe de la Fig. 12, vue dans corpus/fig). Classé `probleme` sur toutes les compositions.
- Lecture de la Fig. 1 : (311) vers 34,9° contre 35,58° attendu pour a = 8,361 Å. Classé seulement `reserve`, à cause de la précision de lecture (± 0,2°) et d'un décalage d'échantillon possible.
- Fig. 5 : un sixième tracé « 0.25 », hors série, est noté dans le contrôle IRTF.
- Pastille : densité de 94 à 97 % sans frittage décrit, et grains restés à 30 nm. Classé `probleme`, avec Zaspalis 2024 (≈ 97 % seulement après frittage vers 1000–1200 °C). La densité à cru de 50 à 65 % n'est pas sourcée (signalé dans sources_not_found).
- Mécanisme proposé : dénitration puis cristallisation à l'état solide à 600 °C, plutôt qu'une combustion. Variante donnée si un citrate a été omis.
- Recherches : 10 recherches web et 2 lectures de page échouées (ncbi.nlm.nih.gov et mdpi.com injoignables, DNS). Rien n'est ajouté à fondateurs.md ni à constantes.md (consigne).
