# PMC4951059 — critique scientifique (Opus)

- Sol de silice, rapport TEOS:HNO3 = 1:1,7 : rapporté à 1 mol de TEOS (≈ 728 mL de sol), cela donne [HNO3] ≈ 2,3 mol/L, donc de l'acide en quantité stœchiométrique et non catalytique. Classé `probleme` (bilan), pas « corrigé » : le texte écrit bien 1,7. La source « as described previously » n'a pas été retrouvée, donc l'hypothèse d'une coquille (0,017) n'est pas vérifiée.
- Même voie : l'acide à 65 % apporte 3,2 H2O par TEOS, donc le rapport réel H2O/TEOS vaut ≈ 5,2 et non 2. Classé `reserve`.
- Sécurité : le prémélange HNO3/éthanol contient ≈ 24 % en masse de HNO3. CAMEO n'a pas de fiche sur le couple acide nitrique–éthanol : je cite la fiche des mélanges nitrants (7196) et l'oxydant fort, sans affirmer un seuil d'explosion.
- Sol d'aluminosilicate : 67 mL de TEOS donnent 0,300 mol de Si, contre 19,6 mmol d'Al, soit Al/Si = 0,065. C'est le calcul central : Al2SiO5 « prédominant » demanderait 30 fois plus d'Al. `probleme`.
- Kyanite : polymorphe de haute pression d'Al2SiO5. Je cite le point triple de Holdaway 1971 via le rapport USGS OF 92-298 (source secondaire) ; DOI de Holdaway non vérifié, donc non donné.
- Zr5Al3O0.5 : retrouvé comme intermétallique Zr5Al3 de type Mn5Si3 avec O interstitiel (Kim et al. 1988, fiche COD 1530163 vue en résultat de recherche). Le rejet est redox (calcination sous air), `probleme`.
- ZrSiO4 à 400 °C : la notice OSTI 784452 (gels ZrO2–SiO2, zircon à 1 200 °C, silice amorphe avant) a été préférée à une étude avec minéralisateur NaF (550 °C), sans objet ici puisque le sol n'en contient pas.
- Figure 3 ouverte moi-même (corpus/fig) : stishovite en 3A, coésite et « Aluminum zirconium » (00-016-0075) en 3B, aucune fiche de t-ZrO2 en 3A et 3B alors que le substrat en 3C la donne. Ces observations renforcent le diagnostic d'une indexation automatique.
- Épaisseur de 10 µm : Landau–Levich avec des propriétés de sol estimées (η 2 mPa·s, γ 22 mN/m) donne ≈ 2 µm de silice dense à 80 mm/s et 0,14 µm à 80 mm/min. Comparée à l'épaisseur critique de ≈ 0,3 µm (Kappert 2015), elle est classée `reserve` seulement, car la mesure est faite après cuisson de la porcelaine (zone d'interdiffusion probable).
- « Four times larger cell volume » : recalculé par motif (× 1,94 par Zr ; −17 % pour ZrO2 + SiO2 → ZrSiO4). `reserve`, car l'argument porte sur une phase déjà douteuse.
- Tukey refait par simulation (200 000 tirages, pas de scipy) avec n = 12 barres et s commun 2,72 MPa : je retrouve exactement les P de l'article (0,67, 0,013, 0,18, 0,008). Cela confirme aussi la lecture du témoin sur la figure 6 (20,52 ± 2,8) ; il reste une pseudo-réplication (barres contre blocs).
- Réversion m→t pendant la cuisson de la porcelaine (S) : seules des sources sans DOI fiable ont été trouvées, donc l'appui reste `chimie_generale` en `reserve`, sans citation.
- Pages web directes (Ewha, Penn State, COD) inaccessibles par DNS : sources citées par l'URL de leur notice, avec les métadonnées des extraits de recherche.
- 9 recherches web. DOI donnés mais non vérifiés sur Crossref : 10.1039/C4SM02085E (Kappert) ; 10.1021/cr00099a003 (Hench & West) vient de fondateurs.md, déjà vérifié.
