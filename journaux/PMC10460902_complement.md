# Journal de la passe de complément — PMC10460902 (28/10/2026)

Principe : ajouter seulement ; seules exceptions, les chaînes `conditions` des essais photocatalytiques (H2, dégradation), complétées par concaténation (texte d'origine conservé en tête).

## Points de la sonde écartés ou rattachés ailleurs
- agitation (rpm), centrifugation : 10000 rpm = séparation du photocatalyseur des prélèvements de 3 mL pendant l'essai de dégradation (annexe). Appartient à la mesure, pas à la synthèse : rangé dans `characterizations.conditions` (la mention existait déjà ; ajout du contexte complet). Aucune étape `centrifuge` créée.
- ultrasons : traitement de la suspension avant dégazage (H2) et avant l'agitation à l'obscurité (dégradation). Mesure, pas synthèse : dans `conditions`.
- puissance (W) : lampe Xe 300 W déjà présente ; complété par la référence du modèle et l'absence d'intensité lumineuse / distance lampe-réacteur.
- purification : faux positif (« k-point mesh » de la section DFT). Aucune purification dans la synthèse.

## Ajouts
- Résultats (45) : pour chaque échantillon (l'article dit « all the samples ») pics XRD 13,1° et 27,4° ; XPS C 1s (288,2 / 286,4 / 284,8 eV) et N 1s (398,2 / 399,8 / 400,8 eV) ; RMN 13C (157,2 / 165,6 ppm) ; RMN 1H (9,05 / 1,03 / 3,61 ppm) ; pic respiratoire IR à 810 cm−1 ; type n (Mott–Schottky).
- Conditions de mesure : nouvelles entrées `characterizations` (14) : RMN 1H (3 voies), Mott–Schottky (3 voies, cellule à trois électrodes ; électrolyte non précisé), RMN 13C / XPS pour GCN et NCN, FT-IR et PL/TRPL pour GCN (résultat 5,93 ns lu sur Fig. 6B, déjà en outcome), DFT (VASP, PBE, 600 eV, supercellule 4 × 4, vide 15 Å) pour GCN et VCN.
- `conditions` des essais complétées (6 entrées) : masse de catalyseur, volumes, TEOA, dégazage, GC/TCD, durée 2 h, CIP/TC concentrations, lampe, ultrasons + 30 min d'agitation à l'obscurité, centrifugation, spectrophotomètre, pièges (méthanol, t-BuOH, BQ), longueurs d'onde, dix cycles.

## Cases `not_stated` ajoutées (4)
- GCN étape 2 : `gas_flow` (air dans un creuset couvert, type de four inconnu, débit jamais cité ; cherché dans tout le texte et l'annexe).
- `repetitions` aux trois voies (aucun nombre de lots ni de répétitions de synthèse cité).
Non ajoutés : refroidissement (déjà `cooling_rate`), pH, lavage, séchage, centrifugation de synthèse, vieillissement (sans objet pour un traitement thermique de poudre), `pressure` de NCN (déjà déclaré).

## Non fait / fragile
- Conditions absentes de l'article, consignées dans un `doubt` : dégazage BET, plage et pas XRD, référence et plage UV-vis DRS, longueur d'onde d'excitation PL, mode AFM, électrolyte, agitation et intensité lumineuse des essais, mode de dépôt de Pt. Les champs `conditions` restent à null.
- AQE de GCN et NCN (Fig. S4) et dégradation de TC (Fig. S6) : annexe sans les données, donc pas ajoutés.
- Aucune figure rouverte : toute condition retenue figure dans le texte ou l'annexe.
