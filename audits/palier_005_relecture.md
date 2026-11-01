# Relecture du palier 5 (publications 201 à 250)

Session cloud des 15 au 17 octobre 2026, avec 3 agents en parallèle (4 au début) selon le plan du 2026-10-14. Le palier a été interrompu par trois limites d'usage de 5 h (15/10 vers 2 h 20, 6 h 30 et 14 h 05) et par une pause demandée par l'utilisateur le 15/10 à 16 h 50, reprise le 17/10 à 3 h 18.

## Bilan

- **Volume :** 50 publications closes, soit 466 voies (132 de base, 334 branches), 9 581 citations vérifiées, toutes exactes (100 %), 4 017 résultats et 2 997 cases déclarées non citées. La complétude moyenne est de 0,73.
- **Licences :** 40 CC BY, 5 CC BY-NC, 5 CC BY-NC-ND.
- **Audit :** `audit.py 5` donne 0 bloquant. Les 35 avertissements sont tous des faux positifs ou des limites de l'article, acceptés un par un (voir plus bas) : 0 ouvert.
- **Relectures intégrales :** 9 publications, 1 112 valeurs contrôlées, 0 fausse.
- **Échantillon de 30 valeurs du rapport d'audit :** 0 erreur.
- **Coût :** médiane de 0,66 M jetons par publication (moyenne 0,64 M, total 32,1 M pour les 50), hors orchestrateur. Médianes par passe : extraction 158 k, critique de fidélité 153 k, critique scientifique 177 k, correction 145 k.

## Relectures intégrales

| Publication | Valeurs contrôlées | Fausses |
|---|---|---|
| PMC9908928 | 53 | 0 |
| PMC5793645 | 73 | 0 |
| PMC9464223 | 124 | 0 |
| PMC10077552 | 160 | 0 |
| PMC11891312 | 172 | 0 |
| PMC6837232 | 73 | 0 |
| PMC11269599 | 115 | 0 |
| PMC7550332 | 231 | 0 |
| PMC10386591 | 111 | 0 |

PMC10386591 : la Fig. 7 (pH et élimination du colorant) a été relue sur l'image : 28, 47, 89, 61 et 59 % sont justes.

## Critiques : constats et comparaison avec les paliers précédents

| | Palier 1 | Palier 2 | Palier 3 | Palier 4 | Palier 5 |
|---|---|---|---|---|---|
| Constats de fidélité | 526 | 403 | 435 | 406 | 428 |
| Médiane par publication | 10 | 8 | 8,5 | 8 | 8 (de 4 à 15) |
| Constats « faux » | 29 | 7 | 5 | 7 | 4 |

Répartition des 428 constats : `mineur` 181, `manquant` 140, `deduit` 70, `non_cite_a_tort` 17, `attribution` 16, `faux` 4.

Sur les 428 constats : 410 corrigés, 14 rejetés, 4 acceptés sans changement de valeur.

Les 4 constats « faux » :
- **PMC8621345 :** le résultat TEM de CoFe2O4-0.5 avait recopié « quasi sphériques facettées » des autres échantillons. L'article dit « more pronounced spherical-like aspect », 3–4 nm, cristallinité plus faible. Corrigé d'après le texte.
- **PMC9667963 :** la solution de HCl de 100 mL portait la pureté du HCl commercial (36 wt%). L'article utilise une solution 1 M. Corrigé.
- **PMC8838941 :** B43 et B44 étaient rangés en `method_sources`, alors que ce sont des renvois de contexte (« In our previous works »). Retirés.
- **PMC9908928 :** une seconde population de diffusion dynamique (1500–3000 nm) rangée à tort. Corrigée.

Aucun des « faux » n'est un nombre mal recopié du texte. Trois sont des erreurs de rattachement ou de rôle, une est une pureté mal reprise.

Les 14 rejets (motifs) :
- paramètres de synthèse lus seulement sur un schéma de figure : règle de la grille du RUNBOOK, ils restent `not_stated` (PMC11269599, 3 constats) ;
- héritage justifié par une phrase générale des Méthodes ou par la règle « analogously » (PMC6273754, 2 constats ; PMC6955683) ;
- renvoi de contexte et non source de méthode (PMC9908928, PMC10870712, 2 constats) ;
- valeur non rattachable sans deviner : nombres d'annexe sans étiquette, « r-GO » non défini, recuit illisible (PMC10870712, PMC9865864, PMC8474143) ;
- hors périmètre : RMN des produits de la réaction catalytique (PMC11883551) ;
- phrase « analytical grade » qui couvre HCl (PMC5793645) ; mélanges listés sans résultat (PMC7254336).

Les 4 constats acceptés sans changement : les deux contradictions texte contre figure de PMC13257848 (butachlor et anilofos inversés sur la Fig. 3 ; l'article se contredit), PMC5465224 et PMC9063869 (valeurs du texte gardées, limite en annotation).

**Critique scientifique :**
- 299 jugements de voie : 140 cohérentes, 125 douteuses, 28 invérifiables, 6 incohérentes ;
- 1 338 contrôles : 253 `ok`, 832 `reserve`, 253 `probleme` ;
- aucun `probleme` n'a changé une valeur. Ceux qui viennent des articles sont devenus des annotations `limite_reproductibilite` (voir les journaux `journaux/<PMCID>_correction.md`).

Exemples de problèmes venant des articles, tous consignés en annotation : teneur en cobalt de 0,065 mol/g plus lourde que le cobalt pur (PMC10169762) ; laser « HeNe » à 532 nm (PMC8125317) ; dispersion aqueuse « à 350 °C » et DCO initiale 45 à 70 fois trop haute (PMC10386591) ; écarts types 10 fois trop petits sur 10 larves × 5 répétitions (PMC6297187) ; sursaturation des herbicides, qui mêle précipitation et adsorption (PMC13257848) ; énergie d'activation recalculée à ≈ 43 kJ/mol au lieu de 17 (PMC5101912).

## Avertissements de l'audit acceptés (35)

Tous vérifiés dans le texte.
- **PMC8149873, 2 avertissements :** 3LCVO-SSR et 0LCVO-SSR n'ont pas de protocole dans l'article (renvoi à une référence). Sources de Li et V absentes, déclarées `not_stated`, annotées.
- **PMC12311843, 1 avertissement :** FP(B/I)@S n'ajoute que le TEOS ; Pb, Br, I viennent des réactifs de la voie parente.
- **PMC7550332, 10 avertissements :** Co et Fe viennent du réactif « mixed Co-Fe oleate », dont l'article ne donne pas la formule. L'heuristique ne lit pas les éléments d'un nom sans formule.
- **22 faux positifs de l'heuristique « température au-dessus de l'ébullition du solvant » :**
  - **PMC9667963, 16 avertissements :** cristallisation en autoclave en Téflon déclaré à l'étape précédente (même récipient, conditions statiques) ou gel en autoclave.
  - **PMC11243152 :** évaporation du sol à 200 °C sur plaque, l'étape le décrit.
  - **PMC4585659 :** traitement à la vapeur d'eau.
  - **PMC8474143, 3 avertissements :** hydrosilylation à 150 °C sous argon sur ligne de Schlenk.
  - **PMC9063653 :** cuisson d'un film à 300 °C après évaporation du solvant.
  - **Cause commune :** l'heuristique ne rattache pas les récipients clos de l'étape précédente.

## Échantillon de 30 valeurs du rapport d'audit

J'ai relu les 30 lignes de `palier_005.md` : dans les 30 cas, la citation soutient la valeur pour la bonne étape et la bonne voie : 0 erreur.

Points particuliers :
- **PMC9814928 (4 lignes de la Table S2 et S12) :** les rangées aplaties du tableau se lisent par l'en-tête (« [Zn2+] Conc. | [2-MIM] Conc. | Reaction Time ») : ZIF-8 10 nm = 0,06 M de Zn, ZIF-8 30 nm = 1 M de 2-MIM, ZIF-67 30 nm (a) = 0,008 M de Co. Conformes.
- **PMC9865864 :** les 2,16 mg cm−2 sont ceux de l'électrode de carbone activé (positive), les 0,8 mg cm−2 ceux de CDs-r-GO-6 (négative). Conforme.
- **PMC10077552 Co/SBA-16 :** la citation ne dit pas « sans nitrate de nickel », mais montre que le catalyseur Co/SBA-16 seul existe et ne réagit pas. Elle reste faible mais exacte.

## Stœchiométrie et cohérence chimique (5 voies recalculées)

| Voie | Contrôle | Verdict |
|---|---|---|
| PMC10386591 ZnS | 11,358 g de Zn(NO3)2·6H2O = 0,0382 mol, soit 0,382 M dans 100 mL (article : 0,4 M) ; Na2S 3,122 g = 0,0400 mol anhydre, 0,400 M ; Zn:S = 0,95 | cohérent à 5 % près ; 0,4 M de Na2S ne vaut que pour le sel anhydre (annoté) |
| PMC8621345 CoFe2O4 | Fe(NO3)3·9H2O 8,08 g = 20,0 mmol ; Co(NO3)2·6H2O 2,91 g = 10,0 mmol ; Fe:Co = 2,000 | conforme à CoFe2O4 |
| PMC9099495 TiO2 | TiCl4 5 mL (d = 1,726) = 45,5 mmol ; éthanol 50 mL = 856 mmol ; rapport 1/18,8 | contredit le « 1/10 » du résumé (rapport de volumes) ; annoté |
| PMC13257848 ZIF-8@TPPa | PA 13,4 mg = 0,124 mmol ; TP 17,4 mg = 0,0828 mmol ; PA:TP = 1,50 | conforme à la stœchiométrie 3:2 de la condensation |
| PMC8125317 ZnO | Zn(NO3)2 0,05 M, urée 0,25 M, soit 1:5 ; calcination 300/500/700 °C à l'air | conforme à la voie urée → hydroxycarbonate → ZnO |

## Contrôle croisé (`compare.py`)

- **CoFe2O4 :** 7 voies de base. Les tailles de cristallites sont du même ordre (≈ 5 à 6 nm pour PMC8621345 et PMC3088885) quelle que soit la voie (coprécipitation à 80 °C, sol-gel puis 400 °C, solvothermal à 140 °C). Aucun écart.
- **ZIF-8 :** 14 voies de base, de natures très différentes (microémulsion, gabarit PCTE, eau). Pas de contradiction ; surfaces BET élevées pour les synthèses en phase liquide.
- **ZnO :** 30 voies de base (hydrothermal, précipitation, urée). Les tailles et phases (wurtzite) concordent avec la méthode.

## Sources du critique scientifique

Crossref est bloqué depuis le cloud. Les 176 DOI du palier sont listés dans `palier_005_doi_a_verifier.txt`, à vérifier depuis le PC (`python -I sources_check.py --palier 5 10`). Les agents ont signalé dans leurs rapports les DOI qu'ils n'ont pas pu confirmer (par exemple 10.1021/ac0702084, 10.1016/j.molliq.2018.10.048, 10.1039/c6nr00156d). Plusieurs sources sont des pages web (NIST, CAMEO, ASTM par ricochet, Wikipédia) citées par URL et marquées comme secondaires par les agents.

## Défauts d'outil et de consigne trouvés pendant le palier

- **`sections.py` (corrigé le 15/10 puis le 17/10) :**
  - il ne rendait pas les `table-wrap` rangés dans `<back>` (vu sur PMC10386591). Corrigé, textes complétés pour 10 articles ;
  - le texte de PMC9181868 avait gardé les légendes des Tables 1 à 6 sans leurs rangées. Les rangées ont été insérées le 17/10 et un scan de tout le corpus (rangées du XML absentes du texte) n'a trouvé aucun autre cas.
- **Compléments d'extraction pour 4 publications closes** (PMC6631201 palier 1, PMC9866506 palier 2, PMC9181868 palier 3, PMC7285084 palier 4) : +14, +30, +103 et +21 valeurs ajoutées d'après les tableaux, 3 branches nouvelles pour PMC7285084, 0 valeur existante supprimée (`diff_valeurs.py`), citations toutes exactes. Journaux `journaux/<PMCID>_complement.md`.
- **Contradictions des articles révélées par ces compléments** (valeurs gardées, doutes ouverts) : PMC6631201 recouvrements 96,2–105,6 % (texte) contre 94,9/96,2 et 105,6/104,9 % (tableau) ; PMC7285084 5 mol % de TBAB (texte) contre 2 mol % (note du Table 1) ; PMC9866506 tailles de pores au Table 2 alors que le texte dit « nonporous ».
- **Règle ajoutée à `PROMPT_CORRECTION.md` (erreur vue deux fois : PMC12312155 et PMC9464223) :** `value_text` ne contient que des mots de l'article, jamais de note d'attribution ni de préfixe commentaire. Une attribution incertaine se consigne dans un doute et une annotation.
- **Agent de correction hors périmètre :** un agent a lancé `load.py load` (PMC10077337), sans conséquence puisque la clôture recharge.
- **Piste non réalisée :** rattacher aux étapes les récipients clos de l'étape précédente dans `audit.py`, pour supprimer 22 faux positifs de température sans toucher au contrôle.

## Consommation et limites d'usage

Trois limites de session de 5 h sont tombées pendant le palier (≈ 8 à 10 M jetons d'agents par fenêtre, soit 13 à 14 publications). La limite hebdomadaire n'a pas été atteinte. Le palier 5 a coûté 32,1 M jetons d'agents en tout.
