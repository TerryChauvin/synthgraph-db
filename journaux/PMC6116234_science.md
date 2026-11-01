# PMC6116234 — critique scientifique (journal de décisions)

- **Problème 1 (solubilité)** : 0,2 mg/1 mL = 0,2 g/L ; solubilité du PbI2 de 0,76 g/L à 20 °C (CRC via PubChem) et 4,1 g/L à 100 °C (ChemicalBook, secondaire). La solution est à 5 % de saturation à chaud : « oversaturated » est impossible tel qu'écrit. Classé `probleme` et non `reserve`, car même avec un facteur 2 d'erreur sur la valeur à chaud la conclusion tient.
- L'hypothèse « 0,2 g » est donnée comme piste (suspension, sursaturation de 5,4 au refroidissement), mais pas retenue comme correction : on ne répare pas la donnée.
- **Problème 2 (XRD « 10 nm »)** : Scherrer avec K = 0,9 et L = 10 nm donne 0,80° de largeur à 13,9° ; les raies de la figure 2a sont lues bien plus fines (< 0,3°). Lecture visuelle sur la figure, d'où une formulation prudente (« vraisemblablement »). La géométrie θ–2θ sur des plaquettes orientées mesure bien l'épaisseur : l'argument tient.
- Bragg : les pics à 13,9° et 28,17° tombent plus près de (002)/(004) que de (110)/(220), avec des paramètres de Stoumpos 2013 cités de mémoire (article non ouvert, signalé dans `sources_not_found`). Classé `reserve` seulement : le décalage d'échantillon peut expliquer 0,1–0,3°.
- La TEM de la figure 3a (plaquette « 10 nm » totalement opaque) est rapprochée du problème XRD, mais laissée en `reserve` : jugement qualitatif, sans calcul de libre parcours.
- Zone [011] déduite de (200) et (02¯2) en I4/mcm : pointée comme incohérence d'orientation possible, mais la plaquette a pu être inclinée sur la grille ; `reserve`.
- Pb 4f : un écart de 5,5 eV contre 4,87 eV (Thermo Fisher) ; la figure 3e montre environ 143,8 eV, donc faute de frappe probable ; `reserve`, attribuée aux auteurs.
- C1s du méthylammonium vers 286 eV : aucune source trouvée en une recherche ; laissé en `reserve`, signalé « de mémoire ».
- Cinétique : la source RSC Adv 2020 (≥ 125 min à 100 °C et 9 Torr pour 225 nm de PbI2) sert à dire que 5–30 min est court pour des plaquettes épaisses. Les pressions diffèrent (< 1 Torr ici), d'où `reserve` et non `probleme`.
- Chute de PL × 30 : Beer-Lambert avec α ≈ 1–1,5 × 10^5 cm−1 en explique 21 à 24. Valeur de α prise comme ordre de grandeur (De Wolf 2014, figure non relue) ; jugé `ok`.
- Décalage de PL : la coupure nette vers 775–780 nm sur la figure 2b (filtre probable) et la réabsorption sont proposées comme explications concurrentes de l'« expansion de réseau ».
- « Single unit cell (2 nm) » contre une maille d'environ 1,3 nm (Liu et al. 2016, même groupe) : le lien vient de l'abstract ACS lu dans la recherche ; auteurs abrégés « Liu J., Xue Y. et al. ».
- PDMS : pas de point de fusion (élastomère réticulé) ; il aurait aussi supporté les 180 °C de la méthode antérieure, donc l'avantage « bas point de fusion » n'est pas démontré. Noté sans source web (chimie générale).
- Témoin « CH3NH3I insuffisant » : trois variables confondues (quantité, durée, épaisseur) → verdict `invérifiable`, `non_reproductible`.
- Ha et al. 2014 (facteur 1,81) cité via la revue PMC6199035, article non ouvert.
- Mécanisme jugé `a_revoir` : l'annotation de l'extraction attribue la cristallisation au refroidissement seul ; à 0,2 g/L, c'est l'évaporation de la goutte qui crée la sursaturation.
- 7 recherches web ; Crossref inaccessible : aucun DOI vérifié, rien ajouté à fondateurs.md ni à constantes.md.
