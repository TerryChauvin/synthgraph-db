# Relecture du palier 7 (publications 301 à 350)

Session cloud du 18 octobre 2026, 3 agents en parallèle (période autorisée jusqu'au 18/10 à 17 h Paris). Pipeline habituel : extraction → chargement → critique de fidélité → critique scientifique → correction → clôture.

## Bilan

- **Volume :** 50 publications closes, 424 voies, 9 238 citations vérifiées, toutes exactes.
- **Audit :** `audit.py 7` donne 0 bloquant et 0 avertissement ouvert. Le seul bloquant initial était un doute que la relecture intégrale venait d'ajouter (PMC9034275), résolu. Les 46 avertissements sont tous des faux positifs ou des limites de l'article, acceptés un par un (voir plus bas).
- **Relectures intégrales :** 9 publications, 1 032 valeurs contrôlées, 2 fausses (PMC9034275), corrigées et rechargées. Faites par agents Sonnet en lecture seule.
- **Critique de fidélité :** 421 constats (médiane 8 par publication) : 409 corrigés, 12 rejetés avec raison. Par nature : 178 mineurs, 153 manquants, 50 déduits (héritage non fondé), 16 non cités à tort, 15 attributions, 9 faux (2 %).
- **Critique scientifique :** 289 jugements de voie (135 douteuses, 122 cohérentes, 24 invérifiables, 8 incohérentes) ; 1 309 contrôles : 280 ok, 772 réserves, 257 problèmes. Tous les problèmes viennent de l'article et sont rangés en annotations `limite_reproductibilite`, jamais en correction de valeur.
- **Coût :** médiane de 0,69 M jetons par publication (moyenne 0,68 M, total 34,2 M pour les 50), hors orchestrateur. Médianes par passe : extraction 178 k, critique de fidélité 159 k, critique scientifique 189 k, correction 151 k. Une relecture intégrale par agent coûte en moyenne 80 k jetons par publication.

## Relectures intégrales (agents Sonnet, lecture seule)

| Publication | Valeurs contrôlées | Fausses |
|---|---|---|
| PMC6814701 | 121 | 0 |
| PMC9036664 | 49 | 0 |
| PMC10966523 | 120 | 0 |
| PMC8866530 | 185 | 0 |
| PMC9034275 | 119 | 2 |
| PMC9036896 | 47 | 0 |
| PMC9609168 | 148 | 0 |
| PMC11904774 | 191 | 0 |
| PMC11012633 | 52 | 0 |

- **PMC9034275 :** les résultats `organic_content` de `Tube_Na010_2h` et `Tube_Na010_4h` portaient 16 wt % alors que la citation ne donne cette valeur que pour Na2O/SiO2 = 0,15 (pour 0,10 elle dit seulement que la tendance est la même, valeur dans le Tableau S3 absent du dépôt). Valeur numérique retirée, doute ajouté, base rechargée.
- Points signalés, non comptés comme erreurs : incohérences d'article recopiées fidèlement (12,0 g pour 0,1 mol de mélamine, PMC9036664 ; total 91 % pour 550 °C, PMC8866530 ; trois récupérations du Tableau S3 de PMC9036896 qui ne suivent pas détecté/ajouté) ; rattachement par déduction des 0,17 g de ZnBr2 au rapport Br:Pb = 6:1 (PMC11012633), en doute et cohérent avec le bilan de matière.

## Échantillon de 30 valeurs du rapport d'audit

30 lignes relues (citation contre valeur, étape et branche) : 29 sans réserve, 1 remarque, aucune fausse.

- PMC4951059 `Bars_Si` étape 3 `duration_dry` (2,0 min) : la citation est une rangée de tableau de cuisson de la porcelaine sans en-tête de colonne ; l'attribution de la colonne se fait par l'ordre du tableau.
- Valeurs textuelles (« slowly », « overnight », « thrice », « 5 min », « 0,45 μm » de filtre) : conformes, gardées en `value_text` quand l'article ne chiffre pas.
- Variations (PMC7747735 régénération 15Co/900MA, PMC8966659 KF à la place de K2SO4) : la citation soutient bien le remplacement.

## Stœchiométrie et cohérence (5 voies, par la critique scientifique et vérifiées dans ses blocs `calculs`)

| Voie | Contrôle | Résultat |
|---|---|---|
| PMC11012633 CsPbBr3_150C | Br:Pb = 6,02 avec 0,17 g de ZnBr2, 10,03 avec le double ; Cs-oléate 0,123 M (0,125 M annoncé) ; Cs limitant | cohérent ; incertitudes de taille de 1 à 3 % peu crédibles comme écart type (annotées) |
| PMC9038048 gnp-citrate | 7,88 mg HAuCl4·3H2O = 0,0200 mmol Au ; 400 mg de citrate trisodique dihydraté = 1,36 mmol ; 68:1, ≈ 57 mM de citrate libre | arithmétique recalculée par l'agent de correction ; le rapport est ≫ Turkevich (0,5 à 4:1), annoté ; l'exposant 10⁵ μg mL⁻¹ avait été aplati en 105 par la conversion du texte |
| PMC11904774 CQD_2.5_180_12h | carbone dans le gaz = n(CO+CO2) × 12 / 10 g, donc rapporté à la masse de coque ; bilan O et pression du réacteur | incohérences de l'article (gaz seul = 72 % du carbone apporté à l'optimum, 103 % à 210 °C ; besoin d'oxygène > H2O2 disponible) annotées |
| PMC8981973 UiO-66-2HBr | volumes d'acide du Tableau S1 = n × M / densité (acide pur) ; « 1 éq. » ≈ 0,37 à 0,40 éq. réel ; RME maximal d'un UiO-66 sec 69,7 % | incohérences de l'article, annotées (RME de 80 à 112 % annoncés) |
| PMC10967699 PCN-600-NS-10 | ΔGads du Tableau 2 = −RT exactement ; −RT ln Kd = −3,43 / −3,92 / −4,47 kJ/mol ; dose ×10 | incohérences de l'article, annotées (ΔH de signe inversé, « exothermic » faux) |

Aucune de ces anomalies n'est une erreur d'extraction : les citations sont conformes ; chaque incohérence est gardée littérale, avec un doute et une annotation `limite_reproductibilite`.

## Anomalies de l'audit (46 avertissements, tous acceptés)

- **Éléments du produit sans source parmi les réactifs (32) :** faux positifs du contrôle chimique. Produits LLZO obtenus de poudres commerciales ou de références (PMC9041118, 9) ; CsPbBr3 de précurseurs désignés par une abréviation (PMC10966523 et PMC11012633, 17) ; MgAl2O4 (PMC7747735, 4) ; produits nommés par formule composée (PPN-TFSI, Al(OH)(PZDC), 2).
- **Voie de base sans réactif (6) :** poudres commerciales ou substrats (PMC9041118 ×4, PMC9912144, PMC5978183), la matière première est la voie elle-même.
- **Branches identiques (1) :** A2′, A3′, A4′ (PMC11931415), résultats distincts, une seule variable déclarée par l'article.
- **Température au-dessus de l'ébullition du solvant (6) :** chauffage de gel ou de film sans solvant, ou autoclave implicite (PMC10815866, PMC5302706, PMC7759625, PMC9034275 ×2).
- **Unité non reconnue (1) :** `fs` (durée d'impulsion laser, PMC9147655).
- **Vitesse de chauffe invraisemblable (1) :** 350 °C est la température du substrat (PMC8433875).

## Constats récurrents du palier (déjà couverts par RUNBOOK.md et PROMPT_CORRECTION.md)

- **Héritage non fondé** vers une branche, une série ou un témoin (50 constats « déduit ») : NFM (PMC10815866), DSSC_N3_only (PMC11904774), films rGO (PMC9419793), branches d'optimisation (PMC3998862), DPPH de l'extrait (PMC9609168). Corrigé en `not_stated` avec doute.
- **Citations qui ne portent pas la valeur** (PMC9034275) : repérées à la relecture intégrale.
- **Rattachement d'une analyse de données en `method_sources`** (PMC9609168, PMC3998862) : retiré ou passé en rôle « autre ».
- **Décisions résiduelles dans le modèle de prompt de correction** (`T_cor.txt` contenait les décisions d'une autre publication) : repéré par deux agents de correction qui ne les ont pas appliquées ; modèle nettoyé.

## Défaut de conversion du texte : exposants aplatis

`sections.py` aplatit les balises `<sup>` : le XML `10<sup>5</sup> μg mL<sup>−1</sup>` devient `105 μg mL−1` dans `corpus/text` (PMC9038048, vérifié dans le XML). Cas voisins vus dans le palier : `4.94 × 1015 cm−3` (PMC10967699), `more than 105 times` (PMC5302706). Pour PMC9038048 les valeurs hors citation ont été corrigées (« 105 μg mL−1, exposant aplati, XML : 10^5 μg mL−1 = 100 mg/mL ») et les citations laissées littérales. Une tâche séparée a été proposée à l'utilisateur pour mesurer l'ampleur sur les 350 publications sans casser les citations existantes (`load.py` exige des sous-chaînes exactes de `corpus/text`).

## Sources à vérifier depuis le PC

Crossref reste bloqué depuis le cloud. Les DOI cités par les critiques scientifiques mais non vérifiés sont dans `audits/palier_007_doi_a_verifier.txt` (liste brute par publication, avec du bruit).

## Règles ajoutées à RUNBOOK.md

Aucune. Les erreurs vues (héritage non fondé, citation de rang n'ayant pas la valeur, analyses de données en sources de méthode) sont déjà des règles ; elles ont été rappelées dans les consignes de correction.
