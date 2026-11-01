# Critique des ajouts — PMC10324055 (Ce(III)-BDC, adsorption du phosphate et du fluorure)

Sources lues : `corpus/text/PMC10324055.txt` (annexe comprise), `corpus/refs/PMC10324055.txt` (renvois bibliographiques, utile pour savoir si une valeur est citée d'une autre publication), liste `PMC10324055_ajouts.md` et entrées correspondantes de `extractions/PMC10324055.json` (lecture seule). Une seule voie (`Ce-BDC_RT`), donc la question du rattachement à la voie ne se pose pas ; elle se pose pour l'espèce adsorbée (phosphate / fluorure) et pour la série de l'annexe.

## 1. Caractérisations et conditions de mesure (10 entrées, 10 conditions)

Les conditions de mesure sont les champs `conditions` des mêmes 10 entrées ; une ligne par couple.

| # | Catégorie | Élément | Verdict | Raison |
|---|---|---|---|---|
| 1 | caractérisation | Batch : réactifs, puretés, fournisseurs | juste | Matériaux relus ; rôles prudents, 5 réactifs sans rôle déclarés |
| 1 | condition | « analytical grade, no further treatment » | juste | Phrase de la section Materials, vaut pour tous |
| 2 | caractérisation | Calcul % adsorption / capacité (définitions) | juste | Co, Ce, V, m conformes ; équations absentes du texte |
| 2 | condition | Co, Ce en mg/L, V en mL, m en g | juste | Unités citées mot pour mot |
| 3 | caractérisation | Calcul désorption (définition) | juste | « adsorbed = (Co – Ce) » présent dans le texte |
| 3 | condition | désorption pH 2, 4, 6, 8, 10 (Fig. S10) | juste | Section Desorption Study ; autre protocole que eau / NaOH 0,1 M |
| 4 | caractérisation | Modélisation isotherme | juste | Langmuir et Freundlich, RL, 1/n et n comme écrits |
| 4 | condition | 10 à 50 ppm, reste à l'optimum, ambiante | juste | Paragraphe isothermes ; « ambient temperature » sans nombre |
| 5 | caractérisation | Modélisation cinétique | juste | PFO / PSO, formules de k1, k2, qe conformes au texte |
| 5 | condition | temps 1, 2, 3, 6 h ; 25 mL ; min dans le texte, h en annexe | juste | Texte, légendes S8 en h ; voir manque 3 sur la plage phosphate |
| 6 | caractérisation | Modélisation thermodynamique | juste | Kc = qe/Ce, pentes et ordonnées de ln Kc vs 1/T |
| 6 | condition | 20-60 °C « in the Methods » | juste | Réserve écrite ; Tableau 3 et Fig. S9 ne couvrent que 303-333 K |
| 7 | caractérisation | pHpzc (tracé de l'annexe) | douteux | Citation (légende S3) ne contient pas 4,61 ; doublon de l'entrée pHpzc |
| 7 | condition | procédure « refs 39, 40 » | juste | Renvois [[ref39]], [[ref40]] confirmés dans refs |
| 8 | caractérisation | Légendes S3 et S4 | juste | Valeurs conformes (Co 20, 0,1 g, 120 rpm, 16 h, pH 3 et 4, 0,2 et 0,35 g) |
| 8 | condition | 16 h contre 24 h des Méthodes | juste | Contradiction réelle et signalée ; 16 h absurde pour la série en temps |
| 9 | caractérisation | Légende S5a, série agitation | juste | 0,2 et 0,35 g, 3 et 6 h, pH 3 et 4 : mot pour mot |
| 9 | condition | légende d'annexe | juste | Rien d'ajouté |
| 10 | caractérisation | Légende S5b, série concentration | douteux | Légende brouillée ; citation ne contient pas « 100 and 120 rpm » |
| 10 | condition | Co = 20 mg/L pour la série en concentration | douteux | Co varie de 10 à 50 ; texte principal dit 120 puis 100 rpm |

## 2. Résultats (42)

Toutes les valeurs ont été comparées au texte, à l'abstract, aux Tableaux 1 à 4 et au texte de l'annexe. Espèce : phosphate toujours en premier, fluorure en second dans l'article ; les rattachements ci-dessous sont corrects sauf mention.

| # | Catégorie | Élément | Verdict | Raison |
|---|---|---|---|---|
| 1 | résultat | fluoride_PSO_R2_table2 = 0,99 | juste | Tableau 2, colonne R2 du PSO ; texte et annexe donnent 0,9997 (déjà en doutes) |
| 2 | résultat | fluoride_PSO_qe_calculated_text = 0,99 mg/g | juste | « 1.17 and 0.99 mg g–1 » phosphate puis fluorure ; tableau 0,999 |
| 3 | résultat | phosphate_Langmuir_Qo_text = 7,43 | juste | « 7.43 and 2.99 for Qo » ; unité non écrite, tableau 1 : 7,4 |
| 4 | résultat | optimum_pH_phosphate = 3 | juste | Abstract « optimized pH (3, 4) … respectively » |
| 5 | résultat | optimum_dose_phosphate = 0,2 g | juste | Idem ; Results : 0,05 à 0,2 g |
| 6 | résultat | optimum_contact_time_phosphate = 3 h | juste | Idem ; 98,7 % à 3 h |
| 7 | résultat | optimum_agitation_phosphate = 120 rpm | juste | Idem ; 120 puis 100 rpm |
| 8 | résultat | optimum_Co_phosphate = 10 ppm | juste | Idem ; 10 mg/L dans Results |
| 9 | résultat | optimum_pH_fluoride = 4 | juste | Abstract |
| 10 | résultat | optimum_dose_fluoride = 0,35 g | juste | Abstract ; Results 0,05 à 0,35 g |
| 11 | résultat | optimum_contact_time_fluoride = 6 h | juste | Abstract ; 96,7 % à 6 h |
| 12 | résultat | optimum_agitation_fluoride = 100 rpm | juste | Abstract |
| 13 | résultat | optimum_Co_fluoride = 15 ppm | juste | Abstract ; 15 mg/L dans Results |
| 14 | résultat | TGA perte 98-235 °C = 18,7 wt % | juste | Citation exacte ; somme des pertes incohérente, déjà en doutes |
| 15 | résultat | TGA seconde perte « up to 570 °C » = 10,4 wt % | douteux | Appelée « plateau stable » ; aucune borne basse ; somme > 100 % |
| 16 | résultat | TGA perte 570-664 °C = 59,8 wt % | juste | Citation exacte (Fig. 3 donne ≈ 35 %, déjà en doutes) |
| 17 | résultat | XRD première réflexion < 10 ° 2θ | juste | Conclusions ; unité ° implicite pour 2θ |
| 18 | résultat | FTIR changement après adsorption | douteux | Phrase générique « Always, a new peak … » ; aucun pic cité |
| 19 | résultat | phosphate Langmuir pente 0,1352 | juste | Fig. S6a ; 1/pente = 7,40 cohérent avec Qo |
| 20 | résultat | phosphate Langmuir ordonnée 0,1406 | juste | Fig. S6a ; pente/ordonnée = 0,96 = b |
| 21 | résultat | fluorure Langmuir pente 0,3347 | juste | Fig. S6b ; 1/pente = 2,99 |
| 22 | résultat | fluorure Langmuir ordonnée 0,5126 | juste | Fig. S6b ; b = 0,65 |
| 23 | résultat | phosphate Freundlich pente 0,5441 | juste | Fig. S7a ; 1/n = 0,54 |
| 24 | résultat | phosphate Freundlich ordonnée 0,5133 | juste | Fig. S7a ; Kf = 10^0,5133 = 3,26 |
| 25 | résultat | fluorure Freundlich pente 0,4507 | juste | Fig. S7b ; 1/n = 0,45 |
| 26 | résultat | fluorure Freundlich ordonnée 0,0467 | juste | Fig. S7b ; Kf = 1,11 |
| 27 | résultat | phosphate PFO pente +0,7098 | douteux | k1 = 1,63 (Tab. 2) = 2,303 × 0,7098 impose une pente négative ; signe sans doute perdu dans l'annexe |
| 28 | résultat | phosphate PFO ordonnée 1,4436 | juste | Recopie fidèle de Fig. S8a ; (qe = 27,8 contredit le tableau 2,75, article) |
| 29 | résultat | fluorure PFO pente −0,2457 | juste | k1 = 2,303 × 0,2457 = 0,566 = 0,56 du tableau |
| 30 | résultat | fluorure PFO ordonnée 0,4481 | juste | 10^0,4481 = 2,81 ≈ 2,80 du tableau |
| 31 | résultat | phosphate PSO pente 0,8548 | juste | 1/pente = 1,17 = qe calc du texte |
| 32 | résultat | phosphate PSO ordonnée 0,3828 | juste | Fig. S8b ; R2 = 1 |
| 33 | résultat | fluorure PSO pente 1,0007 | juste | 1/pente = 0,999 = tableau |
| 34 | résultat | fluorure PSO ordonnée 0,3462 | juste | Fig. S8d ; R2 = 0,9997 |
| 35 | résultat | phosphate ln Kc vs 1/T pente −1578,5 | juste | Fig. S9a ; ΔH ≈ 13,1 kJ/mol, tableau 1312,5 (×100, article) |
| 36 | résultat | phosphate ln Kc vs 1/T ordonnée 6,6755 | juste | ΔS ≈ 55,5 J/mol/K, tableau 55,3 |
| 37 | résultat | fluorure ln Kc vs 1/T pente −2390,6 | juste | Fig. S9b ; ΔH ≈ 19,9 kJ/mol, tableau 1987,5 |
| 38 | résultat | fluorure ln Kc vs 1/T ordonnée 8,1047 | juste | ΔS ≈ 67 J/mol/K, tableau 65,9 |
| 39 | résultat | phosphate thermo R2 = 0,991 | juste | Fig. S9a |
| 40 | résultat | fluorure thermo R2 = 0,9991 | juste | Fig. S9b |
| 41 | résultat | Table S1 phosphate 7,4 mg/g (pH 3, 3 h) | juste | Ligne « This work » ; c'est le Qo du Tableau 1, charge « 0.2 g L-1 » ambiguë (doutes) |
| 42 | résultat | Table S1 fluorure 2,99 mg/g (pH 4, 6 h) | juste | Ligne « This work », fluorure en colonne fluorure |

Attributions des équations de l'annexe aux espèces vérifiées par les R2 du texte (PSO phosphate 1, fluorure 0,9997 ; PFO 0,89 et 0,98) et par k1, qe, ΔH, ΔS recalculés : aucune inversion phosphate / fluorure.

## 3. Comparaisons littérature (20)

Rangées du Tableau S1 relues cellule par cellule (colonnes : pH, charge, temps, phosphate, fluorure, renvoi). Aucune confusion de colonne P / F. Valeurs rangées en littérature qui viennent de l'article lui-même : une seule suspecte (n° 4).

| # | Catégorie | Élément | Verdict | Raison |
|---|---|---|---|---|
| 1 | littérature | autres MOF au Ce · BET 5,28 m²/g | juste | Renvoi [[ref36]] derrière la valeur |
| 2 | littérature | Ce-BDC-2 · BET 1,34 m²/g | juste | Renvoi [[ref48]] |
| 3 | littérature | Ce(IV)-BDC UiO-66(Ce) · stabilité ≈ 200 °C | juste | Renvoi [[ref47]] (publication antérieure des mêmes auteurs) |
| 4 | littérature | acide téréphtalique · décomposition 370 °C | douteux | Aucun renvoi ; l'ATG de H2BDC est la Fig. 3 de l'article, donc possible mesure propre (déjà en doutes) |
| 5 | littérature | MOF Ln-BDC · hydrothermal 140 °C | juste | « hydrothermal (140 °C for 12 h) », renvois [[ref34]], [[ref35]] |
| 6 | littérature | MOF Ln-BDC · urothermal 120 °C | juste | « urothermal (120 °C for 5 days) » ; métal par voie non précisé, cité tel quel |
| 7 | littérature | La-ABDC · F 4,95 | juste | Ligne 1, colonne fluorure, réf. (1) |
| 8 | littérature | Ce-ABDC et Ce-BDC · F « 4,91 & 4,88 » | douteux | Deux matériaux, un seul enregistrement, ordre non écrit (signalé dans les conditions) ; « Ce-BDC » de la réf. (2) n'est pas celui de l'article |
| 9 | littérature | Montmorillonite · F 0,263 | juste | Réf. (3) Tor, fluorure |
| 10 | littérature | Alumine revêtue MnO2 · F 1,10 | juste | Réf. (4) |
| 11 | littérature | Argile décolorante usée · F 0,94 | juste | Ligne à 5 cellules seulement, réf. (5) traite du fluorure ; cellule manquante signalée |
| 12 | littérature | Poudre décolorante · F 0,2 | juste | Réf. (6), 0,2 en colonne fluorure |
| 13 | littérature | Chitosane FNP · P 1,87 | juste | Colonnes P puis F, réf. (7) |
| 14 | littérature | Chitosane FNP · F 1,22 | juste | Idem |
| 15 | littérature | Chitosane · F 1,39 | juste | « - - 1.39 » : fluorure, réf. (8) |
| 16 | littérature | Zéolite Zr + acide humique · P 4,21 | juste | Colonne phosphate, réf. (9) |
| 17 | littérature | Magnésie-pullulane · P 7,76 | juste | Réf. (10) colonne en lit fixe ; appariement des pH / temps non écrit (signalé) |
| 18 | littérature | Magnésie-pullulane · F 6,21 | juste | Idem |
| 19 | littérature | Biochar de coque d'amande · P 7,10 | juste | Rangée fidèle ; la réf. (11) porte sur des biochars Fe/Al, écart de l'article |
| 20 | littérature | Collagène imprégné de Zr(IV) · F 2,7 | juste | Réf. (12) Liao, fluorure |

## 4. Manques restants

1. Mécanisme d'adsorption écrit par les auteurs, absent de l'extraction : chimisorption suggérée par l'ajustement PSO, complexe Ce–F par échange de ligand avec les OH, complexation de surface du fluorure par Ce3+ (acide dur), interaction électrostatique, compétition OH- / anions à pH élevé, lavage jugé insuffisant pour la baisse de performance en recyclage (Recyclability Study, Adsorbent Dose et pH). À ranger en annotation de mécanisme.
2. Séries de l'annexe : les légendes S3 à S5 sont recopiées, mais la dose de la Fig. S4a est en g sur l'axe alors que les Méthodes écrivent g L-1 ; à porter en limite de reproductibilité (le doute existant sur la dose ne mentionne pas les axes de l'annexe).
3. Cinétique du phosphate : les axes de la Fig. S8a, b courent de 1,0 à 3,0 h, ceux du fluorure de 1 à 6 h ; la phrase « 1, 2, 3 et 6 h » du texte vaut peut-être seulement pour le fluorure. Non précisé dans l'extraction.
4. Étapes de mesure non fournies et pas déclarées `not_stated` pour le test d'adsorption : type et porosité du filtre, température numérique « ambiante », réactifs et temps de développement du bleu de molybdène (réactifs listés sans rôle), pH-mètre ; pour les techniques : vitesse de chauffe de l'ATG, dégazage avant BET, tension et courant DRX, tension d'accélération MEB, résolution et nombre de balayages IR.
5. Désorption : le pourcentage à pH 10 (62,5 et 68,9 %) est extrait, mais pas la précision du texte « regardless of the initial concentration » rattachée à ces valeurs (présente deux fois dans le fichier, donc probablement couverte).
6. Les ajouts n'ont pas de ligne pour la phrase « one of the most stable reported MOFs » (affirmation qualitative, sans nombre) : sans conséquence.

## Bilan

- Ajouts contrôlés : 82 (10 caractérisations, 10 conditions de mesure, 42 résultats, 20 comparaisons) ; aucune valeur n'est rattachée à la mauvaise espèce ou à la mauvaise rangée du Tableau S1.
- Faux : 0.
- Douteux : 8 lignes (7 ajouts, la série S5b comptant pour deux) — pHpzc (citation sans la valeur), série S5b et son Co de 20 mg/L (légende brouillée), TGA seconde perte 10,4 %, FTIR (phrase générique), pente PFO du phosphate (+0,7098, signe incohérent avec k1), 370 °C du linker (peut-être mesure de l'article, Fig. 3), « 4,91 & 4,88 » (deux matériaux en un enregistrement).
