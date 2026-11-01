# Leçons du palier 1 : consignes scientifiques récurrentes et coût en jetons

Relecture faite le 2026-10-13 par l'orchestrateur, à la demande de l'utilisateur, sur 10 publications tirées au hasard parmi les 50 (graine 20261013) : PMC5122874 (CsPbX3, morphologies), PMC6266651 (V2C MXène), PMC3497326 (ZnO, tensioactifs), PMC10326808 (ZIF-8 creux), PMC7022538 (points de carbone verts), PMC2897037 (nanorubans SiC), PMC3107715 (Ag/gélatine), PMC5309769 (pérovskites, porteurs chauds), PMC8255795 (points de carbone micro-ondes), PMC9043336 (hydrogel GO/chitosane).

Ce qui a été lu : les critiques scientifiques (verdicts, 24 problèmes « résultats », 9 « mécanisme », 6 « bilan », 4 « sécurité », 3 « thermique », 2 « solubilité », 2 « cinétique »), les sources citées, les points « à vérifier avant de refaire », et les 16 sources réutilisées d'une publication à l'autre sur tout le palier.

## 1. Ce qui revient : huit contrôles à faire systématiquement

Ajoutés à `PLAUSIBILITE.md` (section « Contrôles qui reviennent »).

| # | Contrôle | Vu dans |
|---|---|---|
| 1 | Température contre récipient : consigne au-dessus du point d'ébullition sans reflux (SOCl2 80 °C, hexane 50 °C), ultrasons sans température, autoclave trop rempli ou pression non estimée | PMC9043336, PMC10326808, PMC3497326 |
| 2 | Tout en moles : réducteur insuffisant (gélatine contre 10 mmol Ag+), « excès » d'amine 7 fois moindre que l'acide, concentration impossible (HF 48 mol/L), solubilité dépassée (mélamine/DMSO) | PMC3107715, PMC5122874, PMC6266651, PMC9043336 |
| 3 | Grandeurs dérivées à recalculer : Bragg (facteur 1,10 constant), 4V/S contre diamètre BJH, signe de ΔS contre ΔG(T), colorimétrie d'une LED | PMC9043336, PMC3497326, PMC7022538 |
| 4 | Vocabulaire physique faux des auteurs : « blue shift » vers les nombres d'onde plus bas, ester « nucléophile », mésopore de 1,2 nm, « ablation laser » sans laser, polytype 2H non démontré, silicium « fondu » sous son point de fusion | PMC3497326, PMC5122874, PMC9043336, PMC3107715, PMC2897037 |
| 5 | Témoin qui change plusieurs variables (NaF + HF « sans Cl− » change aussi Na+, acidité, température ; éthanol miscible pris pour un gabarit) | PMC6266651, PMC10326808 |
| 6 | Cohérence entre sections : isolement décrit de deux façons, 6,9 contre 13,8 mg/mL in vivo, tri en taille impossible tel qu'écrit, tableau contre texte | PMC7022538, PMC8255795, PMC5309769, PMC3497326 |
| 7 | Preuve discriminante : FTIR qui ne distingue pas greffage et intercalation, bande IR hors plage mesurée, fluorophore moléculaire pris pour un point de carbone | PMC9043336, PMC10326808, PMC7022538, PMC8255795 |
| 8 | Sécurité non écrite : H2O2 + amine (exotherme rapporté par les auteurs eux-mêmes), DMSO + halogénure d'acyle, HF, autoclave, fibres de SiC | PMC7022538, PMC9043336, PMC6266651, PMC3497326, PMC2897037 |

Constat transversal : **les problèmes viennent des articles, pas des extractions**. Sur les 10 publications, aucune valeur extraite n'était en cause ; ce sont des erreurs de calcul, de vocabulaire ou de cohérence des auteurs, et des omissions. Les annotations `limite_reproductibilite` sont donc la bonne sortie, et le chimiste doit les lire avant la fiche.

## 2. Mécanismes qui reviennent, par famille

- **Pérovskites halogénées** : le rapport acide oléique / oléylamine (équilibre acide-base, Almeida 2018) commande la morphologie ; les ligands sont dynamiques et le lavage dégrade les nanocristaux (De Roo 2016) ; CsPbBr3 colloïdal est orthorhombique, pas cubique (Cottingham 2016) ; transformation réversible CsPbBr3 ↔ Cs4PbBr6 par les ligands (Palazon 2017). Les auteurs invoquent souvent un « nucléophile » ou une « neutralisation » que le bilan molaire ne permet pas.
- **ZIF-8 en eau** : la synthèse aqueuse demande un large excès de 2-méthylimidazole (Pan 2011) ; ZIF-L est la phase concurrente (Chen 2013) ; une « micro-émulsion » exige un liquide non miscible, l'éthanol n'en est pas un.
- **Argent par voie verte** : le réducteur doit être compté en équivalents (Raveendran 2003) ; le plasmon renseigne sur la taille (Agnihotri 2014) mais le décalage doit être lu dans le bon sens ; l'acide gluconique acidifie le milieu.
- **Points de carbone « bottom-up »** : la fluorescence peut venir de fluorophores moléculaires (Essner 2018) ; dialyse et comparaison dialysat/rétentat obligatoires ; rendement quantique selon l'IUPAC (Brouwer 2011) ; l'émission du film diffère de celle de la solution.
- **Oxyde de graphène** : Marcano 2010 pour les quantités, Dreyer 2010 pour la réactivité des fonctions ; un chlorure d'acyle ne survit pas à un séchage à l'air et à un lavage à l'éthanol ; Bragg à recalculer.
- **MXènes** : gravure LiF/HCl (Ghidiu 2014) contre HF ; le rôle de Cl− ne se démontre qu'à acidité et [F−] égales ; sécurité HF (Alhabeb 2017).
- **Hydrothermal** : taux de remplissage et pression de vapeur ; mélange tensioactif cationique + anionique précipite (Kaler 1988) ; le précipité avant autoclave devrait être identifié.

## 3. Bibliothèque de référence (nouveau)

- `references/fondateurs.md` : 52 papiers fondateurs et revues, par famille, **tous vérifiés sur Crossref** le 2026-10-13 (`references/verif_doi.py`, 0 échec). 16 d'entre eux avaient déjà servi à deux publications du palier.
- `references/constantes.md` : où prendre chaque constante (NIST WebBook, PubChem, NOAA CAMEO, ECHA, IUPAC Gold Book, COD) et ce qu'il faut recalculer ; table des valeurs vérifiées, qui grandit avec les critiques.
- Le critique scientifique part de ces deux fichiers avant toute recherche web ; une source trouvée pour la deuxième fois y est ajoutée après vérification.

## 4. Consommation de jetons

Mesures de cette session (jetons d'un sous-agent, entrée et sortie, cache compris) :

| Passe | Modèle, effort | Jetons par publication |
|---|---|---|
| Extraction ou mise à niveau format 2 | Sonnet, high | ≈ 280 k |
| Critique de fidélité | Sonnet, high | 210–290 k |
| Critique scientifique | Opus, high | ≈ 190 k (39 appels d'outils, dont les recherches web) |
| Correction | Sonnet, high | 160–240 k |
| **Total** | | **≈ 0,9 M par publication**, orchestrateur non compris |

450 publications restantes ≈ 400 M jetons au rythme actuel. Où ça part : chaque agent relit l'article entier (41 ko en moyenne, jusqu'à 220 ko), l'extraction JSON (66 ko en moyenne, dont la moitié en citations), `RUNBOOK.md` (19 ko) et les critiques (20 ko) ; le critique scientifique refait les mêmes recherches web d'un article à l'autre ; l'agent de correction réécrit le JSON après l'avoir lu en entier.

Ce qui change (appliqué) :

1. **Critique scientifique** : lit `review.py <PMCID> science` (vue sans citations : 19 k caractères au lieu de 48 k pour le JSON de PMC6199062) et part de la bibliothèque ; recherches web limitées aux points non couverts. Gain attendu : 30 à 40 % de cette passe.
2. **Agent de correction** : lecture ciblée (critiques, section Format du RUNBOOK, voies visées, passages cherchés par `Select-String`), modification du JSON par script. Gain attendu : 30 à 40 % de cette passe.
3. **Critique de fidélité** : inchangée. C'est elle qui garantit les citations ; rogner sa lecture ferait perdre la rigueur.
4. **Correction par l'orchestrateur** pour les petits cas : écartée après mesure. Aucune publication du palier n'a eu moins de 3 constats (médiane 10), et l'orchestrateur coûte plus cher par jeton.
5. **Effort `high`** conservé partout ; l'orchestrateur ne relit jamais une transcription d'agent et les rapports finaux restent courts.

Ordre de grandeur après ces changements : ≈ 0,75 M par publication, soit ≈ 340 M pour le reste du projet, sans retirer un seul contrôle. Le gros levier restant serait de ne faire qu'une critique (fidélité + science dans un même agent), ce qui ferait perdre l'indépendance des deux lectures : non retenu.

## 5. Non fait

- Les leçons sur le pilotage (règles d'héritage, sources de méthode, `route_removed`) ne sont pas encore reportées dans le fichier des défauts du skill.
- Les gains de jetons sont des estimations à partir des tailles de fichiers ; ils seront mesurés sur les 10 premières publications du palier 2.
