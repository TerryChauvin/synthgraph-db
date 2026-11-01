# Journal critique de fidélité PMC8263741

- Ma liste d'échantillons (faite après lecture de l'article, avant le JSON) : Li3PS4·DME, verre 1.5Li2S–0.5P2S5–LiI, 3 voies x (175, 200, 250 °C) = 9, plus l'expérience pTR in situ à 250 °C. Identique à `sample_inventory` : aucune branche manquante, aucune inventée.
- J'ai lu par inadvertance `journaux/PMC8263741_extraction.md` après l'article et avant le JSON ; il n'a rien changé à ma liste, mais je le signale pour l'indépendance de la lecture.
- Fig. 3 ouverte : σ (4.2e-6, 1.7e-5, 2.3e-6 ; 6.6e-4, 1.5e-4, 6.4e-5 ; 2.6e-3, 3.5e-3, 7.3e-5) et ρ (1.47, 2.38, 1.53 ; 2.07, 2.58, 2.65 ; 4.57, 3.06, 2.95) lus sur le graphique : écarts < 5 % avec le texte. Aucun constat de valeur.
- Fig. 2b/2c ouvertes : la présence de Li6PS5I à 200 °C (voie solide) n'est pas lisible ; je n'ai pas fait de constat, le doute de l'extracteur reste la bonne forme.
- Constat `non_cite_a_tort` (atmosphère du pressage à chaud) classé `probable` : « All processing steps » est général, mais la presse décrite ailleurs (CR31) n'est pas dite dans la boîte à gants ; texte à l'appui, interprétation à confirmer.
- Constat « Excess P2S5 » classé `sure` : phrase explicite dans les Méthodes, absente des données, et l'annotation la traite en hypothèse alors que c'est un fait. Stœchiométrie vérifiée : 10.62/4.553 = 2.33 < 3 (Li3PS4 : 3 Li2S pour 1 P2S5), donc P2S5 en excès, cohérent ; 500 mg Li3PS4·DME = 1.851 mmol cohérent avec M = 270 g/mol et 247.7 mg LiI = 1.851 mmol.
- Table S1 (Rwp, χ2) : `sure`, valeurs en annexe attribuées par colonne (Wet-chemical, Solid-state, Hot-press) aux échantillons à 250 °C.
- Fig. S2 (pTR sans évolution à 175 et 200 °C) : `sure` mais sans valeur numérique ; c'est un résultat qualitatif de l'article.
- Écarté : pression 176 contre 173 MPa. 2 t sur un disque de 12 mm donne ≈ 173 MPa ; l'extraction a retenu 173 avec un doute, c'est juste.
- Écarté : rattachement de l'expérience pTR à HotPress_250 (choix de découpage défendable, inventaire explicite) ; palier 5.5 h contre 5 h déjà en doute.
- Écarté : conductivités du verre ~1.2e-3 et 1.1e-3 (deux valeurs du texte, deux outcomes, doute présent).
- method_sources : CR29 et CR31 conformes à la règle du 2026-10-13 ; CR25 (DSC antérieure), CR52–54 (logiciels) et le « ref.1 » de la Fig. S3 (calcul) sont de l'analyse ou du contexte, non signalés.
- Mécanisme : le texte de l'article utilise ΔG = Ga – Gc et ΔV = Va – Vc puis écrit « ΔG < 0 » et « ΔV > 0 » en concluant verre plus dense ; les signes sont incohérents dans l'article. Constat `mineur` sur l'annotation, qui répète « ΔV > 0 » et « plus dense » sans le dire.
