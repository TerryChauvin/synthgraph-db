# Journal d'extraction PMC9795147 (N@CQDs de feuilles d'Eruca sativa)

- Une seule voie de base `N@CQDs` : l'article décrit une unique condition de synthèse (micro-ondes 4 min). Aucune branche : les optimisations de pH (7), de concentration de N@CQDs (0,15 mg mL−1) et de temps de réaction (10 min) (Fig. 3b-d, Tableau 4) portent sur le dosage fluorimétrique du modafinil, pas sur la fabrication du matériau.
- Puissance : 700 W retenu (« Only low-power microwave-assisted synthesis at 700 W for 4 min », introduction ; résumé « at 700 w ») contre « 0- 1000 W for 4 min » dans la section de synthèse, qui décrit la plage de l'appareil. Contradiction notée en doute, citation de l'introduction utilisée.
- Réactif : seul le filtrat de feuilles (40 mL) est chiffré ; masse de feuilles, liquide d'extraction, pureté et fournisseur déclarés `not_stated`. Rôle `carbon_source` (le filtrat fournit aussi l'azote d'après les auteurs, « nitrogen from natural source »).
- « crushed well and filtrate » découpé en deux étapes (grind, filter) avec la même citation, faute de phrases séparées.
- Étape micro-ondes : température déclarée non citée malgré la mention d'une sonde IR (0–300 °C) dans la liste d'équipement, aucune valeur n'étant donnée.
- Étape sonication : « The residue was dispersed » sans milieu de dispersion ; doute ouvert, milieu en `not_stated`.
- Taille HR-TEM « 2.0 nm ± 0.21 » : Fig. 1b (lue) montre un espacement réticulaire de 0,21 nm dans l'encart ; confusion possible des auteurs, texte retenu. Valeur 0,21 nm lue sur la figure ajoutée en résultat `from_figure` (lecture à basse résolution).
- XPS : pics donnés à 395,6 eV pour N 1s puis 399,2/400,8 eV dans le détail ; incohérence conservée en doute, aucune correction.
- Tableaux 2 à 10 (récupérations, plasma, pharmacocinétique, uniformité de teneur, robustesse) non extraits en résultats du matériau : validations analytiques du dosage du modafinil. Seul le Tableau 1 (plage, LOD, LOQ, r²) est repris comme performance de la sonde.
- Échantillons sans voie dans l'inventaire : modafinil/Bravamax (produit commercial, analyte) et plasma humain (matrice).
- `method_sources` : renvois CR22/CR23 (précipitation des protéines au méthanol) et CR33 (protocole USP) gardés comme `autre`, route nulle, car ce sont des protocoles d'essai ; les renvois de contexte (CR13, CR16-18) ne sont pas des sources de méthode de synthèse.
- Pas de `securite_auteurs` : l'article ne donne aucune précaution ; le contrôle exige une citation, donc seule `securite_analyse` est écrite.
- Tableau 11 (verdissement GAPI/AGREE) : image seule dans le dépôt, sans texte, non lue (hors synthèse).
