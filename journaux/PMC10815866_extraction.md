# Journal d'extraction PMC10815866

- Découpage : voie de base NFM-Mg (phrase « The NFM-Mg was prepared using the sol–gel method… »), branche NFM (« similar approach, excluding the addition of magnesium nitrate salt »), une voie device NaCell_coin. Trois voies, une branche.
- NFM en branche et non en voie de base : la phrase des Méthodes le définit par une seule différence (pas de nitrate de Mg). « similar approach » n'est pas « same procedure », donc doute posé sur l'héritage des étapes ; les quantités des autres nitrates ne sont pas données (la formule change), seul le nitrate de Mg est inscrit en variation (`absent`).
- Aucune quantité de nitrate ni d'eau dans l'article : `amount` déclaré non cité pour les cinq réactifs ; pour l'acide citrique, seul le rapport 0,5:1 acide citrique:cations est écrit, repris en `amount_text`. Je n'ai pas déduit de masses depuis la formule visée.
- Pureté 99 % donnée pour NaNO3, Fe(NO3)3·9H2O et Mn(NO3)2·4H2O ; Mg(NO3)2·6H2O et acide citrique sans pureté. « All chemicals… purchased from Junsei » nomme chaque réactif : fournisseur retenu pour les cinq. L'eau distillée n'est pas citée dans cette phrase : fournisseur et pureté non cités.
- Étape de gélification à 80 °C : « for a certain period » ne donne aucune durée, donc `duration` déclaré non cité (pas de value_text). L'agitation magnétique est portée par la même étape (une seule action `heat`).
- Chauffage à 200 °C (auto-combustion) : pas de durée, d'atmosphère ni de four ; déclarés non cités. « overnight » à 120 °C en vacuum oven : `value_text`.
- Trempe et stockage : deux étapes (quench, store) tirées de la même phrase, car la trempe et la conservation en boîte à gants sont deux actions ; vitesse de refroidissement non citée.
- Table 2 (ICP-OES) : en-tête fusionné ; chiffres attribués dans l'ordre Na, Mg, Fe, Mn de la ligne d'en-tête, cohérent avec la formule du tableau.
- « respectively » du débit : 158, 137, 117, 68 mAh g−1 attribués à 40, 100, 200, 600 mA g−1 dans cet ordre (phrase de la section 2.2) ; recoupé avec la Fig. 4d (NFM-Mg ≈ 158, 137, 117, 68).
- Valeurs lues sur figure (Fig. 4c, 4d) : cinq capacités en débit du NFM et la capacité à 40 cycles, citées avec la légende de la Fig. 4. Précision de lecture ± 5 à 10 mAh g−1, 2 chiffres significatifs, signalée en doute. Les valeurs du NFM-Mg sont dans le texte et n'ont pas été relues sur le graphique. Les autres figures (1, 3) ne portent pas de résultats chiffrés absents du texte.
- Fig. S2 et Table S1 : l'article les cite mais aucune section Supporting Information n'est dans le fichier ; annotation « Annexe absente du dépôt ». Les capacités du NFM de la Fig. S2a sont données dans le texte et extraites de là.
- Libellé XPS « Mg 2p » (texte) contre « Mg 1s » (légende Fig. 2), 1303,75 eV : valeur gardée telle quelle, doute noté.
- « 20 mAh g−1 » (résumé et section 2.2) pour une densité de courant : erreur d'unité de l'article, unités mA g−1 utilisées dans les noms de propriété ; doute noté.
- Voie device : une seule pour les deux cathodes (« at the same condition »), car la seule phrase de montage ne distingue pas les deux ; électrode, séparateur, collecteur non cités. Les résultats de capacité restent sur les voies matériau.
- Échantillons sans voie : états d'électrodes cyclées (XAS ex situ, DRX in situ), qui ne sont pas des synthèses.
- `method_sources` vide : les Méthodes ne contiennent aucun renvoi [[id]] dans corpus/refs ; la sol–gel n'est citée qu'en introduction (contexte).
