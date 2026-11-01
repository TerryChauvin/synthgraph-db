# Journal d'extraction PMC6237675 (ZSM-5 hiérarchisée, gabarit mou ST)

- Découpage : 8 voies. Voie de base = MZ-3 (échantillon optimal, seul décrit en détail avec 170 °C, 3 jours et TPAOH/ST = 8). MZ-1, MZ-2 et MZ-4 sont des branches dont seule la masse de ST change (1,3 / 2,2 / 3,9 g), lue dans la phrase « respectively » en notant l'ordre MZ-1 à MZ-4 = 1,3 ; 2,2 ; 3,1 ; 3,9 g.
- ST (gabarit) : voie `intermediate` à part, car synthétisé par les auteurs puis réutilisé ; MZ-3 le cite comme réactif de rôle `intermediate`. Quantités des deux silanes, rendement et rapport non cités (déclarés `not_stated`). Remarque en analyse : la formule C24H57O13NSi3 = 1 APTMS + 2 GPTMS.
- TZ : « same method of MZ without the mesoporogen ST ». Comme l'étape 1 de MZ-3 est l'ajout de ST, TZ reçoit ses propres étapes (copie sans ST) plutôt que d'hériter d'une étape d'ajout de ST. Variation sur le réactif ST = `absent`.
- TPAOH : seule la plage « 20–60 mL » est écrite pour le protocole type ; elle est gardée en `amount_text` pour MZ-3 avec un doute. Aucune branche par borne de plage (règle des plages), les plages 160–200 °C, 1–5 jours et 2–7 ST vont dans l'annexe absente (Tables S1–S3).
- Cristallisation en deux étapes : 80 °C 24 h (protocole type) puis 170 °C 3 jours (phrase des échantillons optimaux et phrase des MZ), deux étapes `heat`.
- Ion échange NH4NO3 + calcination 550 °C 6 h : l'article parle de « Na+-form samples » en général ; une seule voie `post_treatment` « H-form_exchange », rattachée à MZ-3 par son réactif. Forme (Na ou H) des mesures de la Table 1 non dite : doute.
- HT-MZ-3 : voie `post_treatment` (traitement hydrothermique 150 °C, 10 jours, donné dans la section Caractérisation) ; milieu, récipient et forme non cités. Valeurs de Table de Fig. 10 : textes préférés ; seule Vmic = 0,1 cm3/g lue sur la figure (valeur imprimée).
- Table 1 : une rangée entière en citation par échantillon, attribuée par le nom (TZ, MZ-1 à MZ-4) ; 7 propriétés par rangée.
- Figures lues (4 valeurs + 1) : Fig. 7 (conversion à 5 h, MZ-3 ≈ 74 %, TZ ≈ 6 %), Fig. 8 (DIPB 38,2 % pour TZ ; DIPB 26,4 % et IPB 42,8 % pour MZ-3, valeurs imprimées), Fig. 10 (Vmic 0,1). Légende en citation.
- Recyclage (20 essais) : MZ-3-used n'est pas une voie ; résultats (31,8 %, 21,6 %, coke 18,57 %) rangés sur MZ-3 ; échantillon d'inventaire sans voie. Essai à blanc LDPE sans voie (pas de matériau).
- Annexes : Additional file 1 (Figures S1–S10, Tables S1–S10) absente du fichier texte ; une annotation `limite_reproductibilite` « Annexe absente du dépôt ».
- Aucune source de méthode (`method_sources` vide) : les renvois CR33, CR39, CR41 etc. sont de l'interprétation ou des formules (HF), pas des protocoles à reprendre.
- Résultats catalytiques ajoutés sur MZ-3 et TZ seulement, conditions des tests dans `characterizations` (instrument et conditions).
