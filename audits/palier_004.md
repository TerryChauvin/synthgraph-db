# Audit du palier 4

Genere le 2026-10-14T17:01:25Z — publications n°151 a n°200 (50 sur 50).

## Volume

- Voies : 515 (140 de base, 375 branches)
- Citations verifiees : 9920 — exactes : 9920 (100.0 %)
- Completude moyenne : 0.70
- Familles : {'composite': 133, 'autre': 96, 'oxyde': 62, 'nanoparticule_metallique': 47, 'perovskite': 37, 'carbone': 30, 'MOF': 26, 'batterie': 25, 'chalcogenure': 16, 'zeolithe': 13, 'materiau_2D': 13, 'quantum_dot': 6, 'phosphure': 4, 'silice_mesoporeuse': 3, 'carbure': 2, 'nitrure': 2}
- Methodes : {None: 29, 'sol-gel': 25, 'ring-opening copolymerization in bulk, TBAB 5 mol%, 80 °C, 24 h (criblage du Table S1)': 17, 'carbonization of γ-CD-MOF/GO under Ar, HCl etching, vacuum drying': 14, 'microwave-assisted synthesis induced by graphene oxide, methanol as antisolvent (GO concentration 3 g/L chosen as the reference)': 12, 'adsorption/precipitation of Au and Pd hydroxide precursor on TiO2 at pH 10, then reduction under H2 at 150 °C': 11, 'ring-opening copolymerization in bulk, catalysed by tetrabutylammonium bromide, 80 °C, 24 h, argon': 10, 'hydrothermal (121 °C, 2 h) from zinc acetate and NaOH, no ionic liquid': 10, 'drop coating of a SDS dispersion of the solid on a glassy carbon electrode, stabilized with Nafion': 10, 'coating of silicon nanoparticles by PAN precipitated with water, then pre-oxidation and carbonization': 9, 'ultrasound-assisted liquid-phase exfoliation of etched Ti3AlC2 in NMP': 9, 'ultrasound-assisted liquid-phase exfoliation of graphite in NMP': 9}

## Anomalies ouvertes

| Controle | Bloquant | Avertissement | Info |
|---|---|---|---|
| citation | 0 | 0 | 0 |
| physique | 0 | 0 | 0 |
| chimie | 0 | 0 | 297 |
| coherence | 0 | 0 | 170 |

| id | Gravite | Controle | Article | Cible | Description |
|---|---|---|---|---|---|

Anomalies de niveau info : 467 (table audit_findings).

## Echantillon a relire a la main

Pour chaque ligne : la citation soutient-elle bien cette valeur, pour cette etape et cette branche ? Consigner le resultat dans `audits/palier_004_relecture.md`, avec le controle de stoechiometrie de 5 voies.

| Article | Voie | Etape | Parametre | Valeur | Citation |
|---|---|---|---|---|---|
| PMC5407272 | Reaction_1a_to_2a | 2 | atmosphere | Ar (1 atm)  | the mixture was stirred at 160 °C under Ar (1 atm) |
| PMC6222835 | HOOC-[PECH-MIM]Cl | 9 | duration | 24.0 h | the mixture was stirred at 80 °C for 24 h |
| PMC4957122 | mBeta | 3 | duration | 6.0 h | the solution containing 0.033 g NaOH, 0.17 g NaAlO2 and 2 mL distilled water was slowly added into the resultant solution and further stirred at 313 K for 6 h. |
| PMC5364236 | AgNP-180-Results | 1 | reaction_vessel | Schlenk flask immersed in a silicon oil bath  | The powder was heated by immersing a Schlenk flask into silicon oil bath and allowed to react for 20 min |
| PMC12455581 | ZIF-67 | 1 | temperature | room temperature  | stirred at room temperature |
| PMC12195685 | MCM-RHA | 7 | temperature | 60.0 °C | dried at 60 °C overnight |
| PMC10489885 | MCSe-400 | 2 | duration | 5.0 min | The electrochemical deposition process was performed at −0.7 V for 5 min to obtain a MnCo selenide electrode sample, which was dried and denoted MCSe-0. |
| PMC9034142 | SERS_Ag3Au | 3 | duration | 10.0 min | the nanoparticles sol was first centrifuged at 6000 rpm for 10 min in an ultracentrifuge several times to concentrate the colloids, and remove the excess reactants and supernatant |
| PMC9370708 | F-1 | 2 | film_thickness | 0.2 mm | The mixture was suction filtered through a 0.1 μm filter membrane into a film with a thickness of 0.2 mm. |
| PMC9689030 | TiO2-PANI_composite | 9 | spin_speed | 3000.0 rpm | Then, the samples were deposited on an ITO substrate with a spin speed of 3000 rpm for 60 s. |
| PMC12455581 | ZIF-67 : Ni (1 : 2) | 3 | duration | 1.0 h | The mixtures were stirred at room temperature for 1 hour |
| PMC6403542 | PEDOT:PSS (neat) | 1 | probe_sonication_duration | 1.0 min | the polymer (0.05 mg for each sample) was dissolved in 5 mL of DMSO by heating at 50 °C and stirring at 300 rpm for 5 min combined with probe sonication for 1 min |
| PMC9057918 | MoS2(1-x)Se2x | 5 | temperature_furnace_growth | 850.0 °C | When the furnace reached 850 °C, the argon gas carries the vaporized selenium, sulfur and molybdenum trioxide to the substrates during the deposition process. |
| PMC6403542 | P/HDI-GO 6 (5.0 wt%) |  | HDI-GO 6 | 2.5 mg | the desired amount (0.25, 0.5, 1.0, 2.5, and 5.0 mg) of HDI-GO was dispersed in 2.5 mL of DMSO by probe sonication for 1 min at a 40% amplitude followed by ultrasonication in an ultrasonic bath for 1 h to create a homogeneous suspension of HDI-GO nanosheets in the solvent |
| PMC9418622 | White_3560K |  | MAPbBr3-2L | 0.52 ratio of integrated emission intensities (red = 1) | 3560 / 0.36 / 0.52 / 0.58 / 1 / 93.33 / 0.40 / 0.39 |
| PMC9370708 | DNF | 6 | wash_solvent | deionized water  | The samples were repeatedly centrifuged and washed with deionized water at 9000 rpm until the supernatant was neutral. |
| PMC11556383 | NZF2C2B | 2 | duration | 6.0 h | This was followed by calcination at 1200 °C for 6 hours. |
| PMC10625068 | Carbon_600 | 1 | atmosphere | Ar gas  | An appropriate amount of precursors γ-CD-MOF/GO was heated to 300, 400, 500, 600, and 700°C at a heating rate of 1°C·min-1 in an atmosphere of Ar gas, and held at that temperature for 2 h, before being allowed to naturally cool to room temperature. |
| PMC6403542 | HDI-GO 1 | 2 | sonication_method | ultrasonicated  | The dispersion was ultrasonicated for 2 h |
| PMC9046778 | ZnS-0 | 6 | wash_solvent | deionized water  | The product was collected after centrifuging and washing several times with deionized water. |
| PMC5448492 | FeSi0-xerogel | 1 | duration | 3.0 hours | An initial molar ratio of 255 EtOH: 4 TEOS: x Fe(NO3)3.9H2O: 9H2O2: 40H2O was mixed and vigorously stirred for 3 hours in an ice-cooled bath. |
| PMC12195685 | GCE-Fe/MCM-41(5) |  | MCM-41 (route MCM-41) | replaced by Fe/MCM-41(5) (route Fe/MCM-41(5))  | The electrochemical study of MCM-41, MCM-RHA, and Fe-based catalysts was carried out by a drop coating method of glassy carbon electrodes described as follows. |
| PMC8132056 | TiO2_pristine_600C | 1 | atmosphere | air  | after calcination at 600 °C in air for 3 h |
| PMC4957122 | mBeta | 7 | temperature | 383.0 K | Subsequently, the products were washed with distilled water and dried at 383 K for 12 h. |
| PMC5448492 | FeSi0-500 | 2 | pressure | atmospheric conditions  | Sol samples were dried in a temperature-controlled oven at 60 °C at atmospheric conditions to form a xerogel. |
| PMC8717584 | Cu-TiO2/GO | 3 | ph | 12.0  | The mixture was adjusted to pH 12 using 1 M sodium hydroxide solution, followed by the addition of 1.79 mg sodium borohydride. |
| PMC9425827 | Z-HPMC-0.24 | 11 | duration | 5.0 h | Zeolite particles were then dried at 100 °C and calcined at 550 °C for 5 h. |
| PMC8132056 | PSC_12F |  | TiO2_pristine | replaced by TiO2_12F  | We incorporated F‐TiO2 nanocrystals as novel ETLs |
| PMC6403542 | P/GO (10 wt%) |  | HDI-GO 6 | replaced by raw GO  | For comparative purposes, reference samples containing neat PEDOT:PSS (0 wt % HDI-GO) and 5.0 mg of raw GO (10 wt % GO) were prepared in a similar way. |
| PMC5448492 | FeSi0-500 | 1 | temperature | ice-cooled bath  | An initial molar ratio of 255 EtOH: 4 TEOS: x Fe(NO3)3.9H2O: 9H2O2: 40H2O was mixed and vigorously stirred for 3 hours in an ice-cooled bath. |
