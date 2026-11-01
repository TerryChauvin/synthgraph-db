# PMC12505225 — critique scientifique (journal de décisions)

- Composite (ZnO-SiO2-700) jugé `incoherente` / `non_reproductible` : la méthode G4 citée (Mocioiu 2022, Gels, 10.3390/gels8080498, ouverte sur PMC9407535) ajoute le TEOS en dernier à acétate de Zn + eau + HCl + éthanol (EtOH:TEOS:H2O:HCl = 10:1:3:0,03, 10 % molaire ZnO, séchage 200 °C, 2 h de recuit). L'article inverse l'ordre, n'a pas d'éthanol, écrit « HCl 0,03 M » et 10 % en masse : quatre écarts à la source dont il se réclame.
- « HCl 0,03 M » lu comme le rapport molaire HCl/TEOS = 0,03 de Mocioiu : hypothèse, écrite comme « probablement ».
- Rôle de HCl contre Zn(OH)2 : calcul tampon acétate (0,164 mol AcO− par mol TEOS contre 0,002–0,03 mol HCl → pH 5,4–6,6). Mis en `reserve`, pas en `probleme`, car le volume d'eau est inconnu ; le Ksp de Zn(OH)2 n'a pas été utilisé dans le JSON faute de source vérifiée.
- Absence d'étape sol → poudre en `probleme` : le sol G4 ne gélifie qu'en un mois selon Mocioiu, donc 18 h de vieillissement ne donnent pas de poudre sans séchage.
- ZnO : 10 g Zn(OAc)2·2H2O / 100 mL EtOH = 12,7 g/100 g contre 3 g/100 g à 25 °C (PubChem/HSDB, lu dans l'extrait de recherche ; la page PubChem et un SDS n'ont pas pu être ouverts, erreur DNS). Mis en `probleme` malgré cela : l'écart est d'un facteur 4 et aucun chauffage n'est écrit.
- Décalage DRX : les 11 raies du ZnO pur sont à +0,42° de la fiche 05-0664 (fiche lue dans une annexe de thèse CMU, source secondaire), alors que celles du composite sont pile sur la fiche ; signalé en `reserve` (valeurs du composite peut-être prises à la fiche).
- Le pic du quartz à 27° (26,64° + 0,36°) est cohérent avec ce même décalage : je n'ai donc pas contesté la position, seulement l'identification sur un pic unique (contamination par mortier en agate possible).
- 579 cm−1 : deux attributions publiées (Si–O–Zn vitreux 560–568 cm−1 chez Mocioiu ; ZnO4 de la willémite 574–578 cm−1 chez Alibe 2018, Arch. Metall. Mater., 10.24425/118972). Gardé en `reserve` (preuve non discriminante), avec la bande 885–890 cm−1 comme test.
- « ZnSiO4 » en `probleme` (formule fausse) ; argument d'Alibe : trace de ZnO à 36,37° à côté de la willémite indexée, donc 36,2° est propre au ZnO. Les raies willémite vers 22 / 25,5° viennent de ma mémoire et sont marquées « à confirmer » ; 38,8° est vu dans PMC12018908 (extrait de recherche).
- Tridymite : pas de recherche web ; argument de chimie générale (cristobalite d'abord, tridymite pure rare) gardé en `reserve`.
- λ = 1,54 nm en `probleme` (sin θ = 2,73) bien que ce soit une coquille évidente : un lecteur qui recalcule avec la valeur écrite se trompe d'un facteur 10.
- Homogénéité du Zn (résumé/conclusion) contre « sparse and unevenly distributed » (Résultats) : `probleme` de cohérence entre sections.
- Pic EDS du carbone : alternative du ruban carboné ajoutée (non discutée par les auteurs), en `reserve`.
- Fardad 2000 (mésoporosité par catalyse acétique) non ouvert : cité seulement comme référence de l'article ; affirmation non mesurée ici (pas de BET).
- Recherches web : 4 WebSearch + 3 recherches Parallel, 2 pages ouvertes (Mocioiu sur PMC, Alibe PDF) ; WebFetch hors service (DNS), PubChem bloqué par le proxy.
