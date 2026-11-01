# PMC8693586 — critique scientifique (journal de décisions)

- Voies jugées : RBM_extract, pH4_2h (base), pH10_2h_ratio_1to5 (porte la série en proportion), pH9_2h (anomalie 176 nm), pH10_6h (échantillon caractérisé et testé). Les 30 autres branches pH × durée ne changent pas la chimie : non jugées une à une.
- Série en proportion jugée « incoherente / non_reproductible » : avec AgNO3 = 5,0 mL et mélange = 10,0 mL, seul 1:1 est possible ; mélange à 10 mL → Ag de 33 à 83 µmol ; AgNO3 fixé → volume total de 6,0 à 15,0 mL. Problème de l'article, pas de l'extracteur.
- Rendement « constant » : les deux lectures donnent des sens opposés à une absorbance constante ; j'ai retenu la lecture « Ag+ épuisé, réducteur en excès » comme la plus compatible, sans la donner pour sûre.
- Absorbances 0,13–1,5 contre 5 mM d'Ag : borne basse A(250 nm) = 17,5 avec ε interbande 3 500 M⁻¹ cm⁻¹ (Abkhalimov, PMC9504487) → spectres forcément dilués. Paramelle 2014 (table SPR) préféré mais page RSC bloquée par le proxy ; je n'ai pas cité de valeur SPR que je n'ai pas lue.
- Seuil Ag2O : Ksp(AgOH) 1,52 × 10⁻⁸ (Wikipedia, secondaire) et 2 × 10⁻⁸ (table UCF/OpenStax) → pH ≈ 8,5–8,6 à 5 mM. Statut « reserve » et non « probleme », car le pH du mélange n'est pas connu (l'extrait non tamponné peut s'acidifier au mélange).
- Réactif d'ajustement du pH absent : « probleme » sur RBM_extract, car NaOH et NH3 (Tollens) donnent des chimies différentes ; ajout d'un avertissement argent fulminant si NH3.
- DPPH 2,5 mg/mL = 6,34 mM → 3,17 mM dans le mélange → A ≈ 40 avec la pente 12 509 de Brand-Williams (lue dans l'extrait de recherche, HAL inaccessible). Second calcul indépendant : 0,8 µg de matière ne fournit au plus que ≈ 13 nmol d'électrons, contre 45 nmol de DPPH à réduire même à 0,1 mM → 44,8 % impossible ; artefact ou extrait libre.
- MTT : « 20 mL », « 150 mL » par puits = µL ; « 5,0 µg/mL » probablement mg/mL. Source d'interférence AgNP/MTT : RSC Adv. 2015 (10.1039/C5RA14100A), auteurs non relus ; l'étude 2020 (PMC7028487) trouvée mais non ouvrable, non citée.
- IC50 vs viabilités : HCT116 41,1 % à 12,5 (IC50 13,07) et HeLa 48,1 % à 20,0 (IC50 26,18) incohérents pour une courbe décroissante ; laissé en « reserve » (un ajustement sur des points dispersés peut le produire).
- Doses biologiques en masse de lyophilisat sans teneur en Ag dosée : « probleme » (dose d'argent réelle inconnue ; ≤ 5,4 mg d'Ag par lot).
- SAED : a recalculé 4,04–4,11 Å (moyenne 4,077) contre 4,086 Å ; anneaux (222), (400), (331) absents avant (420) → réserve sur l'indexation, pas sur l'identité Ag.
- FTIR de l'extrait seul (Fig. S3) présenté comme preuve des agents de recouvrement : « probleme » de preuve discriminante (contrôle 7).
- Mécanisme des auteurs (« ligands complexants qui accélèrent ») jugé à revoir : complexer Ag+ ralentit sa réduction ; préféré : phénolates et sucres plus réducteurs à pH élevé, Ag2O transitoire possible au-dessus de pH 8,5.
- Okitsu (chapitre Springer, 10.1007/978-90-481-3887-6_5) cité pour la réduction sonochimique possible ; témoins sans ultrasons, sans extrait et à l'obscurité absents.
- Recherches web : 10. Rien ajouté à fondateurs.md ni constantes.md (Crossref bloqué, consigne).
