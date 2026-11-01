# Registre des tests et analyses de contrôle

Chaque ligne : ce qui a été testé, l'hypothèse, le résultat, et si le test est **positif** (l'hypothèse ou la méthode tient) ou **négatif** (elle ne tient pas, et ce qui a changé ensuite). Mis à jour à chaque nouveau test. Détails dans les rapports cités.

## Construction de la base (paliers 1 à 10, 12–25/10/2026)

| Test | Hypothèse | Résultat | Verdict |
|---|---|---|---|
| Vérification mécanique des citations (`load.py`, chaque chargement et chaque audit) | chaque valeur a une citation exacte qui la contient | ≈ 95 000 citations, 100 % exactes | positif |
| Relectures intégrales (1 publication sur 5, 106 publications, ≈ 13 000 valeurs) | les valeurs sont justes, bien rattachées | 10 fausses sur 561 au calibrage (1,6 %), puis 6 sur ≈ 12 500 (≈ 0,05 %), toutes corrigées | positif après calibrage ; négatif au départ (règles ajoutées au RUNBOOK) |
| Critique de fidélité indépendante (500 publications) | une seconde lecture trouve peu d'erreurs | médiane 8–10 constats par publication, dont ≈ 2 % « faux » ; surtout des manques et des précisions | positif sur la justesse ; négatif sur l'exhaustivité d'une extraction seule (d'où la passe de correction) |
| Critique scientifique (500 publications) | les incohérences viennent des articles, pas de l'extraction | confirmé : problèmes d'auteurs restitués en annotations, aucune valeur changée sur cette base | positif |
| Audits de palier (10) | aucune anomalie bloquante | 0 bloquant ; avertissements surtout faux positifs du contrôle chimique | positif ; heuristique chimique trop bruyante (négatif sur l'outil) |
| Sources citées par la critique scientifique | les DOI existent | échantillons ouverts conformes ; ≈ 1 900 DOI restent à vérifier depuis le PC (Crossref bloqué) | non conclu |

## Après la cible (28/10/2026)

| Test | Hypothèse | Résultat | Verdict | Rapport |
|---|---|---|---|---|
| Ré-extraction à l'aveugle (20 publications) | une extraction indépendante retrouve les mêmes valeurs | paramètres concordants 91,5 %, résultats 84 %, 0 conflit sur valeur univoque ; la base contient 30 % de paramètres et 40 % de résultats de plus qu'une extraction seule | positif (justesse) | `audits/audit_verification.md` |
| Stœchiométrie nominale | les quantités de précurseurs correspondent à la formule visée | 24 des 60 voies vérifiables à 10 % près ; écarts surtout dus aux articles (excès voulus, formules nominales) | non conclu (contrôle partiel) | `audits/audit_verification.md` |
| Branches sans résultat propre | chaque branche a un résultat | 5,3 % sans résultat (24 % pour les MOF) | négatif localisé | `audits/audit_verification.md` |
| Paramètres essentiels par méthode | les paramètres essentiels sont cités ou déclarés absents | angles morts : refroidissement, débit de gaz, répétitions, puissance, remplissage d'autoclave | négatif (grille incomplète) | `audits/audit_verification.md` |
| Vocabulaire canonique (`canon.py`) | les noms bruts se ramènent à un vocabulaire commun | propriétés non classées 25,8 % → 9,1 % ; paramètres 0,9 % | positif | `docs/vocabulaire/README.md` |
| Sonde des manques (`sonde_manques.py`) | un terme présent sans rien d'extrait signale un manque | ≈ la moitié des alertes de procédé sont des faux positifs (réglages d'une mesure, pas de la synthèse) | négatif comme détecteur de valeurs ; utile pour les conditions de mesure | `audits/sonde_manques.md` |
| Pilote de complément (20 publications) | une passe guidée par la sonde ajoute des informations utiles, sans erreur | 27 paramètres, 223 `not_stated`, 187 conditions, 177 résultats ; 0 valeur retirée ; critique : 2 faux sur 217 (rattachements), 24 douteux | positif sur la justesse ; mitigé sur l'utilité (peu de paramètres, `not_stated` trop larges) | `audits/pilote_complement.md` |
| Couverture des valeurs (`couverture_valeurs.py`, sans agent) | la base contient les nombres de l'article | 95,5 % (expérimental), 88 % (résultats en texte), 81 % (tableaux) | positif dans l'ensemble | `audits/couverture_valeurs.md` |
| La sonde prédit-elle les valeurs manquantes ? | les publications à fortes alertes sont celles où manquent des valeurs | corrélation de rang 0,0 ; l'« option A » ne contenait que 44 % des valeurs absentes | **négatif** : option A abandonnée | `audits/couverture_valeurs.md` |
| Le pilote a-t-il comblé les valeurs absentes ? | oui | 1 % des cellules de tableaux, 11 % des nombres du texte | **négatif** : la consigne visait autre chose | `audits/couverture_valeurs.md` |
| Valeurs « hors périmètre » | littérature, statistiques, DFT, références sont inutiles | objection de l'utilisateur, retenue : elles servent à comprendre et comparer la mesure ; table `comparisons` et voies `calcul` ajoutées | négatif (périmètre élargi) | ce registre |

| Test de complétude (20 publications par strates) | l'extraction contient l'essentiel ; la mesure de couverture repère les publications à compléter | synthèse complète dans 20/20 ; 557 résultats, 178 conditions, 341 valeurs de littérature, 5 voies de calcul ajoutés ; couverture des tableaux 83 → 99,9 % ; témoins aussi lacunaires que les sélectionnées ; critique : 1 faux sur 630 hors erreur de source (réponses aux relecteurs, 25 faux, corrigée) | **positif** sur la synthèse ; **négatif** sur l'exhaustivité des propriétés et réglages ; **négatif** sur la sélection | `audits/test_completude.md` |
| Grille de synthèse (`load.py`) | chaque case attendue est citée ou déclarée absente, à bon escient | remplie à 100 % (imposée) ; ≈ 10 % des « non cité » de température, durée et pureté suspects (valeur présente dans la citation de l'étape) ; réglages hors grille souvent ni extraits ni déclarés (agitation 84 %, remplissage 95 %, refroidissement 53 %) | **positif** sur le remplissage ; **négatif** sur la justesse partielle et l'étendue | `audits/audit_grilles.md` |
| Grille de caractérisation | les réglages de chaque mesure sont extraits | aucune grille imposée ; réglages présents dans la base très en dessous de ce que disent les articles (plage XRD 46 % contre 97 %, électrolyte 33 % contre 99 %, masse active 1 % contre 44 %) ; pas de lien valeur → mesure | **négatif** | `audits/audit_grilles.md` |

## En cours

| Test | Hypothèse | Plan |
|---|---|---|
| — | — | aucun test en cours |
| Architecture v2, extraction en une passe (50 publications déjà extraites en v1) | une extraction au format 3 avec vocabulaire contrôlé est au moins aussi complète et juste que la v1 en 4 passes | couverture des tableaux 95,6 % (v1 71,6 %), résultats ×1,7, 2 088 réglages de mesure cités, 97 % des résultats liés à leur mesure ; 0 erreur de citation ; 233 k jetons par publication (v1 640 k) | **positif** | `audits/v2/rapport.md` |
| Critique de fidélité des extractions v2 (10 publications) | la v2 n'a pas plus d'erreurs que la v1 avant correction | périmètre commun : 42 constats contre 84, graves 6 contre 10 (les 2 « faux » v2 sont des annotations) ; 96 constats propres au format 3, dont 12 attributions (témoins, liens résultat → mesure) | positif sur la justesse ; négatif localisé (témoins sans place) | `audits/v2/critiques_v1_v2.md` |
| Vocabulaire contrôlé avec ajouts définis (153 ajouts, fusion en version 2) | les agents choisissent un nom de la liste et n'ajoutent que l'utile | 100 % des noms dans le vocabulaire ; ≈ 3 ajouts par publication ; 1 doublon de sens, 1 nom refusé ; noms génériques bloqués après la règle de l'utilisateur ; ≈ 145 avertissements « technique inhabituelle » résolus par la fusion | positif | `audits/v2/rapport.md` |
| Grille de synthèse par action (v2) | plus de cases qu'en v1 | 2,6 cases par étape contre 3,3 : les actions courantes (dissoudre, mélanger, ajouter, filtrer) ont trop peu de cases ; 1 738 « non cité » contre 2 847 | **négatif** : cases à enrichir avant de généraliser | `audits/v2/rapport.md` |
| Concordance des valeurs v1 / v2 | les deux extractions disent la même chose | 84,5 % des valeurs v1 retrouvées (89,4 % sans exiger la même écriture d'unité) ; écarts surtout dus aux lectures de figure ; les 66 « conflits » de la comparaison par nom sont des erreurs d'appariement des voies (vérifié) | positif | `audits/v2/comparaison_v1_v2.md` |
