# Test de 10 publications, palier 2 (2026-10-13, session cloud)

Test demandé par l'utilisateur avant de lancer le palier 2. Les consignes révisées sont appliquées : inventaire des échantillons, lecture des figures, autocontrôle, bloc `calculs`, bibliothèque `references/` et correction ciblée.

## Résultat en bref

1. Les 10 publications sont closes : extraction, chargement, deux critiques, correction et clôture. Cela fait 133 voies, aucune erreur au `load.py check`, aucun doute ouvert et `critic_pending` vide.
2. Constats de fidélité : **médiane 5 par publication**, contre 10 au palier 1, pour un total de 52. Il y a **3 « faux »**, contre 29 sur 526 au palier 1, et aucun ne porte sur une valeur de l'article : ce sont deux annotations et un renvoi de méthode.
3. Jetons : **≈ 0,67 M par publication**, contre ≈ 0,9 M au palier 1, soit −25 %. Ce chiffre ne compte pas l'orchestrateur.
4. Figures : 68 valeurs lues sur figure (`from_figure`) dans 6 publications. Le critique de fidélité les a toutes relues, et aucune ne s'écarte de plus de 10 %.
5. Contrôle scientifique : 71 points `probleme`, tous venant des articles, devenus des annotations `limite_reproductibilite`. Aucune valeur n'a été modifiée. J'ai recompté un bloc `calculs` par publication (10 sur 10), et tous sont exacts.

## Constats de fidélité par publication et par gravité

| Publication | Voies | faux | attribution | déduit | non cité à tort | manquant | mineur | Total | dont « sure » | rejetés |
|---|---|---|---|---|---|---|---|---|---|---|
| PMC5466191 | 64 | 0 | 0 | 2 | 0 | 1 | 5 | 8 | 1 | 0 |
| PMC6409700 | 10 | 1 | 0 | 2 | 0 | 0 | 2 | 5 | 1 | 0 |
| PMC9366981 | 14 | 0 | 0 | 2 | 0 | 0 | 5 | 7 | 2 | 2 |
| PMC9866506 | 11 | 0 | 0 | 0 | 0 | 1 | 5 | 6 | 0 | 1 |
| PMC3088885 | 7 | 0 | 1 | 0 | 1 | 0 | 2 | 4 | 2 | 0 |
| PMC6678425 | 5 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 |
| PMC7996286 | 4 | 0 | 0 | 1 | 0 | 0 | 4 | 5 | 0 | 0 |
| PMC10405785 | 6 | 1 | 0 | 1 | 0 | 0 | 1 | 3 | 0 | 0 |
| PMC7033158 | 4 | 1 | 0 | 0 | 0 | 3 | 1 | 5 | 3 | 0 |
| PMC5521283 | 8 | 0 | 0 | 0 | 0 | 1 | 5 | 6 | 1 | 1 |
| **Total test** | 133 | **3** | **1** | **8** | **1** | **6** | **33** | **52** | 10 | 4 |
| Palier 1 (50 publ.) | 609 | 29 | 51 | 88 | 22 | 107 | 229 | 526 | | 39 |

Répartition rapportée à 10 publications : palier 1 → 5,8 faux, 10,2 attributions, 17,6 déduits, 21,4 manquants. Test → 3 faux, 1 attribution, 8 déduits, 6 manquants. La baisse la plus nette porte sur les attributions (rangées de tableau, « respectively »). Avant chaque critique, l'orchestrateur a vérifié rangée par rangée les tableaux de 8 publications, sans trouver d'erreur.

Prudence sur la comparaison : au palier 1, les critiques portaient surtout sur des **mises à niveau** d'extractions au format 1. Ici, ce sont des extractions neuves faites directement au format 2. Les deux échantillons ne sont donc pas strictement comparables.

Ce qui reste, par ordre d'importance :

- **« déduit »** (8) : des branches qui héritent du protocole du parent sans que l'article le dise (séries de température en annexe, points de vérification d'un plan d'expériences, témoins). Les voies sont gardées, et le doute de chacune dit maintenant que l'héritage n'est pas écrit.
- **« manquant »** (6) : des conditions d'essais préliminaires, une étape de séchage citée seulement dans une variation, les niveaux d'un plan CRCD.
- **« faux »** (3) : une annotation de comparaison (PMC7033158), et deux renvois de contexte pris pour des sources de méthode (PMC6409700, PMC10405785). La règle 6 existe déjà ; elle n'est pas encore assez appliquée par l'extracteur.

## Critique scientifique

| Publication | Points `probleme` | Nature dominante |
|---|---|---|
| PMC7033158 | 13 | Surfaces BET et volumes poreux impossibles (4V/S = 0,26 nm contre 2,9 nm), NaBH4 qui donne du Fe0 et non Fe2O3, raies DRX attribuées à Ag qui ne sont pas celles de Ag |
| PMC9866506 | 14 | BET sur isothermes de type III, attributions XPS, nombres de Li faux, équation déséquilibrée |
| PMC7996286 | 11 | Distances d qui ne suivent pas Bragg (8,61 Å recalculés contre 10,40), méthionine au-dessus de sa solubilité, Freundlich incohérent |
| PMC9366981 | 7 | Modèle statistique non refaisable, prédictions de la Table 4 qui ne découlent pas des équations, incohérence 21,94 % contre 0,198 mg |
| PMC5466191 | 6 | Unités d'activité incompatibles, plasmon à 550 nm incompatible avec 22–39 nm |
| PMC6409700 | 6 | Pics d'émission Br/I plus bleus que la formule nominale (iodure incomplet) |
| PMC6678425 | 5 | Quantité de NaOH non définie, pH mesuré incompatible avec 2–6 M, sécurité de l'autoclave |
| PMC10405785 | 5 | O/C = 0,85 incompatible avec du « graphène monocouche », témoin qui change trois variables |
| PMC3088885 | 3 | Ms ramenée à la ferrite = 1 à 7 % du massif, Hc trop faible |
| PMC5521283 | 1 | Baisse de gap attribuée à tort à un effet de taille quantique |

Médiane : 6 points par publication. Recomptés par l'orchestrateur, un par publication : moles et Ms de PMC3088885, masses de sels de PMC6409700, 21,94 % de 1 mg et UI de PMC9366981, Li par FeVO4 de PMC9866506, pH et [OH⁻] de PMC6678425, Bragg de PMC7996286, O/C de PMC10405785, 4V/S et surface de l'Ag de PMC7033158, indices de Cauchy de PMC5521283, facteur 7,0 de PMC5466191. Tous sont justes.

## Jetons par passe (valeurs `subagent_tokens`, `audits/jetons.csv`)

| Passe | Modèle | Moyenne test | Plage | Palier 1 |
|---|---|---|---|---|
| Extraction | Sonnet high | 199 k | 170–287 k | ≈ 280 k (mise à niveau) |
| Critique de fidélité | Sonnet high | 155 k | 130–230 k | 210–290 k |
| Critique scientifique | Opus high | 185 k | 151–211 k | ≈ 190 k |
| Correction | Sonnet high | 132 k | 115–153 k | 160–240 k |
| **Total par publication** | | **≈ 672 k** | 571–879 k | **≈ 900 k** |

La plus chère est PMC5466191, avec 64 voies, à 879 k. Les gains viennent de la critique de fidélité (consigne « review.py seulement ») et de la correction ciblée ; la critique scientifique reste au même niveau. Extrapolation à 440 publications restantes : ≈ 300 M de jetons hors orchestrateur, contre ≈ 400 M estimés après le palier 1.

## Valeurs lues sur figure

- 68 valeurs `from_figure` dans 6 publications : PMC7996286 (22), PMC5521283 (13), PMC5466191 (10), PMC9866506 (9), PMC7033158 (9), PMC10405785 (4) et PMC3088885 (1).
- 3 publications n'en ont aucune, parce que leurs figures ne répètent que le texte ou n'ont pas d'échelle (PMC6409700, PMC9366981, PMC6678425).
- Toutes les valeurs ont été relues sur l'image par le critique de fidélité : aucun écart ne dépasse 10 %, et le plus grand est d'environ 3 %.
- Les lectures ont aussi fait apparaître des contradictions entre texte et figure. Ce sont des légendes de panneaux inversées (PMC3088885, PMC9866506), une bande G à 1548 cm-1 dans le texte contre ≈ 1585 sur la figure, et une transmittance de 80 % dans le texte contre 66 % sur la figure. Elles sont gardées en doutes.

## Annexes absentes

| Publication | Ce qui manque |
|---|---|
| PMC9866506 | Fig. S1, S2, S4, et **Tableaux 1 et 2 absents du texte** (aucun bloc `[TABLE]`) |
| PMC9366981 | Images des Fig. S1–S3 (seules les légendes sont dans le texte) |
| PMC10405785 | Images des Fig. S1–S4 (Table S1 présente, aplatie) |
| PMC5466191 | Annexe `mmc1.docx` lue, mais sa colonne « Sample number » est vide : les 32 essais sont numérotés par l'ordre des lignes, ce que le critique a confirmé en recalculant l'équation de l'article |

Les 6 autres publications ne renvoient à aucune annexe.

## Ce qui n'a pas marché ou a dû être corrigé

1. **Crossref bloqué** (proxy 403) : ni `sources_check.py` ni `references/verif_doi.py` ne tournent. Aucune source n'a été ajoutée à `fondateurs.md`, alors que Zhao 1998 (10.1021/ja974025i) y est attendu à sa deuxième citation. Les **64 DOI** cités par les critiques scientifiques restent à vérifier depuis le PC (`sources_check.py --palier 2`) ; liste ci-dessous.
2. **Un critique de fidélité a lancé `critic_load.py`**, qui écrit en base, contrairement à la consigne. Je l'ai relancé moi-même et le résultat est identique. Les prompts suivants l'interdisent explicitement (« review.py seulement ») ; à reporter dans `CRITIQUE.md`.
3. **Rôle manquant** : l'eau d'hydrolyse d'un alcoxyde avait été rangée en `reducing_agent`. Le rôle `hydrolysis_agent` est maintenant ajouté au RUNBOOK.
4. **`diff_valeurs.py`** avait un chemin de git propre à Windows. Il est maintenant portable, sans changement de contrôle.
5. **Question de périmètre (PMC5466191)** : environ 50 voies sur 64 décrivent l'optimisation de la culture de la laccase (criblages, 32 essais factoriels, doses gamma), et non un matériau. Le critique juge le choix défendable mais pose la question. **Décision de l'utilisateur à prendre** : garder ces voies de bioprocédé dans la base de matériaux, ou ne garder que la voie intermédiaire réutilisée.
6. Le scratchpad est partagé entre agents parallèles : un fichier de travail a été écrasé, sans effet sur les résultats. À l'avenir, chaque agent devrait nommer ses fichiers avec son PMCID.
7. Relecture intégrale « 1 sur 5 » : `full_review_due` était vide pour ce lot, donc aucune relecture intégrale de l'orchestrateur. Les contrôles faits sont les doutes tranchés, les tableaux vérifiés rangée par rangée sur 8 publications et `diff_valeurs` à chaque clôture (aucune valeur perdue).

## DOI à vérifier sur Crossref (depuis le PC)

- PMC3088885 : 10.1007/s10854-019-01863-3, 10.1007/s10973-008-9687-6, 10.1016/S0304-8853(01)00151-2, 10.1063/1.1616655, 10.1103/PhysRev.99.1727
- PMC6409700 : 10.1002/adfm.201600109, 10.1002/adma.201603964, 10.1002/sdtp.12529, 10.1021/acs.nanolett.5b02404, 10.1021/acsnano.5b06295, 10.1021/acsnano.7b08357, 10.1021/jacs.7b01409, 10.1021/nl5048779, 10.1039/C9TC01130G, 10.1126/science.aag2700
- PMC9366981 : 10.1016/0021-9797(68)90272-5, 10.1021/cm9911363, 10.1021/ie50501a040, 10.1021/ja974025i, 10.1126/science.279.5350.548, 10.1515/pac-2014-1117, 10.3390/pharmaceutics10020057
- PMC6678425 : 10.1016/j.carbon.2007.02.034, 10.1103/physrevb.61.14095
- PMC10405785 : 10.1002/advs.201901316, 10.1002/chem.200802097, 10.1007/s12274-014-0644-3, 10.1021/acs.chemmater.7b04446, 10.1021/acsami.6b07807, 10.1039/D0GC00998A, 10.1063/1.2196057, 10.1351/pac-rep-10-09-31
- PMC9866506 : 10.1007/s12613-024-2845-4, 10.1016/j.apsusc.2007.09.063, 10.1016/j.elspec.2004.03.004, 10.1016/j.susc.2021.121894, 10.1021/ja01167a001, 10.1039/c3ta12821k (le plus fragile : vu seulement dans une bibliographie)
- PMC7996286 : 10.1016/j.progpolymsci.2011.06.003, 10.1016/j.watres.2017.04.014, 10.1021/ja01539a017, 10.1021/nn1006368, 10.1039/B917103G
- PMC7033158 : 10.1021/acsomega.3c01261, 10.1021/am1004943, 10.1021/ed084p322, 10.1021/es970039c
- PMC5521283 : 10.1002/jrs.1250070606, 10.1007/s10853-010-5113-0, 10.1016/S0022-3093(87)80333-2 (titre non confirmé), 10.1021/j100045a026, 10.1364/JOSA.55.001205
- PMC5466191 : 10.1007/s00253-008-1628-6, 10.1016/j.bbabio.2007.06.004, 10.1039/DF9511100055, 10.5897/AJB11.2233

## Pour décider de la suite

- Qualité : elle est au moins au niveau du palier 1, avec deux fois moins de constats et aucune valeur d'article fausse.
- Coût : environ −25 % de jetons par publication.
- Ce qui bloque le palier 2 dans le cloud : les figures des publications suivantes ne sont pas dans le dépôt (à fournir depuis le PC avec `enrich.py figs`), et Crossref est inaccessible.
