# Journal de la critique de fidélité PMC6274424

- Ma liste d'échantillons avant ouverture de l'extraction : RE (extrait), SP-Ag-1 à -5 (0,1 ; 0,5 ; 1,0 ; 2,0 ; 3,0 mL), volumes de 3 à 5 mL (aucune formation), témoin sans RE, C-Ag (citrate), précipité blanc de l'extrait (non synthétisé), et « SP-Ag » générique (XRD, FT-IR, dispersion). Identique à `sample_inventory` : aucune branche manquante, aucune inventée.
- Table 1 relue rangée par rangée contre les colonnes (M. luteus, S. aureus, E. coli, P. aeruginosa) : les 7 rangées et les 28 valeurs sont correctes, l'unité mm vient de l'en-tête. Fig. 11 confirme les barres.
- « SP-Ag » rattaché à SP-Ag-3 pour XRD, FT-IR et dispersion : constat `deduit`, `probable` (pas `sure`), car le texte n'écrit jamais le volume ; l'extracteur a déjà un doute, donc je ne le traite pas comme une erreur de valeur.
- Fig. 6c (valeur `from_figure`) : étiquette « 10.95 ± 0.09 nm », extraction 11 nm, écart 0,5 %, sous le seuil de 10 %. Mais l'histogramme (≈ 4 à 24 nm, comptes ≈ 7, 17, 12, 4, 3) rend fausse la déclaration `size_distribution_values` manquante : constat `non_cite_a_tort`, `probable` (lecture graphique approximative).
- Bandes UV : texte 450 nm (SP-Ag-3) et 420 nm (C-Ag) ; Fig. 2b ≈ 400-410 nm, Fig. 9a ≈ 445 nm. Ce ne sont pas des valeurs `from_figure`, donc pas de constat de valeur fausse ; je ne retiens que l'absence de C-Ag dans l'annotation de limite de reproductibilité (constat mineur).
- Fig. 3 (cinétique) : signal quasi nul à 15 et 30 min, épaulement à 45-90 min, plateau 2-3 h, ce qui contredit « fast formation for the first 60 min ». Pas une erreur d'extraction ; j'ai demandé l'ajout des points de temps comme résultat et noté l'écart.
- Écarté : l'héritage des étapes pour la branche > 3 mL (même série, « All experiments were executed at 90 °C ») ; l'extracteur l'a signalé, je le laisse.
- Écarté : `method_sources` ; seule B45 (« according to the literature ») figure dans les sections 3.x de `corpus/refs`, présente et bien classée. Le test de Kirby-Bauer n'a pas de renvoi.
- Étape 4 de RE (séparation du précipité blanc) : ordre cohérent avec 2.5 (avant évaporation) ; `separation_method` non cité à raison.
- Les 35 `not_stated` ont été vérifiés dans le texte : la durée de centrifugation de la synthèse est bien absente (le 30 min / 9000 rpm de 2.2 et 3.3.4 est celui des échantillons purifiés pour FT-IR, correctement rangé dans les conditions FT-IR).
- Annotation `mecanisme_analyse` de C-Ag (« Turkevich ») : relève de la méthode de Lee et Meisel pour l'argent ; sans passage de l'article, c'est dans `mechanism_check` et non un constat.
- Constat sur « heated / aqueous » du témoin sans RE : `deduit` mineur, ces mots ne sont pas dans « under a similar set of conditions ».
