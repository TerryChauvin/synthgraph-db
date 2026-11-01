# Relecture du palier 1 (publications 1 à 50)

Relecture faite par l'orchestrateur le 2026-10-12, après `audit.py 1`.

## Bilan

- 50 publications, 465 voies (78 de base, 387 branches), 5 330 citations.
- Citations : 100 % retrouvées mot pour mot dans le texte des articles (contrôle automatique), et chaque valeur numérique apparaît dans sa citation.
- 0 anomalie bloquante. 5 avertissements, tous examinés et acceptés (ci-dessous).
- Tous les doutes des extracteurs (environ 280) ont été tranchés en relisant le passage concerné.

## Relectures intégrales

| Lot | Articles | Valeurs contrôlées | Valeurs corrigées |
|---|---|---|---|
| Calibrage (publications 1 à 10) | 10 | 561 | 9 (1,6 %) |
| Échantillon 1 sur 5 (publications 11 à 50) | 10 | 746 | 1 (0,13 %) |

Erreurs du calibrage, toutes devenues des règles de `RUNBOOK.md` :
- pureté et fournisseur sans citation propre → champ `supplier_quote` et contrôle bloquant ;
- libellé de variation ajoutant des mots absents de l'article (« more layers ») → `value_text` reprend les mots de la citation ;
- une branche mêlant deux observations distinctes (température de croissance et température du substrat) → une branche = une condition ;
- branches créées pour les bornes d'une plage, et branches héritant à tort d'une valeur du parent quand l'article ne donne qu'une plage → règle des criblages par plages.

Erreur de l'échantillon : un rapport masse/volume nommé `molar_ratio` (PMC3833323), renommé.

## Échantillon de 30 valeurs du rapport d'audit

Les 30 lignes de `palier_001.md` ont été relues : dans les 30 cas la citation contient la valeur, pour la bonne étape et la bonne voie. 0 erreur.

## Contrôle de stœchiométrie et de cohérence chimique (5 voies)

| Voie | Contrôle | Verdict |
|---|---|---|
| PMC6199062 Sb2S3-150 | 2 mmol SbCl3 + 3 mmol L-cystéine → Sb:S = 2:3 | conforme à Sb2S3 |
| PMC6631201 MnO2NFs | 1 mmol KMnO4 + 1,5 mmol MnSO4 → 2 MnO4⁻ + 3 Mn²⁺ → 5 MnO2 | stœchiométrie exacte |
| PMC7578857 CsPbBr3 | 0,1 mmol PbBr2 + 0,1 mmol CsBr → Cs:Pb = 1:1 | conforme ; le dopage Nd (0,15 mmol pour x = 7,2 %) est incohérent chez les auteurs, signalé |
| PMC5309769 MAPbBr3 | 0,16 mmol MABr + 0,2 mmol PbBr2 (MA:Pb = 0,8) | conforme au protocole LARP cité par les auteurs |
| PMC6994313 Zn-MOF | 0,120 mmol nitrate de zinc + 0,120 mmol ligand → 1:1 | plausible ; formule du MOF non donnée par l'article |

Atmosphères vérifiées contre l'état d'oxydation visé : Na3V2(PO4)3 calciné sous argon (V³⁺), ZnSe sélénié sous vide, LiCoO2 recuit sous air (Co³⁺), SiC et V2C traités sous argon : cohérent partout.

Incohérences qui viennent des articles eux-mêmes, conservées telles quelles et signalées dans les doutes : rapport Ca/P de PMC6928996, masses de nanotubes de PMC9300655, « 0.2 g » de NrGO de PMC6631201, rapport Na2O/SiO2 de 3.0 de PMC6025012.

## Avertissements acceptés

- PMC11231976 (4 avertissements) : 230 °C dans la section de préchauffage d'une pyrolyse par pulvérisation, au-dessus du point d'ébullition de l'eau. C'est le principe du procédé (vaporisation des gouttelettes), pas une erreur.
- PMC10529665 : deux branches aux conditions identiques. L'article donne bien deux rangées identiques dans son tableau 1, avec deux diamètres mesurés différents.

## Corrections apportées aux contrôles pendant l'audit

Le premier passage donnait 37 avertissements, dont 32 faux positifs du script, corrigés dans `audit.py` et `load.py` :
- unités « minutes », « hr », « mTorr », « °C·min–1 » non reconnues ;
- paramètres dont le nom contient « rate » (concentration, débit) traités à tort comme des vitesses de chauffe ;
- comparaison au point d'ébullition du solvant appliquée à des pyrolyses à plus de 350 °C ;
- seuil de 100 °C appliqué aux recuits doux de films ;
- « FA » de FAPbBr3 lu comme du fluor ; cystéine non reconnue comme source de soufre.

Les 50 extractions ont été rechargées après ces corrections (`reload_all.py`), puis l'audit relancé.

## Limites constatées sur ce palier

- 123 voies sur 465 n'ont pas de méthode propre (branches héritant de leur parent) : normal.
- 289 voies sans formule chimique du matériau (composites, MOF sans formule, membranes) : le bilan d'éléments n'y est pas applicable.
- Un seul article (PMC9026548, membranes MOF/polymère) pèse 79 voies : ce sont les cases de trois tableaux de formulation, avec pour seul résultat une appréciation visuelle (++/+/−) dont la légende n'est pas dans le texte converti.
- Le Supporting Information n'est pas lu : plusieurs articles y renvoient leurs quantités exactes.

---

# Second audit du palier 1, après format 2 et critiques (2026-10-13)

Les 50 publications ont été remises au format 2 (grille de reproductibilité, annexes, sources de méthode, dispositifs, mécanisme, sécurité), puis soumises à une critique de fidélité et à une critique scientifique, et corrigées. `audit.py 1` relancé ensuite.

## Bilan

- 50 publications, 609 voies (124 de base, 485 branches), 8 712 citations, toutes retrouvées mot pour mot.
- 0 anomalie bloquante, 0 avertissement ouvert (7 acceptés, ci-dessous). 0 doute ouvert.
- Critiques de fidélité : 526 constats, soit 473 corrigés, 39 rejetés texte à l'appui, 14 acceptés.
- Critiques scientifiques : 284 voies jugées ; 205 annotations `limite_reproductibilite` en base.

## Constats de fidélité par gravité

| Gravité | Nombre |
|---|---|
| faux | 29 |
| attribution | 51 |
| déduit | 88 |
| non cité à tort | 22 |
| manquant | 107 |
| mineur | 229 |

Les erreurs dominantes ne sont pas des chiffres mal recopiés mais des valeurs rangées sur la mauvaise voie, des étapes héritées du parent sans que l'article le dise, des branches ou résultats oubliés, et des références de contexte prises pour des sources de méthode. Chaque type est devenu une règle de `PROMPT_MISE_A_NIVEAU.md` et `PROMPT_CORRECTION.md`.

## Relectures de l'orchestrateur

- Relecture intégrale de PMC6199062 refaite au format 2 : 66 valeurs, 0 fausse.
- Lectures de figures et de tableaux d'annexe faites par l'orchestrateur sur image, marquées `from_figure` : PMC5309769 (tableau S1), PMC11231976 (Fig. S4), PMC6025012 (Fig. 5, 7, 10, précision ±3 mg/g), PMC10131834 (Fig. S1).
- Échantillon de 30 valeurs du rapport : 30 correctes. Une vérifiée dans le texte (PMC10529665 Alg/CS_0rpm, fondée par le tableau 2) ; une soutenue indirectement (PMC5977331 ZnO-MCM-0, réactif absent déduit de « without salicylaldimine modification »).

## Stœchiométrie (5 voies)

| Voie | Contrôle | Verdict |
|---|---|---|
| PMC6199062 Sb2S3-150 | 2 mmol SbCl3 + 3 mmol L-cystéine | Sb:S = 2:3, conforme |
| PMC7352182 Cu-MOF | 0,7248 g Cu(NO3)2·3H2O (3,00 mmol) + 0,4242 g H3BTC (2,02 mmol) | Cu:BTC = 3:2, conforme à Cu3(BTC)2 |
| PMC10906077 FAPbBr3 | 15 mmol d'acétate de formamidinium = 1,563 g | 104,2 g/mol, conforme (104,11) |
| PMC6297875 Na3V2(PO4)3 | NH4VO3 et NaH2PO4, V:Na = 2:3 | Na:V:P = 3:2:3, conforme |
| PMC7578857 CsPbBr3:Nd | 0,1 mmol PbBr2 + 0,1 mmol CsBr ; 0,15 mmol NdBr3 pour x = 7,2 % | Cs:Pb conforme ; dopage nominal très supérieur au dopage annoncé, signalé |

## Sources du critique scientifique

- `sources_check.py --palier 1 10` : 397 sources distinctes, 10 tirées au hasard, 8 DOI confirmés par Crossref (titre et année), 2 pages web.
- Pages ouvertes à la main : Wikipedia « Calcium hydroxide » (1,89 g/L à 0 °C : exact), nextsds 2-méthylimidazole (classement reprotoxique 1B : exact). Vérifiées plus tôt dans le palier : arXiv 2106.07366 et DOI 10.7536/PC200625.
- 0 source inventée.

## Contrôle croisé (`compare.py`)

- CsPbBr3 (3 publications) : précipitation à température ambiante, injection à chaud en flux, dopage Nd ; méthodes différentes, aucun résultat aberrant.
- Nanoparticules d'argent (3) : bande plasmon entre 420 et 455 nm, cohérent.
- MoS2 (2) : CVD à 850 °C (MoCl5) contre 750 °C (MoO3) ; mobilité 0,003–0,03 contre 42 cm2/V·s sur h-BN : écart attendu (substrat, contacts), pas une anomalie.
- ZnO (3) : voies hydrothermale et par précipitation, sans valeur isolée.

## Avertissements acceptés

- PMC7352182 (3) : le cuivre de CuS vient du réactif intermédiaire Cu-MOF, sans formule dans l'article.
- PMC9048217 (2) : témoins ZIF-8 et Ag/AgCl dont l'article ne décrit pas la préparation.
- PMC5122874 : faux positif, durées « 10 min » et « 10 hours ».
- PMC7601971 : unité « t cm−2 » gardée telle qu'écrite.

## Corrections des outils pendant ce second audit

- `audit.py` : une valeur marquée `from_figure` n'a pas à figurer dans sa citation (la légende), même règle que `load.py` ; 77 faux bloquants supprimés.
- `sections.py` : un renvoi groupé (« 27,28 », « 5–8 ») marque maintenant toutes ses références dans `corpus/refs` ; références régénérées.
- `critic_load.py`, `clore.ps1`, `relabel.py` : voie renommée ou supprimée après la critique scientifique.
- `load.py` : rôle `intermediate` dispensé de pureté et de fournisseur.

## Limites

- Les ajouts des agents de correction ont leurs citations vérifiées par script, mais n'ont été relus contre le texte que par échantillon.
- PMC9026548 : tableau S1 (quantités) absent du dépôt open access.
- 6 articles sans aucun renvoi bibliographique marqué dans `corpus/refs` (cause non examinée).
- `compare.py` cherche par sous-chaîne : « Ag » ramène des voies hors sujet.
- Les valeurs lues sur figure par l'orchestrateur ont une précision de lecture, pas celle d'un tableau.
