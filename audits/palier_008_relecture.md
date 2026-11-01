# Relecture du palier 8 (publications 351 à 400)

Sessions cloud du 18 octobre (11 publications) et du 22 octobre 2026 (39 publications), 3 agents en parallèle, période autorisée jusqu'au 22/10 à 10 h Paris. Pipeline habituel : extraction → chargement → critique de fidélité → critique scientifique → correction → clôture. Une limite d'usage vers 00 h 20 UTC le 22/10 (réinitialisation à 03 h), reprise des 3 agents coupés par SendMessage.

## Bilan

- **Volume :** 50 publications closes, 515 voies, 9 859 citations vérifiées, toutes exactes ; 887 résultats lus sur figure.
- **Audit :** `audit.py 8` donne 0 bloquant et 0 avertissement ouvert. Les 134 avertissements sont des faux positifs du contrôle chimique ou des limites de l'article déjà annotées, acceptés un par un (voir plus bas).
- **Relectures intégrales :** 8 publications, 1 181 valeurs contrôlées, 1 fausse (PMC5535248), corrigée et rechargée. Faites par agents Sonnet en lecture seule.
- **Critique de fidélité :** 437 constats (médiane 9 par publication, de 3 à 14) : 434 corrigés, 3 rejetés avec raison. Par nature : 195 mineurs, 124 manquants, 70 déduits (héritage non fondé), 19 attributions, 18 non cités à tort, 11 faux (2,5 %).
- **Critique scientifique :** 293 jugements de voie (144 douteuses, 106 cohérentes, 28 invérifiables, 15 incohérentes) ; 1 307 contrôles : 247 ok, 790 réserves, 270 problèmes. Tous les problèmes viennent de l'article et sont rangés en annotations `limite_reproductibilite`, jamais en correction de valeur.
- **Coût :** médiane de 0,67 M jetons par publication (moyenne 0,70 M, total 35,1 M pour les 50), hors orchestrateur. Médianes par passe : extraction 169 k, critique de fidélité 156 k, critique scientifique 194 k, correction 150 k. Relecture intégrale : ≈ 75 k jetons par publication relue.

## Relectures intégrales (agents Sonnet, lecture seule)

| Publication | Valeurs contrôlées | Fausses |
|---|---|---|
| PMC10342722 | 111 | 0 |
| PMC5535248 | 130 | 1 |
| PMC9082527 | 188 | 0 |
| PMC5680254 | 93 | 0 |
| PMC13057244 | 116 | 0 |
| PMC9696917 | 118 | 0 |
| PMC5304159 | 67 | 0 |
| PMC9080687 | 358 | 0 |

- **PMC5535248 :** `OPL-C500`, rapport IG/ID lu sur la Fig. 4 : 1,3 extrait, ≈ 1,24 sur l'image (vérifié par l'orchestrateur), donc 1,2 à deux chiffres significatifs. Corrigé, rechargé, statuts des critiques conservés.
- Points signalés, non comptés comme erreurs : lectures de figure à la limite de l'arrondi (OPL-C900 1,0 contre ≈ 1,05 ; M1 120 contre ≈ 124 mAh/g dans PMC13057244 ; deux barres de PMC9696917 à ±0,5) ; attribution de l'IPCE 83,9 % de PMC9080687 (Fig. S10 qui ne couvre que les dispositifs MAPbI3), déjà en doute ; contradictions de l'article recopiées fidèlement (650/600 °C dans PMC9082527 ; durées M1/M2 permutées entre texte et Tableau S1 dans PMC13057244 ; 25/30 wt% dans PMC9080687).

## Échantillon de 30 valeurs du rapport d'audit

30 lignes relues (citation contre valeur, étape et branche) : 29 sans réserve, 1 remarque, aucune fausse.

- PMC11197484 `PeLED_optimized` étape 7 `atmosphere` = « O2 plasma » : c'est un traitement de surface plus qu'une atmosphère ; la citation le soutient (5 s pour le film de TFB, distinct des 2 min du substrat).
- Rangées multiples vérifiées dans le texte : épaisseurs « 50, 1, and 100 nm, respectively » (TPBi, LiF, Al) bien rattachées ; « below 10 °C », « once more », « six equal portions », « vigorous stirring » gardés en `value_text`.

## Stœchiométrie et cohérence (5 voies, par la critique scientifique, calculs recontrôlés)

| Voie | Contrôle | Résultat |
|---|---|---|
| PMC7352254 GO | 18,0 g KMnO4 = 0,114 mol ; 3,5 g C = 0,291 mol ; KMnO4/C = 0,39 mol/mol, 5,1 en masse ; H2O2 1,5 mL à 30 % insuffisant pour réduire tout le Mn(VII) restant | conforme à Marcano en milieu, rapport plus fort ; limites annotées |
| PMC10653075 Cs-oleate_0.5M | 1,63 g Cs2CO3 = 5,00 mmol (Cs 10,0 mmol) ; acide oléique 57–63 mmol ; C ≈ 0,48–0,50 M | cohérent avec les 0,5 M annoncés |
| PMC13057244 Spent_CAM | Tableau 1 : Li/(Ni+Mn+Co) = 0,93 (0,78 à 1,07 avec l'incertitude) ; Ni:Mn:Co = 0,65:0,20:0,15 contre NMC622 0,6:0,2:0,2 | déficit de Li annoncé compatible ; Co déficitaire, annoté |
| PMC6447565 CuFe2O4@HNTs | Fe:Cu = 2,04 ; NaOH 12,5 mmol (×2,7 l'excès) ; ≈ 24 % en masse de CuFe2O4 → 7–11 emu/g attendus | aimantation de 30 emu/g incompatible, annotée |
| PMC13516552 Poly-CoPc | CoCl2:ODPA:NH4Cl:urée = 2:1:6:12 → 1 Co par unité phtalique (0,25 attendu) | cobalt en excès ×4 ou ordre inversé, annoté ; rendement 89 % rapporté à l'ODPA seulement |

Aucune de ces anomalies n'est une erreur d'extraction : les citations sont conformes ; chaque incohérence est gardée littérale, avec un doute et une annotation `limite_reproductibilite`.

## Anomalies de l'audit (134 avertissements, tous acceptés)

- **Éléments du produit sans source parmi les réactifs (104) :** faux positifs du contrôle chimique. Élément apporté par une voie intermédiaire (Cs-oléate de PMC10653075, 46 ; Imide_mixed de PMC8307816, 17 ; gel MW_gel de PMC9778285, 6 ; régénération de PMC10411504, 1) ; carbone de biomasse (PMC5535248, 13) ; matière active usagée sans réactif (PMC13057244, 13) ; abréviations lues comme formules (DPPA de PMC11197484, 6 ; MWNT de PMC5515720 ; PI de PMC9412554).
- **Matériau non oxyde chauffé à l'air au-delà de 400 °C (21) :** SiC chauffé à 650 °C à l'air pour brûler le carbone non réagi (PMC13209189, 20 voies) ; pyrolyse de la mélamine à l'air pour g-C3N4 (PMC6409917). Méthodes standards, citations exactes.
- **Température au-dessus de l'ébullition du solvant (7) :** autoclave cité ailleurs dans les Méthodes (PMC6237675) ; poudres sèches sous argon (PMC13209189) ; autocombustion d'un gel (PMC9082527) ; recuit d'un film de PEDOT:PSS (PMC11197484) ; solution aqueuse « à 200 °C » en flacons ouverts (PMC9782101), contradiction de l'article déjà en doute et en `limite_reproductibilite`.
- **Branches identiques (1) :** V-Mo-MCM-41(85/39/31) de PMC10835253 : l'article ne donne pas les masses de sels par échantillon ; résultats distincts.
- **Unité non reconnue (1) :** `℃` (caractère Unicode de l'article, PMC10540474), valeur exacte.

## Constats récurrents du palier (déjà couverts par RUNBOOK.md et PROMPT_CORRECTION.md)

- **Héritage non fondé** (70 constats « déduit ») : corrigé en `not_stated` avec doute.
- **Tests du matériau fini rangés en branches** : PMC10368083 (41 branches de tests catalytiques) renvoyé à l'extracteur avant chargement et restructuré en résultats (RUNBOOK, ligne 44).
- **Renvois de mesure pris pour des sources de méthode** : rejetés à la correction faute de formule de renvoi (PMC8401075 ; règle du 13/10).
- **Constat de critique à deux passages** (`article_says` avec deux extraits séparés par « // ») : `critic_load.py` le refuse ; réduit au premier passage (PMC6409917).

## Sources à vérifier depuis le PC

Crossref reste bloqué depuis le cloud. Les 259 DOI cités par les critiques scientifiques (50 publications) sont dans `audits/palier_008_doi_a_verifier.txt`, un par publication, dédoublonnés.

## Branches `verif` et `docs`

Aucun commit nouveau à fusionner au moment de l'audit.

## Règles ajoutées à RUNBOOK.md

Aucune. Les erreurs vues (héritage non fondé, tests rangés en branches, renvois de mesure en sources de méthode, lecture de figure arrondie au-delà de la précision) sont déjà des règles.
