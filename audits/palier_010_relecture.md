# Relecture du palier 10 (publications 451 à 500)

Audit fait le 25/10/2026 vers 22 h UTC (cloud). Avec ce palier, la cible de **500 publications closes** est atteinte.

## Bilan

- 50 publications closes (500 au total), chacune avec ses deux critiques (fidélité et scientifique) et sa correction.
- Audit (`audit.py 10`) : 549 voies, 9 498 citations vérifiées, **0 bloquant, 0 avertissement ouvert** après traitement (41 avertissements : 2 corrigés, 39 acceptés).
- Critiques de fidélité : 446 constats, médiane 9 par publication, **11 « faux »** ; 434 corrigés, 12 rejetés par l'agent de correction (texte à l'appui).
- Jetons d'agents : 35,5 M pour le palier, soit **0,71 M par publication** (paliers 2 à 9 : 0,61 à 0,69 M). La hausse vient de 5 relectures intégrales ajoutées en fin de palier et de critiques scientifiques plus longues sur des articles riches en calculs.
- Taux d'erreur de l'échantillon de relecture intégrale : 3 valeurs fausses sur 1 222 (0,25 %).

## Relectures intégrales (agents Sonnet, lecture seule)

Le palier n'en comptait que 5 à la clôture de la dernière publication ; 5 autres ont été tirées au hasard (graine 10) pour revenir à 10, comme aux paliers précédents.

| Publication | Valeurs contrôlées | Fausses |
|---|---|---|
| PMC6278251 | 66 | 0 |
| PMC6443225 | 86 | 0 |
| PMC11194767 | 84 | 0 |
| PMC5369406 | 211 | 3 |
| PMC10725426 | 70 | 0 |
| PMC6926885 | 116 | 0 |
| PMC9080747 | 112 | 0 |
| PMC9121351 | 241 | 0 |
| PMC8348040 | 131 | 0 |
| PMC7503881 | 105 | 0 |

- PMC5369406 : trois résultats d'analyse des gaz émis (EGA) étaient rangés sur `ZG-AC` alors que la légende de la Fig. S6 les donne pour l'échantillon non lavé ; déplacés sur `ZG-AC_nowash` par l'orchestrateur, rechargés, doute tranché.
- Points signalés, non comptés comme erreurs : contradictions de l'article recopiées fidèlement (Ca 2p 347,27 eV dans le texte contre 347,4 eV sur la Fig. 5a de PMC6278251 ; 64 % des Conclusions contre 68 et 62 % des Résultats de PMC8348040 ; « jusqu'à 38 wt % » contre 36,5 % du tableau 1 de PMC9121351 ; lettre A attribuée à deux minéraux selon la figure dans PMC6926885 ; étiquette de ligne du tableau 2 de PMC9080747).

## Échantillon de 30 valeurs du rapport d'audit

30 lignes relues (citation contre valeur, étape et branche) : 30 soutenues, aucune fausse. Remarques :

- PMC6474109 `T120`, 120 °C : la citation est la légende de la Fig. 3 et la valeur est marquée `from_figure` (Fig. 3b) ; la valeur n'est écrite que sur la figure.
- PMC5369406 `ZG-SC_nowash`, « absent (precipitate not washed) » : la citation (profil TPR « without washing ») soutient l'absence de lavage, mais pas mot pour mot l'étape ; acceptable.
- PMC4725629 `Glycine_NaClO`, angle de vue de la LED de 140° : caractéristique de la lampe ajoutée par la correction, héritée par toutes les voies irradiées.

## Stœchiométrie et cohérence (5 voies)

| Voie | Contrôle | Résultat |
|---|---|---|
| PMC10262684 OctA | 72,3 mg de SnBr2 (M 278,5) = 0,26 mmol ; 140 μL d'HBr à 48 % (ρ 1,49) = 1,24 mmol ; Br/Sn ≈ 6,8 | cohérent avec le 1,2 mmol de l'article seulement à 48 % (la synthèse écrit 40 %) ; Br/Sn proche de A4SnBr6, annoté |
| PMC8717625 CsPbBr3 | 101,7 mg de Cs2CO3 (M 325,8) = 0,62 mmol de Cs dans ≈ 5,3 mL ; 0,4 mL injectés = 0,047 mmol de Cs ; 69 mg de PbBr2 (M 367,0) = 0,188 mmol | Cs limitant, Pb et Br en excès comme dans l'injection à chaud classique ; argon cohérent avec Pb(II)/Cs |
| PMC11818718 CuS | Na2S 2 M dans 25 mL = 50 mmol de S ; CuCl2 2 M dans 10 mL = 20 mmol de Cu | sulfure en excès (S/Cu 2,5), Cu(II) cohérent avec la covellite CuS, eau à température ambiante |
| PMC3414225 SiO2_CdS_8h | 1 mL de TEOS (ρ 0,933, M 208,3) = 4,5 mmol ; 0,2 mL de NH3 à 28 % = 3,0 mmol ; 25 mL d'eau = 1,39 mol (H2O/Si ≈ 310) | conditions de type Stöber, ammoniac catalytique ; cohérent |
| PMC9182795 Chi_AuNPs | 2 mL de HAuCl4 2 mM = 4 μmol d'Au (0,79 mg) ; 3 électrons par Au, soit 12 μmol d'électrons | chitosane à 0,2 % comme réducteur et stabilisant, mais volume non donné : bilan impossible à boucler (manque déjà signalé dans l'extraction) |

Aucune anomalie d'extraction. Les incohérences venant des articles (HBr 40/48 %, sels d'ammonium de PMC10262684) sont gardées littérales et annotées.

## Anomalies de l'audit (41 avertissements)

- **Corrigées (2)** : branches sans leur variation distinctive.
  - PMC11393933 : `TBA-TEOS-traceNaOH` et `TBA-TEOS-traceNaCl` ne portaient pas la nature du sel de sodium. Variation `trace sodium salt` (NaOH ou NaCl, parent « none ») ajoutée avec la citation de la ligne du tableau.
  - PMC6410306 : `ZnO_HS_300`, `_400` et `_800` portaient la même variation générique de gabarit. Variation réécrite par branche (taille de ZnO HS obtenue) et doute tranché : l'article ne dit pas quel gabarit donne quelle taille.
- **Acceptées (39), faux positifs ou lectures conformes à l'article** :
  - « BDC » lu comme du bore (PMC9121351, 17) ;
  - éléments apportés par une voie intermédiaire ou un post-traitement (hydroxyapatite calcinée de PMC8434467, PBMO-m recuit de PMC7913101, ZSM-5 calciné de PMC9418510, Cs-oléate de PMC8717625 ; 20) ;
  - basalte comme source d'Al et Si sans formule (PMC6926885) ;
  - nitrure de carbone graphitique massif obtenu sous air à 520 °C, comme l'écrit l'article (PMC4976354) ;
  - `CDs_PEI-CA` distinguée de `CDs_T1_no1_noAA` par une étape propre (PMC9080747) ;
  - éthanol simple dispersant d'un échange ionique à l'état solide, évaporé au four (PMC11393933).

## Sources citées par les critiques scientifiques

Crossref reste bloqué depuis le cloud. Les 247 DOI cités (50 publications) sont dans `audits/palier_010_doi_a_verifier.txt`, un par publication, dédoublonnés. Les DOI donnés de mémoire ou non vus par les critiques ont été remplacés par « DOI non vérifié retiré » avant le chargement (PMC10200858, PMC5551800, PMC6928214, PMC8153126) ; les corrections n'en recopient aucun.

## Contrôle croisé

`compare.py "CsPbBr3"` : 41 voies de base. Les injections à chaud de PMC8717625 (180 °C) et PMC10148794 (170 °C) sont dans la fenêtre habituelle. Les cristallites de 40 à 42 nm de PMC10383321 (recristallisation à température ambiante) sont plus gros que les nanocristaux des autres voies (5 à 15 nm), ce qui est cohérent avec la méthode. Aucune valeur aberrante non annotée.

## Constats récurrents du palier (déjà couverts par RUNBOOK.md et PROMPT_CORRECTION.md)

- **Tests du matériau fini rangés en voies** (RUNBOOK l. 44) : stabilité de PMC11393933 et PMC9858013, tissus `Fabric_*` de PMC9121351, pressage de PMC7321157, étapes de dialyse de PMC8465261. Réorganisés en résultats par la correction.
- **Héritage non fondé dans des branches** : PMC10200858, PMC4725629 (essais au chlorure et à l'hypochlorite), PMC10262684 (essais sans cristaux qui héritaient du vortex et du bain de glace).
- **Valeur déduite d'une plage et d'un ordre** : PMC8118497 (47,67 % attribué au rapport 1:1) ; passée en lecture de figure, la plage reste en doute. Premier cas observé, pas encore une règle.
- **Affirmation de produit non soutenue** : PMC4725629 (`Glycine_NaClO` marquée réussie avec des nanoparticules d'argent alors que l'article attribue la couleur à ClO−).
- **Lectures de figure trop précises** : PMC11739850 (arrondies à 2 chiffres significatifs).
- **DOI de mémoire chez les critiques scientifiques** : retirés (voir plus haut).

## Incidents d'orchestration

- Limite d'usage vers 18 h UTC (réinitialisation 18 h 50) : 3 agents coupés, repris par SendMessage à 19 h 12 ; environ 20 minutes perdues, car le redémarrage du conteneur a empêché de programmer le réveil à temps.
- Une critique de fidélité (PMC8118497) a été lancée sur une consigne absente après une erreur de syntaxe dans la commande de chargement. Elle a été arrêtée aussitôt, sans fichier écrit, puis relancée après le chargement.

## Branches `verif` et `docs`

Aucun commit nouveau à fusionner au moment de l'audit.

## Règles ajoutées à RUNBOOK.md

Aucune : les erreurs du palier relèvent de règles existantes (tests du matériau fini, héritage, valeurs déduites).
