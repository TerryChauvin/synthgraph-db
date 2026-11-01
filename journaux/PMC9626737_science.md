# PMC9626737 — critique scientifique (journal de décisions)

- Gravure : 1,6 g LiF / 20 mL HCl 9 M / 1 g Ti3AlC2 / 24 h à 40 °C est exactement la recette EN-MILD (Shayesteh Zeraati 2021, Nanoscale, recette lue dans l'annexe RSC) : bilan jugé `ok`. LiF 61,7 mmol < HCl 180 mmol, donc LiF limitant comme l'exige Alhabeb 2017.
- Gravure incomplète malgré cette recette : jugée `reserve` (cause probable : la poudre MAX commerciale), pas `probleme` : les auteurs le disent eux-mêmes.
- `probleme` (MXene_NMP_5h_30C) : film de MXene à 5,54 MΩ contre 3,0 kΩ pour le graphène. Les films Ti3C2Tx MILD font ≈ 5,8 × 10^3 S/cm (Shayesteh Zeraati 2021, abstract RSC) : l'ordre est inversé. Retenu comme incohérence de résultat et de conclusion, pas comme erreur de recopie.
- `probleme` (MXene_NMP_5h_30C) : doublet XPS 458,9/464,7 eV appelé Ti3+. Näslund 2020 (JPCC, tableau dans l'extrait) donne TiO2 à 459,0/464,8 eV : coïncidence exacte, donc oxydation en TiO2. Halim 2016 cité en appui du mécanisme (non lu au-delà de la notice ORNL).
- `probleme` (GrMX_10vol) : synergie comparée à volume égal de suspensions de concentrations 0,78 / 0,18 / 0,24 mg/mL, donc 3,9 / 0,9 / 1,2 µg déposés (5 µL). Témoin qui change la masse en plus de la composition (contrôle n° 5).
- `probleme` (GCE_GrMX_sensor) : EIS dans « 0,1 M chlorpromazine » = 35,5 g/L de chlorhydrate, contre 10 mg/mL en PBS pH 7,2 (fiche Cayman) et base libre à 2,55 mg/L (PubChem). Le pKa 9,3 utilisé pour la fraction neutre est une valeur de mémoire, signalée comme telle dans `calculs`.
- Graphène 26,0° → 3,43 Å, au-dessus de 3,354 Å du graphite : `reserve`, car un décalage d'échantillon peut l'expliquer ; « haut degré de graphitisation » non démontré.
- Concentration de graphène 0,18 mg/mL en 5 h : jugée plausible entre Hernandez 2008 (0,01 mg/mL) et Khan 2010 (1,2 mg/mL après 460 h), avec 20 mg/mL de départ. Pas de `probleme`.
- Masse de graphène requise (10 mg pour l'adsorption + 3 mg pour le film) = 2,9 lots de 25 mL : noté dans `calculs`, sans constat, car rien n'interdit de faire plusieurs lots.
- Branche MXene_DMSO jugée seule pour toute la série de solvants : Maleski 2017 trouve DMF, NMP, DMSO et éthanol bons pour Ti3C2Tx délaminé. L'écart est attribué à la poudre séchée de départ ; `reserve`.
- Les branches de composition ne sont pas jugées séparément : leurs fractions se recalculent exactement (bloc `calculs` de GrMX_10vol).
- Fiche ECHA (NMP Repr. 1B, H360D) : document CLH de l'ECHA retenu tel que l'extrait l'affiche ; ce n'est pas la page « substance info ».
- Mécanisme d'électro-oxydation de la chlorpromazine et de la RhB : proposé de mémoire, sans source (`sources` vide, noté dans `sources_not_found`).
- 7 appels web (6 recherches, 1 lecture de la page RSC pour confirmer les auteurs de Nanoscale 2021). Les DOI hors `fondateurs.md` ne sont pas vérifiés sur Crossref (bloqué ici) : 10.1039/D0NR06671K (vu sur la page RSC), 10.1021/acs.jpcc.0c07413, 10.1016/j.apsusc.2015.11.089, 10.1021/acs.chemmater.6b04830, 10.1038/nnano.2008.215, 10.1002/smll.200902066.
