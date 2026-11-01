# Journal d'extraction PMC9418510

- Voie de base = ZSM-5-5 (5 : 1 : 30, broyage 50 min, 180 °C 48 h) : c'est la condition « réussie » que les Méthodes (sections 2 et 3) prennent comme point de départ de tous les balayages ; quantités des Méthodes (SiO2 24 mmol), pas du tableau S1 (24.13), signalé en doute.
- Séries de composition : une branche par ligne du tableau S1 (23 branches), nommée par les auteurs quand le Tableau 2 donne un nom (ZSM-5-6, MOR-9, MOR-7, ZSM-5-7, ZSM-5-8), sinon N<x>-S<y>[-OH]. Les cases « — » du Tableau 1 ne sont pas créées (mélanges non préparés).
- Phases : chaque rangée entière du Tableau 1 est citée, l'attribution se fait par l'en-tête « 30 | 30 (with NaOH) | 40 | 40 (with NaOH) » (vérifiée par script) et recoupée avec les légendes Fig. 3, Fig. 4, Fig. S3 et S4.
- Branches avec NaOH : NaOH (2,5 mmol, 99,8 %, Fisher) ajouté en réactif de la branche avec variation « sodium hydroxide / none » (règle du RUNBOOK) ; d'où 11 avertissements attendus du contrôle.
- Unground et Ground-25min : durée de chauffage donnée seulement par « varied from 24 to 72 h » ; je n'ai pas inventé de branche par durée, durée en value_text. Unground a ses propres étapes (pas de broyage), Ground-25min hérite du parent.
- Quartz sur Fig. 1C/D : la légende marque des pics de quartz pour les produits 48 h et 72 h alors que le Tableau 1 écrit « ZSM-5 » ; les deux sont gardés, doute noté.
- Calcination : trois voies post_treatment (Calc-24h/48h/72h), durée 6 h tirée de la phrase générale des Méthodes (« selected products »), atmosphère air des Résultats ; doute noté.
- Échange acide : voie post_treatment H-ZSM-5-5 et trois branches (le réactif intermédiaire est remplacé) ; Méthodes (NH4NO3 1 M) préférées aux Résultats (« NH4Cl »), doute noté. Les tests catalytiques sont des outcomes (Tableau 3), pas des branches ; protocole de test en characterizations.
- Zéolithes commerciales et essai sans catalyseur : sans voie (non synthétisés), dans sample_inventory avec raison.
- Rendement : « at or above 80% » est un rendement typique ; gardé en 80 % sur la voie de base seulement.
- Fig. 6 ouverte : valeurs déjà au Tableau 3, rien lu sur figure. Les figures 1 à 5 sont qualitatives (XRD, MEB) et décrites dans le texte ; Fig. S1 à S7 absentes en image (SI texte seulement), signalé en limite_reproductibilite.
- method_sources : cit49 (procédure de catalyse), cit24 (cristallinité relative), cit55 et cit56 (pyridine IR, SI) ; les renvois à leurs travaux antérieurs (cit32, cit43) relèvent du contexte et ne sont pas repris.
- Pureté de la silice non citée (« silica gel SiO2 (Sigma-Aldrich) ») ; nature gel ou fumée ambiguë (Méthodes contre Résultats), doute noté.
