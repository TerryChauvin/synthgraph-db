# Journal de correction PMC7181732

- Raman (constats 1 et 2) : ajout, pour rGO-Br et rGO-Am, de G 1580, D 1345, 2D 2685, D+D' 2935, 2D' 3202 cm−1 en `outcomes`. Les trois bandes du second ordre ont pour citation la phrase « Both rGO-Am and rGO-Br also present three second order bands… ». La bande D (1345) n'est donnée par l'article que pour les matériaux graphéniques en général : rattachée aux deux échantillons avec un doute.
- rGO-Br : ajout d'une caractérisation Raman (mêmes conditions que GO) et d'une caractérisation TEM/SAED (phrase « After the bromination procedure rGO-Br continues to exhibit lamellar defect-free structure… »). Conditions TEM recopiées de celles du GO (méthodes communes).
- Photoémission (constat 3) : une caractérisation « Valence band / secondary electron cut-off » ajoutée à GO, rGO-HT et rGO-Am (BESSY-II, hν = 130 eV, ultravide) ; résultats propres à chaque échantillon. Pour rGO-Am : N à ≈ 5,0 et ≈ 7,3 eV, pic large 18–20 eV (value_text « between 18 and 20 eV »). Ajout aussi des pics ≈ 5,5 eV (GO) et ≈ 3,2 eV (rGO-HT), cités par le critique.
- Taille latérale « up to 100 µm » du GO (constat 4) : pas de second résultat `lateral_size` ; la contradiction est déjà dans l'annotation `limite_reproductibilite` du GO (décision de l'orchestrateur : annotation, valeurs gardées).
- XAS (constat 5) : non listé dans les décisions mais soutenu par le texte ; ajouté en résultat de rGO-Am (« absence of angular dependence of π*-resonances »), sans la conclusion « isotrope » déduite.
- Répétitions « three times » / « 5 times » / « 3 times » (constat 7) : pas de modification des étapes (portée non établie par l'article) ; un doute ajouté, qui complète celui existant.
- « one hour » de rGO-Am-Benz étape 5 (constat 8) : rejeté, `value_num` = 1 ne figure pas dans la citation (le contrôle exige le nombre tel quel) et l'unité ne doit pas être déduite.
- Chauffage 150 °C de rGO-Am-Benz (constat 9) : seule la description de l'étape 7 est précisée (« up to », partie Résultats, ordre non établi).
- Exposants perdus (constat 10) : `value_text` laissés tels quels ; le doute existant précise que ×10^n est confirmé par l'épaisseur implicite ≈ 1,7 µm (1,2 µm pour rGO-Br) ; annotation article-niveau `limite_reproductibilite`.
- ID/IG figure 3b contre texte (constat 11) : texte retenu, annotation et doute.
- `mecanisme_analyse` rGO-Am (constats 12 et décision 8) : retrait de « (hypothèse des auteurs) » sur les imines ; réécriture avec le mélange SN1 / élimination de HBr / ouverture des époxydes par NH3 et amination réductrice, présenté comme hypothèse de l'analyse ; `mecanisme_auteurs` non touché.
- SEM (constat 13) : solvant de dépôt varié inscrit dans les conditions de la caractérisation SEM de rGO-Am ; pas de branche (aucun protocole).
- Sécurité : annotation `securite_analyse` du dioxane de l'aérogel (inflammable, peroxydes, cancérogène suspecté, lyophilisation).
- Critique scientifique : les deux `probleme` (test CuCl/HCl ; triéthanolamine) sont des `limite_reproductibilite` sans toucher aux valeurs. Les réserves concises (74 % non retrouvé, « C/O » non atomique, somme C1s ≈ 0,98, SN2 impossible, N1s pyrrolique, électro-attracteur/donneur, 0,197 nm, atmosphère du recuit, bande interdite, épaisseur des films) sont réparties par voie. Pour le chiffre « ≈ 94 % avec correction de dilution », je reprends celui de la critique sans l'avoir recalculé.
- La somme des composantes C1s de rGO-Am est écrite « ≈ 0,98 » (mon calcul donne 0,981 avec <0,001 pour les défauts) au lieu de 0,982.
- Aucune voie retirée ni renommée.
