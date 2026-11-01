# PMC11302435 — critique scientifique (journal de décisions)

- Tableau 2 contre section 3.4 : le tableau est la recette du texte à 0,75 pour le zinc (1,468 → 1,101 g) et pour le volume (200 → 150 mL, en lisant « 100 mL » comme 100 mL par solution), pas pour le ligand (0,75 × 1,620 = 1,215 g contre 1,125 g écrit). Hypothèse d'une inversion de chiffres, notée comme hypothèse. Classé `probleme` parce qu'un chimiste ne sait pas quelles masses appliquer, même si la chimie est la même (Hmim/Zn de 3,7 à 4,0, [Zn] 24,7 mmol/L).
- Lecture « 2 × 100 mL » retenue comme la plus probable : c'est la seule qui donne la même concentration en zinc que le tableau (24,7 mmol/L).
- ZIF8_MeOH_80C jugé `incoherente` : 80 °C > Tb du méthanol (337,8 K, NIST), 1,81 bar par l'équation d'Antoine (Ambrose et Sprake 1970, domaine 288–357 K, donc 353 K est dans le domaine). Aucun reflux ni récipient fermé dans le texte.
- Pour 100 °C (373 K), j'ai pris le second jeu de coefficients d'Antoine (353,5–512,6 K) : 3,3 bar.
- ZIF8_MeOH_50C_2to1 : Hmim/Zn = 1,81 < 2. `probleme` parce que l'échantillon peut ne pas être du ZIF-8 pur (hydroxyde de zinc aux faibles rapports chez Zhang 2018), et l'article n'a aucune DRX.
- Optimum 1:2 en masse = 7,25 en moles : rapproché de l'optimum de 8 de Zhang 2018, lu dans l'article (PMC6018639) et non de mémoire.
- Voie aqueuse = recette de Pan 2011 multipliée par 10 (1:70) : identification par les masses. La taille de 85 nm chez Pan est de mémoire, signalée comme telle dans le JSON.
- PDI 0,725 : seuil de 0,7 de Malvern (livre blanc « DLS terms defined ») ; `reserve` et non `probleme`, puisque les auteurs écartent eux-mêmes cette voie.
- Marquage au 99mTc : `probleme` sur les kits 1 et 2. Le calcul qui le fonde : 4,43 µmol de Sn(II) contre 2,20 µmol de Zn par kit (≈ 0,67 mg d'équivalent SnO2 contre 0,5 mg de ZIF-8). La CCM ITLC-SG à l'acétone laisse colloïdes et particules à l'origine (Schorr 2024, tables UKRG/BNMS 2021). Il n'y a pas de témoin sans particules.
- Source retenue pour ce point : Schorr et al. 2024 (10.1021/acsptsci.4c00383), lue sur PMC11406700. Banerjee 2005 (interférence des colloïdes d'étain), citée par Schorr, n'a pas été ouverte et n'est pas utilisée.
- Stabilité dans le PBS (< 10 % de Tc libéré) contre ZIF-8 instable en tampon : Wahid et al. 2026 (ACS Omega, 10.1021/acsomega.5c11300), extrait lu sur PMC13044602. Laissé en `reserve`, car c'est un indice, pas une preuve.
- Mécanisme de liaison dative Tc–N : jugé peu probable dans le volume du solide (tous les N du réseau sont liés au Zn). Je propose à la place une adsorption ou coprécipitation de Tc(IV) hydrolysé et d'étain : c'est une hypothèse, non démontrée.
- Kit 3 à 0 % contre kit 4 à 10 % : en `reserve`, pas d'explication chimique sûre (adsorption de TcO4− qui disparaîtrait à 70 °C ?).
- Sécurité : 2-méthylimidazole Repr. 1B H360Df, harmonisé CLP (ECHA Annex XV, 2020) ; Skin Corr. 1C et Carc. 2 d'après la fiche Carl Roth. Absent de l'annotation de sécurité de l'extraction.
- Cravillon 2011 : notice bibliographique seule, contenu non lu, donc non cité comme appui (dans `sources_not_found`).
- Recherches web : 7 recherches et 3 lectures de pages (2 lectures ont échoué, DNS sur ncbi.nlm.nih.gov et vcu.edu). Rien n'a été ajouté à fondateurs.md ni à constantes.md (consigne : Crossref bloqué).
