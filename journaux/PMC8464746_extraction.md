# Journal d'extraction PMC8464746

- Découpage : trois voies de base (MSN-NH2, MSN-NAD en `intermediate`, ZIF@ADH/NAD-MSN/LDH en `material`) car l'article prépare le coenzyme greffé (2.2) puis l'enrobe dans le ZIF-8 (2.3) ; MSN-NAD est un réactif `intermediate` de la voie ZIF.
- MSN (synthèse « according to literature methods ») et MSN-COOH (carboxylation jamais décrite) n'ont pas de voie : listés dans `sample_inventory` avec raison ; MSN renvoyé aux réfs B36 et B37 dans `method_sources`.
- « 700 mL of APTSES » pour 200 mL d'éthanol et 0,2 g de MSN : recopié tel quel (unité probablement fausse), doute et `limite_reproductibilite` ; de même 0,2 g de MSN contre 2 g de MSN-COOH.
- Rangées du tableau 1 : les cinq premières (ADH seul, LDH seul, LDH+MSN-NAD, ADH+MSN-NAD, ADH+LDH) deviennent cinq branches de la voie de base, car la note de tableau dit que la préparation est « consistent with 2.3 » ; chaque composant retiré est une variation `absent` citée par la rangée entière. Les trois dernières rangées (substrats éthanol seul, pyruvate seul, les deux) sont des essais du même matériau : `outcomes` de la voie de base.
- Note 1 du tableau 1 (1 mg d'enzymes au total, 1 mg de MSN-NAD+) contre 2.3 (1 mg + 1 mg, 2 mg) : pas de variation de quantité ajoutée (trop ambigu pour les systèmes à une ou deux enzymes), doute écrit.
- Séries en température (30–50 °C) et en pH (6,5–9) : conditions d'essai du matériau fini, donc `outcomes` lus sur les Fig. 6A et 6B, pas des branches. Valeurs arrondies à 2 chiffres significatifs (ex. 108 → 110, 123 → 120).
- Fig. 5 : cinétique du matériau (7 points) lue ; le texte donne 124,605 μg/mL alors que la courbe plafonne vers 120 : les deux sont gardées, doute écrit.
- Témoins en enzymes libres : aucune voie (mélanges non synthétisés). Leurs deux concentrations écrites (58,850 et 46,235 μg/mL) vont en annotation `tendance_observee`, car le texte ne dit pas quelle valeur va à quel témoin.
- Fig. 3 : les Méthodes et la légende (rouge = rhodamine B = LDH) contredisent les Résultats (rouge = ADH) ; je n'ai pas attribué les couleurs. Fig. 1 : texte et légende ne s'accordent pas sur les lignes C et D ; non rangées sur une voie.
- Fournisseurs : NAD+ = RUIBIO (parenthèse) bien que la phrase le range sous Hefei Bomei ; HCl, éthanol, méthanol = Tianjin Weiyi par « All other reagents » (lecture littérale, pureté non citée).
- Solvant des solutions de Zn et de 2-méthylimidazole non écrit en 2.3 (« aqueous solution » seulement en 3.2) : non cité, pas de réactif eau ajouté ; rapport 40 mM / 2,8 mM noté comme inhabituel dans une annotation.
- Annexes S1, S2 et Table S1 absentes du dépôt : annotation « Annexe absente du dépôt : ». Figures 1 à 4 non converties en valeurs (qualitatives).
- Recyclage : 4 cycles (texte, Fig. 7A) contre « five repeated uses » en 2.7.2 ; texte et figure retenus, doute écrit.
