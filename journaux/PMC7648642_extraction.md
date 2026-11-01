# Journal d'extraction PMC7648642

- Une seule voie de base (HCF) : l'article ne décrit qu'une préparation (section Synthesis). Aucune branche : pH, force ionique, temps, concentration et température (Fig. 3, 4, 5, 7) sont des conditions d'essai d'adsorption du matériau fini, donc des résultats et non des branches (règle « tests du matériau fini »).
- HST (MOF seul, « The blue powder product HST was obtained by a simple solvothermal method ») : laissé sans voie. Aucun protocole propre, et l'article ne dit pas que c'est celui de HCF sans coton ; créer une branche aurait fait hériter d'étapes non fondées. Noté dans `sample_inventory` et en doute.
- CF (coton seul) : échantillon commercial, `route: null`. Ses valeurs du tableau 1 (Qm 104,56 mg g−1) sont rangées dans une annotation `tendance_observee` (résultat de comparaison, pas une voie).
- « 0.3948 of H3BTC » : unité omise dans le texte ; `amount_text` sans unité, pas de `g` déduit (doute ouvert).
- Pureté et fournisseurs : citation continue de trois phrases des Materials (Cu nitrate / BA et H3BTC / « All reagents were of analytical grade… ») en `supplier_quote`. Éthanol : pureté « analytical grade » par la phrase générale, fournisseur non cité. Eau déionisée : ni l'un ni l'autre (non nommée dans la phrase générale).
- « hydrothermal » (mécanisme) contre « solvothermal » (Synthesis) pour le même mélange eau/éthanol : libellé « solvothermal » retenu, doute noté.
- Régénération : HNO3 0,1 mol L−1 (Résultats) contre 3 M (Méthodes). Non tranché ; protocole non extrait en étapes car test du matériau fini, valeurs de cyclage (99,11 % puis 88,24 %) en résultats de HCF.
- Tableau 1, rangée HCF : β et E tous deux 0.56, incohérent avec E = 1/√(2β) ; seul E (valeur du texte) extrait, β laissé de côté. Résultats du tableau 2 : seule la rangée T = 0.8 (celle dont le texte dit qu'elle donne le meilleur ajustement) a été extraite.
- Figures : le dossier corpus/fig/PMC7648642/ est absent du dépôt, donc aucune valeur lue sur figure ; les figures 3, 4, 7, 8 sont citées dans `limite_reproductibilite` et en doute. Pas de section Supporting Information et aucun renvoi à une annexe dans le texte.
- `method_sources` vide : les renvois du texte portent sur des modèles (Langmuir, D–R, Toth), des attributions FTIR/XPS et des comparaisons de capacité, pas sur une préparation ou un protocole à refaire.
- ATG : le résultat n'est que dans la Fig. 1A (« shown in Fig. 1A ») ; seules les conditions de mesure (30–900 ℃, 10 K/min, argon) sont extraites.
