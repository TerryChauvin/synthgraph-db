# Journal du complément — PMC11269599 (28/10/2026)

Ajouts seulement ; aucune valeur, citation, étape ni annotation existante retirée. `load.py check` : 0 erreur, 0 avertissement.

## Points de la sonde
- **pH** : l'article ne règle le pH que pour le test catalytique (7–11, optimum 9,0), déjà en résultats (`kobs_pH_*`). Pas de paramètre `ph` ajouté aux étapes de synthèse. Ajout d'une entrée `characterizations` « pH-métrie » (pH-mètre AD1030 Adwa ; tampons de la légende de la Fig. 8 : borax/HCl, NaHCO3/NaOH, phosphates). `ph` déclaré non cité pour le mélange chitosane/GO de la dernière voie.
- **vide** : « evaporated under vacuum » (Co-TPHPP, étape 4) : paramètre `atmosphere` = vacuum ajouté ; `pressure` reste dans `not_stated` car aucun niveau de vide n'est donné (la sonde signalait ce point, la case n'est donc pas contredite). Même case `pressure` ajoutée au séchage « in a vacuum » de Co-TPHPP-Cs.
- **purification (silice 60–120 mesh)** : réactif listé dans Matériaux sans étape ; probablement une colonne pour la porphyrine, mais non dit. Écarté (aucune étape inventée), consigné en `doubts`.
- **XRD** : positions de pics ajoutées en `outcomes` pour PHCS (6,42° ; 18,62°), Co-TPHPP-PHCS (22,8°), Co-TPHPP-Cs (20,81°), GO (10,32°), nanocomposite (9,60°). Chitosane de départ non ajouté (pas de voie).
- **UV-vis / bande interdite** : pas de bande interdite dans l'article. λmax de TPHPP et Co-TPHPP ajoutés en `outcomes` (`value_text`, plusieurs valeurs). Plage 200–600 nm (Instruments) ajoutée aux `conditions` des trois entrées UV–Vis existantes (seul champ existant enrichi, par ajout de texte).
- **PL** : résultat (220 / 80) déjà présent. Ajout d'une entrée Fig. 14 (plage 350–550 nm, t = 0–75 min) et du maximum d'émission ≈ 420 nm lu sur figure (`from_figure`). Excitation, appareil et concentration de NaTA non cités.
- **EDS** : la Fig. 5e imprime un tableau en % massique (C 23,10 ; O 74,53 ; N 1,53 ; Co 0,84). Ajouté avec `from_figure` et la légende de la Fig. 5 comme citation (règle des valeurs lues sur figure). Ce n'est pas de l'ICP.

## Autres ajouts
- Entrée COT (50 % en 60 min à 40 °C, conditions standard de l'abstract ; appareil non cité).
- `not_stated` de la grille étendue (48 ajouts) après recherche des mots-clés (stirring, rpm, nitrogen, dried, centrifug, filtrat, ice, ambient, triplicate, repeated) dans tout le fichier, annexes comprises : seuls « filtration » et « washed with distilled water » (recyclage du catalyseur) existaient, hors synthèse. Cases ajoutées par étape : agitation, atmosphère, mode d'addition, mode de refroidissement, séchage, lavage, purification, récipient, répétitions (voies de base TPHPP et nanocomposite seulement, pour ne pas alourdir les autres).
- `missing_fields` de la dernière voie : agitation du test, fluorimètre, GC–MS, COT, TEM.

## Non fait, et pourquoi
- Conditions du greffage et de la déprotection lues sur le schéma de la Fig. 2 (80 °C, 4 h, azote) : déjà traitées en `doubts` et limite de reproductibilité par l'extraction ; la règle du RUNBOOK range en « non cité » ce qui n'est lisible que sur un schéma.
- Aucune donnée de répétition, de puissance ou de fréquence : sans objet (pas de micro-ondes ni d'ultrasons de synthèse).

## Fragile
- Maximum de fluorescence ≈ 420 nm lu à l'œil (± 5 nm).
- Unités « ° » des angles XRD : omises dans les Instruments, prises des phrases de résultats.
- Tension du MEB : texte 10 kV, bandeaux de la Fig. 5 à 20 kV (doute noté).
