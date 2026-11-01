# PMC5456199 — critique scientifique (journal de décisions)

- « 27,0 g of SiO2 (HS-30 Ludox) » lu comme masse de suspension (30 % SiO2) : le gel vaut alors Si/Al = 1,01 (4,7 Na2O : Al2O3 : 2,0 SiO2 : 154 H2O), proche de la recette IZA de NaA ; lu comme silice pure, Si/Al = 3,4 (domaine FAU), incompatible avec la LTA obtenue. Statut `reserve` (ambiguïté d'écriture, pas d'erreur de chimie).
- Aluminate « Nalco 680 » : aucune fiche trouvée ; calcul fait en NaAlO2 pur et en grade technique Sigma (Al2O3 50–56 %, Na2O 37–45 %) pour donner une fourchette de Si/Al (1,13–1,26).
- `probleme` « % of PSS » : les six pourcentages suivent p = m/(m + X) avec X = 10,9–11,05 g, ni m/16,5 ni m/(16,5+m) ; je n'ai pas identifié ce que sont ces 11 g (ni l'eau du PSS, 13,6 g, ni 16,5 g). Conséquence : la fenêtre optimale 3,5–6,8 % n'est pas transposable.
- `probleme` Table 2 : sur feuille d'aluminium |pente| baisse (0,0033 → 0,0024), donc prise plus lente, contraire à « significant improvement » ; et la 4A commerciale (−0,0039) est plus rapide que NZ040 (−0,0033), contraire au résumé. Pris tel quel dans les chiffres publiés, sans supposer d'inversion de colonnes.
- Constante de temps ≈ 300 s pour toutes les tailles (rapport attendu 225 entre Z0 et NZ040) : je conclus à une mesure limitée par la chaleur ou le lit, pas à la « surface barrier » des auteurs ; signalé en `reserve` avec Cheung et al. 2013 (même groupe, même constat sur nano-NaA).
- `probleme` calcination : les Méthodes l'appliquent à tous les produits, la conclusion la nie ; l'état des poudres mesurées (Table 1, figure 5) est indéterminé.
- Polymère : « Methocel HG » = hypromellose dans PubChem (ChemIDplus/RTECS), Dow réserve « A » à la MC, et la HPMC Sigma de Mn ≈ 86 000 correspond au « MW 87000 » ; ChemicalBook range « Methocel 90 HG » sous méthylcellulose, source jugée moins fiable. Gardé en `reserve` (« très probablement »).
- Mécanisme `a_revoir` : à ≈ 3,5 mol/kg de Na+, les ions « salting-out » abaissent la température de gel (sources MC/HPMC), alors que les auteurs invoquent une hausse ; la gélification faible et la « pâte blanche » font préférer un rôle de viscosité, de gêne à l'agrégation et d'adsorption sur les germes à un confinement dans un hydrogel homogène.
- Sélectivité : seul le rapport des quantités à 100 kPa est calculable (≈ 10 pour NZ040, 12 pour Z0) ; non comparable à la sélectivité idéale 0,15/0,85 bar de la revue Cheung & Hedin 2014 (≈ 60), dit comme tel.
- Surface externe : ρ(NaA déshydratée) recalculée à 1,525 g/cm³ depuis la maille pseudo-cubique 12,29 Å ; 61 m²/g ↔ cubes de 65 nm, cohérent. Constante non sourcée en ligne (calcul).
- Pages de Cundy & Cox non reprises (non relues) ; auteur et DOI de Joshi 2011 vérifiés sur PMC. Enthalpie de dissolution de NaOH et pression de vapeur à 82 °C : valeurs de manuel, non relues en ligne (listées dans `sources_not_found`).
- Aucune voie NaA dans la base pour comparaison (compare.py).
- Recherches web : 8 recherches + 1 lecture de page.
