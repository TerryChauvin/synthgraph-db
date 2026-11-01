# Journal d'extraction PMC12917697

- Découpage : 15 voies matériau, une par échantillon (1A à 5C, Table 1), car chaque répétition a ses propres rendements (Table S2 du SI) et ses propres diffractogrammes (Fig. 1) ; le texte insiste sur la reproductibilité, donc A, B, C ne sont pas fusionnés.
- Voie de base : 1A (premier échantillon de Table 1, tout à 25 °C). Les échantillons A des jeux 2 à 5 sont des branches de 1A ; B et C sont des branches de A de leur jeu, seule variation « replicate » (paramètre inventé faute de différence de protocole, d'où 10 avertissements volontaires du contrôle, expliqués dans `doubts`).
- Table 1 : colonne « Stirring » rattachée à l'étape 2 (agitation, 400 rpm) et colonne « Incubation » à l'étape 4 (diffusion de vapeur de MeOH). Le texte ne dit pas si l'agitation continue pendant l'incubation : doute noté, `stirring_speed` déclaré non cité à l'étape 4.
- Rendements : Methods renvoie à « Table S1 » mais le SI donne les rendements dans Table S2 (Table S1 = benchmark DFT). Valeurs prises dans Table S2 par ordre de colonne (« 1A, 1B, 1C » puis « 68, 84, 76 »), citation sur deux lignes.
- Rendement moyen du jeu 4 : texte « 83 % », Table S2 84, 81, 80 (moyenne 81,7 %). Le 83 % n'est pas repris comme donnée (annotation tendance_observee et doute).
- `succeeded` : faux pour 1A, 1B, 1C (aucune phase γ-CD-MOF) ; vrai pour 2C, 3A, 4A, 4B, 4C, 5A, 5B ; vide pour 2A, 2B (« suboptimal »), 3B, 3C (seulement « only 3A »), 5C (déviations) car le texte ne tranche pas.
- 4A : DRX élargi (petits cristallites) mais MEB cubique et pics alignés ; marqué réussi, avec les deux observations en résultats.
- Étapes de lavage et trempage : une seule phrase donne 30 mL de MeOH et « left undisturbed ... 7 days » ; deux étapes (wash, age) avec la même citation, `repetitions` et température du trempage non citées.
- Séchage : « sequential vacuum drying ... 25 °C for 10 h and 45 °C for 12 h » → deux étapes dry successives, pression non citée.
- Pureté de l'eau : « 18.2 Ω resistivity » copiée telle quelle comme pureté ; fournisseur non cité (Isolab est le fabricant du système de purification, pas un fournisseur d'eau).
- Chargement de la curcumine : voie `post_treatment` de base Cur_1mgmL (1 mg/mL), branches 2, 3, 4, 5 mg/mL par la variation du réactif « curcumin » ; taux de chargement tirés du texte (1, 2, 3, 5 mg/mL) et de la barre de la Fig. 8b pour 4 mg/mL (≈ 23 %, `from_figure`, une seule valeur lue sur figure).
- Série basse concentration (0,001–0,016 mg/mL) : branche Cur_low, hérite du protocole 50 mg / 10 mL / 24 h sans que l'article le dise (doute). Paramètres de Langmuir (Table 3) rangés par échantillon 5A, 5B, 5C comme résultats des voies matériau, rangée entière en citation ; il y a deux rangées « 5A » (basse et haute concentration), distinguées par leurs valeurs.
- Échantillon du chargement 1–5 mg/mL : non nommé dans les Méthodes, donc réactif « γ-CD-MOF-5 samples (routes 5A, 5B, 5C) » et doute ; XRD/FT-IR de Cur-5A-4 et Cur-5A-5 et ATG de 5C chargé rangés dans Cur_4mgmL et Cur_5mgmL.
- γ-CD chargée en curcumine (7,05 %) : aucun protocole ni concentration ; laissée sans voie et reprise dans une annotation plutôt qu'en branche (éviter un héritage non fondé).
- BET 430,8 m2/g : échantillon non nommé, non rattaché à une voie (annotation limite_reproductibilite).
- DFT et CBMC : calculs, pas des synthèses, non extraits ; ΔG(T) résumé en annotation tendance_observee.
- method_sources : aucun marqueur [[id]] dans le corps de corpus/refs ; ref2 (Smaldone et al. 2010) retenu car l'auteur est nommé dans la phrase « adapted from Smaldone et al. ».
- Annexe absente : MPIF (ZIP) des 15 échantillons.
