# Journal d'extraction PMC8539213

- Découpage : une seule procédure générique (3.2) pour quatre oxydes CZLEY, CZLPY, CZEYG, CZLPG ; CZLPY est la voie de base parce que c'est l'échantillon décrit et étudié en détail (Tables 2 et 3, Fig. 4 à 6), les trois autres sont des branches « un cation remplacé ».
- Filiation : CZLEY et CZLPG héritent de CZLPY (Pr→Eu, Y→Gd d'après les formules de la Table 1) ; CZEYG hérite de CZLEY (La→Gd) pour n'avoir qu'une différence de réactif. L'héritage d'étapes repose sur la phrase générique « synthesized using a modified, aqueous sol-gel citrate route » : l'article ne dit pas « same procedure » pour chaque échantillon.
- Quantités des nitrates : seul « a total amount of 1 mmol » est écrit ; les 0,2 mmol par cation découlent de la formule et sont déduits, donc non extraits (`amount_text` + doute).
- Acide citrique et eau : « 10 g in 100 mL » décrit la solution mère, pas le volume utilisé ; mis en `amount_text`, jamais en `amount` numérique.
- Température de chauffage « 120° » sans C : 120 °C retenu d'après le schéma 2, doute écrit. Durée « until the water evaporated » en `value_text`.
- Atmosphère de calcination non citée (aucun « air » dans le texte) : `not_stated`.
- Raman : Résultats (532 nm) contre Méthodes (765 nm) ; aucune valeur extraite n'en dépend, les deux sont signalées en doute et 765 nm figure dans les conditions.
- Tableau 2 : chaque rangée est attribuée par le nom d'échantillon (CZLEY…CZLPG), jamais par position ; l'ordre des acidités du texte (CZLEY < CZLPG < CZEYG < CZLPY) est cohérent avec la table.
- « respectively » du paramètre de maille et des bandes Raman : ordre relu phrase par phrase (CZLEY, CZLPY, CZEYG, CZLPG pour a ; CZLPG, CZEYG, CZLPY, CZLEY pour Raman).
- Essais catalytiques : traités en `outcomes` des voies (règle « tests du matériau fini »), pas en branches. Les variations de réaction (additif, charge en acide benzoïque, charge en aldéhyde) sont dans les résultats de CZLPY, valeurs lues sur Fig. 4A/4B/4C.
- Fig. 5 : valeurs de conversion et de rendement en dicétone lues pour CZEYG, CZLPG, CZLEY (CZLPY vient de la Table 3, 90/81, qui concorde avec la barre). Précision estimée ±2 à 5 points.
- Fig. 6B contre texte : filtration « après 16 h (60 % conversion) » (texte), 12 h (Méthodes), plateau ≈ 57 % dès 12 h (figure). Aucune lecture ne tranche, doute écrit ; la valeur du texte est retenue.
- Recyclage : texte « practically complete » contre ≈ 87 % lus au cycle 6 ; valeurs de la figure gardées.
- Annexes S1 à S10 et Fig. S1 à S4 absentes du dépôt : annotation `limite_reproductibilite` d'article ; Table S10 (oxydes simples, mélanges physiques) laissée sans voie dans l'inventaire.
- `method_sources` : B49 et B50 (sol-gel citrate) en `protocole_adapte` ; B51 (FULLPROF) et B52 (VESTA) écartées comme logiciels d'analyse, B47/B48 comme contexte ou mécanisme.
- Figures 1 à 3 non ouvertes : leurs résultats chiffrés sont dans le texte et les tableaux.
