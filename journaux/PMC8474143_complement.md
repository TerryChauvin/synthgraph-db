# Journal de la passe de complément — PMC8474143

Ajout seulement : aucune valeur, citation, étape ni annotation existante n'a été modifiée ; seuls trois champs `null` ont été renseignés (`scale` de QDs-TES, `conditions` des TEM de QDs-HSQ et QDs-SiO).

## Points de la sonde écartés ou déjà couverts
- rampe de chauffe (3 occurrences) : ce sont les conditions de la TGA (10 °C min-1, 25 ou 30 à 900 °C), déjà en `characterizations.conditions` de QDs-TES. Pas de rampe de recuit dans l'article : `heating_rate` reste dans `not_stated` des étapes de recuit et d'hydrosilylation.
- débit de gaz (« N2 flow of 50 mL/min ») : mesure TGA, déjà dans `conditions`. Rien sur le débit de Ar/H2 au recuit ni de l'argon de la ligne de Schlenk : `gas_flow` ajouté en non cité.
- puissance (15 W cm-2) : densité de puissance du laser de la mesure de déclin, déjà dans `conditions` du déclin résolu en énergie ; pas une consigne de synthèse. Puissance et fréquence des ultrasons (« ultrasonic », « ultrasonication ») non citées : ajoutées en non cité.
- vide (3 occurrences) : le séchage 24 h sous vide à température ambiante est dans l'étape 5 ; ajout du paramètre `drying_mode` = vacuum. Aucun niveau de vide : `pressure` reste non cité. Les deux autres occurrences sont des commentaires ATR de l'annexe.
- XRD / TEM / UV-vis : voir ci-dessous.
- catalyse / adsorption : faux positif (« light conversion for photovoltaics » ; aucune mesure catalytique).

## Ajouts
- Paramètres : atmosphère argon de l'étape 1 de QDs-TES (la phrase la donne) ; `drying_mode` à l'étape 5. Échelle de QDs-TES (55 mmol de TES, ~2,5 g de xerogel, ~90 mg de QDs pour 2,2 g de poudre recuite), recopiée de l'annexe S1/S4.
- `not_stated` (33) cherchés dans tout le texte, annexes et légendes comprises : `ph` (sol-gel acide, seule la concentration de HNO3 est donnée), `wash_volume` (lavage du gel à l'éthanol), `gas_flow`, `cooling_mode` et `vessel` (four, creuset ou nacelle jamais nommés) pour les recuits et l'hydrosilylation, `power` et `frequency` pour les trois sonications et la dispersion dans l'OSTE, `stirring_speed` pour les mélanges de HSQ, SiO et du mélange des monomères, `repetitions` au niveau voie pour HSQ, SiO et OSTE (un seul lot décrit ; les sept lots de la Table S9 sont déjà dans les résultats de QDs-TES).
- Conditions de mesure : conditions du TEM reprises pour HSQ et SiO (même protocole de préparation, « Si QDs in toluene solutions were drop-casted… ») ; nouvelles entrées UV-vis, PLQY et déclin PL pour HSQ et SiO avec l'instrument et les conditions de QDs-TES (méthodes communes aux trois précurseurs) ; entrées TGA pour HSQ et SiO (Fig. S3 couvre les trois précurseurs).
- Résultats : positions des pics XRD du Si (28, 48, 55°) et bande large SiO2 amorphe à 21° (références pré-recuites), pour les trois voies de base ; taille moyenne TEM 4–5 nm (phrase valant pour les trois précurseurs) ; bosses des SiO pré-recuits (28, 50°).

## Non ajouté
- Taille de cristallite, paramètre de maille, bande interdite, surface BET : aucune valeur dans l'article. Nombre de particules comptées en TEM et pas de balayage XRD : non donnés (aucune case pour les déclarer dans `characterizations`).
- Valeurs des histogrammes de la Fig. 2c-e : ouverte, aucune moyenne chiffrée lisible, donc rien lu sur figure.

## Fragile
- TGA : 25 °C (Méthodes) contre 30 °C (légende Fig. S3) ; noté en doute. Les entrées TGA de HSQ et SiO portent la phrase de l'annexe propre à chaque précurseur ; les conditions sont celles de la méthode générale.
- Rattachement des UV-vis, PLQY et déclin de HSQ et SiO : les méthodes sont écrites une seule fois pour toutes les voies.
