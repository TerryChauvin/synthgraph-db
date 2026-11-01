# Journal d'extraction PMC11931415 (CaCl2/MOF-303)

- Découpage : quatre voies de base (A0 powder, A0 granule, A1, A1′) et six branches (A2–A4 depuis A1 par la concentration de la solution de CaCl2 ; A2′–A4′ depuis A1′ par la teneur en CaCl2). A0 granule et A1 sont des voies de base car leur protocole change de structure (extrusion ; imprégnation de granulés), les granulés et la poudre intervenant comme réactifs de rôle `intermediate`.
- Mapping A1–A4 = 10/20/30/40 % : « respectively » se trouve dans deux paragraphes différents (concentrations, puis noms) ; ordre croissant retenu, appuyé par la teneur croissante du Tableau 1 (doute consigné).
- A1′–A4′ : définis seulement par le Tableau 2, jamais dans les Méthodes. Lus comme les mélanges physiques « according to the content of CaCl2 » des composites imprégnés ; masses non citées, la quantité est portée en `amount_text` avec la phrase du mélange physique.
- Tableau 3 « A0 » : attribué aux granulés (colonne de 10 cm remplie de granulés), pas à la poudre ; doute consigné.
- Test de 50 cycles (Fig. 13) : échantillon non nommé dans le texte ; légende « (3) » ; rattaché à A3 en doute. Fig. 13 et Fig. 8 ouvertes : le pic (~980 mg g−1) n'est pas repris, les 96,1 % / 94,8 % sont dans le texte. Aucune valeur lue sur figure.
- TGA, EDS, FTIR du composite : échantillon non nommé, donc pas de caractérisation rattachée à une voie ; signalé dans `limite_reproductibilite`. FTIR de MOF-303 rattaché à A0 powder (phrase sur la synthèse de MOF-303).
- Surface BET : texte « 568–683 », résumé « 588–683 », Tableau 1 : 561 pour A4. Valeurs du Tableau 1 par échantillon, plage du texte ignorée.
- Pureté/fournisseur : phrase de la section Matériaux (Macklin) citée en `supplier_quote` pour AlCl3·6H2O, ligand, NaOH, méthylcellulose, CaCl2 ; l'eau n'a ni pureté ni fournisseur. Le mélange eau/éthanol du granulé n'est pas rattaché à l'éthanol absolu listé (non cité).
- Ligand : « pyrazolecarboxylic » (Matériaux) vs « pyrazole dicarboxylic » (Méthodes) ; « 43.08 mol » = coquille pour mmol (7,5 g ≈ 43 mmol) ; seule la masse est extraite.
- Source de méthode : [[cit30]] (Méthodes) et [[cit25]] (Résultats) pour la même préparation de MOF-303 ; deux entrées `method_sources`. [[cit29]] (valeur BET de la littérature) et [[cit31]]–[[cit36]] (Tableau 2) sont des comparaisons de résultats, pas des méthodes.
- Échantillons sans voie : tamis moléculaires 3A/4A/5A/13X, gel de silice, MOF de la littérature du Tableau 2 (commerciaux ou repris de la littérature).
- Pas de voie `device` : les essais d'adsorption sont des mesures du matériau fini (outcomes).
