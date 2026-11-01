# Journal d'extraction PMC6915586 (points de carbone, effet du solvant, détection du violet de cristal)

- Découpage : une voie de base `CDs-EA` (protocole 2.3 avec l'éthanol, premier échantillon de la Table 1) et une branche par solvant (IPA, MT, NBA, DMF, eau), la seule différence étant le solvant (24 mL, « with the other synthesis parameters fixed »). Le protocole de 2.3 est écrit pour « solvent » sans le nommer : le solvant de la base vient de la section 3.1, signalé en doute.
- Identification R-CDs = éthanol et Y-CDs = n-butanol : déduite de λem 605 / 543 nm (résumé et Table 1) et de « these two solvents (ethanol and n-butanol) ». Lecture retenue ; doute consigné.
- Table 1 : une rangée = une propriété, une colonne = un échantillon (EA | IPA | MT | NBA | DMF) ; chaque valeur est rattachée par le nom de la colonne, en citant la rangée entière. MT et NBA ont tous deux QY 10.0.
- Eau : branche `succeeded: false` (« weak fluorescence », solution brune, agrégation défavorable) ; les auteurs ne parlent pas d'échec, doute consigné. Variation du solvant : l'eau n'a ni pureté ni fournisseur (la phrase fournisseur ne vise que les solvants organiques).
- Formamide, DMSO, THF, cyclohexane : cités dans « A series of solvents … investigated regarding their impacts » sans aucun résultat. Branches créées (règle : une branche par valeur explicitement listée) sans résultats, avec doute sur l'héritage du protocole.
- Section 3.1, redispersion des R-CDs dans sept solvants (Fig. 3) : essai du matériau fini, donc résultats de `CDs-EA`, pas branches. Texte préféré à la figure quand il donne la valeur (eau 615 nm, MT/EA/IPA ≈ 607 nm) ; lues sur la figure seulement les longueurs d'onde dans CP, EAC, MC et les intensités de PL des sept solvants (Fig. 3a, 3b).
- Longueurs d'onde lues sur figure gardées à 3 chiffres (écarts de quelques nm entre solvants) malgré la règle des 2 chiffres significatifs ; précision ±3 nm écrite en doute.
- Séparation sur gel MCI : voie `post_treatment` `MCI_sep_R-CDs` et branche `MCI_sep_Y-CDs` (variation de l'intermédiaire chargé). Les valeurs de fractions (619, 608, 554 nm ; 476, 484, 543, 586 nm) viennent du texte ; Fig. S1 absente, Fig. 4c non ouverte (valeurs données au texte).
- Fig. 2 (UV-vis de la matière première dans les solvants, 1 mg/mL) : pas un résultat des CDs, non extrait.
- Fig. 1a : couleurs du schéma incohérentes avec les spectres, non utilisées. Fig. 5 et 6 : valeurs de TEM, Raman, XPS et FTIR déjà dans le texte et les tableaux ; non ouvertes.
- FTIR : listes appariées (3141, 3128 …) non attribuables, non extraites ; seules les bandes explicitement attribuées (3046 pour R-CDs ; 2965/2933/2878 pour Y-CDs).
- Volume de l'autoclave : « 25-mL lining » dans 3.1 (pas dans 2.3), 24 mL transférés, soit ≈ 96 % ; en équipement et en analyse de sécurité.
- Détection du violet de cristal : rangée en résultats et caractérisation de `CDs-NBA` (test du matériau fini, section 2.5 en conditions). Pas de voie de dispositif.
- `method_sources` : seule la référence B12 (standards de QY) en `autre`. Non retenus : références de contexte sur l'ajustement de λem, de mécanisme et de comparaison de LOD.
- Annexes : figures S1 à S7 présentes seulement par leurs légendes : annotation `limite_reproductibilite` « Annexe absente du dépôt ».
