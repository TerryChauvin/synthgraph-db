# Journal critique de fidélité — PMC10077552

- Ma liste d'échantillons (faite avant l'extraction) : Ni, Co, NiCo0.1, NiCo0.3, NiCo0.5 (série de rapport) ; calcination 300/400/500/600 °C (Table 1, Fig. 7a) ; réduction 400/500/600/700 °C (Fig. 7b) ; catalyseur récupéré (Fig. 8b). Identique à `sample_inventory` : 13 voies, aucun échantillon oublié. Solvants, température et pression de réaction (Fig. S4, S5) sont des conditions de test, donc outcomes et non branches (règle RUNBOOK).
- Tableau 2 (image 0010.jpg) : les 12 rangées lues une à une, tout est exact (ex. m-NAP Ni 65.8/95.3, NiCo0.3 90.4/99.6 à 5.0 h ; p-CNB 98.7/95.9). Aucun constat.
- Fig. 6 : Co ≈ 17 % et NiCo0.1 ≈ 93 % à 120 min confirmés. NiCo0.5 se lit ≈ 95 % alors que le texte écrit 92 % : écart de 3 points, sous le seuil de 10 %, et déjà tranché en doubt par l'extracteur (valeur du texte). Pas de constat ; mis dans les notes.
- Fig. 8b : 20/12 % (20 min) et 45/37 % (40 min) confirmés, courbe « New catalysts » identique à NiCo0.3 de la Fig. 6. Fig. 7a/7b : barres cohérentes avec le texte.
- `not_stated` : vérifié mot à mot (volumes, vitesses de chauffe, débits, four, agitation, pureté de l'eau, de SBA-16, rendement) ; aucune de ces cases n'est dans le texte ni dans l'annexe, 0 faux.
- Héritage Ni/SBA-16 et Co/SBA-16 : l'extracteur a un doute sur l'héritage des étapes, mais l'étape 1 hérite aussi des concentrations 0,8 M du métal absent ; constat `deduit`, `probable` car l'article ne décrit pas la préparation des monométalliques.
- Conditions de Fig. S5b (120 °C, pas 80 °C) : seule la légende d'annexe le dit ; le résultat « ≥ 0,5 MPa » est enregistré sans cette condition. Constat `manquant`, `sure` (citation exacte).
- Résultats textuels non repris (pics TPR, énergies XPS, TEM de Co) : `manquant` mineur, `sure`, car chiffrés dans le texte ; ce sont des détails de caractérisation, pas de la synthèse.
- Annotation conclusion_auteurs : durcit en faits des hypothèses (« may be due », « possibly due to pore collapse ») ; `mineur` `probable`.
- Incohérence de l'article : BET 600 °C (248) > 500 °C (232) alors que le rendement baisse ; auteurs invoquent pourtant « mainly due to the decrease of specific surface areas ». Signalé comme `mineur` à traiter par annotation limite_reproductibilite, sans changer de valeur.
- `method_sources` vide jugé correct : les renvois [[ref]] du texte portent sur le contexte, l'interprétation XPS/TPR et les sous-produits, aucun sur la préparation ou le protocole de test.
- Non retenu comme constat : le choix de `value_text` = nom d'échantillon pour les variations NiCo0.1/NiCo0.5 (aucune quantité nominale dans l'article, doubt présent) ; la formule « Ni1Co0.5 » contre « Co/Ni 0.5/1 » (déjà en doubt).
