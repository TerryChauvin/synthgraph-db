# Journal de la correction PMC9036664

- Constat 1 (durée de vie avec Fe3+) : la condition 9 μmol L−1 est lue sur la légende de la courbe de la Fig. 7f (ouverte et confirmée). Elle est mise dans le nom de la propriété, avec `from_figure: Fig. 7f` ; la citation reste la phrase du texte, qui porte 4.73.
- Constat 2 (séries) : seules des valeurs lues avec une marge d'environ ±3 % sont ajoutées, à 2 chiffres significatifs : Fig. 7a (F0/F à 9, 90, 180, 360 μmol L−1 : 1,2 ; 1,6 ; 1,7 ; 1,7) et Fig. 7d (9 et 180 μmol L−1 à 298 et 338 K). Les points intermédiaires, plus serrés, sont laissés de côté. La tendance imprimée dans le texte (« decreases as the temperature rises ») est ajoutée en `value_text`. Citations : légendes (a) et (d) de la Fig. 7.
- Constat 3 : conditions du test (15 μL à 90 μmol L−1 dans 3 mL, 1 min ; série en température, 10 min de maintien puis 1 min) ajoutées en `conditions` de la fluorescence, recopiées de la section Méthodes.
- Constat 4 (XPS), non couvert par les décisions de l'orchestrateur : le texte donne les énergies de liaison, donc ajoutées (C 1s dans l'entrée existante, O 1s et N 1s en deux entrées). Les attributions ne sont pas recopiées : les symboles de liaison sont perdus dans le texte (balises SVG). « five peaks » pour quatre énergies : doute.
- Constat 5 : R2 garde 0.909 (texte) ; écart avec la Fig. 7b (0.887) en doute et en annotation `limite_reproductibilite`.
- Constat 6 : liste d'ions texte/Fig. 6 en doute et en annotation (Ba2+, Cu2+, Zr2+/Zr3+).
- Constat 7 (rôles déduits) : rôles gardés dans les réactifs (champ attendu par le schéma), doute explicite disant qu'ils viennent de l'extracteur ; `mecanisme_analyse` les présentait déjà comme hypothèse.
- Constat 8 (étape 6) : séparée en deux étapes (mise dans le moule ; ajout des trois réactifs dans l'ordre). L'ordre d'ajout est écrit dans le texte (« in sequence »). Les cases `not_stated` sont réparties entre les deux ; la cuisson devient l'étape 8. Aucune branche ne référence ces numéros.
- Constat 9 (« High yield ») : `yield` reste `not_stated` (aucun nombre) ; la mention qualitative figure déjà dans l'annotation `limite_reproductibilite` existante, rien d'ajouté.
- Science : les 4 `probleme` sont des annotations (`securite_analyse` complétée pour l'éther de pétrole ; trois `limite_reproductibilite` pour la purification, la frange 0,21 nm et l'extinction par Fe3+). Aucune valeur modifiée. DOI non vérifiés non repris ; sources citées par nom seulement (Ullah et al. 2014, NOAA CAMEO).
- `mecanisme_analyse` de NCDs réécrit selon la décision de l'orchestrateur (dégradation partielle, oligomères triazine, points de polymère faiblement carbonisés) ; `mecanisme_auteurs` intact.
- Masse de mélamine et nom du tensioactif : doutes existants gardés, ajout dans une annotation `limite_reproductibilite` de LSMF_foam (absente jusque-là).
- Fig. 7d : 298 à 338 K lus contre 298 à 348 K dans les Méthodes, noté en doute.
