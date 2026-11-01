# Journal d'extraction PMC10674298 (CaTiO3, méthode Pechini)

- Découpage : une seule voie de base `CaTiO3-700` (Méthodes 2.1) ; une branche `CaTiO3-350` pour l'échantillon traité à 350 °C, seul autre traitement thermique comparé (FTIR, Fig. 6 / Tableau 4). Pas de branche pour les doses de catalyseur (3, 5, 10, 15 g/L) : ce sont des conditions d'essai du matériau fini, rangées en `outcomes` de la voie (règle « tests du matériau fini »).
- Branche 350 °C : phrase citée « IR spectra of the samples that were heat-treated at 350 and 700°C were taken ». L'article ne dit pas que les étapes 1 à 6 sont identiques ; héritage accepté car la comparaison porte uniquement sur la température finale, signalé en doubt.
- Durée du traitement à 350 °C : 4 h lue sur l'étiquette imprimée « 350 °C / 4 H » de la figure 6b (`from_figure`, citation = légende de la figure 6). Le texte ne donne aucune durée.
- Contradiction Fig. 6 : le texte 3.3.1 place le spectre 350 °C en 6a, la légende, la figure et le Tableau 4 le placent en 6b. Légende et tableau retenus (doubt).
- Contradiction Fig. 4 : légende « 900 °C », texte et résumé 700 °C. 700 °C retenu, aucune branche à 900 °C (doubt).
- Résumé contre Tableau 6 : le résumé attribue 79,4 % au méthyl orange à 5 g/L ; le Tableau 6 et le texte donnent 88,1 % à 5 g/L (79,4 % = 15 g/L). Tableau retenu (doubt).
- Pourcentages de dégradation : pris dans les phrases « respectively » (ordre 3, 5, 10, 15 g/L écrit dans la phrase) et non par position dans le tableau ; constantes k prises par rangée du Tableau 6 nommée par la dose, en vérifiant la concordance avec la légende de la figure 14c,d.
- Constantes de vitesse du témoin sans catalyseur (0,000153 et −0,000292 min−1) : valeurs imprimées dans la légende du graphique 14c,d, extraites en `from_figure` ; les barres de la figure 14e,f n'ont pas été converties en nombres (graduation de l'axe des temps ambiguë : 13 groupes de barres pour des repères tous les 20 min).
- pH de synthèse : « a suitable pH » seulement. Le titrage (3.1) se stabilise à pH 8–8,2 et 0,300 mL/s, mais c'est un essai de titrage distinct (2.2) ; `ph` déclaré non cité, titrage gardé en caractérisation.
- Quantités des cinq réactifs : jamais données (`amount` non cité) ; pureté et fournisseur pris dans la même phrase que le réactif (Merck Millipore / Sigma Aldrich).
- Tableau 3 : valeurs du perovskite prises dans la première colonne (Structure = Orthorhombic) et rutile dans la seconde ; facteur de tolérance 0,903 (tableau) malgré 0,902 dans le texte ; unités de Ti–O et Ti–O–Ti non écrites, laissées vides plutôt que déduites.
- Échantillons sans voie : témoin de photolyse sans catalyseur et matériaux CaTiO3 de la littérature du Tableau 7 (non préparés par les auteurs). La poudre pré-calcinée (TGA/DSC) est rattachée à l'étape 6 de la voie de base.
- Aucune annexe mentionnée ; `method_sources` vide (aucun renvoi bibliographique dans les Méthodes ; équations de Kubelka–Munk, Scherrer, BET non comptées).
