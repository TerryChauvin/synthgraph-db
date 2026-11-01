# PMC5567205 — critique scientifique (journal de décisions)

- PTO_solgel : seuls 10 mL d'acac « equal molar » sont chiffrés ; j'ai pris le plomb comme référent pour estimer l'échelle (0,0974 mol, ≈ 29,5 g de PbTiO3, ≈ 15 lots de 2 g). C'est cohérent avec la calcination « in small batch », mais c'est une hypothèse : statut `reserve`, pas `probleme`.
- Eau d'hydrolyse : aucune eau n'est ajoutée ; h ≈ 3 vient du trihydrate, plus l'eau d'estérification acide acétique + butanol (Doeuff et al. 1987, DOI non vérifié). Le mécanisme proposé par l'extraction est donc gardé (`ok`).
- 450 °C/1 h jugé limite basse (et non incohérent) d'après Lanki et al. 2014 (arXiv), qui obtiennent la phase pure à 460 °C. Aucune source trouvée pour la recette exacte acétate/butoxyde/acac.
- Frange de 4,1 Å : recalcul d(001) = 4,156 Å contre d(100) = 3,905 Å ; l'attribution « (100) » de l'article est fausse (`reserve`, sans conséquence sur la synthèse).
- Table S1 : J recalculé avec 39,7 nA donne 2,02 × 10^7 A/m² pour r = 25 nm et 5,05 × 10^6 pour r = 50 nm ; le diamètre de 50 nm (Fig. S9) est la bonne lecture, « Beam radius » est une erreur des auteurs.
- Emax recalculés à 300 keV (Pb 4,11 ; Ti 17,8 ; O 53,2 eV) : les valeurs de l'article sont 5–6 % trop hautes, écart proche du facteur 1,061 entre « 318349.44 ev » de la Table S1 et 300 keV. J'ai signalé la piste sans affirmer la cause.
- `probleme` 1 (mécanisme) : l'article écrit que le choc élastique est « quenched » par les électrons délocalisés ; c'est la radiolyse qui l'est. Appui : Egerton et al. 2004 (extrait lu : la désorption KF continue jusqu'à ce que le matériau soit assez conducteur). Le texte intégral n'a pas pu être lu (fetch direct en échec DNS), d'où la mention dans `sources_not_found`.
- KF sur Pb2+ : `reserve` et non `probleme`, car la perte d'O par ESD reste plausible ; seul le site du trou de cœur (Ti4+ de valence maximale, pas Pb2+ 6s²) est discutable.
- Pulvérisation du Pb : Emax(Pb) 4,1 eV > ΔsubH ≈ 2,0 eV/atome (valeur de manuel, non relue) ; j'en tire seulement que la perte de Pb n'est pas exclue, d'autant que la phrase « volatilization of Pb does take place » contredit la suite.
- `probleme` 2 (EDS) : électroneutralité avec Ti4+ inchangé ⇒ y = x ; O at.% = (3−x)/(5−x) ne descend qu'à 50 % pour x = 1. Une baisse de « 10 to 20 at.% » est impossible en points d'at.%, et la borne haute l'est aussi en relatif. J'ai gardé les deux lectures dans `calculs` pour que l'orchestrateur tranche.
- `probleme` 3 (XPS) : rapport de surface spot MET / spot XPS ≈ 10^-8 avec un spot XPS pris à 250 µm de rayon (hypothèse : l'article ne donne pas le spot). La conclusion « n-type » repose sur cet échantillon sans protocole ; alternative citée par les auteurs eux-mêmes : Pb0 créé par Ar+ (Zhu et al.).
- Survol XPS « non-irradiated shows higher Pb » contre EDS « excess of Pb » : contradiction rangée dans le `probleme` 3 plutôt qu'en constat séparé.
- Pb0 à 136,3 eV : comparé à 136,9 eV (Thermo) et PbO 137,8–137,9 eV (NIST) ; `reserve` (charge différentielle possible), pas d'erreur certaine sans référence d'énergie.
- Pb contre α-PbO : d(110) litharge = 2,811 Å (a = 3,9744 Å, AIST d'après Boher 1985) ≈ d(111) Pb 2,858 Å ; la frange seule ne discrimine pas, mais les FFT d'axe de zone + macles + EDS 99 % suffisent : `ok`.
- Superparamagnétisme du Pb : une seule étude (Theivasanthi & Alagar 2013, arXiv) contre le diamagnétisme établi (Bernardi et al. 2006) ; affirmation sans mesure dans l'article : `reserve`.
- Robertson 2000 (10.1116/1.591472) : existence confirmée par la recherche, valeurs PbTiO3 non relues ; la limite de Schottky 2,6 eV est recalculée exactement.
- Branches : seules EBI_40s (calcul de coalescence) et EBI_prolonged (dose) jugées ; EBI_20s, 80s, 175s ne changent que la durée et n'apportent rien de chimique à part.
- Recherches : 9 recherches web + 1 extraction de page (Egerton, Lanki). Aucun ajout à fondateurs.md ni constantes.md (Crossref bloqué).
