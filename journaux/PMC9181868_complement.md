# Complément PMC9181868 — tableaux du texte (8 présents, 2 exploitables)

- Constat principal : sur les 7 tableaux annoncés, seuls les Tables 7 et 8 ont des rangées dans `corpus/text/PMC9181868.txt`. Les Tables 1 à 6 (constantes cinétiques k1, k2, qe, R2 ; paramètres de Langmuir et de Freundlich) n'ont que leur légende dans le texte, alors que leurs rangées existent dans `corpus/xml/PMC9181868.xml`. Sans rangée dans le texte, aucune citation valide n'est possible : rien n'est extrait de ces six tableaux, et un doute le dit. Le rendu de ces tableaux par `sections.py` est donc encore défaillant (probablement les en-têtes à colspan et les lignes de sous-titre).
- Table 8 (rendement d'élimination de Pb2+, Cu2+, Zn2+ après calcination à 500, 600, 700 °C) : 6 valeurs ajoutées sur `MgFe2O4-NH2-600` (58, 58, 58 %) et `MgFe2O4-NH2-700` (55, 56, 56 %), colonne choisie par l'en-tête. Les valeurs à 500 °C (73, 59, 62), déjà extraites de la phrase du résumé, concordent.
- Table 7 (comparaison de qm) : 12 rangées de la littérature, non extraites. La rangée « Present work » (145.04 et 55.7 mg/g) ne dit pas à quelle température de calcination elle se rapporte ; la rattacher à une voie reviendrait à deviner, donc doute et pas de valeur.
- Les valeurs de pente, ordonnée et R2 déjà extraites des figures 7 à 18 ne sont pas touchées ; elles seraient à recouper avec les Tables 1 à 6 quand celles-ci seront rendues.
- Trois doutes ajoutés (Table 8, Tables 1 à 6 absentes du texte, Table 7).
- Contrôle : `load.py check` 0 erreur, 0 avertissement.

## Complément 2 : Tableaux 1 à 6 (rangées maintenant présentes dans le texte)

- 105 valeurs ajoutées aux voies MgFe2O4-NH2-500/600/700 : Tableau 1 (Cu2+, ordre 1 et 2) 18, Tableau 2 (Pb2+) 16, Tableau 3 (Zn2+) 18, Tableau 4 (Cu2+, Langmuir et Freundlich) 18, Tableau 5 (Pb2+) 17, Tableau 6 (Zn2+) 18. Noms du type `k2_Cu2+_pseudo_second_order`, `qe_...`, `R2_...`, `qm_Zn2+_Langmuir`, `KL_...`, `KF_Pb2+_Freundlich`, `n_...` ; citation = la rangée entière (trois températures par rangée).
- Règle de rattachement : colonnes lues dans l'ordre 500, 600, 700 °C, trois colonnes (k, qe ou KL ou n, R2) par température. Le premier bloc du Tableau 1 n'a pas d'en-tête de température : même ordre supposé, confirmé par les R2 identiques aux Fig. 7a, b, c.
- Les valeurs existantes (pentes, ordonnées, R2 des figures) ne sont pas touchées. Toutes les R2 de tableau concordent avec celles des figures sauf trois, non ajoutées : Pb2+ ordre 1 à 500 °C (tableau 0.86184, Fig. 9a 0.86836) et à 600 °C (0.86836 contre Fig. 9b 0.86184), soit un intervertissement ; Freundlich Pb2+ à 600 °C (0.7984 contre 0.79804 sur la Fig. 16b).
- Valeurs étranges relevées telles quelles et signalées en doute : k2 négatifs (six valeurs de Cu2+ et Pb2+, une de Zn2+), R2 de Langmuir Pb2+ identique aux trois températures, n identique pour Cu2+ et Pb2+.
- Unité de KF recopiée de l'en-tête rendu (« mmol1(1/n)L1/n/g ») : les exposants sont perdus au rendu du texte ; qm est en mmol/g (le Tableau 7 le donne en mg/g, sans lien de rattachement fait ici pour la rangée « Present work »).
- Quatre doutes ajoutés (rattachement des colonnes, contradiction Pb2+ tableau/figure, valeurs inhabituelles, doute ancien « tableaux absents » périmé). Contrôle : `load.py check` 0 erreur, 0 avertissement, 311 citations vérifiées.
