# Journal d'extraction PMC6447565 (CuFe2O4@HNTs)

- Une seule voie de base `CuFe2O4@HNTs` : l'article ne décrit qu'une préparation du catalyseur, aucune variation de synthèse (ni température, ni charge, ni ratio) ; donc zéro branche.
- Les 11 pyrazolopyridines 5a-k (Table 1) et le recyclage sont des tests du matériau fini : rangés en `outcomes` du catalyseur (une rangée du tableau par produit, recopiée entière), pas en voies ni en branches, conformément au RUNBOOK. Le protocole du test (réactifs, éthanol, température ambiante, 20 min) est décrit dans une annotation `limite_reproductibilite`, pas en étapes.
- Contradiction interne : 50 mg de catalyseur (Résultats) contre 5 mg (procédure générale). Aucune des deux n'est extraite ; doute ouvert.
- Fournisseur : la phrase « Chemicals were purchased from Sigma-Aldrich and Merck companies and applied without any further purifications » couvre tous les réactifs, donc fournisseur recopié « Sigma-Aldrich and Merck » pour chacun, pureté en `not_stated` (« without further purifications » ne donne aucune pureté).
- HNTs rangé en rôle `substrate` (support, ni précurseur ni solvant) : aucun rôle « support » dans le vocabulaire.
- La solution de NaOH (« 5 mL solution of NaOH (0.50 g, 12 mmol) ») : solvant non écrit, donc pas de réactif eau pour cette étape (volume 5 mL mis en paramètre de l'étape 4, solvant et concentration en `not_stated`).
- Étape 2/3 : la phrase « HNTs was added ... stirred for 1 h at room temperature » est scindée en une addition et une agitation de 1 h, avec la même citation ; « room temperature » en `value_text`.
- Étape 9 : « kept in a furnace at 500 °C for 5 h » : atmosphère et vitesse de chauffe non écrites (le four n'est pas dit « air »), déclarées `not_stated`, bien que l'ATG soit faite sous air.
- Valeurs sans unité dans le texte : pore volume 0,126 et pore size 9,87, extraits sans unité, doute ouvert (la Fig. 5b est en nm, pic vers 6 nm).
- Figures lues : Fig. 3a (tableau EDX imprimé, 5 valeurs exactes), Fig. 2b (masse restante à 800 °C, environ 94 %, précision ±1 %). Fig. 3b, 4a, 5 ouvertes : pas de nouvelle valeur extraite ; écarts texte/figure (VSM 30 contre 23–24 emu/g ; ATG 20 % contre 13 % pour HNTs) en doutes, valeurs du texte conservées.
- Échantillons sans voie : HNTs de départ, CuFe2O4 seul et HNTs seuls comme catalyseurs de la réaction modèle (Table S1 absente), catalyseur recyclé (Fig. S5-S7 absentes).
- Annexe absente : le fichier texte n'a aucune section Supporting Information ; Table S1, Fig. S5, S6, S7 signalées en `limite_reproductibilite`.
- `method_sources` vide : les renvois [[CR33]] (aimantation de CuFe2O4 seul), [[CR35]] (valeurs de HNTs) et [[CR36]] (mécanisme) sont des comparaisons ou de l'interprétation, non des protocoles à reprendre.
- Mécanisme : `mecanisme_auteurs` porte uniquement sur le mécanisme de Hantzsch de la réaction catalysée (précisé dans le texte de l'annotation) ; la formation du catalyseur est en `mecanisme_analyse`, avec stœchiométrie vérifiée (Fe 1,17 mmol et Cu 0,58 mmol cohérents avec les masses, NaOH en excès).
