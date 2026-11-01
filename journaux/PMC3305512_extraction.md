# Journal d'extraction PMC3305512

- Découpage : une seule série de cinq compositions Ni0.7-xZnxCu0.3Fe2O4 (x = 0 à 0,20) avec un protocole unique décrit dans « Material preparation ». Voie de base = x=0.00 (sans zinc, premier de la série) ; quatre branches x=0.05 à 0.20, héritage des huit étapes accepté sur la phrase « Nanoparticles of Ni0.7-xZnxCu0.3Fe2O4 (0.0 ≤ x ≤ 0.2, x = 0.05) were prepared by auto-combustion method ».
- Variations des branches : le zinc est un réactif ajouté (`dopant`, parent_value « none », valeur de x citée par la rangée du Tableau 1) et le nickel change (`nickel nitrate hexahydrate`, value_text « Ni0.7-x »). Les quatre avertissements du contrôle viennent du nom `dopant`, voulu par le RUNBOOK pour un réactif absent du parent.
- Quantités des précurseurs : l'article dit seulement « stoichiometric mixtures » ; `amount` déclaré non cité plutôt qu'un `amount_text` déduit de la formule.
- Pureté « 'AR' grade » : la phrase de tête de section nomme les quatre sels ; pureté recopiée pour Ni, Cu, Fe et Zn, fournisseur non cité.
- Formules « Fe(NO3)2.9H2O » et « CuCl » recopiées telles qu'écrites et signalées en doute (Fe(NO3)3 et Cu(II) seraient attendus) ; aucune correction silencieuse.
- Étape 4 : « annealed at 200°C for 24 h » classée `dry` car le produit est ensuite appelé « dried gel » ; grille d'un séchage (température, durée) au lieu de celle d'un recuit.
- Étape 6 (combustion) : aucune température ni durée dans l'article, déclarées non citées.
- Pastilles : « pressed into circular disk-shaped pellets… silver coating » traité comme voie `device` unique (Pellet_Ag_dielectric), sans résultats ; les résultats diélectriques restent sur les voies du matériau.
- Tableaux 1 à 3 : chaque rangée attribuée par la valeur de x écrite dans la première cellule, et recopiée entière en citation. Cgb en `value_text` (« 3.9E - 2 » n'est pas un nombre JSON recopiable). Tableau 2 : « Dhkl (nm) » pour une densité de 5,5 ; valeur sans unité et doute.
- Tableau 3, x = 0.00 : Cgb calculée 3.9E - 2 contre observée 4.3E - 3 avec 0.05 % d'erreur ; incohérence consignée en doute, valeurs inchangées.
- Fig. 10 : l'encart donne n ≈ 0,68–0,76 alors que le texte dit 0.073 à 0.086 ; aucune valeur de n extraite, doute posé (texte et figure se contredisent).
- Fig. 11 : seule figure lue (ε' à 5 kHz pour les cinq compositions, plus ε'' et tanδ à x = 0,10, soit 7 valeurs). La fréquence 5 kHz vient de la légende de la courbe, pas du texte. Le point de x = 0 est tracé vers −0,065 : ignoré comme position, attribué à x = 0.00 avec doute. Pas de lecture de σac (valeurs trop proches de zéro).
- Figs. 2b, 3b, 4b : la légende cite une composition « 0.5 » ; non attribuée à x=0.05 (inventaire : route null) ; MEB/MET rattachés seulement à 0.00 et 0.10.
- Fig. 1, 5, 6–9, 12 : non lues pour des valeurs (DRX, spectres, courbes) ; le Tableau 3 et le texte donnent déjà les valeurs numériques utiles.
- Pas de `method_sources` : aucun renvoi `[[B…]]` dans les Méthodes ; les renvois portent sur les équations d'analyse et le contexte.
- Mécanisme : `mecanisme_auteurs` limité à la phrase de combustion ; `mecanisme_analyse` signale l'absence de combustible organique ajouté, point que l'article ne commente pas.
