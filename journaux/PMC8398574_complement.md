# Journal de complément PMC8398574

Extraction déjà très complète (grille, annexes absentes, Fig. 4 lue). Peu d'ajouts utiles ; tout est en ajout seul.

Points de la sonde écartés :
- Rampe de chauffe (10 °C/min) : phrase de l'ATG/DSC (STA449F3, N2), déjà dans `conditions` des entrées TGA-DSC ; l'article ne donne aucune rampe du four de calcination, `heating_rate` reste non cité (doute existant).
- pH : « pH close to 7 » est le critère de fin de lavage, déjà `endpoint_ph` ; le pH initial/final de la précipitation est déjà non cité (étape 1 `ph`, missing_fields).
- Vide : séchage « under vacuum » déjà `atmosphere`, `pressure` déjà non cité (niveau de vide absent du texte).
- Magnétisme, électrochimie, catalyse/adsorption : termes de l'introduction ou de la perte de masse en ATG ; aucune mesure de ce type dans l'article (pas de VSM, pas de test électrochimique ni catalytique).
- SEM : JEOL JSM-7800F déjà en instrument ; tension, grossissement, nombre de particules comptées jamais donnés (la structure des caractérisations n'a pas de case non cité).
- XRD : seul « Cu Ka radiation » est donné (déjà en conditions) ; plage, pas, méthode de taille de cristallite absents. ICP : aucune condition.

Ajouts :
- 1 caractérisation EDS (LDH) : appareil et confirmation du rapport Ni/Fe, détail en Figure S2 (annexe absente du dépôt, déjà signalé en annotation).
- 1 caractérisation DSC (LDH) : absence de pic endo/exothermique après 475 °C, appareil et conditions repris de l'ATG/DSC.
- 1 résultat : rapport M2+/M3+ de 2–4 (LDH), en value_text.
- `not_stated` : `vessel` (étape 1 LDH, récipient de précipitation non donné) ; `repetitions` (route LDH et route MMO, nombre de lots non donné). Cherché dans Méthodes, Résultats, légendes ; aucune annexe de synthèse dans le fichier.
- 1 doute récapitulant les points de la sonde écartés.

Non ajouté volontairement : `cooling_mode` (déjà `cooling_rate` non cité pour la calcination), `atmosphere` de la précipitation (sans objet signalé pour Ni/Fe(III)), puissance/fréquence (méthode sans micro-ondes ni ultrasons).
