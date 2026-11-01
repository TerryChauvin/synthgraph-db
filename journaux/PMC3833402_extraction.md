# Journal d'extraction PMC3833402

- Découpage en deux voies de base, sans branche : le complexe [Cd(detu)2(OOCCH3)2]·H2O (section 2.2) et les nanoparticules de CdS (section 2.4). Aucune série de conditions n'est testée (une seule thermolyse à 150 °C), donc rien à mettre en branche.
- Le complexe est classé `kind: intermediate` (isolé, caractérisé puis réutilisé comme précurseur), famille `autre`. Dans la voie des nanoparticules il figure en réactif de rôle `intermediate`, nommé avec le label de la voie du complexe, sans pureté ni fournisseur (règle du RUNBOOK).
- Quantités du complexe : « 2 mmol (0.533 g) » de Cd(CH3COO)2·2H2O et « 4 mmol of diethylthiourea (0.529 g) ». Valeur en mmol extraite, masse laissée dans la citation (une seule valeur par réactif). Lecture cohérente : 0,533 g correspond à 2 mmol du dihydrate.
- Pureté et fournisseur : la phrase « All the reagents and solvents used were of analytical grades and used without further purification. » (2.1) couvre explicitement tous les réactifs ; pureté = « analytical grade » avec cette phrase en `supplier_quote`, fournisseur déclaré non cité. Appliqué au méthanol et au toluène aussi, qui sont des solvants de la synthèse.
- Méthanol et toluène des nanoparticules : « an excess of methanol » et « redispersed in toluene » n'ont pas de quantité ; `amount` déclaré non cité.
- Étape de cristallisation du complexe : « left to evaporate slowly at room temperature » + « obtained after few days » en `value_text` (température et durée), jamais en nombre.
- Étape 4 du complexe (filtration) : l'article ne dit pas si c'est à chaud ; laissé non cité plutôt que supposé.
- Étape 3 des nanoparticules : « heated to 150°C and stabilized at this temperature for 1 h » vient après la chute de 20–30 °C ; la chute est portée en paramètre `temperature_drop` (valeur textuelle) de l'étape d'injection, avec sa phrase.
- Contradiction interne : « hexagonal phase » mais pics indexés 111, 200, 220, 311, 331 (indices de la blende cubique). Phase « hexagonal » retenue comme écrite, doute ouvert.
- « trinoctylphosphine » : orthographe conservée telle quelle, doute signalé (probablement trioctylphosphine).
- Angle C–S–Cd : 111,59(8)° dans le texte contre 115,59(8)° dans la Table 2 ; sans lien avec la synthèse, aucune valeur extraite, doute ouvert pour mémoire.
- Résultats du complexe : seules des valeurs de synthèse et de caractérisation à effet direct sont gardées en outcomes (système cristallin, groupe d'espace, paramètre a, fusion 145 °C, endotherme 182 °C, perte de masse 71 %, carbone trouvé). Les distances et angles des Tables 2 et 3 ne sont pas repris : ils ne servent pas à refaire le matériau.
- Résidu ATG « calculated for CdS (3.68 mg) ... expected (3.65 mg) » : non extrait en outcome, ambigu sur ce qui est « calculated » et « expected » ; résumé seulement dans la caractérisation ATG.
- Figures : aucune ouverte. Tous les résultats comparables (420 nm, 559 nm, 2θ, 5–19 nm, courbes ATG) sont écrits dans le texte. Aucune annexe n'est citée dans l'article.
- Échantillons sans voie dans l'inventaire : la diéthylthiourée libre (comparée en IR, non synthétisée) et le CdS massif de référence.
- `method_sources` vide : les renvois [[B..]] du texte portent sur le contexte, la cristallographie (SAINT, SHELX) ou la thermolyse de complexes voisins, pas sur la préparation décrite ici.
