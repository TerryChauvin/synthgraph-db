# PMC11001879 — critique scientifique (journal de décisions)

- Teneurs des composites : la recette écrite (2 mmol Mg + 2 g d'AC) donne 0,399/(0,399+2) = 16,6 % de MgFe2O4 ; 25/45/65 % exigeraient 1,7/4,1/9,3 fois les précurseurs. Classé `probleme` (bilan), pas seulement manque.
- Borne de mélange SBET (1−w)·2134 + w·178 : 1645/1254/863 m2/g contre 1897/1645/1223 mesurés. Un dépôt d'oxyde ne peut pas dépasser cette borne ; 1897 m2/g correspond à w ≈ 0,12-0,17, ce qui rejoint le calcul de la recette. `probleme`.
- Calcination sous air à 550 °C appliquée aux composites (« same method ») : j'ai retenu que l'AC brûle vers 500 °C à l'air. Seule source accessible : l'énoncé de fidélité de l'ASTM D3466 (« au voisinage de 500 °C »). Les recherches sur l'oxydation catalysée par l'oxyde de fer n'ont rien donné de chiffré (un brevet sur mousse de carbone dit même que 5 % d'oxyde de fer ne baisse pas le début d'oxydation) ; l'affirmation « catalysée » reste de la chimie générale.
- Capacité 870 F/g : borne faradique 2F/M = 965 C/g, soit 1930 F/g sur 0,5 V pour la ferrite seule ; MF45-AC exige 1816 F/g de ferrite (94 %), impossible avec 16,6 %. `probleme` ; Brousse 2015 cité pour « comportement batterie → mAh/g ».
- Cyclage à 3 A/g : rétentions recalculées = valeurs finales / valeurs à 1 A/g (89,7 ; 94,1 ; 95,0 %) ; rapporté à 396 F/g (3 A/g) on aurait 209 %. `probleme` de cohérence entre sections.
- Constante de maille : a0 = 2d/√3 est la formule hexagonale (d100). Avec 30,47° et Cu Kα supposée (λ non déclarée), a = 8,29 Å correct, 3,38 Å avec leur formule ; 4,9-5,5 Å ne vient d'aucun pic listé. `probleme`.
- Indexation : (420) éteint en Fd-3m (h+k+l = 6 ≠ 4n), (311) à 35,5° absent, 36,97/37,08° = (222), 55,78° loin de (511) 57,06°. Hypothèse MgO (36,9 ; 42,9 ; 62,3°) envisagée puis non retenue (63,05° ne colle pas) : non écrite dans le JSON.
- Déformation : ε·D ≈ 0,40 nm constant (même β) contre 0,114 nm attendu au (311) avec K = 0,9 → facteur ≈ 3,5 ; équations 5-6 absentes, donc `reserve` et non `probleme`.
- SBET de MF 178 m2/g contre 86 m2/g géométriques pour 15,5 nm (ρ = 4,51 g/cm3 calculée avec a = 8,38 Å, Z = 8) : `probleme`.
- Électrode 80 % noir / 10 % actif : lecture littérale retenue (comme l'extracteur) ; `probleme` parce que la contribution du noir n'est pas soustraite (Stoller & Ruoff 2010), avec la mention qu'une inversion d'écriture est possible.
- ASC : E = ½·448·0,5²/3,6 = 15,56 Wh/kg exactement ; facteur 4 possible si 448 est une capacité d'électrode → `reserve` (équations absentes).
- AC : « rapport molaire 2:1 » KOH/écorce sans sens pour une biomasse → lu comme massique, `reserve`. Porcelaine + KOH fondue signalée (attaque des silicates), chimie générale.
- FTIR AC : attributions C=C/C=N à 2316/2044 cm-1 et C–H à 1036 cm-1 signalées en `reserve` (pas d'effet sur la synthèse).
- Mécanisme MF45-AC `a_revoir` : conversion en spinelle à faire sous N2 pour garder le carbone ; proposition sans source dédiée.
- DOI non vérifiés (Crossref bloqué) : Lillo-Ródenas 2003 (10.1016/S0008-6223(02)00279-8, DOI non retrouvé par la recherche), Brousse 2015 (10.1149/2.0201505jes, DOI non affiché par la recherche), Wang & Kaskel 2012 (10.1039/c2jm34066f, page RSC trouvée), Stoller & Ruoff 2010 (10.1039/C0EE00074D, confirmé par la recherche).
- 8 recherches web, 1 fetch échoué (PDF ASTM, hôte injoignable).
