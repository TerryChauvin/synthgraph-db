# Journal d'extraction PMC5028751

- Découpage : six voies de base, aucune branche. L'article ne balaie aucun paramètre de synthèse ; les échantillons sont des préparations distinctes (TGMs, TGHMs, PT, TiO2 sans GO, photoanodes).
- TGMs mis en voie `intermediate` (étapes 1–4 de la section Experimental) et réutilisé comme réactif `intermediate` de TGHMs, pour ne pas dupliquer les étapes. Voie de base de l'article : TGHMs (`is_baseline`).
- « TGMs » désigne deux choses : l'intermédiaire enrobé de GO, et l'échantillon de comparaison « directly autoclaved » à 180 °C 24 h. Deux voies (TGMs, TGMs_autoclaved), sans résultat pour la seconde ; doute écrit.
- PT : la phrase « same as the above experimental section. Differently ... directly autoclaved » ne dit ni milieu liquide ni séchage ; je n'ai extrait que l'autoclave (180 °C, 24 h) et déclaré le milieu en `not_stated`. Pas de branche de TGHMs, car l'héritage n'est pas fondé.
- TiO2_HCl_noGO : voie indépendante (« directly hydrothermal treated in HCl solution without the graphene oxides wrapping process »), sans température ni durée ; pas de parent.
- Échantillon TiO2@rGO à facette {101} : renvoyé au SI et à la réf. b47, absent du dépôt ; `route: null` dans l'inventaire, entrée `method_sources` (protocole_complet) et annotation « Annexe absente du dépôt ».
- Tests photocatalytiques : rangés en `outcomes` de TGHMs et PT, pas en branches. Les concentrations de Rh B et de Cr(VI) du balayage (Fig. 7c, 7d) sont des conditions de mesure ; elles sont dans le nom de la propriété (conditions écrites dans la légende).
- Figures lues (précision d'environ ±2 points) : Fig. 7a (TGHMs Rh B 89 % à 120 min, TGHMs Cr(VI) 50 %, PT Cr(VI) 14 %, PT Rh B 35 % à 150 min), Fig. 7c (5 barres), Fig. 7d (5 barres). Citation = légende de la figure 7.
- Contradiction texte/figure : texte « Rh B near 100 % à 150 min » pour TGHMs ; la courbe s'arrête à 120 min (~89 %). Les deux sont gardés, le texte avec sa citation, la figure en from_figure ; doute écrit.
- Fig. 7c : la concentration de Cr(VI) associée à chaque concentration de Rh B n'est pas donnée ; je n'ai pas supposé de couplage.
- Constantes cinétiques Kapp : valeurs du texte (4,47 × 10−2 et 2,35 × 10−2 min−1) en `value_text` (le contrôle refuse la conversion en 0,0447) ; Table S1 absente.
- XRD : la courbe « a » de la Fig. 5a n'est pas explicitement nommée PT ; I004/I101 de PT (0,28) pris dans la phrase de comparaison du texte.
- Photocourant : « environ 6 fois » en outcome de TGHMs (ratio donné par l'article), les courbes sont en Figure S4 absente. Voie `device` pour les photoanodes (FTO, goutte de 10 uL à 5 mg/mL, séchage IR 60 °C 2 h), partagée par PT et TGHMs.
- Fournisseur et pureté : aucune phrase générale ne couvre les réactifs ; tout en `not_stated`.
- Sécurité : aucune précaution dans l'article ; uniquement des annotations `securite_analyse`.
