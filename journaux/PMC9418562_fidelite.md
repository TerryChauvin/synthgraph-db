# Journal critique de fidélité — PMC9418562

- Ma liste d'échantillons avant lecture de l'extraction : MoS2 avec AuNP 60 nm (une goutte de 100 µL), témoin sans AuNP (même croissance, Fig. 1d et S1), AuNP 40 nm et 100 nm (Fig. S2), 2 et 4 dépôts (Fig. S3), FET avec AuNP, FET sans AuNP (renvoi cit50). Identique à `sample_inventory` ; les trois familles de flocons de la Fig. 2a sont bien sans voie propre.
- Valeurs numériques du texte (T1 140 °C, T2 785 °C, 175 mg S, 50 mg MoO3, 300 sccm, rampe 20 min, stabilisation 5 min, croissance 10 min, δ, FWHM, % de décroissance PL, Vth, μ, gm/W, dopage) toutes recoupées : aucune valeur fausse. Mobilité recalculée ≈ 0,94 cm2 V−1 s−1 et dopage 1,85 × 10^12 cm−2 : concordants.
- Constat « deduit » sur le témoin sans or : l'article dit seulement « one without them » ; l'absence de poly-l-lysine est inférée. `sure` car aucune phrase ne l'écrit.
- Constat « deduit » sur l'héritage des branches 40/100 nm et 2/4 dépôts : l'annexe ne dit pas « same procedure » ; `probable` car « CVD process » et la mention du 60 nm « similar to the ones of the manuscript » rendent l'identité plausible.
- Équipement « deux zones, nacelle de soufre en T1 » : la citation retenue (« open tube ») ne le porte pas ; la Fig. 1b (ouverte) le montre. Constat de citation, pas de valeur ; `probable`.
- FET sans or : `−20 V` est suivi d'un renvoi [cit50] ; j'ai écarté l'idée d'une valeur fausse, mais l'attribution à la croissance témoin de cet article est incertaine, d'où `probable`.
- Incohérence propre à l'article : « B exciton ... decreased by ... 21% » pour BL/ML contre le tableau S3 (864) et S1 (685), soit +26 %. Mis en `mineur` `sure` : l'extraction est fidèle au texte, il faut seulement l'annoter.
- Figures : Fig. 1 et Fig. 5 ouvertes ; aucune valeur `from_figure` dans l'extraction, donc aucun écart de lecture à mesurer. Histogramme 5c : pics visibles vers 17,5–18 et 19,5–20,5 cm−1, cohérent avec le texte.
- Écarté, non-constat : le renvoi à « Fig. 6a » au lieu de 7a (déjà en doute, sans effet) ; T1 = 140 °C non répété dans l'étape de croissance (lecture possible, héritage de l'étape 10).
- method_sources : cit34, cit36 acceptés ; cit35 (PTCDA) acceptable ; cit37 jugé contexte (justification de l'inversion du flux) donc `mineur` ; cit50 laissé (sert de source à la voie FET sans or). Aucun renvoi de méthode manquant dans corpus/refs (cit38–cit52 sont des renvois d'interprétation).
- Cases `not_stated` vérifiées (≈ 45) : aucune ne contredit l'article ni l'annexe.
