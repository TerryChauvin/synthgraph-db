# PMC5707940 — critique scientifique (journal de décisions)

- Recette de carboxylation (0,2 g GO ; 12 g NaOH ; 10 g ClCH2COOH) jugée « ok » et non « excès suspect » : rapports 60 et 50 g/g de GO, identiques à Sun et al. 2008 (1,2 g + 1,0 g pour 10 mL à ≈ 2 mg/mL) multipliés par 10. Le protocole de Sun vient de l'extrait de la recherche web (PMC, arXiv et RSC injoignables par DNS) : à confirmer sur le texte.
- Volume d'eau non écrit : pris à ≈ 100 mL par analogie avec Sun pour estimer l'exotherme (≈ 19 kJ, ≈ +45 K). Hypothèse affichée dans le calcul, statut « reserve » seulement.
- « Ce 900 mg/L → 780 mg/g » classé `probleme` : bilan C0 = Ce + qe·m/V sur les points lus de la Fig. 3a donne C0 ≈ 978 pour (490 ; 780) et ≈ 902 pour (455 ; 715). Donc 780 mg/g = C0 1000, et le point à C0 900 vaut ≈ 715.
- qm : intercept Langmuir 0,00208 → 481 mg/g ; pente « 0000216 » lue 0,000216 après contrôle sur la Fig. 3c (≈ 0,0097/44). Le 780 du tableau 2 (colonne qm) est un qe ponctuel → `probleme`.
- KF : Fig. 3b est en ln (axes « lnqe », « lnCe »), donc KF = e^5,706 ≈ 301, et non 508 (ln 508 = 6,23). Vérifié par la prédiction à Ce = 488 (733 contre 1239 mg/g). Aucune origine trouvée au 508.
- Cinétique : le qe implicite de la Fig. 4b (≈ 915 mg/g) a été reconstruit à partir des premier et dernier points (ln(qe−qt) 6,45 et 4,38) et des qt de la Fig. 4d ; lecture graphique à ± 5 %.
- Thermodynamique : régression refaite sur les 4 points lus de la Fig. 5b (R² 0,64, IC 95 % de ΔH −32 à +83 kJ/mol) ; les ΔG du tableau 3 sont exactement ΔH − TΔS (calculés depuis la droite, pas depuis Kd). Les Kd recalculés par bilan depuis la Fig. 5a sont monotones, ce que la Fig. 5b n'est pas.
- Problème d'unité de Kd (L/g) : appuyé sur Milonjić 2007 (page du dépôt VinaR, DOI non relevé) et Tran et al. 2017 (DOI du résultat de recherche, non vérifié sur Crossref).
- Comparaison des séries à condition nominale identique (665 → 990 mg/g) : « reserve » et non « probleme », car la série en pH n'a pas de température écrite (« aforementioned protocol » suppose 303 K).
- 1190 mg/g contre 2630 m²/g : aire du MB 1,30 nm² (suppdata RSC c7nj01900a, auteurs non relevés) ; 2630 m²/g recalculé (aire de 0,0262 nm² par atome C, deux faces) plutôt que cité de mémoire (Stoller 2008 non vérifié, donc non cité).
- Mécanisme : « electrophilic addition » → `probleme` de vocabulaire (SN2 de Williamson) ; la réduction partielle du GO en milieu basique est appuyée sur Guo et al. 2020 (Nanoscale Adv.), trouvé en cherchant Sun et al. ; Fan et al. 2008 (Adv. Mater.) n'a pas été retrouvé, donc pas cité.
- Preuve de carboxylation `probleme` : 3470 cm−1 = O–H ; les composantes XPS « C–O »/« C=O » de GO-COOH descendent en énergie (286,65/287,45 eV) ; aucune composante O–C=O vers 289 eV n'est annoncée.
- Régénération : le choix de pH 3 est jugé peu désorbant d'après la Fig. 6a de l'article lui-même (≈ 600 mg/g à pH 3).
- Recherches web : 7 (et 4 ouvertures de page refusées par DNS). Rien n'a été ajouté à fondateurs.md ni à constantes.md (Crossref bloqué).
