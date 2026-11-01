# Journal d'extraction PMC7075151

- Voie de base CQDs_PC_4h : protocole de 2.2 (453 K, 4 h) ; la durée de 4 h est celle de l'échantillon dont le texte donne le rendement quantique de 20.3 % et que les Résultats appellent « CQDs/PC (4 h) ».
- Branches 2, 6, 8 et 10 h : définies seulement par « samples prepared at 453 K for different times (2, 4, 6, 8 and 10 h) ». L'article ne dit pas qu'elles suivent le même protocole de filtration/séchage ; j'ai gardé l'héritage de CQDs_PC_4h avec la seule durée variée, signalé en doute.
- Résultats des branches : seuls les rendements quantiques de la figure 5c (étiquettes imprimées sur la figure : 17.0, 16.9, 15.2, 2.3 %) ; la légende de la figure 5 sert de citation. La chute d'intensité à 10 h (fig. 5b) est qualitative et va dans l'annotation de comparaison, sans valeur.
- Fig. 7b (masse résiduelle) : lecture à 10 h seulement (393 K ≈ 98 %, 423 K ≈ 87 %), 2 chiffres significatifs ; l'échantillon testé n'est pas identifié, donc résultats rangés en outcomes de la voie de base.
- Formamide : rôle `solvent` bien que seule source d'azote ; volumes séparés non donnés (20 mL au total, rapport 1:1), donc `amount_text` pour formamide et glycérol, aucune division en 10 mL déduite.
- Fournisseurs : la phrase « Glycerol OE-625 silicone LED encapsulation AB glue … Dow Corning » fusionne glycérol et colle ; Dow Corning attribué à la colle seulement, fournisseur du glycérol en `not_stated`. Pureté : « used without further purification » n'est pas une pureté, donc `not_stated`.
- CCT : résumé 5430 K, corps et conclusion 5340 K ; 5340 K retenu, doute noté.
- Dispositif WLED : voie `device` séparée (A-gel/B-gel, 50 mg de luminophore, puce 460 nm) ; le luminophore est un réactif `intermediate` relié à CQDs_PC_4h faute de précision de l'article.
- Échantillons sans voie : phtalimide standard (référence), CQDs dissous dans le DMF (préparation de TEM), échantillons de stabilité thermique.
- Pas de renvoi de méthode dans les sections Méthodes (les renvois sont dans l'introduction et l'interprétation) : `method_sources` vide. Aucune annexe citée ni absente.
- Séchage et broyage : une seule phrase sans valeur, deux étapes (dry, grind) avec grille déclarée en `not_stated`.
