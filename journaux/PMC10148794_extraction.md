# Journal d'extraction PMC10148794

- Article de physique (spectroscopie CTA de CsPbBr3) dont la synthèse tient en un paragraphe de Méthodes : gardé, non rejeté, car NC5 est décrit avec toutes ses quantités et NC6/NC8/NC12 avec presque toutes.
- NC5 (injection à chaud, Cs-oléate + PbBr2/ZnBr2/OA/OAm/ODE) et NC6 (Cs-octanoate + PbBr2/TOPO/OPA dans le toluène) sont deux méthodes indépendantes : deux voies de base. Le stock de Cs-oléate est traité comme des étapes (1 et 2) de NC5, non comme une voie `intermediate`, car il n'est ni isolé ni réutilisé ailleurs.
- NC8 et NC12 sont des branches de NC6 : « The synthesis of NC6, NC8, and NC12 was performed according to a previously reported method » et « growth period (30 s, 2 min and 30 min for NC6, NC8 and NC12, respectively) » ; ordre de la phrase écrit avant attribution (NC6=30 s, NC8=2 min, NC12=30 min). Variation sur l'étape 6 (`duration`).
- Le rôle de ZnBr2 n'est pas donné par les auteurs : rôle « additive », hypothèse sur le bromure en excès seulement dans `mecanisme_analyse`.
- Stocks de NC6 (Cs-octanoate 0,1 M, PbBr2/TOPO/OPA, DDAB 0,05 M) : réactifs bruts avec `amount` non cité quand l'article ne donne que la concentration, plus une ligne par aliquote (55 μL, 0,5 mL, 155 μL) pour que les quantités réellement utilisées apparaissent.
- « 0.2 M of octylphosphonic acid » : saisi comme amount 0,2 unité M, tel que cité (concentration, pas masse).
- « Centrifugations multiples selon la méthode publiée » (NC6) : étape de centrifugation sans valeur, `speed`, `duration`, `wash_solvent` déclarés non cités ; source de méthode CR53 en `protocole_complet` pour cette purification, `protocole_adapte` pour la synthèse ; CR52 `protocole_adapte` pour NC5 (« slight modifications »).
- Température de réaction de NC6 : « room temperature ambient conditions » est écrit dans la phrase générale ; reprise en `value_text` à l'étape 6 (croissance), non attribuée aux autres étapes.
- Température après injection pour NC5 : implicite (170 °C), donc déclarée non citée à l'étape 5.
- PTF (film polycristallin) : voie de base séparée (CsBr/PbBr2 dans le DMSO, spin-coating 4 000 r.p.m., recuit 100 °C 10 min) ; épaisseur ~40 nm en résultat (le AFM de la Fig. S5 donne 40 ± 7 nm, mais la citation retenue est celle des Méthodes).
- « NC solids » : voie `device` à part (spin-coating 500–800 r.p.m.) avec un intermédiaire générique, car l'article ne dit pas quelles tailles sont déposées ; doute consigné.
- Énergie de structure fine de NC5 (~1,7 meV) : le texte principal ne nomme pas l'échantillon de la Fig. 2c ; seule la réponse aux relecteurs (fichier Peer Review) écrit « for sample NC5 », citée.
- Figures 2 et 3 ouvertes : aucune valeur lue sur figure (les durées de vie de spin ne sont pas des résultats de synthèse ; maxima de τs écrits dans le texte). Fig. 1 non ouverte (TEM et spectres d'absorption, valeurs dans le texte).
- Source Data (figures 2 et 3) absent du dépôt : consigné en `limite_reproductibilite`.
- XRD : phrase du SI « all samples (no data for NC5 ...) » appliquée à NC6, NC8, NC12 et PTF, pas à NC5.
