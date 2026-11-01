# Journal critique de fidélité PMC5727554

- Liste d'échantillons établie avant l'extraction : P25 (Fig. 2a), nanofeuillets après hydrothermal (2b), nanotubes lavés HCl (2c), recuits 400, 600, 800 °C (2d-f). Identique à `sample_inventory` ; P25 sans voie est justifié par la règle « échantillon commercial » du RUNBOOK, donc pas de constat.
- Valeurs lues sur figure vérifiées une à une avec les images : σ = 2,01 (Fig. 8), 2,73 et 2,02 (Fig. 10a, 10b), 18,5 (Fig. 12), 2,83 (Fig. 4, en annotation). Écart nul, aucun constat. Pic Na en EDS (Fig. 6) : intense en (a), résiduel très faible en (b), conforme à « strongly reduced ».
- Tableau 1 : puretés chiffrées (NaOH 99,1 ; P25 ≥ 99,5 ; HCl 99,7 ; eau « 18 Ω ») absentes du champ purity. Constat `mineur`/`sure` : l'extracteur l'a signalé en doute mais l'information est dans l'article ; rien ne dit que la citation de la rangée serait refusée.
- Broyage au mortier d'agate des échantillons recuits : absent du JSON (aucune occurrence « agate »). `manquant`/`sure`, car c'est une étape de préparation avant mesure.
- SEM seulement dans la voie 400 °C alors que le texte parle de « each annealing temperature » et que la légende Fig. 9 range SEM d) à 600 °C : `manquant`/`probable` (le texte ne détaille pas ce que montre le MEB à 600 °C).
- Étapes 5-7 de TiO2NT-AW : `deduit`/`probable`. Le séchage décrit est celui de l'échantillon qui est ensuite divisé ; l'article ne dit pas que (c) a subi centrifugation, lavage et séchage avant mesure. Le doute de l'extracteur ne couvre que le séchage.
- Annotation « disparition du pic Na » : plus forte que l'article et que la Fig. 6b (pic résiduel). `mineur`/`sure`.
- Eau Milli-Q citée dans les réactifs, jamais attribuée à une étape ; eau de lavage dite « distilled ». Solvant de NaOH laissé `not_stated` à bon droit, donc seulement `mineur`/`probable` pour demander une note.
- Écarté : `succeeded=false` pour TiO2NT-800 (choix d'interprétation sans texte contraire, mis dans `notes`) ; « hours » contre « h » (cosmétique) ; step 1 `not_stated` durée/température (l'agitation est l'étape 2).
- Écarté : Eg = 3,28 eV contre intersection graphique de la Fig. 13 vers 3,20 eV : valeur écrite par les auteurs (378 nm correspond à 3,28 eV), donc fidèle ; consigné comme lacune de reproductibilité.
- `method_sources` : Kasuga (bib0050) et Nada (bib0080, HCl 3 h) conformes ; Le Bail, FullProf, JCPDS exclus par la règle de méthode du 2026-10-13. Pas de renvoi de méthode manquant.
