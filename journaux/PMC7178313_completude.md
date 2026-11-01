# Journal — test de complétude PMC7178313

- La synthèse (une voie de base, six branches en teneur d'Eu3+) était déjà complète : aucune valeur de procédé ajoutée. La sonde n'avait qu'un point, « débit de gaz » : les 2 ml/min sont la vitesse d'addition de l'APT, déjà en `addition_rate` ; écarté.
- L'échantillon à 2 % préparé par réaction à l'état solide (Tableaux 1 à 3) est « re-mesuré dans ce travail » mais sa synthèse n'est pas décrite : pas de voie, donc 17 entrées `comparisons` rattachées à BMW_5Eu (une valeur par entrée, la rangée du tableau en citation), avec la mention « re-mesuré à 266 nm » dans `conditions`. Voie `calcul` non créée : Judd–Ofelt est calculé à partir d'un spectre mesuré, pas une simulation.
- Tableau 3 : la colonne des références est vide dans le texte. B15 (Ran et al., (Li, Na, K)LaMgWO6) est déduit de la phrase qui compare les Ω à ces trois composés ; dit dans les `conditions` et dans un doute.
- Positions de pics de la série (2θ des phases parasites, 584,4 / 618,7 / 665 / 721,3 nm) : l'article les donne pour la série entière. Rangées sur la voie de base BMW_5Eu (échantillon des Fig. 5, 10 et Tableau S1), avec un doute, car les marqueurs de la Fig. 2a n'y montrent que Ba3WO6.
- Les positions 2θ sont une seule caractérisation XRD « série entière » plutôt que dix outcomes, pour ne pas les attribuer à un échantillon précis.
- Conditions de mesure : excitation (McPherson, lampe Xe 150 W, R928, suivi à 596 nm) et déclin à 77 K (Lecroy + Nd:YAG ; 588, 602, 596, 722 nm) ajoutés en nouvelles entrées, sans modifier les `characterizations` existantes (leurs `conditions` sont déjà renseignées).
- Valeurs de référence du calcul de Judd–Ofelt (n = 1,874, U(2), U(4), U(6), 4e harmonique du Nd:YAG, spectre à 300 K) dans les `conditions` d'une caractérisation propre à BMW_5Eu.
- Tableau S1 (≈ 86 raies vibroniques, une valeur par ligne dans le texte) : non transcrit en entier. Entrée de caractérisation qui donne l'étendue (548,25 à 760,5 nm) et seules la raie 5D0–7F0 à 585 nm (outcome) est reprise. Le compte « ≈ 86 » est une lecture approchée du tableau, pas une valeur de l'article.
- Rayons ioniques (Shannon, réf. B6) : en `comparisons` car ce sont des valeurs de la littérature qui fondent l'argument du site occupé et du co-dopage Li+.
- Figure 1 ouverte : confirme le doute déjà noté (24 h sur le schéma, 20 h dans le texte) ; aucune autre figure ouverte, les résultats chiffrés étaient déjà lus.
- Vérifié par script que rien d'existant n'a été modifié ni retiré (le JSON d'origine est un sous-ensemble du nouveau).
