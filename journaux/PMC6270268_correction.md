# Journal de correction PMC6270268

- Fidélité 1 (Fig. 1e/1f) : image rouverte ; à 1 000 °C la courbe e est nettement au-dessus de f (e ≈ 15 %, f ≈ 13 %, entre d ≈ 19 % et g ≈ 4 %). Ajoutées en `from_figure` (HAP-50 = 15, HAP-300 = 13, ±2 points), citation = légende de la figure 1. Le doute « courbes e et f se confondent » est réécrit (f peut aller de 12 à 14 %).
- Fidélité 2 : AAS ajoutée à HAP-NH2 avec la phrase de 3.3 sur « the samples » ; le lien avec HAP-NH2 vient de la note c du tableau 1, consigné en doute. Analyse élémentaire ajoutée avec la phrase de 2.1 (« characterised by elemental analysis and TEM … ») ; aucun résultat n'existe dans l'article, dit dans `result`.
- Fidélité 3 : load.py n'a aucun contrôle de rôle ; `catalyst` (déjà utilisé dans d'autres extractions, absent de la liste du RUNBOOK) remplace `precursor` pour Pd/C ; doute posé (catalyseur d'hydrogénation).
- Fidélité 4 : la phrase « Four specimens were tested under each condition » est ajoutée au champ `conditions` de toutes les caractérisations GPC (HAP-5 à HAP-300), pas à une seule voie, puisque le même appareil et la même phrase valent pour la série.
- Fidélité 5 : phrase « approximately 111% higher » ajoutée à `tendance_observee` ; 83,18 / 39,31 = 2,11 donc cohérent avec le tableau 1.
- Critique scientifique : aucune valeur modifiée. Huit problèmes regroupés en 8 annotations `limite_reproductibilite` (HAP-NH2 ×2, HAP-5 ×3, HAP-50, HAP-PLGA ×2) plus une annotation d'article sur les contradictions internes (TGA < 6 % vs ≈ 8 %, phrase « decreased from 5/1 to 100/1 », rapport molaire/massique), qui n'existait pas en annotation.
- La base de calcul de 89 g par « mole » de HAP-NH2 est présentée comme hypothèse du critique, déduite à rebours, pas comme affirmation des auteurs.
- `mecanisme_analyse` HAP-5 réécrit en hypothèse (amine normale, amorçage par l'eau, PBLG en grande partie libre) ; ajout d'un `mecanisme_analyse` HAP-NH2 (adsorption du carboxylate sur Ca2+, β-alanine surtout éliminée au lavage). `mecanisme_auteurs` non touchés.
- `securite_analyse` complété : Pd/C sans filtration dans le produit, H2.
- Sources web : Hadjichristidis 2009 et Fleet 2004 sont nommées seulement, sans rien en importer. DOI non vérifiés (10.1021/cr900049t ; Fleet 2004 sans DOI) : à porter dans doi.txt par l'orchestrateur, je n'y ai pas touché.
- Aucun manque (quantités, DMF, « alcohol », H2, etc.) n'a reçu de valeur : tous restent `not_stated`.
