# Journal du test de complétude — PMC6443225

- Aucune figure ouverte : toutes les valeurs ajoutées sont dans le texte ; aucune annexe dans le fichier (Figures S1–S4 déjà signalées absentes).
- Règle « ajouter seulement » : les conditions de mesure déjà présentes ont été prolongées en ajoutant à la fin de la chaîne (le texte d'origine reste en tête, mot pour mot), pour garder une seule entrée par technique comme demandé. L'entrée EDS, dont `conditions` était nul, a été renseignée. Aucune valeur, citation, étape, voie ou annotation retirée ou modifiée.
- Les entrées ajoutées aux conditions n'ont pas de citation propre (le champ `quote` de l'entrée existante est conservé) ; le texte reprend les formulations de l'article.
- Essais biologiques (croissance bactérienne, comptage de colonies, MEB, MTS) : quatre entrées `characterizations` créées, identiques dans les deux voies car les essais portent sur les deux colloïdes (les résultats par voie y existaient déjà). Les appareils de suivi de croissance et de lecture MTS ne sont pas nommés : doute, pas `not_stated`.
- Pics XRD : l'article donne une seule liste « pour Ag/AuNPs et AuNPs » (identique aux massifs Ag et Au) ; mêmes valeurs dans les deux voies, doute posé.
- Rapport ICP 1,13 : valeur de l'article incohérente avec ses concentrations (≈ 0,88) ; ajoutée sous le nom `ICP_atomic_ratio_Ag_to_Au_as_written`, avec un doute renvoyant à l'annotation existante, pour que le chiffre de l'article soit présent sans être présenté comme mesuré.
- Témoins AgNPs (406 nm) et mélange physique (402/521 nm) : pas de voie ; rangés dans les outcomes de Ag/AuNPs, qui leur est comparé en Fig. 2, avec un doute.
- Valeurs de la littérature : 470 nm (b52), 27,4 nm et 524 nm (b53), a de référence du Tableau 3 (sans renvoi), potentiels standard cités, critère ±30 mV : dans `comparisons`, jamais en `outcomes`. Le critère ±30 mV et les potentiels ne sont pas des comparaisons à un échantillon précis ; ils servent à juger la stabilité et la faisabilité de la réduction.
- 27,4±2,0 nm : gardé dans `comparisons` avec le renvoi de l'article, bien que la valeur semble sortir de la formule de Khlebtsov (annotation existante).
- `repetitions` : « six lots » ajouté en `value_text` sur l'étape 6 de AuNPs (la citation n'a pas de chiffre « 6 ») ; la branche Ag/AuNPs en hérite.
- Écartés : numéros de figures et de références, 100 µL/mL « 1,000 » comme volume (c'est une concentration d'étalon, déjà dans les conditions ICP), 3 500 et 12 500 rpm (déjà extraits).
- `not_stated` : aucun ajout, la grille de la synthèse était déjà complète.
- Non ajouté : forces ioniques ou composition du milieu LB (non données), nombre de particules comptées en MET (absent, en doute).
