# Journal d'extraction PMC9050136

- Voie de base = (0,6:1) Fe–Mg MOF (`FeMg_0.6-1`) : c'est le premier protocole détaillé (« 1 mmol of Mg(NO3)2·6H2O, Fe(NO3)3·9H2O (0.6 mmol or 1 mmol) … ») ; (1:1), Mg-MOF et Fe-MOF en branches car l'article dit « In the same manner ».
- `FeMg_1-1` : une seule variation, la quantité de Fe(NO3)3·9H2O (0,6 → 1 mmol), lue dans « (0.6 mmol or 1 mmol) ».
- Mg-MOF et Fe-MOF : « using only Fe(NO3)3·9H2O or Mg(NO3)2·6H2O as the metal precursor » ne donne pas la quantité du métal restant. Réactif retiré = `absent` ; réactif restant = variation en `value_text` sans nombre, route déclarée `metal_precursor_amount` non cité, et doute.
- Tests du matériau fini (xanthène, adsorption, réutilisation, pH) rangés en `outcomes` des quatre voies, pas en branches (règle du RUNBOOK) ; conditions des essais dans `characterizations.conditions`.
- Tableaux 2 et 3 : l'ion n'est écrit que sur la première rangée de chaque bloc. Rangées attribuées par nom d'échantillon et position du bloc (4 rangées par ion), citation = rangée entière ; noté en doute.
- Tableau 1 contre texte sur SBET : le texte dit « Fe-MOF, Mg-MOF … 774, 983 … respectively », le tableau donne Mg-MOF 774 et Fe-MOF 983. Tableau retenu (rangée nommée).
- Cu(II) : qmax (tableau 2) 175 pour (0,6:1) et 172 pour (1:1), qe(Exp) (tableau 3) l'inverse. Recopié tel quel, doute ; pareil pour les lignes Mg-MOF Pb/Cd et Fe-MOF Cd/Cu du tableau 3, presque dupliquées.
- Constantes k2 inférieures à 1e-4 (0.000056…) mises en `value_text` : le contrôle de `value_num` ne retrouve pas « 5.6e-05 » dans « 0.000056 ».
- Fig. 7 : le point (0,6:1) se lit vers 88 % alors que le tableau 1 et le texte disent 93,5 %. Valeur du tableau gardée, figure non extraite, doute.
- Figures lues (4 séries, 8 valeurs) : Fig. 8A, essais 1 à 4 (93, 90, 85, 83 %), car le texte ne dit que « remarkably similar activity » ; Fig. 9 : Pb pH 4, Cd pH 5 et 6, Cu pH 4 (130, 56, 110, 88 mg g−1). Les valeurs écrites dans le texte restent en `value_num` avec leur phrase ; lectures à 2 chiffres, ±3 unités.
- Caption de Fig. 8 écrit « (0.61) » : citation gardée telle quelle, doute.
- Séries de temps, de dose et de concentration (Fig. S1 à S3) : images absentes du dépôt, seulement légendes et graduations dans le fichier ; non extraites, annotation « Annexe absente du dépôt : ». Le texte ne donne que 75 min, 50 mg, 150 mg L−1 (outcomes qualitatifs).
- Conditions de catalyse contradictoires : 0,05 g (section Catalytic activity) contre 0,03 g (Reusability). Rendements du tableau 1 rattachés à la première ; doute.
- Fournisseur Sigma Aldrich : la phrase de « Materials » ne vise que Mg et Fe nitrates, acide téréphtalique et DMF ; pureté non citée. Pb, Cu, Cd nitrates (BDH) et réactifs de la réaction test ne sont pas des réactifs de synthèse du MOF.
- `method_sources` : cit27 (protocole « as reported previously », rôle `protocole_adapte` car l'article réécrit le protocole) et cit28 (titrage n-butylamine). Scherrer, Langmuir, Freundlich, Weber–Morris, Boyd écartés (formules d'analyse).
- Échantillons sans voie dans l'inventaire : adsorbants et catalyseurs de la littérature (tableau 4, section réutilisation) et le xanthène produit (réaction test, pas un matériau).
- Formule du MOF laissée `null` : l'article n'en donne aucune. Mécanisme : un `mecanisme_auteurs` (Fe-MOF dispersé dans les pores puis en surface) et un `mecanisme_analyse` ; pas de `securite_auteurs`, l'article ne dit rien.
