# PMC8125317 — critique scientifique (journal de décisions)

- Bilan urée/Zn : écrit 5 Zn2+ + 2 CO2 + 8 H2O → Zn5(OH)6(CO3)2 + 10 H+, donc 1 urée hydrolysée par Zn suffit ; l'urée à 5 par Zn est un excès usuel, pas un problème. Formule hydrozincite supposée (l'article dit seulement « LZHC »).
- Volume de solution absent : la pression du flacon (≈ 3,6 bar de vapeur + 0,7 à 3,4 bar de CO2) est calculée sur une hypothèse de 10 mL dans 35 mL, signalée comme telle ; statut `reserve`, pas `probleme`.
- Cinétique de l'urée à 140 °C : constante non trouvée (Shaw et Bordeaux 1955 identifié par citation secondaire, sans DOI). Je n'ai pas inventé de valeur ; la complétude en 15 min reste « plausible, non démontrée ».
- « Pyrolyse incomplète » à 300 °C : gardée en `reserve` (Kanari 2004 : décomposition notable dès 200 °C, une étape). À 500 °C, l'affirmation de la section 3.2 est jugée peu plausible pour le cœur du solide ; j'ai préféré l'hypothèse de carbonates/OH de surface réadsorbés (ATR à l'air, 38 m²/g), sans la poser comme certaine : une ATG trancherait.
- `probleme` 1 : Raman « HeNe ... 532 nm » et plage « 70 to 17,800 nm » ; contradiction interne, longueur d'onde d'excitation réelle inconnue.
- `probleme` 2 : E2High/E2Low inversés (98 et 437 cm−1). Source Cuscó 2007 retenue pour l'attribution, mais ses valeurs numériques n'ont pas été lues dans le texte intégral (consigné dans sources_not_found).
- Éclairement UV-C : 3 × 27 W UV-C (fiche OSRAM copiée par un tiers) sur 533 mm à 27,5 cm → ≈ 8,8 mW/cm² au plus contre 35 annoncés. Gardé en `reserve` et non en `probleme` : la puissance UV-C vient d'une copie secondaire de la fiche et la géométrie (réflecteur) n'est pas décrite.
- Flux de photons : soleil ≤ 8×10^15 contre lampe 4,5×10^16 photons cm−2 s−1 pour des k voisins ; j'en déduis seulement que la vitesse n'est pas limitée par les photons ou que l'éclairement est surestimé, sans trancher.
- Points à 15 min lus sur figure (±0,03) nettement au-dessus de exp(−15k) pour les trois échantillons : ajustement avec ordonnée libre probable ; `reserve` (cinétique), pas d'erreur de calcul des auteurs à 60 min (1 − exp(−60k) reproduit 91/92/>99 %).
- PL jaune 596 nm : BC→Oi (2,28 eV) donnerait 544 nm, seule Zni→Oi (2,06 eV, 602 nm) colle ; `reserve`. Origine des niveaux attribuée « vraisemblablement » à Lin et al. 2001, valeur non lue.
- « Blue shift » pour 3,25 → 3,26 eV (1,2 nm) : jugé non significatif, effet de queue de défauts plutôt que de gap.
- « Millimolaire » pour une RhB à 8,35 µM : mot faux mais régime de premier ordre justement valable à faible concentration ; pas de conséquence.
- Branches ZnO-500 et ZnO-700 traitées comme voies (chimie thermique différente) avec leurs propres calculs (BET → diamètre/épaisseur équivalents, k).
- Comparaison base : seule PMC3497326 (7–16 m²/g) est un point de comparaison BET utile ; aucune autre voie hydrozincite + calcination.
- Recherches web : 9 (plus 4 lectures directes échouées) ; plusieurs domaines (hal, intechopen, run.unl.pt, osram.com) injoignables en lecture directe, contenus pris dans les extraits de recherche seulement.
