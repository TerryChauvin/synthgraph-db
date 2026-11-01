# Journal d'extraction PMC10511489

- Découpage : la zéolithe T parent (voie `ZeoliteT`, kind `intermediate`) est une voie de base à part, réutilisée comme réactif `intermediate` dans S1 ; son protocole est donné en détail (Methods, « Synthesis of the parent zeolite T ») avec purité et fournisseur de chaque réactif.
- Voie de base de la conversion : S1 (KOH, sans ultrasons, 353 K, 48 h), premier échantillon du Tableau 1 ; S8 (NaOH sans ultrasons) en dérive par remplacement de la base (variation sur le réactif `potassium hydroxide`, valeur `replaced by sodium hydroxide`).
- Sonication = étape en plus : S2 a ses propres étapes (étape 4 sonicate, 313 K, 2 h, 200 W, 40 kHz) car S1 n'en a pas ; S3 à S13 héritent de S2 (ou de S9 pour la série NaOH). Le contrôle donne donc un avertissement attendu sur la variation `ultrasonic_treatment` (doute écrit).
- Place de la sonication : le texte dit seulement « before hydrothermal synthesis » ; placée après l'agitation de 2 h (doute).
- Parents des branches : S3 parent S2 (durée US 4 h) ; S4 parent S3 (96 h) ; S5 parent S2 (333 K) ; S6 parent S5 (4 h) ; S7 parent S6 (96 h) ; S9 parent S2 (NaOH) ; S10 parent S9 ; S11 parent S9 (333 K) ; S12 parent S11 (4 h) ; S13 parent S12 (96 h). Le choix du parent suit la plus proche des rangées du Tableau 1 (un seul paramètre qui change).
- Contradiction Tableau 1 / texte : échantillons 16 à 21 notés KOH au tableau, mais Méthodes et Résultats parlent de la série en temps « NaOH-treated ». Rangée du tableau retenue (parent S2), autre lecture en doute.
- S14 : table `NaOH, 313, 0, 353, 6` ; le texte dit « without the ultrasonic treatment » donc branche de S8 (durée 6 h), sans sonication ; la température 313 K est ignorée (durée 0 h).
- S15 et S16 : synthétique 0 h / 0 K dans le tableau = pas de traitement hydrothermal ; voies à étapes propres (dissolution, ajout, agitation, sonication seulement) car hériter du chauffage et du lavage serait un héritage non fondé ; température de la variation gardée en `value_text` « 0 » pour ne pas écrire 0 K.
- Séries 17 à 21 : une branche par rangée, toutes enfants de S2 (même KOH, 313 K, 2 h), seule la durée hydrothermale change (6, 12, 20, 28, 40 h). Résultats de S14 à S21 tirés du texte des Résultats ; les figures S4 à S6 (annexe) n'ont pas d'image dans le dépôt.
- Tableau S5 : l'en-tête annonce B/L en premier mais les nombres suivent l'ordre B, L, total, B/L ; contrôlé par la somme B + L = total sur les 12 groupes.
- Pureté et fournisseur de KOH/NaOH de l'étape de conversion : non cités (la phrase de la synthèse de la zéolithe T ne couvre pas explicitement cette étape).
- Figure 9c-d : seule figure lue (valeurs d'adsorption de CO2 à 760 mmHg des échantillons 1, 2, 8, 9, 2 chiffres, ±2 cm3/g) car le texte ne donne que l'ordre ; les autres figures (DRX, MEB, RMN) sont décrites dans le texte.
- Lecture figure Fig. 9b non reprise (pic à environ 3,8 nm pour les quatre, différences de hauteur seules) ; les plages de taille de pores du texte ne sont pas extraites en résultats numériques.
- Résultats du matériau fini (BET, acidité, Si/Al, CO2) rangés en `outcomes` des voies S1, S2, S8, S9 (pas en branches).
- Source de méthode : un seul renvoi (`b0170`, « our previous report ») pour la synthèse de la zéolithe T ; la formule de la maille (réf. b0210) est une équation d'analyse, exclue.
- Les rendements de S2, S8, S9 sont en `outcomes` (S1 porte le rendement de voie de base) ; le rendement est défini en note du Tableau S2 comme CHA finale divisée par zéolithe T de départ.
