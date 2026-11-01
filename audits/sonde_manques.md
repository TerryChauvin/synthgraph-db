# Sonde des manques d'extraction

500 publications closes. Un « manque » = terme présent dans les sections expérimentales (ou, pour les mesures, dans tout l'article)
sans paramètre, action, équipement ni case `not_stated` correspondant ; pour les mesures, technique sans `conditions` ou sans résultat lié.
Script : `analyses/sonde_manques.py` ; détail par publication : `python3 -I analyses/sonde_manques.py <PMCID>`.

| Sonde | Articles concernés | Manques | % | dont déclarés `not_stated` |
|---|---|---|---|---|
| échelle / lot | 10 | 10 | 100.0 | 10 |
| rendement (chiffré) | 12 | 12 | 100.0 | 11 |
| répétitions | 27 | 24 | 88.9 | 0 |
| mesure : magnétisme | 28 | 19 | 67.9 | 0 |
| mesure : ICP/EDS composition | 290 | 194 | 66.9 | 0 |
| mesure : XPS | 191 | 124 | 64.9 | 0 |
| mesure : Raman | 124 | 73 | 58.9 | 0 |
| mesure : catalyse / adsorption | 388 | 223 | 57.5 | 0 |
| mesure : PL | 134 | 76 | 56.7 | 0 |
| mesure : UV-vis / band gap | 293 | 162 | 55.3 | 0 |
| mesure : électrochimie | 249 | 134 | 53.8 | 0 |
| mesure : BET | 167 | 87 | 52.1 | 0 |
| taux de remplissage | 2 | 1 | 50.0 | 0 |
| mesure : TGA | 133 | 64 | 48.1 | 0 |
| vide | 162 | 75 | 46.3 | 64 |
| mesure : DLS / zêta | 81 | 37 | 45.7 | 0 |
| débit de gaz | 46 | 21 | 45.7 | 2 |
| mesure : TEM/SEM | 481 | 198 | 41.2 | 0 |
| puissance (W) | 66 | 26 | 39.4 | 10 |
| pH | 164 | 55 | 33.5 | 7 |
| purification (dialyse, colonne, tamis) | 93 | 29 | 31.2 | 0 |
| vitesse d'addition | 107 | 33 | 30.8 | 33 |
| mesure : XRD | 429 | 125 | 29.1 | 0 |
| rampe de chauffe | 108 | 31 | 28.7 | 27 |
| vieillissement / repos | 50 | 11 | 22.0 | 0 |
| ultrasons | 152 | 30 | 19.7 | 7 |
| atmosphère | 156 | 23 | 14.7 | 15 |
| refroidissement | 119 | 14 | 11.8 | 9 |
| séchage | 383 | 21 | 5.5 | 6 |
| agitation (rpm) | 174 | 8 | 4.6 | 6 |
| centrifugation | 216 | 9 | 4.2 | 6 |
| lavage (n fois) | 118 | 1 | 0.8 | 1 |

## Répartition par publication

| Manques par publication | Publications |
|---|---|
| 0 | 12 |
| 1 | 56 |
| 2 | 75 |
| 3 | 85 |
| 4 | 82 |
| 5 | 76 |
| 6 | 59 |
| 7 | 28 |
| 8 | 18 |
| 9 | 6 |
| 10 | 1 |
| 11 | 1 |
| 12 | 1 |

## Publications les plus touchées

| PMCID | Manques | Sondes |
|---|---|---|
| PMC11891312 | 12 | débit de gaz, puissance (W), pH, ultrasons, répétitions, vitesse d'addition, mesure : TEM/SEM, mesure : XPS, mesure : UV-vis / band gap, mesure : PL, mesure : ICP/EDS composition, mesure : électrochimie |
| PMC9054805 | 11 | rampe de chauffe, débit de gaz, agitation (rpm), pH, centrifugation, ultrasons, atmosphère, mesure : XRD, mesure : UV-vis / band gap, mesure : ICP/EDS composition, mesure : électrochimie |
| PMC10460902 | 10 | agitation (rpm), puissance (W), centrifugation, ultrasons, purification (dialyse, colonne, tamis), mesure : XRD, mesure : BET, mesure : XPS, mesure : UV-vis / band gap, mesure : PL |
| PMC7184584 | 9 | rampe de chauffe, puissance (W), vide, vitesse d'addition, mesure : XRD, mesure : PL, mesure : ICP/EDS composition, mesure : électrochimie, mesure : catalyse / adsorption |
| PMC13446275 | 9 | refroidissement, débit de gaz, puissance (W), mesure : BET, mesure : XPS, mesure : UV-vis / band gap, mesure : PL, mesure : ICP/EDS composition, mesure : électrochimie |
| PMC7153708 | 9 | puissance (W), vide, échelle / lot, mesure : XRD, mesure : Raman, mesure : UV-vis / band gap, mesure : PL, mesure : ICP/EDS composition, mesure : catalyse / adsorption |
| PMC9795147 | 9 | refroidissement, pH, mesure : XRD, mesure : TEM/SEM, mesure : XPS, mesure : UV-vis / band gap, mesure : ICP/EDS composition, mesure : DLS / zêta, mesure : électrochimie |
| PMC12917697 | 9 | vide, rendement (chiffré), mesure : BET, mesure : XPS, mesure : TGA, mesure : UV-vis / band gap, mesure : ICP/EDS composition, mesure : électrochimie, mesure : catalyse / adsorption |
| PMC6804187 | 9 | pH, rendement (chiffré), mesure : XPS, mesure : Raman, mesure : UV-vis / band gap, mesure : PL, mesure : ICP/EDS composition, mesure : électrochimie, mesure : catalyse / adsorption |
| PMC7645746 | 8 | agitation (rpm), centrifugation, mesure : BET, mesure : TEM/SEM, mesure : UV-vis / band gap, mesure : ICP/EDS composition, mesure : DLS / zêta, mesure : électrochimie |
| PMC9563711 | 8 | mesure : XRD, mesure : TEM/SEM, mesure : XPS, mesure : Raman, mesure : UV-vis / band gap, mesure : PL, mesure : ICP/EDS composition, mesure : DLS / zêta |
| PMC8474143 | 8 | rampe de chauffe, débit de gaz, puissance (W), vide, mesure : XRD, mesure : TEM/SEM, mesure : UV-vis / band gap, mesure : catalyse / adsorption |
| PMC12552603 | 8 | vide, mesure : XRD, mesure : BET, mesure : TGA, mesure : UV-vis / band gap, mesure : ICP/EDS composition, mesure : magnétisme, mesure : électrochimie |
| PMC10386591 | 8 | pH, mesure : XRD, mesure : TEM/SEM, mesure : XPS, mesure : UV-vis / band gap, mesure : ICP/EDS composition, mesure : électrochimie, mesure : catalyse / adsorption |
| PMC13257848 | 8 | agitation (rpm), centrifugation, répétitions, mesure : XRD, mesure : BET, mesure : TEM/SEM, mesure : XPS, mesure : ICP/EDS composition |
| PMC11002299 | 8 | pH, vide, mesure : XRD, mesure : TEM/SEM, mesure : XPS, mesure : Raman, mesure : ICP/EDS composition, mesure : catalyse / adsorption |
| PMC8398574 | 8 | rampe de chauffe, pH, vide, mesure : TEM/SEM, mesure : ICP/EDS composition, mesure : magnétisme, mesure : électrochimie, mesure : catalyse / adsorption |
| PMC8966659 | 8 | vide, purification (dialyse, colonne, tamis), mesure : TEM/SEM, mesure : XPS, mesure : Raman, mesure : UV-vis / band gap, mesure : PL, mesure : ICP/EDS composition |
| PMC9083554 | 8 | puissance (W), vitesse d'addition, purification (dialyse, colonne, tamis), mesure : TEM/SEM, mesure : TGA, mesure : UV-vis / band gap, mesure : ICP/EDS composition, mesure : magnétisme |
| PMC8292365 | 8 | refroidissement, puissance (W), centrifugation, mesure : BET, mesure : TEM/SEM, mesure : XPS, mesure : UV-vis / band gap, mesure : ICP/EDS composition |
| PMC10219592 | 8 | vieillissement / repos, rendement (chiffré), mesure : TEM/SEM, mesure : XPS, mesure : Raman, mesure : TGA, mesure : UV-vis / band gap, mesure : catalyse / adsorption |
| PMC10967699 | 8 | pH, mesure : XRD, mesure : BET, mesure : XPS, mesure : TGA, mesure : UV-vis / band gap, mesure : ICP/EDS composition, mesure : électrochimie |
| PMC11904774 | 8 | refroidissement, mesure : XRD, mesure : TEM/SEM, mesure : TGA, mesure : UV-vis / band gap, mesure : PL, mesure : ICP/EDS composition, mesure : catalyse / adsorption |
| PMC9038048 | 8 | pH, vieillissement / repos, mesure : XRD, mesure : TEM/SEM, mesure : PL, mesure : DLS / zêta, mesure : électrochimie, mesure : catalyse / adsorption |
| PMC8822483 | 8 | rampe de chauffe, rendement (chiffré), échelle / lot, mesure : TGA, mesure : ICP/EDS composition, mesure : magnétisme, mesure : électrochimie, mesure : catalyse / adsorption |
| PMC6915586 | 8 | mesure : XRD, mesure : TEM/SEM, mesure : XPS, mesure : Raman, mesure : UV-vis / band gap, mesure : PL, mesure : ICP/EDS composition, mesure : électrochimie |
| PMC10200858 | 8 | pH, vide, vitesse d'addition, mesure : TEM/SEM, mesure : XPS, mesure : UV-vis / band gap, mesure : ICP/EDS composition, mesure : électrochimie |
| PMC5858874 | 7 | rampe de chauffe, refroidissement, débit de gaz, puissance (W), lavage (n fois), atmosphère, mesure : électrochimie |
| PMC8125239 | 7 | puissance (W), pH, mesure : XRD, mesure : BET, mesure : UV-vis / band gap, mesure : électrochimie, mesure : catalyse / adsorption |
| PMC9631917 | 7 | mesure : BET, mesure : TEM/SEM, mesure : XPS, mesure : Raman, mesure : UV-vis / band gap, mesure : PL, mesure : ICP/EDS composition |
