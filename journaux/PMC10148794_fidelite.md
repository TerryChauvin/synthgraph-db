# Journal critique de fidélité PMC10148794

- Ma liste d'échantillons avant ouverture de l'extraction : NC5 (hot-injection, Méthodes), NC6/NC8/NC12 (Cs-octanoate, durées 30 s / 2 min / 30 min), PTF (film polycristallin), NC solids (films de NC préformés). Même liste que `sample_inventory`.
- Écart avec l'inventaire : le fichier Peer Review cite NC5.1 (lot un peu plus petit) et un mélange NC5.1 + NC5.5 (Fig. R1). Absents de l'inventaire ; constat `manquant` probable, sans voie à créer car aucun protocole écrit.
- Valeurs de synthèse vérifiées une à une pour NC5 (0,815 g, 2,5 mL, 40 mL, 75 mg, 183,8 mg, 2 mL x2, 5 mL, 0,5 mL, 100/120/170 °C, 15 s, 11 627 g, 1860 g, 10 min), NC6 (225 mg, 2,9 g, 0,2 M, 5 mL, 55 µL, 155 µL, 0,1 M, 0,05 M, 5 min) et PTF (0,2 M, 1:1, 20 µL, 4000 r.p.m., 100 °C, 10 min) : toutes conformes.
- Attribution NC6/NC8/NC12 : « respectively » (30 s, 2 min, 30 min) et maxima de τs (« 200 K, 260 K, 320 K for NC12, NC8, NC6 ») bien rangés ; FSS 1,6/1,2/1,1 meV pour NC6/NC8/NC12 correct et cohérent avec Fig. 3c (Ω ≈ 2,4 ; 1,8 ; 1,7 ps^-1 lues sur l'image).
- FSS 1,7 meV de NC5 : le texte principal ne nomme pas l'échantillon ; la réponse aux relecteurs écrit « for sample NC5 » et Fig. 2j montre NC5 dans la série. Rangé en conforme, pas de constat.
- Aucune valeur `from_figure` dans l'extraction : j'ai ouvert Fig. 1, 2, 3 ; rien à vérifier. Fig. 3b (τs vs T) n'est pas reprise : constat `mineur` probable, car les durées de vie sont la mesure principale mais pas un résultat de synthèse.
- Constat `faux` sûr : substrat de verre rangé en « 10 mm » alors que l'article dit 10 mm × 10 mm.
- Constats `non_cite_a_tort` : « All procedures are done in a nitrogen-filled glove box » (PTF) n'est porté que par l'étape de recuit ; « room temperature ambient conditions » (NC6/8/12) n'est porté que par l'étape 6. Sûr pour PTF (phrase « all procedures »), probable pour NC6 (phrase de la méthode, pas de chaque étape).
- `deduit` : « jusqu'à turbidité » (NC5 étape 7) n'est pas dans l'article, qui constate seulement que le mélange est devenu trouble.
- Écarté : CR39 (technique CTA) n'est pas une source de méthode au sens de la règle du 2026-10-13 (pas de « according to », renvoi de technique de mesure) ; ne pas l'ajouter. Écarté aussi : XRD « (101), (121), (202) » non repris dans les caractérisations (détail de rapport, pas de constat).
- method_sources : CR52 et CR53 sont les deux seuls renvois de préparation ; les trois entrées sont justes.
- Annotations : mécanismes écrits comme hypothèses (« Probablement », « vraisemblablement ») ; le texte n'en donne pas, donc `mecanisme_check` ok.
