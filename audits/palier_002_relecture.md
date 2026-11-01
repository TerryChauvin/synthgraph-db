# Relecture du palier 2 (publications 51 à 100)

L'orchestrateur a fait cette relecture le 2026-10-13, dans le cloud, après `audit.py 2`. Le palier comprend les 10 publications du test (`test_10_palier2.md`) et 40 nouvelles publications.

## Bilan

- **Volume :** 50 publications, 581 voies (111 de base, 470 branches), 8 796 citations. Chaque citation est retrouvée mot pour mot dans le texte de l'article, et chaque valeur numérique figure dans sa citation (contrôle automatique de `load.py`).
- **Audit :** 0 anomalie bloquante. Les 34 avertissements de l'audit ont tous été examinés et acceptés (détail plus bas). Le dernier `audit.py 2` donne 0 bloquant et 0 avertissement.
- **Doutes :** tous tranchés, aucun doute ouvert.
- **Critiques :** chaque publication a eu ses deux critiques (fidélité et science) et une correction, puis a été rechargée.
- **Valeurs lues sur figure :** 814 résultats portent `from_figure`. Le texte ou un tableau prime toujours sur la figure. Les lectures sont arrondies à 2 chiffres significatifs.
- **Annexes :** le dépôt S3 PMC, joignable depuis le cloud, a fourni les annexes et les figures. Il en manque encore pour plusieurs articles (images S1 à Sn absentes alors que les légendes sont présentes). Chaque cas est signalé par une annotation « Annexe absente du dépôt ».

## Relectures intégrales

| Publication | Valeurs contrôlées | Valeurs fausses |
|---|---|---|
| PMC3088885 | 41 | 0 |
| PMC9366981 | 99 | 0 |
| PMC6678425 | 50 | 0 |
| PMC10405785 | 62 | 0 |
| PMC9060541 | 161 (dont 97 rangées du plan composite, contrôlées par script) | 0 |
| PMC9685500 | 124 | 0 |
| PMC8708305 | 54 | 0 |
| PMC6315938 | 99 | 0 |
| PMC10342551 | 86 | 0 |
| **Total** | **776** | **0** |

Pour toutes les autres publications, l'orchestrateur a vérifié au chargement le rattachement des rangées de chaque tableau aux échantillons, rangée par rangée. Pour les plans d'expériences (PMC9060541, PMC10780621), ce contrôle a été fait par script. Taux d'erreur de l'échantillon cumulé (`sample_error_rate`) : 0,07 %.

## Critiques : constats et comparaison avec le palier 1

| | Palier 1 | Palier 2 |
|---|---|---|
| Constats de fidélité | 526 | 403 |
| Médiane par publication | 10 | 8 (de 3 à 15) |
| Constats « faux » | 29 | 7 |

Répartition des 403 constats par type :
- `mineur` : 176
- `manquant` : 130
- `deduit` : 55
- `non_cite_a_tort` : 19
- `attribution` : 16
- `faux` : 7

Sur les 403 constats, 385 ont été corrigés et 18 rejetés. Chaque rejet est motivé par le texte :
- une borne de plage qui n'est pas un essai ;
- un renvoi de contexte qui n'est pas une source de méthode ;
- un support nommé dans le commentaire d'une figure ;
- ou une couverture déjà documentée dans un doute.

Les 7 constats « faux », relus un par un dans la base (vérification du 2026-10-13, soir) :
- 4 portent sur `method_sources` (PMC6409700, PMC10405785, PMC6104471, PMC6720160) : rôle mal classé, étalons de rendement quantique pris pour une source de méthode, renvoi mal numéroté par l'article lui-même.
- 2 portent sur des annotations de l'orchestrateur, pas sur des données extraites (PMC7033158 : « seul AgNPs-Fe2O3 dépasse… » ; PMC10754887 : ordre des coefficients de diffusion). Elles ont été réécrites.
- 1 porte sur une valeur (PMC3920662, écart-type DLS à 30 mg) : le texte donne 0,0231 µm, la figure 0,0347 µm. La valeur du texte est gardée, l'écart est annoté.

Autrement dit, aucune valeur numérique recopiée de l'article ne s'est révélée fausse sur ce palier ; les 7 « faux » sont des erreurs de classement ou d'interprétation. Une version antérieure de ce rapport disait à tort que 4 d'entre eux étaient « des valeurs corrigées après retour au texte ».

Critique scientifique : 276 jugements de voie (96 cohérentes, 141 douteuses, 24 invérifiables, 15 incohérentes) et 298 contrôles au statut `probleme`. Tous les problèmes venant de l'article sont devenus des annotations `limite_reproductibilite`. Aucune valeur n'a été changée sur la foi de la critique scientifique.

Pour chaque publication, l'orchestrateur a recompté au moins un calcul de la critique scientifique. Ils étaient tous exacts. Exemples :
- Bragg : (111) de NiFe2O4 attendu à 18,4° et non à 22,5° ; (100) de ZnO à 31,77° ;
- produit de solubilité de Ag2O à pH 11 ;
- 4V/S = 48,7 nm (PMC11752637) ;
- Cu2C8H6O8 = 357,22 g/mol ;
- 0,1 g d'acide boronique dans 30 mL = 0,024 mol/L ;
- LDR de 203 dB et non 213 dB ;
- ΔrG de TiO2 + ½ N2 → TiN + O2.

## Avertissements de l'audit acceptés (34)

- **12 sur PMC6104471 :** « B » est le butylammonium (BA) de la formule, pas du bore.
- **6 sur PMC3088885 et 9 sur PMC5452520 :** les éléments du produit viennent d'une voie intermédiaire (alcogel THEOS, sol de zircone), référencée comme réactif.
- **PMC10460902 :** g-C3N4 sous air à 823 K, c'est le procédé standard écrit par l'article.
- **PMC8125239 LaCoO3, PMC8941405 S60 et S80 :** voies sans réactif, parce que l'article ne donne pas la recette. C'est annoté en limite.
- **PMC9043841 :** branches CoFe/NiCo sans conditions de départ écrites, seuls les rapports des produits sont donnés.
- **PMC10754887 :** combustion en solution à 185 °C en récipient ouvert, c'est normal.
- **PMC8941405 :** cristallisation à 170 °C sans autoclave nommé. L'enceinte fermée est signalée en sécurité.

## Échantillon de 30 valeurs du rapport d'audit

Le tirage de `audit.py` est à graine fixe mais la population change à chaque passage : l'échantillon du premier passage (30 lignes relues) et celui du dernier passage (celui de `palier_002.md`) n'ont que 10 lignes en commun. Les 20 lignes nouvelles ont été relues à leur tour le 2026-10-13 au soir. Au total, 50 lignes relues : dans les 50 cas la citation soutient la valeur, pour la bonne étape et la bonne voie. 0 erreur, 3 réserves :
- **PMC6720160 TPPH2, 141 °C :** valeur lue sur un schéma d'annexe sans légende (`from_figure`). La citation est la phrase de renvoi aux annexes, et un doute le dit.
- **PMC8941405 1%Zn, « calcined at 550 for 6 h » :** l'article n'écrit pas d'unité. L'unité °C a été reprise par l'extracteur et un doute le signale.
- **PMC10780621 NaHCO3_t48h, étape 5, 33 µL de HF :** la citation est celle du protocole type des Méthodes. La branche de la série en temps déclare pourtant `gel_composition` non cité (l'article ne dit pas quel gel a servi à cette série) tout en portant les volumes du protocole type dans ses étapes. Le doute « séries NaOH_t*, Na2CO3_t*, NaHCO3_t* (composition du gel) » le dit ; un lecteur doit comprendre ces volumes comme hérités du protocole type, non comme cités pour cet échantillon.

Sur les lignes de tableau (PMC8941405 tableau 1, PMC10780621 tableau 2, PMC8159122 tableau 4, PMC9060541 plan composite), la colonne et la rangée ont été vérifiées contre l'en-tête du tableau.

La voie Ce-MOF-HT de PMC11266555 reprend la centrifugation de la voie RT. L'article justifie cet héritage par « according to the RT synthesis procedure ».

## Stœchiométrie et cohérence chimique (5 voies)

| Voie | Contrôle | Verdict |
|---|---|---|
| PMC9475401 N-LMFP | 15 mmol LiH2PO4, 12 mmol MnO, 3 mmol de sel de Fe → Li:Mn:Fe:P = 1:0,8:0,2:1 ; Ar et carbone du saccharose pour Fe(II) | conforme à LiMn0.8Fe0.2PO4 |
| PMC6104471 Br_n et I_n | BAX 2, MAX n−1, PbX2 n → X = 3n+1 ; Tableau 1 conforme | conforme à (BA)2(MA)n−1PbnX3n+1. Les Méthodes écrivent 2 : n−1 : 3n+1, incohérence annotée |
| PMC13393389 Al/Mg/Fe-BDC | 0,952 + 0,893 + 0,555 = 2,40 mmol de métaux pour 2,046 mmol de BDC (0,85) | quantités exactes. L'incorporation de Mg n'est pas démontrée, c'est annoté |
| PMC3477086 ZnO_0Cd | 15 mmol de métal pour 0,3024 g de LiOH (12,6 mmol) → OH/M = 0,84 | base en défaut, au plus ≈ 40 % du Zn en ZnO. Annoté |
| PMC4829567 ZHS/GO | Na2Sn(OH)6 + ZnSO4 → ZnSn(OH)6 ; Zn:Sn ≈ 1,9 | excès de Zn (risque de Zn(OH)2), stannate écrit tétrahydraté alors que la forme commerciale est trihydratée. Annoté |

## Contrôle croisé (`compare.py`)

Matériaux présents dans plusieurs publications du palier : SiO2 (4), Ag (4), g-C3N4, ZnO, TiO2, NiFe2O4, CsPbBr3, CdS et Au (2 chacun).

- **NiFe2O4 :** les tailles de cristallites sont comparables (13–25 nm en synthèse verte, 17 nm en couche recuite à 600 °C). La capacité de 1169 F/g de PMC10574157 sort du lot ; elle dépasse la limite faradaïque, c'est annoté.
- **CsPbBr3 :** injection à chaud à 170 °C (PMC10870029) contre précipitation à température ambiante (PMC5122874). Les « 0.69 mg » de PbBr2 de PMC10870029 sont 100 fois en dessous de la recette de Protesescu : coquille probable, annotée.
- **g-C3N4 :** 5,5 m²/g pour la mélamine sous air (PMC10460902) contre 27,4 m²/g (PMC9078232). L'écart est plausible (durée et récipient différents) mais à garder en tête.
- **ZnO et CdS :** voies et résultats cohérents entre publications.

## Sources du critique scientifique

Crossref est bloqué depuis le cloud, donc `sources_check.py` n'a pas pu tourner. Les 144 DOI des 40 nouvelles publications sont listés dans `palier_002_doi_a_verifier.txt`. Les 64 DOI du test sont dans `test_10_palier2.md`. Tous sont à vérifier depuis le PC (`python -I sources_check.py --palier 2 10`, puis la liste complète).

Trois sources ont été contrôlées par recherche web :
- **10.1021/jf048741x :** Apak et al. 2004, méthode CUPRAC, réduction de Cu(II) par les polyphénols. Conforme à ce que la critique lui attribue.
- **10.1016/0376-7388(95)00102-I :** Wijmans et Baker 1995, « The solution-diffusion model: a review ». Conforme.
- **10.1039/C2DT32073H :** Vuong, Pham et Do, Dalton Trans. 2013, 42, 550. La source existe, mais elle porte sur le nœud Fe2Ni(μ3-O) du MIL-88B, pas sur Fe2Co. L'annotation de PMC10372942 a été corrigée : elle cite maintenant cette source par analogie, en disant que l'article porte sur le nickel. La source n'est pas inventée, l'attribution était imprécise : pas d'anomalie bloquante.

## Règles et outils modifiés pendant le palier

- **RUNBOOK.md :** ajout du rôle `hydrolysis_agent` (eau d'hydrolyse en sol-gel) et du rôle `carbon_source` (vu deux fois : PMC3293091, PMC9475401), et de la règle « Périmètre : bioprocédé » (décision de l'utilisateur).
- **load.py :** reconnaissance du signe moins typographié « – » et de la notation « 1,73 × 10−4 » (faux positifs de recopie). Les contrôles ne sont pas affaiblis.
- **diff_valeurs.py :** le chemin de git est rendu portable, et la comparaison se fait sur la copie prise au chargement.
- **Prompts des critiques :** seul `review.py` est autorisé ; l'orchestrateur lance lui-même `critic_load.py`.

## Coût en jetons (agents seuls, hors orchestrateur)

| Passe | Médiane par publication |
|---|---|
| Extraction (Sonnet) | 171 k |
| Critique de fidélité (Sonnet) | 148 k |
| Critique scientifique (Opus) | 171 k |
| Correction (Sonnet) | 141 k |
| **Total par publication** | **≈ 0,63 M** (31,8 M pour le palier) |

Le palier 1 coûtait environ 0,9 M par publication, soit une baisse d'environ 30 % à rigueur égale.

## Ce qui n'a pas été vérifié

- Les DOI sur Crossref (cloud) : liste à passer depuis le PC.
- Les pages sources elles-mêmes : la plupart des sites d'éditeurs sont injoignables depuis le proxy du cloud. Les critiques se sont appuyés sur les extraits des moteurs de recherche.
- Les valeurs de manuel citées de mémoire par les critiques (tables de vapeur, paramètres de maille), signalées dans `sources_not_found` de chaque fichier `_science.json`.
