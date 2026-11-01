# Audit du palier 7

Genere le 2026-10-18T11:20:37Z — publications n°301 a n°350 (50 sur 50).

## Volume

- Voies : 424 (155 de base, 269 branches)
- Citations verifiees : 9238 — exactes : 9238 (100.0 %)
- Completude moyenne : 0.72
- Familles : {'composite': 96, 'oxyde': 46, 'autre': 44, 'perovskite': 44, 'MOF': 41, 'nanoparticule_metallique': 31, 'quantum_dot': 28, 'ceramique': 23, 'zeolithe': 20, 'batterie': 12, 'silice_mesoporeuse': 12, 'carbone': 12, 'chalcogenure': 7, 'nitrure': 6, 'materiau_2D': 2}
- Methodes : {'solvothermal synthesis in DMF with HBr acid modulator (2 molar equivalents to ZrCl4), precursors at 0.2 mol L−1': 29, None: 21, 'green synthesis: reduction of AgNO3 by an aqueous Agrimoniae herba extract at room temperature': 19, 'hydrothermal oxidation of pecan nutshell with H2O2 in a 2 L Parr reactor': 14, 'interzeolite conversion from AcT-FAU with DMDMPOH, 180 °C, stainless-steel tube reactor, Na2O/SiO2 = 0,15': 11, 'two-step Stöber-type sol-gel with CTAB micellar template (core growth, then shell growth in the same pot), then calcination': 9, 'impregnation of the 800MA spinel with cobalt nitrate, then calcination at 600 °C': 8, "dépôt à la tournette d'une solution CsI/DMAI/PbI2 dans le DMSO, antisolvant acétate d'éthyle, recuit en deux temps à l'air": 8, 'one-step photo-ultrasonic-assisted reduction of GO/Ag3PO4 QDs (sodium oleate-assisted ion exchange, precipitation under ultrasound, then Xe-lamp and ultrasonic probe in ethanol)': 7, "co-precipitation (acétates de Ba et Mg + paratungstate d'ammonium), évaporation, pré-frittage et recuit à 1150 °C": 7, 'polymérisation par ouverture de cycle de BLG-NCA amorcée par les groupes amine de HAP-NH2, dans le DMF, 48 h sous N2': 7, 'two-step alkali-metal-assisted green-solvent synthesis (aqueous impregnation and annealing, step II)': 6}

## Anomalies ouvertes

| Controle | Bloquant | Avertissement | Info |
|---|---|---|---|
| citation | 0 | 0 | 0 |
| physique | 0 | 0 | 0 |
| chimie | 0 | 0 | 200 |
| coherence | 0 | 0 | 99 |

| id | Gravite | Controle | Article | Cible | Description |
|---|---|---|---|---|---|

Anomalies de niveau info : 299 (table audit_findings).

## Echantillon a relire a la main

Pour chaque ligne : la citation soutient-elle bien cette valeur, pour cette etape et cette branche ? Consigner le resultat dans `audits/palier_007_relecture.md`, avec le controle de stoechiometrie de 5 voies.

| Article | Voie | Etape | Parametre | Valeur | Citation |
|---|---|---|---|---|---|
| PMC4951059 | Bars_Si | 3 | duration_dry | 2.0 min | Wash firing / 440 / 2 / 45 / 860 / 1.5 / Yes / 3 |
| PMC6779780 | BiOBr-g-C3N4-4:1 | 5 | temperature | 160.0 °C | the temperature was kept at 160°C for 12 h |
| PMC3998862 | Bare_AgNPs_citrate | 2 | stirring_speed | vigorous  | After vigorous stirring for 10 minutes |
| PMC8949796 | ColdCryst_PLLA2_85C | 1 | duration | just some minutes  | Cold crystallization for just some minutes at 85 and 95 °C in PLLA2 leads to the α’ form |
| PMC5834413 | R-2.3 | 6 | duration | 5.0 min | After 60 min, the precipitate was centrifuged (5000 rpm) for 5 min |
| PMC5923560 | 22C-SC | 1 | temperature | 22.0 °C | In the first step, 100 mL of ethanol, 8 mL of water, and 4 mL of ammonia solution (catalyst) were mixed and kept at a given temperature (8 °C, 15 °C, 22 °C, 45 °C, or 60 °C) in covered beakers. |
| PMC11904774 | CQD_2.5_180_12h | 7 | pore_size | 0.45 μm | A 47 mm glass vacuum filtration apparatus with 0.45 μm Teflon filter paper was used to separate the mixture that was left in the reactor. |
| PMC8966659 | CsPbBr3-SO4 | 3 | addition_rate | slowly  | Next, a certain amount of K2SO4 aqueous solution was slowly add into the above mixed solution |
| PMC3998862 | AH-AgNPs | 3 | repetitions | thrice  | rinsing the precipitate of AH-AgNPs thrice |
| PMC9034275 | AcT-FAU | 1 | agitation | under stirring  | Then, 5.0 g of H-type FAU and 50 g of 0.70 M H2SO4 aq. were mixed and heated at 75 °C for 4 h under stirring. |
| PMC5834413 | Ag3PO4_QDs | 5 | centrifuge_speed | 5000.0 rpm | After 60 min, the precipitate was centrifuged (5000 rpm) for 5 min |
| PMC9419793 | GO-0 | 3 | stirring_speed | 300.0 rpm | under magnetic stirring (300 rpm) |
| PMC8949796 | PLLA2SBA8 | 5 | pressure | 30.0 bar | at a pressure of 30 bar for 6 min |
| PMC9054805 | RHA1 | 3 | duration | overnight  | It was sieved to obtain uniform size, washed several times with distilled water to remove any contaminants, and dried at 105 °C in oven overnight. |
| PMC3330020 | SGAc | 8 | duration | 4.0 h | The mixture was pelletized and heated in a nitrogen atmosphere at 600°C for 4 h, and then cooled slowly to room temperature. |
| PMC10523092 | CdSe_NPL | 2 | atmosphere | vacuum  | This mixture was degassed under vacuum for 1 h. |
| PMC9036896 | Bulk_gC3N4 | 2 | heating_rate | 10.0 °C min−1 | a ramping rate of 10 °C min−1 and kept at this temperature for 2 h and then continued to heat up to 520 °C at the same heating rate |
| PMC5923560 | 22C-SCMS-C | 11 | duration | overnight  | A portion of the obtained suspension was centrifuged (5 min, 7900 RCF) and the obtained particles were washed with ethanol and dried at 50 °C overnight. |
| PMC8866530 | pCFO_phi1.325_900C | 1 | temperature | room temperature  | stirred at room temperature for 5 min with a magnetic stir bar spinning at 200 rpm |
| PMC8966659 | CsPbBr3_pristine | 5 | atmosphere | argon  | Then, the obtained mixture was ground and calcined at 700 °C for 30 min with a heating rate of 5 °C min−1 in the tubular furnace in argon atmosphere. |
| PMC7759625 | NiMo/Z5 | 5 | temperature | 500.0 °C | finally calcined at 500°C for 4 h |
| PMC11990281 | Ti-SBA-15 | 6 | wash_solvent | deionized water  | The resulting catalyst was filtered, washed with deionized water, and then dried at 100 °C for 24 h. |
| PMC5834413 | Ag3PO4_QDs | 6 | repetitions | several times  | washed several times with hexyl alcohol and absolute ethanol to obtain GO/Ag3PO4 QD composites |
| PMC9147655 | W-TiN | 2 | lens_cuvette_distance | 95–97 mm, exact value adjusted independently for each liquid  | The lens–cuvette distance was 95–97 mm, while the exact value was adjusted independently for each liquid to ensure the highest productivity of the laser ablative synthesis. |
| PMC11931415 | A0 powder | 4 | duration | 24.0 h | the mixed solution was heated at 373 K for 24 h |
| PMC6913939 | Ag@AGG | 2 | duration | 30.0 min | Post 30 min, the NPs formation was observed by visual color change followed by UV-Vis spectroscopic characterization. |
| PMC8966659 | CsPbBr3-F |  | potassium sulfate | replaced by potassium fluoride  | Other passivation ions, such as F-, OH-, Br-, can also be achieved by changing the type of potassium salt (KF, KOH, KBr) under the same experimental conditions. |
| PMC7747735 | 15Co/900MA_regenerated |  | used 15Co/800MA catalyst (route 15Co/800MA) | replaced by used 15Co/900MA catalyst (route 15Co/900MA)  | The regeneration of the used catalyst was performed on 15Co/800MA and 15Co/900MA samples |
| PMC5834413 | Ag3PO4_QDs | 8 | frequency | 20.0 kHz | The ultrasonic irradiation was performed with a high-intensity ultrasonic probe (Xinzhi Co., China, JY92-2D, 10 mm diameter, Ti-horn, 20 kHz) which was placed in the reaction system. |
| PMC9041118 | Nb-LLZO_commercial_sintered | 2 | atmosphere | in air resp. motherpowder  | the sintering procedure (10 h at 1100 °C in air resp. motherpowder) |
