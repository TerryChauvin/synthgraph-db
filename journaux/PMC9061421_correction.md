# Journal de la correction, PMC9061421

- Constat 1 (« Filter the supernatant ») : corrigé, « the solution » ; l'article dit « the obtained solution was centrifuged … and filtered ».
- Constat 2 (température de l'étape 2) : `not_stated` conservé (décision de l'orchestrateur). Le renvoi à la température mesurée de 228 °C (résultat `microwave_reaction_temperature_final`) est ajouté au doute existant et à l'annotation `limite_reproductibilite` des manques.
- Constat 3 (700 W) : le paramètre `power` devient `power_nominal_oven` (valeur 700 W gardée, citation inchangée), la description de l'étape dit « nominal power 700 W » et le détail de l'équipement précise que la puissance appliquée n'est pas donnée ; nouveau doute et phrase ajoutée à l'annotation de manques. Pas de value_text : il n'aurait contenu que des mots hors article.
- Constat 4 (« against a dialysis tube ») : reformulé « in a dialysis tube (MWCO = 1000 Da) ».
- Constat 5 (annotation de sécurité) : réécrite en tête par « Analyse (non écrite dans l'article) » ; « bécher ouvert » remplacé par « il ne dit pas s'il est couvert » ; K2Cr2O7 étiqueté seul sel de Cr(VI) listé, sans affirmer son emploi. Les mots « arc éventuel » et « brûlures, projections » sont retirés.
- Constat 6 (eau de rivière) : nouveau doute avec les deux citations opposées, plus une annotation `limite_reproductibilite` ; aucune valeur corrigée.
- Constat 7 (Fig. 5) : doute et annotation reformulés (« non relevés », Ni2+ ≈ 1000 et Zn2+ ≈ −900 non nuls) ; les valeurs relevées sont inchangées.
- Critique scientifique : les quatre `probleme` (identité du produit, sécurité, XPS, bioimagerie) et les réserves concises (LOD, IFE, sélectivité, EPA, base du rendement) sont des annotations `limite_reproductibilite` sans citation, valeurs inchangées. L'identité du produit s'appuie sur Essner 2018 et sur les rapports O/C calculés par le critique (1,13 contre 0,82), non vérifiés par moi contre une source externe.
- Sécurité : seul le risque (anhydride maléique + amines > 150 °C, source NOAA CAMEO) est consigné ; aucun protocole ni condition nouvelle.
- `mecanisme_analyse` réécrit : présenté comme hypothèse, polycondensation de type polysuccinimide parallèle à la décomposition de l'urée, oligomère peu carbonisé plutôt que point de carbone ; le « noyau graphitique » de l'ancienne version est retiré de l'affirmation. `mecanisme_auteurs` intouché.
- Aucune voie retirée ni renommée ; `method_sources` reste vide (le critique de fidélité l'a vérifié).
