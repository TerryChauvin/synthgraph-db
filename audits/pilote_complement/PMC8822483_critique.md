# Critique des ajouts de complément — PMC8822483

Article lu : sections Experimental, Results and Discussion, et SI (§1.2 à 3.3, tableaux S3 à S9). Les 5 doutes ajoutés ne sont pas listés dans le fichier d'ajouts et n'ont pas été jugés.

## Paramètres ajoutés

| catégorie | voie | élément | verdict | raison |
|---|---|---|---|---|
| paramètre | UMCM-1_R1 | étape 7 wash, exchange_interval = DCM frais chaque jour | juste | citation exacte (Synthetic Optimization) ; valable aussi pour R2–R6 par héritage |
| paramètre | MUF-77-methyl_R1 | étape 5 wash, exchange_interval | juste | citation exacte, même phrase pour MUF-77 |
| paramètre | truxene | étape 2 reflux, cooling_mode = refroidi puis versé sur glace | juste | SI « cooled and poured on ice », bonne voie et étape |
| paramètre | MgFe2O4@bed | étape 5 pack, packing_density = 0.1498 g/mm3 | juste (réserve) | Table S6 le dit, mais l'unité est incohérente : 0,1329 g / (π·2,76²·37 mm ≈ 887 mm3) = 1,5e-4 g/mm3, soit 0,150 g/cm3. Erreur d'unité des auteurs, à signaler en `limite_reproductibilite`. |

## not_stated ajoutés

| catégorie | voie | élément | verdict | raison |
|---|---|---|---|---|
| not_stated | UMCM-1_R1 | repetitions | juste | « average yield » sans nombre d'essais |
| not_stated | UMCM-1_R1 | vessel | douteux | « 10 mL reactor coil », Vaportec R4 donnés ; seule la matière du serpentin manque |
| not_stated | UMCM-1_R1 | gas_flow | juste | « dried under flowing N2 » sans débit |
| not_stated | MUF-77-methyl_R1 | repetitions | juste | « average yield », nombre d'essais absent |
| not_stated | MUF-77-methyl_R1 | vessel | douteux | « 10 mL reactor coil » donné, comme pour UMCM-1 |
| not_stated | MUF-77-methyl_R1 | gas_flow | juste | « dried under flowing N2 » sans débit |
| not_stated | truxene | atmosphere | juste | rien sur l'atmosphère du reflux |
| not_stated | truxene | stirring_speed | juste | agitation non mentionnée |
| not_stated | MgFe2O4 | atmosphere | juste | « heated under reflux », atmosphère muette |
| not_stated | MgFe2O4 | heating_rate | juste | aucune rampe donnée |
| not_stated | MgFe2O4 | stirring_speed | juste | agitation non mentionnée |
| not_stated | MgFe2O4 | pressure | douteux | reflux à pression ambiante implicite ; seul le niveau de vide du séchage manque |
| not_stated | MgFe2O4@bed | repetitions | douteux | si « répétitions » = cycles d'adsorption : 5 cycles (25/75) et 3 cycles (3/97) sont donnés ; vrai seulement pour les essais de préparation |
| not_stated | MgFe2O4@bed | stirring_speed | juste | roller mixer 24 h sans vitesse |

## caracterisations ajoutées

| catégorie | voie | élément | verdict | raison |
|---|---|---|---|---|
| caractérisation | MUF-77-methyl_R4_25C_5min | SEM, sphériques, 50 nm | juste | texte : « synthesized at 25 °C … decrease in size to 50 nm » |
| caractérisation | MUF-77-methyl_R5_25C_10min | SEM, sphériques, 50 nm | juste | même phrase, vaut pour les deux synthèses à 25 °C |
| caractérisation | UMCM-1_insitu_26C | Scherrer, (010) 770 nm, (111) 680 nm à 10 min | juste | texte principal, valeurs exactes |
| caractérisation | UMCM-1_insitu_26C | ajustement AE/FW | juste | texte et SI §2.2 ; Table S3 existe |
| caractérisation | MUF-7a_insitu_26C | Scherrer (042), max 800 Å | juste | « 900 and 800 Å for 80 and 26 °C » |
| caractérisation | MUF-7a_insitu_26C | ajustement AE/FW | juste | Table S4, texte |
| caractérisation | MgFe2O4@bed | SEM et EDX du composite | juste | Fig. S19–S20 : points brillants bien dispersés |
| caractérisation | MgFe2O4@bed | isothermes 2,3-DMB et N2 à 298 K | faux | le texte parle de l'isotherme du MUF-77-methyl (capacité d'équilibre 200 cm3/g, Table S8 « MUF-77 – Isotherm »), pas du composite |

## conditions_mesure ajoutées

| catégorie | voie | élément | verdict | raison |
|---|---|---|---|---|
| condition | MUF-77-methyl_R4_25C_5min | SEM : JEOL 7001F, suspension dans DCM sur Si, Ir, électrons secondaires | juste | SI §1.3.5 |
| condition | MUF-77-methyl_R5_25C_10min | SEM, mêmes conditions | juste | SI §1.3.5 |
| condition | UMCM-1_insitu_26C | Scherrer : ScatterBrain, OriginPro, K = 0,9, λ = 1,000 Å, FWHM | juste | SI §2.1 et §2.2 |
| condition | UMCM-1_insitu_26C | ajustement AE/FW : OriginPro, moindres carrés non linéaires | juste | SI §2.2 |
| condition | MUF-7a_insitu_26C | Scherrer, mêmes conditions | juste | SI §2.2 |
| condition | MUF-7a_insitu_26C | AE/FW, mêmes conditions | juste | SI §2.2 |
| condition | MgFe2O4 | SEM : JEOL 7001F, électrons secondaires, Ir | juste | SI §1.3.5 et légende S19 |
| condition | MgFe2O4@bed | SEM/EDX : JEOL 7001F, SE et BSE, EDX, Ir | juste | SI §1.3.5 et Fig. S19–S20 |
| condition | MgFe2O4@bed | isothermes 2,3-DMB/N2 : 3Flex, 298 K, 0–0,27 bar, activation 80 °C 24 h | douteux | conditions §1.3.4 exactes, mais échantillon = MUF-77-methyl ; le 3Flex n'est cité que pour la vapeur, pas pour N2 à 298 K |

## resultats ajoutés

| catégorie | voie | élément | verdict | raison |
|---|---|---|---|---|
| résultat | UMCM-1_R1 | TGA perte initiale 150 °C | juste | texte pour les UMCM-1 en général (DMF dans les pores) ; non propagé à R2–R6 |
| résultat | UMCM-1_R1 | décomposition 450 °C | juste | même phrase ; Fig. S5 ne précise pas l'échantillon |
| résultat | UMCM-1_R1 | particle_size 100 nm | juste | « fibrous crystals with diameters of 100 nm » ; Fig. 3A légendée à 130 °C, échantillon non précisé |
| résultat | UMCM-1_R1 | fraction UMCM-1 estimée 89 % | juste | estimation des auteurs d'après le rapport RMN des linkers, pour tous les échantillons |
| résultat | UMCM-1_R1 | fraction MOF-5 estimée 11 % | juste | même phrase |
| résultat | MUF-77-methyl_R1 | décomposition 435 °C | juste | « TGA of MUF-77-methyl … 435 °C (Figure S6) », échantillon non précisé |
| résultat | MUF-77-methyl_R4_25C_5min | particle_size 50 nm | juste | texte sur les synthèses à 25 °C |
| résultat | MUF-77-methyl_R5_25C_10min | particle_size 50 nm | juste | même phrase |

## Manques restants

- **Unité du packing_density** : l'ajout recopie 0,1498 g/mm3, incompatible avec la masse (0,1329 g) et le volume du lit (≈ 887 mm3 d'après DE 3/8", paroi 2 mm, hauteur 37 mm). À annoter en `limite_reproductibilite` (probablement g/cm3).
- **Mauvais rattachement de l'isotherme 298 K** : l'ajout doit passer à une voie MUF-77-methyl, et non au composite. L'échantillon exact n'est pas dit ; la lot R3 est celui utilisé pour le lit, mais l'isotherme n'est pas précisée.
- **Branche MUF-7a_insitu_80C** : elle n'a que la caractérisation « in situ WAXS ». Elle n'a ni la ligne Scherrer (max 900 Å à 80 °C, texte principal) ni l'ajustement AE/FW avec leurs conditions (OriginPro, K = 0,9, λ = 1,000 Å). Les conditions ont été ajoutées à 26 °C seulement.
- **Résultats TGA, SEM et fraction 89/11** : ajoutés à R1 seulement. Le texte les donne pour les UMCM-1 ou MUF-77 en général, donc potentiellement pour R2–R6 (UMCM-1) et R2–R5 (MUF-77) ; la fraction 89/11 vaut pour « all samples ». Conditions TGA (Mettler Toledo TGA 2, 25–850 °C, 5 °C/min, N2 20 mL/min) non attachées aux résultats TGA ajoutés (déjà présentes ailleurs dans le JSON).
- **Conditions d'instrument de la mesure in situ** : le Scherrer in situ n'a pas son instrument (SAXS beamline, Pilatus 2M, 742 mm, 11,5 keV, faisceau 0,25 × 0,45 mm2, q de 0,020 à 1,716 Å-1) dans l'ajout, même si l'extraction les a ailleurs.
- **Incohérence de l'article non signalée** : PEG Mn = 1400 (Materials SI) contre 1500 (synthèse MgFe2O4) ; à annoter si absent.
- **Cycles du lit** : 5 cycles (25/75), 3 cycles (3/97) donnés dans le texte, donc `repetitions` n'est pas « non indiqué » pour les expériences de percée.

## Bilan

- Ajouts contrôlés : 43 (4 paramètres, 14 not_stated, 8 caractérisations, 9 conditions, 8 résultats).
- Faux : 1 (isotherme 2,3-DMB/N2 rattachée au composite alors qu'elle concerne le MUF-77-methyl).
- Douteux : 5 (2 `vessel`, `pressure` de MgFe2O4, `repetitions` du lit, conditions de l'isotherme du composite). Le packing_density est jugé juste (la citation le soutient) mais son unité est fausse chez les auteurs.
