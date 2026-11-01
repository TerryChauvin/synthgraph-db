# Journal de la critique de fidélité, PMC10386591

- Liste d'échantillons faite avant d'ouvrir l'extraction : GO, rGO, rGO-ZnS 13.3 (base), 9.3, 11.4, 15.2, 17.0 wt%, ZnS nu (8 voies), plus ZnO, Nano ZnO, blanc sans catalyseur et amoxicilline sans préparation. Identique à `sample_inventory` : aucun échantillon manquant.
- Aucune section Supporting Information dans `corpus/text` : Fig. S1-S5 et Tables S1-S3 absentes, donc aucun résultat par teneur en rGO ; l'extracteur l'a bien signalé, pas de constat.
- ZnS, FT-IR : « 3246 cm−1 ... in synthesized ZnS nanoparticles » (section 3.5) est absent de la voie ZnS, qui n'a que XRD et SEM. Constat `manquant`, `sure` (passage explicite, attribution claire à ZnS).
- XPS, C 1s (284.5 / 284.7 / 286.9 eV) : absent. `sure` pour l'absence ; l'échantillon est ambigu (texte « for rGO », légende Fig. 4 « XPS spectra of the rGO-ZnS »), je le dis dans le correctif plutôt que de trancher.
- Table 2 : vérifié arithmétiquement. 5376.0/9049.6 = 0.594 : 59.4 % est la fraction restante, pas l'élimination (40.6 %) ; la rangée 150 min est cohérente (806.4/9049.6, 91.1 % éliminé). Valeur correctement recopiée, donc `mineur` : à annoter, pas à corriger. `sure` car c'est un calcul.
- Table 1 et Table 3 relues rangée par rangée contre l'extraction : 88.7 / 63.5 / 52.1 / 38.2 et colonnes rGO (9, 11, 10, 11, 10), ZnS (9, 12, 10, 9, 9), rGO-ZnS (15, 21, 23, 17, 19) attribuées aux bonnes voies. Texte (BQ 63.5) et table (38.2) divergent : déjà en doute, rien à ajouter.
- Fig. 7 ouverte (valeurs `from_figure`) : lecture ≈ 27.5, 47, 88.7, 61, 59 contre 28, 47, 89, 61, 59 extraits ; écart maximal < 2 %, bien sous le seuil de 10 %.
- Fig. 5 et Fig. 8 ouvertes (hors `from_figure`) : ZnS lu ≈ 87 % contre 81.8 % du texte (doute déjà en place). Fig. 8 : le dernier point de chaque cycle donne ≈ 87, 82 et 77 % de dégradation, qui ne correspondent pas à 93.7 / 68.4 / 63.9 ; constat `mineur`, `probable` (lecture graphique ± 3 points), demandant seulement de compléter le doute existant.
- ZnO (78.8 %) et Nano ZnO (61.1 %) : non stockés nulle part ; `probable` car l'absence de voie est un choix défendable, mais l'information se perd.
- Rôle « precursor » pour NaNO3 : interprétation de l'extracteur, l'article ne donne aucun rôle. `mineur`, `probable`.
- Écarté : température de l'étape 2 de rGO déclarée `not_stated` alors que « at 350 °C » figure à l'étape 1 ; l'article ne la répète pas et la valeur est physiquement impossible, la lecture littérale de l'extracteur est défendable (mise dans `notes`).
- Écarté : volume de H2SO4, quantité d'hydrazine, `rGO_amount` pour les branches : les `not_stated` correspondent bien à des absences réelles dans le texte.
- `method_sources` : trois renvois de méthode en section 2 (B43 COD, B44 Hummers, B45 rGO), tous présents, aucun faux ; le rôle `autre` pour B43 est acceptable.
- Reproductibilité (notes) : 11.358 g de Zn(NO3)2·6H2O dans 100 mL donne 0.38 M, pas 0.4 M ; 3.122 g de Na2S = 0.4 M seulement pour la forme anhydre, non précisée. Je ne l'ai pas mis en constat (ce n'est pas une erreur d'extraction) mais dans `reproducibility_gaps`.
