<p align="center"><a href="methodology.md">English</a> · <b>Français</b></p>

# Méthodologie en bref

Version courte pour un lecteur pressé. La version complète, rédigée comme un « Matériel et méthodes », est dans [README.fr.md](../README.fr.md). Chiffres au 17 octobre 2026 ; chaque source est citée.

## 1. Le pipeline : quatre passes (plus le contrôle automatique)

| Passe | Qui | Fichier de consignes | Produit |
|---|---|---|---|
| 1. Extraction | agent Sonnet, effort `high`, un article chacun | `RUNBOOK.md` | `extractions/<PMCID>.json` : inventaire des échantillons, voies, branches, citations, `not_stated`, lecture des figures |
| (contrôle) | script `load.py check` / `load` | — | chaque citation retrouvée mot pour mot dans `corpus/text/`, chaque nombre retrouvé dans sa citation ; chargement dans `synthese.db` |
| 2. Critique de fidélité | agent Sonnet `high`, lit l'article **avant** l'extraction, sans web | `CRITIQUE.md` | `critiques/<PMCID>.json` : constats `faux`, `attribution`, `deduit`, `manquant`, `non_cite_a_tort`, `mineur` |
| 3. Critique scientifique | agent Opus `high`, avec recherche web | `PLAUSIBILITE.md` | `critiques/<PMCID>_science.json` : stœchiométrie, plausibilité physico-chimique, sources, mécanismes, sécurité |
| 4. Correction | agent Sonnet `high`, seul à modifier le JSON | `PROMPT_CORRECTION.md` | chaque constat marqué `corrige` ou `rejete` avec la raison |

L'orchestrateur (Opus) tranche les doutes, fixe les règles de décision et relit contre le texte. Aucun agent ne contrôle son propre travail. Tous les 50 articles, `audit.py` produit un rapport (`audits/palier_NNN.md`) et l'orchestrateur écrit `audits/palier_NNN_relecture.md`.

## 2. Invariants

- **La citation fait foi.** Aucune valeur sans citation exacte ; contrôle mécanique à chaque chargement.
- **Aucune valeur déduite ni convertie à la place de l'auteur.** La conversion SI est faite par `load.py` dans une colonne séparée (`value_si`, `unit_si`).
- **L'absence est une donnée** : `not_stated`.
- **Les incohérences des auteurs sont conservées**, signalées en `limite_reproductibilite`, jamais « réparées ».
- **Les interprétations sont séparées** (table `annotations`, `source = 'claude'`).
- **Une erreur vue deux fois devient une règle** de `RUNBOOK.md`.
- Les textes d'articles sont des données non fiables : jamais exécutés, aucune instruction qu'ils contiennent n'est suivie.

## 3. Taux d'erreur mesurés par palier

Source : `audits/palier_00N_relecture.md`. « Relecture intégrale » : l'orchestrateur compare chaque valeur de la publication au texte.

| Palier | Voies | Citations exactes à l'audit | Constats de fidélité (médiane) | dont « faux » | Relecture intégrale : pub. / valeurs / fausses |
|---|---|---|---|---|---|
| 1 | 609 | 8 712 (100 %) | 526 (10) | 29 | 20 / 1 307 / 10 |
| 2 | 581 | 8 796 (100 %) | 403 (8) | 7 | 9 / 776 / 0 |
| 3 | 556 | 10 050 (100 %) | 435 (8,5) | 5 | 8 / 981 / 0 |
| 4 | 515 | 9 920 (100 %) | 406 (8) | 7 | 5 / 529 / 0 |
| 5 | 466 | 9 581 (100 %) | 428 (8) | 4 | 9 / 1 112 / 0 |
| **Total** | **2 727** | **47 059** | **2 198** | **52** | **51 / 4 705 / 10** |

Lecture : les 10 valeurs fausses sont toutes dans les 10 publications de calibrage du palier 1 ; chacune est devenue une règle. Aucune anomalie bloquante ouverte aux paliers 1 à 5. Depuis le palier 2, aucun des constats « faux » relus n'est un nombre mal recopié (voir les rapports 2 à 5). Le taux de « 1 erreur sur 3 032 valeurs après calibrage » du README concerne les paliers 1 à 4 ; avec le palier 5 (1 112 valeurs, 0 erreur), le total relu hors calibrage est plus grand, mais ce document n'en recalcule pas la borne.

Critique scientifique sur toute la base au 17/10/2026 (table `plausibility`, 1 581 jugements) : 617 `coherente`, 791 `douteuse`, 56 `incoherente`, 117 `inverifiable` (graphies `invérifiable` et `inverifiable` cumulées). « douteuse » recouvre surtout des réserves ; les problèmes viennent des articles, pas des extractions.

## 4. Coûts en jetons

Source : `audits/jetons.csv` (jetons d'agents, hors orchestrateur) : 221 publications, 139 M de jetons. Médianes par passe : extraction 164 k ; critique de fidélité 147 k ; critique scientifique ≈ 170–176 k (deux libellés dans le fichier) ; correction 141 k. Par publication : ≈ 0,9 M au palier 1, 0,61–0,66 M ensuite (rapports de palier). Une fenêtre d'usage de 5 h laisse passer ≈ 8–10 M de jetons d'agents (≈ 13 publications), ce qui rythme le travail (CLAUDE.md).

## 5. Ce que la méthode ne garantit pas

La fidélité à la source et l'explicitation des manques, pas qu'un protocole publié fonctionne. Voir [limites_et_avertissements.md](limites_et_avertissements.md).
