# Journal d'extraction PMC6443225

- Découpage : une voie de base AuNPs (protocole complet : amidon, reflux, centrifugation, ajout du précurseur à 70 °C et pH 11, 2 h, centrifugation, redispersion) et une branche Ag/AuNPs. Table 1 est le seul endroit où l'article distingue les deux systèmes (500/0/250 µL contre 500/250/250 µL) ; la note de Table 1 dit « for both systems » pour 2 h, 70 °C, pH 11, ce qui fonde l'héritage des étapes.
- Voie de base = AuNPs (et non Ag/AuNPs) parce que le titre de la section de Méthodes cite d'abord les AuNPs et que Ag/Au s'en déduit par ajout de AgNO3 ; la variation est donc un réactif ajouté (`silver_nitrate_solution`, parent « none (0 µL) »), d'où l'avertissement du contrôle, expliqué dans `doubts`.
- Étapes 4 et 5 (chauffage à 70 °C, pH 11) : une seule phrase les donne ensemble (« at the preset temperature of 70°C±1°C and pH=11±0.2 »). Ordre arbitraire, déclaré en doute. NaOH n'est jamais dit servir au réglage du pH : gardé comme base, quantité non citée.
- Réactif amidon : la quantité utilisable est le 500 µL de la solution à 1 % m/v de Table 1 (rangée AuNPs). Masse d'amidon et volume préparé déclarés non cités. Pureté et fournisseur non cités (amidon extrait de pomme de terre par les auteurs, la phrase « minimum 99% purity » vise les produits achetés).
- Fournisseurs de AgNO3, NaAuCl4, NaOH : une seule phrase les donne avec la pureté « minimum 99% » ; elle sert de `supplier_quote` pour les trois.
- Tailles : rangées de Table 2 et Table 3 citées par nom d'échantillon, jamais par la phrase « respectively » qui inverse l'ordre Ag/Au puis Au selon les phrases (λmax : Ag/AuNPs d'abord ; tailles TEM : AuNPs d'abord).
- Contradiction taille cristallite AuNPs : Table 2 (22.5±9.9) contre Table 3 (23.5±10.3) ; Table 3 retenue, doute écrit.
- Rapport Ag:Au par ICP : l'article écrit 1.13, le calcul à partir de 17,0 et 35,1 µg/mL donne 0,88 ; aucune valeur déduite, valeurs de concentration extraites, rapport laissé de côté, doute écrit.
- Valeur UV-visible 27.4±2.0 nm des AuNPs : même nombre que la valeur de littérature citée dans le texte ; extrait depuis Table 2, doute écrit.
- Figures lues (Read) : Fig. 5B (potentiel ζ et pH de mesure), Fig. 11A/B et 12A/B (prolifération à 72 h, 20 µg/mL seulement, pour ne lire que ce qui est lisible). Fig. 7, 8, 9 (courbes de croissance, Gompertz, colonies) non lues : le texte donne les conclusions et Table 4 donne les IC50 ; Fig. 6 (histogrammes) redondante avec le texte.
- Durée de l'essai de cytotoxicité : Méthodes 24 h, Résultats 24 h et 72 h ; rangée 72 h lue sur figure, doute écrit.
- Échantillons sans voie : AgNPs seules (synthèse non décrite, Fig. S1 absente), mélange physique AgNPs+AuNPs, amidon pur de référence. Les six lots indépendants (Fig. 3) sont rattachés aux deux voies.
- Annexes : aucune section Supporting Information dans le texte ; Figures S1 à S4 citées, annotation « Annexe absente du dépôt » écrite.
- Essais antibactériens et cytotoxicité rangés en `outcomes` des deux voies (jamais en branches) ; résultats donnés pour le groupe (Gompertz, MEB) dans une annotation `tendance_observee`.
- Renvoi de méthode : une seule source utile, b47 (méthode « improved » à partir d'un travail antérieur sur des clusters d'argent), rôle protocole_adapte. Gompertz (b48) et équation de Khlebtsov (b53) sont des formules d'analyse, exclues.
