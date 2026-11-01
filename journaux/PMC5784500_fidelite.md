# Journal de la critique de fidélité PMC5784500

- Ma liste d'échantillons avant ouverture de l'extraction : NaY (germes puis gel), HY, SYS7/6/4/2/1 (pH), NaY/SBA-15 et HY/SBA-15 (TPD, Py-FTIR), SBA-15 et Y de référence (isothermes), HY traité H2SO4 (RMN, masse), spectres Raman 1 à 5, PS seul, PS+HY, PS+SYS2. Tout est dans `sample_inventory` ; aucun échantillon oublié.
- Valeurs des tableaux 1 à 4 comparées une à une au texte : aucune erreur de recopie, sommes des colonnes de la table 4 et des rangées de la table 3 proches de 100 %. Aucune attribution de rangée fausse.
- Constat 1 (annotation NaY/SBA-15) classé `mineur` / `sure` : le texte dit « medium and strong acids ... increased » mais le tableau donne 24.60 -> 20.87 pour les fortes ; l'annotation recopie le texte alors que ses propres chiffres le contredisent. Pas `faux` : ce n'est pas une valeur extraite.
- HY/SBA-15 = SYS2 : `deduit` / `probable`. L'article ne relie jamais les deux noms ; l'extracteur l'a signalé en doute mais la donnée reste rangée sous SYS2.
- NaY/SBA-15 sans branche : `manquant` / `probable` seulement, car l'article ne décrit aucun protocole ; créer une branche demande de marquer le pH non cité.
- Témoin PS seul : toluène, éthylbenzène (3.10 est aussi dans le texte), autres, coke absents de toute structure ; `probable` car une voie sans synthèse est un choix de format.
- RMN, ESI-MS, Raman : valeurs jamais extraites. Je n'ai pas exigé de voie : l'échantillon (HY traité par H2SO4) n'est pas décrit ; j'ai proposé annotation ou résultat sans voie.
- Figures ouvertes : Fig. 1 (plage SXRD ≈ 0.6–5° confirmée ; le doute de l'extracteur est juste), Fig. 7 (pics 1.85 nm et ≈ 5.5 nm, conforme au texte), Fig. 8 (désorption à 473 K et 673 K non extraite ; étiquettes 1544/1442 et 1542/1455 proches du texte, écart < 1 %), Fig. 6 et Fig. 9 (qualitatives, rien à reprendre).
- Fig. 1b contredit le texte pour SYS6 (raies FAU les plus fortes alors que le texte dit « very weak ») : extraction fidèle, donc `mineur` / `probable`, pour que l'orchestrateur ajoute une limite de reproductibilité plutôt qu'une correction de valeur.
- Table 1 : j'ai recalculé les % atomiques à partir des % massiques ; O et Na concordent, Al et Si non (A : Al 0.021 contre 0.058). L'extracteur n'avait vu que le point D (91 contre 79.5). Je n'ai pas conclu à une erreur d'extraction : annotation seulement.
- Étape 10 de NaY (« wash at 110 °C ») : lecture littérale conservée par l'extracteur, doute écrit ; non retenu comme constat.
- `not_stated` : 45 cases vérifiées environ (rendement, volumes, rampes, atmosphère de calcination, vitesse d'agitation, pureté du verre soluble et de H2SO4), aucune ne figure dans le texte ni dans une annexe (aucune annexe).
- `method_sources` : CIT0026 deux fois (XRF, TPD) avec role « autre » ; je ne l'ai pas contesté. Aucun renvoi de préparation (« according to », « as reported ») dans les Méthodes de cet article.
- Écarté : isotherme SBA-15 « type V » (le texte se trompe, la figure montre une hystérèse IV) ; non extrait, donc rien à corriger. Somme BET 406 + 493 ≈ 900 m2/g douteuse : à laisser à la critique scientifique.
