# Journal d'extraction PMC8184743

- Découpage : une voie de base « ZnO » (0 mol.%) et six branches (1, 3, 5 mol.% Ni ; 1, 3, 5 mol.% Ag), toutes comparées au ZnO pur. Une seule grandeur varie (teneur en dopant), ce qui justifie des branches et non des voies indépendantes. Inventaire : 7 échantillons, tous avec voie.
- Voie de base = ZnO pur : les quantités (9,9163 g de nitrate de zinc, 6,4041 g d'acide citrique, 80 mL d'eau) viennent de « Preparation of ZnO nanopowder » ; les étapes (agitation à 42 °C, repos 24 h, 72 °C 48 h, 92 °C jusqu'au gel, séchage, broyage, calcination) sont écrites dans la section Ni/Ag. Je les ai appliquées au ZnO pur car la phrase sur les rapports molaires (0, 1, 3 et 5 mol.%) inclut 0 mol.% ; l'article ne le dit pas explicitement (doute).
- Étapes combinées « stirred for another 1.5 h and heated at 72 °C for 48 h » et « stirred for 1 h and heated at 92 °C until gels were obtained » : coupées en une étape d'agitation puis une étape de chauffage. Durée du chauffage à 92 °C = value_text « until gels were obtained ».
- « kept at room temperature for 24 h » : étape age, température en value_text « room temperature ».
- Calcination : atmosphère, vitesse de chauffe et refroidissement non cités (cherchés dans tout le texte, pas d'annexe) → not_stated.
- Dopants : la teneur n'est donnée qu'en mol.% ; amount_text « N mol.% » sans base ni masse. Variation `dopant` avec parent_value « none », valeur numérique 1/3/5 mol.% (la citation est la phrase « (0, 1, 3 and 5 mol.%) »). Nickel : Fluka 98 % (phrase de la section Ni) ; AgNO3 : pureté et fournisseur non cités.
- Acide citrique rangé en rôle `ligand` (choix de rôle ; l'article ne précise pas sa fonction).
- Tableau 3 : une rangée = un échantillon, attribuée par le nom écrit dans la rangée (« 3 mol.% Ag-ZnO | 22.21 | … »). Pour le ZnO pur, a, c et c/a viennent de la phrase du texte (identiques au tableau).
- Contradiction : bande interdite de 1 mol.% Ag = 2.8 eV (texte, figure 9) contre 2.90 eV (tableau 3, insert de la figure 8). Tableau 3 retenu (section la plus détaillée), le texte est cité dans le doute. Figures 8 et 9 ouvertes seulement pour ce contrôle : aucune valeur lue sur figure n'est enregistrée.
- Bandes interdites de 2,00 et 1,80 eV pour 3 et 5 mol.% Ag, incompatibles avec les seuils d'absorption à 387 et 390 nm : extraites telles quelles, annotées en limite de reproductibilité.
- Tableau 1 : « Ni2O3ZnO » attribué à deux raies, contre le texte (« no other crystalline phase ») ; en-tête brouillé. Texte retenu, tableau non extrait (doute).
- Tableaux 1 et 2 (D par pic) non extraits : en-tête illisible, moyennes par échantillon dans le tableau 3.
- Résultats qualitatifs d'absorption et de transmission (texte) rangés en outcomes de l'échantillon cité (1 mol.% Ni, 5 mol.% Ni, 1/3/5 mol.% Ag) ; tendances de groupe en annotation `tendance_observee`.
- Références : aucune source de méthode (les renvois portent sur le contexte, les équations de Scherrer/Tauc et la comparaison de résultats) → method_sources vide. Pas d'annexe : aucune section Supporting Information, aucun renvoi à une annexe.
