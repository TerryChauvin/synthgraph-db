# Journal d'extraction PMC9036664

- Découpage : deux voies de base indépendantes. `LSMF_foam` (kind `intermediate`) = mousse précurseur préparée par les auteurs ; `NCDs` (kind `material`) = calcination de cette mousse. La mousse est réutilisée comme réactif de rôle `intermediate` dans NCDs (pas de pureté ni de fournisseur demandés). Les deux sont des voies de base car aucune comparaison ni variation n'est faite entre échantillons : zéro branche.
- Aucune série de synthèse (une seule température, 250 °C) : les seize ions métalliques, la température et le pH de mesure sont des conditions d'essai du matériau fini, rangées en `outcomes` de NCDs et non en branches (règle « tests du matériau fini »).
- Tensioactif : « sodium dodecyl sulfonate » dans « Experimental materials » mais « sodium lauryl sulfate » dans la préparation. Je n'ai pas fusionné les deux noms (pas de déduction) : le fournisseur de ce réactif est déclaré `not_stated`, avec un doute.
- Les autres réactifs de la mousse (mélamine, paraformaldéhyde, chlorure d'ammonium, triéthanolamine, éther de pétrole) reçoivent le fournisseur « Tianjin Kermel Chemical Reagent Company » et la phrase des matériaux en `supplier_quote` ; la lignine sulfonate reçoit celui de Qianjin Welfare. « All reagents were used as received » ne donne aucune pureté : `purity` non cité partout.
- Mélamine : 0.1 mol et « about 12.0 g » ne concordent pas exactement (12,6 g attendus) ; je garde la quantité de matière, la masse reste en `amount_text`. Même chose pour le paraformaldéhyde (0.3 mol, 9.0 g).
- Calcination : durée, vitesse de chauffe, débit de N2 et four absents des Méthodes et des Résultats (je n'ai trouvé que « 250 °C » et « N2 »), déclarés `not_stated`. Lyophilisation : température, durée et pression non citées.
- Étape de durcissement : action `cure` (durée 24 h, 80 °C) ; elle n'entre pas dans la grille de chauffage, mais j'ai gardé les deux paramètres.
- Étape 5 de la mousse : « continue to stir until the solution is clear » enregistré en `value_text` pour la durée, sans nombre.
- HRTEM : l'espacement de 0.21 nm attribué à (002) contredit le pic XRD à 25,6° (≈ 0,35 nm). Recopié tel quel, doute écrit ; pas d'annotation corrigeant les auteurs.
- Excitation : Méthodes = 500 nm, Résultats = « strongest ... under excitation at 514 nm ». Conditions de caractérisation = 500 nm (section la plus détaillée, Méthodes).
- Taille : 5–20 nm (TEM) et « about 10 nm » (Conclusion) extraites comme deux résultats distincts.
- Figure lue : Fig. 6a (F/F0 de Fe3+ ≈ 0,63, barres 3D, précision ≈ ±0,03). Les autres ions ne sont pas extraits un par un (tendance en annotation). Fig. 2 ouverte pour vérifier la morphologie ; aucune valeur nouvelle. Les autres figures sont des spectres sans valeurs de synthèse ; Fig. 5d (pH) : seule la valeur 3.74 du texte est reprise.
- `method_sources` vide : le seul renvoi dans les Méthodes (cit30, cit31) porte sur la fonction bi-exponentielle d'ajustement de durée de vie, c'est une formule d'analyse, pas une source de méthode.
- Aucune annexe n'est citée dans l'article ; `corpus/fig/` contient une image `t1` qui est l'équation de τavg.
