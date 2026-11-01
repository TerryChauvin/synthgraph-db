# Journal d'extraction PMC5890287

- Découpage : sept voies. Base GO (Hummers modifiée, `intermediate`), RGO (témoin), Fe2O3-RGO (`intermediate`, réutilisé), Chlorophyll (`intermediate`), Au-Fe2O3-RGO (voie finale). Deux branches : Fe2O3 (hématite pure) et Au-Fe2O3-RGO-noChl (sans chlorophylle).
- RGO : l'article n'a aucun protocole propre. Voie minimale créée à partir de « reduction of GO to RGO under hydrothermal method at 180 °C for 12 h » (phrase FTIR) pour porter ses résultats (ID/IG 1,2015, FTIR) ; quantités non citées et doute posé.
- Fe2O3 (« similar hydrothermal preparation process in the absence of GO solutions ») : branche de Fe2O3-RGO, avec ses propres étapes (dissolution, chauffage) car l'étape 1 du parent dissout les sels dans la suspension de GO ; 180 °C / 12 h pris de la phrase des Résultats. Lavage et séchage déclarés non cités. Réactifs hérités du parent (doute).
- Au-Fe2O3-RGO-noChl : étapes propres (sans l'ajout de chlorophylle) ; centrifugation et séchage repris par « similar » avec doute. Variation de durée : « 0 to 60 min » en `value_text` (légende Fig. 9a), la durée de collecte n'est pas écrite.
- Durée d'irradiation : Méthodes 20 min (retenue, section la plus détaillée) contre 30 min dans le résumé, la Fig. 9b et la conclusion ; 30 min gardé comme résultat « reduction_time ».
- HAuCl4 « 50 mM » dans 10 ml pour 100 mg de support : valeur recopiée, plausibilité mise en doute (0,5 mmol d'Au).
- Fournisseur : la phrase « Graphite flakes … were supplied by Sigma Aldrich » ne nomme ni H2SO4, H2O2, HCl, acétate de sodium ni éthanol : fournisseur non cité pour ceux-là ; pureté « analytical grade » reprise de la phrase générale « All chemicals were of analytical grade… ».
- Extrait de chlorophylle : voie intermédiaire séparée (2 g de feuilles dans 5 mL d'éthanol, concentration tirée de la section Résultats sur le film I-V, rapprochée de « 5 ml of chlorophyll » des Méthodes avec doute). Rôle `intermediate` dans la voie Au.
- Échantillons sans voie : Au@RGO et Au (XRD Fig. 3a, 8 nm sans préparation), film de chlorophylle sur ITO (mesure I-V), témoin MB sans catalyseur.
- Résultats MB : durées de dégradation complète (240, 180, 120 min) prises de la phrase unique « respectively » dans l'ordre α-Fe2O3, α-Fe2O3@RGO, Au@α-Fe2O3@RGO. Contradiction : Fig. 10b montre des spectres jusqu'à 210 min et la courbe 10d s'arrête vers 150 min pour α-Fe2O3@RGO ; texte retenu.
- Figures : seule Fig. 11a lue en valeur (≈ 99 % par cycle, ± 2 %). Fig. 10d non retranscrite (durées dans le texte), spectres UV non retranscrits.
- Raman : l'article attribue les bandes à la magnétite alors que l'hématite est annoncée ; seules les valeurs ID/IG ont été extraites (rangée « respectively » : GO 0,8911, RGO 1,2015, ternaire 1,2157).
- `method_sources` vide : le fichier refs ne contient aucun renvoi `[[id]]` dans la partie Méthodes (Hummers « modified » sans citation).
- Aucune annexe : pas de renvoi à un Supporting Information dans le texte.
