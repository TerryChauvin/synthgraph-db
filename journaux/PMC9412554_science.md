# PMC9412554 — critique scientifique (journal de décisions)

- Teneur en solide « 25 % » (§ 2.2) : recalcul 8,30 g / (8,30 + 35 × 0,944) = 20,1 %. Classé `reserve` et non `probleme` : la chimie reste juste (rapport PMDA:ODA = 1,001), seule la concentration à reproduire est incertaine.
- FTIR (§ 3.1) : la phrase « 1648 cm−1 … tertiary amide, which indicated that imidization was completed » est l'inverse de l'usage (l'amide I signe l'acide polyamique). Classé `probleme` sur la voie PI parce que le taux d'imidation, déjà sans programme thermique, n'est donc démontré par rien. Source : notice Bell Labs « IR studies of polyimides I » (résumé seulement) ; les bandes 1780/1720/1380/725 cm−1 sont du savoir de manuel.
- « Titania powder » (Materials) contre « titanium powders » (§ 2.3) : retenu titane métal, seule lecture compatible avec le mécanisme Ti + HCl → TiCl3 + H2 ; TiO2 ne se dissoudrait pas dans HCl 1 M à 160 °C.
- Oxygène pour Ti(III) → Ti(IV) : besoin 0,21–0,26 mmol O2 contre 0,15 mmol dans le ciel gazeux d'un autoclave de 50 mL (0,57 mmol pour 100 mL). Laissé en `reserve` car le volume d'autoclave est inconnu.
- DRX rutile : les six 2θ annoncés coïncident à 0,01° avec le calcul à partir de a = 4,593 et c = 2,959 Å ; je note que ce sont vraisemblablement les valeurs de la fiche, sans en faire un problème.
- XPS Mo 3d : 229,5 eV attribué à 3d3/2 et 232,8 eV à 3d5/2 = inversion (3d5/2 toujours plus bas). `probleme` de vocabulaire, à signaler car l'extraction le reproduit. Appui : arXiv 1906.05436 (229,5/232,7 eV), lu en extrait de recherche seulement.
- Bande interdite 2,7 eV : cohérente avec le seuil 450 nm (2,76 eV), mais le Tauc d'un composite à MoS2 noir n'abaisse pas la bande interdite du TiO2, et la référence 3,2 eV est celle de l'anatase alors que le TiO2 est du rutile (3,0 eV ; Hanaor & Sorrell 2011, DOI paru dans la recherche). `probleme` (contrôle 7, preuve non discriminante).
- Voie MoS2 : `non_reproductible` (aucune quantité, aucune masse de fibres, aucun volume), et `probleme` de bilan ; rapport TAA/Mo minimal de 3 tiré du bilan redox MoO4^2− + 3 H2S + 2 H+ → MoS2 + S + 4 H2O.
- La phrase « few layers of MoS2 … ultrafine TiO2 nanobelts » reprend le titre de Zhou et al., Small 2013 (TiO2 en nanoceintures) : relevé en `reserve` (cohérence entre sections), pas en accusation de plagiat.
- Photocatalyse : 30 min d'obscurité contre forte adsorption du MB par MoS2 (Zhou 2013) : `reserve`, témoins manquants listés.
- Tenue du polyimide en HCl 1 M à 160 °C puis à 200 °C : aucune donnée chiffrée trouvée (fiche DuPont inaccessible, DNS bloqué) ; réserve sur base de chimie générale, consignée dans `sources_not_found`.
- Comparaison base : PMC10458794 (molybdate + thioacétamide, 200 °C, 24 h) identique ; conditions MoS2 donc habituelles.
- Recherches : 8 recherches web, 3 lectures de page échouées (khazna.ku.ac.ae, cameochemicals, electro-wind : DNS). CAMEO thioacétamide cité d'après l'URL relevée dans la recherche (chemical/16062), page non ouverte.
- DOI non vérifiés (Crossref bloqué) : 10.1007/s10853-010-5113-0 (Hanaor), 10.26565/2312-4334-2021-4-02 (Morgunov) ; Zhou 2013 cité par notice ANU sans DOI.
