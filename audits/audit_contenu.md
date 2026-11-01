# Audit de contenu de la base (28/10/2026)

Audit de ce que contient `synthese.db` une fois les 500 publications closes : types de synthèse, propriétés communes, conditions, trous de couverture, qualité des données, limites de reproductibilité, mécanismes, comparaison à des références externes. Cadrage fixé avec l'utilisateur en quatre salves de questions (description + trous + qualité ; les 500 publications ; tableau de bord interactif par onglets ; croisements simples ; toutes les conditions potentiellement importantes).

**Régénération** : `python3 -I analyses/audit_contenu.py` → `docs/audit_contenu/data/*.json` (39 jeux complets) et `docs/audit_contenu/dash/*.json` (18 jeux regroupés pour la page). La page est `docs/audit_contenu/index.html` (elle s'exécute dans le tableau de bord Claude, qui fournit `dash` et `d3` ; ce n'est pas un HTML autonome). Les sorties des agents sont dans `docs/audit_contenu/sources/`.

## Méthode

- **Périmètre** : 500 publications closes, 5 338 voies (1 382 de base, 3 956 branches), dont **747 voies de base d'un matériau** (les autres voies de base sont des intermédiaires, post-traitements ou dispositifs). Les conditions d'une voie sont calculées à partir de ses étapes ; une branche hérite de ses parents.
- **Types de synthèse** : deux classements indépendants des 747 voies de base, l'un par mots-clés du champ « méthode » (29 classes, règles par priorité), l'autre par signature des étapes (actions, équipement, température maximale ; 14 classes). Concordance : **68,8 %**. Les discordances les plus fréquentes : « hydrothermal » annoncé sans autoclave dans les étapes (24 voies) et méthodes non classées (43 voies, 5,8 % : noms de matériau sans méthode, mélanges, procédés singuliers).
- **Propriétés** : les 16 577 noms bruts de propriétés (10 941 vus une seule fois) sont ramenés à **73 propriétés canoniques** par une table d'expressions régulières (`PROP_RULES`), sans modifier les données. **25,8 % des valeurs restent dans « autre »** : noms trop spécifiques (`XRD_intensity_ratio_002_100`, `supernatant_Si_concentration`, `Rct`…).
- **Mécanismes** : deux agents Opus ont confronté, pour 512 voies, le mécanisme décrit par les auteurs et l'hypothèse du critique scientifique (type, accord, incompatibilité avec les conditions extraites, travaux fondateurs de `references/fondateurs.md`).
- **Références externes** : un agent Opus a relevé sur le web des plages de référence pour 131 couples matériau-propriété (28 matériaux fréquents) et les a comparées à la base. CoRE MOF, IZA et Materials Project ne sont pas joignables depuis le cloud (`zenodo.org`, `europe.iza-structure.org`, `api.materialsproject.org` : hôtes à autoriser dans l'environnement ; Materials Project demande aussi une clé API).

## Ce que contient la base

- Familles de matériau (voies de base) : composites 170, oxydes 89, pérovskites 73, MOF 67, nanoparticules métalliques 62, chalcogénures 41, « autre » 41, quantum dots 39, zéolithes 35, carbones 30, céramiques 21, batteries 20, silices mésoporeuses 20, matériaux 2D 18, nitrures 17, carbures 3, phosphures 1.
- Méthodes : hydrothermal 18,6 %, précipitation 8,4 %, sol-gel 7,5 %, solvothermal 5,9 %, voies vertes 4,4 %, dépôt de films 4,4 %, réduction chimique 4,3 %, injection à chaud 4,0 %… Méthode principale par famille : hydrothermal presque partout, injection à chaud pour les pérovskites, solvothermal pour les MOF, voies vertes pour les nanoparticules métalliques, CVD pour les matériaux 2D.
- Propriétés les plus fournies (valeurs) : composition élémentaire 2 656, performance catalytique 2 187, capacité d'adsorption 1 771, taille de particule 1 470, ajustements cinétiques 1 404, phase 1 086, XPS 1 027, capacité spécifique 1 022, pic de PL 1 008, rendement 916, pic d'absorption 893, morphologie 836, cristallite 796, BET 755, band gap 415, rendement quantique 335.
- Conditions (747 voies de base) : température maximale connue pour 80 % (P10 60 °C, médiane 170 °C, P90 750 °C) ; durée totale pour 87 % (médiane 12 h, P90 56 h) ; 6 étapes en médiane ; pH donné pour 10 % des voies, agitation pour 6 %, rampe pour 10 %, volume pour 19 %. Atmosphère non citée pour 500 voies sur 747 ; eau solvant principal de 307 voies, aucun solvant déclaré pour 198.
- Années : 2016–2023 pour les trois quarts ; revues : RSC Advances 77, Scientific Reports 63, Nanomaterials 49, Materials 48.

## Trous

- **132 cases famille × méthode sur 175 ont moins de 5 voies** : au-delà de l'hydrothermal et du sol-gel, presque chaque méthode n'est représentée que par une poignée de voies par famille (électrochimie : 4 voies en tout ; auto-assemblage : 1 ; micelles : 3).
- **43 couples famille-propriété attendus sont couverts à moins de 30 %** des voies : band gap et rendement quantique des pérovskites (19 % et 29 %), FWHM des quantum dots (3 %), BET des oxydes (29 %) et des carbones (10 %), rétention de capacité et efficacité coulombique des batteries (0 % et 20 %), densité et dureté des céramiques (5 %), épaisseur et Raman des matériaux 2D (28 %), phase des MOF (24 %) et des nanoparticules métalliques (26 %).
- **Couverture chimique** : Zn (97 voies), S, Si, Ag, Fe, Na, Pb, Ti dominent ; Nd, Nb, Ir, Re, Ru, Sm, Eu n'apparaissent qu'une fois ; Pd et Sb deux fois.
- **Plages de conditions** : par famille, les intervalles de température, durée et pH vides sont visibles dans l'onglet Trous (ex. presque rien au-dessus de 300 °C pour les MOF et les quantum dots, rien sous 100 °C pour les céramiques).

## Qualité des données

- **Unités** : 64 propriétés canoniques fournies (≥ 10 valeurs) ont plus d'une unité. Les variantes typographiques (m2 g−1, m2·g−1, m2/g) sont fusionnées par l'audit ; restent des unités hétérogènes réelles (composition en %, at.%, wt.% ; capacité en mAh/g, mAh/cm2, F/g) et des noms mal fusionnés par les règles.
- **7 valeurs hors plage physique**, toutes recopiées de l'article : rendements quantiques de 112 à 241 % pour des points de carbone (PMC10583617, « %QY » relatif à un étalon) et une surface BET de 0 m2/g après test de stabilité (PMC12312155, tableau de l'article).
- **Complétude** : moyenne 0,74 ; batteries 0,87, pérovskites 0,85, oxydes 0,82 ; « autre » 0,57, nitrures 0,64, matériaux 2D 0,65. Champs les plus souvent non cités : pureté des réactifs (25 % des voies), rendement (25 %), durée d'étape (24 %), quantité de réactif (23 %), température d'étape (22,5 %), fournisseur (22 %), vitesse d'agitation (19 %).
- **Doublons entre publications** : 45 matériaux apparaissent dans au moins deux articles. Les écarts de « taille de particule » (ZnO 0,022–209 nm ; Ag 0,6–88 nm ; CsPbBr3 2,6–800 nm) montrent que ce nom regroupe des grandeurs différentes (cristallite, diamètre TEM, hydrodynamique, agrégat) ou des unités mal lues : une table de correspondance plus fine est à prévoir avant toute exploitation statistique de la taille.
- **Verdicts** : 2 640 voies « reproductibles avec réserves », 269 « non reproductibles », 75 « reproductibles » ; critique scientifique « douteuse » ou « incohérente » pour 50 à 80 % des voies de base selon la famille. Constats de fidélité : 4 345, dont 90 « faux » (corrigés).

## Limites de reproductibilité et mécanismes

- **83 % des voies de base** portent au moins une limite (41 % de toutes les voies, branches comprises). Motifs (règles sur le texte des 4 558 annotations) : incohérence interne de l'article 21 %, preuve non discriminante 10 %, interprétation contestée 10 %, bilan de matière ou stœchiométrie 9,5 %, annexe absente du dépôt 7 %, conditions manquantes 6 %, quantités manquantes 5 %, unité ou lecture ambiguë 5 %, calcul du critique 4 %, valeur hors plage 4 % ; 12 % non classés.
- **Mécanismes (512 voies)** : 83 accords, 346 nuances (dont 106 voies où les auteurs ne décrivent aucun mécanisme de formation), 83 désaccords. Les auteurs invoquent surtout la nucléation-croissance (71), la réduction chimique (64), la décomposition thermique (47) et le gabarit (37) ; le critique reclasse souvent vers l'hydrolyse-condensation (44) et la polymérisation-réticulation (40, points de carbone vus comme fluorophores moléculaires). Désaccords concentrés sur les composites (14), oxydes (14), nanoparticules métalliques (10). **25 mécanismes sont contredits par les conditions extraites** (réduction sans réducteur, AgCl précipité avant toute réduction dans les voies vertes, gabarit détruit avant cristallisation, « hydrothermal » à 80 °C) ; deux cas (PMC13516552, PMC6297875) pointent plutôt une température mal extraite ou un mot impropre des auteurs, à revérifier.
- **Travaux fondateurs** : LaMer 1950 (13 voies) et Essner 2018 (22) sont les plus invoqués ; les plus souvent absents alors qu'ils fondent la méthode : Iravani 2011 (synthèses vertes, 29), Cundy & Cox 2003 (zéolithes, 16), Hench & West 1990 (sol-gel, 15), Sadat-Shojai 2013 (hydroxyapatite, 12), Pechini 1967 (10).

## Comparaison à des références externes (131 couples)

31 conformes, 12 plus bas, 7 plus haut, 13 plus larges, 68 sans plage publiée (tailles, zêta, rendements : grandeurs propres à chaque synthèse). Écarts nets : band gap du SnS (médiane 2,81 eV contre 1,07–1,40 eV massif), PL du CdS (580 nm contre 490–505 nm : émissions de pièges), silices « mésoporeuses » (BET 274 m2/g contre 400–1 137 ; volume mésoporeux 0,62 contre 0,95–1,53 cm3/g), ZIF-8 (BET 1 194 contre 1 250–1 600 ; volume microporeux 0,15 contre 0,52–0,62 cm3/g), ZSM-5 (BET 309 contre 350–500), rendement quantique de MAPbBr3 (41 % contre 48–93 %), capacité de LiFePO4 (149 contre 157–170 mAh/g). Conformes : band gaps de TiO2, ZnO, CuO, CsPbBr3, MAPbBr3 ; mailles de ZnO, LiFePO4, NMC622 ; PL de CsPbBr3, FAPbBr3 ; plasmon de l'argent. Sources : URL réellement vues par l'agent, listées dans l'onglet Références ; aucun DOI de mémoire.

## Ce qu'il faudrait faire ensuite

1. **Nommage des propriétés** : imposer dans `RUNBOOK.md` une liste fermée de noms canoniques pour les 30 propriétés les plus fréquentes (avec unité attendue), et distinguer explicitement cristallite / diamètre TEM / taille hydrodynamique / agrégat. C'est le premier obstacle à toute exploitation par apprentissage.
2. **Conditions** : l'atmosphère (non citée pour 2 voies sur 3), le pH, l'agitation et l'échelle sont rarement extraits alors qu'ils comptent pour la reproduction ; vérifier sur un échantillon si l'article les donne vraiment ou si l'extraction les saute.
3. **Trous de couverture** : si la base doit s'étendre, cibler les familles sous-représentées (carbures, phosphures, nitrures, matériaux 2D) et les méthodes rares (électrochimie, micelles, auto-assemblage, mécanochimie), et exiger les propriétés attendues manquantes (band gap et PLQY des pérovskites, BET des carbones, rétention des batteries).
4. **Revérifier** les 25 mécanismes contredits par les conditions et les 7 valeurs hors plage ; corriger les deux températures suspectes si l'article le confirme.
5. **Bases externes** : autoriser `zenodo.org`, `europe.iza-structure.org` et `api.materialsproject.org` dans l'environnement cloud (et fournir une clé Materials Project) pour une comparaison structurée MOF / zéolithes / band gaps.

## Fichiers

- `analyses/audit_contenu.py` : script d'audit (taxonomies, fusion des synonymes, conditions par voie, trous, qualité, limites, agrégation des sorties d'agents).
- `docs/audit_contenu/data/` : 39 jeux de données complets ; `docs/audit_contenu/dash/` : 18 jeux pour la page ; `docs/audit_contenu/index.html` : page du tableau de bord ; `docs/audit_contenu/sources/` : prompts et sorties des agents (mécanismes A et B, références web, journaux).
- Coût des agents : mécanismes 346 k + 357 k jetons, références 278 k ; orchestrateur non compté.

---
*Mise à jour du 28/10/2026 (point 2 du plan d'amélioration)* : le vocabulaire canonique est désormais dans la base (`canon.py`, colonnes `name_canon` et `property_canon`, table `vocabulaire`, export `docs/vocabulaire/`). Avec les règles ajoutées, la part de propriétés non classées passe de 25,8 % à 9,1 % (95 propriétés canoniques) ; 0,9 % pour les paramètres (37 canoniques). Les chiffres de ce rapport datent d'avant cette mise à jour ; les données de `docs/audit_contenu/data/` sont régénérées.
