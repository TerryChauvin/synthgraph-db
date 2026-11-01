# PMC3330020 — critique scientifique (journal de décisions)

- Tableau 1, acide acétique logβ = 8,3 pour Fe2+ : jugé `probleme`. Martell & Smith (via Harvey/LibreTexts) donnent log K1(Fe2+–acétate) = 1,40, donc logβ3 ≤ ≈ 4. L'attribution de 8,3 à un complexe de Fe3+ vient de mémoire (Lange's) : écrite comme « non vérifiée », placée dans `sources_not_found`.
- Oxalate 5,22 rapproché de β2(Fe2+) = 3,05 + 2,10 = 5,15 (μ = 1 M) : les constantes du tableau sont d'ordres différents, d'où `probleme` sur la comparaison acétate/oxalate qui fonde l'« exception ».
- Éthanediol logβ 9,67 : aucune valeur trouvée ; un diol neutre ne peut pas égaler tris(en)fer(II). `probleme` motivé par la chimie et l'absence de source, pas par une source contraire.
- SGEn jugée `incoherente`/`non_reproductible` : même avec seulement 3 en par Fe (6 équivalents basiques) contre ≈ 2–3 équivalents acides, le mélange est basique ; on ne peut pas descendre à pH 6,5 avec de l'ammoniaque. Calcul robuste quelle que soit la quantité d'en, d'où le verdict fort.
- pKa de l'éthylènediamine : PubChem ne donne que les valeurs à 0 °C (10,71 ; 7,56) ; j'ai calculé la spéciation avec elles et avec les valeurs usuelles à 25 °C (≈ 9,9 ; 6,9, non sourcées). Conclusion identique : en libre < 0,02 % à pH 6,5.
- « Saturated solution » : `probleme` pour l'acide acétique et l'éthanediol (miscibles), `ok` pour l'oxalique (solide). Conséquence concrète : quantité d'organique, donc de carbone, indéfinie.
- SGOc : précipitation probable de FeC2O4·2H2O après réduction (pKsp 6,5 → ≈ 0,1 g/L) ; source ChemicalBook (secondaire) faute de mieux, statut `reserve` seulement.
- CFSE : j'ai recalculé −0,40 Δo (oct) et −0,27 Δo (tét, Δt = 4/9 Δo) ; la conclusion qualitative des auteurs tient, mais l'argument double-compte une énergie déjà incluse dans logβ et la géométrie tétraédrique de Fe2+ en solution aqueuse n'est pas étayée → `probleme`.
- Mécanisme proposé à la place de celui des auteurs : xérogel de sels + organiques, auto-combustion nitrate/organique, carbone issu aussi de l'acide ascorbique (oublié par les auteurs). Appui : revue PMC11431264 (2024) sur les gels précurseurs nitrate/chélatant.
- Électrode : DMP comme solvant du PVDF retenu comme `reserve` (solvant latent, gels thermoréversibles, PubMed 18366217) plutôt que `probleme`, car le PVDF s'y dissout à chaud.
- Comparaison base : 4 autres publications LiFePO4 (650–750 °C sous Ar/H2) ; 600 °C sous N2 reste dans la plage, `ok`.
- Recherches web : 6 recherches + 2 lectures de page. Crossref bloqué : DOI de Padhi 1997 pris dans fondateurs.md ; aucun DOI nouveau à vérifier (sources citées par URL).
