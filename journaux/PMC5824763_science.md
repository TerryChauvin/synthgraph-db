# PMC5824763 — critique scientifique (journal de décisions)

- Voies jugées : les trois voies de base (OVE_OH, AuNP-OH-1mL, AuNP-OH-1mL_KI) et deux branches qui changent la chimie : AuNP-OH-0.25mL (réducteur très limitant) et AuNP-OF-1mL (autre extrait). Les autres volumes ne font que prolonger la série et n'apportent pas de contrôle nouveau.
- Bilan d'électrons tiré du TPC (2 158 µg GAE/mL) : 1 mL d'extrait = 12,7 µmol GAE, soit 25 µmol e− à 2 e− par équivalent, contre 60 µmol nécessaires. Classé `reserve` et non `probleme` : le TPC (Folin) n'est pas un compte d'électrons, les unités galloyle peuvent céder plus de 2 e−, et les sucres réduisent aussi à 85 °C.
- A400 : la légende de la figure 1 dit que les colloïdes sont dilués 1:1 avant mesure ; avec ce facteur, 1,3 au plateau est compatible avec une réduction complète (1,14 attendu). Sans lire la légende, on aurait conclu à tort à un facteur 2 manquant.
- TPC du colloïde 6,25 mg/g DW : se recalcule exactement en rapportant 31,27 µg/mL à 100 mg DW / 20 mL (et non 21 mL) ; écart de 5 %, non signalé comme problème.
- `probleme` carvacrol/thymol « à groupes cétone » : structure vérifiée sur PubChem (phénols, C10H14O, aucun carbonyle). Erreur de chimie qui porte l'explication des auteurs sur les nanoplaquettes ; mécanisme alternatif retenu : rapport réducteur/or et réduction lente (plaquettes les plus grandes à 0,25 mL), avec Shankar et al. 2004 comme appui.
- `probleme` plage 522–546 nm (Méthodes) contre 534–560 nm (Résultats, figure 1) : déjà signalé comme doute par l'extracteur ; gardé comme incohérence de l'article.
- `probleme` antimicrobien : témoin multivariable (pH 2,5–3,2, extrait oxydé, extrait témoin à 10 %). Source sur l'activité faible des AuNP : revue J. Environ. Sci. Health C 2015 (DOI trouvé, auteurs non confirmés, contenu connu par une citation secondaire) ; signalé dans la source.
- `probleme` souches : ATCC 13076 donné pour Listeria dans les Chemicals ; ATCC 13932 confirmé L. monocytogenes sur la fiche ATCC ; 13076 = Salmonella Enteritidis d'après une table secondaire seulement.
- `probleme` IC50 : 15,9 et 6,5 µg/mL au-delà de la dose maximale de 4,0 µg/mL (viabilités encore 83 % et 67 %) : extrapolation, pas une mesure.
- DPPH sans blanc colloïde : laissé en `reserve` (biais de sens indéterminé : absorption plasmon à 517 nm contre agrégation dans l'éthanol). Source : article PMC12561802 vu seulement par l'extrait du moteur de recherche (PMC injoignable par DNS).
- Haiss : formule λ = 512 + 6,53·exp(0,0216 d) prise de mémoire ; elle redonne exactement les 56 nm des auteurs, ce qui la conforte. DOI non trouvé, noté dans `sources_not_found`.
- Le « 105 cells/well » et le « 108 CFU/mL » du texte sont des exposants aplatis par sections.py (10^5, 10^8) : non signalés comme erreurs des auteurs.
- Recherches web : 9 (dont 2 lectures de page échouées : PubMed et PMC injoignables). Rien ajouté à fondateurs.md ni à constantes.md (Crossref bloqué).
