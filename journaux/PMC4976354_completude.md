# Journal du test de complétude, PMC4976354

- Lecture complète du texte, de l'extraction et des deux listes. La procédure de synthèse était déjà complète (BCN, SCN, HCN/NCN en héritage, témoin fritté, électrode) : aucune étape ni quantité ajoutée.
- Table 3 (TRPL) : seule la durée de vie moyenne était extraite. Ajout de τ1, τ2, B1, B2 et χ² pour chaque échantillon, avec la ligne du tableau en citation. Unité laissée vide pour τ1, τ2 car l'en-tête n'en donne pas (doute noté) ; χ² rangé en statistique.
- Table TS2 (annexe) : texte aplati une cellule par ligne, avec le μ codé en U+F06D (police Symbol). Les neuf lignes de la littérature reconstruites dans l'ordre des colonnes et rangées dans `comparisons`, en `value_text` (pas de conversion), citation = la cellule de valeur avec le caractère d'origine. Pas de `ref_id` : les références S1–S9 sont celles de l'annexe, absentes de corpus/refs.
- Front d'absorption « 487 to 454 nm » : attribué à SCN par cohérence avec les bandes interdites (2,72 eV vaut environ 456 nm), mais l'article ne l'attribue pas à un échantillon ; doute noté.
- Pic XRD (100) à 14,1°, plage FT-IR 1200–1650 cm−1, isotherme de type IV et pseudo-premier ordre : l'article les dit pour tous les échantillons, donc ajoutés aux quatre voies. Les valeurs du pic (002) n'ont pas été touchées (phrase du texte confuse, déjà en doute).
- Conditions de mesure : plage 350–800 nm du UV-vis (légende de la Fig. 5) et seconde mesure du potentiel zêta (ZetaProbe, pH neutre) en nouvelles entrées `characterizations` dans les quatre voies. Les conditions déjà présentes (XRD, TEM, TRPL, MB, H2, électrochimie) n'ont pas été prolongées.
- Conditions absentes de l'article (tension MEB, plage et pas XRD, dégazage BET, appareil FT-IR, lampe du test MB) : rangées dans un doute, pas dans `not_stated`.
- Sonde B (PL, résultat absent) : écartée, les occurrences sont des mentions de TRPL ; la PL stationnaire n'a aucun résultat dans l'article.
- Écartés : 2,7 eV (valeur générale de l'introduction), fragment « 95 » (7.95 déjà extrait), numéros de figures et de références.
- Fragile : le paramètre `observation` (couleur) est un nom hors vocabulaire existant, faute d'équivalent.
