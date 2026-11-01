# Journal critique de fidélité PMC9034275

- Ma liste d'échantillons avant d'ouvrir l'extraction : FAU parent, AcT-FAU, autoclave 2/6/10 h (Fig. 2a), tube 0,15 à 0/15 min/30 min/1/2/4 h (Fig. 5, 6), tube 0,10 (2 h, 4 h, autres durées en Table S1), tube 0,05, sans DMDMPOH x = 0,15 et 0,25, FAU commerciaux de comparaison (Fig. S2), « MOR ». Identique à `sample_inventory` ; aucun échantillon absent de l'inventaire.
- Constat « faux » sur la phase de Tube_Na015_2h (sure) : Fig. 6 relue, AEI 17,3 wt % contre FAU 1,4 wt % ; la branche hérite du nom « high-silica FAU » du parent. Même défaut à 1 h (mélange, probable) et à 0 min (solide amorphe, probable : la phrase sur le « slight peak near 350 °C for 0–15 min … amorphous aluminosilicates » le soutient mais ne dit pas explicitement « pas de FAU »).
- Morphologie « internal voids » héritée par toutes les branches FAU du tube : probable seulement, car le texte généralise parfois (« the numerous voids in the high-silica FAU crystals shown in Fig. 3 ») sans dire quel échantillon est en Fig. 3.
- DMDMP+ par supercage : l'article calcule à partir de Table S2 (série tubulaire, 0,013 Al2O3), donc l'attribution à HSFAU_2h est douteuse ; probable et non sure car la légende de la Fig. 3 ne précise pas l'échantillon.
- Teneur en matière organique ≈ 16 wt % (15 min à 4 h) : sure, phrase explicite, absente des résultats.
- Valeurs sur figure vérifiées : Fig. 6 (toutes les valeurs à ± 0,3 wt %), Fig. 5a (écart max 0,7 point, soit < 5 %), Fig. 5b (pics à ± 10 °C), Fig. 2a (phases) : aucun écart > 10 %. 2 h DTA montre aussi un petit épaulement à 380 °C, non gênant.
- not_stated : 38 cases vérifiées, aucune à tort. Concentrations des solutions de DMDMPOH/NaOH vraiment absentes ; ma stœchiométrie suggère ≈ 35 et 30 wt %, mis en gap seulement (valeur non écrite).
- Gel 0,018 contre 0,013 Al2O3 : 0,018 correspond à Si/Al = 27,7, 0,013 à ≈ 38 ; incohérence venant de l'article, signalée en gap, pas en constat.
- method_sources : cit26 est un traitement de données HEXTS ; je le signale `mineur` probable (règle du 2026-10-13) plutôt que `faux`, car la correction de diffusion conditionne la mesure. cit52 (MOR) lié au constat MOR. cit25, cit39, cit40 écartés : contexte.
- MOR : lu comme « les essais sans DMDMPOH ont donné de la MOR » mais « Additionally » peut aussi désigner une synthèse distincte ; donc `probable`.
- Écarté : la mention intro « 3,5-diethyl » (déjà en doute chez l'extracteur) ; « Si/Al 6–8 » de la discussion de la Fig. 7 (pas d'échantillon).
- Verdict `corrections_mineures` : aucune valeur numérique fausse, le défaut principal est l'héritage de phase/morphologie dans la série tubulaire.
