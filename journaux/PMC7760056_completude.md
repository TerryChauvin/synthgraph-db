# Journal du test de complétude — PMC7760056

- Aucune voie ni étape de synthèse modifiée : l'extraction d'origine couvrait déjà les réactifs, les 9 voies, les tableaux 1 et 2 et les conditions du test catalytique. Seuls des résultats, des conditions de mesure, des valeurs de référence et la liste de comparaison ont été ajoutés (vérification : tout l'existant est identique à la version précédente).
- Pas de section Supporting Information dans `corpus/text` et l'article ne cite pas d'annexe ; aucune figure ouverte, car aucun résultat chiffré n'en dépend en plus du texte.
- Tableau 3 : les 8 lignes de littérature vont dans `comparisons` (route AgNPs-opt, ref_id pris dans `corpus/refs/PMC7760056.txt`, B79 partagé par Zeo-TiO2 et Zeo-ZnO). La ligne « Present Work » (93.39 %) est un résultat de l'article, donc en `outcomes` de AgNPs-opt, avec un doute sur l'écart avec 93.37 et 93.36.
- Positions DRX : la deuxième est écrite « 44. 83 » dans l'article ; le contrôle de citation refuse 44.83 en `value_num`, donc `value_text` avec la mention de la lecture. Pas d'unité écrite pour les 2θ : `unit` laissé vide, doute ajouté.
- Bandes FTIR : le texte ne dit pas si les positions viennent du spectre de l'extrait ou des AgNPs (« similar peaks ») ; rattachées à AgNPs-opt (Fig. 7), doute ajouté. Attributions recopiées dans le nom de propriété.
- Raies EDX : l'article écrit « binding energies » pour des raies d'émission Lα, Lβ, Lβ2 ; recopié tel quel, doute ajouté.
- Valeurs de référence des calculs : deux entrées `characterizations` (nombre d'atomes par particule : ρ, D, M, NA ; concentration molaire : N total, V, N), plus K = 0.9 de Scherrer et la poudre pour la DRX dans deux autres. Chacune a sa citation ; aucune n'est ajoutée à une chaîne `conditions` existante. Pas de voie `calcul` : ce n'est pas une simulation, seulement un calcul arithmétique de l'article (déjà annoté comme surestimé par la critique scientifique).
- NA est écrit « 6.023 × 1023 » dans l'article (exposant aplati par l'extraction du XML) ; reporté en « 10^23 » dans mes conditions avec la mention de l'aplatissement.
- Écartés comme hors sujet : numéros de figures et de références, échelle SEM de 2 µm, 4000× déjà présent, constantes générales (R = 8.314, π = 3.14), valeurs de la littérature citées dans l'introduction.
- Le témoin catalytique sans AgNPs reste sans valeur dans l'article (déjà dans l'inventaire) ; rien à ajouter.
- Aucune case `not_stated` ajoutée : les conditions de mesure absentes ne vont pas dans `not_stated`, et la grille de synthèse était déjà remplie.
