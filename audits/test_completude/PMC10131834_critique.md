# Critique des ajouts — PMC10131834

Source : `corpus/text/PMC10131834.txt` (article + SI) ; liste : `audits/test_completude/PMC10131834_ajouts.md`. Lecture seule, aucun script exécuté (lecture de `extractions/PMC10131834.json` limitée à la vérification des rattachements et de la présence de quelques valeurs).

## Contrôles propres à ce test

- **Voie de calcul TD-DFT** : elle ne contient que des valeurs calculées ou des descripteurs de modèle (structures choisies, taille, niveau de théorie, logiciels). Aucune valeur expérimentale (tailles TEM, gaps UV-vis 3,50/3,47/2,17/2,06 eV, longueurs d'onde mesurées 430/507/540/600 nm) n'y est rangée. Les gaps et longueurs d'onde calculés (3,90 eV/364, 3,65/389, 3,20/415, 1,33/612) sont bien ceux du texte principal et de la Fig. S6.
- **Comparaisons littérature** : les 26 valeurs viennent des 13 lignes de précurseurs du Tableau S6 (réf. 4 à 16). Aucune ne vient du travail de l'article : la ligne « trimellitic acid and o-phenylenediamine, 380 nm, 6009 K, 97, (0.32, 0.35), This work » n'est pas reprise (vérifié ligne par ligne : aucune valeur 6009, 97 ou (0.32, 0.35) dans les ajouts). La ligne « poly(vinyl alcohol) and ethylenediamine » (tout en tirets) n'a rien généré, à bon droit. Les « - » ne sont pas devenus des valeurs.
- **Étiquette `[T]`** : l'unique voie ajoutée apparaît sous `[T]` dans la liste, alors que le JSON porte bien `TD-DFT_pyrene_models` (voie `kind: calcul`). C'est un défaut d'affichage du script de delta (première lettre du libellé), pas de l'extraction.

## Tableau

| Catégorie | Voie | Élément | Verdict | Raison |
|---|---|---|---|---|
| paramètre | TD-DFT_pyrene_models, étape 1 | model_blue_fraction = hexahydropyrène + un carboxyle | juste | SI : « One carboxyl group … model of BCDs » |
| paramètre | TD-DFT, étape 1 | model_green_fraction = hexahydropyrène + carboxyle + amide | juste | SI : phrase identique, « model of GCDs » |
| paramètre | TD-DFT, étape 1 | model_yellow_fraction = pyrène + un amide | juste | SI : « model of YCDs » |
| paramètre | TD-DFT, étape 1 | model_red_fraction_carbon_core = benzopyrène | juste | SI : cœur RCDs ; groupes de surface bien non précisés |
| paramètre | TD-DFT, étape 1 | model_size = environ 1 nm | juste | Texte principal ; valable pour les modèles pyrène |
| paramètre | TD-DFT, étape 2 | method = TD-DFT | juste | SI, Computational Details |
| paramètre | TD-DFT, étape 2 | functional_basis_set = B3LYP/6-31G(d,p) | juste | SI et légende Fig. 5 |
| paramètre | TD-DFT, étape 2 | software = Gaussian 09 | juste | SI, même phrase |
| paramètre | TD-DFT, étape 2 | analysis_software = Multiwfn | juste | « applied to analysis the emission wavelength » |
| paramètre | TD-DFT, étape 3 | aromatic_rings_in_models = 2, 4 et 5 | juste | SI : « three models containing 2, 4, and 5 aromatic rings » |
| paramètre | TD-DFT, étape 3 | amide_groups_in_models = zéro, un et deux | juste | SI : « zero, one and two amide groups » |
| not_stated | WCDs | repetitions | juste | Aucun nombre de répétitions ni de lots nulle part |
| not_stated | WCDs (étape 1, dissolve) | addition_order | douteux | « dissolved in 20 mL ethanol » : dissolution conjointe, pas un ordre ignoré |
| caractérisation | WCDs_T220 | PL et CIE, Fig. S1 seulement | juste | Légende Fig. S1 ; aucune valeur numérique écrite |
| caractérisation | WCDs_T180 | idem | juste | Idem |
| caractérisation | WCDs_t6h | idem | juste | Idem |
| caractérisation | WCDs_t14h | idem | juste | Idem |
| caractérisation | WCDs_ratio_1to1 | idem | juste | Idem |
| caractérisation | WCDs_ratio_1to4 | idem | juste | Idem |
| condition de mesure | WCDs_T220 | 0,375 mg mL-1 | juste | Légende Fig. S1 couvre les séries a, b et c |
| condition de mesure | WCDs_T180 | 0,375 mg mL-1 | juste | Idem |
| condition de mesure | WCDs_t6h | 0,375 mg mL-1 | juste | Idem |
| condition de mesure | WCDs_t14h | 0,375 mg mL-1 | juste | Idem |
| condition de mesure | WCDs_ratio_1to1 | 0,375 mg mL-1 | juste | Idem |
| condition de mesure | WCDs_ratio_1to4 | 0,375 mg mL-1 | juste | Idem (la voie de base WCDs est à 0,625 mg mL-1 ailleurs, bien distinct) |
| résultat | WCDs | pic long (599 nm) augmente avec la concentration | juste | Texte, Fig. S8 ; solvant non précisé dans la phrase |
| résultat | WCDs | émission indépendante de λex ; intensités relatives varient | juste | Texte principal, les deux propriétés citées |
| résultat | BCDs | FTIR C-O-C 1282 cm-1 | juste | Tendance « de BCDs à YCDs », bande unique à 1282 |
| résultat | BCDs | UV-vis bande forte UVC 200-280 nm, (π,π*) | juste | « All of the CDs show… » |
| résultat | BCDs | HRTEM sans franges résolues | juste | « only RCDs show well-resolved lattice fringes » |
| résultat | GCDs | FTIR C-O-C 1282 cm-1 | juste | Idem BCDs |
| résultat | GCDs | UV-vis bande UVC | juste | Idem |
| résultat | GCDs | HRTEM sans franges | juste | Idem |
| résultat | YCDs | FTIR C-O-C 1282 cm-1 | juste | Idem ; position unique donnée par l'article |
| résultat | YCDs | UV-vis bande UVC | juste | Idem |
| résultat | YCDs | HRTEM sans franges | juste | Idem |
| résultat | RCDs | FTIR =C-H aromatique 2922 cm-1 | juste | « For RCDs … appears at 2922 cm-1 » |
| résultat | RCDs | UV-vis bande UVC | juste | Idem |
| résultat | TD-DFT | Egap calculé BCDs 3,9 eV | juste | « 3.90 eV/364 nm for BCDs » (calcul) |
| résultat | TD-DFT | λem calculée BCDs 364 nm | juste | Idem |
| résultat | TD-DFT | Egap calculé GCDs 3,65 eV | juste | Idem |
| résultat | TD-DFT | λem calculée GCDs 389 nm | juste | Idem |
| résultat | TD-DFT | Egap calculé YCDs 3,2 eV | juste | Idem |
| résultat | TD-DFT | λem calculée YCDs 415 nm | juste | Idem |
| résultat | TD-DFT | Egap calculé RCDs 1,33 eV | juste | Idem |
| résultat | TD-DFT | λem calculée RCDs 612 nm | juste | Idem |
| résultat | TD-DFT | tendance Egap (modèles à variable unique) | juste | Texte : décroît avec conjugaison et amides (Fig. S5) |
| étape | TD-DFT | model (choix des modèles) | juste | Cohérent avec SI |
| étape | TD-DFT | calculate (calcul TD-DFT) | juste | Idem |
| étape | TD-DFT | calculate (modèles à variable unique) | juste | Idem |
| voie | TD-DFT_pyrene_models | voie de calcul (`kind: calcul`) | juste | Matériau, méthode, citation SI exacts |
| littérature | réf. 4 | CIE (0,34, 0,37) | juste | Tableau S6, ligne poly(styrene-co-glycidylmethacrylat) |
| littérature | réf. 6 | CIE (0,31, 0,33) | juste | Ligne urée + acide citrique |
| littérature | réf. 7 | CIE (0,29, 0,31) | juste | Ligne acide citrique + PAN |
| littérature | réf. 8 | CIE (0,32, 0,31) | juste | Ligne 1,6-dihydroxynaphtalène + L-asparagine |
| littérature | réf. 9 | CRI 68,4 ; CCT 6565 K ; CIE (0,32, 0,33) (3 lignes) | juste | Ligne citrate d'ammonium + EDTA |
| littérature | réf. 10 | CRI 70,6 ; CCT 3938 K ; CIE (0,39, 0,38) (3 lignes) | juste | Ligne 1,5-diaminonaphtalène + CHCl3 |
| littérature | réf. 11 | CRI 82,0 ; CCT 5028 K ; CIE (0,34, 0,38) (3 lignes) | juste | Ligne lycorine HCl + acide borique |
| littérature | réf. 12 | CRI 85,3 ; CCT 8756 K ; CIE (0,268, 0,346) (3 lignes) | juste | Ligne urée + acide phosphorique |
| littérature | réf. 13 | CRI 86,7 ; CCT 5994 K ; CIE (0,33, 0,33) (3 lignes) | juste | Ligne o-PD + acide tartrique |
| littérature | réf. 14 | CRI 87,8 ; CIE (0,37, 0,39) (2 lignes) | juste | Ligne éthanol, CCT « - » non reprise |
| littérature | réf. 15 | CRI 91 ; CCT 3032 K ; CIE (0,42, 0,38) (3 lignes) | juste | Ligne guanidine carbonate + KH2PO4 |
| littérature | réf. 16 | CRI 89 ; CIE (0,33, 0,30) (2 lignes) | juste | Ligne acide 2,2'-dithiodibenzoïque, CCT « - » non reprise |

## Manques restants

- Colonne chromatographique (voie Multicolor_CDs_column) : phase stationnaire, gradient exact ou rapports d'éluants, dimensions, volumes non donnés par l'article ; seul `yield` figure en `not_stated`. À ajouter en `not_stated`.
- Fig. S1 (séries en T, t, rapport) : longueur d'onde d'excitation et solvant du « sample solution » à 0,375 mg mL-1 non donnés. À ajouter en `not_stated` ou en manque de condition de mesure.
- Pic de pression/vide du séchage à 40 °C (« under vacuum » sans valeur) et vitesse de refroidissement de l'autoclave : à vérifier en `not_stated` (non confirmé dans le JSON).
- Conditions de mesure absentes de l'article pour Raman (longueur d'onde du laser), XRD (plage, pas, vitesse), TEM (tension d'accélération), UV-vis (solvant, concentration) : à passer en `not_stated` si la grille les prévoit.
- Littérature, Tableau S6 : la longueur d'onde de pompe (365 à 460 nm) de chaque ligne n'a pas été reprise alors qu'elle est donnée ; condition de mesure utile pour comparer les CRI.
- Pas d'écart repéré sur les valeurs expérimentales principales (tailles, IG/ID, durées de vie, tableaux S1 à S7, CRI/CCT/CIE) : les chaînes testées (74,63, 79,94, 48,06, 51,20, 21,57, 1,143, 4229, 6995, 50110…) sont toutes présentes dans le JSON.

## Remarques sur les rattachements

- Les valeurs des branches WCDs_T220/T180/t6h/t14h/ratio_1to1/ratio_1to4 (non ajoutées par cette passe) ne sont pas dans le texte : le texte n'en donne que la légende Fig. S1. Leur lecture vient de la figure (`from_figure`) ; les ajouts de cette passe (caractérisation et condition) y sont cohérents mais ne peuvent pas être revérifiés sur le texte seul.
- La citation d'ancrage des ajouts de branche est tronquée (« …under different (a) reaction ») ; elle soutient la concentration, pas l'ensemble de la variation. Acceptable.

## Bilan

- Ajouts contrôlés : 77 (11 paramètres, 2 not_stated, 6 caractérisations, 6 conditions de mesure, 22 résultats, 3 étapes, 1 voie, 26 comparaisons).
- Faux : 0.
- Douteux : 1 (`addition_order`, étape de dissolution conjointe).
