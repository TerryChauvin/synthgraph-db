# Journal de la passe de complément — PMC5858874

Lecture de la sonde (7 points), de l'extraction entière et de corpus/text/PMC5858874.txt (méthodes, légendes, annexe mmc1 qui ne contient que des figures XRD/XPS sans texte utile).

## Points de la sonde écartés
- rampe de chauffe, débit de gaz, atmosphère : ce sont les réglages de la TGA (10 °C min-1, azote pur, 50 ml min-1) et du four de la GC-MS. Ils sont déjà dans `characterizations.conditions` (TGA, GC-MS). Le `not_stated` « atmosphère » / « heating_rate » de la calcination reste juste : l'article ne dit rien de l'atmosphère ni de la rampe du four à moufle à 600 °C.
- puissance (W) : 3600 W est la puissance du tube Rh de l'XRF, déjà dans les conditions de la caractérisation XRF.
- refroidissement : concerne le réacteur de HTL (refroidi à 25 °C), déjà dans les conditions de l'essai de HTL ; la vitesse de refroidissement n'est pas citée.
- lavage (n fois) : lavage du réacteur au DCM après HTL (au moins trois fois, 400 mL), déjà dans les conditions de l'essai ; pas de lavage du catalyseur dans l'article.
- mesure : électrochimie : faux positif (« Parr Instruments Co., Moline » et réacteur de 1800 ml), aucune mesure électrochimique dans l'article.

## Ajouts
- `not_stated` : `ph` à l'étape 1 (solution d'imprégnation, pH jamais donné) ; `drying_mode` à l'étape 5 (séchage à 110 °C, four ou type d'étuve non précisé) ; `repetitions` au niveau de la voie Ni/TiO2 (aucun nombre de lots pour la préparation du catalyseur ; les répétitions citées valent pour les essais de HTL). Recherche dans tout le texte, légendes et annexe comprises.
- un doute sur les conditions de HTL non citées (rampe, agitation, pression initiale de N2, vitesse de refroidissement).

## Non ajouté
- Aucune valeur nouvelle : les conditions de mesure (XRF, XRD, XPS, viscosité, TGA, TAN, GC-MS, analyse élémentaire) et les résultats chiffrés du texte et des tableaux 1 à 3 étaient déjà extraits. Les entrées « XRF du catalyseur réutilisé », TAN et test de stabilité n'ont pas d'instrument cité ; je n'ai pas supposé l'ARL ADVANT'X pour l'XRF du catalyseur réutilisé.
- `scale` laissé à null (jamais renseigné dans la base ; 20 g de TiO2 et 100 mL figurent déjà aux étapes).
- Les figures 1 et 2 ne sont pas ouvertes : leurs valeurs sont hors du périmètre de la sonde (déjà signalé en doute).
