# Vocabulaire canonique

Table de correspondance entre les noms écrits par les extracteurs (conservés tels quels dans la base) et un nom
canonique qui rend les paramètres et les propriétés comparables d'une publication à l'autre. Règles : `canon.py`
(première règle qui correspond). Colonnes en base : `parameters.name_canon`, `outcomes.property_canon`,
`outcomes.property_group`, table `vocabulaire`. Regénérer : `python3 -I canon.py apply && python3 -I canon.py export`.

| | Occurrences | Noms bruts | Canoniques | Non classées (« autre ») |
|---|---|---|---|---|
| Paramètres d'étape | 12731 | 682 | 37 | 111 (0.9 %) |
| Propriétés mesurées | 39350 | 16577 | 95 | 3597 (9.1 %) |

## Paramètres : canoniques par occurrences

| Canonique | Groupe | Occurrences | Noms bruts | Exemples |
|---|---|---|---|---|
| `duration` | temporel | 3854 | 62 | duration, spin_duration, duration_cooling, duration_dry, duration_hold |
| `temperature` | thermique | 3179 | 40 | temperature, temperature_final, temperature_initial, temperature_start, temperature_average |
| `atmosphere` | atmosphere | 786 | 5 | atmosphere, atmosphere_vacuum, gas, glovebox_atmosphere, glovebox_moisture_oxygen |
| `wash_solvent` | chimie | 689 | 9 | wash_solvent, wash_additive, wash_interval, delay_before_rinse, final_wash_ph |
| `molar_ratio` | chimie | 647 | 102 | concentration, molar_ratio, concentration_agno3, ratio, mixing_ratio |
| `volume` | chimie | 535 | 54 | volume, volume_teos, volume_hf, volume_sda_oh_solution, total_volume |
| `repetitions` | procede | 465 | 8 | repetitions, cycles, microwave_cycles, number_of_cells, number_of_portions |
| `stirring_speed` | hydrodynamique | 280 | 5 | stirring_speed, agitation, stirring, mixing_speed, stirring_mode |
| `centrifuge_speed` | hydrodynamique | 274 | 2 | centrifuge_speed, centrifuge_speed_mixture |
| `addition_rate` | hydrodynamique | 240 | 10 | addition_rate, addition_time, delay_before_addition, number_of_drops, number_of_drop_casts |
| `ph` | chimie | 195 | 11 | ph, final_ph, ph_endpoint, acid_solution_ph, endpoint_ph |
| `dimension` | geometrie | 189 | 54 | pore_size, diameter, particle_size, membrane_cutoff, mesh_size |
| `pressure` | atmosphere | 151 | 9 | pressure, atomizer_inlet_gas_pressure, base_pressure, compaction_pressure, distillation_pressure |
| `heating_rate` | thermique | 139 | 4 | heating_rate, heating_rate_final, heating_rate_initial, ramp_up |
| `thickness` | geometrie | 116 | 29 | thickness, film_thickness, layer_thickness, thickness_al, pellet_thickness |
| `autre` | autre | 111 | 80 | uptake_rate, added_radioactivity, bars_per_group, composition, endpoint |
| `spin_speed` | hydrodynamique | 96 | 9 | spin_speed, spin_speed_step1, spin_speed_step2, spin_coating_times, spin_speed_stage_1 |
| `irradiation` | energie | 80 | 14 | wavelength, light_exposure, light_source, illumination, led_luminosity |
| `gas_flow` | atmosphere | 76 | 12 | gas_flow, flow_rate, gas_flow_hydrogen, gas_flow_borazine, gas_flow_direction |
| `power` | energie | 75 | 8 | power, amplitude, acoustic_power_density, lamp_power, heating_tape_power |
| `mass` | chimie | 72 | 38 | extract_dose, mass, mass_loading, molecular_weight_cutoff, active_material_loading |
| `mass_ratio` | chimie | 68 | 13 | mass_ratio, weight_ratio, liquid_solid_ratio, solid_content, g_c3n4_zno_weight_ratio |
| `potential_current` | energie | 60 | 21 | voltage, current_density, led_current, led_voltage, potential |
| `cooling` | thermique | 52 | 7 | cooling_rate, cooling_mode, cooling_medium, cooling_method, cooling |
| `volume_ratio` | chimie | 43 | 4 | volume_ratio, solvent_ratio, mass_volume_ratio, solvent_volume_ratio |
| `milling_speed` | hydrodynamique | 39 | 10 | milling_speed, rotation_speed, rotation_rate, ball_to_powder_mass_ratio, ball_to_powder_ratio |
| `frequency` | energie | 33 | 1 | frequency |
| `addition_order` | hydrodynamique | 32 | 4 | addition_mode, premixed_component, addition_order, order_of_addition |
| `distance` | geometrie | 31 | 12 | distance, led_diagonal_distance, collecting_distance, needle_collector_distance, tip_collector_distance |
| `deposition_rate` | hydrodynamique | 28 | 14 | deposition_rate, evaporation_rate_mai, evaporation_rate_pbi2, pulse_duration, withdrawal_speed |
| `solvent` | chimie | 27 | 5 | solvent, dispersion_solvent, eluent, dialysis_medium, dispersion_medium |
| `drying_mode` | thermique | 17 | 3 | drying_method, drying_mode, drying_gas |
| `mode` | procede | 15 | 7 | method, deposition_method, end_condition, transfer_method, oscillation_method |
| `concentration` | chimie | 11 | 7 | dilution_factor, nitrogen_content, binder_content, cnt_content, ha_content |
| `wash_volume` | chimie | 7 | 1 | wash_volume |
| `substrate` | geometrie | 7 | 4 | substrate_orientation, substrate, position_substrate, substrate_cleaning |
| `humidity` | atmosphere | 6 | 2 | relative_humidity, humidity |
| `fill_fraction` | chimie | 6 | 2 | fill_fraction, filler_loading |

## Propriétés : canoniques par occurrences

| Canonique | Groupe | Occurrences | Noms bruts | Exemples |
|---|---|---|---|---|
| `autre` | autre | 3597 | 2209 | solvent_viscosity, MOF_mass, PSI, R2IPD, R2k1 |
| `elemental_composition` | composition | 2625 | 1048 | carbon_content, anatase_content, c_a_ratio, polytype_3C_content, polytype_6H_content |
| `catalytic_performance` | fonctionnelle | 2396 | 1352 | photocatalytic_degradation_efficiency_PDE_60min, Al_conversion, Si_conversion, H2_evolution, sorbitol_conversion_TableS1 |
| `adsorption_capacity` | fonctionnelle | 1771 | 1337 | TC_removal_efficiency_pH7_120ppm_1gL_120min, CO2_uptake_298K_1bar, MB_removal_efficiency, COD_removal, sonocatalytic_color_removal_Metanil_Yellow |
| `kinetics_fit` | fonctionnelle | 1685 | 990 | k_obs, pseudo_second_order_R2, pseudo_first_order_R2, Li_diffusion_coefficient, pseudo_first_order_k1 |
| `particle_size` | morphologie | 1469 | 457 | particle_size, average_particle_size, particle_size_TEM, particle_size_SEM, average_sphere_diameter |
| `phase` | structurale | 1086 | 109 | phase, xrd_phase, XRD_phase, phase_purity, product_phase_pXRD |
| `xps_binding_energy` | composition | 1027 | 509 | XPS_C_content, XPS_O_content, XPS_N_content, XPS_C1s_C-C, XPS_C1s_C=O |
| `specific_capacity` | electrochimique | 1022 | 503 | calcium_ion_exchange_capacity, discharge_capacity_1C, initial_discharge_capacity_0.1C, initial_discharge_capacity, MB_sorption_capacity_qeq |
| `PL_emission_peak` | optique | 986 | 379 | PL_peak_wavelength, emission_maximum, PL_emission_peak, PL_lifetime, PL_decay_lifetime |
| `yield` | rendement | 954 | 522 | yield, product_mass, reaction_mass_efficiency, SiC_yield, yield_1_4_sorbitan_TableS1 |
| `absorption_peak` | optique | 869 | 325 | uv_vis_peak_absorbance, absorption_edge, SPR_peak_absorbance, SPR_peak_wavelength, absorbance_440nm_at_4.5h |
| `morphology` | morphologie | 836 | 99 | morphology, morphology_SEM, surface_morphology, morphology_TEM, TEM_morphology |
| `crystallite_size` | structurale | 796 | 159 | crystallite_size, crystal_size, average_crystallite_size, crystallite_size_Scherrer, crystallite_size_XRD |
| `BET_surface_area` | texturale | 766 | 57 | BET_surface_area, S_BET, bet_surface_area, specific_surface_area, BET_specific_surface_area |
| `antibacterial` | fonctionnelle | 747 | 438 | cell_viability_NIH-3T3_24h, cytotoxicity_NIH-3T3_24h, zone_of_inhibition_E_coli, cell_viability, cell_viability_percent_of_control |
| `composition_measured` | composition | 619 | 355 | x, theoretical_nanoplatelet_concentration, AAS_concentration, BAS_to_SAS_ratio_IPATPD, Si1_content_organosilane_silica |
| `retention_stability` | fonctionnelle | 611 | 322 | capacity_retention_10_cycles_0.5C, C5h RhB photoconversion after 5 h of UV irradiation, capacity_retention_100_cycles, capacity_retention_50_cycles_0.5C, particle_size_DLS_after_16_days |
| `decomposition_temperature` | thermique | 564 | 244 | TGA_total_weight_loss, TGA_BDC_experimental_coordination_number, TGA_T10_10pct_weight_loss, TGA_Ti_2pct_weight_loss, TGA_Tmax_stage_I |
| `adsorption_isotherm_fit` | fonctionnelle | 561 | 314 | Freundlich_KF, CIPD boundary layer constant, Freundlich_kF_T25, Freundlich_n_T25, Langmuir_b_T25 |
| `pore_diameter` | texturale | 491 | 94 | pore_diameter, average_pore_diameter, pore_size, average_pore_size, BJH_desorption_pore_diameter |
| `pore_volume_total` | texturale | 477 | 47 | total_pore_volume, pore_volume, V_total, BJH_desorption_pore_volume, BJH_pore_volume |
| `visual_appearance` | qualitatif | 459 | 121 | visual_assessment, appearance, solution_color, color, pellet_color |
| `electrochemical_other` | electrochimique | 432 | 214 | charge_plateau_potential, CV_oxidation_peak, FF_champion, nitrogen_adsorbed_volume_plateau, CV_peak_separation_dE |
| `band_gap` | optique | 418 | 65 | band_gap, optical_band_gap, bandgap, band_gap_Eg, band_gap_energy |
| `xrd_peak_intensity` | structurale | 388 | 151 | XRD_intensity_ratio_002_100, CPO_index_(002)/(011), CPO_index_(002)/(112), I003_I104, XRD_I111_7.3deg_area |
| `spectroscopic_band` | structurale | 372 | 227 | relative_intensity_broad_peak_RelI_BP, COO_sym_stretch_nu_s, COO_asym_stretch_nu_as, COO_stretch_separation_delta_nu, main_PL_band |
| `quantum_yield` | optique | 355 | 52 | quantum_yield, PLQY, PLQY_toluene, PL_quantum_yield, pl_qy |
| `thickness_layers` | morphologie | 353 | 139 | film_thickness, XRD_c-axis_(002)_to_(100)_thickness_ratio, layer_number, pellet_thickness, coating_thickness |
| `crystallinity` | structurale | 333 | 57 | crystallinity, relative_crystallinity, relative_crystallinity_FAU_RCFAU, crystallinity_degree_Xc, crystallinity_index_CI |
| `solution_concentration` | composition | 323 | 198 | supernatant_Al_concentration, supernatant_Si_concentration, carbon_in_solution, Ca2+_removed, carbon_recovery_in_byproducts |
| `hydrodynamic_size` | morphologie | 319 | 77 | dls_average_size, composite_size_dls, hydrodynamic_diameter, z_average, hydrodynamic_size_DLS |
| `xrd_peak_position` | structurale | 317 | 141 | XRD_020_2theta_PEDOT_PSS, xrd_peak_position_2theta_101, XRD_111_peak_position_2theta, XRD_peak_position_2theta, XRD_002_peak_2theta |
| `raman_band` | structurale | 310 | 95 | Raman_peak_position, Raman_IG_ID_ratio, Raman_frequency_difference_dk, Raman_antisymmetric_CC_stretching, Raman_single_CC_stretching |
| `acidity` | composition | 305 | 64 | Bronsted_Lewis_ratio, Bronsted_acid_loading, Bronsted_acid_site_density, NH3_acid_site_loading, total_acid_site_density |
| `impedance_resistance` | electrochimique | 293 | 107 | Rs, Rsh, EIS_Rct, Rct, EIS_Rs |
| `magnetic` | fonctionnelle | 290 | 78 | saturation_magnetization, saturation_magnetization_300K, blocking_temperature, relative_volumetric_susceptibility, saturation_magnetization_380K |
| `density` | physique | 278 | 88 | tap_density, bulk_density, pellet_density, relative_density, xray_density |
| `microstructure` | morphologie | 277 | 146 | colloidally_stable, SEM_aqueous_face, solid_state, alignment_FESEM, microstructure |
| `lattice_parameter` | structurale | 277 | 82 | lattice_parameter, h-GaN_lattice_a, h-GaN_lattice_c, c-TiN_lattice_a, lattice_a |
| `ftir_band` | structurale | 274 | 143 | BSA_adsorption_FTIR, SBF_21d_FTIR, FTIR_SiOH_band, FTIR_SiOSi_asym_stretch_band, FTIR_SiOSi_sym_stretch_band |
| `biological` | fonctionnelle | 266 | 135 | SBF_21d_SEM_coverage, SBF_21d_SEM_globules, CT_number_HU, DPPH_scavenging_20min, HTL_HHV_of_biocrude_270C |
| `FWHM` | optique | 261 | 54 | FWHM, PL_FWHM, fwhm, anatase_FWHM, XRD_FWHM |
| `statistic_or_model` | qualitatif | 247 | 149 | grey_relational_grade, grey_relational_grade_rank, tunability_automated_setup, fit_RMSE, hierarchy_factor_HF |
| `optical` | optique | 244 | 124 | Huang_Rhys_factor, X1_X2_energy_separation, cie_1931_coordinates, PLQE, integrated_emission_intensity_300K_266nm |
| `resistivity` | electrique | 238 | 75 | charge_transfer_resistance_Rct, sheet_resistance, charge_transfer_resistance, Hall_resistivity, series_resistance_Rs |
| `surface_property` | texturale | 235 | 126 | surface_area_per_mole_of_silica, microporous_area, V_pore, vsur global surface reaction, photoactive_area |
| `size_dispersity` | morphologie | 234 | 56 | dispersity, polydispersity_index, pdi, sphere_diameter_standard_deviation, PDI |
| `rietveld_fit` | structurale | 226 | 56 | Rietveld_Rwp, Rwp, Rietveld_chi2, GOF, Rietveld_Rp |
| `strength` | mecanique | 210 | 55 | tensile_strength, toughness, elongation_at_break, compressive_strength_SN_ratio, compressive_strength_mean_as_reported |
| `product_identity` | qualitatif | 203 | 73 | product, SAED_no_pattern_reason_per_authors, SAED_pattern_obtained, c-GaN_presence, formation_status |
| `lattice_parameter_a` | structurale | 202 | 24 | lattice_parameter_a, lattice_constant_a, Ag_fcc_cell_parameter_a, CoFe2O4_cell_parameter_a, lattice_parameter_a_Rietveld |
| `size_dimension` | morphologie | 198 | 107 | exfoliation_efficiency, extrapolation_length_xi_of_LC_solution, average_NP_size_FE-SEM, AFM_top_ten_height_Sz, QD_diameter_from_optical_gap |
| `specific_capacitance` | electrochimique | 194 | 79 | specific_capacitance_20Ag-1, specific_capacitance_0.5Ag-1, double_layer_capacitance_Cdl, specific_capacitance_at_1_A_g-1, specific_capacitance_at_1.0_A_g-1 |
| `microstrain_dislocation` | structurale | 194 | 31 | dislocation_density, micro_strain, microstrain, Ag_fcc_microstrain, CoFe2O4_microstrain |
| `PL_lifetime` | optique | 192 | 80 | average_PL_lifetime, average_fluorescence_lifetime, Mn_PL_decay_time_vs_x_1.6nm_core, TRPL_tau1, TRPL_tau2 |
| `zeta_potential` | morphologie | 179 | 25 | zeta_potential, zeta_potential_pH7, zeta_potential_water, zeta_potential_in_ethanol, MSN_zeta_potential |
| `ph_measured` | composition | 169 | 103 | dispersion_pH_after_synthesis, pH_initial_mesure, pH_isoelectric_point, pH_measured, optimum_pH |
| `d_spacing` | structurale | 166 | 79 | XRD_d_spacing_002, d_spacing, lattice_fringe_spacing, XRD_d_spacing, d_spacing_interlamellar |
| `micropore_volume` | texturale | 151 | 13 | micropore_volume, V_micro, V_micro_DR, micropore_volume_t-plot, micropore_volume_DR_N2 |
| `mass_loss_residue` | thermique | 151 | 79 | carbon_in_residue, coke_weight_loss_TG_deactivated_catalyst, mass_loss_PBS_12h_crosslinked, mass_loss_PBS_12h_uncrosslinked, mass_loss_PBS_24h_crosslinked |
| `porosity` | texturale | 149 | 72 | porosity, isotherm_type, N2_isotherm_type, Pb_uptake_at_C0_200_mg_L_last_isotherm_point, isotherm |
| `roughness` | morphologie | 147 | 49 | surface_roughness_Ra, surface_roughness, AFM_RMS_roughness, rms_surface_roughness, AFM_average_roughness_Sa |
| `voltage_window_potential` | electrochimique | 130 | 83 | cell_voltage_window, turn_on_voltage, CV_redox_potential_difference, forming_voltage, potential_window |
| `hardness` | mecanique | 128 | 21 | grey_relational_coefficient_hardness, hardness_SN_ratio, hardness_mean_as_reported, hardness_reading_1, hardness_reading_2 |
| `peak_shift` | optique | 123 | 65 | 29Si_MAS_NMR_Q3_shift_TableS3, 29Si_MAS_NMR_Q4_shift_TableS3, PL_peak_shift_with_dopant_concentration, SPR_lambda_max_shift_5_to_45min, PL_peak_shift_with_Ag_Na_ratio |
| `lattice_parameter_c` | structurale | 121 | 13 | lattice_parameter_c, lattice_constant_c, lattice_parameter_c_Rietveld, XRD_lattice_parameter_c, unit_cell_c |
| `PCE` | electrochimique | 119 | 32 | PCE, efficiency, PCE_best, PCE_champion, PCE_layers_series |
| `unit_cell_volume` | structurale | 116 | 10 | unit_cell_volume, cell_volume, anatase_cell_volume, rietveld_cell_volume, 3D_ED_cell_volume |
| `thermal_property` | thermique | 111 | 64 | NH3_desorption_temperature_T1, NH3_desorption_temperature_T2, DTA_exothermic_peak_temperature_AP_mixture, DTG_peak_temperatures, desorption_peak_temperature_5th_dehydrogenation |
| `molecular_weight` | composition | 111 | 45 | Mn_SEC, Mn_PL_intensity_normalized_vs_x_1.6nm_core, Mn, Mn_PL_main_band, Ni_Mn_molar_ratio_titration |
| `coulombic_efficiency` | electrochimique | 108 | 45 | initial_coulombic_efficiency, initial_coulombic_efficiency_0.05C, first_cycle_coulombic_efficiency, LIB_initial_coulombic_efficiency, coulombic_efficiency |
| `mesopore_volume` | texturale | 98 | 9 | mesopore_volume, V_meso, mesopore_volume_Vmeso, mesopore_volume_DFT, mesopore_volume_fraction |
| `external_surface_area` | texturale | 97 | 10 | S_ext, external_surface_area, external_surface_area_t-plot, S_EXT_external_surface_area, S_EXT_over_S_INT |
| `melting_glass_transition` | thermique | 93 | 43 | Li_TM_molar_ratio_final, DSC_transition_temperature_Tm, TG_mass_attenuation_150-300C, Tg_cooling, Tg_first_heating |
| `conductivity` | electrique | 89 | 34 | electrical_conductivity, room_temperature_ionic_conductivity, conductivity, bulk_ionic_conductivity_298K, total_ionic_conductivity_298K |
| `Jsc` | electrochimique | 89 | 24 | Jsc, Jsc_champion, Jsc_average_60_devices, JSC_mean_10_devices, Jsc_average_20_devices |
| `carrier_transport` | electrique | 85 | 34 | Hall_carrier_concentration, Hall_conduction_type, hot_carrier_energy_loss_rate, work_function, Williamson_Hall_fit_intercept |
| `mobility` | electrique | 84 | 32 | Hall_mobility, field_effect_mobility, carrier_mobility_before_annealing, electron_mobility, FET_mobility |
| `Voc` | electrochimique | 84 | 20 | Voc, Voc_average_60_devices, Voc_champion, VOC_mean_10_devices, Voc_average_20_devices |
| `IPCE_EQE` | electrochimique | 78 | 36 | EQE_max, peak_EQE_at_-10_V, peak_EQE_at_-15_V, peak_EQE_at_-20_V, peak_EQE_at_-5_V |
| `raman_ID_IG` | structurale | 77 | 10 | Raman_ID_IG, Raman_ID_IG_ratio, ID_IG_ratio, raman_ID_IG, Raman_ID/IG |
| `activation_energy` | thermique | 67 | 24 | activation_energy, Ea_Friedman, Ea_Kissinger, Ea_alpha_trend_Friedman_Fig11, Ea_reference_previous_studies_cited_by_authors |
| `mechanical` | mecanique | 65 | 16 | tensile_stress_max, structural_strain_dd_d_x1e-4, strain_SSP, strain_UDEDM, strain_UDM |
| `transmittance_reflectance` | optique | 64 | 22 | transmittance_550nm, transmittance_633nm, DRS_reflectance_trend, reflectance_visible_plateau, reflectivity_edge |
| `contact_angle` | physique | 54 | 18 | water_contact_angle, water_contact_angle_crosslinked, water_contact_angle_final_about_5_s, water_contact_angle_initial, water_contact_angle_uncrosslinked |
| `fill_factor` | electrochimique | 53 | 16 | FF, fill_factor, fill_factor_FF, DSSC_fill_factor_sample_A1, DSSC_fill_factor_sample_A2 |
| `overpotential_tafel` | electrochimique | 52 | 19 | Tafel_slope, OER_overpotential_at_10_mA_cm-2, normalized_anodic_current_density_at_overpotential_592_mV, overpotential_eta10, overpotential_eta50 |
| `micropore_surface_area` | texturale | 50 | 7 | S_micro, micropore_surface_area_t_plot, S_INT_micropore_surface_area, micropore_area_t-plot, Smicro |
| `purity` | composition | 42 | 13 | pc_purity, Li2CO3_impurity, radiochemical_purity_RCP, rock_salt_impurity_intensity_ratio_I(43.6°)/I(44.3°), impurity |
| `lattice_parameter_b` | structurale | 40 | 6 | lattice_parameter_b, lattice_constant_b, unit_cell_b, 3D_ED_cell_b, unit_cell_b_Table1 |
| `elastic_modulus` | mecanique | 40 | 11 | Youngs_modulus, Young_modulus_E, Youngs_modulus_E, loss_modulus_G_double_prime_at_100_rad_s, storage_modulus_G_prime_at_100_rad_s |
| `nmr_signal` | structurale | 33 | 14 | Q3_area_29Si_NMR, Q4_area_29Si_NMR, 29Si_NMR, oxidized_carbon_content_NMR, static_7Li_NMR_motional_narrowing_temperature_range |
| `point_of_zero_charge` | composition | 28 | 7 | pHPZC, point_of_zero_charge, pHpzc, point_of_zero_charge_pHpzc, isoelectric_point |
| `dielectric` | electrique | 21 | 10 | relative_permittivity_25C_automated_sensor, dielectric_loss_100kHz (tan δ), dielectric_constant_of_solvent_mixture, dielectric_loss_tangent_5-7_GHz, real_permittivity |
| `refractive_index` | optique | 16 | 6 | refractive_index_633nm, refractive_index_n_trend, effective_refractive_index_632.8nm_EP, effective_refractive_index_632.8nm_SAR, refractive_index |
