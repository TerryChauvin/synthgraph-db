# Journal — test de complétude PMC10131834

- Extraction d'origine déjà dense (310 citations, 18 voies) : la liste A ne contenait que 8 nombres, dont 2 bornes redondantes avec le tableau S1 (73,5 et 16,5, `deja_present`) et 2 pourcentages de titres de références (`hors_sujet`).
- 1282 cm−1 : la phrase vaut pour la série « de BCDs à YCDs » ; ajouté à ces trois voies seulement (le texte dit « faibles » pour les RCDs, sans position).
- Bande UVC (200−280 nm) : « all of the CDs » ; ajoutée en `value_text` sur les quatre fractions avec la mention « donné pour les quatre ensemble », comme le font déjà les bandes XPS.
- Calculs DFT : voie `kind: calcul` sans parent ni réactif ; les paramètres de calcul sont les paramètres des étapes (noms snake_case en minuscules exigés par le contrôle). Les valeurs calculées figurent déjà dans les voies mesurées : non retirées (règle d'ajout seul), signalé dans un doute. Les groupes de surface du modèle RCDs ne sont pas décrits dans le texte.
- Citation du modèle GCDs coupée avant « 2 » (numéro de page inséré par l'aplatissement du PDF dans le texte).
- Tableau S6 : une entrée par valeur (CRI, CCT, CIE), citation = la rangée aplatie du tableau, `route` = `WLED_WCDs`, source de pompe et numéro de référence du SI en `conditions`. Pas de `ref_id` : les références du SI ne sont pas dans `corpus/refs`. Ligne PVA + éthylènediamine ignorée (aucune valeur de performance).
- Fig. S1 : les valeurs de CIE/PL ne sont que des courbes ; seule la concentration (0,375 mg mL-1) est ajoutée, en condition d'une entrée `characterizations` des six branches (`from_figure` Fig. S1, citation = la légende).
- Rapport massique 3:5:2:3 : ajouté en variation de `WLED_remixed` (avertissement attendu : le parent n'a pas ce paramètre, `parent_value` « none »).
- Décalage de Stokes « > 200 nm » : non ajouté, la phrase ne dit pas entre quelles longueurs d'onde (1 émission de donneur ou excitation à 400 nm) ; la TCSPC de la TRPL est dans un doute, la condition existante n'étant pas modifiable.
- `not_stated` : `repetitions` (voie WCDs) et `addition_order` (étape 1), après recherche de « batch », « repeat », « order » dans le texte.
- Conditions de mesure absentes (TEM, XRD, Raman, FTIR, XPS, UV–vis, PL, électroluminescence) : dans `doubts`, pas dans `not_stated`.
- Comparaison avant/après par script : aucune clé ni valeur existante perdue ou modifiée.
