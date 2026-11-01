# Journal du complément — PMC11891312

Lecture : sonde, RUNBOOK (grille), extraction entière, texte entier (corps, annexe SI, légendes), Fig. 1 et Fig. 2 ouvertes.

## Points de la sonde écartés
- débit de gaz, pH, vitesse d'addition, puissance (W) : les occurrences viennent de l'essai photocatalytique (débit d'air 1 à 2.5 mL/min, pH 5 à 9, deux lampes de 60 W), déjà portés par la caractérisation « Plan d'expériences RSM » et par les noms d'outcomes. Ce ne sont pas des consignes de synthèse. Les cases `power` des sonications restent déclarées non citées (la puissance de 60 W est celle des lampes).
- ultrasons : durées (18 et 30 min) déjà extraites ; seule la fréquence manquait (ajoutée en `not_stated`).
- TEM/SEM, EDS : Table 1 ne donne aucune condition (tension, comptage) ; recherche de « kV », « voltage » sans résultat : conditions laissées à `null`, rien inventé.
- PL : texte purement qualitatif, excitation 403 nm déjà en conditions ; aucun résultat chiffré à ajouter.
- électrochimie : faux positif (« band gap », « adsorption ») ; aucune mesure électrochimique dans l'article.
- BET MCM-41 : dégazage non attribué à MCM-41 (doute existant), laissé tel quel.

## Ajouts
- Paramètres (7) : `addition_mode` (« drop by drop » CdS étape 1 et CT étape 2, « quickly » CdS étape 2) ; `drying_mode` = oven sur les 4 étapes de séchage, lu sur l'organigramme Fig. 1 (`from_figure`, citation = légende).
- `not_stated` (8) : `ph` (MCM-41 étape 1, CdS étape 2, CT étape 3), `gas_flow` (calcination MCM-41), `volume` (lavage CdS), `frequency` (sonications CT et CTM), `atmosphere` (CT étape 3). Recherche de « pH », « flow », « frequency », « kHz », « atmosphere » dans tout le fichier : seuls les usages liés à l'essai photocatalytique ressortent.
- Résultats (9) : énergies de liaison XPS de CTM (15%) (Ti 2p, Cd 3d, S 2p, O 1s, Si 2p), attribution aux composantes telle que le texte l'écrit ; O 1s : deux pics sans attribution individuelle.
- Conditions de mesure (4) : méthode de calcul de la bande interdite (Kubelka-Munk, Tauc, n = 1/2 à 3) pour CT, CTM (5%), CTM (15%) ; triplicat et seuil 0.05 des essais.
- Équipement (1) : photoréacteur d'après la Fig. 2 (pH-mètre, agitateur, pompe à air, circuit d'eau froide), en entrée de caractérisation car les étapes ne décrivent pas l'essai.
- Doutes (2) : énergies XPS très éloignées des valeurs usuelles (aucune correction) ; origine des ajouts lus sur figure.

## Rattachements non évidents
- Triplicat et photoréacteur sur CTM (15%) : l'essai est mené sur ce matériau (les autres CTM sont comparés en Fig. 9 sans protocole propre).
- Aucune `not_stated` retirée ; aucune valeur existante modifiée.
- Fragile : l'état de `drying_mode` repose sur l'organigramme seul (le texte dit « dried ») ; la température de séchage de CTM y diffère du texte (déjà en doute).
