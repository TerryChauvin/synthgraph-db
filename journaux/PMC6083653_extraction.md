# Journal d'extraction PMC6083653

- Voie de base = L1 (rapport de charge 1 : 0,5), choisie parce que c'est le premier rapport listé dans « w/w = 1 : 0.5, 1 : 1, 1 : 2, 1 : 3 » et l'échantillon central de l'article (seul à émettre fortement à l'état solide). Le protocole unique de « Preparation of carbon quantum dots » donne les étapes de toutes les voies.
- L2, L3, L4 sont des branches de L1 avec une seule variation, sur le réactif « triethylenediamine hexahydrate » (`value_text` en rapport de charge), car les masses d'amine ne sont pas données (seulement les rapports massiques avec 2 g d'acide phtalique) : `amount_text` = « feed ratio of 1 : 0.5 », aucune masse calculée.
- L1-2 et L2-2 : variation de durée du chauffage (étape 2, 2 min contre 60 s), rattachées à L1 et L2 respectivement. L'article ne dit pas que dialyse et lyophilisation ont été identiques ; héritage accepté parce que seul « the reaction time was increased » est mentionné, signalé en doute.
- Ordre de « respectively » : QY 15,8 / 16,1 % attribués à L1 puis L2 (la phrase dit « the prepared CQDs » sans les nommer), diamètres 3,5 ± 0,7 / 3,7 ± 0,8 nm, d-spacing 0,34 / 0,21 nm, excitation 430 / 454 nm, CIE, maxima SSF 542 / 520 nm : tous attribués dans l'ordre L1, L2 donné par la phrase.
- Contradiction texte / figure 6b : le texte donne un pic SSF de L2 à 520 nm, la figure le montre vers 545 nm ; valeur du texte extraite, désaccord en doute.
- Contradiction texte / figure 5c,d sur les équations d'ajustement en pH (signe du terme linéaire, 1317 contre 1373, −157,6 contre −175,6, plage 3–6 contre 4–7) : texte retenu, doute.
- Attribution des plans (100) à 0,34 nm et (002) à 0,21 nm contraire à l'usage : seules les distances sont extraites, doute.
- Figures lues : seule la Fig. 6b (intensités de pic SSF L1 ≈ 8400, L2 ≈ 170, panneau « Em 365 nm »), parce que le texte dit seulement « very weak » pour L2. Fig. 1b non extraite (échelles différentes, intensités non comparables), Fig. 5 déjà couverte par le texte. Panneaux « Em 460 nm » ignorés (étiquettes ambiguës).
- Résultats communs à L1 et L2 (gamme de taille 2–6 nm, pic d'émission 480–510 nm, solubilité, Δλem = 10 nm) : une annotation `tendance_observee` plutôt qu'une valeur par voie ; la gamme 480–510 nm figure tout de même en caractérisation PL.
- Tests du matériau fini (pH, cytotoxicité, imagerie, SSF en KBr et gel d'agarose) rangés en `outcomes` de la voie concernée, pas en branches. L'effet « tous les gels d'agarose émettent » est noté sur L1 à L4 car la phrase dit « all of them ».
- « KBr tablets only L1 strong » noté sur L1 seulement ; pour L2 à L4 écrire « pas forte » serait une déduction.
- Échantillons sans voie : tablettes KBr et gels d'agarose (protocole non décrit), étalon sulfate de quinine.
- Annexes S1 à S7 et tableau S1 absents du fichier texte : annotation `limite_reproductibilite` « Annexe absente du dépôt ». Aucune concentration de CQDs pour les tests cellulaires.
- `method_sources` vide : aucun renvoi bibliographique dans la section expérimentale (vérifié dans corpus/refs).
- Rôles : acide phtalique `carbon_source` (« as carbon source »), triéthylènediamine `precursor` (les auteurs la nomment « passivant »).
