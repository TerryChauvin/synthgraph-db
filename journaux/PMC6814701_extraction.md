# Journal d'extraction PMC6814701

- Trois voies : `Mt_extract` (intermédiaire, macération de l'écorce), `AuMt1` (voie de base) et `AuMt2` (branche). L'extrait est préparé par les auteurs et réutilisé comme réducteur : voie `intermediate`, et réactif de rôle `intermediate` dans AuMt1. Ce n'est pas un bioprocédé (aucune optimisation de culture).
- Quantités de AuMt1 et AuMt2 : les volumes de HAuCl4 0,01 M, d'extrait et d'eau ne sont que dans le tableau S1 de l'annexe, écrit avec des virgules décimales (« 3,2 », « 1,20 », « 2,8 »). Lecture 3,2 / 1,6 / 1,2 mL et 1,6 / 1,6 / 2,8 mL, validée par la somme de 6 mL et par 0,01 × 3,2/6 = 5,3 mM et 0,01 × 1,6/6 = 2,6 mM.
- Concentrations de précurseur (5,3 et 2,6 mM) mises en paramètre de l'étape 1 et en variation d'AuMt2, parce que les auteurs raisonnent en concentration ; les deux volumes (HAuCl4, eau) sont aussi en variations, car ce sont eux qui changent réellement.
- Contradiction : extrait à 32,5 mg/mL dans les Méthodes contre 121,8 mg/mL dans l'en-tête du tableau S1. Je garde 32,5 mg/mL en résultat de `Mt_extract` (texte principal) et signale l'autre dans un doute et dans `limite_reproductibilite`.
- Durée de réaction avant lavage : l'article ne la donne pas (« within a few minutes » ne décrit que le changement de couleur ; 60 et 120 s sont le maximum d'absorbance en cuve) : déclarée `not_stated`, pas déduite.
- Lavages : « repeating the process twice » ne dit pas si la centrifugation est refaite. Étape à l'eau avec `repetitions` = « twice » en texte, étape éthanol avec `repetitions` non citée, puis centrifugation finale en étape distincte.
- XRD, HRTEM et EDS (Fig. 6) sont attribués à « AuMt » sans numéro : rattachés à AuMt1 avec un doute, sans valeur numérique propre à un échantillon.
- Potentiels zêta du tableau 1 : la rangée écrit « − 35.3 » avec une espace, donc `value_text` plutôt que `value_num` (le contrôle exige le nombre signé tel quel).
- K de la dégradation du bleu de méthylène : « 8.24 × 10−3s » (AuMt1) et « 3.54 × 10−3/s » (AuMt2) en `value_text` (le contrôle numérique ne reconnaît pas ces écritures) ; le tableau 2 (0,4944 et 0,2124 min−1) recoupe les valeurs en s−1.
- Figures lues : Fig. 7a/7b (viabilité MTT à 25, 50, 100, 200 μg/mL, 24 et 48 h, 16 valeurs, précision environ ±3 points) car le texte ne donne que des fourchettes ; Fig. 12b et 12e (dégradation finale). Écart signalé : texte « almost 30% » contre ≈ 36 % lus pour AuMt1 à 48 h et 50 μg/mL.
- Fig. 5c/f : distributions de taille non relues, car le texte donne déjà 40 et 150 nm.
- Tests biologiques et catalytiques rangés en résultats des voies AuMt1 et AuMt2, pas en branches ; aucune voie `device`.
- `method_sources` : seuls les renvois de protocole de mesure (DPPH CR40–41, polyphénols CR42–43, MTT CR46–47) sont retenus, rôle `autre` ; ImageJ, Henry, Smoluchowski, Boltzmann sont des outils d'analyse, exclus.
- Témoins sans voie : vitamine C, catéchines (témoins du test DPPH) et cellules HUVEC non traitées.
- Annexe absente : figures S1 à S7 seulement par légende ; annotation `limite_reproductibilite` correspondante.
