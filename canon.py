"""Vocabulaire canonique des paramètres et des propriétés (point 2 du plan du 28/10/2026).

Les noms bruts écrits par les extracteurs (682 noms de paramètres, 16 577 noms de propriétés) sont
conservés tels quels ; ce module leur associe un nom canonique et un groupe, dans des colonnes séparées
(`parameters.name_canon`, `outcomes.property_canon`, `outcomes.property_group`) et dans la table
`vocabulaire` (nom brut → canonique, groupe, occurrences). Rien n'est déduit sur les valeurs.

    python3 -I canon.py apply     # remplit les colonnes pour toutes les lignes et reconstruit `vocabulaire`
    python3 -I canon.py export    # écrit docs/vocabulaire/{parametres,proprietes}.csv et README.md
    python3 -I canon.py test      # part des occurrences non classées (« autre »)

`load.py` appelle `apply_paper` après chaque chargement. Les règles de propriétés sont celles de l'audit
de contenu (`analyses/audit_contenu.py` les importe d'ici) ; les règles de paramètres remplacent celles de
`analyses/audit_verification.py`. Première règle qui correspond, dans l'ordre : les cas particuliers
précèdent les cas généraux.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# (canonique, groupe, regex sur le nom brut en minuscules, '-' et ' ' remplacés par '_')
PARAM_RULES = [
    ("wash_volume", "chimie", r"(wash|rins).*vol"),
    ("wash_solvent", "chimie", r"wash|rins"),
    ("addition_order", "hydrodynamique", r"addition_order|order_of_addition|addition_mode|addition_sequence|premixed"),
    ("addition_rate", "hydrodynamique", r"addition|injection_rate|injection_time|drip|dropwise|feed_rate|number_of_drops|drop_cast"),
    ("deposition_rate", "hydrodynamique", r"deposition_rate|withdrawal|evaporation_rate|growth_rate|pulse"),
    ("duration", "temporel", r"duration|^time$|_time$|^time_|dwell|hold|interval|delay|residence|storage|aging_time|^age"),
    ("heating_rate", "thermique", r"heating_rate|ramp|heat_rate|heating_speed"),
    ("cooling", "thermique", r"cool|quench"),
    ("drying_mode", "thermique", r"dry"),
    ("temperature", "thermique", r"temp|^t_"),
    ("centrifuge_speed", "hydrodynamique", r"centrifug"),
    ("spin_speed", "hydrodynamique", r"spin"),
    ("milling_speed", "hydrodynamique", r"mill|ball_|rotation_speed|^rotation_rate$|^speed$"),
    ("stirring_speed", "hydrodynamique", r"stir|agitation|shak|rpm|mixing_speed|mixing_rate"),
    ("ph", "chimie", r"(^|_)ph($|_)"),
    ("humidity", "atmosphere", r"humidity"),
    ("atmosphere", "atmosphere", r"atmosph|^gas$|ambient|environment|^air$|glove"),
    ("gas_flow", "atmosphere", r"flow"),
    ("pressure", "atmosphere", r"pressure|vacuum|torr|_bar$|^bar$"),
    ("fill_fraction", "chimie", r"fill"),
    ("power", "energie", r"power|wattage|amplitude|intensity"),
    ("frequency", "energie", r"frequency|_hz$"),
    ("potential_current", "energie", r"potential|voltage|current|bias|scan_rate|charge|c_rate"),
    ("distance", "geometrie", r"distance|gap|spacing"),
    ("irradiation", "energie", r"light|lamp|laser|led|irradi|illumin|wavelength|_uv|^uv|photon|exposure"),
    ("thickness", "geometrie", r"thick|layer"),
    ("repetitions", "procede", r"repetition|cycle|number_of|^n_|repeat|^times$|^count"),
    ("volume_ratio", "chimie", r"volume_ratio|vol_ratio|v/v|solvent_ratio"),
    ("mass_ratio", "chimie", r"mass_ratio|weight_ratio|wt_ratio|w/w|liquid_solid|solid_to|solid_content"),
    ("molar_ratio", "chimie", r"ratio|stoichiometr|equivalent"),
    ("mass", "chimie", r"^mass|_mass$|weight|loading|^amount|dose$"),
    ("concentration", "chimie", r"concentration|molarity|conc|dilution|content$|_dose"),
    ("volume", "chimie", r"volume|^vol_|_vol$"),
    ("dimension", "geometrie", r"size|diameter|dimension|mesh|sieve|cutoff|mwco|area$|length|width|height|^orientation"),
    ("solvent", "chimie", r"solvent|eluent|medium$|dispersant"),
    ("substrate", "geometrie", r"substrate|support$"),
    ("mode", "procede", r"method|mode$|^type$|condition$|^state$|^source$"),
]
PARAM_RE = [(c, g, re.compile(r)) for c, g, r in PARAM_RULES]
PARAM_GROUPS = {c: g for c, g, _ in PARAM_RULES}


def norm_name(n):
    return re.sub(r"[\s\-]+", "_", (n or "").strip().lower())


def canon_param(name):
    """Nom canonique d'un paramètre d'étape (ou 'autre')."""
    n = norm_name(name)
    for c, _, r in PARAM_RE:
        if r.search(n):
            return c
    return "autre"


# propriétés : (canonique, groupe, regex sur le nom brut avec '_' et '-' remplacés par des espaces)
PROP_RULES = [
    ("external_surface_area", "texturale", r"external_surface|\bs_?ext\b"),
    ("micropore_surface_area", "texturale", r"micropore_(area|surface)|\bs_?micro\b"),
    ("micropore_volume", "texturale", r"micropore_vol|\bv_?micro"),
    ("mesopore_volume", "texturale", r"mesopore_vol|\bv_?meso"),
    ("pore_volume_total", "texturale", r"pore_vol|total_pore|\bv_?total|\bvp\b"),
    ("pore_diameter", "texturale", r"pore_(diameter|size|width)|average_pore|mean_pore|bjh"),
    ("BET_surface_area", "texturale", r"^(?!.*(per_|_per_|reduction|electrode|irradiated|cm2)).*(\bbet\b|bet_|\bsbet\b|specific_surface|surface_area|s_bet|\bssa\b|langmuir_surface)"),
    ("phase", "structurale", r"^phase$|crystal_phase|xrd_phase|phase_xrd|product_phase|^phase_|_phase$|secondary_phase|impurity_phase|phase_(identified|purity|composition|assignment)|crystal_structure|space_group|crystal_system|polymorph|crystal_formation"),
    ("lattice_parameter", "structurale", r"^lattice_parameter$|^lattice_constant$|lattice_parameters$"),
    ("crystallinity", "structurale", r"crystallin"),
    ("crystallite_size", "structurale", r"crystallite|scherrer|coherence_length|domain_size|crystal_size|grain_size"),
    ("lattice_parameter_a", "structurale", r"lattice_(parameter|constant)_?a\b|\ba_lattice|cell_(parameter_)?a\b"),
    ("lattice_parameter_b", "structurale", r"lattice_(parameter|constant)_?b\b|cell_(parameter_)?b\b"),
    ("lattice_parameter_c", "structurale", r"lattice_(parameter|constant)_?c\b|cell_(parameter_)?c\b"),
    ("unit_cell_volume", "structurale", r"cell_volume|unit_cell_vol"),
    ("d_spacing", "structurale", r"d[_-]?spacing|interplanar|interlayer|lattice_fringe|fringe"),
    ("xrd_peak_position", "structurale", r"2theta|two_theta|xrd_peak|diffraction_peak|bragg"),
    ("microstrain_dislocation", "structurale", r"microstrain|strain$|dislocation"),
    ("raman_ID_IG", "structurale", r"id/ig|id_ig|i_?d/i_?g|d_g_ratio|raman_ratio|ig/id|id_over_ig"),
    ("raman_band", "structurale", r"raman"),
    ("ftir_band", "structurale", r"ftir|ft_ir|ir_band|infrared|wavenumber"),
    ("xps_binding_energy", "composition", r"xps|binding_energy"),
    ("thickness_layers", "morphologie", r"thickness|layer_number|number_of_layers|monolayer"),
    ("FWHM", "optique", r"fwhm|linewidth|line_width|spectral_width|half_maximum"),
    ("peak_shift", "optique", r"shift|spread"),
    ("IPCE_EQE", "electrochimique", r"ipce|\beqe\b|external_quantum|incident_photon"),
    ("rietveld_fit", "structurale", r"rwp|rexp|rbragg|chi2|\bgof\b|goodness|rietveld|r_factor"),
    ("porosity", "texturale", r"porosity|isotherm"),
    ("kinetics_fit", "fonctionnelle", r"k_obs|pseudo_|kinetic|\br2\b|r_squared|_k1\b|_k2\b|half_life|diffusion_coefficient"),
    ("acidity", "composition", r"acid_site|acidity|\bnh3_tpd|bronsted|lewis"),
    ("band_gap", "optique", r"^(?!.*(diameter|size|from_)).*(band_?gap|optical_gap|\beg\b|tauc)"),
    ("quantum_yield", "optique", r"quantum_yield|plqy|\bqy\b|qy_|photoluminescence_quantum"),
    ("PL_emission_peak", "optique", r"pl_peak|emission_(max|peak|wavelength|maximum|band)|lambda_em|pl_max|pl_wavelength|photoluminescence_peak|em_max|emission_centre|emission_center|^pl_"),
    ("absorption_peak", "optique", r"absorption_(edge|onset|peak|max|band|maximum)|absorbance_peak|\bspr\b|spr_|plasmon|lspr|uv_vis|uv-vis|lambda_max|exciton|absorption_|absorbance"),
    ("PL_lifetime", "optique", r"lifetime|decay_time|\btau"),
    ("transmittance_reflectance", "optique", r"transmitt|reflect"),
    ("refractive_index", "optique", r"refractive"),
    ("conductivity", "electrique", r"conductiv"),
    ("resistivity", "electrique", r"resistiv|sheet_resist|resistance"),
    ("dielectric", "electrique", r"dielectric|permittiv"),
    ("mobility", "electrique", r"mobility"),
    ("retention_stability", "fonctionnelle", r"retain|retention|stability_test|after_\d+_(h|days|cycles)"),
    ("PCE", "electrochimique", r"\bpce\b|pce_|power_conversion|conversion_efficiency|^efficiency$"),
    ("voltage_window_potential", "electrochimique", r"voltage|potential_window|redox_potential|\bocp\b"),
    ("Voc", "electrochimique", r"^(?!.*module).*(^voc|open_circuit)"),
    ("Jsc", "electrochimique", r"^jsc|short_circuit"),
    ("fill_factor", "electrochimique", r"^ff$|fill_factor"),
    ("coulombic_efficiency", "electrochimique", r"coulombic"),
    ("specific_capacitance", "electrochimique", r"capacitance"),
    ("specific_capacity", "electrochimique", r"capacity(?!.*adsorp)|discharge_cap|charge_cap|mah"),
    ("overpotential_tafel", "electrochimique", r"overpotential|tafel|onset_potential"),
    ("adsorption_capacity", "fonctionnelle", r"adsorption|uptake|removal|q_?max|\bqe\b|loading_capacity|release"),
    ("catalytic_performance", "fonctionnelle", r"conversion|selectivity|degradation|rate_constant|turnover|activity|photocatal|evolution|production|completion_time|reduction_time|_in_gas|gas_products"),
    ("magnetic", "fonctionnelle", r"magnetiz|coerciv|saturation|remanen|blocking_temperature|susceptib"),
    ("antibacterial", "fonctionnelle", r"inhibition|\bmic\b|antibact|viability|cytotox|ic50"),
    ("decomposition_temperature", "thermique", r"decomposition|\btd\b|tga|thermal_stability|onset_temperature"),
    ("mass_loss_residue", "thermique", r"mass_loss|weight_loss|residue|char_yield"),
    ("melting_glass_transition", "thermique", r"melting|\btm\b|glass_transition|\btg\b"),
    ("hardness", "mecanique", r"hardness"),
    ("elastic_modulus", "mecanique", r"modulus|young"),
    ("strength", "mecanique", r"strength|stress_at|toughness|elongation"),
    ("density", "physique", r"^density|bulk_density|tap_density|true_density"),
    ("contact_angle", "physique", r"contact_angle|wettab"),
    ("morphology", "morphologie", r"morpholog|^shape$|shape$|structure_sem|structure_tem"),
    ("hydrodynamic_size", "morphologie", r"hydrodynamic|\bdls\b|dls_|z_average|z-average"),
    ("zeta_potential", "morphologie", r"zeta"),
    ("size_dispersity", "morphologie", r"polydispersity|\bpdi\b|size_distribution|dispersity|standard_deviation|std_dev"),
    ("particle_size", "morphologie", r"particle_size|particle_diameter|particle_length|average_(size|diameter)|mean_(size|diameter)|size_tem|tem_size|nanoparticle_size|diameter_tem|^size$|^diameter$|nc_size|nanocrystal_(size|edge)|edge_length|dot_size|core_size|qd_size|sem_size|sphere_(size|diameter)|particle_width|_size$|_diameter$|^length$|^width$|length_range|width_range|aspect_ratio|length_to_diameter|nanowire|nanorod|crystal_(length|diameter|width)|_length$|_width$|size_range|size_sem"),
    ("elemental_composition", "composition", r"_content$|_ratio$|composition|loading$|_fraction$|atomic_percent|weight_percent|\bwt_|\bat_|_at%|_wt%|doping_level|si/al|si_al|ca/p|ca_p|stoichiometry|edx|eds|icp|elemental"),
    ("molecular_weight", "composition", r"molecular_weight|\bmn\b|\bmw\b|mn_|mw_|degree_of_polymer"),
    ("yield", "rendement", r"^yield|_yield$|yield_|^mass_obtained|product_mass"),
    ("visual_appearance", "qualitatif", r"colou?r|appearance|visual|solution_color"),
    # règles ajoutées le 28/10/2026 (point 2 du plan) : elles ne touchent que les noms jusque-là « autre »
    ("lattice_parameter", "structurale", r"lattice|\bd100\b|\ba0\b|interlayer|interplanar|spacing"),
    ("xrd_peak_intensity", "structurale", r"xrd|diffraction|peak_intensity|\bi\d{3}|cpo_index|\(\d{3}\)|^phases"),
    ("impedance_resistance", "electrochimique", r"\brs\b|\brct\b|\brsh\b|\beis\b|resistance|impedance|warburg|charge_transfer"),
    ("roughness", "morphologie", r"roughness|\brms\b|\bra\b"),
    ("adsorption_isotherm_fit", "fonctionnelle", r"langmuir|freundlich|\bqm\b|\bkf\b|\bkl\b|isotherm|pseudo|rate_constant|\bk ?app|\bk1\b|\bk2\b|half_life|t1/2|boundary_layer|intraparticle"),
    ("ph_measured", "composition", r"(^| )ph( |$)"),
    ("catalytic_performance", "fonctionnelle", r"c/c0|ct_over_c0|c_over_c0|degrad|conversion|removal|turnover|\btof\b|\bton\b|inhibition|\bmic\b|activity|separation_factor|permeation|flux|selectiv"),
    ("point_of_zero_charge", "composition", r"pzc|zero_charge|isoelectric"),
    ("density", "physique", r"density"),
    ("activation_energy", "thermique", r"activation_energy|\bea\b|arrhenius"),
    ("magnetic", "fonctionnelle", r"curie|magnet|coerciv|squareness|\bms\b|\bmr\b|\bhc\b|\bilp\b|\bsar\b"),
    ("carrier_transport", "electrique", r"hall|carrier|work_function|mobility|conduction_type|sheet_resistance|seebeck|thermoelectric"),
    ("nmr_signal", "structurale", r"nmr|\bq[34]\b|chemical_shift"),
    ("solution_concentration", "composition", r"supernatant|in_solution|residual|leach|dissolved|removed$|recovery|byproduct|by_product"),
    ("purity", "composition", r"purity|impurit|contaminat"),
    ("yield", "rendement", r"yield|mass_efficiency|atom_economy|e_factor|grafting"),
    ("mechanical", "mecanique", r"stress|strain|tensile|compress|modulus|hardness|toughness|flexur|young"),
    ("thermal_property", "thermique", r"desorption_temperature|\btg\b|melting|glass_transition|thermal_stability|decomposition|onset_temperature|_temperature"),
    ("kinetics_fit", "fonctionnelle", r"_time$|^time_|gelation|onset|induction|reaction_rate|\brate\b"),
    ("product_identity", "qualitatif", r"^product$|^products|formation|status|presence|obtained|observation|identified|species|coexist|reason"),
    ("biological", "fonctionnelle", r"cell_|viabil|antibact|antimicrob|bacteria|dpph|hemoly|cytotox|ic50|\bsbf\b|apatite|\bbio|\bhu\b|ct_number"),
    ("electrochemical_other", "electrochimique", r"potential|voltage|current|plateau|\bcv\b|rrde|ring_|capacity|capacitance|coulomb|retention|rate_capab|energy_density|power_density|\bff\b|champion|\bpce\b|tafel|onset"),
    ("optical", "optique", r"emission|absorb|absorption|excitation|lifetime|decay|\bcie\b|chromaticity|plqe|plqy|quantum|photon|transmit|reflect|haze|wavelength|\bnm\b|huang|energy_separation|hot_carrier|luminesc|fluoresc"),
    ("spectroscopic_band", "structurale", r"band|peak|stretch|vibration|shift|cm-1|binding_energy|xps|raman|ftir|\bir\b|uv|nu_s|nu_as"),
    ("surface_property", "texturale", r"surface|area|pore|porosity|adsorbed_volume|uptake|bet"),
    ("composition_measured", "composition", r"content|at%|wt%|atomic|ratio|stoichiom|dopant|doping|concentration|loading|fraction|\bx\b|si/al|sio2"),
    ("size_dimension", "morphologie", r"size|diameter|thickness|length|width|height|dimension|aspect|platelet|layer|sheet|particle|grain|domain|exfoliation"),
    ("microstructure", "morphologie", r"microstructure|morpholog|alignment|homogeneity|uniform|aggregat|agglomer|dispers|colloid|stable|stability|shape|texture|\bsem\b|\btem\b|\bafm\b|hrtem|saed|solid_state"),
    ("statistic_or_model", "qualitatif", r"\br2\b|r_squared|rank|grade|index|factor|coefficient|parameter|constant|exponent|slope|\bfit|optimum|theoretical|setup"),
]
PROP_RE = [(c, g, re.compile(r.replace("_", " "))) for c, g, r in PROP_RULES]  # les noms sont normalisés : '_' et '-' deviennent des espaces, donc \b fonctionne


def canon_prop(p):
    """(propriété canonique, groupe) d'un nom de propriété de résultat ; ('autre', 'autre') sinon."""
    pl = re.sub(r"[_\-]+", " ", (p or "").lower()).strip()
    for c, g, r in PROP_RE:
        if r.search(pl):
            return c, g
    return "autre", "autre"


# ---------------------------------------------------------------- base

def ensure_columns(con):
    for table, column, decl in (("parameters", "name_canon", "TEXT"), ("outcomes", "property_canon", "TEXT"),
                                ("outcomes", "property_group", "TEXT")):
        if column not in [r[1] for r in con.execute(f"PRAGMA table_info({table})")]:
            con.execute(f"ALTER TABLE {table} ADD COLUMN {column} {decl}")
    con.execute("CREATE TABLE IF NOT EXISTS vocabulaire (kind TEXT NOT NULL, raw TEXT NOT NULL, canon TEXT NOT NULL,"
                " groupe TEXT, n INTEGER NOT NULL, PRIMARY KEY (kind, raw))")


def apply_paper(con, paper_id):
    """Remplit les colonnes canoniques des lignes d'une publication (appelé par load.py)."""
    ensure_columns(con)
    rows = con.execute("SELECT p.id, p.name FROM parameters p JOIN steps s ON p.step_id = s.id"
                       " JOIN synthesis_routes r ON s.route_id = r.id WHERE r.paper_id = ?", (paper_id,)).fetchall()
    con.executemany("UPDATE parameters SET name_canon = ? WHERE id = ?", [(canon_param(n), i) for i, n in rows])
    rows = con.execute("SELECT o.id, o.property FROM outcomes o JOIN synthesis_routes r ON o.route_id = r.id"
                       " WHERE r.paper_id = ?", (paper_id,)).fetchall()
    con.executemany("UPDATE outcomes SET property_canon = ?, property_group = ? WHERE id = ?",
                    [canon_prop(p) + (i,) for i, p in rows])


def rebuild_vocabulaire(con):
    con.execute("DELETE FROM vocabulaire")
    con.executemany("INSERT INTO vocabulaire VALUES ('parameter', ?, ?, ?, ?)",
                    [(n, canon_param(n), PARAM_GROUPS.get(canon_param(n), "autre"), k) for n, k in
                     con.execute("SELECT name, COUNT(*) FROM parameters GROUP BY name")])
    con.executemany("INSERT INTO vocabulaire VALUES ('property', ?, ?, ?, ?)",
                    [(n,) + canon_prop(n) + (k,) for n, k in
                     con.execute("SELECT property, COUNT(*) FROM outcomes GROUP BY property")])


def apply_all(con):
    ensure_columns(con)
    con.executemany("UPDATE parameters SET name_canon = ? WHERE name = ?",
                    [(canon_param(n), n) for (n,) in con.execute("SELECT DISTINCT name FROM parameters")])
    con.executemany("UPDATE outcomes SET property_canon = ?, property_group = ? WHERE property = ?",
                    [canon_prop(p) + (p,) for (p,) in con.execute("SELECT DISTINCT property FROM outcomes")])
    rebuild_vocabulaire(con)
    con.commit()


def coverage(con):
    out = {}
    for kind in ("parameter", "property"):
        tot = con.execute("SELECT SUM(n) FROM vocabulaire WHERE kind=?", (kind,)).fetchone()[0] or 0
        autre = con.execute("SELECT SUM(n) FROM vocabulaire WHERE kind=? AND canon='autre'", (kind,)).fetchone()[0] or 0
        ncanon = con.execute("SELECT COUNT(DISTINCT canon) FROM vocabulaire WHERE kind=? AND canon<>'autre'", (kind,)).fetchone()[0]
        nraw = con.execute("SELECT COUNT(*) FROM vocabulaire WHERE kind=?", (kind,)).fetchone()[0]
        out[kind] = dict(occurrences=tot, autre=autre, pct_autre=round(100.0 * autre / max(tot, 1), 1), canoniques=ncanon, bruts=nraw)
    return out


def export(con):
    d = ROOT / "docs" / "vocabulaire"
    d.mkdir(parents=True, exist_ok=True)
    for kind, fn in (("parameter", "parametres.csv"), ("property", "proprietes.csv")):
        with open(d / fn, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["canonique", "groupe", "nom_brut", "occurrences"])
            w.writerows(con.execute("SELECT canon, groupe, raw, n FROM vocabulaire WHERE kind=? ORDER BY canon, n DESC, raw", (kind,)))
    cov = coverage(con)
    lines = ["# Vocabulaire canonique", "",
             "Table de correspondance entre les noms écrits par les extracteurs (conservés tels quels dans la base) et un nom",
             "canonique qui rend les paramètres et les propriétés comparables d'une publication à l'autre. Règles : `canon.py`",
             "(première règle qui correspond). Colonnes en base : `parameters.name_canon`, `outcomes.property_canon`,",
             "`outcomes.property_group`, table `vocabulaire`. Regénérer : `python3 -I canon.py apply && python3 -I canon.py export`.", "",
             "| | Occurrences | Noms bruts | Canoniques | Non classées (« autre ») |", "|---|---|---|---|---|"]
    for kind, lab in (("parameter", "Paramètres d'étape"), ("property", "Propriétés mesurées")):
        c = cov[kind]
        lines.append(f"| {lab} | {c['occurrences']} | {c['bruts']} | {c['canoniques']} | {c['autre']} ({c['pct_autre']} %) |")
    for kind, lab in (("parameter", "Paramètres"), ("property", "Propriétés")):
        lines += ["", f"## {lab} : canoniques par occurrences", "", "| Canonique | Groupe | Occurrences | Noms bruts | Exemples |", "|---|---|---|---|---|"]
        for c, g, n, k, ex in con.execute(
                "SELECT canon, groupe, SUM(n), COUNT(*), GROUP_CONCAT(raw, ', ') FROM (SELECT * FROM vocabulaire WHERE kind=? ORDER BY n DESC)"
                " GROUP BY canon ORDER BY SUM(n) DESC", (kind,)):
            ex = ", ".join(ex.split(", ")[:5])
            lines.append(f"| `{c}` | {g} | {n} | {k} | {ex} |")
    (d / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return cov


def main():
    sys.path.insert(0, str(ROOT))
    import db
    con = db.connect()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "test"
    if cmd == "apply":
        apply_all(con)
        print(coverage(con))
    elif cmd == "export":
        ensure_columns(con)
        print(export(con))
    else:
        ensure_columns(con)
        rebuild_vocabulaire(con)
        print(coverage(con))
        for kind in ("parameter", "property"):
            print(kind, "non classés :", [tuple(r) for r in con.execute("SELECT raw, n FROM vocabulaire WHERE kind=? AND canon='autre' ORDER BY n DESC LIMIT 40", (kind,))])
        con.rollback()


if __name__ == "__main__":
    main()
