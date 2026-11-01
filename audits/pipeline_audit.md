# Audit du pipeline — 2026-10-12

Audit demandé par l'utilisateur au moment du passage au format 2 (grille de reproductibilité, annexes, critiques). Contrôles automatiques exécutés sur la base réelle (50 publications extraites, 615 articles téléchargés), plus revue des scripts.

## 1. Ce qui est vérifié et tient

| Contrôle | Résultat |
|---|---|
| Unicité des articles (`papers`, fichiers XML) | 615 lignes, 615 PMCID distincts, 615 XML |
| Cohérence base ↔ fichiers | aucun article en file sans texte, aucune extraction sans JSON |
| Intégrité référentielle SQLite | 0 violation de clé étrangère |
| Structure des voies | 0 voie de base sans étapes, 0 branche sans variation, 0 citation nulle |
| Citations après enrichissement du texte (annexes ajoutées en fin de fichier) | 2 709 positions revérifiées, 0 décalée |
| Vue `v_route_complete` | reconstitue bien une branche héritée (9 lignes) et une branche à étapes propres (9 lignes) ; 487 valeurs remplacées par une variation |
| `enrich.py` relancé sur un article déjà enrichi | fichier identique (idempotent) |
| `reload_all.py` (rechargement des 50 extractions) | mêmes effectifs avant/après dans toutes les tables ; rangs, paliers, relectures et doutes tranchés conservés |
| Auto-test de `load.py` (citation altérée, valeur absente de la citation, branche sans variation, pH impossible, cases de la grille oubliées ou contradictoires) | chaque cas est refusé |
| Test cloud (2026-10-12) | Python, `load.py check`, dépôt PMC, clonage Git, sous-agents : OK ; Europe PMC bloqué (403) |

Relectures humaines simulées : 17 publications relues intégralement (10 de calibrage + 7 tirées au hasard), 33 relues sur leurs doutes ; taux d'erreur de l'échantillon aléatoire : 0,15 %.

## 2. Défauts trouvés pendant l'audit et corrigés

- `audit.py` identifiait les anomalies par l'identifiant de ligne SQL, qui change à chaque rechargement : les acceptations étaient perdues. Cible remplacée par « voie / étape / paramètre ».
- 32 faux positifs du contrôle physique (unités « minutes », « hr », « mTorr », « °C·min–1 » ; débits pris pour des vitesses de chauffe ; pyrolyses comparées au point d'ébullition du solvant ; recuits doux de films ; « FA » lu comme du fluor ; cystéine non reconnue comme source de soufre). Corrigés dans `load.py` et `audit.py`.
- Nombres avec séparateur de milliers (« 1,226.1 ») refusés par le contrôle valeur-dans-citation. Corrigé.
- Les réactifs propres à une branche (dopant, additif) n'étaient pas comptés dans le score de complétude ni dans le bilan d'éléments. Corrigé.
- Titres d'articles avec balises HTML échappées. Corrigé.
- Les manques d'information étaient une liste libre non contrôlée : impossible de distinguer « l'article ne le dit pas » de « l'extracteur n'a pas cherché ». Remplacé par la grille `not_stated` contrôlée (format 2).
- Trouvés par les critiques pendant l'essai : `critic_load.py` effaçait les décisions de l'orchestrateur à chaque rechargement d'une critique (corrigé : statut et résolution conservés par constat) ; les verdicts du critique scientifique disparaissaient à chaque rechargement d'une extraction, par cascade sur les voies (corrigé : lien par label de voie, rétabli par `load.py`).
- Annexes, légendes de figures, notes de tableau et références bibliographiques n'étaient pas lues. `enrich.py` les ajoute ; 220 articles ont une annexe exploitable, 265 n'en ont pas dans le dépôt PMC.

## 3. Risques et limites qui restent

**Fidélité (valeur = article)**
- Le contrôle automatique garantit que la citation existe et contient le nombre ; il ne garantit pas que la citation parle du bon échantillon. C'est l'erreur dominante observée (attribution de rangées de tableaux, phrases « respectively »). Réponse : agent critique de seconde lecture (`CRITIQUE.md`), en cours de test.
- Les valeurs lues sur figures (format 2, `from_figure`) sont approximatives par nature et marquées comme telles.
- Le texte des annexes PDF est extrait sans mise en page : les tableaux d'annexe peuvent être difficiles à lire pour l'extracteur. À surveiller sur l'essai.

**Complétude (tout ce qu'il faut pour refaire)**
- Avant le format 2, un tiers des voies de base n'avait pas toutes ses quantités de précurseurs. Le format 2 rend ces trous explicites, il ne les comble que si l'information existe dans l'article ou ses annexes.
- Les publications sources (« as reported previously ») sont listées, pas encore extraites.
- Les 50 publications du palier 1 sont au format 1 : à remettre à niveau (`format1_to_upgrade` dans `state.py status`).

**Validité scientifique**
- Les contrôles physique/chimie de l'audit de palier sont des garde-fous grossiers (plages, bilan d'éléments, atmosphère). Le jugement de cohérence et de faisabilité est confié à l'agent critique scientifique (`PLAUSIBILITE.md`), qui doit s'appuyer sur des sources vérifiables ; ses sources seront contrôlées par échantillon (existence de l'URL ou du DOI).
- Rien ne remplace une reproduction au laboratoire.

**Exploitation**
- Europe PMC est bloqué dans le cloud : réapprovisionnement depuis le PC uniquement (552 articles en file aujourd'hui, assez pour 500 publications après rejets).
- PDF, annexes et figures sont hors du dépôt Git (volume) ; le texte des annexes, lui, est versionné.
- Coût : format 2 + deux critiques ≈ 3 à 4 fois le coût du format 1 par article.
- Les fichiers téléchargés (XML, PDF, annexes) sont des données non fiables ; ils sont lus par des bibliothèques (ElementTree, PyMuPDF), jamais exécutés, et les agents ont pour consigne de n'en suivre aucune instruction.

## 4. Décisions prises

1. Format 2 obligatoire pour toute nouvelle extraction ; mise à niveau des 50 premières publications avant le palier 2.
2. Deux critiques par publication : fidélité (Sonnet, sans web) et cohérence scientifique (Opus, avec recherche web et sources obligatoires). Leurs constats sont chargés dans les tables `critiques` et `plausibility` et tranchés par l'orchestrateur.
3. Audit de palier complété par : vérification d'un échantillon de sources citées par le critique scientifique, et contrôle croisé entre synthèses du même matériau (`compare.py`).
4. Bascule vers le cloud après validation du format 2 et des critiques sur les deux articles d'essai.
