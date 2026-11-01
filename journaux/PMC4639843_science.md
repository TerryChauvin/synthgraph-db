# PMC4639843 — critique scientifique (journal)

- TGA contre stœchiométrie (`probleme`, base et 3 branches) : 1 mmol de Cu + 1 mmol de thioacétamide = 95,6 mg de CuS pour 1 à 20 mg de GO-COOH, soit 83–99 % de CuS attendus contre 89/47/24/20 % annoncés ; conversion implicite 8,5/4,6/3,3/5,2 % (non monotone). Classé `probleme` et non `reserve` : la composition d'un composite refait n'est pas prévisible.
- Dosage TGA sous N2 : la covellite perd du soufre avant 900 °C (CuS → ½ Cu2S, résidu 83,2 %) ; source retenue : rapport USBM via CDC Stacks (Kullerud, 235 °C) ; l'article de J. Chem. Thermodyn. 1987 (780,5 K) gardé en appoint avec DOI déduit du PII, non vérifié.
- k RhB de -1 : durée commune recalculée à ≈ 100 min sur -5/-10/-20 (−ln(1−X)/k = 96–100 min) ; 72,7 % impose k ≈ 0,013 min−1 ; 0,0013 donnerait ≈ 1 000 min. Erreur ×10 du tableau (`probleme`).
- Même calcul sur GO-COOH et CuS (RhB) : 55 et 223 min tels qu'écrits, 106 et 116 min si les deux k sont permutés → `reserve` seulement (moins net).
- Annexe SI-1.2 : 159,4 mg/L de phénol restant pour -10 = 20,3 %, exactement la valeur du tableau pour -20 (159,8 mg/L) → `probleme` de cohérence entre sections (colonnes -10/-20).
- XRD : covellite d'après Mindat (2,813 Å pour (103)) et PMC8467990 (indexation JCPDS 06-0464). 33,85° → d = 2,646 Å, ni (103) ni (006) ; « cubic » avec indices hexagonaux → `probleme` d'identification de phase. Fiche JCPDS 01-1281 introuvable : listée dans `sources_not_found`.
- DMSO « source de H2S » : Cao et al. 2010 (Adv. Mater.) ne l'obtiennent qu'à 180 °C ; aucune source pour la température ambiante → `probleme` de mécanisme ; source de soufre retenue = thioacétamide (Swift & Butler 1956).
- Carboxylation : quantités inversées par rapport à Sun et al. 2008 (1,2 g NaOH / 1,0 g acide → ici 1,2 g acide / 1 g NaOH, 100 mL au lieu de ≈ 10 mL) ; excès NaOH ≈ 0,12 M contre ≈ 1,9 M. Guo et al. 2020 : à 0,1 M (pH 13) pas d'augmentation nette des COOH → `probleme` (le chiffre 123 mM de leur revue correspond à notre excès calculé).
- Lixiviation : 5,8 % de Cu de 1 g/L à 47 % CuS ≈ 18 mg/L, contre 2 mg/L (OMS 2022) → `reserve` (résultat, pas protocole) ; témoin Cu2+ seul manquant pour la désinfection.
- XPS Tableau S1 : S/Cu 2–12, sommes 93–100 % ; extraction PDF douteuse (doute de l'extracteur), donc seulement `reserve`.
- Branche -20 : pas de `probleme` propre au-delà de la TGA ; la valeur 20,1 % est cohérente avec son k, l'anomalie est portée par -10.
- Recherches web : 7 recherches + 1 lecture de page (Guo 2020). Rien ajouté à fondateurs.md ni constantes.md (Crossref bloqué).
