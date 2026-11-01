# PMC9078281 — critique scientifique (journal de décisions)

- Concentration de Mn : 1 mL × 0,1 M dans 12 + 1 + 37 = 50 mL donne 2,0 × 10−3 M. Le protocole standard est donc bien l'optimum de la Fig. 5d, ce que le doute de l'extracteur laissait ouvert.
- Classé `probleme`, la concentration 6,52 mg/mL : l'ESI la mesure en lyophilisant le surnageant avant dialyse. Les solutés introduits font 367 à 410 mg dans 50 mL (7,3 à 8,2 mg/mL), on retrouve donc 79 à 89 % de la masse, surtout du citrate de sodium. Les doses du MTT, de l'imagerie et du test Hg2+ ne sont pas des doses de points quantiques.
- Classé `probleme`, la DRX : d = 9,60 et 2,84 Å, rapport 3,38, ce qui rend l'indexation (001)/(002) impossible. 2,84 Å n'est ni graphite (3,36 Å) ni g-C3N4 (3,26 Å, Fina 2015). Je propose un sel (NaCl (200) à 31,7°, carbonate ou citrate de sodium) comme hypothèse, pas comme constat : la figure S2 n'est pas lisible ici.
- Classé `probleme`, le Raman : 1411 et 1645 cm−1 ne sont pas D et G (Ferrari & Robertson). Ces positions correspondent aux bandes carboxylate et amide, comme le couple IR 1580/1407. Les ID/IG en base ne sont donc pas des rapports D/G.
- Classé `probleme`, le zêta en « eV » : l'axe de la Fig. S9 est en mV. Un correctif d'unité ou une annotation est à prévoir côté extraction.
- Classé `probleme`, le test Hg2+ : 200 µL de « 0–5 µM » dilués à 5 mL (facteur 25) contre 0–5 µM dans la cuve sur la Fig. 6b. J'ajoute l'équation F0/F décroissante (c'est F/F0) et le σ de 0,13 % pris sur le « lowest signal ».
- Fluorophore moléculaire contre GQD : laissé en `reserve`, pas en `probleme`. La convergence est forte (bleu indépendant de l'excitation, mono-exponentiel, poudre blanche, bandes moléculaires), mais il n'y a pas de mesure directe (dialysat, spectre de masse). Sources : Essner 2018, Song 2015 (IPCA), Fang 2017 (glycine + acide citrique : dérivés pyridiniques).
- Mécanisme retenu, préféré à l'« effet de confinement » des auteurs : Mn2+ en acide de Lewis chélaté par le citrate favorise l'amidation et la cyclisation. Appui : N de surface 2,2 → 4,24 %. C'est une hypothèse, je l'écris comme telle.
- Quinine : la valeur 0,546 vaut pour H2SO4 0,5 M. L'IUPAC (Brouwer 2011) ne tabule pas 0,1 M ; dans 0,05 M les valeurs vont de 0,52 à 0,60. Laissé en `reserve` (5 à 10 % relatifs).
- Le pic isolé à 2 mM (42 % entre deux points à ≈ 30 %), sans répétition, est laissé en `reserve` : impossible de trancher sans les données brutes.
- Témoin acide citrique : il change le pH (≈ 8 → ≈ 3) et retire 3,6 mmol de Na+. C'est le contrôle 5, laissé en `reserve`.
- Série M-NG : un ion résiduel extincteur (Cu2+, Fe3+, Pb2+…) suffit à expliquer les rendements bas, sans effet de formation. Ag+ est presque sûrement réduit en Ag0 par le citrate à 180 °C. Jugé sur M-NG_Ag+ et M-NG_Fe3+ seulement ; le constat s'étend à la série.
- Sodium absent du Tableau S1 (somme = 100 %) alors que 3,6 mmol de Na+ sont introduits : `reserve`.
- Mn 2p à 641 eV : ne distingue pas Mn(II) de Mn(III) (Biesinger 2011). Laissé en `reserve`, car Mn(II) est chimiquement attendu.
- Durée de vie de NG recalculée à 8,89 ns, ce qui confirme les 8,88 ns annoncés (Tableau S3 cohérent).
- Fidélité, hors de mon rôle : l'annotation de l'extraction dit que les références [S1] à [S3] sont absentes. Elles figurent pourtant à la fin de l'ESI ; je le signale dans `article_level.summary`.
- Recherches web : 6, sur la quinine, les fluorophores citrate–amine, l'XPS du Mn, les DOI Song et Fang, les tables de vapeur NIST et la DRX de g-C3N4. Crossref est bloqué, donc 5 DOI ne sont pas vérifiés. Rien n'a été ajouté à fondateurs.md ni à constantes.md.
