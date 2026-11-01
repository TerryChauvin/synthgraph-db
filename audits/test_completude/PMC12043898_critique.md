# Critique de fidélité des ajouts — PMC12043898

Article : `corpus/text/PMC12043898.txt` (texte principal l. 1-66, SI MOESM1 l. 67-1255, données MOESM3 l. 1260-2553, **fichier d'évaluation par les pairs MOESM4 l. 2554-5185**). Les citations de la liste sont tronquées à 200 caractères et les valeurs à 60 : les verdicts portent sur le texte complet retrouvé dans l'article.

Règle appliquée en plus de CRITIQUE_AJOUTS.md : toute valeur dont la citation est dans MOESM4 (réponses aux relecteurs, « Response: », « Fig. R… ») est `faux`, même si le même nombre existe ailleurs dans l'article (alors `douteux` : la citation est à remplacer par le passage de l'article). Les ajouts sans défaut sont regroupés par série dans une même ligne, avec leur nombre ; chaque ajout de la liste est couvert (415 : 48 paramètres, 18 not_stated, 4 équipements, 16 caractérisations, 16 conditions de mesure, 134 résultats, 8 réactifs, 11 étapes, 3 voies, 157 comparaisons).

## 1. Paramètres (48)

| Catégorie | Voie | Élément | Verdict | Raison |
|---|---|---|---|---|
| parametre | Ni-BTA | étape 3 concentration = 14 M (ammoniaque) | juste | « ammonia (~14 M) » dans Méthodes |
| parametre | Electrode_RRDE | étape 4 : scan_rate 10 mV/s, rotation 1600 rpm, pH des 4 électrolytes, potentiel anneau 1,5 V (alcalin) et 1,2 V (neutre), efficacité de collecte 0,37, température ~25 °C (7 ajouts) | juste | Méthodes, « Electrochemical measurements » |
| parametre | Electrode_GDE | étape 3 épaisseur Nafion 117 = 0,18 mm | juste | Méthodes, Materials |
| parametre | Electrode_GDE | étape 5 : surface 1,0 × 1,0 cm2, pH (KOH 13,8 ; NaCl 6,5), potentiels 0,7 à −0,6 V, FE faite une seule fois (4 ajouts) | juste | Méthodes, cellule à flux |
| parametre | Electrode_GDE | étape 5 distance = 2 cm | **faux** | citation dans MOESM4 (réponse au relecteur sur l'EIS, l. 3796), absente de l'article |
| parametre | Electrode_GDE | étape 6 : 100 mA cm-2, 24 h, 30 mL, deux renouvellements d'électrolyte à 8 h et 15 h (4 ajouts) | juste | texte principal, Fig. 4d |
| parametre | Electrode_GDE | étape 7 : 200 mA cm-2, 30 mL KOH, 10 h (3 ajouts) | juste | texte principal |
| parametre | Electrode_GDE | étape 8 : 100 mA cm-2 initial, 260 mL, 0,2 V vs RHE, 40 h (4 ajouts) | juste | texte principal |
| parametre | DFT_ORR_thermodynamics | boîte 7,62 × 20 × 25 Å, PBE, coupure 400 eV, k-points 3×1×1 Gamma, force 0,02 eV/Å, énergie 10-6 eV, 298,15 K, modèle CHE, U = 0,695 / 1,23 V (9 ajouts) | juste | Méthodes, « DFT Calculation » |
| parametre | AIMD_slow_growth_d-OH-Ni | 24 H2O, 300 K (étapes 2 et 3), coupure 400 eV, k-points 1×1×1, pas 0,5 fs, NVT, vitesse 0,0005 Å/pas, variable collective Ni-O / O-O (9 ajouts) | juste | Méthodes, AIMD slow growth |
| parametre | AIMD_slow_growth_d-OH-Ni | étape 2 stabilization_time = 500 fs | **faux** | citation dans MOESM4 (l. 2784), pas dans l'article |
| parametre | AIMD_slow_growth_d-OH-Ni | étape 2 selected_snapshot_time = 1000 fs | **faux** | même passage de MOESM4 (l. 2785) |
| parametre | DFT_IR_frequencies | B3LYP, 6-31+G(d), D2O avec deutérium dans les fichiers d'entrée (3 ajouts) | juste | SI Tableau 7, « Calculation method » |

## 2. not_stated (18)

| Catégorie | Voie | Élément | Verdict | Raison |
|---|---|---|---|---|
| not_stated | Ni-BTA | repetitions, ph, atmosphere, vessel, wash_volume, centrifuge_speed (6) | juste | Méthodes de synthèse ne donnent rien de tel (3 lavages, séchage 60 °C sous vide) |
| not_stated | Electrode_RRDE | supplier (tige de graphite) | juste | fournisseur de la tige non indiqué |
| not_stated | Electrode_RRDE | amount, purity (2 + 2 : tige de graphite et Ag/AgCl) | douteux | sans objet pour du matériel ; si visé sur les électrolytes, KOH, NaCl, Na2SO4 ont une pureté (Matériaux) |
| not_stated | Electrode_GDE | anode_material | **faux** | feuille de Pt 2×2 cm2 en contre-électrode, donc anode, dite dans Méthodes |
| not_stated | Electrode_GDE | membrane_area | juste | surface de la membrane Nafion non donnée |
| not_stated | Electrode_GDE | amount, purity | douteux | charge 0,1 mg cm-2 donnée ; « pureté » sans objet pour une GDE |
| not_stated | DFT_ORR / AIMD / DFT_IR | yield (3) | douteux | n'a pas de sens pour un calcul |

## 3. Équipements (4) et réactifs, étapes (19)

| Catégorie | Voie | Élément | Verdict | Raison |
|---|---|---|---|---|
| equipement | Electrode_RRDE | CHI 760E, 3 électrodes, tige de graphite, Ag/AgCl | juste | Méthodes |
| equipement | DFT_ORR | VASP, PAW | juste | Méthodes |
| equipement | AIMD | VASP, SHAKE | juste | Méthodes |
| equipement | DFT_IR | Gaussian 09 | juste | SI Tableau 7 |
| reactif | Electrode_RRDE / Electrode_GDE | graphite, Ag/AgCl (R0302), KOH 0,1 M, NaCl 0,9 et 3,6 %, Na2SO4 0,1 M, O2 (8) | juste | Méthodes |
| etape | Electrode_RRDE (1), Electrode_GDE (3), DFT_ORR (3), AIMD (3), DFT_IR (1) : 11 étapes | juste | décrivent le texte des Méthodes / SI ; les ordres 6-7-8 des essais de flux suivent le texte principal |

## 4. Voies (3)

| Catégorie | Voie | Élément | Verdict | Raison |
|---|---|---|---|---|
| voie | D | DFT s-Ni, s-OH-Ni, d-Ni, d-OH-Ni et analogues M-BTA | juste | Méthodes + SI Tableau 8 |
| voie | A | AIMD slow growth de d-OH-Ni | juste | Méthodes + légende SI Fig. 44 |
| voie | D | Ni-O2, Ni-OOD, Ni-OD, fréquences IR | douteux | contenu dans SI Tableau 7, mais libellé renvoie à « Fig. R4 » (fichier de réponses) |

## 5. Caractérisations (16) et conditions de mesure (16)

| Catégorie | Voie | Élément | Verdict | Raison |
|---|---|---|---|---|
| caracterisation | Ni-BTA | liste XRD / simulation (SI Tab. 1) | juste | valeurs du tableau reprises |
| condition_mesure | Ni-BTA | XRD : D8 Advanced, Cu Kα | juste | Méthodes |
| caracterisation | Ni-BTA | simulation XRD (Materials Studio) | **faux** | « Materials Studio » seulement dans MOESM4 (l. 3157) |
| condition_mesure | Ni-BTA | simulation XRD, Materials Studio, maille a = 7,6 b = 11,6 c = 7,6 Å | **faux** | citation de MOESM4 ; la maille est dans SI Fig. 6 mais pas le logiciel |
| caracterisation | Ni-BTA | analyse élémentaire (SI Tab. 2) | juste | 35,7 / 26,8 / 9,6 / 3,4 / 24,5 % retrouvés ; rapports molaires recalculés cohérents |
| condition_mesure | Ni-BTA | Vario Micro Cube, ICP pour Ni, théorique à polymérisation infinie | juste | légende SI Tab. 2 |
| caracterisation | Ni-BTA | ajustement EXAFS, seuil K du Ni (SI Tab. 3) | juste | toutes les valeurs correspondent |
| condition_mesure | Ni-BTA | EXAFS : S02 0,93, fenêtres de R et de k, critères, facteurs R de référence | juste | SI Tab. 3, notes |
| condition_mesure | Ni-BTA | EXAFS : « pondéré k3 selon le Peer Review File » | douteux | dernier élément seulement dans MOESM4 (l. 4099) ; le reste est juste |
| caracterisation | Ni-BTA | EXAFS après catalyse (SI Tab. 6) | juste | valeurs correspondent |
| condition_mesure | Ni-BTA | Athena/Artemis, 7 h à 0 V ; conflit avec la légende Fig. 35 signalé | juste | Tab. 6, légende Fig. 35 et Méthodes bien opposés |
| caracterisation | Ni-BTA | cartographie EDS-TEM | juste | texte principal |
| condition_mesure | Ni-BTA | TEM JEOL-200CX | juste | Méthodes |
| caracterisation | Ni-BTA | ATR-SEIRAS, bande N-H | juste | texte principal |
| condition_mesure | Ni-BTA | Bruker Tensor, détecteur MCT, KOH 0,1 M dans D2O, OCP à 0,7 puis 0,2 V ; pas, nombre de balayages absents | juste | Méthodes + texte |
| caracterisation | Ni-BTA | capacité de double couche Cdl | juste | SI Fig. 22 |
| condition_mesure | Ni-BTA | Ar, 0,92-1,00 V, 10 à 50 mV/s, pente de Δj à 0,96 V ; électrolyte non dit | juste | note SI Fig. 22 |
| caracterisation | Ni-BTA | réduction de H2O2 (H2O2RR) | juste | Fig. 3c, SI Fig. 21 |
| condition_mesure | Ni-BTA | Ar, KOH 0,10 M + 10 mM H2O2, non corrigé iR, -0,2 V | juste | SI Fig. 21 |
| caracterisation | Ni-BTA | calibrage de l'efficacité de collecte 0,37 | juste | Méthodes + SI Fig. 19 |
| condition_mesure | Ni-BTA | anneau 1,5 V, K3Fe(CN)6 5 mM, KOH 0,1 M sous Ar ; disque 0,2475 / anneau 0,1866 cm2 | juste | note SI Fig. 19 + Méthodes |
| caracterisation | Ni-BTA | RRDE dans HClO4 0,1 M (essai du fichier des relecteurs) | **faux** | provient de MOESM4 (l. 3384-3395) ; la réponse dit elle-même que l'essai est retiré du manuscrit |
| condition_mesure | Ni-BTA | RRDE HClO4, 1600 rpm, 10 mV/s, Fig. R2 / R3 | **faux** | idem, uniquement MOESM4 |
| caracterisation | Ni-BTA | XRD in/ex situ (pic supplémentaire à 26,4°) | **faux** | le pic à 26,4° (fibre de carbone) n'est que dans MOESM4 (l. 3892) |
| condition_mesure | Ni-BTA | in situ 0-120 min, ex situ 7 h, 0 V, NaCl 3,6 % sur fibre de carbone | douteux | conditions dans légende SI Fig. 33 et Méthodes ; la citation et « fibre de carbone » viennent de MOESM4 |
| caracterisation | Electrode_RRDE | conditions LSV, calibrage de l'électrode de référence, formules | juste | Méthodes |
| condition_mesure | Electrode_RRDE | CHI 760E, RRDE carbone vitreux / Pt, CV à 1,0 mV/s sous H2, non corrigé iR | juste | Méthodes + légendes |
| caracterisation | Electrode_GDE | EIS en cellule à flux : Rct ≈ 0,85 Ω (NaCl) et 0,70 Ω (KOH), plus résistance de solution | douteux | Rct dans l'article ; la résistance de solution (4,53 / 4,92 Ω) vient de MOESM4 |
| condition_mesure | Electrode_GDE | EIS : 5 mV, 10^5 à 0,1 Hz (« 105 Hz » dans le texte), circuit Rs, Rct, CF, Warburg | douteux | 5 mV et fréquences dans SI Fig. 26 (exposant aplati par l'extraction du texte, interprétation correcte) ; le circuit d'ajustement n'est que dans MOESM4 (l. 3790) |
| caracterisation | Electrode_GDE | TOF 1,56 s-1 (NaCl, −0,59 V) et 2,27 s-1 (KOH, −0,42 V) | juste | texte principal |
| condition_mesure | Electrode_GDE | tous les Ni actifs, 24,5 % Ni, M 58,69, F 96485, calculé une fois | juste | texte + note SI Fig. 28 |
| caracterisation | Electrode_GDE | formule du rendement faradique | juste | Méthodes |
| condition_mesure | Electrode_GDE | FE mesurée une seule fois | juste | « only performed once » |

## 6. Résultats (134)

| Catégorie | Voie | Élément | Verdict | Raison |
|---|---|---|---|---|
| resultat | Ni-BTA | positions 2θ expérimentales et simulées, d-spacings expérimentaux et simulés, indices de Miller, écarts Δd (SI Tab. 1) (6 ajouts) | juste | valeurs identiques au tableau |
| resultat | Ni-BTA | teneurs C, N, O, H expérimentales, Ni théorique 30,44 % (5) | juste | SI Tab. 2 |
| resultat | Ni-BTA | facteurs R (10,5 / 2,6 / 1,0 %), distances Ni-N 2,03 et Ni-O 2,13 Å, pas de chemin Ni-Ni, résultats après catalyse (Ni-N4O2 : 2,03 et 2,10 ; Ni-N4O1,5 : 2,04 et 2,15) (10) | juste | SI Tab. 3 et 6 ; Tab. 6 recopié fidèlement |
| resultat | Ni-BTA | XPS 398,3 / 399,6 / 531,2 eV ; FTIR 3300, 3300-3500, 1500-1700 cm-1 ; Raman 600-700 cm-1 (7) | juste | texte principal |
| resultat | Ni-BTA | SEIRAS 3240 cm-1 ; pas de signal Ni-OD vers 2900 (calculé 2740,97) (2) | juste | texte principal + SI Tab. 7 |
| resultat | Ni-BTA | potentiel de démarrage 0,70-0,80 V (1) | juste | texte principal |
| resultat | Ni-BTA | sélectivité / Jdisk / JH2O2 pour KOH, NaCl 3,6 %, Na2SO4 (SI Tab. 4) (9) | juste | tableau, valeurs exactes ; plages (0-0,65 V, > 80 % de −0,2 à 0,4 V) diffèrent du texte (0-0,6 V, > 85 % de −0,1 à 0,4 V) : écart de l'article, non annoté |
| resultat | Ni-BTA | sélectivité ≈ 80 % de 0 à 0,5 V dans HClO4 | **faux** | MOESM4 uniquement |
| resultat | Ni-BTA | courant d'anneau 0,005-0,01 mA dans HClO4 | **faux** | MOESM4 uniquement |
| resultat | Ni-BTA | pic XRD 26,4° (fibre de carbone) | **faux** | MOESM4 uniquement |
| resultat | Electrode_GDE | potentiel cathodique −0,25 V ; rendement alcalin 27,0 ; courants > 50 et > 100 mA cm-2 ; triplicats de la désinfection (4) | juste | texte principal et légende Fig. 4g |
| resultat | Electrode_GDE | Rs = 4,53 Ω (KOH) | **faux** | MOESM4 (l. 3795) |
| resultat | Electrode_GDE | Rs = 4,92 Ω (NaCl) | **faux** | MOESM4 (l. 3795) |
| resultat | Electrode_GDE | rendement, FE et stabilité des 3 lignes Ni-BTA du SI Tab. 5 (9) | juste | tableau ; stabilité > 12 h contredit l'essai de 10 h du texte, non annoté |
| resultat | DFT_ORR | énergies de correction et ΔG (U = 0) de *O2, *OOH, *O, *OH pour s-Ni, s-OH-Ni, d-Ni, d-OH-Ni (32) | juste | SI Tab. 8 ; chaque ligne vérifiée, affectation confirmée par ΔG*OOH du texte |
| resultat | DFT_ORR | ΔG*OOH de s-Mn, s-Fe, s-Co, s-Cu, s-Ni, s-OH-Ni, d-Ni, d-OH-Ni, d-OH-Co / Fe / Mn / Cu, optimum 4,23 (13) | juste | texte principal |
| resultat | DFT_ORR | surtensions thermodynamiques 0,02 / 0,35 / 0,26 / 0,60 eV (4) | juste | texte principal, bon ordre |
| resultat | DFT_ORR | espacement 0,35 nm, N-H 1,04 / 1,03 vs 1,02 Å, charge de H, liaison O…H 1,9-2,0 Å, structure électronique double couche (5) | juste | texte principal |
| resultat | DFT_ORR | ΔG*O2 = −0,281 eV, ΔG*O = −0,257 eV, ΔG*OOH = −0,016 eV à 0,695 V | **faux** | MOESM4 (l. 5101-5104) (3 ajouts) |
| resultat | DFT_ORR | ΔG*O − ΔGH2O2 = −0,26 eV | **faux** | MOESM4 (l. 4928) |
| resultat | DFT_ORR | niveau d'énergie de départ de la voie 4e = 4,92 eV | douteux | la citation est dans MOESM4 ; 4,92 figure dans l'équation 9 des Méthodes |
| resultat | DFT_ORR | niveau d'énergie de H2O2 = 3,53 eV | **faux** | MOESM4 (l. 5055) |
| resultat | DFT_ORR | potentiel d'équilibre 2e = 0,695 V | douteux | citation de MOESM4 ; la valeur est dans le texte et les Méthodes |
| resultat | DFT_ORR | stabilité de surface, diagrammes de Pourbaix | **faux** | MOESM4 (l. 3944) |
| resultat | AIMD | barrières 0,33 eV (2e, Ni-O) et 1,21 eV (4e, formation de *O) ; trois simulations indépendantes (3) | juste | texte principal et légende SI Fig. 46 |
| resultat | AIMD | barrière 4e de la version précédente = 1,17 eV | **faux** | MOESM4 (l. 4551) |
| resultat | AIMD | moyennes 0,30 et 1,22 eV | **faux** | MOESM4 (l. 3990-3991) ; la citation parle même de rupture C-O |
| resultat | AIMD | énergie libre 1,18 eV à 0,68 Å et 1,21 eV à 0,88 Å | **faux** | MOESM4 (l. 4555-4557) (2 ajouts) |
| resultat | AIMD | seuil de rupture O-O sur 0,8 Å | **faux** | MOESM4 (l. 4553) |
| resultat | DFT_IR | O-O de Ni-O2 1306,22 ; Ni-OOD 1031,48 ; Ni-OD 2740,97 ; décalage ~180 cm-1 ; liste des 12 fréquences (5) | juste | SI Tab. 7 et sa note (nombres et décalage ; les 12 valeurs sont toutes là) |

## 7. Comparaisons littérature (157), toutes contrôlées contre SI Tab. 4 et 5

| Catégorie | Voie | Élément | Verdict | Raison |
|---|---|---|---|---|
| comparaison | RRDE (Tab. 4) | Pb-OxSy, Co-Pc-S-COFs, ZnO nanosheets, Eley-Rideal ZnO, Mesoporous carbon (ligne KOH), B/N-C, B/N/OH-C, Co-N4 SACs (ligne KOH), Ni-N2O2, CoZn-ZIF (ligne KOH), In-N3S-B (ligne KOH), Co-Pc/O-CNT (ligne KOH), ZnO@ZnO2, h-SnO2, Co-N5 : charge, sélectivité, plage, Jdisk, JH2O2 (64 ajouts) | juste | chaque nombre, signe ~ et > vérifié ; aucune ligne n'est une valeur de Ni-BTA |
| comparaison | RRDE (Tab. 4) | secondes lignes d'électrolyte : Mesoporous carbon PBS (4), Co-N4 K2SO4 (4), CoZn-ZIF PBS (2), In-N3S-B PBS (4), Co-Pc/O-CNT K2SO4 (4) | douteux | valeurs justes, mais le libellé (sélectivité_RRDE) est identique pour les deux électrolytes d'un même catalyseur ; à vérifier dans le JSON que l'électrolyte est porté ailleurs (18 ajouts) |
| comparaison | flux (Tab. 5) | Pb-OxSy, Co-Pc/O-CNT, h-SnO2, Co-N5 SACs, ZnO nanosheets, Eley-Rideal ZnO, Co-N4-P, Zn-N2O2, Pd-SACs, Co-Pc-S-COF, B/N-C, B/N/OH-C, Co-N4, Ni-N2O2, CoZn-ZIF (KOH), In-N3S-B (KOH), ZnO@ZnO2 : charge, rendement, FE, stabilité (68 ajouts) | juste | tous les nombres correspondent ; densités de courant en condition non reprises dans le libellé |
| comparaison | flux (Tab. 5) | CoZn-ZIF PBS (3) et In-N3S-B Na2SO4 (3) | douteux | même absence d'électrolyte dans le libellé (6 ajouts) |
| comparaison | texte principal | désinfectants du commerce ~30 g L-1 (1) | juste | comparaison des auteurs, hors de leurs valeurs |

(Total : 157 = 64 + 68 juste, 24 douteux, 1 hors littérature.)

## 8. Manques restants (paramètres de procédé et conditions de mesure que l'article donne et que la liste n'a pas)

1. Aucun manque de valeur majeur ; la grille existante (JSON) contenait déjà ink, cycles de nettoyage, débits (6 mL/min, 100 mL/min), prétraitement Nafion (durée manquante signalée), colorimétrie, souches ATCC, dyes.
2. Incohérences de l'article non annotées par la passe (annotations ajoutées = 0) : Δd du premier pic (SI Tab. 1 : 6,2512 − 6,1326 = 0,119 Å, le tableau donne 0,049 ; d-spacing simulé à 14,205° devrait être ≈ 6,23 Å) ; essai KOH de 10 h (texte) contre stabilité > 12 h (SI Tab. 5) ; plages de sélectivité du texte et du Tab. 4 ; Na2SO4 0,1 M (Méthodes) contre 0,5 M (SI Fig. 36) ; ΔE0 du Tab. 6 identique (0,15 ± 1,48) à celui de Ni-N4O1,5 avant catalyse.
3. Cases `not_stated` pertinentes absentes pour les calculs : correction de dispersion, polarisation de spin, U de Hubbard, thermostat pour l'AIMD (non dits dans l'article).
4. Conditions de caractérisation sans valeur ajoutée : SEM S4800 et Raman HR800 (déjà dans le JSON), mais aucune condition pour la FTIR ni pour les mesures de la Fig. 4g (temps d'incubation donné dans Méthodes : 16-20 h, présent ailleurs).
5. L'en-tête de la liste annonce `retires_ou_modifies = 3` alors que l'exigence est 0 ; les trois éléments ne figurent pas dans la liste et n'ont pas pu être contrôlés ici.

## Bilan

- Ajouts contrôlés : 415 (tous les paramètres, not_stated, équipements, caractérisations, conditions, résultats, réactifs, étapes, voies et les 157 comparaisons).
- Faux : 26 (3 paramètres, 17 résultats, 5 caractérisations/conditions, 1 not_stated), dont 25 viennent du fichier de réponses aux relecteurs (MOESM4) ; aucun ne vient d'une comparaison en littérature.
- Douteux : 40 (24 comparaisons sans électrolyte dans le libellé, 9 not_stated, 2 résultats, 4 conditions/caractérisations, 1 voie).
