# Journal d'extraction PMC6270268

- Voie de base de la série : HAP-5 (premier échantillon du tableau 2). Les six autres (HAP-10 à HAP-300) sont des branches à une seule variation, `molar_ratio` à l'étape 2 (« HAP-10 | 10/1 », rangée entière du tableau 2). L'article ne décrit qu'un protocole pour toute la série ; héritage complet accepté, consigné en doute.
- HAP-NH2 est une voie `intermediate` à part (protocole 3.2, premier paragraphe) ; HAP-5 le reçoit en réactif de rôle `intermediate`, sans quantité (« various amounts », seuls les rapports sont donnés).
- HAP-PLGA est une voie `post_treatment` de base (étapes propres), réactif `intermediate` = HAP-100 (« HAP-100, 0.5 g »). Je n'en ai pas fait une branche : le protocole n'a ni les mêmes réactifs ni les mêmes étapes.
- Rapport « molar » ou « weight » : le texte 2.1 dit « feed weight ratio » une fois, le tableau 2 et le reste du texte disent « molar ». Lecture molaire retenue, doute écrit.
- Tableau 1, rangée HAP-NH2 : « -- | -- | -- | -- | 38.46 | 15.89 » lu comme rendement, Mn, PDI, greffage absents, puis Ca théorique 38,46 % et mesuré 15,89 % (la ligne de sous-titre « Theoretical value | Measured value » porte sur la dernière colonne seulement).
- Mn : colonne sans unité dans l'article, `unit` laissé à null ; pour HAP-5/10/20 (« -- ») j'utilise la phrase « could not be detected by GPC » comme résultat, pas une valeur nulle.
- Phrase TGA « weight loss … increased when the ratio was decreased from 5/1 to 100/1 » : contredit tableau 1 et figure 1, donc non extraite et doutée. Le « less than 6% » de HAP-NH2 est extrait tel quel alors que la figure 1a montre ≈ 8 % de perte : les deux gardés, doute.
- Figure 1 lue (TGA, masse résiduelle à 1 000 °C) : a, b, c, d, g, h. Courbes e (HAP-50) et f (HAP-300) superposées, non lues. Courbe h négative (≈ −5 %) gardée avec mention d'artefact. Correspondance lettre-échantillon prise dans la légende (f = HAP-300, g = HAP-200, h = HAP-100).
- Spectres IR : la première phrase de 2.6 (PO43−, C=O, N-H) n'attribue pas d'échantillon ; rangée sur HAP-NH2 (spectre a, premier de la liste), HAP-100 pour les bandes explicitement liées à la figure 6b.
- HAP non modifiée (TEM 15,3 nm, DRX) : pas de protocole dans les Méthodes, `route: null` dans l'inventaire ; la taille de 15,3 nm n'est rattachée à aucune voie.
- BLG-NCA : monomère synthétisé selon Mori et al. (B32), simple réactif de HAP-5 avec amount/purity/supplier non cités ; entrée `method_sources` de rôle `precurseur`. Le γ-benzyl-L-glutamate (Sigma-Aldrich) n'est pas un réactif des protocoles décrits, donc non listé.
- Fournisseurs : Fengchuan (Ca(OH)2), Tianjin Damao (H3PO4), Sigma-Aldrich + « analytical purity » pour la β-alanine (phrase qui vise aussi le γ-benzyl-L-glutamate) ; pureté de Ca(OH)2 et H3PO4 non citée. DMF, méthanol, Pd/C, eau : aucune pureté ni fournisseur.
- Hydrogénation : aucune source d'hydrogène, pression ni température dans le texte ; déclarées non citées (pas de H2 ajouté comme réactif).
- Annexes : aucune annexe ni renvoi à un tableau SI dans le texte ; pas d'annotation « Annexe absente ».
