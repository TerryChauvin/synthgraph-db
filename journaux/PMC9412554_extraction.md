# Journal d'extraction PMC9412554 (PI/TiO2@MoS2)

- Découpage : trois voies de base sans aucune branche. L'article ne balaie aucun paramètre ; la plage « 0.04~0.05 g » de titane est une fourchette, pas une série, donc pas de branche.
- PI (électrofilage, section 2.2) et PI/TiO2 (2.3) sont des voies `intermediate` : chacune est réutilisée comme réactif de l'étape suivante (réactif de rôle `intermediate`). PI/TiO2@MoS2 (2.4) est la voie `material` et la seule `is_baseline`.
- Les tests de photodégradation du bleu de méthylène (section 3.2) sont rangés en `outcomes` et en `characterizations` de chaque voie, jamais en voie `device` ni en branche.
- Figure 8 (droite) : seule source comparant PI, PI/TiO2 et PI/TiO2@MoS2 ; C/C0 à 180 min lu 0,91 / 0,30 / 0,05 (`from_figure`, citation = légende de la figure 8, précision ± 0,02 notée en doute). Le texte donne « about 95% », cohérent avec 0,05. Je n'ai pas lu les points intermédiaires (non lisibles de façon fiable).
- Figures 1, 4, 5, 7 ouvertes : le schéma de la figure 1 n'apporte aucune condition (pas de température d'imidation) ; la figure 4 montre un échantillon PI/MoS2 sans préparation décrite, donc `route: null` dans l'inventaire ; les figures 5 et 7 n'ont pas de valeurs ajoutant au texte.
- Titane : « Titania powder » en 2.1 contre « titanium powders » en 2.3 ; lecture littérale (poudre de titane), pureté et fournisseur déclarés non cités, avec doute. Le mécanisme (Ti + HCl → TiCl3) confirme qu'il s'agit de titane métallique.
- Teneur en solide 25 % (synthèse du PAA) contre solution électrofilée à 15 % : deux valeurs gardées chacune dans son étape, doute ouvert ; la dilution n'est pas décrite.
- Durée de 8 h de la polycondensation : l'article dit « we stopped stirring after 8 h », donc durée d'agitation retenue comme durée de réaction, noté en doute.
- Imidation thermique : étape sans aucun paramètre dans l'article ; `heat` avec température, durée, atmosphère, rampe déclarées non citées (pas de valeurs prises sur les polyimides usuels).
- Quantités « A small amount » de molybdate et de thioacétamide : mises en `amount_text` (non chiffrées), non déclarées `not_stated` car l'article s'exprime (sans nombre) ; limite signalée en `limite_reproductibilite`.
- Fournisseur et pureté : « chemical reagent grade » pour PMDA et ODA (phrase 2.1, avec sublimation avant usage) ; Sinopharm Shanghai pour HCl, DMF, molybdate, thioacétamide (pureté non citée). Eau et fibres intermédiaires : non cités ou exemptés par la grille.
- `method_sources` vide : le seul renvoi de méthode possible (B34, « PAA was analyzed in our previous report ») concerne une analyse, pas la préparation ; B38 (Fujihara) concerne le mécanisme.
- Contradiction nanosphères / nanofeuillets (MoS2) et bâtonnets / « nanobelts » (TiO2) : texte de la section 3.1 (MEB, nanosphères) retenu pour le résultat de morphologie, doute noté.
- Aucune annexe mentionnée dans l'article ni dans le fichier texte : pas d'annotation « Annexe absente ».
