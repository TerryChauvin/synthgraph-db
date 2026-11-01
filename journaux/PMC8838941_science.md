# PMC8838941 — critique scientifique (journal de décisions)

- Bilan carbone du WRN estimé à partir de la composition (amidon 44,4 % C ; protéines ≈ 53 % ; lipides ≈ 77 %) : ≈ 10,8 g C/100 g. Ces teneurs des protéines et lipides sont des moyennes de manuel ; elles ne servent qu'à des ordres de grandeur (rétention 65 % dans HTC, ≈ 38 % dans les produits finaux).
- « Sans pollution secondaire » classé `reserve` et non `probleme` : c'est une affirmation de discussion, pas un paramètre de synthèse.
- `probleme` Table 3 Cr(VI) : à Ce = 10 mg/L, Langmuir donne 0,164 et Freundlich 0,022 mmol/g (facteur 7), avec deux R2 > 0,99. Pour Pb, les deux modèles concordent à ±20 %, donc l'erreur porte sur Kf du Cr (recopie ou unité), pas sur la méthode.
- Cinétique d'adsorption : q_e expérimentaux = C0/(A·D) à 0,3 % près (élimination totale) ; pas de `probleme`, mais l'argument « chimisorption » par le R2 du pseudo-second ordre est jugé non étayé.
- Cr(VI) dosé seul par diphénylcarbazide : réserve « réduction en Cr(III) », appuyée sur la revue Mohan & Pittman 2006 (DOI donné de mémoire, à vérifier).
- AC-Cr/AC-Pb : −36 % de BET pour 1–2 % de prise de masse ; je demande un témoin sans métal plutôt que de conclure au bouchage.
- CQDs : frange de 0,283 nm « (020) » : graphite (020) = 0,107 nm, aucune distance du graphite vers 0,28 nm, d'où `probleme`. Comparaison avec PMC6769153 et PMC7022538 (0,21–0,22 nm).
- CQDs/TiO2 : carbone 0,442 g > prise de masse 0,40 g. Gardé en `reserve`, car une perte de TiO2 au centrifugeage est plausible ; l'annotation « ≈ 85 % de TiO2 » de l'extraction est à corriger (70–75 %).
- Indexation TiO2 recalculée (anatase a = 3,785, c = 9,514 Å ; rutile a = 4,594, c = 2,959 Å) : (213) correct, (004) faux (0,238 nm), 0,169 nm = rutile (211).
- `probleme` bande interdite 1,55 eV : un composite à 70–75 % de TiO2 ne voit pas sa bande changer ; c'est le seuil d'absorption du carbone (Makuła 2018).
- `probleme` lux : V(λ) à 405 nm encadré par HyperPhysics (0,000396 à 400 nm, 0,00121 à 410 nm) ; 8×10^4 lx donnent 10–30 W/cm2, impossible pour 20 W. La table CVRL n'a pas pu être chargée (DNS bloqué).
- `probleme` photocatalyse : pas d'équilibre à l'obscurité, colorants cationiques à 4 g/L de catalyseur (Rochkind 2015). Nuance retenue : 35 mg/g cumulés sur 7 cycles dépassent une monocouche estimée (≈ 20 mg/g sur 50 m2/g), donc une dégradation réelle existe à long terme.
- 405 nm = 3,06 eV > seuil du rutile : réserve « pas une preuve d'activité visible », Scanlon 2013 cité pour le contexte anatase/rutile (les valeurs 3,0/3,2 eV sont de manuel).
- XPS 288–289 eV attribués à C=C par les auteurs : je les lis O–C=O, ce qui contredit la disparition des carboxyles vue en IR.
- CQDs/TiO2-4 : `invérifiable` / `non_reproductible`, faute de Table S2.
- Recherches web : 8 (Wang & Kaskel, Sevilla & Fuertes, Mohan & Pittman, Rochkind, Makuła, Scanlon, V(λ) ×2) ; 2 accès directs échoués (cvrl.org, wikipedia : DNS).
