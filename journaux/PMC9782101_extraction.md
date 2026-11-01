# Journal d'extraction PMC9782101 (CDs-berbérine, activité herbicide)

- Découpage : deux voies de base, `CDs` et `CDs-Ber`, sans branche. Un seul jeu de conditions est décrit pour chacune ; les séries (15,6–500 mg/L de berbérine, 100/200/400 mg/L en hydroponie) portent sur l'essai biologique, pas sur la fabrication, donc ce sont des résultats et non des branches.
- `CDs` gardé en `kind: material` et non `intermediate` : l'article les caractérise (TEM, XPS, IR, fluorescence) et les teste seuls (Fig. 5, tableau 2). `CDs-Ber` les reprend en réactif de rôle `intermediate` avec la concentration 100 mg/L (« The CDs solution (100 mg/L) »).
- Phrase tronquée « stored at 4 °C.100 mg/L (Scheme 1) » : le « 100 mg/L » est rattaché à la solution de CDs utilisée dans CDs-Ber, pas à l'étape de stockage (doute consigné).
- « Hydrothermal » (section 3.2) contre « stirred in three flasks … at 200 °C » (Méthodes) : lecture littérale retenue, étape `react` avec équipement « flask », pression et récipient fermé en `not_stated`. Doute consigné.
- PAA : la quantité extraite est « 90 mL » de solution à 10 %, avec le paramètre `concentration` de l'étape 2 ; pureté « BR » et fournisseur Aladdin pris dans la phrase de la section 2.1 qui nomme le PAA. Éthylènediamine : « AR » et Maclin ; le « (98%) » de la même phrase ne vise que la berbérine.
- XPS : l'ordre « C1S, N1S, O1S » associé à 532.1, 401.1, 285.1 eV est inversé par rapport aux éléments ; je n'ai pas repris cette attribution. Les teneurs 60.16/30.58/9.26 % sont attribuées à C, O, N dans l'ordre de « carbon, oxygen, and nitrogen, respectively ».
- Berbérine et témoin eau : absents des voies (échantillons à `route: null` dans l'inventaire). Leurs valeurs (CI50 du tableau 1, rangées Ber du tableau 2, barres de la Fig. 5) sont rapportées en annotations `tendance_observee`, pas en résultats d'une voie.
- Tableau 2 : seules les rangées « CDs » et « x mg/L CDs-Ber » sont en résultats ; chaque rangée est citée en entier. Le nom de propriété ne contient que ce que la rangée écrit (la légende donne l'espèce et l'hydroponie, signalé en doute).
- Figures lues (outil Read) : Fig. 5a/5b (barres racine et hauteur), Fig. 7a-c (SOD, POD, CAT), Fig. 8 (colonies). 14 valeurs lues pour CDs-Ber et CDs, précision en doute. Fig. 6 (photos), Fig. 1-4 non ouvertes sauf besoin : tout le contenu quantitatif est dans le texte.
- Contradiction texte / figure : dernière phrase de 3.6 (« only the activity of CAT in the leaves … ») contre lettres de Fig. 7a-b ; aucune valeur tirée de cette phrase, annotation `limite_reproductibilite`.
- Valeur CAT racine CDs-Ber : barre à ≈ 305 U/g, arrondie à 300 (deux chiffres significatifs au plus).
- `method_sources` : B27 (méthode publiée des CDs, `protocole_adapte`) et B28 (hydroponie, essai) ; les autres renvois sont de l'interprétation (XPS, IR, IFE, quenching).
- Aucun fichier Supporting Information dans le texte et aucun renvoi à une annexe : pas d'annotation « Annexe absente ».
