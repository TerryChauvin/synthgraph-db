# Journal d'extraction PMC9713890

- Deux voies seulement : la synthèse de Fe-HA à partir de cendres (voie de base `FeHA_coal_ash`) et la bandelette de papier (voie `device` `FeHA_test_strip`). L'article ne balaie aucun paramètre de synthèse, donc aucune branche.
- La fabrication de la bandelette (« The stock solution of Fe-HA NPs (3 mM)… », « A sheet of filter paper was cut into 2 × 1 pieces… », « When the filter paper dried… ») est une voie `device` à part ; le Fe-HA y entre comme réactif `intermediate`. Les tests (étalonnage, sélectivité, pH, eaux réelles) sont des résultats de cette voie, pas des branches.
- Contradiction : « synthesized by a facile method at room temperature » contre « stirred at 60 °C for 1 h ». Les 60 °C sont extraits pour l'étape de lixiviation ; la température des autres étapes est déclarée non citée (doute).
- NaOH est listé dans « Materials » mais son usage n'est pas décrit ; je ne l'ai pas ajouté comme réactif (non cité dans le protocole), doute écrit.
- Pureté/fournisseur : « analytical grades purchased from Sigma-Aldrich » est attribué à NaH2PO4 (nommé dans la phrase). Pour l'eau, la phrase « All solutions were supplied by deionized water from a Milli-Q Plus system (Millipore) » est prise comme couvrant l'eau de dispersion ; fournisseur recopié « Millipore » (le contrôle refuse la parenthèse). HCl et cendre : non cités.
- La cendre de charbon n'a ni pureté ni fournisseur (« received from the power plant ») : déclaré non cité, composition en `missing_fields`.
- Table 2 : rangées sans première cellule (« | 10 | … ») attribuées à l'échantillon du dessus (robinet ou rivière) par la structure du tableau ; la citation ne contient pas le nom de l'eau, d'où le doute.
- Figures lues (Fig. 4A, 4B, 4C, avec la légende comme citation) : intensité aux 5 concentrations 15 à 130 ppm, ΔI de H2S (≈ 60) et plage des interférents (≈ 2 à 5), ΔI de pH 4 à 10. Les deux points proches de 0 ppm de la Fig. 4A n'ont pas été extraits (attribution incertaine : légende à six concentrations, sept points).
- Équation d'étalonnage « y = 0.8406x + 42.309, R² = 0.9909 » : imprimée dans la figure 4A (et le graphique de résumé), pas dans le texte ; extraite en `value_text` avec `from_figure`.
- Fig. 1 (SEM, EDS, DRX), Fig. 2 (XPS) et Fig. 3 : les valeurs numériques utiles sont déjà dans le texte ; XPS : Fe 2p à 707/720,6 eV dans le texte contre ≈ 708/721 eV sur la figure ; texte conservé, point mis en doute.
- Plage DRX : texte « 20 and 60° », figure tracée jusqu'à 90° ; texte retenu.
- `method_sources` vide : les renvois (ref41 structure de HA, ref42 JCPDS, ref43–46 attributions XPS/FTIR, ref47 interprétation du pH) sont du contexte ou de l'interprétation, aucun ne fournit un protocole.
- Aucune annexe : l'article ne renvoie à aucun Supporting Information.
- Échantillons sans voie dans l'inventaire : cendre (matière première), eaux dopées, interférents (réactifs d'essai).
- Mécanisme : aucun mécanisme de formation écrit par les auteurs au-delà de « to precipitate out the cations » ; `mecanisme_auteurs` cite cette phrase, `mecanisme_analyse` propose la précipitation de l'apatite en signalant le Fe/Ca = 0,57 anormalement élevé pour un dopage.
