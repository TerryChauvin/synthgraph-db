# Journal d'extraction PMC8125317

- Découpage : une voie de base ZnO-300 (synthèse du LZHC puis calcination à 300 °C) et deux branches ZnO-500 et ZnO-700. La phrase « calcinated ... at 300, 500, and 700 °C for 2 h with a heating rate of 250 °C h−1 » dit que seule la température diffère ; les branches héritent donc des étapes 1 à 4 et ne varient que l'étape 5.
- Choix de la base : ZnO-300 parce que c'est le premier échantillon listé par les auteurs, bien que ZnO-700 soit le plus étudié.
- LZHC : précurseur isolé et séché, mais non caractérisé dans cet article (renvoi à la publication antérieure, Fig. S2 absente). Gardé comme étapes 1 à 4 de la voie ZnO-300, sans voie propre ; inscrit à l'inventaire avec `route: null` et cette raison.
- Réactifs : concentrations 0,05 M et 0,25 M recopiées comme montants en M, sans volume (non cité). Pureté et fournisseur pris dans la même phrase que la quantité (98 % et 99,0–100,5 %, Sigma–Aldrich). L'urée est rangée en `precipitating_agent` : elle libère le carbonate qui précipite le LZHC (rôle déduit, l'article ne le dit pas).
- Séchage à température ambiante : `value_text` « room temperature », pas de nombre.
- Résultats rangés par rangée de phrase « respectively » : BET 38,51 / 11,68 / 6,41 pour 300 / 500 / 700 ; bande interdite 3,25 / 3,26 / 3,26 ; k UV 0,037 / 0,038 / 0,091 ; k soleil 0,040 / 0,046 / 0,084 ; dégradation UV 91 / 92 / >99 ; soleil 92 / 95 / >99. Ordre vérifié sur la phrase et sur les légendes des figures 4c et 5c.
- « >99 % » gardé en `value_text` sans valeur numérique pour ne pas transformer une borne en valeur.
- Propriété de dégradation UV nommée sans « 60 min » car la phrase qui porte les pourcentages ne cite pas la durée ; la phrase solaire la cite, donc `..._sunlight_60min`.
- Valeurs lues sur figure (Fig. 4b, 5b, 4e) : seulement C/C0 à 15 min, le point où les courbes se séparent le plus ; les valeurs à 60 min sont dans le texte. Précision ±0,03 environ ; signalé dans les doutes. Figures 1 à 3 sans valeur numérique supplémentaire.
- Cycles de réutilisation : le lavage, la centrifugation et le séchage sous vide du catalyseur récupéré forment une voie `post_treatment` (ZnO-700_recovery) ; le premier cycle est rattaché à ZnO-700, les 2e et 3e à cette voie. Réactif d'entrée en rôle `intermediate`, quantité déclarée non citée (« same amount of powder »).
- Témoin RhB sans catalyseur : pas de voie (rien n'est synthétisé).
- Annexes : Fig. S1, S2, S3 absentes (aucune section Supporting Information dans le fichier) ; signalées en `limite_reproductibilite`.
- Contradictions de l'article mises en doute sans correction : laser HeNe à 532 nm, plage Raman « 70 and 17,800 nm », renvoi Fig. 3a/3b pour la réflectance.
- Source de méthode : un seul renvoi (B56, protocole complet de la voie ZnO-300). Les renvois à la méthode de Kubelka–Munk et à l'IUPAC sont des méthodes d'analyse, non retenus.
