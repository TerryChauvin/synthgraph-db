# Journal d'extraction PMC7931434 (Mo/TiO2, micelles inverses)

- Découpage : une seule synthèse « typical synthesis » pour six échantillons (0 à 10 % Mo nominal). Voie de base choisie : `Mo_1` (plus faible teneur dopée) ; `Mo_2.5`, `Mo_5`, `Mo_7.5`, `Mo_10` en branches, variation = quantité du précurseur de Mo (« wt % Mo (nominal) », citation « Mo wt % nominal contents of 0.0, 1.0, 2.5, 5.0, 7.5, and 10 »). Aucune masse de précurseur n'est écrite : la grille déclare `amount` non cité pour tout, sauf l'heptamolybdate en `amount_text`.
- Pourquoi pas le TiO2 comme base : le protocole écrit contient la dissolution du sel de Mo ; la voie de base doit être un protocole décrit en entier. Le TiO2 non dopé est donc une branche « sans sel de Mo » (variation `absent`) avec ses propres étapes, sans l'étape de dissolution du sel.
- Phase aqueuse du TiO2 non dopé : l'article ne dit pas si de l'eau seule est ajoutée ; l'étape « add water/stir 45 min » est reprise avec la citation de la phrase du sel et la réserve écrite dans la description et en doute. `aqueous_phase_composition` est déclaré non cité.
- « at the same temperature » (dissolution du sel) : renvoie à 50 °C dans la même phrase ; gardé en `value_text` sans nombre (règle : rien de déduit).
- Rangées de tableaux : chaque échantillon prend ses rangées entières des tableaux 1 et 2 par son nom ; vérifié que les phases du tableau 1 correspondent à la figure 1b.
- Désaccord tableau/figure : Eg de Mo_2.5 (2.76 tableau, 2.59 Fig. 7b) et VB de Mo_7.5 (2.5 tableau, 2.55 Fig. 7b). Valeurs du tableau gardées pour Eg et VB ; CB de la figure 7b (valeurs imprimées) gardées telles quelles, avec doute.
- Énergies de liaison XPS du Mo3d5/2 : le texte attribue 231,3 à Mo6+ et 232,5 à Mo5+, l'inverse de la Fig. 6b et de l'ordre usuel. Valeurs de groupe, non extraites en résultats ; doute.
- Valeurs lues sur figure : volume de maille de l'anatase (Fig. 2b, 6 points, recoupé avec Fig. 1c) en 5 chiffres significatifs (la variation tient dans les centièmes d'Å3), et CB (Fig. 7b, imprimées). Ti2p3/2 (Fig. 6c) et distributions de taille (Fig. 2a) non extraites.
- Résultat de groupe des lacunes d'oxygène (15 ± 2 %) : annotation `tendance_observee` ; seule la valeur de Mo_5 (9 ± 1 %) est un résultat de voie.
- Raman (Fig. S1) : seulement TiO2, Mo_1, Mo_5, Mo_10 mesurés ; bandes Mo=O à 944 (Mo_5) et 956 cm-1 (Mo_10) en résultats ; le texte principal (« ≥5 wt % ») incluant Mo_7.5 est signalé en doute.
- `method_sources` : ref65 (revue sur les micelles inverses) en `autre` ; ref66 (MAUD) écartée comme logiciel d'analyse ; ref13 (introduction seulement) hors méthode.
- Annexes : Fig. S1 (légende et texte), S2, S3 (images, légendes seules) présentes dans le fichier texte ; images de l'annexe non disponibles dans corpus/fig, signalé en `limite_reproductibilite`. Aucune annexe absente.
- Sécurité : aucune précaution écrite dans l'article, donc seulement `securite_analyse`.
