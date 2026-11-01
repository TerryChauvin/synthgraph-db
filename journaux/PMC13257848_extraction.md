# Journal d'extraction PMC13257848 (ZIF-8@TPPa)

- Une seule voie de base `ZIF-8@TPPa` : l'article ne décrit qu'une synthèse (3.2.2) et ne varie aucune condition de synthèse. Tous les essais d'adsorption (pH, dose, temps, cinétique, isothermes, thermodynamique, ions, eaux réelles, recyclage) sont des tests du matériau fini, donc des `outcomes` et des `characterizations`, pas des branches.
- ZIF-8 : synthèse renvoyée à « Text S1 » (absente de `corpus/text`). Pas de voie `intermediate` (aucune étape citable) ; ZIF-8 est un réactif de rôle `intermediate` de la voie (6 mg, citation de 3.2.2). Dans `sample_inventory` : `route: null`.
- Zn(NO3)2·6H2O, 2-méthylimidazole et DMF (section Matériaux) ne sont pas extraits : l'article ne dit pas pour quelle synthèse ils servent, ils relèvent vraisemblablement de Text S1. Consigné en doute.
- PA (97 %, McLean) et TP (97 %, Aladdin) : pureté et fournisseur lus dans les deux phrases de 3.1 qui les nomment (PA, TP, PbCl2 >99 %). PbCl2 est enregistré comme solution saturée de 50 μL, rôle `catalyst` (l'article écrit « used as a catalyst »).
- Méthanol : la phrase de 3.1 nomme « methanol of HPLC grade ... Merck ». Lecture littérale retenue (pureté et fournisseur), mais le doute est ouvert car cela vise peut-être le LC-MS/MS.
- Étape « shaken for 10 s » : action `mix` avec durée 10 s ; l'ajout de TP puis sa sonication de 10 min sont deux étapes (add, sonicate) tirées de la même phrase. La première sonication n'a pas de durée : déclarée dans `not_stated`.
- « desiccated at 60 °C for 24 h » lu comme un séchage (action `dry`), atmosphère non citée.
- Table 1 : une rangée = un herbicide ; chaque rangée recopiée en citation et attribuée par le nom (butachlor, anilofos, pendimethalin). K2 écrit « 4.13 × 10−4 » : `value_text` car le nombre n'apparaît pas tel quel. Les ± ne sont pas séparés de la valeur.
- Contradiction texte / Figure 3 : le texte attribue des plages au butachlor qui, sur la figure, sont sur la courbe rouge de l'anilofos (pH et temps ; départs de la dose permutés). Texte retenu tel quel (attribution dans l'ordre de la phrase), doute ouvert. Aucune valeur de figure n'est enregistrée : tous les chiffres sont déjà dans le texte.
- Légende de la Fig. 3 (b temps, c dose) contre texte (dose en 3b, temps en 3c) : la figure suit la légende ; les valeurs viennent du texte, qui les nomme.
- Capacités du résumé (232,56 ; 188,68 ; 285,71 mg/g) : modèle non dit, Table S3 absente, qe expérimentaux de la Fig. 4 plus bas (≈165–200). Enregistrées comme dans le résumé et la conclusion, doute ouvert. R2 d'isothermes : ordre des herbicides non écrit, valeurs enregistrées en bloc.
- Fig. 1a : étiquettes TP et Pa inversées par rapport au texte ; texte retenu.
- `method_sources` vide : aucun renvoi `[[id]]` ne porte sur la méthode de préparation ; les renvois sont de contexte, d'attribution de pics ou d'interprétation. La synthèse de ZIF-8 n'a pas de renvoi bibliographique.
- Annexes absentes (Text S1, S3, Tables S1–S4, Figures S1–S7, équations S1–S6) : annotation `limite_reproductibilite` d'article ; aucune valeur reconstituée.
- Échantillons sans voie dans l'inventaire : ZIF-8, TPPa seul (comparateur non décrit), matériau après adsorption et après cinq cycles (états d'usage).
