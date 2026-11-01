# PMC9069485 — critique scientifique (journal de décisions)

- d(002) de GP : Bragg avec λ = 1,5406 Å donne 3,81 Å pour 2θ = 23,33° (3,72 Å correspondrait à 23,90°), alors que 22,93° redonne bien 3,88 Å pour SGP. Jugé `probleme` d'auteur sur la voie GP ; l'expansion réelle est ≈ 0,07 Å, pas 0,16 Å.
- Tableau S1 : Re + Rs + Rct = 52,32 Ω pour SGP après 10 cycles contre Rtotal 50,38 (= Rs) ; les trois autres colonnes bouclent. `probleme` sur SGP, sans effet sur le classement SGP < SnS2.
- « He–Ne (532 nm) » : contradiction interne. Classé `probleme` (et non simple vocabulaire), parce qu'ID/IG dépend de l'énergie laser (Cançado 2006) : les valeurs 0,92/1,04 ne sont pas comparables à la littérature tant que la longueur d'onde reste inconnue.
- « Trois ordres de grandeur » pour 3630 (3,56 ordres) : jugé acceptable, laissé en `reserve` dans le contrôle D(Li+). Point plus utile : un facteur (1,54/0,81)² = 3,6 de ce rapport vient des seules aires d'électrode.
- D(Li+) recalculé à l'identique avec n = 4,4, C = 1×10−3 mol/cm3 et σ en Ω s−1/2 : l'unité Ω cm2 s−1/2 du tableau 1 est donc fausse. Classé erreur d'auteur dans `article_level`, `reserve` dans la voie.
- Masses de GO et de SnS2 absentes pour le papier : mis en `reserve` (bilan), et non en `probleme` ; c'est un manque de reproductibilité, pas une incohérence. Il justifie `reproductible_avec_reserves`. Cohérence vérifiée : 60 % de SnS2 implique une perte de ≈ 33 % de la masse du GO, plausible.
- Mécanisme SGP en `a_revoir` : la vapeur d'eau à 180 °C réduit déjà le GO (Zhou 2009), et le témoin à l'eau ne mesure pas la réduction du carbone. Le rôle de « réducteur » du thioacétamide n'est donc pas démontré ; seul son rôle de stabilisant l'est. J'ai préféré l'équilibre d'hydrolyse SnS2 + 2 H2O ⇌ SnO2 + 2 H2S (Le Chatelier) à l'« oxydation » des auteurs (Sn reste +IV).
- Soufre élémentaire possible dans le papier (GO + H2S → S0) : seule source trouvée, un brevet USPTO (US 8 609 183), retenu faute d'article primaire ; cela met en doute la lecture EDX « S/Sn ≈ 2 » et la teneur de 60 %.
- Rendement coulombique de SnS2 seul (51 %) contre la borne de 4,4/8,4 = 52 % si la conversion est irréversible : sert d'argument de cohérence, et non de problème.
- Synthèse de SnS2 : S/Sn = 2,0 exactement, sans excès ; mis en `reserve` (rendement en Sn possiblement incomplet), pas en problème, car la DRX ne montre pas d'impureté.
- LiFePO4 commercial à 74 % de rendement initial avec une coupure à 4,5 V : signalé en `reserve` (oxydation probable de l'électrolyte), voie `douteuse`.
- Rs « SEI » avant tout cyclage : attribution du circuit jugée discutable (`reserve`), sans effet sur les conclusions.
- Recherches : 7 recherches web ; la page Monash n'a pas pu être lue (DNS) et doi.org est bloqué par le proxy, donc les DOI de Zhou 2009, Chen 2010 et Cançado 2006 ne sont pas relevés. Le DOI de Zhang 2011 (10.1021/es202012b) vient de la bibliographie de l'article, il n'a pas été vérifié. Rien n'a été ajouté à fondateurs.md ni à constantes.md (Crossref bloqué).
- Pressions de vapeur de l'eau (2,7 bar à 130 °C, 10 bar à 180 °C) données de mémoire comme valeurs de table NIST arrondies, sans consultation en ligne.
