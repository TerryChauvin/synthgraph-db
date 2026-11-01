# Audit du palier 9

Genere le 2026-10-24T23:57:16Z — publications n°401 a n°450 (50 sur 50).

## Volume

- Voies : 566 (143 de base, 423 branches)
- Citations verifiees : 9719 — exactes : 9719 (100.0 %)
- Completude moyenne : 0.73
- Familles : {'composite': 105, 'chalcogenure': 105, 'nanoparticule_metallique': 62, 'carbone': 57, 'oxyde': 53, 'autre': 48, 'zeolithe': 32, 'silice_mesoporeuse': 28, 'MOF': 26, 'perovskite': 18, 'quantum_dot': 12, 'materiau_2D': 10, 'batterie': 6, 'ceramique': 4}
- Methodes : {None: 89, 'colloidal synthesis, one-pot heat-up of Cp*2Ba, Zr(NEtMe)4 and CS2 in oleylamine': 51, 'hot injection of a chalcogenourea into cadmium acetate and oleic acid in 1-octadecene at 195 °C': 27, 'one-pot hydrothermal carbonization (sodium citrate, glycine, MnCl2) at 180 °C for 10 h': 26, 'sol-gel condensation of sodium metasilicate on a cetylpyridinium chloride micellar template, Ni salt added in situ, 313 K, pH 5 with NH3·H2O, calcination 923 K': 19, 'post-fabrication hot plate annealing in air': 13, 'green synthesis: reduction of AgNO3 by an aqueous extract of herbal medicine residue under ultrasonic radiation': 12, 'thermally assisted oxidative precipitation in water with citrate, 90 °C, open to air': 11, 'one-step solvothermal method (170 °C, 5.5 h) in absolute ethanol': 10, 'one-step solvothermal synthesis (150 °C, 8 h, stainless steel autoclave with Teflon-lined flask)': 10, 'green synthesis by reduction of AgNO3 with Citrus limon zest extract at 60 °C': 9, 'one-pot hydrolytic sol–gel at room temperature in 1-propanol (Ti(OBu)4 modified by catechol, then water)': 9}

## Anomalies ouvertes

| Controle | Bloquant | Avertissement | Info |
|---|---|---|---|
| citation | 0 | 0 | 0 |
| physique | 0 | 0 | 0 |
| chimie | 0 | 0 | 305 |
| coherence | 0 | 0 | 118 |

| id | Gravite | Controle | Article | Cible | Description |
|---|---|---|---|---|---|

Anomalies de niveau info : 423 (table audit_findings).

## Echantillon a relire a la main

Pour chaque ligne : la citation soutient-elle bien cette valeur, pour cette etape et cette branche ? Consigner le resultat dans `audits/palier_009_relecture.md`, avec le controle de stoechiometrie de 5 voies.

| Article | Voie | Etape | Parametre | Valeur | Citation |
|---|---|---|---|---|---|
| PMC10511489 | ZeoliteT | 8 | temperature | 393.0 K | After homogenized by vigorous magnetic stirring for 6 h and statically aged for 12 h, the milk-like precursor was transferred to stainless steel autoclave and kept at 353 K for 4 days and 393 K for 4 days under static hydrothermal crystallization. |
| PMC8830207 | T-dop0.05 | 3 | temperature | room temperature  | In a typical hydrolytic sol–gel procedure carried out at room temperature |
| PMC7503313 | O-CDs_RT | 8 | repetitions | double centrifugation cycle  | The procedure consists on double centrifugation cycle, each at 9000 rpm for 20 min at RT. |
| PMC12693316 | BPA-MSNs | 17 | atmosphere | vacuum  | vacuum-dried |
| PMC5456199 | NZ040 | 6 | repetitions | several times  | The products (a mixture of zeolite A crystals and MC) were washed several times with deionized (DI) water, followed by centrifugation at 6000 rpm for 10 min. |
| PMC11648698 | BZS_HU | 4 | heating_tape_power | 30-50% power (110-120V source)  | heating tape was typically set between 30-50% power (110-120V source) |
| PMC9064236 | Anneal_F_150C_120min |  | Device_A | replaced by Device_F  | F: FTO/am-TiOx/π-SnS/CdS/i-ZnO/ITO 150 oC, 120 min 200 3.50 31 0.1 0.22 |
| PMC9078281 | M-NG_K+ |  | MnCl2 solution | replaced by K+ salt (not specified)  | were also prepared using the similar method as Mn(ii)-NGQDs, except for using different metal salts |
| PMC10708100 | CdZnS | 6 | wash_solvent | anhydrous ethanol and deionized water  | After completion, the reaction mixture was cooled to room temperature, filtered, and the resulting Cd0.5Zn0.5S precipitate was washed several times with anhydrous ethanol and deionized water. |
| PMC7931434 | TiO2 | 7 | duration | 24.0 h | dried at 100 °C for 24 h |
| PMC10249076 | YIG_solgel | 2 | temperature | 80.0 °C | The solution is stirred for 30 min at 80 °C. |
| PMC10511489 | ZeoliteT | 8 | duration | 4.0 days | After homogenized by vigorous magnetic stirring for 6 h and statically aged for 12 h, the milk-like precursor was transferred to stainless steel autoclave and kept at 353 K for 4 days and 393 K for 4 days under static hydrothermal crystallization. |
| PMC7503313 | O-CDs_70C_180mM_40min |  | hydrochloric acid (HCl) | replaced by dichloromethane  | quenching the reaction after 20 and 40 min, respectively, by adding immiscible CH2Cl2 in order to extract the O-CDs by centrifugation |
| PMC8830207 | T-cat0.1C | 1 | molar_ratio | Ti/catechol/ligand = 1:0.1:0.3  | with a molar ratio of Ti/catechol/ligand = 1:0.1:0.3 |
| PMC10059734 | MnZnFe-DC7 | 8 | temperature | room temperature  | After cooling down to room temperature |
| PMC7931434 | Mo_1 | 10 | duration | 2.0 h | calcination in air at 500 °C for 2 h with a temperature ramp of 2.5 °C min–1 to remove the surfactant |
| PMC9042205 | Biosurfactant | 3 | pressure | 15.0 atm | The prepared broth media was wrapped with aluminium foil for sterilization (autoclave at 121 °C for 20 min at 15 atm). |
| PMC10511489 | S12 | 4 | duration | 4.0 h | 12 / NaOH / 333 / 4 / 353 / 48 / CHA |
| PMC8830207 | T-dop0.05p | 1 | temperature | room temperature  | In a typical hydrolytic sol–gel procedure carried out at room temperature |
| PMC8693586 | pH10_2h_ratio_1to2 |  | RBM extract (route RBM_extract) | RBM extract : AgNO3 = 1:2  | Waste extract:AgNO3 2:1 1:1 1:2 1:3 1:5 Size/nm 49.6±0.8 32.3±1.8 35.8±1.2 54.8±3.9 53.4±3.3 |
| PMC10148794 | NC5 | 8 | duration | 10.0 min | Then, the mixture was centrifuged at a Relative Centrifugal Force (RCF) of 11,627 × g for 10 min. |
| PMC11648698 | S1_run04 | 15 | temperature | 340.0 °C | 4 Cp*2Ba + Zr(NEtMe)4 + CS2 0.85:1:62. 5 and 1:1:62.5 One-pot, heat-up, 340 °C, 3 h No, CS2 dried under UHP Ar flow 0.04 4 Glas-Col, 25 mL (Fabric) Amorphous n/a |
| PMC7503313 | O-CDs_70C_180mM_20min | 2 | temperature | 70.0 °C | (a) Pictures of the vials containing the CPC initial solutions after the addition of 90, 180 and 360 mM NaOH solutions at 70 °C, at different reaction times; |
| PMC3833402 | CdS-HDA-150 | 3 | duration | 1.0 h | The solution was heated to 150°C and stabilized at this temperature for 1 h. |
| PMC9369949 | CIM-80_10 |  | urea | 10.0 mmol | CIM-80_10 / 10 mmol / 27 |
| PMC5887100 | ACD-BI |  | HATU | replaced by 1-benzylimidazole  | HATU (0.5 mmol) or other precursors (0.5 mmol benzyltriethylammonium chloride, 0.5 mmol 1-benzylimidazole, 1 mL diisopropylamine) were added with stirring at room temperature to poly(tetrafluoroethylene) (Teflon) lined flasks (50 mL) containing 30 mL solvent. |
| PMC7563594 | GO-EDA | 2 | concentration_tris | 10.0 mM | A mixed solution containing 2 g/L dopamine hydrochloride and 10 mM of Tris(hydroxymethyl)aminomethane acetic acid was prepared, and the support PES ultrafiltration membrane was immersed in the mixed solution for 48 h. |
| PMC9227472 | AgNPs_2mM | 1 | concentration | 2.0 mM | mixing each concentration of AgNO3 solution (2, 1, 0.5 mM) with 9 mL of Citrus limon zest extract |
| PMC11648698 | S1_run03 | 11 | molar_ratio | Ba:Zr:S 1:1 Ba/Zr  | 3 Cp*2Ba + Zr(NEtMe)4 + MePT + CS2 1:1 Ba/Zr One-pot, heat-up, 330 °C%, 15 min-1 hr Yes 0.24 1 Glas-Col, 25 mL (Fabric) SP-BZS# No |
| PMC6804187 | [3]- | 4 | wash_solvent | cold water and brine solution  | washed with cold water and brine solution |
