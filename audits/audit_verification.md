# Vérification de la base : paramètres communs et contrôles internes (28/10/2026)

Suite de l'audit de contenu (`audits/audit_contenu.md`). Ici, la question n'est plus « que contient la base ? » mais « le travail d'extraction est-il bien fait, et la base est-elle utilisable pour comparer des synthèses ? ». Neuf analyses : profils de paramètres par méthode, paramètres essentiels absents, et sept contrôles internes dont une ré-extraction à l'aveugle. Tout est reproductible : `python3 -I analyses/audit_parametres.py`, `python3 -I analyses/audit_verification.py`, `python3 -I analyses/compare_blind.py` ; résultats dans `docs/audit_contenu/data/`.

Périmètre : 747 voies de base de matériau (sans parent, nature « matériau »), 3 956 branches, 12 731 paramètres d'étape, 7 714 réactifs, 39 350 résultats.

## 1. Profils de paramètres par méthode de synthèse

### 1.1 Ce que les voies d'une même méthode ont en commun

Pour chaque méthode (classement par mots-clés du champ « méthode »), la similarité des jeux de paramètres cités entre deux voies est mesurée par l'indice de Jaccard moyen (1 = mêmes types de paramètres partout).

| Méthode | Voies | Similarité | Param. / voie | Paramètres cités (part des voies) |
|---|---|---|---|---|
| hot-injection | 30 | 0,43 | 5,6 | T 90 %, durée 93 %, centrifugation 80 %, atmosphère 70 %, volume 57 % |
| reflux / chauffage en solution | 23 | 0,41 | 5,4 | T 100 %, durée 100 %, lavage 65 %, atmosphère 52 % |
| solvothermal | 44 | 0,39 | 5,3 | T 100 %, durée 100 %, lavage 61 %, répétitions 48 %, volume 27 % |
| hydrothermal | 139 | 0,38 | 5,3 | T 97 %, durée 96 %, lavage 62 %, répétitions 39 %, atmosphère 24 %, concentration 22 % |
| sol-gel | 56 | 0,37 | 5,4 | T 100 %, durée 100 %, vitesse d'addition 43 %, atmosphère 39 % |
| précipitation | 63 | 0,34 | 5,9 | durée 97 %, T 94 %, lavage 67 %, vitesse d'addition 35 % |
| réduction chimique | 32 | 0,34 | 5,3 | durée 97 %, T 88 %, concentration 41 % |
| traitement thermique | 23 | 0,31 | 4,0 | T 83 %, durée 83 %, atmosphère 52 %, rampe 35 % |
| voies vertes | 33 | 0,29 | 6,3 | T 94 %, durée 94 %, concentration 52 %, centrifugation 42 % |
| dépôt de films | 33 | 0,28 | 6,8 | durée 100 %, T 97 %, atmosphère 61 %, vitesse de spin 27 % |
| échange ionique / imprégnation | 25 | 0,27 | 4,3 | durée 80 %, T 80 %, concentration 40 % |
| mécanochimie | 21 | 0,26 | 4,6 | durée 86 %, T 81 %, atmosphère 62 %, vitesse de broyage 24 % |
| solution à température ambiante | 31 | 0,23 | 4,3 | durée 81 %, T 71 % |
| non classée | 43 | 0,19 | 4,5 | durée 74 %, T 67 % |

Lecture. Le socle commun à toutes les méthodes se réduit à la température et à la durée (cités dans 90 à 100 % des voies des méthodes principales). Au-delà, deux voies d'une même méthode ne partagent que 25 à 45 % de leurs types de paramètres. Les méthodes à protocole codifié (injection à chaud, reflux, solvothermal) sont les plus homogènes ; les méthodes « fourre-tout » (solution à température ambiante, échange ionique) et les voies non classées sont les moins homogènes. Une comparaison de synthèses au sein d'une méthode est donc possible sur la température, la durée et, pour certaines méthodes, l'atmosphère, la vitesse d'addition ou la centrifugation ; elle ne l'est pas sur l'agitation, les rampes ou le pH, trop rarement présents.

### 1.2 Paramètres essentiels : manque de l'article ou manque de l'extraction

Pour chaque méthode, une liste de paramètres qu'un chimiste exige (voir `ESS` dans `analyses/audit_parametres.py` ; ex. hydrothermal : température, durée, volume, concentration, taux de remplissage, pH, rampes de chauffe et de refroidissement). Trois états par voie et paramètre : **cité** ; **déclaré absent** par l'extracteur dans la grille `not_stated` (l'article ne le donne pas) ; **hors grille** (ni cité ni déclaré : l'extraction ne l'a pas cherché).

| Méthode | Voies | Cité | Déclaré absent | Hors grille | Paramètres les moins couverts |
|---|---|---|---|---|---|
| hydrothermal | 139 | 33 % | 39 % | 27 % | taux de remplissage 1 %, refroidissement 3 %, rampe 9 % |
| solvothermal | 44 | 38 % | 41 % | 22 % | taux de remplissage 5 %, rampe 11 % |
| sol-gel | 56 | 45 % | 25 % | 31 % | rapport molaire 16 %, agitation 23 %, rampe 23 % |
| précipitation | 63 | 45 % | 28 % | 27 % | agitation 25 %, vitesse d'addition 35 % |
| voies vertes | 33 | 52 % | 22 % | 26 % | pH 12 %, agitation 33 % |
| dépôt de films | 33 | 53 % | 8 % | 39 % | vitesse de spin 27 % |
| réduction chimique | 32 | 47 % | 21 % | 32 % | pH 16 %, vitesse d'addition 25 % |
| hot-injection | 30 | 52 % | 23 % | 25 % | refroidissement 0 %, vitesse d'addition 37 % |
| mécanochimie | 21 | 39 % | 17 % | 44 % | vitesse de broyage (nom `milling_speed`, 24 %), répétitions 10 % |
| sonochimie | 21 | 54 % | 19 % | 27 % | fréquence 29 %, puissance 33 % |
| CVD/ALD/PVD | 19 | 59 % | 25 % | 16 % | rampe 21 %, débit de gaz 47 % |
| micro-ondes | 16 | 60 % | 19 % | 21 % | pression 6 % |
| combustion/pyrolyse | 15 | 63 % | 25 % | 12 % | débit de gaz 20 % |
| solide-solide | 13 | 40 % | 45 % | 15 % | répétitions 15 %, rampe 23 % |

Trois enseignements.

- **Les articles sont la première source de manque** pour les méthodes en autoclave : 40 % des paramètres essentiels d'une voie hydrothermale ou solvothermale ne sont pas donnés, et l'extracteur l'a écrit. Le taux de remplissage de l'autoclave, qui fixe la pression, est donné dans 1 à 5 % des voies ; les rampes de chauffe et de refroidissement dans moins de 12 %.
- **L'extraction a ses angles morts**, propres aux paramètres de procédé : vitesse de refroidissement (jamais cherchée dans 7 à 60 % des voies selon la méthode), débit de gaz (60 à 78 % hors grille en traitement thermique et pyrolyse), répétitions de cycles (77 % hors grille en solide-solide), pression en micro-ondes (50 %), fréquence et puissance en sonochimie (38 %). Ces paramètres ne figurent pas dans la grille de reproductibilité du RUNBOOK, donc les extracteurs ne les déclarent ni présents ni absents.
- **Concentration, volume, rapport molaire et pH apparaissent « hors grille » à tort** : ces quantités sont portées par les réactifs (quantité, unité), pas par les étapes. Le contrôle direct sur les précurseurs le montre : la quantité est donnée pour 87 % des précurseurs hydrothermaux, 95 % en précipitation, 92 % en injection à chaud, 97 % en voies vertes, 71 % en sol-gel, 69 % en mécanochimie, 59 % en CVD ; et dans tous les cas, quand elle manque, l'extracteur l'a déclarée (0 % hors grille). Le pH, lui, n'est pertinent que s'il est ajusté : cité dans 20 à 29 % des voies hydrothermales, sol-gel et par précipitation, il est déclaré absent dans 3 à 11 %, ce qui est cohérent.

### 1.3 Lecture par paramètre (part des voies, méthodes à ≥ 20 voies)

| Paramètre | Cité | Déclaré absent | Commentaire |
|---|---|---|---|
| température | 67–100 % | 0–19 % | socle commun ; les 29 % manquants en solution à température ambiante sont des « RT » non chiffrés |
| durée | 74–100 % | 0–16 % | socle commun |
| atmosphère | 3–61 % | 12–54 % | cité surtout en dépôt de films (61 %) et sol-gel (39 %) ; les voies vertes ne la donnent jamais (3 %) |
| agitation | 7–33 % | 47–75 % | presque toujours déclarée absente : les articles ne la donnent pas |
| rampe de chauffe | 0–24 % | 10–90 % | déclarée absente dans 90 % des voies hydrothermales |
| refroidissement | 0–11 % | 6–90 % | idem |
| pression | 3–19 % | 15–82 % | déclarée absente dans 81 % des voies en autoclave (elle découle du remplissage, lui aussi absent) |
| répétitions (lavages, cycles) | 18–48 % | 3–31 % | bien couvert |

## 2. Branches sans résultat propre

Une branche est une variante testée par les auteurs ; elle ne sert à relier une variation à une propriété que si elle porte au moins un résultat.

| Famille | Branches | Sans résultat | « Mortes » (ni résultat ni caractérisation) | Résultats / branche |
|---|---|---|---|---|
| toutes | 3 956 | 6,4 % | 5,3 % | 5,6 |
| MOF | 329 | 24,9 % | 24,0 % | 5,1 |
| batterie | 127 | 12,6 % | 12,6 % | 7,9 |
| pérovskite | 502 | 11,0 % | 4,2 % | 3,8 |
| carbone | 211 | 6,6 % | 6,6 % | 3,2 |
| chalcogénure | 228 | 6,1 % | 6,1 % | 6,0 |
| oxyde | 376 | 0,8 % | 0,5 % | 10,2 |
| composite | 683 | 2,5 % | 2,3 % | 6,6 |

Aucune branche n'est sans variation (contrôle `load.py`). Les 211 branches mortes sont concentrées dans les MOF (79) : ce sont surtout des séries de conditions de synthèse (durée, solvant, échelle) dont l'article ne rapporte que le rendement ou la phase au niveau de la série, et des branches de dispositif. Pour les pérovskites, 11 % des branches n'ont pas de résultat mais 7 % ont une caractérisation (spectres sans valeur chiffrée). En dehors des MOF et des batteries, la base relie bien variation et mesure.

## 3. Stœchiométrie nominale contre formule du produit

Pour les voies de base dont la formule du matériau est lisible (339 sur 747) et dont au moins deux éléments principaux ont des quantités de précurseurs convertibles en moles (60 voies), le rapport molaire nominal des deux éléments majoritaires est comparé au rapport de la formule.

| Écart entre nominal et formule | Voies |
|---|---|
| ≤ 10 % | 24 |
| 10–50 % | 5 |
| 50–200 % | 17 |
| > 200 % | 14 |

Les 24 voies à moins de 10 % confirment la cohérence des quantités extraites (MAPbBr3 à Br/Pb = 2,8 pour 3 ; VS4 à S/V = 5 pour 4). Les écarts au-delà de 50 % ont trois causes, visibles au cas par cas : excès voulu d'un réactif qui n'est pas limitant (soufre en hydrothermal, halogénure en solution, acide bromhydrique compté comme précurseur : Br/Pb = 40 pour CsPbBr3 dans PMC8360258) ; précurseur apporté par une voie intermédiaire non comptée (Cs-oléate des pérovskites, d'où des rapports Br/Cs de 0,08 à 0,3) ; formule simplifiée du produit (Cu1,97S). Aucun de ces cas n'est une erreur d'extraction : le contrôle valide les quantités là où il peut conclure, et il montre que pour relier quantités et formule, il faut suivre les précurseurs à travers les voies intermédiaires, ce que la base permet (réactifs de rôle « intermediate » renvoyant à une voie).

## 4. Complétude contre verdict de la critique scientifique

| Verdict | Voies | Complétude moyenne | ≥ 0,8 | < 0,5 |
|---|---|---|---|---|
| douteuse | 1 493 | 0,77 | 45 % | 5 % |
| cohérente | 1 149 | 0,73 | 41 % | 8 % |
| invérifiable | 233 | 0,56 | 21 % | 35 % |
| incohérente | 108 | 0,69 | 28 % | 13 % |

| Faisabilité | Voies | Complétude moyenne | ≥ 0,8 |
|---|---|---|---|
| reproductible avec réserves | 2 639 | 0,75 | 43 % |
| non reproductible | 269 | 0,61 | 22 % |
| reproductible | 75 | 0,72 | 40 % |

Corrélation de Spearman entre complétude et « non reproductible » : −0,16. Les deux contrôles mesurent des choses différentes et c'est voulu : la complétude compte les cases remplies de la grille ; la critique juge la chimie. Une voie « douteuse » est en moyenne plus complète qu'une voie « cohérente », parce que les articles détaillés donnent plus de prise à la critique. Les deux sont cohérents aux extrêmes : les voies « invérifiables » sont les moins complètes (35 % sous 0,5), et les voies « non reproductibles » ont la complétude la plus basse. La base ne contient donc pas de contradiction entre ses deux indicateurs, et ils doivent être lus ensemble : complétude basse = il manque des données ; verdict douteux = les données posent un problème de chimie.

## 5. Variation d'une branche → effet mesuré

C'est la densité utile de la base pour l'apprentissage : 3 064 variations numériques entre une branche et son parent ; **61 % ont au moins une propriété mesurée des deux côtés** (5 575 paires comparables). 693 séries d'au moins trois points varient un même paramètre et mesurent une même propriété ; **56 % sont monotones** (|Spearman| ≥ 0,8), ce qui est la proportion attendue quand les auteurs balaient un paramètre autour d'un optimum.

Variation médiane de la propriété quand le paramètre change (paires parent-branche) :

| Paramètre varié | Propriété | Paires | Variation médiane |
|---|---|---|---|
| température | taille de cristallite | 120 | 43 % |
| température | surface BET | 81 | 42 % |
| température | taille de particule | 75 | 43 % |
| température | rendement | 82 | 50 % |
| température | composition élémentaire | 92 | 15 % |
| réactif (quantité ou nature) | taille de particule | 155 | 44 % |
| réactif | composition élémentaire | 153 | 22 % |
| réactif | surface BET | 149 | 16 % |
| réactif | pic de PL | 151 | 9 % |
| réactif | band gap | 85 | 8 % |
| réactif | pic d'absorption | 80 | 5 % |

Les séries portent d'abord sur les réactifs (332), puis la température (178), la durée (101), la concentration (42), le pH et le rapport molaire (19 chacun). Exemples de séries monotones longues : puissance d'ultrasons → taille hydrodynamique (20 points, ρ = −0,85, PMC9060541) ; pH → rendement et cristallinité (11 et 10 points, ρ = +0,87 et +0,81, PMC8136633) ; acide sulfurique → surface BET et volume poreux (10 points, ρ = −0,88 et −0,96, PMC10411504). Ordre de grandeur à retenir : un changement de température déplace les propriétés texturales et de taille de 40 à 50 % en médiane, un changement de réactif déplace les propriétés optiques de moins de 10 %.

## 6. Synonymes de noms de paramètres

682 noms distincts de paramètres (391 vus une seule fois) pour 27 types ; 88 % des occurrences portent le nom principal de leur type. Les types bien normalisés : durée (97 % sous `duration`, 54 variantes comme `spin_duration`, `duration_dry`), température (97 % sous `temperature`, 42 variantes), atmosphère (99 %), agitation (94 %), centrifugation (99,6 %). Les types dispersés : volume (69 % sous `volume`, 60 noms : `volume_teos`, `wash_volume`, `volume_ratio`…), concentration (81 %, 64 noms spécifiant le réactif), rapport molaire (48 %, 60 noms : `mass_ratio`, `solvent_ratio`, `mixing_ratio`), et un reste de 221 noms (507 occurrences, 4 %) sans type : `pore_size`, `mesh_size`, `drying_method`, `membrane_cutoff`. La dispersion vient de noms qui encodent le réactif ou l'étape dans le nom du paramètre ; elle se résout par une règle de nommage, pas par une relecture.

## 7. Conversions SI

71 % des 8 320 paramètres numériques ont une valeur SI. Température (99,9 %), durée (99 %) et rampe (97 %) sont converties ; volume (508 valeurs), concentration (403), centrifugation (270), épaisseur (104), vitesse de spin (91), agitation (87) ne le sont jamais, bien que leurs unités soient régulières (mL, µL, L ; M, mM, mg/mL ; rpm, × g ; nm, µm, mm). 253 paramètres numériques n'ont pas d'unité, dont les 147 pH (normal) et 40 rapports molaires (normal) ; le reste (≈ 60) est un défaut de citation à l'unité. La conversion SI est donc partielle par construction de `load.py`, qui ne connaît que les unités de temps et de température, et non par erreur d'extraction.

## 8. Ré-extraction à l'aveugle (20 publications)

Vingt publications tirées au sort (graine 2026) ont été ré-extraites par un agent Sonnet qui n'a vu ni l'extraction en base, ni les critiques, ni les journaux (`analyses/check_blind.py`, `audits/verification/aveugle/`). La comparaison (`analyses/compare_blind.py`) apparie les voies par libellé et matériau, puis cherche chaque valeur numérique de l'un dans l'autre : même type canonique, même unité normalisée, ±2 %. Deux mesures : le **rappel** (part des valeurs de la base retrouvées par l'aveugle) et la **précision** (part des valeurs de l'aveugle présentes en base). La base a passé quatre passes (extraction, critique de fidélité, critique scientifique, correction), l'aveugle une seule : le rappel mesure donc surtout l'apport des trois passes suivantes, la précision mesure la justesse de la base.

| Mesure | Cumul (20 publications) | Médiane par publication |
|---|---|---|
| voies appariées | 167 / 172 (97 %) ; 178 voies à l'aveugle, 123 branches contre 117 | — |
| paramètres : précision | **91,5 %** (conflits sur valeurs univoques : 0) | 100 % |
| paramètres : rappel | 67,8 % (70,6 % toutes voies confondues) | 89 % |
| résultats : précision | **83,6 %** | 84 % |
| résultats : rappel | 56,8 % (67,0 % toutes voies confondues) | 63 % |
| quantités de réactifs : précision | 78 % | — |
| quantités de réactifs : rappel | 77 % (78 % toutes voies confondues) | — |
| doutes déclarés | 231 en base contre 163 à l'aveugle | — |

Lecture.

- **Les paramètres de synthèse concordent** : 91,5 % des valeurs trouvées à l'aveugle sont dans la base, 100 % en médiane, et aucune valeur univoque (une seule température, une seule durée dans la voie) ne diffère entre les deux extracteurs. Les deux publications sous 80 % (PMC7153708, PMC9143007) le doivent à des découpages de voies différents (séries en concentration et en temps rattachées autrement), pas à des valeurs différentes.
- **Les résultats concordent à 84 %**, avec 11 conflits sur 1 000 valeurs environ, tous des différences d'attribution et non de transcription : intensités de PL lues sur la Fig. 3a de PMC9080747 attribuées à des températures décalées par l'aveugle (la relecture intégrale avait validé la base), épaisseur de coque 4,3 nm (tableau S1) contre 8,5 nm (texte) dans PMC7153708, capacité de double couche et énergie DFT de deux échantillons différents dans PMC9043841. Les publications sous 70 % de précision (PMC4725629, PMC6600758, PMC6926885, PMC7481534, PMC7648642) sont celles où l'aveugle a rangé les mêmes mesures sur d'autres voies (témoin en voie séparée contre résultat préfixé `control_`, électrode contre pile bouton) ou lu d'autres figures.
- **Le rappel mesure la valeur ajoutée des critiques** : la base contient en moyenne 30 % de paramètres et 40 % de résultats de plus que ce qu'une extraction seule trouve. Le cas extrême est PMC4725629 (rappel 7 %) : la correction y avait ajouté les caractéristiques de la lampe sur six voies (36 des 74 paramètres), que l'aveugle n'a pas relevées. À l'inverse, l'aveugle a trouvé 178 voies pour 172 en base et plus de branches (123 contre 117) : les découpages diffèrent à la marge (témoins, séries décrites par une plage), sans qu'un découpage soit faux.
- **Les choix non évidents divergent de façon prévisible** : voie de base choisie dans une série (« 160, 180 ou 200 °C » : l'aveugle prend la première, la base l'échantillon optimal), essais du matériau fini en résultats plutôt qu'en branches (les deux le font, conformément au RUNBOOK), héritage des étapes pour un témoin décrit par « same condition without X » (accepté avec doute des deux côtés), quantités déclarées non citées plutôt que déduites (10 g de NaOH déductibles d'un rapport 1:1 : les deux déclarent).
- **Trois agents sur vingt ont écrit un journal dans `journaux/`** malgré l'interdiction ; un a écrasé le journal original (restauré depuis git), les deux autres ont été déplacés dans `audits/verification/aveugle/`. Aucun n'a lu les fichiers interdits d'après leurs rapports.

Coût : 2,85 M jetons pour 20 publications (143 k par publication, 1,5 à 6 min chacune), soit un quart du coût des quatre passes.

Conclusion de la ré-extraction : sur les valeurs qu'un extracteur indépendant trouve, la base est juste dans plus de 9 cas sur 10 pour les paramètres et plus de 8 sur 10 pour les résultats, et les désaccords restants portent sur l'attribution d'une valeur à un échantillon ou à une voie, c'est-à-dire sur les mêmes points que les critiques de fidélité signalent depuis le palier 1. La base est en outre plus riche qu'une extraction seule, ce qui est le résultat attendu des passes de critique.

## 9. Lecture d'ensemble

- **Ce que la base garantit** : la fidélité des valeurs à l'article (citations vérifiées à 100 % ; ré-extraction indépendante : 91,5 % des paramètres et 84 % des résultats retrouvés à l'identique, aucun conflit sur les valeurs univoques), la déclaration explicite de ce que l'article ne donne pas (grille `not_stated` cohérente sur les quantités, la température, la durée, l'agitation, les rampes), et une densité variation → mesure suffisante pour l'apprentissage sur la température, la durée et les réactifs.
- **Ce qu'elle ne garantit pas** : l'exhaustivité des paramètres de procédé hors grille (refroidissement, débit de gaz, répétitions, puissance, remplissage), l'homogénéité des noms de paramètres et de propriétés sans table de correspondance, et la conversion SI des volumes, concentrations et vitesses.
- **Ce que disent les articles eux-mêmes** : les méthodes en autoclave sont publiées sans 40 % de leurs paramètres essentiels ; l'agitation et les rampes manquent dans 70 à 90 % des cas, toutes méthodes confondues ; les voies vertes ne précisent jamais l'atmosphère.
- **Couverture** : les familles carbures (3 voies), phosphures (1), nitrures (17), matériaux 2D (18) et céramiques (21) sont trop peu représentées pour une comparaison intra-famille ; polymères, verres, alliages, COF, électrolytes solides, thermoélectriques et géopolymères sont absents ou noyés dans « autre » (41 voies). Les propriétés attendues les moins couvertes sont le band gap et le rendement quantique des pérovskites, la surface BET des carbones, la rétention de capacité des batteries, la densité et la dureté des céramiques, l'épaisseur des matériaux 2D ; la pureté de phase quantifiée, la distribution de taille, le rendement massique, la stabilité dans le temps et l'échelle du lot ne sont presque jamais extraits.

## Fichiers

- `analyses/audit_parametres.py` → `profil_parametres.json`, `homogeneite_methodes.json`, `essentiels_methode.json`, `reactifs_quantites.json`
- `analyses/audit_verification.py` → `verif_branches*.json`, `verif_stoechiometrie*.json`, `verif_completude_*.json`, `verif_variation_resume.json`, `verif_series.json`, `verif_paires.json`, `verif_effet_param_prop.json`, `verif_param_synonymes*.json`, `verif_si*.json` ; regroupés pour la page dans `docs/audit_contenu/dash/verif_*.json`
- `analyses/check_blind.py`, `analyses/compare_blind.py`, `audits/verification/aveugle/<PMCID>.json` → `verif_reextraction.json`
