# Journal — passe de complément PMC10411504

Extraction déjà très complète (conditions de caractérisation, grille, TDS partiellement) : peu d'ajouts, aucun retrait.

Points de la sonde :
- **rampe de chauffe** (10 °C/min, TGA et NH3-TPD) : déjà dans `characterizations.conditions` de la voie de base ; la rampe de calcination reste `not_stated` (déjà déclarée, recherchée à nouveau : aucune valeur dans le texte, les annexes ni les légendes). Seul ajout : la TGA du précatalyseur non calciné (légende de la Fig. S11, rampe 10 °C/min), qui avait des résultats sans caractérisation.
- **vide** : deux occurrences. (1) « without pressure or vacuum setups » décrit l'essai catalytique à l'air libre ; l'entrée « catalytic test » dit déjà « ambient air », je n'ai pas modifié sa chaîne. (2) séchage sous vide 48 h = analyse TDS de 0.1-SZ-525, pas la synthèse : ajouté comme caractérisation « TDS gravimétrique » sur la branche 0.1-SZ-525 (récipient, filtre, bain d'huile, concentration sous pression réduite 48 h) avec trois résultats du Tableau S2 (masse sèche 73,0 mg, humins 21,3 mg, bilan 100,4 %).
- **rendement chiffré** : 74 %, 67 % et 96 % sont déjà en outcomes (rendement de l'essai ou de l'isolement de l'isosorbide, pas du catalyseur). Rendement du catalyseur : reste `not_stated` (déjà déclaré).
- **échelle / lot** : « scale-up » concerne l'essai catalytique, pas la synthèse du catalyseur. Ajout de `scale` et `repetitions` en `not_stated` sur la voie de base (aucune masse de catalyseur, aucun nombre de lots dans l'article ; recherche de batch, scale, g, mg, replicate).
- **électrochimie** : faux positif (« capacity » dans une phrase sur l'acide sulfurique résiduel). Rien à ajouter, pas de mesure électrochimique dans l'article.

Autres ajouts :
- Étape 2 de la voie de base : `vessel` et `atmosphere` ajoutés en `not_stated` (l'argon n'est cité que pour la dilution, pas pour l'addition à l'acide ; récipient jamais décrit). Étape 6 : `cooling_mode` (pas de refroidissement décrit après calcination).
- Voie 0.5-SZ-625_regenerated : caractérisation de la préparation des échantillons RMN du recyclage (fractions MeOH concentrées, filtre 0,2 µm, sans GdCl3). Instrument laissé null (« as described above »).
- Doute ajouté : la section Catalytic Reactions (tubes en verre, bain d'huile, 450 rpm) pourrait s'appliquer aux essais de recyclage ; l'article ne le dit pas, donc `vessel` et `stirring_speed` restent non cités sur cette voie.

Cases `not_stated` retirées : aucune (aucune n'était contredite par le texte).
