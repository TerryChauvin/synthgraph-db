# PMC9464223 — critique scientifique (journal de décisions)

- Recette NS jugée « coherente » : rapports 1 TEOS : 0,017 P123 : 5,68 HCl : 197 H2O = SBA-15 de Zhao 1998 (P123/TEOS massique 0,47 avec Mn 5 800 ; HCl ≈ 1,5 M, pH ≈ −0,2). Les problèmes portent sur l'interprétation, pas sur le protocole.
- Raie petits angles à 2,02° : Bragg d = 4,37 nm. Indexée (200), la (100) devrait être à 1,01° (dans la plage mesurée) ; indexée (100), a0 = 5,05 nm < D(DFT) 6,66 nm, paroi négative. Classé `probleme` (contrôle 4 : symétrie affirmée sans raie discriminante). Comparaison PMC6812203 : (100) à 0,96°.
- Table 3 : k2 = 1/qcal exactement pour les quatre échantillons (0,5023 ↔ 1,99 ; 0,356 ↔ 2,81…) ; la colonne « k2 » est la pente de t/qt. qcal 1,5–2,8 mg/g contre qe 78–168 : ajustement faux → `probleme`.
- Série en dose (Table 5) recalculée avec V = 0,2 L, C0 = 50 mg/L : retraits 16,5–94,8 % cohérents avec la Fig. 11, mais qe = 331 mg/g à Ce ≈ 41,7 mg/L contre 177 mg/g à Ce ≈ 56 mg/L dans la série en concentration → contradiction d'équilibre, `probleme`.
- Langmuir refait sur la Table 5 : qmax 192, KL 0,21 L/mg, R2 0,996 (accord avec les auteurs, sauf unité g/mg). Freundlich refait : n 2,69, KF 42,6, R2 0,78, contre n 10,4 et KF 1,312 publiés (prédit 1,9 mg/g au lieu de 177) → `probleme`.
- Capacité par m2 : 0,162 → 0,318 mg/m2 de NS à NSG-1 % ; la texture (+9 % SBET, +0,5 nm) ne rend pas compte du facteur 2,1 → `probleme` de preuve discriminante (contrôle 7) ; alternatives proposées : silanols, résidus N de gélatine, pH.
- Mécanisme gélatine écarté : à pH ≈ −0,2 pas de –COO−, ester avec 2 OH terminaux de PEO défavorisé dans ≈ 50 M d'eau, polycation et non « tensioactif anionique ». Hydrolyse partielle de la gélatine à 100 °C dans HCl 1,5 M : argument de manuel (hydrolyse totale 6 M, 110 °C, 24 h), aucune source trouvée → `reserve`, noté dans sources_not_found.
- Point isoélectrique de la gélatine (A : 7–9 ; B : 4,7–5,4) pris sur la page technique GELITA (fabricant), à défaut de source primaire.
- Bande 1075 cm−1 « symmetric » corrigée en asymétrique (table SpringerOpen 10.1186/s40645-025-00756-w) : `reserve`, sans effet sur la synthèse.
- Empreinte du bleu de méthylène 1,43 × 0,60 nm (arXiv:1308.5652) retenue ; aires de 160–197 Å2 trouvées seulement dans des brevets, écartées comme source.
- NSG-4 % : SBET et D(DFT) sous NS, contredit le résumé → `probleme` au niveau de la branche.
- Pas de source pour la variabilité d'un lot à l'autre des SBA-15 : l'argument « +0,5 nm dans le bruit » est donné comme chimie générale, sans chiffre de littérature.
- 6 recherches web. DOI Zhao (Science, JACS) et Ho–McKay non vérifiés sur Crossref (bloqué) ; rien ajouté à fondateurs.md ni constantes.md (consigne).
