# Journal d'extraction PMC9043841 (ré-extraction à l'aveugle)

- Voie de base : Ni2Fe1-LDH. La procédure « typique » ne nomme aucun rapport Ni/Fe ; Ni2Fe1 est l'échantillon vedette (263 mV, 349,1 mA cm−2), donc pris comme base. Les quantités de NiCl2 et FeCl3 sont déclarées non citées (seul le total de 1 mmol est écrit), je n'ai pas calculé 0,667/0,333 mmol.
- Ni9Fe1, Ni4Fe1, Ni1Fe1 : branches de Ni2Fe1, avec deux variations (une par chlorure) sur la phrase « Ni/Fe atomic ratio = x/y » ; pas de variation chiffrée en mmol car l'article n'en donne pas.
- Séries CoFe et NiCo (8 échantillons) : branches de Ni2Fe1 (« similar to » la procédure NiFe, sauf les chlorures), rapports tirés de la légende Fig. S4 du SI. Héritage des étapes accepté malgré « similar » ; signalé en doute. Aucun résultat par échantillon (Fig. S7 non lisible, SI sans images) : seule une annotation de groupe.
- Essai à grande échelle (Fig. S5) : branche Ni2Fe1-LDH_scaleup, variation sur le réactif « water » (volume du récipient augmenté, valeur absente), résultat « gram level » en value_text.
- Électrode (encre catalyseur + Nafion sur GC) : voie `device` séparée ; les résultats OER restent sur les voies matériau (tests du matériau fini). L'encre est décrite pour « catalysts » en général, rattachée à Ni2Fe1 par commodité (doute).
- Pureté et fournisseur : la phrase « All reagents ... Sinopharm » est prise pour les réactifs des synthèses (NiCl2, FeCl3, persulfate, ammoniaque, CoCl2) ; refusée pour l'eau (non nommée comme achetée), Nafion pris chez Sigma-Aldrich selon sa propre phrase.
- Fig. 3A : pentes Ipa–ν1/2 lues sur les équations imprimées (valeurs exactes, from_figure). Fig. 3B : courants à 1,8 V de Ni9Fe1, Ni4Fe1, Ni1Fe1 lus à 2 chiffres significatifs (160, 220, 90) ; la courbe de Ni2Fe1 monte vers ~370 contre 349,1 dans le texte : texte retenu. Fig. 3C (histogramme 3D, axe « mV » 0–0,60) illisible : non extrait.
- Contradictions notées sans correction : texte sur les « plus grandes ECSA de Ni1Fe1 et Ni4Fe1 » contre les Cdl ; Fig. 4E Ni4Fe1 (texte) contre Ni2Fe1 (légende).
- Tableau S1 (ICP en g/kg) : non utilisé, les rangées sont éclatées sur plusieurs lignes ; les rapports atomiques sont repris de la phrase du texte principal.
- Énergies DFT : valeurs du texte (−2,71 …, 4,66 …) plutôt que celles, plus précises, des Tables S2/S3 ; mêmes valeurs à l'arrondi.
- method_sources vide : les renvois [[cit]] portent sur le contexte, les paramètres DFT et l'interprétation FTIR, pas sur une préparation.
- Hors périmètre : catalyseurs de la littérature et IrO2 commercial de la Table S4, échantillon après test de stabilité (route null).
