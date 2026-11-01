# Relecture du palier 4 (publications 151 à 200)

Session cloud du 2026-10-14. Ce palier a été traité avec le palier 3 : 100 publications en tout, avec 4 agents en parallèle selon le plan validé le 2026-10-14.

## Bilan

- **Volume :** 50 publications closes, soit 515 voies (140 de base, 375 branches) et 9 920 citations vérifiées, toutes exactes. La complétude moyenne est de 0,70.
- **Audit :** `audit.py 4` donne 0 bloquant et 0 avertissement ouvert après traitement. Les 17 avertissements ont été acceptés, dont 12 faux positifs de l'heuristique de température (voir plus bas).
- **Relectures intégrales :** 5 publications, 0 valeur fausse sur 529 valeurs contrôlées.
- **Échantillon de 30 valeurs :** 0 erreur.
- **Coût :** 0,625 M jetons par publication (médiane).

## Relectures intégrales

| Publication | Valeurs contrôlées | Fausses | Remarque |
|---|---|---|---|
| PMC11678781 | 90 | 0 | |
| PMC10099130 | 124 | 0 | ordre des rangées du Tableau S1 vérifié |
| PMC9418622 | 129 | 0 | `step_order` retiré des variations d'octylamine (règle du RUNBOOK) |
| PMC10585300 | 170 | 0 | Tableau 2 à cellules fusionnées vérifié |
| PMC7451673 | 16 | 0 | valeurs de figure non relues sur l'image |

## Critiques : constats et comparaison avec les paliers précédents

| | Palier 1 | Palier 2 | Palier 3 | Palier 4 |
|---|---|---|---|---|
| Constats de fidélité | 526 | 403 | 435 | 406 |
| Médiane par publication | 10 | 8 | 8,5 | 8 (de 3 à 12) |
| Constats « faux » | 29 | 7 | 5 | 7 |

Répartition des 406 constats :
- `mineur` : 169
- `manquant` : 147
- `deduit` : 49
- `non_cite_a_tort` : 18
- `attribution` : 16
- `faux` : 7

Sur les 406 constats, 385 ont été corrigés et 21 rejetés. Motifs des rejets :
- valeurs littérales gardées malgré une contradiction interne de l'article (PMC8199406, PMC12191741, PMC9050136). L'écart est passé en `limite_reproductibilite`.
- héritage justifié par une phrase générale des Méthodes (PMC9370708, PMC11678781).
- hors périmètre : test du matériau fini, portée de substrats (PMC5407272, PMC12624334).
- lecture de figure à moins de 10 % près (PMC9057918).
- valeur en toutes lettres gardée en `value_text` (PMC9054292).
- renvoi de contexte, qui n'est pas une source de méthode (PMC6864515).
- règle du RUNBOOK sur `step_order` (PMC9418622).

Les 7 constats « faux » :
- **PMC11329678 : le seul cas où l'article lui-même se trompe sur une valeur.** Les pourcentages EDX sont appelés « weight percent » dans le texte. Le tableau de la Fig. 4 les range dans la colonne atomique. L'unité est corrigée d'après le tableau, et l'erreur du texte est annotée.
- **PMC9085430 :** une longueur de 10 µm avait été lue sur la Fig. 3a. C'est la barre d'échelle ; les particules mesurent environ 5,5 à 9 µm. La valeur est corrigée.
- **PMC11197016 :** un R² = 0,99 était attribué à la Fig. 4h, qui n'en affiche aucun. Le résultat est retiré.
- **PMC4957122, deux constats, et PMC10489885 :** il s'agit d'annotations de comparaison entre branches, dont la phrase était inexacte (classement des volumes poreux ; « même ordre » pour Rct et la capacité). Elles ont été réécrites.
- **PMC9374656, constat rejeté :** il porte sur la conductivité de Ge. J'ai relu la Fig. 2e (axe logarithmique) : le point est juste au-dessus de 10³, donc 1300 S/cm est gardé. Le « up to 1200 » du texte est noté à côté.

Deux de ces « faux » sont des lectures de figure (PMC9085430 et PMC11197016). Aucune valeur recopiée du texte n'était fausse.

**Critique scientifique :**
- 301 jugements de voie : 85 cohérentes, 175 douteuses, 29 invérifiables, 12 incohérentes ;
- 294 contrôles au statut `probleme`, passés en annotations quand ils venaient de l'article ;
- aucune valeur changée sur la foi de cette critique.

## Avertissements de l'audit acceptés (17)

Tous ont été vérifiés dans le texte.
- **12 faux positifs de l'heuristique « température au-dessus de l'ébullition du solvant » :**
  - **PMC6864515 :** l'étape 1 dissout PbO et l'acétate de Cs dans l'acide oléique et l'oléylamine (Éb > 300 °C). Le toluène et le DCM n'arrivent qu'après.
  - **PMC7285084, 4 avertissements :** copolymérisation en masse à 80 °C, en tube ou en Schlenk sous Ar. Le chloroforme (Éb 61 °C) ne sert qu'à dissoudre le produit après la réaction.
  - **PMC5407272, 2 avertissements :** réduction sous H2 (1 atm) à 150 °C d'un solide sec.
  - **Cause commune :** les solvants de ces voies n'ont pas de `step_order`. L'audit les rattache donc à toutes les étapes. Ce n'est pas une erreur d'extraction.
- **PMC5388254 :** durée de stockage en « months », recopiée sans conversion SI.
- **PMC9085430, 4 avertissements :** Ni et Mn viennent de l'intermédiaire carbonate NMC (voie de base). La lithiation ajoute Li2CO3 en quantité stœchiométrique plus 5 %.
- **PMC5080270 :** Au vient des nanoparticules préparées dans une voie séparée.
- **PMC11345764 :** Co3Mo3N est préparé selon la méthode de Kojima et Aika citée, sans réactifs donnés. La voie est gardée avec ses manques et sa `method_source`.
- **PMC5448492, 3 avertissements :** les branches xérogel et calcinée à 500 °C diffèrent par leurs étapes (pas de calcination pour le xérogel), pas par une variation.

## Échantillon de 30 valeurs du rapport d'audit

J'ai relu les 30 lignes de `palier_004.md`. Dans les 30 cas, la citation soutient la valeur, pour la bonne étape et la bonne voie : 0 erreur.

Points particuliers :
- **PMC9418622 White_3560K :** 0,52 se trouve bien dans la colonne « Green » du tableau, d'après l'en-tête « CCT (K) | Blue | Green | Yellow | Red | CRI | x | y ».
- **PMC6403542 P/HDI-GO 6 :** 2,5 mg correspond à 5 % en masse, ce qui est cohérent avec 5,0 mg de GO brut = 10 %.
- **PMC12195685 GCE-Fe/MCM-41(5) et PMC8132056 PSC_12F :** pour ces substitutions de branche, la citation est une phrase générale. Elle reste exacte, mais faible.

## Stœchiométrie et cohérence chimique (5 voies)

| Voie | Contrôle | Verdict |
|---|---|---|
| PMC9085430 LNMO | urée : métaux = 2:1. Li2CO3 stœchiométrique + 5 % (volatilisation). Calcination à 750 °C à l'air pour atteindre Mn(III/IV) et Ni(II) | conforme à LiNi0.5Mn1.5O4. Quantités d'acétates non données (manque déclaré) |
| PMC12455581 ZIF-67 | Co(NO3)2·6H2O 2 mmol, 2-MeIm 12 mmol, soit 1:6 dans le méthanol à température ambiante | conforme (rapport usuel de 1:4 à 1:8) |
| PMC4957122 mBeta | H2SiO3 3,9 g, soit 50 mmol de Si. NaAlO2 0,17 g, soit 2,07 mmol d'Al. Si/Al ≈ 24 | dans le domaine de la zéolithe bêta (12–50). Rapport non écrit par l'article, calculé ici |
| PMC11556383 NZF (Ni0.5Zn0.5Fe2O4) | NiO + ZnO + oxyde de fer à 1200 °C à l'air | atmosphère cohérente avec Fe(III). EDS « en accord » selon les auteurs. Masses non données |
| PMC5448492 FeSi | 255 EtOH : 4 TEOS : x Fe(NO3)3·9H2O : 9 H2O2 : 40 H2O. Branche à 25 % Fe/Si, soit x = 1 | cohérent. Calcination à l'air à 500 °C vers Fe2O3/SiO2 ; le taux de 25 % est lu sur l'axe de la Fig. 5 (`from_figure`) |

## Contrôle croisé (`compare.py`)

- **MCM-41 :** SBET de 996 m²/g (PMC12195685, référence TEOS), 791 m²/g pour Al-MCM-41 (PMC8233738) et 739 m²/g avec ZnO (PMC5977331). L'ensemble est cohérent.
- **TiO2 sol-gel :** anatase à 400 °C (PMC5521283) et anatase majoritaire avec un peu de rutile à 600 °C (PMC5858874). C'est cohérent.
- **CsPbBr3 :** 17 voies de base dans la base ; les émissions (526–530 nm) et les tailles (≈ 8 nm) concordent entre publications. Le rapport Br/Pb ≈ 0,27 de PMC6864515 est déjà annoté en limite.
- **ZIF-67 :** il n'est présent que dans une publication, donc pas de comparaison possible.

## Sources du critique scientifique

Crossref est bloqué depuis le cloud. Les 132 DOI du palier sont listés dans `palier_004_doi_a_verifier.txt`, à vérifier depuis le PC (`python -I sources_check.py --palier 4 10`).

Sur un tirage de 4 sources, 3 sont des références classiques. Leurs DOI et leurs titres correspondent à la bibliographie connue (contrôle de mémoire, pas en ligne) :
- Obrovac et Chevrier, Chem. Rev. 2014, 10.1021/cr500207g ;
- Danks, Hall et Schnepp, Mater. Horiz. 2016, 10.1039/C5MH00260E ;
- Deacon et Phillips, Coord. Chem. Rev. 1980, 10.1016/S0010-8545(00)80455-5.

La quatrième est la fiche PubChem du thioacétamide.

## Règles et outils modifiés pendant le palier

- Aucune nouvelle règle au RUNBOOK.
- **Erreur vue une fois :** l'agent de correction avait ajouté un `step_order` à une variation de réactif du parent (PMC9418622), contre la règle existante. Si elle se répète, il faudra la rappeler dans `PROMPT_CORRECTION.md`.
- **Piste d'amélioration de `audit.py` :** rattacher les solvants sans `step_order` à l'étape où ils apparaissent dans les citations. Cela supprimerait les faux positifs de température. Ce n'est pas fait, parce que cela toucherait un contrôle.

## Coût en jetons (agents seuls, hors orchestrateur)

| Passe | Médiane par publication |
|---|---|
| Extraction (Sonnet) | 156 k |
| Critique de fidélité (Sonnet) | 143 k |
| Critique scientifique (Opus) | 173 k |
| Correction (Sonnet) | 145 k |
| **Total par publication** | **0,625 M** (moyenne 0,635 M, soit 31,8 M pour le palier) |

Paliers 3 et 4 ensemble : 62,3 M jetons pour 100 publications. C'est stable par rapport au palier 2 (0,63 M) et environ 30 % en dessous du palier 1.

## Ce qui n'a pas été vérifié

- Les DOI sur Crossref et les pages sources.
- Les 706 résultats lus sur figure : seuls ceux contestés par la critique ont été relus sur l'image.
