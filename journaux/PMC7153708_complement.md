# Journal du complément — PMC7153708

Passe de complément (ajouts seulement) sur la base de `audits/pilote_complement/PMC7153708_sonde.md`.

## Points de la sonde écartés
- « échelle / lot » : le terme vient d'une référence bibliographique (Scarabelli et al., « large-scale self-assembly »), pas d'une échelle de synthèse. Écarté.
- Raman et PL : mots de l'introduction ou des références ; aucune mesure Raman ni PL dans l'article. Écartés.
- XRD « résultat absent » : l'article ne donne aucun chiffre XRD (ni taille de cristallite ni paramètre de maille), seulement l'indexation des phases (déjà dans les résultats des voies). Rien à ajouter.
- « vide » : trois occurrences ; deux sont les séchages « in a vacuum » (déjà en `atmosphere = vacuum`), la troisième est « speed of light in vacuum » (formule de l'IPCE). Pour les deux séchages, aucun niveau de vide n'est donné : `pressure` ajouté à `not_stated`.
- « puissance 150 W » : lampe de l'IPCE, déjà dans `instrument` de l'entrée IPCE. L'intensité d'irradiation à 600 nm (0,607 mW·cm-2, annexe) et l'électrolyte de l'IPCE (annexe) ont été ajoutés à la fin du champ `conditions` existant (texte d'origine conservé).
- UV-vis « conditions absentes » : ni plage spectrale ni mode de mesure dans l'article ou l'annexe ; `conditions` laissé à null (rien à citer).

## Rattachements non évidents
- Les caractérisations des voies Au-CdSe, Au-Bi2Se3 et Au-CuSe (annexe) n'avaient ni appareil ni conditions : rempli avec la section 2.6 (« Characterizations »), qui est générale ; l'annexe ne nomme pas d'autre appareil. TEM, HRTEM, HAADF-STEM : Tecnai F20, 200 kV ; XRD : Bruker D8-advance, Cu kα (λ = 1,5406 Å) ; EDS : intégré au HRTEM. Même remplissage pour les entrées existantes qui avaient `null` (EDS et HAADF-STEM de la voie jaune d'œuf, etc.).
- Entrées de caractérisation créées pour les techniques dont les résultats étaient en `outcomes` sans entrée : UV-vis (Au@Se, voie jaune d'œuf, séries 0,25/0,50/0,75 mM), TEM (séries en concentration, en temps, en épaisseur de coque Se, nanocubes, PbSe_NCs, nanoprismes), photocourant et EIS (électrodes PbSe-NCs, haltère, TiO2 nu), IPCE (PbSe-NCs). Chaque entrée reprend la citation d'un résultat déjà extrait de la même voie, ou une phrase du texte (Au@Se).
- Conditions du photocourant et de l'EIS des électrodes PbSe-NCs, haltère et TiO2 nu : copiées de l'entrée de la voie Device_yolk-shell@TiO2 (même montage décrit en 2.7 pour tous les photoanodes).

## Cases `not_stated` ajoutées (16) et où j'ai cherché
Recherche dans 2.2 à 2.5, les Résultats, les légendes et l'annexe (synthèses Au-CdSe/Bi2Se3/CuSe, Table S1).
- `pressure` : séchage sous vide du film TiO2 (étape 6) et de l'électrode (étape 4 du dispositif).
- `cooling_mode` : fin des étapes de réaction à 38 °C (Au@Se), 80 °C (jaune d'œuf) et 60 °C (Au-Bi2Se3), et recuit à 550 °C du film TiO2 (seul le refroidissement de l'autoclave est dit « slowly »).
- `atmosphere` : les trois mêmes étapes de réaction en tube à essai (rien sur l'air, le bouchon ou un gaz).
- `ph` (Au@Se, Au-Bi2Se3 : pH jamais mesuré ni ajusté) et `ph_final` (jaune d'œuf : seul le pH ajusté de 9,8 est donné).
- `repetitions` au niveau des voies Au_NRs, Au@Se, jaune d'œuf et film TiO2 : nombre de lots non précisé (« four parallel samples » ne concerne que les photoanodes).

## Non fait
- Aucun `not_stated` retiré : aucune case déclarée n'était contredite par le texte.
- Aucun équipement ni étape ajoutés. Pas de figure ouverte : aucune condition de mesure n'est donnée seulement sur figure.
