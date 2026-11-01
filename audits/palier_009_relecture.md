# Relecture du palier 9 (publications 401 à 450)

Sessions cloud des 22 et 24–25 octobre 2026, 3 agents en parallèle. Une limite d'usage le 22/10 vers 17 h UTC (reprise à 19 h 22 UTC). Pipeline habituel : extraction → chargement → critique de fidélité → critique scientifique → correction → clôture. Le scratchpad a été recréé le 24/10 à partir de `audits/attente/` (nouveau conteneur).

## Bilan

- **Volume :** 50 publications closes, 566 voies, 9 719 citations vérifiées, toutes exactes ; 759 résultats lus sur figure.
- **Audit :** `audit.py 9` donne 0 bloquant et 0 avertissement ouvert après traitement. Le seul bloquant (relecture intégrale de PMC3212207 non faite) a été levé par la relecture. Sur 16 avertissements : 14 faux positifs acceptés, 2 erreurs d'extraction corrigées (voir plus bas).
- **Relectures intégrales :** 11 publications, 1 258 valeurs contrôlées, 0 fausse. Faites par agents Sonnet en lecture seule (modèle `audits/attente/T_rev.txt`).
- **Critique de fidélité :** 424 constats (médiane 8,5 par publication, de 4 à 17) : 414 corrigés, 10 rejetés avec raison. Par nature : 180 mineurs, 148 manquants, 53 déduits (héritage non fondé surtout), 21 attributions, 18 non cités à tort, 4 faux (0,9 %).
- **Critique scientifique :** 320 jugements de voie (170 douteuses, 106 cohérentes, 35 invérifiables, 9 incohérentes) ; 1 443 contrôles : 267 ok, 861 réserves, 315 problèmes. Tous les problèmes viennent de l'article et sont rangés en annotations `limite_reproductibilite`, jamais en correction de valeur.
- **Coût :** médiane de 0,69 M jetons par publication (moyenne 0,73 M, total 36,7 M pour les 50, relectures intégrales comprises), hors orchestrateur. Médianes par passe : extraction 175 k, critique de fidélité 154 k, critique scientifique 190 k, correction 155 k, relecture intégrale 106 k.

## Relectures intégrales (agents Sonnet, lecture seule)

| Publication | Valeurs contrôlées | Fausses |
|---|---|---|
| PMC10059734 | 60 | 0 |
| PMC10698638 | 70 | 0 |
| PMC5793535 | 148 | 0 |
| PMC12693316 | 181 | 0 |
| PMC6915586 | 113 | 0 |
| PMC9136838 | 146 | 0 |
| PMC8360258 | 122 | 0 |
| PMC6804187 | 171 | 0 |
| PMC7563594 | 105 | 0 |
| PMC11280918 | 60 | 0 |
| PMC3212207 | 82 | 0 |

Points signalés, non comptés comme erreurs : contradictions de l'article recopiées fidèlement (Fig. 7c contre texte dans PMC10059734 ; 92 % contre ≈ 96 % dans PMC10698638 ; foie « close to 10 » contre ≈ 12 sur la Fig. 6 dans PMC6804187 ; rejets section 3.4 contre Conclusions dans PMC7563594) ; attributions par déduction déjà en doute (mobilités de PMC3212207, fournisseur générique de PMC11280918). Plusieurs relectures ont été rapides (25 à 45 s) ; l'échantillon de 30 valeurs ci-dessous a été relu par l'orchestrateur pour recouper.

## Échantillon de 30 valeurs du rapport d'audit

30 lignes relues (citation contre valeur, étape et branche) : 28 sans réserve, 2 remarques, aucune fausse.

- PMC7503313 `O-CDs_70C_180mM_40min` : « HCl replaced by dichloromethane » est une lecture de la phrase sur l'arrêt par CH2Cl2 ; la citation la soutient, la formulation en remplacement est un choix de structure (correction du 24/10).
- PMC10511489 `S12` étape 4, 4 h : rangée de tableau « 12 / NaOH / 333 / 4 / 353 / 48 / CHA » lue colonne par colonne (333 K pendant 4 h puis 353 K pendant 48 h), conforme à l'en-tête.
- Valeurs fautives de l'article gardées littérales et annotées : « 15 atm » de PMC9042205 (15 psi).

## Stœchiométrie et cohérence (5 voies, calculs de la critique scientifique recontrôlés)

| Voie | Contrôle | Résultat |
|---|---|---|
| PMC10511489 S8 | 0,96 g de NaOH = 24,0 mmol ; 0,96 g de KOH = 17,1 mmol ; OH/Si 2,1 contre 1,5 | comparaison NaOH/KOH à deux variables, annotée |
| PMC5887100 ACD-DIPA | 1 mL de diisopropylamine (ρ 0,722, M 101,2) = 7,14 mmol contre 0,5 mmol pour les autres précurseurs | comparaison non équimolaire, annotée |
| PMC10420257 éthanol | 4,39 g d'acétate de zinc dihydraté (M 219,5) = 20,0 mmol dans 70 mL d'éthanol (55 g) = 7,9 g/100 g | au-dessus de la solubilité à 25 °C, annotée |
| PMC6804187 [3]− | 750 mg de composé 2 à 408,9 g/mol = 1,834 mmol contre 1,209 mmol annoncés | quantité incohérente, KSAc en défaut, annotée |
| PMC8103248 libération | 75 mg dans 50 mL = 1 500 mg/L ; 67–73 ppm d'Ag supposent ≈ 4,7 % m/m d'Ag contre ≈ 2 % de charge | bilan de matière impossible, annoté |

Aucune de ces anomalies n'est une erreur d'extraction : les citations sont conformes ; chaque incohérence est gardée littérale, avec un doute et une annotation `limite_reproductibilite`.

## Anomalies de l'audit (16 avertissements)

- **Corrigées (2) :** branches « identiques » de PMC8830207 (`T-cat0.1C` et `T-cat0.1D` ne portaient pas la variation du second ligand, acide citrique ou diéthanolamine) et de PMC10631235 (deux nanoplaquettes Raman sans la variation de morphologie d'interface). Variation ajoutée avec sa citation, rechargées, statuts des critiques conservés.
- **Acceptées (14), faux positifs :** éléments apportés par une voie intermédiaire (Al, Fe, S, Cs ; 7) ; solvant à bas point d'ébullition détecté alors qu'il ne sert qu'au lavage (éther dibenzylique de PMC10059734, TOP/HDA de PMC3833402 ; 4) ; gélification puis autocombustion à 120 °C (PMC10249076) ; rampe en « min » (PMC9418562 ; 2).

## Sources citées par les critiques scientifiques

Crossref reste bloqué depuis le cloud. Les 278 DOI cités (50 publications) sont dans `audits/palier_009_doi_a_verifier.txt`, un par publication, dédoublonnés. Trois DOI reconstruits ou déduits par les critiques sans avoir été vus ont été retirés des fichiers de critique par l'orchestrateur (PMC6985175, PMC10249076, PMC5746929) ; les corrections n'en citent aucun.

## Contrôle croisé

`compare.py "ZIF-8"` : 29 voies de base. Le Zn-Mn-ZIF de PMC13368945 annonce 1 657 m2/g avec 0,36 cm3/g, volume poreux bas pour cette surface (ZIF-8 de référence ≈ 0,64 cm3/g) ; déjà annoté par la critique scientifique.

## Constats récurrents du palier (déjà couverts par RUNBOOK.md et PROMPT_CORRECTION.md)

- **Tests du dispositif ou du matériau fini rangés en branches :** hybridation d'ADN de PMC3212207 (branche « mésappariement » supprimée, résultats rangés en essais).
- **Héritage non fondé dans des branches :** PMC12917697 (`Cur_low` détachée de sa voie parente par l'orchestrateur), PMC7503313, PMC7563594 (GO-0).
- **Valeur de littérature rangée en résultat :** PMC5707940 (446 mg/g), PMC6985175 (indice 1,462).
- **Pseudo-rendement :** PMC9042205 (masse restante en ATG rangée en `yield`).
- **DOI de mémoire chez les critiques scientifiques :** retirés (voir plus haut).

## Branches `verif` et `docs`

Aucun commit nouveau à fusionner au moment de l'audit.

## Règles ajoutées à RUNBOOK.md

Aucune. Les erreurs vues sont déjà des règles (tests en résultats, héritage non fondé, littérature hors résultats, pas de DOI non vérifié).
