# Journal de la passe de complément — PMC10200858

Sonde : 8 points. Résultat : ajouts seulement, `load.py check` à 0 erreur (134 citations vérifiées).

## Points de la sonde écartés
- **pH** : les 3 occurrences décrivent le tampon universel pH 2–12 du test d'adsorption, déjà dans `conditions` de la caractérisation UV-Vis. La synthèse n'a aucun pH (milieu HCl 4 M, aucun ajustement) : pas de case `ph` en `not_stated`.
- **vide** : étape 7 déjà `atmosphere = vacuum` avec `pressure` déclarée non citée (niveau de vide absent) : rien à ajouter.
- **TEM/SEM** : le texte ne donne ni tension ni nombre de particules comptées. Seul « estimated from numerous HRTEM images » est ajouté en `conditions` (HRTEM des deux voies).
- **ICP/EDS** : aucune condition (mise en solution, tension) dans l'article ; seul « EDS mapping » est ajouté en `conditions` de l'EDS.
- **UV-vis / band gap** et **électrochimie** : faux positifs. L'UV-Vis sert à doser le bleu de méthylène à 664 nm, pas à mesurer une bande interdite ; « capacity » renvoie à l'adsorption (Qmax 176,70 mg/g, déjà extrait), pas à une électrode.

## Ajouts
- Étapes 2 et 3 : `addition_mode` en `value_text` (« gradually », « slowly »), qualitatif. `addition_rate` reste en `not_stated` : aucun débit ni durée d'addition n'est chiffré. Aucune case retirée.
- `not_stated` ajoutés : étape 3 `addition_order` (ordre FeCl3 / γ-CS ambigu, voir doute existant), étape 4 `autoclave_volume` et `cooling_mode` (« Teflon container » sans volume ni refroidissement), voie de base `repetitions` (nombre de lots jamais indiqué). Recherche sur tout le fichier (Méthodes, Résultats, légendes, notes) ; l'article n'a pas d'annexe.
- Non ajoutés car sans objet ou déjà couverts : `fill_fraction`, `pressure`, `heating_rate` (déjà là), `centrifuge_speed` (pas de centrifugation), `power`/`frequency` (pas de micro-ondes), purification autre que le Soxhlet.
- XPS : 7 énergies de liaison ajoutées en `outcomes` de la voie de base (Si2p, O1s, N1s ×2, C1s ×3), citations prises dans le texte. Instrument et source XPS absents de l'article.
- XRD grand angle : `conditions` (Cu K, détecteur Lynxeye) reprises de la description générale « Powder X-ray diffraction patterns », qui vaut pour les deux modes ; pas de plage ni de pas.
- Deux entrées `characterizations` UV-Vis ajoutées pour consigner les conditions des séries pH / dose / temps (légendes des Fig. 11, 12, 14) dont les résultats sont déjà en `outcomes`, une par voie concernée (Fe-SBA-15 : série en dose seulement).

## Fragile
- La légende de la Fig. 11 donne 1 h, celle de la Fig. 12 et le texte 30 min : écart déjà en doute, conservé tel quel dans `conditions`.
- Aucune valeur lue sur figure ; aucune figure ouverte (pas nécessaire).
