# PMC12624334 — critique scientifique (journal de décisions)

- Reprise après coupure : aucun fichier science existant ; vue `review.py science` régénérée, article relu en entier (annexe S1–S2 comprise).
- Une entrée par échantillon (6 voies) : chaque branche change la chimie (sel dopant), donc chacune a son calcul de quantités. Les masses par sel (ex. 80:15:5 → 803 mg Zn, 205 mg Fe, 49 mg Ni) sont calculées ici, pas écrites par les auteurs.
- TEA : 3,9 mL × 0,726 g/mL (fiche Sigma) = 28,0 mmol → Zn : MeIm : TEA = 1 : 8 : 8,3. Bilan jugé sain ; nuance au mécanisme de l'extraction : la TEA (pKaH 10,75) ne déprotone pas le ligand libre (pKa N–H ≈ 14,5), elle déplace l'équilibre de coordination.
- Solubilité TEA (17 g/100 mL, ICSC) et LCST ≈ 19 °C : 378 g/L dans la solution de ligand → `reserve` seulement, car le 2-MeIm peut servir de cosolvant ; pas de preuve d'un mélange biphasique.
- BET 378 m2/g mis en `probleme` (comparaison_base) : 4 fois sous Park 2006 et sous les ZIF-8 de la base (PMC9048217, PMC10964133). Gardé en `probleme` et non en `reserve` parce que toutes les comparaisons de surface de l'article reposent sur ce témoin.
- Tableau 2 : les « mass content » coïncident avec la composition nominale ramenée aux métaux (Fe15/Ni5 : 82,2/13,2/4,6 calculé contre 82,96/12,50/4,55) → normalisation non dite ; et cette concordance ne prouve pas la substitution (Fe3+ précipite de toute façon en milieu basique).
- Substitution Fe3+ : `probleme` (preuve non discriminante + compensation de charge absente + erreur de rayons ioniques ; Shannon 1976 : Fe3+ IV 0,49 Å < Ni2+ < Zn2+ 0,60 Å, valeur Fe lue dans le tableau de Shannon).
- XPS Ni3+ 56 % : `probleme` sur la base de Ni(OH)2 à 855,6 eV (table Thermo Fisher) et de Biesinger 2011 ; « Fe métallique » : recouvrement Ni LMM / Fe 2p confirmé sur la page Thermo Fisher du fer (fetch).
- Gaps : 1239,84/2,33 = 532 nm alors que les spectres s'arrêtent à 500 nm → extrapolés hors données ; source Makuła 2018 pour les bords multiples des solides dopés. Ni@ZIF-8 a le plus petit « gap » (2,23 eV) mais moins d'activité : signalé en `probleme` sur la voie Ni@ZIF-8.
- pH 3 : instabilité acide du ZIF-8 sourcée par Sun 2012 (DOI trouvé via une citation ACS, 10.1039/c2dt30357d) ; article ACS Omega 2026 ajouté en appui mais auteurs non relevés.
- Lixiviation (tableau S2) : hypothèse 10 mL / 10 mg (non écrite) → Ni ≈ 20 % lixivié contre Zn ≈ 0,5 %. Hypothèse signalée dans `calculs` ; lecture des rangées Before/After du tableau S2 déduite de l'ordre du texte extrait (étiquette d'élément entre les deux rangées).
- Efficacités : 83,51 % retrouvé à 82,7 % en normalisant par Ce (après adsorption) → confirme le doute de l'extracteur ; incohérence des conditions (pH 6,8/11 ; 10/30 mg) mise en `probleme`.
- GFN2-xTB : angle N–Ni–N de 132° contre « tétraédrique » → `reserve` (calcul des auteurs, hors synthèse).
- Gross, Sherman, Vajo 2012 (TEA en milieu aqueux) : DOI non retrouvé → non cité, placé dans `sources_not_found` ; Nordin 2014 (RSC Adv., URL éditeur) utilisé à la place.
- Recherches : 8 web_search (une refusée par limite de débit) + 1 web_fetch. Rien ajouté à fondateurs.md ni constantes.md (Crossref bloqué).
