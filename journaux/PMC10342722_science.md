# PMC10342722 — critique scientifique (journal de décisions)

- Quantités « 0,95 mg / 0,6 mg » classées `probleme` (bilan) et non simple réserve : 3,26 µmol de Co donnent au plus 0,297 mg de CoS par lot, moins que les 2 mg de l'encre d'électrode (section 2.4). Hypothèse « grammes » (72,5 et 175 mmol/L) jugée plausible, mais non imposée.
- Indexation DRX : recalcul de Bragg (λ 1,5406 Å) et des d(hkl) de CoS type NiAs (a 3,367, c 5,16 Å, Webmineral, source secondaire faute de fiche JCPDS) → les quatre pics sont (100), (101), (102), (110) ; (210) tomberait à 88,7°. `probleme` sur les indices, pas sur la phase.
- Pic « CoO » : lu sur la figure 1 vers 32,5°. CoO NaCl (a ≈ 4,26 Å) donne 36,5 et 42,4°, absents ; β-Co(OH)2 (100) = 32,49° (SI Nanoscale c7nr07879j). `probleme` avec la nuance « un pic unique ne permet pas de conclure ».
- EDX : % atomiques recalculés depuis les % massiques de la figure 3 (relue) : 160 °C exact, 180/200/220 °C décalés (Co 45,25 contre 48,23 at % à 200 °C). S/Co passe de 1,07 (200 °C) à 1,25 (220 °C) : la « perte de soufre » des auteurs est contredite par leurs propres chiffres → `probleme`.
- GCD : temps de décharge lus sur la figure 7 (5 ; 5,5 ; ≈ 11,5 ; ≈ 7,5 s sur ≈ 0,57 V) → 8 à 20 F/g à 1 A/g. Les valeurs du texte valent toutes 100 × Δt/0,6 (Δt = 5 ; 5,5 ; 9,5 ; 0,7 s) : facteur 100 caché ; 116,6 F/g probablement 1166,6 mal recopié (Δt 7 s). Hypothèse donnée comme telle, pas comme correction.
- Figure 8 : 0,0013 « Ah » impossible pour 1 µg ; lu en Ah/g, cela donne ≈ 7,6 F/g, cohérent avec la figure 7 et pas avec 1583 F/g. Argument retenu pour la voie Electrode_CoS (verdict `incoherente`).
- 1583 F/g = 90 % du maximum théorique à un électron (1767 F/g sur 0,6 V, F/M(CoS)) : utilisé comme signal, pas comme preuve seule.
- Rétentions du tableau 2 recalculées : 160 et 200 °C fausses (22,8 et 36,9 % au lieu de 21,3 et 42,55 %).
- Autoclave : capacité non donnée ; 45 g d'eau → 53,6 mL à 220 °C (ρ 840,2 kg/m³, table de vapeur roymech, NIST WebBook non atteint) : godet de 50 mL exclu. Réserve, pas problème, car le volume réel est inconnu.
- Mécanisme : « kinetic ripening » / « Gibbs free energy gained » remplacé par hydrolyse de la thiourée (H2S/NH3) + mûrissement d'Ostwald ; à 220 °C, hydroxyde par montée de pH plutôt que perte de soufre (système fermé). Source : Feng & Xu 2000 (fondateurs.md) et SI β-Co(OH)2.
- Sources électrochimie : Gogotsi & Simon 2011 (10.1126/science.1213003) et Brousse et al. 2015 (10.1149/2.0201505jes), DOI confirmés par recherche web (Crossref bloqué). Non ajoutées à fondateurs.md (consigne de l'orchestrateur).
- Sécurité : classement du nitrate de cobalt pris sur une fiche fournisseur (Glentham), ECHA non atteint ; fiche CAMEO de la thiourée injoignable (ENOTFOUND) → produits H2S/NH3 donnés par la chimie de l'hydrolyse, CAMEO non cité.
- Comparaison base : seule PMC10458794 contient CoS (composite, thioacétamide, 200 °C) ; pas de comparaison directe.
- 10 recherches web, 1 lecture de page (échouée).
