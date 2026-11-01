# Journal de la critique de fidélité, PMC9374656

- Liste d'échantillons faite avant l'extraction : 6 compositions x = 0, 0.15, 0.3, 0.6, 0.8, 1 sur polyimide/SiO2 (Hall, Fig. 2e) et les 6 mêmes sur feuille de Mo (Raman, SEM/EBSD, cellule). Identique à `sample_inventory` ; aucun échantillon manquant. Les points de la Fig. 6b (Réfs 24, 26, 27, 30) sont bien écartés (non synthétisés ici).
- Pas de SI ni de tableaux dans l'article : une seule source de valeurs hors texte, les figures 2e, 5b, 6a, que j'ai ouvertes.
- Fig. 2e : calibré les axes par pixels (σ : 10^2 à y≈287, 10^3 à y≈115 sur le zoom). Point Ge ≈ 1100–1200 contre 1300 extrait, et le texte dit « up to 1200 » : constat `faux`, `probable` (la lecture a une marge ≈ ±8 %, mais 1300 sort du texte et de la figure). σ x = 0.8 ≈ 300 contre 350 : regroupé dans le même constat. Les p (échelle log, un chiffre) sont corrects à ≈ 20 % près, non signalés.
- Fig. 5b : zoom, 0 à y=753 et 3500 à y≈40 ; relu les cycles 1, 50, 100 des 6 compositions : tous à ≤ 5 % de l'extraction (ex. Si cycle 1 = 3130, Ge cycle 50 ≈ 1290). La valeur Ge cycle 50 (1300) > cycle 1 (1250) est correcte graphiquement (marqueur du cycle 1 masqué par 10e/20e). Non-constat.
- Fig. 6a : 0,1 C cycle 1 et 10 C relus (Si 3100, Si0.85 ≈ 2350 pour 2300 extrait, Si0.7Ge0.3 ≈ 260 à 10 C, Si0.4Ge0.6 ≈ 410) : conformes à ≈ 5 %.
- Raman, Fig. 3a : le texte dit « Si–Si, Si–Ge, Ge–Ge … 300, 400, 500 respectively », la figure montre l'inverse (Ge–Ge ≈ 300, Si–Si ≈ 500, Si pur à 520). L'extraction recopie le texte : pas une erreur d'extraction, donc `mineur` `sure`, avec annotation limite suggérée.
- Anode_Si sans variation 400 °C : le texte dit seulement « the same » ; `probable` plutôt que `sure` parce que l'article ne répète pas la température pour Mo (l'extracteur l'a déjà mis en doute).
- Fenêtre de potentiel : non écrite dans le texte, mais lisible sur les axes de la Fig. 4 (0–2.0 V). Classé `non_cite_a_tort` `probable` (appui = légende de Fig. 4, pas de phrase dédiée).
- CV : légende Fig. 4 donne x = 0, 0.6, 1 ; l'extraction met les conditions CV sur la voie x = 0.3, qui n'a pas de CV : `mineur` `sure`.
- `method_sources` vide : confirmé en lisant `corpus/refs` : CR6, CR34–CR38 (contexte), CR39/CR40 (calcul de composition par Raman = analyse de données), CR4 (contexte). Pas de constat.
- Écarté : l'annotation sur la fenêtre « 1 C » non défini et celle sur les masses (déjà en `limite_reproductibilite`) ; les `not_stated` des étapes de dépôt (substrate_temperature, ar_flow, deposition_rate, target_composition) : vérifiés absents du texte, donc corrects.
- Aucune citation de l'extraction hors du texte (vérification par sous-chaîne sur `corpus/text`).
