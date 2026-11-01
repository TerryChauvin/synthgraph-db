# Relecture du palier 6 (publications 251 à 300)

Session cloud du 17 au 18 octobre 2026, 3 agents en parallèle, période autorisée par l'utilisateur jusqu'au 18/10 à 17 h (Paris). Pipeline habituel : extraction → chargement → critique de fidélité → critique scientifique → correction → clôture.

## Bilan

- **Volume :** 50 publications closes, 554 voies, 9 680 citations vérifiées, toutes exactes (100 %).
- **Audit :** `audit.py 6` donne 0 bloquant. Les 9 bloquants initiaux étaient des relectures intégrales dues (tirage 1 sur 5) ; elles sont faites (voir plus bas). Les 56 avertissements sont tous des faux positifs ou des limites de l'article, acceptés un par un : 0 ouvert.
- **Relectures intégrales :** 10 publications, 1 887 valeurs contrôlées, 0 fausse.
- **Critique de fidélité :** 419 constats (médiane 8 par publication) : 396 corrigés, 22 rejetés avec raison, 1 accepté. Par nature : 164 manquants, 174 mineurs, 46 déduits, 17 attributions, 15 non cités à tort, 3 faux (0,7 %).
- **Coût :** médiane de 0,65 M jetons par publication (moyenne 0,66 M, total 33,0 M pour les 50), hors orchestrateur. Médianes par passe : extraction 173 k, critique de fidélité 155 k, critique scientifique 183 k, correction 139 k. Une relecture intégrale par agent coûte en moyenne 80 k jetons par publication.

## Relectures intégrales (agents Sonnet, lecture seule, article lu en entier, figures ouvertes)

| Publication | Valeurs contrôlées | Fausses |
|---|---|---|
| PMC9307632 | 248 | 0 |
| PMC9795147 | 24 | 0 |
| PMC12805362 | 170 | 0 |
| PMC11752507 | 345 | 0 |
| PMC6369825 | 142 | 0 |
| PMC6266794 | 249 | 0 |
| PMC11297172 | 153 | 0 |
| PMC11098855 | 167 | 0 |
| PMC5304631 | 198 | 0 |
| PMC6722878 | 191 | 0 |

Points signalés par les relecteurs, non comptés comme erreurs d'extraction :

- **PMC11297172 :** la barre à 0 % de la Fig. 4b est étiquetée (Ba0,5Sr0,5)CeO3, la voie extraite est (Ba0,4Sr0,6)CeO3 ; l'article désigne cette composition de trois façons (texte, Tableau 2, Fig. 4b). Choix d'attribution déjà en doute et en annotation `limite_reproductibilite`.
- **PMC5304631 :** les barres de la Fig. 16 à 16 ng/mL sont lues à ≈ 105 % pour 100 % extraits, dans la tolérance de ±5 points déclarée.
- **PMC12805362 :** rétention de LFP-W et LFP-E, 75,6 et 53 % dans le texte contre ≈ 41 et 71 % sur la figure ; les deux lectures sont extraites.

## Échantillon de 30 valeurs du rapport d'audit

30 lignes relues (citation contre valeur, étape et branche) : 27 sans réserve. Trois lignes demandent une remarque, aucune n'est fausse :

- PMC6369825 `OLE_t120min` (durée 120 min) : la citation est la légende de la figure de la série en temps, qui ne répète pas « 120 min » ; la valeur est celle de la série.
- PMC8982036 `MnQD_1.6nm_x8` (`molar_ratio` 8) : la citation parle de x = 1, 4 et 8 couches de coque ; le nom du paramètre est approximatif, la valeur est exacte.
- PMC11752507 `LC-PNC_25C_purified` : paramètre qualitatif (double centrifugation), citation correcte.

## Stœchiométrie et cohérence (5 voies, par la critique scientifique et vérifiées dans ses blocs `calculs`)

| Voie | Contrôle | Résultat |
|---|---|---|
| PMC8398574 NiFe-LDH | Ni/Fe = 4,00 introduit, OH⁻ nécessaire 40 mmol (et non 44), NH3 50 mmol | cohérent ; Ni/Fe mesuré 3,79 expliqué par les ammines de nickel |
| PMC6116234 MAPbI3_SiO2Si | 0,2 mg de PbI2 dans 1 mL = 0,2 g/L, soit 5 % de la solubilité à 100 °C | incohérence de l'article (« sursaturée »), annotée |
| PMC5304631 Au-citrate | 50 µmol d'or, particules de 20,9 nm : au plus 1,17 nM, l'article annonce 11,1 nM | incohérence de l'article (≈ 9,5 fois), annotée |
| PMC4726031 LaFeO3/MMT | Co(NO3)3 et Ni(NO3)3 écrits dans l'article : +21 % de métal à peser (353 contre 291 g/mol) | coquille de l'article, annotée ; doute fermé en annotation |
| PMC11098855 MCF | MnCoFe2O4 non neutre, rapport 1:1:4 donne Mn0,5Co0,5Fe2O4 | incohérence de l'article, annotée |

Aucune de ces anomalies n'est une erreur d'extraction : les citations sont conformes ; chaque incohérence est gardée littérale, avec un doute et une annotation `limite_reproductibilite`.

## Anomalies de l'audit (56 avertissements, tous acceptés)

- **Éléments du produit sans source parmi les réactifs (48) :** faux positifs du contrôle chimique. Cœur/coquille (CdSe/ZnS:Mn/ZnS, PMC8982036), ligand AMTP (PMC11036359, élément P), `Li4PS4I` obtenu à partir de LiI (PMC8263741), produits nommés par formule composée (MnCoFe2O4@SiO2, NiCo2S4@PPy), pérovskites obtenues à partir de précurseurs désignés par une abréviation (PMC11297172) ; le chimiste lit les précurseurs réels dans les réactifs et les annotations.
- **Température au-dessus de l'ébullition du solvant (3) :** PMC7181732, PMC11297172 et PMC8539213 ; l'article ne décrit pas le récipient ; limite annotée.
- **Unité non reconnue (3) :** symbole `℃` (2, PMC7648642) et « months » (PMC6369825).
- **Cohérence (2) :** deux branches Co/Ni aux variations identiques (PMC4726031), voie de base sans réactif (PMC8930993, dépôt sur mousse de nickel).

## Constats récurrents du palier (déjà couverts par RUNBOOK.md et PROMPT_CORRECTION.md)

- Figures téléchargées après l'extraction (`enrich.py figs` n'avait pas tourné) : 3 publications, repérées par la critique de fidélité qui a lu les figures (PMC7648642, PMC6266794, PMC11297172 en partie). Les valeurs ont été ajoutées à la correction.
- Héritage non fondé d'une quantité, d'un solvant ou d'une durée vers une branche (BTS12-1300/-1400, voies 0M, essais sans chalcone, essais de gélification) : corrigé en `not_stated` avec doute.
- Erreurs de rattachement de citations de légende de figure à une grandeur lue sur l'image : corrigées à la critique de fidélité.
- Un agent de correction a décalé les `step_order` en insérant deux étapes (PMC11989644) ; `load.py check` reste à 0 erreur.
- Un relecteur de fidélité a lu par inadvertance le journal d'extraction (PMC8263741) ; sans effet sur l'inventaire.

## Sources à vérifier depuis le PC

Crossref reste bloqué depuis le cloud. Les DOI cités par les critiques scientifiques mais non vérifiés sont dans `audits/palier_006_doi_a_verifier.txt`.

## Règles ajoutées à RUNBOOK.md

Aucune. Les erreurs vues (héritage non fondé, citation de légende pour une valeur de figure, figures non lues) sont déjà des règles du RUNBOOK ; elles ont été rappelées dans les consignes de correction.
