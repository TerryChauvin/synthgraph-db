# Journal de la correction PMC9054292

- FTIR (constat 1) : trois entrées FTIR ajoutées (1700/1650, 1560, plage 1000–1400 cm−1), chacune avec une citation coupée avant l'image SVG qui rend « C=O » / « C=C » (le signe = n'existe pas dans le texte). Le résultat écrit C=O et C=C d'après la phrase de l'article, lue avec l'image.
- Sélectivité à pH 7 (constat 2) : deux résultats `from_figure` Fig. 5B (Cr(VI) 0,97 ; autres ions ≤ 0,33), valeurs lues sur l'image f5, deux chiffres significatifs, citation = légende. Les valeurs détaillées (Ag 0,33, Fe(III) 0,32, Hg 0,30, Fe(II) 0,25, Cr(III) 0,08) sont dans un doute de précision de lecture.
- Tableau S1 (constat 3) : équations, R² des deux plages (0,9981 ; 0,4725), n = 11 des LOD/LOQ, plan des RSD (3x3 ; 5x3) et R² de Ksv (0,9966, phrase du texte) ajoutés. Citations tranchées dans le texte aplati (le caractère µ de l'annexe est un caractère privé ; citation recopiée depuis le texte chargé, pas retapée).
- Étape 5 « cooled » (constat 4) : mot retiré de la description, `cooling` ajouté aux `not_stated` de l'étape 4.
- Durées « four hours » / « an hour » (constat 5) : REJETÉ côté valeur. `load.py` exige que `value_num` figure tel quel dans la citation et le texte n'écrit jamais « 4 h » ni « 1 h » ; on ne convertit pas un mot en nombre. Les valeurs restent en `value_text` ; un doute l'explique. La décision de l'orchestrateur d'accepter le constat n'a pas laissé d'autre forme conforme.
- « Concentré » (constat 6) : annotation `limite_reproductibilite` (Introduction contre extrait à 500 mg L−1 sans étape de dilution ou d'évaporation).
- UV-Vis et capteur (constat 7) : citation UV-Vis remplacée par la phrase des régions d'absorbance ; 340 nm reformulé comme longueur d'excitation (le maximum vers 278 nm est dans l'annotation de réserves). Capteur : citation remplacée par la phrase de l'extinction par Cr(VI) ; la partie Cr(III) après H2O2 passe dans une entrée séparée avec sa propre citation.
- Fig. 3 (constat 8) : annotation de limite, citations inchangées ; valeurs lues sur l'image f3 (NaCl 490→570, EDTA 560→630, DMSO 380, THF 680, acétonitrile 860, éthanol 1080, eau 600).
- EDX (constat 9) : résultat `elemental_impurities_EDX` (Cl, K, Ca de l'extrait ; Si et Au non comptés) et caractérisation EDX étendue avec la citation jusqu'à la phrase sur Cl, K, Ca.
- Stabilité intra-jour (constat 10) : 90 min, citation de la Conclusion ; ajout de « sensitivity … constant in the range of 0.5–1.5 mg L−1 ».
- Annotation `conclusion_auteurs` (constat 11) : plateau 3–5 h, 4 h au milieu, seul 180 °C est le point le plus haut.
- Critique scientifique : quatre `probleme` (base de masse des CDs, extinction dynamique impossible, Tableau 2 sous la LOQ, Ag(I)/Fe(III) à 1 mM) en annotations séparées ; les réserves sont regroupées en trois annotations (synthèse avec pressions, caractérisation, capteur) pour rester concises. Aucune valeur de l'article modifiée.
- `mecanisme_analyse` réécrit comme hypothèse (sucres, fructanes, acides aminés, cystéine sulfoxydes, fluorophores moléculaires) ; `mecanisme_auteurs` intact.
- Aucune voie retirée ni renommée. Aucun doute périmé sur les marqueurs `[[id]]` à supprimer (aucun présent).
