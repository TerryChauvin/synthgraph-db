# Journal du complément — PMC5376314

Sonde : 6 points. Un seul a conduit à une correction de fond ; les autres sont écartés ou déjà couverts.

## Points écartés
- **Rampe de chauffe, débit de gaz (TGA)** : déjà dans `characterizations` TGA de Co1 (instrument et conditions). Voir plus bas : ils sont en plus rattachés à l'étape 6 de Co1.
- **Refroidissement** : « cooled to room temperature » concerne la digestion micro-ondes pour l'AAS, déjà dans `conditions` de la caractérisation AAS. Pas une consigne de synthèse.
- **Vitesse d'addition** : faux positif (le terme « stream » du flux d'azote). Les solides sont simplement dissous ; aucune addition progressive.
- **ICP/EDS** : aucune condition d'acquisition de l'EDX dans l'article (ni détecteur ni tension). Instrument et conditions laissés vides, doute ajouté. Rien n'est supposé identique au MET JEOL 2100.
- **Électrochimie** : mention d'application en introduction seulement ; aucune mesure électrochimique dans l'article.

## Rattachement non évident : chauffage du cobalt (Co1 étape 6)
- L'Experimental, dans le paragraphe du cobalt, dit « We heated the as-obtained amorphous products using a Mettler TGA/SDTA 851e ... nitrogen ... 100 mL/min ... 10 K/min ». La première extraction avait déclaré atmosphère, vitesse de chauffe et débit « non cités » dans l'étape 6 car le texte ne relie pas explicitement le palier de 2 h à 500 °C à la thermobalance.
- Les trois cases `not_stated` (atmosphere, heating_rate, gas_flow) sont retirées et remplacées par les paramètres avec la citation de cette phrase, plus l'équipement (Mettler TGA/SDTA 851e, creusets Al2O3). Le doute sur le palier de 2 h est conservé et complété (nouveau doute « Co1 étape 6 (complément) »). Les anciens doutes et `missing_fields` ne sont pas modifiés.

## Ajouts
- Ni3 étape 5 : `drying_mode` = « air-dried » (citation « air-dried for 24 h »).
- `not_stated` ajoutés (après recherche dans Experimental, Résultats, légendes, notes de tableau ; il n'y a pas d'annexe) : voies Ni3 et Co1 `repetitions` ; étape 1 (dissolution) `ph`, `addition_mode` (+ `temperature`, `stirring_speed` pour Co1) ; étape 2 (sonication) `power` (seule l'amplitude en % est donnée, pas la puissance en W), et pour Co1 `temperature`, `pulse_mode`, `probe_immersion_depth` ; étape de lavage `wash_volume` ; Co1 étape 6 `vessel` (four ou thermobalance non établi).
- Caractérisations AAS (instrument et conditions du résumé de l'AAS de Ni3) ajoutées à Ni11 (58,6 % Ni, calculé 57,9 %), Ni5 et Ni6 (64,4 ± 0,3 %, résultat commun aux deux).
- Équipement du cobalt pour les étapes 1-2 non copié (renvoi « same general procedure ») : doute ajouté.

## Fragile
- Lecture du chauffage Co1 (voir plus haut).
- Aucune figure ouverte : aucune condition de mesure n'est donnée seulement sur figure.
