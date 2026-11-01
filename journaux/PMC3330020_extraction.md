# Journal d'extraction PMC3330020

- Découpage : une seule voie de base (SGAc, acide acétique) décrite en entier ; SGEg, SGOc, SGEn en branches où seul l'agent complexant change (variation sur le réactif « acetic acid », valeur « replaced by … », nouveau réactif ajouté à la branche). Raison : un seul protocole est écrit dans Experiment pour les quatre noms d'échantillons.
- Héritage des étapes accepté pour les trois branches : l'article ne dit pas « same procedure » mais écrit « sintering at the same temperature » et un seul protocole ; aucune autre différence n'est donnée (doute consigné).
- Étape 2 (ascorbique, 1 h, 55 °C) : « ascorbic acid was added ... after continuous stirring for 1 h at 55°C » est ambigu sur l'ordre ; lecture littérale retenue (1 h et 55 °C sur l'étape d'ajout), doute écrit.
- Agitation à 75 °C (étape 4) et évaporation (étape 5) séparées : la température d'évaporation et les durées ne sont pas données, donc `not_stated`.
- Aucune quantité de réactif donnée (« stoichiometrically », « saturated solution ») : `amount` en `not_stated` pour tous les réactifs, sans rien déduire de la formule LiFePO4.
- Pureté « A.R » et fournisseur Shanghai Chemical Reagents Co. Ltd. retenus pour LiNO3, Fe(NO3)3·9H2O et NH4H2PO4 (phrase qui les nomme explicitement) ; non étendus à l'acide ascorbique, l'ammoniaque ni aux agents complexants, que la phrase ne nomme pas.
- Noms SCAc, SCOc, SCEg, SCEn dans les Résultats lus comme SGAc, SGOc, SGEg, SGEn (fautes de frappe probables) ; citations laissées telles qu'écrites.
- Tableau 1 : chaque rangée est une citation entière rangée par le nom de l'agent (Acetic acid → SGAc, etc.), jamais par position. Constante de stabilité logβ mise en outcome de chaque voie (propriété de l'agent avec Fe2+, pas du matériau), faute de meilleur emplacement.
- Contradictions : résumé « 200 nm » contre Résultats « 100 nm to 1 μm » pour SGAc ; résumé « < 6.8 wt.% » carbone contre ≤ 5,1 dans le tableau. Valeurs des Résultats et du tableau retenues, doutes écrits.
- Figure 5 ouverte : capacités à 30 cycles de SGOc, SGEg, SGEn lues (≈ 134, 112, 117), arrondies à 2 chiffres significatifs (130, 110, 120), marquées `from_figure: Fig. 5` avec la légende en citation. Les capacités à 1er cycle lues sur la figure concordent avec le tableau 1 (non répétées). Figures 1 à 4 non numérisées (DRX, MEB, CV, profils de charge) : pas de valeur chiffrée demandée par l'article.
- Plateaux 3,49 V / 3,37 V valables pour tous les échantillons : une annotation `tendance_observee` unique, pas de valeurs recopiées par voie.
- Électrode et cellule : deux voies `device` indépendantes (Electrode_LiFePO4C, Cell_LiFePO4C) car décrites dans un paragraphe à part ; conditions du CV et du cyclage rangées en caractérisations de la cellule. Séparateur Celgard 2400 : fournisseur renseigné avec sa phrase.
- Aucun renvoi bibliographique de méthode dans Experiment (références B1 à B11 de contexte uniquement) : `method_sources` vide. Aucun SI ni renvoi à une annexe.
