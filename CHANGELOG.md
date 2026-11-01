# Changelog

Un palier = 50 publications closes et auditées. Sources : `audits/palier_00N_relecture.md`, `state.py status`, `synthese.db` (lecture seule). État au 28 octobre 2026 : cible de 500 publications atteinte.

## Version anglaise de la méthodologie v1 (1er novembre 2026)
Hors palier. `README.md` traduit intégralement depuis `README.fr.md` (mêmes sections 1 à 14, mêmes tableaux et chiffres) ; blocs générés repris tels quels ; titre anglais de la section 7 fixé dans `analyses/build_site.py`.

## Méthodologie v1 restructurée (30 octobre 2026)
Hors palier. `README.fr.md` réorganisé à la demande de l'utilisateur : Europe PMC présentée (opérateur, financeurs, volume, activité, qui y publie) ; conversion des articles (texte, tableaux, figures, annexes, références) et pourquoi ; pipeline expliqué en clair puis en détail, avec un nouveau schéma des consignes et règles strictes par agent (`docs/img/accueil/pipeline_detail_*`) ; choix des modèles ; critères de validité d'une extraction ; nettoyage de la base (vocabulaire canonique, méthodes fusionnées) ; résultats sans comparaison entre paliers ; critique des résultats (besoin d'une grille stricte par méthode et par caractérisation) ; intérêt du travail et v2 ; limites mesurées (nombres manquants, paramètres non cités, ré-extraction à l'aveugle).

## Page d'accueil visuelle (28 octobre 2026)
Hors palier. README.md et README.fr.md s'ouvrent sur des images : schéma du pipeline, huit chiffres clés, modèle de données, exemple dessiné (PMC6199062, Sb₂S₃ à 120, 150 et 180 °C, valeurs lues dans l'extraction) et grille de neuf graphiques à légende courte ; détail de l'analyse en sections repliables. Chaque image existe en clair et en sombre (`<picture>`). Chiffres clés (demande de l'utilisateur) : publications étudiées, voies extraites, matériaux différents (couples composition-phase), méthodes, part de paramètres communs par méthode et de propriétés communes par famille (Jaccard), prix API de l'extraction sur l'historique complet des jetons ; calculés par `analyses/chiffres_accueil.py` (base en lecture seule). Tout est régénéré par `python3 -I analyses/build_site.py`, qui appelle le nouveau `analyses/build_visuels.py` (sorties `docs/img/accueil/`, variantes `docs/img/*_dark.svg`).

## Audit de contenu et vérification de la base (28 octobre 2026)
Hors palier. `analyses/audit_contenu.py` : types de synthèse (29 classes de méthode), 73 propriétés canoniques, conditions par voie, trous, qualité, limites, mécanismes, références. `analyses/audit_parametres.py` et `analyses/audit_verification.py` : profils de paramètres par méthode, paramètres essentiels cités / déclarés absents / hors grille, branches sans résultat, stœchiométrie nominale, synonymes, conversions SI. Ré-extraction à l'aveugle de 20 publications (`analyses/check_blind.py`, `analyses/compare_blind.py`, `audits/verification/aveugle/`) : paramètres concordants à 91,5 %, résultats à 84 %, 0 conflit sur valeur univoque. Rapports `audits/audit_contenu.md` et `audits/audit_verification.md` ; tableau de bord interactif (claude.ai) ; page publique `docs/index.html` (onglets Présentation / Analyse, FR / EN) et blocs « Analyse » des README, générés par `analyses/build_site.py`.

## Palier 10 — publications 451 à 500 (25 octobre 2026) — cible atteinte
549 voies, 9 498 citations exactes, 10 relectures intégrales (1 222 valeurs, 3 fausses corrigées dans PMC5369406), 446 constats (médiane 9, 11 « faux »), 0 bloquant, 39 avertissements acceptés et 2 corrigés, 0,71 M jetons. 247 DOI à vérifier.

## Palier 9 — publications 401 à 450 (22–25 octobre 2026)
566 voies, 9 719 citations exactes, 11 relectures intégrales (1 258 valeurs, 0 fausse), 424 constats (médiane 8,5, 4 « faux »), 0 bloquant, 14 avertissements acceptés et 2 corrigés, 0,69 M jetons. 278 DOI à vérifier.

## Palier 8 — publications 351 à 400 (18–22 octobre 2026)
515 voies, 9 859 citations exactes, 8 relectures intégrales (1 181 valeurs, 1 fausse corrigée dans PMC5535248), 437 constats (médiane 9, 11 « faux »), 0 bloquant, 134 avertissements acceptés, 0,67 M jetons. 259 DOI à vérifier.

## Palier 7 — publications 301 à 350 (18 octobre 2026)
424 voies, 9 238 citations exactes, 9 relectures intégrales (1 032 valeurs, 2 fausses corrigées dans PMC9034275), 421 constats (médiane 8, 9 « faux »), 0 bloquant, 46 avertissements acceptés, 0,69 M jetons. Défaut relevé : `sections.py` aplatit les exposants du XML (`10<sup>5</sup>` devient `105`). 
Le prompt de correction a été nettoyé de décisions résiduelles d'une autre publication.

## Palier 6 — publications 251 à 300 (17–18 octobre 2026)
554 voies, 9 680 citations exactes, 10 relectures intégrales (1 887 valeurs, 0 fausse), 419 constats (médiane 8, 3 « faux »), 0 bloquant, 56 avertissements acceptés, 0,65 M jetons. Trois sessions cloud en parallèle (orchestrateur, vérification, documentation). 

## Palier 5 — publications 201 à 250 (15–17 octobre 2026)
466 voies, 9 581 citations exactes, 9 relectures intégrales (1 112 valeurs, 0 fausse), 428 constats de fidélité (médiane 8, 4 « faux »), 0 bloquant, 35 avertissements acceptés, 0,66 M jetons par publication. Défaut de `sections.py` corrigé et 4 publications closes complétées. 176 DOI à vérifier.

## Palier 4 — publications 151 à 200 (14 octobre 2026)
515 voies, 9 920 citations exactes, 5 relectures intégrales (529 valeurs, 0 fausse), 406 constats (médiane 8, 7 « faux »), 17 avertissements acceptés, 0,625 M jetons. 132 DOI à vérifier.

## Palier 3 — publications 101 à 150 (13–14 octobre 2026)
556 voies, 10 050 citations exactes, 8 relectures intégrales (981 valeurs, 0 fausse), 435 constats (médiane 8,5, 5 « faux »), 0,605 M jetons. Paliers 3 et 4 lancés ensemble sur 100 publications, parallélisation maximale. 123 DOI à vérifier.

## Palier 2 — publications 51 à 100 (13 octobre 2026)
581 voies, 8 796 citations exactes, 9 relectures intégrales (776 valeurs, 0 fausse), 403 constats (médiane 8, 7 « faux »), 0,63 M jetons. Ajouts à `methodologie/RUNBOOK.md` : rôles `hydrolysis_agent` et `carbon_source`, règle de périmètre bioprocédé. Journaux de décisions des agents (`journaux/`). Précédé d'un test de 10 publications (`audits/test_10_palier2.md` : médiane 5 constats, 0,67 M jetons). 144 DOI à vérifier.

## Palier 1 — publications 1 à 50 (jusqu'au 13 octobre 2026)
609 voies, 8 712 citations exactes, 20 relectures intégrales (1 307 valeurs, 10 fausses, toutes dans les 10 publications de calibrage, devenues des règles), 526 constats (médiane 10, 29 « faux »), ≈ 0,9 M jetons. Format 2 (grille de reproductibilité, critiques, annexes et figures). 8 DOI sur 10 confirmés par Crossref. Leçons : `audits/palier_001_lecons.md`.
