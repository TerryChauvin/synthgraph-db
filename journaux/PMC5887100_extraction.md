# Journal d'extraction PMC5887100 (points de carbone amphiphiles à partir de HATU)

- Découpage : voie de base `ACD-HATU` (HATU, toluène, 150 °C, 8 h) ; 5 branches « solvant » (eau, éthanol, acétonitrile, DMF, pyridine) par variation sur le réactif `toluene` (« replaced by ») ; 3 branches « précurseur » (DIPA, BTEAC, BI) par variation sur le réactif `HATU` ; une branche dopée à l'Al.
- Dopant : variation nommée `dopant` avec `parent_value: none` (règle du RUNBOOK pour un ajout) ; le contrôle donne un avertissement attendu, le nom n'existant pas dans le parent.
- Héritage : « same reaction conditions » (précurseurs) et « prepared in the same way » (dopage) fondent l'héritage ; pour les solvants l'article dit seulement « replaced toluene with other solvents », héritage accepté et consigné en doute.
- Fournisseurs : une phrase unique liste cinq sociétés pour tous les réactifs, sans attribution ; purétés extraites (écrites à côté de chaque nom, phrase en `supplier_quote`), fournisseur déclaré `not_stated`.
- Eau solvant de la branche `water` : pureté et fournisseur non cités (l'eau déionisée de la section Chemicals n'est pas liée explicitement à ce solvant) ; en revanche l'eau déionisée de la dispersion aqueuse est citée explicitement.
- Phrase « respectively » des rendements quantiques (« ∼7%, ∼2%, ∼20% and ∼2% prepared from water, ethanol, acetonitrile and DMF ») : ordre écrit avant attribution : eau 7, éthanol 2, acétonitrile 20, DMF 2. Émissions : « 470 nm, 510 nm, 475 nm, 530 nm and 520 nm » = toluène, eau, éthanol, acétonitrile, DMF.
- Contradiction sur l'agrégation (DMF et pyridine selon le paragraphe) : dispersion du DMF non extraite, doute ; autres solvants pris dans la phrase la plus détaillée.
- Rendements quantiques des trois précurseurs de comparaison : seulement une plage de groupe (0,6–1,7 %) ; pas de valeur recopiée sur chaque voie, annotation `tendance_observee`.
- Figures lues : Fig. 2a (angles dièdres DIPA 62°, BTEAC 81°, BI 52°, étiquettes exactes de la figure, citation = légende) ; Fig. 4b (classe modale 1,6–2 nm, ≈ 35 points sur 100). Fig. 2b lue qualitativement (ordre des intensités C–N : BTEAC > DIPA > BI > HATU), consigné en annotation sans valeur chiffrée. Fig. 3 et 5 ouvertes : rien de plus à extraire.
- Dispersion aqueuse (congélation-séchage, sonication, centrifugation) : voie `post_treatment` séparée parce que l'article lui rattache les essais cellulaires ; origine de la mère liquide non précisée (doute).
- Durée de vie « 2 ns pour les ACD non dopés » rattachée à la voie de base (échantillon non nommé, doute) ; EDS « obtained from toluene » sur la base.
- Échantillons sans voie : HATU seul (réactif commercial) et « autres ions métalliques » (non nommés).
- Annexe : le fichier SI ne contient que des légendes ; annotation « Annexe absente du dépôt » pour Table S2, Fig. S4, S10, S12a.
- Bioprocédé : sans objet. Aucun renvoi de méthode (`method_sources` vide) : les références de la partie calcul (B3LYP, base 6-311++G, AIMAll) sont des références théoriques ou logicielles, non retenues.
