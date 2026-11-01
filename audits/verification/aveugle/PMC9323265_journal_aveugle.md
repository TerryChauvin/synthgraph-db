# Journal d'extraction PMC9323265 (extraction à l'aveugle)

- Une seule voie de base, `NFCDs` : la section 2.2 décrit un seul protocole, sans série de conditions de synthèse. Aucune branche.
- Les gammes de concentration de NFCDs, de pH, de NaCl, d'irradiation UV, de Fe3+ et d'AA (2.4, 2.5, 3.3 à 3.5) sont des conditions de mesure du matériau fini : rangées en `outcomes`, pas en branches (règle « tests du matériau fini »).
- « the desired amounts of DL-malic acid and levofloxacin » : aucune quantité ni rapport ; `amount` déclaré `not_stated` pour les deux précurseurs, avec un doute. Seuls 10 mL d'eau sont chiffrés.
- Pureté des précurseurs : « analytical grade » ne vise que les réactifs inorganiques (2.1), donc pas appliquée à l'acide malique ni à la lévofloxacine ; fournisseur Aladdin retenu avec la phrase de 2.1.
- Eau ultrapure : fournie par le Milli-Q du laboratoire, sans fournisseur ni pureté chiffrée ; deux entrées d'eau (première dissolution 10 mL, redissolution après micro-ondes sans volume).
- Étape 2 : « heated in a microwave oven (600 W ...) for 5 min » : puissance et durée extraites, température déclarée non citée (grandeur non donnée pour un four micro-ondes).
- Étape 3 : « for around 24 h » retenu comme 24 h (la citation contient bien le nombre) ; fréquence « 40 KHz » gardée avec l'unité écrite.
- Étape 5 : « MDCO 34-1000 Da » (sans doute MWCO) recopié tel quel en `value_text`.
- Étape 6 : lyophilisation à −70 °C codée `dry` pour passer par la grille ; durée non citée.
- « NFCDs-1 » (2.4) apparaît une seule fois : interprété comme le même échantillon que NFCDs (inventaire et doute).
- Taille 5.5 ± 0.1 nm (Résultats) préférée à 5.49 nm (Conclusions) ; Fe3+ 5-500 µM (Méthodes) contre 5-300 µM (Résultats) laissé en doute.
- Aucune figure lue : tous les résultats chiffrés sont dans le texte ; Scheme 1 ne porte pas de quantités. Figures S1-S7 et tableaux S1-S4 absents du dépôt (annotation `limite_reproductibilite`).
- `method_sources` vide : aucun renvoi bibliographique dans les Méthodes (le travail antérieur N-dopé de l'introduction est un renvoi de contexte).
