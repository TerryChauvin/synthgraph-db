# Journal de la passe de complément — PMC13446275

Passe en ajout seulement ; aucune valeur, citation ni annotation existante modifiée ; aucune case `not_stated` retirée.

## Points de la sonde
- Refroidissement : écarté. Les 5 occurrences sont « Quenching » (extinction de PL, annexe S3), sans rapport avec le refroidissement. Le `cooling_rate` déjà déclaré non cité reste vrai ; j'ai ajouté `cooling_mode` (aucun mode de refroidissement après l'autoclave ni après la calcination).
- Débit de gaz : l'argon à 50 puis 20 mL min−1 est une condition de la mesure photocatalytique. Il figure déjà dans `characterizations.conditions` de toutes les voies ; rien à ajouter, rien dans une étape de synthèse.
- Puissance (1252,65 W) : c'est la puissance calculée de la lumière dans le calcul de l'AQE (annexe S4), pas un paramètre de synthèse. Ajoutée en condition d'une entrée `AQE calculation (SI S4)` de PCS_Na2S_3wt, avec l'aire éclairée, le courant du détecteur et le nombre de photons. Incohérences (10,44 × 120 = 1252,8 ; 3,417 contre 3,147 × 10^21) mises en `doubts`.
- BET : aucune condition (dégazage, température, appareil) dans l'article ni l'annexe (recherche de degas, 77 K, Micromeritics, etc. : rien). Entrées BET créées pour CS_EDTA, CS_PEG3350, CS_PEG9000 avec seule condition « N2 adsorption–desorption ». Pas d'entrée BET pour la série Pd (Table 3 ne nomme pas la méthode ; le résultat reste dans `outcomes`).
- XPS : ni source de rayons X, ni énergie de passage, ni calage du C 1s dans le texte. Rien à ajouter pour les spectres de cœur. Ajout d'entrées « XPS valence band » (CS_Na2S, PCS_Na2S, PCS_Na2S_3wt) car la VBM vient des spectres de bande de valence.
- UV-vis / bande interdite : conditions ajoutées (réflectance diffuse, fonction de Kubelka–Munk, tracé de Tauc ; exposant n non donné) aux deux entrées existantes, et entrées créées pour les 7 voies qui avaient une bande interdite sans entrée (instrument Jasco UV-670 des Méthodes).
- PL : entrées créées (instrument Jasco FP-6300) pour les 8 voies qui avaient `PL_intensity` sans entrée ; longueur d'onde d'excitation non donnée. Résultat chiffré de l'annexe S3 : 19,94 (3 wt%) ajouté en `outcomes` de PCS_Na2S_3wt ; 26,23 non rattaché (échantillon non nommé) et signalé en doute.
- ICP/EDS : l'EDS (Aztec) est déjà dans l'entrée de cartographie de PCS_Na2S_3wt ; aucune composition chiffrée dans l'article ; rien à ajouter.
- Électrochimie (EIS) : électrolyte, fréquences, électrode non donnés nulle part ; entrée EIS laissée telle quelle.

## Autres ajouts
- CO pulse chemisorption : entrées créées pour les voies 2, 3, 4, 5 wt% (elles avaient une dispersion de Pd sans entrée), instrument et conditions recopiés de l'entrée de PCS_Na2S ; citation de la phrase « 1 to 5 wt% » des Résultats.
- Entrée « photocatalytic recyclability test » pour PCS_Na2S_3wt (3 cycles de 12 h).
- Expériences témoins de l'annexe S1 : qualitatives, catalyseur non identifié, donc en `doubts` plutôt que rattachées à une voie.

## Cases `not_stated` ajoutées (13)
Cherchées dans Méthodes, Résultats, légendes et annexe : route CS_Na2S et PCS_Na2S `repetitions` ; CS_Na2S étape 1 `ph`, étape 2 `autoclave_volume`, `addition_mode`, étape 3 `cooling_mode` ; PCS_Na2S étape 2 `ph`, étape 3 `addition_mode`, étape 4 `addition_mode`, `ph`, étape 7 `drying_mode`, étape 8 `vessel`, `cooling_mode`. Non déclarés car sans objet : gas_flow et pression de calcination (déjà `atmosphere` déclaré), puissance/fréquence (ni micro-ondes ni ultrasons).
