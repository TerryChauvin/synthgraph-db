# Journal d'extraction PMC9049756

- Voie de base : Cs3BiBr6_NC (Méthodes « Heating-up synthesis of Cs3BiBr6 perovskite NCs », 160 °C, 60 min, 1,5 mL d'OA), car c'est le seul protocole décrit en entier ; toutes les autres conditions en sont des branches.
- Cs3Bi2Br9_NP : branche de la base avec « 15 mL of OA, 1.5 mL of OM, and 7.5 mL of ODE ». Les volumes sont lus comme des totaux (et non ajoutés à ceux de la base) à cause de « from 1.5 mL to 15 mL » dans les Résultats ; « same conditions » accepté comme héritage des étapes ; doute écrit. Seules l'OA et l'ODE varient (OM identique, pas de variation).
- BiOBr_NP : branche avec ses propres étapes, car la température (135 °C) et la purification (toluène/méthanol, hexane) diffèrent de la base malgré « All reactants and processes were the same ... except that CsBr was absent ». Variation CsBr = absent + température de l'étape 3.
- Le 135 °C des Résultats (« in the presence of 1.5 mL of OA ») n'indique pas si CsBr est présent ; la Fig. S3 est rattachée à la préparation sans CsBr des Méthodes (doute). Fiche JCPDS 73-0348 (texte) contre 78-0348 (étiquette de la Fig. 3) : valeur du texte.
- Contradiction à 160 °C (« Up to ... 160 °C BiOBr predominantly » contre « Cs3BiBr6 predominantly formed at 160 °C ») et à 170 °C (Fig. S4 contre aliquote de 60 min de la Fig. 3) : deux phrases extraites telles quelles, doutes écrits.
- T170 : une seule voie pour l'échantillon de la Fig. S4 (légende : « 170 oC for 1 h ») et l'aliquote de 60 min de la Fig. 3 (même température, même durée que la base), avec deux résultats distincts nommés selon leur source.
- Série en durée à 170 °C : branches de T170 pour 15, 30, 90 et 120 min. 15 et 90 min ont leur valeur dans le texte ; 30 et 120 min seulement dans les étiquettes de la Fig. 3 (`from_figure`, légende en citation). Le texte ne dit pas quels temps sont « early stages » : BiOBr majoritaire attribué à 15 min seulement ; 30 et 120 min décrits à partir de la figure (qualitatif, positions 2θ à ± 1°).
- Les aliquotes n'ont pas d'étapes de refroidissement/purification décrites : héritage de T170 accepté pour comparer la durée, signalé en doute.
- T200 (légende Fig. S5 : 200 °C, 1 h, 1.5 mL OA) et Bi_noCsBr_above180C (« above 180 °C ») : branches créées car ce sont des conditions explicitement citées ; la deuxième n'a qu'une étape de chauffage avec température en value_text (seuil, pas de valeur).
- « up to 300 °C » : borne de plage sans valeur intermédiaire, aucune branche (échantillon sans voie dans l'inventaire).
- Stoich_CsBr : rapport Cs/Bi « stoichiometric » non chiffré, branche de la base avec variation en value_text et succeeded false (BiOBr reste produit final) ; conditions non précisées.
- NP_100C_30min : légende Fig. S6 (100 °C, 30 min, 15 mL OA). Une seule étape propre car le dégazage à 105 °C du protocole hérité est incompatible avec 100 °C et l'article ne dit rien des autres étapes.
- Table S1 : lignes recopiées telles quelles (α1+α2 ≠ 100 %, τave non recalculable) ; doute écrit, pas de correction.
- Toluène anhydre de dilution : réactif de rôle « solvent » avec quantité, pureté et fournisseur non cités (la phrase des Chemicals ne le nomme pas).
- Aucun renvoi de méthode dans les Méthodes (aucun [[cit]] dans la partie expérimentale) : method_sources vide.
- Annexe : le fichier texte contient le SI (légendes S1–S6 et Table S1) ; les images S1–S6 ne sont pas dans le dépôt, signalé en limite_reproductibilite.
