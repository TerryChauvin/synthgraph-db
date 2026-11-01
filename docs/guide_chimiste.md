<p align="center"><a href="chemist_guide.md">English</a> · <b>Français</b></p>

# Guide du chimiste : lire une fiche et interroger la base

Chiffres au 17 octobre 2026 (`synthese.db`, requêtes SELECT en lecture seule). Pour la méthode : [methodologie.md](methodologie.md). Pour ce qu'il ne faut pas croire sans vérifier : [limites_et_avertissements.md](limites_et_avertissements.md).

## 1. Lire une fiche

Chaque publication a une fiche `fiches/<PMCID>.md` (270 fiches), générée par `python3 -I fiche.py <PMCID>`. Exemple court et propre : `fiches/PMC6199062.md`. Ordre d'une fiche :

1. **Avant de refaire** : les limites de reproductibilité et les consignes de sécurité. À lire en premier.
2. **Résumé, objectif, pourquoi ces données, comparaison des branches, tendance observée** : interprétations en français, séparées des données.
3. **Une section par voie** : matériau, méthode, complétude, rendement, tableau des réactifs, étapes numérotées avec leurs paramètres, chacun suivi de la citation de l'article.

Règle de lecture : **la citation fait foi**. Si la valeur et la citation divergent à vos yeux, croyez la citation et signalez-le.

## 2. Le vocabulaire de la base

| Terme | Sens |
|---|---|
| **`not_stated`** (affiché **non cité**) | Information cherchée et absente de l'article (ou seulement implicite). Ce n'est pas zéro ni « par défaut » : c'est à déterminer par vous. La table `not_stated` (15 214 lignes) liste, par voie, les réactifs, étapes ou grandeurs manquants (`scope` = `reagent`, `step` ou `route`). |
| **Voie de base / branche** | Une voie de base est le protocole complet. Une branche (`parent_route_id` non nul) ne décrit que ce qu'elle change par rapport à son parent : température, durée, réactif, rapport… La table `route_variations` donne la valeur de la branche et celle du parent. Les paramètres non redéfinis sont ceux du parent (colonne `overridden_by_branch` de `v_route_complete`). |
| **Doute** (`doubts`) | Ambiguïté rencontrée à l'extraction (unité douteuse, attribution d'une rangée de tableau…). Tous ont une résolution écrite sauf ceux au statut `open` (14 au 17/10/2026). |
| **`limite_reproductibilite`** | Annotation : ce qu'un chimiste doit savoir avant de refaire (manque, incohérence de l'article, annexe absente, précaution). Elle décrit une limite ; elle ne corrige jamais une valeur. 2 399 au total. |
| **`from_figure`** | Valeur lue sur une figure, pas écrite dans le texte. La citation est alors la légende de la figure et `from_figure` donne le panneau (« Fig. 3b »). Lecture approximative (2 chiffres significatifs au plus). Au 17/10/2026 : 3 416 résultats, 158 variations et 35 paramètres sont marqués ainsi (la colonne est vide pour les valeurs écrites dans le texte). |
| **`succeeded = 0`** | Essai raté ou produit non obtenu, conservé exprès. |
| **Complétude** | Score de 0 à 1 de ce que la voie permet de refaire. Un score bas ≠ erreur : l'article est lacunaire. |
| **Verdict de plausibilité** | Jugement de la critique scientifique par voie : `coherente`, `douteuse`, `incoherente`, `inverifiable`. « douteuse » recouvre surtout des réserves (information manquante, témoin à plusieurs variables). Les mécanismes (`mecanisme_analyse`) sont des **hypothèses**, pas des résultats. |

Types d'annotation : `limite_reproductibilite`, `tendance_observee`, `mecanisme_analyse`, `mecanisme_auteurs`, `securite_analyse`, `securite_auteurs`, `comparaison_branches`, `pourquoi_ces_donnees`, `resume`, `objectif_etude`, `conclusion_auteurs`.

## 3. Cinq requêtes SQL testées

La base est un fichier SQLite : DB Browser for SQLite, DBeaver, ou Python (`sqlite3.connect("file:synthese.db?mode=ro", uri=True)`). Les cinq requêtes ci-dessous ont été exécutées le 17/10/2026 sur `PMC6199062` (Sb2S3 hydrothermal, température 120/150/180 °C).

**1. Protocole complet d'une branche, avec citations.**

```sql
SELECT step_order, action, parameter, value_num, value_text, unit, quote
FROM v_route_complete
WHERE pmcid = 'PMC6199062' AND branch_label = 'Sb2S3-150'
ORDER BY step_order;
```
Résultat : étape 1 `dissolve` 15 min, étape 3 `heat` 150 °C et 12 h, étape 4 `wash`… chacune avec sa citation.

**2. Effet d'une variation sur le résultat.**

```sql
SELECT branch_label, parent_label, branch_value, variation_unit, parent_value,
       property, outcome_value
FROM v_comparaison
WHERE pmcid = 'PMC6199062' AND parameter = 'temperature'
ORDER BY branch_label;
```
Exemple de ligne : `Sb2S3-120` contre `Sb2S3-150`, 120 °C contre 150 °C, phase « orthorhombic Sb2S3 phase and monoclinic Sb8O11Cl2 phase », nanofils de 80 à 100 nm.

**3. Ce que l'article ne dit pas.**

```sql
SELECT r.branch_label, n.scope, n.step_order, n.reagent, n.name
FROM not_stated n
JOIN synthesis_routes r ON r.id = n.route_id
JOIN papers p ON p.id = r.paper_id
WHERE p.pmcid = 'PMC6199062' AND n.status = 'non_cite';
```
Pour la voie `Electrode_Sb2S3` : rendement, collecteur, méthode d'enduction, séchage, surface d'électrode.

**4. Ce qu'il faut savoir avant de refaire.**

```sql
SELECT r.branch_label, a.text
FROM annotations a
JOIN papers p ON p.id = a.paper_id
LEFT JOIN synthesis_routes r ON r.id = a.route_id
WHERE p.pmcid = 'PMC6199062' AND a.type = 'limite_reproductibilite';
```
`branch_label` vide = limite valable pour tout l'article.

**5. Valeurs lues sur figure (à prendre avec prudence), ou voies bien documentées d'une méthode.**

```sql
SELECT p.pmcid, r.branch_label, o.property, o.value_num, o.unit, o.from_figure
FROM outcomes o
JOIN synthesis_routes r ON r.id = o.route_id
JOIN papers p ON p.id = r.paper_id
WHERE o.from_figure IS NOT NULL;
-- from_figure contient le panneau (« Fig. 3b »)
```
Variante pour chercher des voies hydrothermales presque complètes :
```sql
SELECT p.pmcid, r.branch_label, ROUND(r.completeness_score, 2) AS completude
FROM synthesis_routes r JOIN papers p ON p.id = r.paper_id
WHERE r.parent_route_id IS NULL AND r.completeness_score >= 0.9
  AND r.method LIKE '%hydrothermal%';
```

## 4. Lire `compare.py`

`python3 -I compare.py "ZnO"` liste les **voies de base** dont le matériau (nom ou formule) contient le mot entier demandé : 31 voies de base pour « ZnO » au 17/10/2026. Pour chacune : publication, libellé, nombre de branches, matériau et phase, `méthode`, `conditions` (température, durée, pH, atmosphère par étape, forme `étape:paramètre=valeur`) et `résultats` (propriété=valeur). Usage : comparer les conditions que diverses équipes utilisent pour un même matériau et repérer une valeur très éloignée des autres. Attention : la casse compte pour une formule (« Ag » ne ramène ni « fragment » ni « AgCl »), et deux publications ne sont comparables que si leurs échelles et leurs grandeurs mesurées le sont ; lisez la citation avant de conclure.
