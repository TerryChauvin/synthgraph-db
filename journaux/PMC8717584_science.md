# PMC8717584 — critique scientifique (journal de décisions)

- Cu–TiO2/GO, « probleme » sur le GO absent : la section « Synthesis of the Cu–TiO2/GO Composite » ne cite ni GO ni suspension, alors que les trois autres protocoles en ont une. J'ai jugé ce manque bloquant pour la reproduction (le meilleur catalyseur), d'où `non_reproductible`.
- ATG « graphene content 13.5 % » jugée non probante : la méthode dit « nitrogen environment » jusqu'à 1000 °C, donc le carbone ne brûle pas. Calcul : 15 mg de GO sur 166,6 mg de TiO2 font au plus 8,2 %, donc 13,5 % est au-dessus du maximum.
- TiO2 témoin, « probleme » sur la BET : 6/(3,89 × 6,55 nm) = 235 m2/g contre 9,82 m2/g mesurés (diamètre équivalent de 157 nm). J'ai retenu Wahi et al. 2006 (même chimie, alcoxyde de Ti dans l'éthanol aqueux à moins de 200 °C, jusqu'à 250 m2/g) plutôt que l'article du Beilstein J. Nanotechnol. 2017 (hydrothermal en présence de silanes, moins proche).
- Masse volumique de l'anatase (3,89 g/cm3) recalculée à partir des paramètres de maille (a = 3,785 Å, c = 9,514 Å, Z = 4) plutôt que cherchée sur le web.
- Bande interdite de 2,11 eV (Cu) mise en « probleme », pas en « reserve » : les auteurs fondent leur conclusion (« optical band gap was the key ») sur cette grandeur. Or la mesure se fait sur une suspension en cuve, avec CuO et GO qui absorbent, et la série 0,5/1/2 % n'est pas monotone (3,10/2,11/2,85 eV).
- Comparaison Ag/Pd/Cu vue comme un témoin qui change plusieurs variables (contrôle 5) : la voie Cu se fait à pH 12, sans citrate, avec NaBH4/métal = 3 au lieu de 1, et sans GO écrit.
- Origine de l'éthanol mise en « probleme », sur la voie de base TiO2/GO (vaut pour toutes les voies) : aucun témoin sans CO2 ni au 13CO2, poudres préparées dans l'éthanol et non lavées. Source : Yui et al. 2011 (adsorbats organiques sur TiO2 comme source de carbone), DOI lu dans la notice ACS.
- Contrôle de cohérence par la XRF (tableau S1) : Ti = 48,8 % pour Cu contre 58,8 % pour Ag, et « autres » 9,4 % contre 0,5 %. J'y vois le sodium du NaOH non lavé, en « reserve » faute de dosage de Na séparé.
- XPS : écarts spin–orbite recalculés (Ag 7,2 eV contre 6,00 ; Pd 2,3 contre 5,26 ; Cu 18,8 contre 19,8). Sources : la base NIST SRD 20 pour Ag et Cu (entrée Fuggle 1977) et la fiche Thermo Fisher pour Pd. J'ai mis « reserve » et non « probleme », parce que la conclusion qualitative (Pd0 + PdO, CuO) reste plausible.
- PdCl2 : seule une compilation secondaire (ChemicalBook) a été trouvée pour l'insolubilité dans l'eau ; c'est déclaré dans `sources_not_found`.
- Pression en autoclave : Antoine de l'éthanol (NIST) à 453,15 K → 18,4 bar ; l'eau à 180 °C (10,0 bar) prise comme valeur de table sans recherche.
- GO : rapports de Hummers recalculés (KMnO4/graphite 3,65 contre 3,0). L'explication « MnO2 soluble en acide » a été jugée fausse mais sans effet sur le protocole (« reserve »).
- « 3.8 g » contre 3,8 mg de nitrate de cuivre : tranché par le calcul (3,8 mg → Cu/Ti = 1,00 %), en accord avec le doute de l'extracteur.
- Recherches web : 5 requêtes de recherche et 1 lecture de page (NIST, éthanol). Rien n'a été ajouté à fondateurs.md ni à constantes.md (Crossref bloqué).
