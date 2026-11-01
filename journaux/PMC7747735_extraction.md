# Journal d'extraction PMC7747735

- Découpage : deux familles de voies de base. Le support spinelle (voie `800MA`, `kind: intermediate`) est la base des quatre supports ; la série en température de calcination (600/700/800/900 °C) donne trois branches, la valeur 800 étant choisie comme base car c'est le support du catalyseur optimal. Le catalyseur `15Co/800MA` est une seconde base (imprégnation + calcination à 600 °C) qui prend le support 800MA en réactif `intermediate`.
- Branches de catalyseurs : 15Co/600MA, 15Co/700MA, 15Co/900MA remplacent le réactif support (variation sur le nom du réactif) ; 10Co/800MA et 20Co/800MA changent la teneur en cobalt (variation `cobalt nitrate`, 10 et 20 wt% citées dans la phrase « x = 10, 15, and 20 »). La masse de nitrate n'est pas donnée : `amount_text` porte seulement la teneur visée.
- CA et CM : branches de 15Co/800MA (« wet-impregnation method under similar conditions »). Héritage de l'étape de calcination accepté mais mis en doute, car la phrase est vague ; supports γ-Al2O3 et MgO déclarés réactifs « précurseur » sans quantité ni fournisseur.
- Précurseurs de Mg et d'Al : introuvables dans Experimental, donc non cités ; la voie 800MA n'a que NH4OH et l'eau de lavage en réactifs.
- Tables 1, 2, 3 : chaque rangée recopiée en citation entière et attribuée par le nom d'échantillon. Table 2 ne contient pas 600MA, 700MA, 900MA, 15Co/600MA, d'où l'absence d'acidité pour ces voies. Tirets « – » ignorés (pas de valeur).
- Rangée « 15Co/800MA (spent) » (Table 1, ligne 11) : rangée en résultats de 15Co/800MA avec le préfixe `spent_catalyst_`, pas une voie.
- Régénération (Fig. 8 et phrase « activated in the airflow ») : deux voies `post_treatment`, la seconde en branche de la première. Température d'activation non citée. Contradiction : texte « no observable change » contre Fig. 8 plus basse que Fig. 7b ; valeurs de la figure gardées, doute écrit.
- Figures lues : Fig. 6a (N2 à 600 et 650 °C), Fig. 6b (CO2 à 650 °C) pour les cinq catalyseurs Co/MA ; Fig. 8 (1 h et 20 h, sélectivité) pour les deux régénérés. Les valeurs à 600 °C sous CO2 ne sont pas reprises de la Fig. 6b car elles contredisent la Table 3 (15Co/900MA et 10Co/800MA inversés, 20Co/800MA à 70 contre 74) : Table 3 retenue, doute écrit.
- Fig. 7 : valeurs du texte (60→37 sous N2 ; 82→59 et 58→37 sous CO2), pas relues sur la figure sauf pour détecter l'écart de 2 points sur 15Co/900MA (doute).
- Valeur TGA « 10% and 11.5% » : attribuée dans l'ordre de la phrase (800MA puis 700MA).
- Annexe : la section Supporting Information du texte ne contient que les légendes S1–S8 ; annotation « Annexe absente du dépôt » écrite. Numérotation S du texte et de l'annexe différente (doute).
- 600MA marquée `succeeded: false` (phase impure) sans que les auteurs parlent d'échec.
- Aucune `method_sources` : les renvois [[CR…]] portent sur le contexte ou les comparaisons de la littérature, pas sur un protocole à refaire.
