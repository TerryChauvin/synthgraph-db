# PMC11541765 — critique scientifique (Opus)

- Verdict « douteuse / non_reproductible » pour ZnOTF-3L : aucune quantité du sol, et le renvoi CR42 (refs : Wahab et al., Ceram. Int. 2023, verre SiO2–P2O5 dopé Er) ne traite pas du ZnO ; mis en `probleme` car le protocole n'est récupérable nulle part.
- Bragg recalculé avec λ = 1,54056 Å : a = 3,247 Å, c = 5,195 Å, conforme à JCPDS 36-1451 et à PMC7962968 (a = 3,2467 Å) ; DRX jugée cohérente, sans taille de Scherrer pourtant annoncée.
- Fig. 3c lue (corpus/fig/…Fig3_HTML.jpg) : extrapolations ≈ 3,24–3,25 eV (3 couches) et ≈ 3,20–3,21 eV (6 couches). Le texte dit 3,19/3,21 eV et « blue shift » : `probleme` (sens inversé ; la Fig. 3a et la phrase « absorption edge … increased » vont aussi vers le rouge). Lecture à ± 0,02 eV.
- 75 % contre 60 % : régression sur les 7 couples (A664 ; C) du laser → C = 11,55·A + 2,68 µM. L'ordonnée à l'origine explique tout l'écart (73 % sur l'absorbance) ; la pente donne ε ≈ 8,7×10^4, cohérente avec 8,2×10^4 (revue Environ. Chem. Lett. 2025). `probleme` porté sur l'étalonnage, pas sur l'arithmétique.
- Tableau 4 recalculé exactement (42,1 % / 3,80e-4 ; 60,0 % / 6,37e-4 ; 60,0 % / 5,09e-3) : les k sont des k à deux points ; l'équation 4 n'est cohérente qu'avec un signe moins. Laissé en `reserve` (coquille), avec la cinétique non d'ordre 1 sous laser (0,031 min−1 sur 0–10 min, plateau ensuite).
- Dimères : fraction calculée avec K2 = 3,97×10^3 L/mol (revue 2025, citant Fernández-Pérez & Marbán) → ≈ 10 % en dimère à 14,8 µM. Avec les rapports 664/612 qui bougent peu (1,86 → 2,11), la rupture des dimères est jugée non démontrée (`probleme`). Je n'ai pas lu le texte complet de Fernández-Pérez 2020, seulement les extraits et la revue qui le cite.
- Lampe contre laser : `probleme` de témoin (spectre, irradiance, géométrie changent ensemble ; lampes données en puissance électrique 120 W seulement). Préféré : gain de flux de photons utiles plutôt que dissociation des dimères.
- « 26,2 eV » : vérifié = 4,2×10−18 W / 1,602×10−19 J, donc des eV par seconde ; `probleme` car il fonde l'argument mécanistique. Énergie de dimérisation ≈ 20,5 kJ/mol tirée de la revue 2025.
- Irradiance : 0,255 (5 cm), 0,177 (60 mm), 0,77 (6,5 cm²) mW/cm², et 25 µW/cm² au résumé ; laissé en `reserve` (déjà signalé par l'extraction comme limite).
- Raie 305 nm de l'argon : vérifiée sur la fiche Coherent Innova Sabre (275,4–305,5 nm, grand cadre) ; le point est plausible, pas d'objection.
- 2-méthoxyéthanol Repr. 1B : pris sur PubChem (données ECHA), pas sur la fiche ECHA elle-même.
- Source PMC10052816 (aminoalcools) citée sans auteurs relevés : je n'ai pas ouvert la page pour économiser les recherches.
- Recherches web : 8. Crossref bloqué : aucun DOI vérifié ; rien ajouté à fondateurs.md ni constantes.md.
