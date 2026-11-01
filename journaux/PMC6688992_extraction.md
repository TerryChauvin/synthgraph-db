# Journal d'extraction PMC6688992

- Découpage : sept voies. CdS et CdS_WOx sont deux voies de base (CdS est préparé indépendamment, puis réutilisé comme réactif de CdS_WOx) ; Ta3N5, WOx sont deux autres voies de base car le texte les résume (« In brief ») sans dire qu'elles suivent le protocole de CdS/WOx. Deux voies `device` : Electrode_FTO (drop-casting) et PEC_cell (montage à trois électrodes).
- Voie de base principale : CdS_WOx (`is_baseline: true`), matériau de l'article, bien que CdS soit décrit en premier dans les Méthodes.
- CdS laissé en voie `material` et non `intermediate` : il est caractérisé (XRD, XPS, UPS, Tauc) et testé comme témoin photoélectrochimique ; CdS_WOx le cite comme réactif de rôle `intermediate`.
- Ta3N5_WOx est une branche de CdS_WOx : « All other reaction conditions, including the heating parameters, the composition and volume of the solvent, and the centrifugation steps ... remained the same as in the CdS/WOx case ». Variations : CdS remplacé par Ta3N5 (3.8 mM) et WCl6 22.8 mM au lieu de 20 mM. Le séchage n'est pas nommé : héritage accepté, signalé dans les doutes.
- « 20 mM » de CdS : reporté tel quel en `amount` (unité mM) ; pas de conversion, volume du mélange non cité (plusieurs cases `not_stated`).
- Durées écrites en lettres (« ten hours ») : `value_text`, car le contrôle exige le nombre en chiffres dans la citation. « 24 hours » est en `value_num`.
- Rapport « W/O atomic ratio ... 2.75 » (Résultats, XPS) : recopié sous le nom des auteurs ; c'est en réalité O/W (49/18 = 2.72), noté en doute et dans une annotation.
- Valeurs lues sur figure : seulement Fig. 8a (≈10 µA) et Fig. 8b (≈120 µA), premier pic de photocourant ; la figure 9 ne donne rien de plus que le texte (constantes déjà citées) ; les figures 1 à 7 sont qualitatives (pas d'échelle exploitable pour une taille).
- Texte préféré à la figure pour la taille de CdS : « less than 200 nm » en `value_text` ; la figure 1a n'est pas lue pour affiner.
- Annexe : la section Supporting Information est présente (Table S1 EDX, Fig. S1 à S4) ; les rapports Cd/S EDX sont pris dans le texte, pas dans la Table S1 (cellules sur des lignes séparées, pas de rangée citable). Aucune annexe absente.
- Références Ta3N5, WOx, Ta3N5/WOx : trois entrées `method_sources` sur CR59 (`protocole_adapte`) ; une quatrième pour le protocole UPS (« protocol described elsewhere », rôle `autre`, route nulle). CR147 pour CdS.
- NaCl et KCl de la voie Ta3N5 : rôle `flux`, interprétation signalée en doute ; l'article ne dit pas leur rôle.
- Les résultats de photocourant des références (Ta3N5, Ta3N5/WOx, WOx, Fig. S4) sont qualitatifs et pris dans le texte des Résultats.
- Électrode : un seul protocole de drop-casting pour tous les échantillons (pas de branche par échantillon) ; la masse de 10 mg est citée.
