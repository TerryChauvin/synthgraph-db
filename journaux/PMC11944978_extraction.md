# Journal d'extraction PMC11944978

- Découpage : une seule voie de base, CDs_220C_6h (section 3.3). L'article n'a aucune branche exploitable : la section 2.1 dit que mélamine et éthylènediamine ont été réagies « under different temperatures and times » et que 220 °C / 6 h donnent la meilleure fluorescence, mais aucune autre valeur n'est écrite (tout est dans la Figure S1, annexe absente). Règle des plages sans valeurs listées : pas de branche, l'optimisation figure dans `sample_inventory` avec `route: null`.
- Annexes : aucune section « Supporting Information » dans le fichier ; Figure S1, Figure S2 et Table S1 sont citées dans le texte. Une annotation `limite_reproductibilite` « Annexe absente du dépôt : » les nomme.
- Figures : le dossier corpus/fig est présent, mais aucune figure ne porte de résultat absent du texte (tailles, bandes Raman, durées de vie, LOD, récupérations sont toutes dans le texte ou la Table 2). Aucune valeur lue sur figure, donc pas de `from_figure`.
- Voie device non créée pour le dosage de l'hémine : c'est un protocole de mesure sur le matériau fini (section 3.5), rangé en `characterizations` avec ses volumes, et ses résultats en `outcomes`, conformément à la règle « tests du matériau fini ».
- Rangées de la Table 2 (comprimés Changxing groupes 1 à 3) : taux de récupération gardés en `outcomes` de la voie CDs avec la rangée entière en citation ; les comprimés ne sont pas des matériaux synthétisés (inventaire : route null).
- XPS : « 56.23%, 24.21%, and 19.55%, respectively » attribué à C, N, O dans l'ordre de la phrase précédente (carbon, nitrogen, and oxygen) ; doute posé.
- Contradiction Figure 3 (légende NaCl 0 à 4 M par 1, pH 2, 4, 6, 8, 12) contre Méthodes 3.4 (pas de 0,5 M ; pH 2,21 à 10,88) : aucune valeur chiffrée extraite de la figure, seul le qualitatif du texte ; doute posé.
- Four : « air blast drying oven » (3.3) et « electric thermostatic drying oven (Shanghai Yiheng) » (3.1) lus comme le même appareil, marque seulement dans l'équipement de l'étape de chauffage.
- Seuil de dialyse « 500–1000 DA » recopié en `value_text` (probable Da).
- Pureté de l'eau : « 18.2 MΩ·cm−1 » repris de la phrase de 3.2 ; fournisseur de l'eau déclaré `not_stated` (Merck KgaA est cité pour le système Milli-Q, pas pour l'eau comme réactif). Pureté de la mélamine et de l'éthylènediamine non citée.
- Ambiguïté de dilution du dosage (50 μL de CDs et d'hémine dans 500 μL) contre les concentrations annoncées dans les Résultats : rapportées telles quelles, doute et limite de reproductibilité.
- Famille du matériau : `carbone` (points de carbone) plutôt que `quantum_dot`.
- Pas de `method_sources` : les renvois bibliographiques portent sur le contexte (modèles, méthodes générales de synthèse de CDs), aucun ne fournit un protocole nécessaire à refaire la préparation.
