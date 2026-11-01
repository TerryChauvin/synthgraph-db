# PMC4726031 — critique scientifique (journal de décisions)

- Sels de Co et Ni (« Co(NO3)3·6H2O », « Ni(NO3)3·6H2O », Materials et Table S1) : jugés `probleme` sur les 5 branches qui les utilisent. Ni(NO3)3 n'existe pas, Co(NO3)3 n'est pas un réactif analytique courant ; pesée avec la formule écrite = +21 % de B (353,0 contre 291,0 g/mol). Le doute de l'extracteur est ainsi tranché : lire M(NO3)2·6H2O. Sources : PubChem CID 61630, Wikipedia Co(III) nitrate (secondaire).
- Interface Si–O–Fe (FTIR 3620 cm−1, 1022 → 1035 cm−1, Si 2p) : `probleme`, parce que la référence est la MMT brute alors que le composite a passé 5 h à 600 °C, dans la plage de déshydroxylation de la montmorillonite (400–700 °C, revue 2022 et LPSC 2009). Il manque le témoin « MMT calcinée ». C'est le contrôle 7 (preuve discriminante).
- Minéralisation de RhB (« degraded into H2O, CO2 ») : `probleme`, déduite de la seule décoloration à 554 nm ; sources : Lesniewicz 2024 (décoloration ≠ minéralisation), PMC3349318 (λmax des rhodamines dééthylées 552 → 498 nm).
- Exotherme à 163,9 °C, 30 % de perte : réinterprété comme réaction redox nitrate-citrate (φ = 1,20 calculé avec les valences de Jain 1981), et pas comme « transformation de l'acide citrique ». Laissé en `reserve` (interprétation, pas une erreur de protocole), mais repris en sécurité (auto-combustion dans le four).
- Jain, Adiga, Pai Verneker 1981 : référence relevée dans la bibliographie d'un article (usf.edu), DOI non vérifié, aucun DOI inventé.
- 36,37 % de LaFeO3 : non retrouvé (37,8 % avec la MMT brute, 39,9 % après perte au feu) ; il faudrait 94 % de rendement. EDS ≈ 51 %. Laissé en `reserve` : l'article ne dit pas comment il calcule.
- EDS O 19,82 % contre ≥ 40 % attendus : `reserve` (EDS semi-quantitatif), signalé pour qu'on ne s'en serve pas comme bilan.
- Bande interdite de « 2.65 eV » en introduction contre 2,15 eV mesurés : incohérence entre sections (contrôle 6), `reserve` ; plage publiée 1,86–2,36 eV (revue PMC8082458) et 2,34 eV en ellipsométrie (JPCM 2014).
- Hausse de Eg de 0,09 eV attribuée à la taille : contestée sans source (confinement négligeable à 12–15 nm pour un oxyde), `reserve`.
- Densité de LaFeO3 (6,64 g/cm3) calculée avec des paramètres de maille approximatifs, non relus sur la fiche JCPDS 37-1493 ; dit dans `calculs` et `sources_not_found`. Sert seulement à l'ordre de grandeur de la surface géométrique (25 m2/g contre 5,37 m2/g mesurés).
- Échange cationique : CEC de SWy-1 = 76,4 meq/100 g (Westrich 1998) → 10–13 % du La3+ peut passer dans l'interfoliaire ; utilisé dans le mécanisme proposé, sans valeur propre à la MMT de Zhejiang Sanding.
- LaNiO3 à 600 °C : `reserve` (bas de la plage de calcination publiée, phases secondaires possibles) ; figure S3 non lisible, donc invérifiable.
- Variantes -0,5 et -2 : `coherente` ; seul le volume de solvant manque. Charge théorique 23,3 % et 54,8 %.
- compare.py « LaFeO3 » : seule publication de la base, pas de comparaison.
- 8 recherches web ; rien ajouté à fondateurs.md ni à constantes.md (Crossref bloqué).
