# Couverture des valeurs chiffrées

500 publications. Script : `analyses/couverture_valeurs.py`.

| Source | Nombres dans l'article | Absents de l'extraction | Couverture |
|---|---|---|---|
| cellules numériques des tableaux | 19386 | 3626 | 81.3 % |
| nombres avec unité, corps hors expérimental | 49677 | 5805 | 88.3 % |
| nombres avec unité, sections expérimentales | 13170 | 592 | 95.5 % |

## Lecture (28/10/2026) : la sélection « option A » mise à l'épreuve

Question de l'utilisateur : la sonde (`analyses/sonde_manques.py`) oublie-t-elle des valeurs, notamment dans les tableaux ? Cette mesure est indépendante de la sonde (nombres de l'article contre nombres de l'extraction, sans agent).

1. **Couverture globale** : 95,5 % des nombres avec unité des sections expérimentales sont dans la base ; 88,3 % des nombres avec unité du reste du corps ; 81,3 % des cellules numériques des tableaux.
2. **La sonde ne prédit pas les valeurs manquantes** : corrélation de rang 0,0 entre le nombre de points de la sonde et le nombre de valeurs absentes. La sélection « option A » (≥ 3 conditions de mesure absentes, 222 publications) ne contient que 44 % des valeurs absentes, et 46 des 100 publications les plus touchées.
3. **Le pilote de complément n'a pas comblé ces manques** : sur ses 20 publications, 1 % des cellules de tableaux absentes et 11 % des nombres absents du texte ont été ajoutés. Sa consigne vise les conditions de mesure et les cases `not_stated`, pas les valeurs oubliées.
4. **Part réelle des manques** :
   - tableaux, classés par titre : résultats d'échantillons 86 % couverts (1 930 cellules absentes), plans d'expérience et recettes 90 % (183) ; hors périmètre : comparaisons avec la littérature 63 % (804), statistiques et ANOVA 38 % (580), calculs DFT 88 % (129). Les manques réels (2 113 cellules) sont concentrés : 50 publications en portent 84 %.
   - texte, 40 nombres absents tirés au hasard : 15 hors périmètre (littérature, DFT, références JCPDS, barres d'échelle, statistiques), 10 conditions de mesure, 8 positions de pics XPS/FTIR/XRD, 7 résultats d'échantillon réels.
5. **Limites de cette mesure** : un nombre présent ailleurs dans l'extraction compte comme couvert (mesure indulgente) ; les valeurs lues seulement sur les figures et les annexes absentes du dépôt (68 publications) ne sont pas mesurées.

Conséquence : deux manques différents, deux sélections. Valeurs (≥ 15 valeurs absentes estimées dans le périmètre) : 102 publications, 65 % des valeurs absentes. Conditions de mesure (≥ 3 points de la sonde) : 209 publications. Union : 272, intersection : 39.
