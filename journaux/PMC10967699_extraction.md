# Journal d'extraction PMC10967699

- Découpage : PCN-600 est la voie de base. PCN-600-NS-10 en est une branche (même réactifs, même chauffage de 150 °C pendant 12 h) avec trois variations tirées de la partie « Doping » : ajout de la BIT (10 mg), lavage au DMF deux fois au lieu de trois, séchage à 80 °C au lieu de 70 °C. Les auteurs ne disent pas « same procedure » entre les deux ; l'héritage repose sur la ressemblance des deux paragraphes (doute noté).
- PCN-600-NS-20 : branche de PCN-600-NS-10 car la phrase dit « The same procedure obtained another sample except that the amount of NS-ligand treated was 20 mg » ; une seule variation (quantité de BIT).
- Variation « dopant » : nom explicite car la BIT est absente du parent ; le contrôle émet un avertissement attendu (ajout, pas remplacement).
- Refroidissement « ambient temperature » (PCN-600) contre « room temperature » (NS-10) : jugé identique, non enregistré comme variation ; signalé en `limite_reproductibilite`.
- Régénération : rangée en voie `post_treatment` (étapes et tableau 4 du recyclage sur cette voie) pour conserver le protocole reproductible, bien qu'elle nettoie le matériau sans le transformer (doute noté). Le volume « 5 mL of water, acetone, and ethanol » est lu comme 5 mL par solvant.
- Essais d'adsorption et de photocatalyse (pH, dose, concentration, scavengers, cinétique, thermodynamique, isothermes) : rangés en `outcomes` de PCN-600-NS-10 comme tests du matériau fini ; le protocole d'essai est décrit dans une `characterizations`.
- Résumé contre texte : le résumé donne 43 % pour PCN-600, le texte 52 % (12 % + ~40 %) ; texte retenu (doute).
- Tableau 1, rangée 20 mg L−1 (29 %, 42 %, k1 = 0,0084) incompatible avec l'essai de référence à 20 mg L−1 (28 %, 59 %, k1 = 0,0129) ; rangées recopiées telles quelles sous leur concentration, doute noté.
- Tableau 2 en 298/318/338 K, texte et tableau 3 en 293/313/333 K : chaque valeur rangée sous la température de sa propre rangée. ΔH et ΔS (une seule rangée du tableau) repris des phrases du texte.
- Band gaps : ordre direct/indirect inversé entre les deux phrases du texte, et 2,53 eV (direct, dopé) > 2,50 eV (direct, nu) malgré une « diminution » annoncée ; extraction littérale phrase par phrase, doute noté.
- Figures lues : Fig. 4b (pH 2, 4, 8, 10, lecture à 120 min, ±3 points), Fig. 4a (NS-20 total ≈ 63 %), Fig. 4d (capacité à 20 mg L−1 ≈ 44). Figures 5 et 7 non lues (valeurs déjà dans le texte).
- Pureté et fournisseur : annexe S1, liste unique « were obtained from Macklin » ; citation recopiée en joignant les lignes de l'extraction (le contrôle l'accepte). TCPP et DMF sans pureté écrite : `not_stated`.
- Constantes cinétiques par pH et par dose (Fig. S6b-c, S7b-c) : présentes dans l'annexe mais association aux conditions illisible dans le texte extrait ; non extraites (annotation `limite_reproductibilite`).
- Annexes : aucune annexe absente (S1, S2, figures et Table S1 sont dans le fichier).
- Source de méthode : une seule, cit19 (CrystEngComm 2012) pour PCN-600, rôle `protocole_adapte`.
- Échantillon sans voie : diagramme XRD simulé de PCN-600 (Fig. 1a), pas un échantillon synthétisé.
