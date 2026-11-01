# PMC9063869 — critique scientifique (journal de décisions)

- Rampe de chauffe : 7 °C/min jusqu'à 120 °C puis 10 °C/min donnent 17,6 min avant le palier de 160 °C ; l'échantillon « 1 min » a donc chauffé 18,6 min (7,9 min au-dessus de 100 °C). Classé `probleme` car les auteurs concluent « within 1 min ».
- Rendement 0,033 kg/L : 40 mmol P / 6 × 1004,6 g/mol = 6,70 g pour 200 mL = 33,5 g/L, soit le maximum stœchiométrique ; aucune masse pesée dans le texte. Classé `probleme` (valeur très probablement calculée, non mesurée).
- Ammoniaque : 8 H+ libérés par HAP ; pour tenir pH 10 (pKa NH4+ 9,25) il faut ~6,6 NH3 par H+ libéré, soit ≈ 26 mL d'ammoniaque à 25 % à 0,4 mol/L. Gardé en `reserve` (quantité absente) ; si ce volume est réel, le rendement annoncé dépasse le maximum (29,6 g/L).
- FTIR : 2925/2856 cm−1 = élongations C–H de CH2 (valeur de manuel IR), pas HCO3−/H2PO4− ; noté `probleme` parce que la conclusion « cristallisation incomplète » en dépend. Assignations 962 (ν1), 603/564 (ν4), 633 (libration OH) confirmées par recherche web (extraits de tables, sources non nommées), donc basis `chimie_generale`.
- Formule MTT du Methods = taux d'inhibition ; les barres à ~100 % ne peuvent venir que de Atreated/Acontrol. `probleme` (erreur des auteurs), sans conséquence sur la conclusion de biocompatibilité.
- Comparaisons TG / DRX 990 °C / FTIR faites contre la poudre commerciale Nanjing Epry (lecture de l'extraction : HAPH = poudre commerciale) : témoin qui change tout ; `probleme` sur la généralisation à « la méthode hydrothermale ».
- Équations des auteurs recomptées : « 2Ca5(PO4)2OH » non équilibrée (P 4 contre 6) ; l'équation CDHA + H2O → HAP + H3PO4 est équilibrée mais contredit le β-TCP observé ; l'équation HAP → 3 TCP + CaO est celle d'une HAP stœchiométrique. Gardé en `reserve` avec Raynaud 2002.
- Raie β-TCP d = 2,8809 Å → 2θ = 31,04° avec λ = 0,154184 nm : discriminante contre HAP (211) à 2,81 Å ; `ok` implicite dans les calculs.
- Solubilité Na2HPO4 : Fisher 77 g/L à 20 °C (0,54 mol/L) contre PubChem ≥ 100 mg/mL ; les deux cités, explication des auteurs jugée plausible (`reserve`).
- Raynaud et al. 2002 retenu pour le comportement thermique des apatites déficientes ; son DOI n'a pas été trouvé (Crossref bloqué), cité par la bibliographie de Minerals 2021. Landi 2000 (formule de cristallinité) trouvé mais non lu : non cité.
- Koutsopoulos 2002 (10.1002/jbm.10280) trouvé mais tables non lues : non cité comme appui.
- Kappe 2006 (Chimia) cité pour les deux mécanismes de chauffage micro-ondes (dipolaire et ionique) ; le mécanisme des auteurs (rotation dipolaire seule) jugé `a_revoir` car le milieu est un électrolyte à 0,1–0,8 mol/L, et la rampe du témoin hydrothermal (7 °C/min) est presque celle du micro-ondes.
- NIST WebBook et PMC injoignables (DNS) depuis ce poste : pressions de vapeur de l'eau (0,62 MPa à 160 °C, 1,00 MPa à 180 °C) données comme valeurs de manuel.
- Témoins : verdict `invérifiable` (pH, lavage, appareil non décrits) ; seul HAP_MH_direct ne change qu'une variable.
- 9 recherches web, 2 lectures de pages échouées.
