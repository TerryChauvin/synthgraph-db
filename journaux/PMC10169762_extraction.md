# Journal d'extraction PMC10169762 (Co-DAT-MOF)

- Découpage : une seule voie de base `Co-DAT-MOF` (aucune branche). L'article ne varie aucun paramètre de la synthèse du MOF ; les seules séries (solvant, température, masse de catalyseur, témoins) portent sur les réactions catalytiques test.
- Essais d'optimisation (Tableaux 2 et 4) rangés en `outcomes` de la voie du catalyseur, pas en branches ni en voies : règle « tests du matériau fini ». Une rangée = un outcome, le nom de propriété reprend seulement catalyseur (mg), solvant, température de la rangée.
- Les deux « General procedure » catalytiques ne sont pas extraites en voies : ce sont des synthèses organiques, pas des matériaux. Les conditions optimales ressortent dans l'annotation `conclusion_auteurs`.
- Tableaux 3 et 5 : la colonne « Product » est vide (images). Durée et rendement extraits par numéro d'entrée ; points de fusion laissés de côté (caractérisation de produits organiques). Rattachement à un aldéhyde ou une amine impossible, signalé en doute et en `limite_reproductibilite`.
- Tableau 2 entrées 11-12 et Tableau 4 entrées 10-11 : les notes [d,e] listent le sel de cobalt et le ligand sans « respectively » ; je n'ai pas attribué d'ordre, la propriété porte `footnote_d` / `footnote_e`.
- Sonication : « 20 min » (phrase du bain) contre « ultrasonic time was 15 min » et puissance 100 W contre bain 380/350 W. Retenu 20 min et 100 W, 15 min non extrait, doute écrit.
- Rendements des Tableaux 2 et 4 sans unité dans le texte : laissés sans unité plutôt que d'ajouter « % » (seuls les Tableaux 3 et 5 écrivent « (%) »).
- Entrée 4 absente du Tableau 4 : non inventée, doute écrit.
- ICP-OES « 0.065 mol.g−1 » : valeur et unité copiées telles quelles malgré l'invraisemblance (≈ 3.8 g Co/g), signalées en doute et en limite de reproductibilité.
- « main peak at 11.78 » extrait sans unité (2θ non écrit).
- Fig. 13 (recyclage) : seule figure lue (rendements des 4 runs ≈ 91, 89, 89, 88, barres 3D, ±1) car aucune valeur dans le texte ; Fig. 9 et 11 (schémas de réaction) ouvertes sans donnée de synthèse du MOF ; Fig. 2-8 et 14 non lues, leurs valeurs utiles sont dans le texte et le Tableau 1.
- Inventaire : catalyseur récupéré, ligand libre et Co(NO3)2·6H2O sans voie (réactifs ou catalyseur usagé du même lot).
- `method_sources` vide : les seuls renvois ([[CR46]] pour le diagramme standard, [[CR47-50]] pour les points de fusion et [[CR48]], [[CR52]] dans le Tableau 6) ne sont pas des protocoles nécessaires ; la synthèse du MOF n'est référencée à aucune publication.
- Sécurité : aucune précaution dans l'article, donc seulement `securite_analyse`.
- Annexe : le seul Supporting Information (MOESM1) ne contient que des spectres RMN de produits ; aucune annexe citée par l'article n'est absente.
