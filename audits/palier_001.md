# Audit du palier 1

Genere le 2026-10-13T13:45:21Z — publications n°1 a n°50 (50 sur 50).

## Volume

- Voies : 609 (124 de base, 485 branches)
- Citations verifiees : 8712 — exactes : 8712 (100.0 %)
- Completude moyenne : 0.74
- Familles : {'composite': 121, 'perovskite': 62, 'MOF': 61, 'autre': 60, 'batterie': 54, 'oxyde': 50, 'zeolithe': 40, 'materiau_2D': 37, 'nanoparticule_metallique': 30, 'chalcogenure': 26, 'carbone': 17, 'ceramique': 17, 'carbure': 14, 'quantum_dot': 14, 'silice_mesoporeuse': 6}
- Methodes : {None: 147, 'one-step hydrothermal synthesis (gel formation, aging, crystallization) from diatomite and aluminum hydroxide in NaOH solution': 40, 'aqueous-phase glucose reduction with hexadecylamine capping (one-pot, oil bath)': 18, 'extrusion-dripping ionic gelation of sodium alginate in CaCl2 aqueous solution': 17, 'hydrothermal synthesis (point central du plan composite centré, 130 °C, 7 h, pH 7)': 16, 'self-limiting chemical vapor deposition in a tube furnace from MoCl5 and sulfur powders under Ar flow': 15, 'room temperature, open atmosphere anti-solvent precipitation in ethyl acetate with oleylamine and oleic acid as capping ligands': 15, 'coulée en solution de MOF-808 et de copolyimide 6FDD dans du THF, évaporation lente puis recuit': 13, 'sonochemical synthesis in water with a direct immersion ultrasonic probe (70% amplitude, 1 h), thioacetamide as sulfur precursor': 12, 'catalyst-free vapor–solid growth from silicon and carbon black powders in a home-built low-pressure CVD tube furnace under argon': 12, 'acid-assisted hydrothermal treatment in HCl aqueous solution at 150 °C for 24 h': 11, 'soft-templating synthesis in a surfactant-stabilized oil-in-water microemulsion (n-hexane/HFS), ultrasonication then low-temperature synthesis at 30 °C': 11}

## Anomalies ouvertes

| Controle | Bloquant | Avertissement | Info |
|---|---|---|---|
| citation | 0 | 0 | 0 |
| physique | 0 | 0 | 0 |
| chimie | 0 | 0 | 383 |
| coherence | 0 | 0 | 85 |

| id | Gravite | Controle | Article | Cible | Description |
|---|---|---|---|---|---|

Anomalies de niveau info : 468 (table audit_findings).

## Echantillon a relire a la main

Pour chaque ligne : la citation soutient-elle bien cette valeur, pour cette etape et cette branche ? Consigner le resultat dans `audits/palier_001_relecture.md`, avec le controle de stoechiometrie de 5 voies.

| Article | Voie | Etape | Parametre | Valeur | Citation |
|---|---|---|---|---|---|
| PMC10906077 | FAPbBr3_purified_R-MBA | 7 | duration | 5.0 min | the mixture was stirred mildly for 5 min at room temperature and then centrifuged at 7500 rpm for 5 min to precipitate the aggregated particles; the supernatant was collected. |
| PMC4102124 | pure_Cu_precursor |  | copper(II) chloride dihydrate | 600.0 μL | (h) 600 μL of CuCl2 |
| PMC9026548 | THF_P10-S-M10_fast | 5 | evaporation_rate | fast: solvent allowed to evaporate without any preventive cover  | (i) the solvent was allowed to evaporate without any preventive cover |
| PMC5122874 | EtOAc_4h | 4 | duration | 4.0 hours | 4 hours Quantum dots + nanoplates + nanobars |
| PMC10326808 | HFS_hexane_13vv |  | n-hexane | 13.0 v/v % | Further increases in oil concentration to 13 v/v % (6 mL), 17 v/v % (8 mL), and 23 v/v % (12 mL) were also studied (Figure S5) |
| PMC3659320 | MoS2-1L-sapphire | 2 | substrate | sapphire  | Fig. 1 a–b show optical images of the MoS2 monolayer and bilayer films grown on sapphire substrates. |
| PMC2964502 | TiO2_HCl_protocol | 2 | duration | 0.5 h | with stirring for 0.5 h |
| PMC10906077 | FAPbBr3_x25 | 8 | duration | 5.0 min | After cooling to room temperature, the solution was centrifuged at 7500 rpm for 5 min to remove unreacted ligands and 1-ODE. |
| PMC10529665 | Alg/Z5A/Cur/CS | 5 | collecting_distance | those optimized in the preliminary experiment  | The process parameters used were those optimized in the preliminary experiment. |
| PMC10326808 | HFS_hexane_3vv |  | n-hexane | 3.0 v/v % | the studied n-hexane concentrations include 3, 5, 9, 17, and 23 v/v %, respectively |
| PMC7352182 | CuS/C-120@PANI | 4 | potential_window | from −0.3 to 0.6 V  | which was performed in a three-electrode system from −0.3 to 0.6 V at 10 mV−1 for 20 cycles. |
| PMC9026548 | THF_P5-S-M0_slow | 5 | heating_rate | 5.0 °C/min | using a heating rate of 5 °C/min |
| PMC2897037 | SiC-1350C | 6 | temperature | 1350.0 °C | Figure 7a–7f show SEM images of the nanostructures synthesized at 1,250, 1,300, 1,350, 1,400, 1,450 and 1,500°C, respectively. |
| PMC6025012 | ZeoX-opt | 8 | wash_solvent | deionized water  | the samples were removed from the reactor, filtered, and washed with deionized water until the pH of the filtrate reached 6–7 |
| PMC10131834 | WLED_remixed |  | WCDs (route WCDs) | replaced by BCDs (0.30 mg), GCDs (0.50 mg), YCDs (0.20 mg), and RCDs (0.30 mg)  | The WCDs/PVP complex solution was prepared from isolated multicolor CDs as follows: BCDs (0.30 mg), GCDs (0.50 mg), YCDs (0.20 mg), and RCDs (0.30 mg) were mixed in PVP ethanol solution (0.25 g mL−1, 120 µL) under ultrasonic treatment for 5 min to obtain WCDs/PVP complex solution. |
| PMC4639899 | graphene_FET_on_hBN | 4 | power | 50.0 W | reactive oxygen etching tool (Plasma-therm—50 W for 10 s) |
| PMC5376314 | Co1 | 5 | duration | 24 h (nickel paragraph, taken over by the reference « as described above »)  | The black precipitate obtained after 1 h of sonication was handled as described above. |
| PMC10529665 | Alg/Z5A/Cur | 2 | volume | 10.0 mL | added to 10 mL of alginate solution |
| PMC6199062 | Sb2S3-150 | 1 | duration | 15.0 min | 3 mmol l-cysteine was dissolved in 30 mL distilled water under magnetic stirring for 15 min to obtain a colorless solution |
| PMC9026548 | CHCl3_P7-L-M30 | 5 | evaporation_rate | not stated  | Based on the promising results using chloroform in Section 3.2, a screening study for chloroform-based MMMs was performed to be able to identify the optimal synthesis parameters for the MMM fabrication. |
| PMC9026548 | THF_P3-S-M10_fast | 5 | evaporation_rate | fast: solvent allowed to evaporate without any preventive cover  | (i) the solvent was allowed to evaporate without any preventive cover |
| PMC10326808 | ZIF-8Lit | 3 | duration | 2.0 h | the synthesis time was increased to 2 h |
| PMC6297875 | NVP_800C_10h_2.5 | 3 | volume | 30.0 mL | After stirring for 2 h at room temperature, 1.5 g mL−1 PVP solution (Solution II, 30 mL) was obtained. |
| PMC5376314 | Ni10 |  | thioacetamide | replaced by sodium thiosulfate pentahydrate  | Ni10 / Na2S2O3 ∙ 5H2O / 1:1 / - / 60 / 70 / NiS, Ni3S4 / 24 (NiS) / 5.0 (NiS) |
| PMC10326808 | HFS_hexane_5vv | 4 | duration | a range of synthesis times (0.5, 1, 1.5, 2, 6, 14, and 24 h)  | maintained at 30 °C and 500 rpm for a range of synthesis times (0.5, 1, 1.5, 2, 6, 14, and 24 h) |
| PMC10326808 | Out_swapped_order_HFS_doubled |  | HFS | doubling the amount of surfactant  | Another attempt was made to stabilize the ME by doubling the amount of surfactant. |
| PMC4735866 | AgNPs_AloeVera | 5 | temperature | room temperature  | After cooling at room temperature |
| PMC8136633 | HAp-run2 | 3 | temperature | 160.0 °C | 2 / 160 / 10 / 10 / 89.75 / 92.79 / 45.48 / 47.00 / 86.13 / 86.82 |
| PMC7352182 | CuS/C-120 | 4 | temperature | 120.0 °C | The experimental temperatures were 80 °C, 120 °C, and 160 °C. |
| PMC7578857 | CsPbBr3 | 3 | volume_precursor | 1.0 mL | 1 mL precursor solution was added into toluene (10 mL) under vigorous stirring for 1 min at room temperature |
