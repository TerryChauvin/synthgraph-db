# Journal — test de complétude PMC9049756

- Liste A : un seul nombre (464, longueur d'onde équivalente de 2,67 eV) ; ajouté comme sortie `optical_band_gap_wavelength` ; 406 nm (gap de Cs3BiBr6) ajouté par symétrie, même phrase.
- Sonde « vide » : écartée, l'atmosphère vacuum est déjà une valeur et la pression est déjà déclarée non citée (aucun niveau de vide dans l'article).
- Sonde XRD/XPS/UV-vis/EDS : l'article ne donne que le nom des appareils ; les conditions restent vides, signalées par une annotation `limite_reproductibilite`, pas de valeur inventée. Seule exception : condition TEM « operating at 200 kV » reportée sur l'entrée TEM/HRTEM de BiOBr_NP (champ conditions jusque-là nul, même phrase que pour les autres voies).
- Sonde « catalyse/adsorption » : faux positif (le mot « conversion » de l'introduction).
- SEM (Carl Zeiss SIGMA, 5 kV) manquait entièrement : ajouté à Cs3Bi2Br9_NP, car la légende Fig. 2c attribue l'image SEM aux nanoplaquettes Cs3Bi2Br9.
- TRPL de Cs3Bi2Br9 : détection à 461 nm tirée du texte (« monitored at 440 nm and 461 nm ... respectively »), 374 nm d'excitation.
- Résultats à plus de 160 °C et jusqu'à 160 °C : rattachés à la voie de base 160 °C faute de voie dédiée, avec un doute qui rappelle la contradiction interne déjà notée. Aucune valeur existante n'est modifiée.
- `comparisons` : valeurs de l'introduction (Yang 4,5 %, Leng ≈ 20 %, PLQY > 90 %, FWHM 12–25 nm). Renvois attribués par le fichier corpus/refs/PMC9049756.txt : cit40, cit41, cit10, cit11 (cit12 aussi cité pour la largeur de bande, un seul retenu, signalé en doute). « bulk Cs3Bi2Br9 » : pas de valeur chiffrée, entrée qualitative rattachée à cit31.
- Le « one of the highest values among solvothermally synthesized Cs3BiBr6 NCs » n'a pas de valeur ni de matériau comparé : non ajouté en comparaison.
- Cases `not_stated` ajoutées : repetitions (voie de base), cooling_mode (refroidissement de base ; étape de chauffage de BiOBr_NP, où aucun refroidissement n'est décrit avant purification). Cherché dans tout le texte et les annexes.
- Aucune figure ouverte : les valeurs numériques sont toutes dans le texte et la Table S1.
