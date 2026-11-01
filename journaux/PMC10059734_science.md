# PMC10059734 — critique scientifique (Opus)

- Quantités « 1,2 / 0,4 / 0,4 mmol L−1 » : recalcul 427,4 mg / 353,17 = 1,21 mmol Fe(acac)3, etc. ; ce sont des mmol (≈ 40 et 13 mmol/L réels dans 30 mL) → `probleme` d'unité. Zn : « 0,4 » implique M = 258, plus proche de l'anhydre que d'un monohydrate.
- (Mn+Zn):Fe 0,654 (précurseurs, Zn anhydre) contre 0,579 (ICP) : écart de 12 % gardé en `reserve` (volatilité des acac ou lavage magnétique), pas en `probleme`.
- XRD : (311) et (440) relus sur la Fig. 2 donnent a = 0,845 et 0,841 nm, cohérents avec 0,8424. Mais la largeur ≈ 0,8–1° ↔ ≈ 10 nm, alors que 2,12 nm donnerait ≈ 3,9° → `probleme`. Le D4,3 de la log-normale TEM (≈ 8 nm) explique la largeur ; c'est le Williamson–Hall qui est suspect, pas le TEM.
- Référence « massive 0,8302–0,8311 nm » : rejetée sur la base des fiches ICDD de manuel (MnFe2O4 8,499 Å, ZnFe2O4 8,441 Å, Fe3O4 8,396 Å) ; aucune source primaire en ligne ouverte (recherche infructueuse), noté dans sources_not_found.
- Pente d'aimantation : Fig. 6b ≈ (104 − 82)/(350 − 233) = 0,19 ; × 0,408 (résidu ATG) = 0,077 ≈ 0,078 du texte. Hypothèse retenue : texte par masse de composite, figure par masse de ferrite. Classé `probleme` (normalisation non écrite, valeurs incohérentes).
- Langevin à 200 K, 0,25 T, sphère de 4,4 nm : ≈ 50 % de saturation contre ≈ 90 % sur la Fig. 6a → `reserve` (grosses particules ou amas), cohérent avec la largeur XRD.
- EPA 200.7 = ICP-AES (résumé NEMI vérifié par recherche) ; la neutralisation après eau régale ferait précipiter Fe(OH)3 → `probleme`. Je n'ai pas pu lire la section 8 de la méthode (PDF EPA non rendu), la contrainte pH < 2 vient des résumés de laboratoires.
- Fantômes : 240 μg/mL / 1,0 mM → 240 g/mol (formule 236) ; 160 / 0,6 → 267 g/mol ; 160 ↔ 0,667 mM = dilution 1:3 → `probleme`. r2* recalculé par moindres carrés passant par l'origine avec c = 0,6 : 1373 et 1209, identique à la Fig. 9 (1370, 1208) : les auteurs ont donc bien utilisé 0,6.
- Non-linéarité R2* (× 2,39 pour × 1,67) : `reserve`, pas `probleme`, car deux points seulement.
- Comparaison à 482 (maghémite–albumine) : r2* par unité formulaire contre une relaxivité par mmol Fe ; ramené au fer 720, aux métaux 457 → `probleme` (affirmation « bien plus élevée » non soutenue). L'unité de la source citée par les auteurs n'a pas été vérifiée : je m'appuie sur l'usage (relaxivités par mM de Fe).
- T1 des fantômes dopés ≈ 10 % plus long que la DC7 pure (Fig. 7b) : impossible pour un agent magnétique → la matrice a changé ; témoin inadéquat (contrôle n° 5) → `probleme`.
- ΔωτD recalculé ≈ 360 (M auteurs) ou 240 (M de la Fig. 6) : la borne « > 180 » tient ; `ok`.
- Entraînement du DBE : ΔHvap supposée 50 kJ/mol (non sourcée, dit dans `calculs`) → P ≈ 70 kPa à 280 °C ; seul un ordre de grandeur, d'où `reserve`.
- Composition de la partie A : la fiche DuPont ne dit que « bi-composant, catalysé au Pt » ; l'affirmation « pas de groupes alcényle » reste invérifiée (`reserve`).
- Recherches web : 8 (2 lectures de pages échouées, DNS). DOI non vérifiés sur Crossref : 10.1021/ja0380852 (Sun 2004, via citation secondaire), 10.1002/adhm.201200078 (Vuong 2012, via plaudit.pub). Rien ajouté à fondateurs.md ni constantes.md (consigne).
