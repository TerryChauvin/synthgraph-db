# Pilote de la passe de complément (28 octobre 2026)

Point 4 du plan d'amélioration validé par l'utilisateur (points 1 et 2 faits le même jour : sonde `analyses/sonde_manques.py`, vocabulaire canonique `canon.py`). Question posée : une relecture ciblée, guidée par la sonde, ajoute-t-elle assez à une extraction déjà close pour justifier de repasser sur les 500 publications ?

## Protocole

- 20 publications choisies parmi les plus touchées par la sonde (paramètres de procédé d'abord), 9 familles, 1 à 39 voies chacune.
- Un agent Sonnet (`high`) par publication, consigne `PROMPT_COMPLEMENT.md` : lit la liste de la sonde (`audits/pilote_complement/<PMCID>_sonde.md`), les sections expérimentales et les annexes, **ajoute seulement** (paramètres, cases `not_stated`, conditions de mesure, résultats chiffrés, doutes), chaque ajout avec sa citation exacte ; `load.py check` à 0 erreur ; journal `journaux/<PMCID>_complement.md`.
- Contrôle de l'orchestrateur à chaque retour : `load.py check`, `analyses/delta_complement.py` (ajouts par catégorie, 0 élément retiré exigé), relecture de 1 à 3 ajouts dans le texte, normalisation des noms de cases hors vocabulaire.
- Critique de fidélité des ajouts sur 4 publications (1 sur 5, les plus fournies) : `audits/pilote_complement/CRITIQUE_AJOUTS.md`, rapports `<PMCID>_critique.md`.
- Chargement en base par lot (pas à chaque publication, pour limiter la croissance de `.git`).

## Résultat

| | Total (20 publ.) | Par publication (médiane) |
|---|---|---|
| Paramètres de synthèse ajoutés | 27 | 0 |
| Cases `not_stated` ajoutées | 223 | 7 |
| Entrées de caractérisation ajoutées | 133 | 5 |
| Conditions de mesure renseignées (entrées nouvelles ou champs `null` remplis) | 187 | 7 |
| Résultats chiffrés ajoutés | 177 | 6 |
| Doutes ajoutés | 46 | 2 |
| Éléments existants retirés | 0 | 0 |
| Champs existants complétés (`null` → valeur, chaîne `conditions` allongée, « modèle non cité » remplacé par le modèle trouvé en annexe) | 39 | 1 |
| Jetons d'agent | 2,79 M | 139 k (112–188 k) |

Détail par publication (paramètres / `not_stated` / conditions / résultats / jetons) :

| PMCID | Famille | Param. | `not_stated` | Conditions | Résultats | Jetons |
|---|---|---|---|---|---|---|
| PMC9054805 | 2D | 0 | 2 | 14 | 8 | 141 k |
| PMC11891312 | zéolithes | 7 | 8 | 5 | 9 | 143 k |
| PMC5858874 | oxydes | 0 | 3 | 0 | 0 | 116 k |
| PMC10460902 | 2D | 0 | 4 | 20 | 45 | 141 k |
| PMC5746929 | oxydes | 3 | 8 | 0 | 6 | 124 k |
| PMC8474143 | quantum dots | 2 | 33 | 10 | 10 | 144 k |
| PMC9778285 | oxydes | 0 | 4 | 1 | 0 | 113 k |
| PMC5376314 | chalcogénures | 4 | 16 | 3 | 0 | 124 k |
| PMC3920662 | nanoparticules | 0 | 6 | 4 | 8 | 123 k |
| PMC10411504 | céramiques | 0 | 5 | 3 | 3 | 133 k |
| PMC13446275 | chalcogénures | 0 | 13 | 29 | 1 | 152 k |
| PMC7153708 | chalcogénures | 0 | 16 | 36 | 0 | 147 k |
| PMC13257848 | MOF | 0 | 6 | 1 | 3 | 134 k |
| PMC8398574 | 2D | 0 | 3 | 2 | 1 | 115 k |
| PMC9083554 | 2D | 2 | 7 | 11 | 5 | 151 k |
| PMC8292365 | 2D | 0 | 4 | 7 | 9 | 139 k |
| PMC8822483 | MOF | 4 | 14 | 9 | 8 | 188 k |
| PMC10200858 | zéolithes | 2 | 4 | 8 | 7 | 133 k |
| PMC8233738 | zéolithes | 2 | 17 | 18 | 41 | 167 k |
| PMC11269599 | 2D | 1 | 50 | 6 | 13 | 160 k |

## Ce que dit le pilote

1. **Les paramètres de synthèse étaient déjà là.** 27 ajouts sur 20 publications, presque tous des modes d'addition (« dropwise », « slowly ») ou de séchage. Environ la moitié des alertes de la sonde sur les paramètres de procédé sont des faux positifs : rampe, débit de gaz, vide, puissance appartiennent à la TGA, à l'XRF ou à l'essai catalytique, et étaient déjà dans les conditions de ces mesures. Les agents les ont écartés correctement, avec la raison dans leur journal.
2. **Le gain est dans les conditions de mesure et les résultats de tableaux.** 187 conditions renseignées (électrolyte, masse de catalyseur, lampe, dégazage BET, rayonnement XRD, tension TEM, méthode de calcul de la bande interdite) et 177 résultats chiffrés absents de l'extraction initiale (énergies de liaison XPS, positions de pics XRD, compositions d'un tableau d'annexe, paramètres d'isothermes). Deux publications concentrent 86 résultats (tableaux de composition et d'adsorption que l'extraction d'origine avait laissés en texte libre).
3. **Les cases `not_stated` ajoutées sont la partie la plus discutable.** 223 ajouts, surtout `repetitions`, `cooling_mode`, `vessel`, `drying_mode`, `stirring_speed`. Elles rendent l'absence explicite, mais la critique en juge environ un quart « douteuses » (paramètre peu pertinent pour la méthode, ou information en fait donnée ailleurs : 2 cas faux sur 4 publications). Une publication a reçu 50 cases sur 8 voies indépendantes.
4. **Fidélité des ajouts** (4 publications, 217 ajouts contrôlés par un second agent) : **2 faux** (0,9 %), corrigés — une case `vessel` « non cité » alors que le creuset et l'autoclave sont donnés à l'étape précédente ; une isotherme rattachée au lit composite alors que le texte parle du MOF seul — et 24 douteux (11 %), surtout des `not_stated` discutables et des conditions de mesure dont la citation est une phrase de résultat plutôt que le protocole. Aucune valeur chiffrée fausse.
5. **Les critiques listent aussi ce que la passe a manqué** : résultats présents pour un échantillon et pas pour ses voisins (TGA sur R1 seulement, « three times » sur FGS1 seulement), techniques décrites sans entrée (SEM de FGS2, FTIR de RHA2), traitements de données (ajustement de déclin PL). La passe suit la sonde ; elle ne remplace pas une relecture intégrale.
6. **Dérives corrigées en cours de route** : noms de cases inventés (`batch_count`, `product_mass`, `furnace_model`, `mixer_type`, `purification_method`, `ph_final`) renommés vers le vocabulaire, règle ajoutée au prompt (règle 8) ; clé `where` des doutes précisée ; doublon `power` / `sonication_power`.
7. **Coût** : 139 k jetons par publication en médiane (agent de complément), plus 122 k par publication critiquée ; soit, avec une critique sur cinq, ≈ 165 k par publication, contre ≈ 650 k pour le pipeline complet.

## Recommandation

- **Généraliser, mais pas aux 500.** Le gain dépend du nombre de points de la sonde « mesure » et de la présence de tableaux non extraits. Cible : les publications ayant au moins 3 points « mesure : conditions absentes » ou un tableau de résultats en texte libre (≈ 200 publications, à lister par `sonde_manques.py`), soit ≈ 33 M jetons avec la critique sur 1 sur 5 (≈ 4 fenêtres de 5 h).
- **Resserrer les `not_stated`** avant de généraliser : liste fermée par méthode (celle de `analyses/audit_parametres.py`, `ESS`), `repetitions` et `vessel` seulement au niveau de la voie, pas de case pour une information donnée à une autre étape de la même voie.
- **Faire porter la critique sur les attributions** (voie et étape) plus que sur les citations, qui sont vérifiées mécaniquement : les deux erreurs trouvées sont des erreurs de rattachement.
- **Intégrer au RUNBOOK** (point 3 du plan) la grille des conditions de mesure par technique, pour les extractions futures.
- Les compteurs des README et de la page publique sont à régénérer après la généralisation (`analyses/audit_contenu.py`, `audit_parametres.py`, `audit_verification.py`, `build_site.py`).

## Fichiers

`PROMPT_COMPLEMENT.md`, `analyses/sonde_manques.py`, `analyses/delta_complement.py`, `audits/pilote_complement/` (`<PMCID>_sonde.md`, `<PMCID>_ajouts.md`, `<PMCID>_critique.md`, `CRITIQUE_AJOUTS.md`), `journaux/<PMCID>_complement.md`, `audits/jetons.csv` (passes `complement` et `critique_ajouts`).
