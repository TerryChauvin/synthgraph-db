# Journal — test de complétude PMC9227472

- Extraction d'origine déjà dense : synthèse complète, séries d'optimisation lues sur la Fig. 2, résultats principaux et contradictions notées en doutes. Les trous étaient dans les tableaux 1 à 3 et 5 et dans les bandes FTIR du texte.
- Tableau 1 : positions 2θ au chiffre du tableau (38.17753 etc.), FWHM, hkl du texte 3.4 rangés en outcomes distincts de la voie AgNPs_opt (le tableau ne donne pas les hkl, le texte oui).
- Tableau 2 : PDI 0,254 ajouté sous un nom propre (`polydispersity_index_table_2`) pour ne pas écraser le 0,248 du texte ; la contradiction était déjà en doute.
- Tableau 3 : intensités nettes (« Net Int. ») ajoutées en `counts` ; l'unité n'est pas écrite par l'article, c'est une convention de lecture de la colonne.
- Tableau 5 : témoins (AgNO3, eau, gentamicine, nystatine) rangés en outcomes `control_*` sur AgNPs_opt, faute de voie propre (inventaire : réactifs commerciaux sans protocole). Ordre des colonnes de l'en-tête (S. aureus, E. coli, C. albicans) respecté ; l'inversion texte/tableau de la gentamicine reste en doute, non résolue.
- Les tirets « - » du Tableau 5 (pas de zone) ne sont pas ajoutés comme valeurs ; l'extrait non actif est déjà couvert par `antibacterial_activity`.
- Constante de Scherrer K = 0,94, plage 0,68–2,08, λ, définition de β et équation de Bragg : nouvelle entrée de `characterizations` plutôt que modification de la chaîne `conditions` de l'entrée XRD existante (règle « ajouter seulement »).
- FTIR de l'extrait : les valeurs sont rattachées à la voie `Extract_dried_powder` (poudre analysée par FTIR), pas à la voie des AgNPs ; les bandes modifiées après réaction (1021, 1443, 1634, 3428) sont sur AgNPs_opt.
- DPPH : écarts-types ajoutés tels qu'écrits, sans trancher la permutation probable des séries extrait/AgNPs (déjà notée) ; l'IC50 de l'ascorbate est un témoin du test.
- Sonde des manques : « UV-vis conditions absentes » : l'article ne donne que l'appareil, pas de plage ; laissé à null avec un doute. « Électrochimie » : faux positif (« IC50 », « capacity »), écarté.
- Aucune valeur de la littérature comparative chiffrée dans l'article (les comparaisons sont qualitatives) : pas de liste `comparisons`. Aucun calcul DFT. Aucune figure ouverte : les figures ne portaient pas de résultat chiffré absent du texte, hors séries déjà lues.
- Toutes les citations sont des sous-chaînes exactes de corpus/text (contrôle par script avant l'écriture, puis `load.py check` : 0 erreur).
