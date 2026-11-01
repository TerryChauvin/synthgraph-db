# Journal de la critique de fidélité PMC13516552

- Ma liste d'échantillons avant d'ouvrir l'extraction : Poly-CoPc, Poly-CoPc/SWCNT, électrode et pile de chacun, et les matériaux de la Table 5 (autres publications). Identique à `sample_inventory` ; l'article ne balaie ni température, ni durée, ni teneur en SWCNT, donc aucune branche de synthèse manquante.
- Tables 2, 3, 4, 6 et 1 recomparées valeur par valeur aux rangées du texte : aucune rangée décalée entre Poly-CoPc et composite. Rétentions (803/1703, 1047/2016) et capacités retrouvées (777/804, 1118/1102) recalculées : cohérentes.
- Efficacité coulombique du 1er cycle : texte 58,30 %, tableau 58,29749 ; extraction retient le tableau, je n'y vois pas de faute.
- 855 mA g−1 (texte) contre 847 mAh g−1 (Table 4) à 0,5 A g−1 : écart d'unité et de valeur dans l'article, déjà noté en doute par l'extracteur ; je n'en fais pas un constat. Je signale seulement dans les lacunes que l'article ne dit pas si 855 vient de la Fig. 8e ou 8f.
- Constat « manquant » sûr : le diamètre des SWCNT (1,4–1,7 nm) en 2.1 est absent de l'extraction (recherche de la chaîne « 1.4–1.7 » dans le JSON : 0 occurrence).
- Constat Raman en `probable` : la citation de la caractérisation ne contient que les bandes D et G, alors que le résultat affirme « ID/IG increased » ; la phrase source existe plus loin dans 3.1, l'écart est de citation et non de valeur.
- Filtration : « vacuum filtration » n'apparaît pas comme paramètre de l'étape 5 du composite ; `probable` car l'extracteur a pu considérer `filter_type` comme le support filtrant (membrane), qui lui n'est pas cité.
- `active_material_loading` en résultat : c'est un réglage de préparation, déjà paramètre de l'étape 5 ; l'unité apparaît en double (value_text + unit). Mineur `probable`.
- Champ manquant mal nommé `current_density_for_CV_beyond_0.1_mV_s-1` : la grandeur est une vitesse de balayage. Mineur.
- Écarté : rôle « mineralizer » du molybdate d'ammonium (l'article dit « reaction promotor ») : vocabulaire de rôle, pas de texte contradictoire.
- Écarté : fournisseur « Sigma-Aldrich or TCI » appliqué à Super P, PAA, éthanol (listés en 2.1) ; non appliqué à acétone, eau, Cu, Li, Celgard, LiPF6 (non listés) : choix correct.
- Sources de méthode : seuls [B27, B28] (« method adopted from earlier works ») sont des renvois de méthode ; les renvois de la Table 5 et de l'introduction sont du contexte. Rien de manquant.
- Figures : dossier `corpus/fig/PMC13516552` vide, aucune valeur `from_figure` dans le JSON ; vérification sur image impossible. Écarts listés dans reproducibility_gaps (Fig. 3b, 7, 8, 9).
- 2.1 liste NMP et méthanol comme solvants, absents des protocoles, et omet l'acétone : ajouté aux lacunes de reproductibilité (incohérence de l'article, pas une erreur d'extraction).
- Température 175–180 °C (Méthodes) contre 185 °C solvothermal (Résultats) : l'extracteur a retenu les Méthodes avec doute et annotation ; pas de constat.
