# Journal d'extraction PMC9083554

- Voie de base : 96CuFe2O4-4RGO, l'échantillon le plus étudié (catalyse, électrode, DFT). Le protocole générique des Méthodes est écrit pour « les nanocomposites » sans quantité ; les quatre compositions et CuFe2O4 pur sont des branches (« Using this procedure ... », « the same procedure, but here GO was not added »).
- Teneur en RGO : exprimée en % en masse du composite final, pas en masse de GO ajoutée. La variation porte sur le réactif « graphene oxide dispersion (route GO) » avec `value_num` 2/6/8 wt% et un `value_text` qui le précise ; CuFe2O4 pur = réactif « absent ».
- Pure CuFe2O4 gardé en branche héritant de toutes les étapes (l'article dit « same procedure »), car l'étape 1 ne concerne pas seulement le GO.
- GO : voie `intermediate` à part, décrite dans l'ESI (texte présent) ; une entrée `method_sources` (cit53, Hummers et Offeman) en `protocole_adapte` à partir de la phrase « modified Hummer's method ».
- Table S5 (ESI) : le PDF l'a rendue une cellule par ligne. Chaque rangée est citée en une chaîne continue (« 98 CuFe2O4-2RGO 7 8.0 (± 0.8) × 10-3 ») qui relie le nom, le temps et kapp. Les Résultats renvoient à « Table S4 » : c'est une erreur de numérotation, signalée en doute et en limite de reproductibilité.
- Contradiction CuFe2O4 pur : kapp = 5.7 (Table S5, Conclusion) contre 4.2 ×10-3 s-1 (Table S6, « This work »). 5.7 retenu, le doute le dit.
- Contradiction époxydation : 100 °C sous N2 (Méthodes) contre 80 °C pendant 8 h (Résultats). Aucun paramètre numérique n'a été créé : les deux figurent dans les conditions de la caractérisation « catalytic test ».
- Tests catalytiques rangés en `characterizations` (conditions, instruments) et `outcomes` des voies matériau, jamais en branches (règle des tests du matériau fini). Blanc sans catalyseur, RGO seul (synthèse non décrite) et catalyseur recyclé : dans l'inventaire avec `route: null`.
- Électrodes : voie `device` de base pour 96CuFe2O4-4RGO en KOH 3 M, branches pour CuFe2O4 pur, RGO (remplacement du matériau actif) et K4[Fe(CN)6] 0,1 M (additif de l'électrolyte, parent_value « none », d'où un avertissement de nom de paramètre expliqué en doute). Les résultats électrochimiques sont sur ces voies et nulle part ailleurs. La recette de pâte 80/10/10 est héritée car l'article la décrit une seule fois pour les trois matériaux actifs.
- Cellule à deux électrodes et démonstration de la DEL : une voie `device` propre, avec très peu de détails (non cité déclaré).
- Pic redox 0,32/0,40 V : rangé sur l'électrolyte avec K4[Fe(CN)6] (la phrase ne nomme pas l'électrolyte), doute inscrit.
- Taille des particules (Scherrer ~14 nm, MET 15–20 nm) : échantillon non précisé ou groupe de deux échantillons, donc une annotation de groupe et aucune valeur dans une voie.
- « respectively » : BET, volume poreux, magnétisation, Rct, TGA lus par l'ordre des échantillons de chaque phrase (pur puis 96CuFe2O4–4RGO ; 96 puis 92 pour la TGA), noté en doute.
- « refluxed at 160 °C » en milieu aqueux : valeur recopiée, doute et annotation de limite (récipient fermé ou température du bain ?). Épaisseur de mousse de nickel de 0,2 mm peu plausible : recopiée, en doute.
- Recyclage : « the catalysts », figures S13b/S14b non lisibles (légendes seules). Rattaché à 96CuFe2O4-4RGO d'après l'abstract et la conclusion.
- Figures principales : aucune lue, les valeurs comparatives sont écrites dans le texte ou dans Table S5. Rct de RGO (Fig. 7c) non écrit, non lu.
