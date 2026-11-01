# PMC9064236 — critique scientifique (journal de décisions)

- Six voies de base jugées : Mo-glass, am-TiOx-FTO, alpha-SnS_Mo, pi-SnS_Mo, Device_A, Anneal_A_200C_20min. Les branches (substrat, durée de recuit) ne changent pas la chimie et sont traitées dans les voies de base.
- Sol de TiOx : 370 μL de TTIP (d = 0,955 ; 97 %) = 1,206 mmol, et 0,070 mmol de HCl dans 5,41 mL, soit 0,223 M et 0,0130 M : c'est exactement la recette « c-TTIP » des couches compactes de pérovskite (0,23/0,013 M, Qin 2017, PMC5747562). Verdict cohérent ; le titre de cet article n'a pas été relevé, il est noté comme tel.
- Précurseur (1) : formule du monomère C11H17N3SSn = 342,05 g/mol. Le bilan SnS + PhN=C(NMe2)2 est équilibré ; il est proposé comme hypothèse non sourcée (texte d'Ahmet 2015 non accessible). La molarité 0,08 M est ambiguë (dimère ou monomère, facteur 2).
- « pressure = 5 bar » sur l'étape de dépôt : l'article dit « until it reached the atomizer » (pression d'alimentation). Classé `reserve` et non `probleme`, car l'erreur vient de l'attribution de l'extraction et non de l'article : à corriger dans le JSON, avec l'annotation de sécurité qui parle d'un réacteur sous 5 bar.
- i-ZnO DC (Méthodes) contre RF (Résultats) : `probleme`, car la pulvérisation DC d'une cible céramique d'i-ZnO très résistive n'est pas plausible. Je n'ai pas trouvé de source dédiée attribuable : basis = chimie_generale, l'extrait NREL n'est pas cité.
- Mécanisme π-SnS : `probleme`, car l'accord de maille invoqué avec du TiOx amorphe est impossible, et une forte densité de nucléation donnerait des grains plus petits. Explication préférée : la taille des grains suit l'épaisseur (0,8 contre 1,8 μm, facteur 2,25 de vitesse de croissance).
- Jsc de l'EQE contre Jsc J–V : F donne 4,84/2,50 = 1,94, 5,35/3,50 = 1,53 et 6,88/5,40 = 1,27, contre B dans ±16 % : `probleme` sur la fiabilité des Jsc des cellules π.
- Rendements recalculés : tous à l'arrondi près, sauf F en conclusion (0,47 % contre 0,398 % recalculé) et le Voc de F dans le résumé (0,135 V) : `probleme` (erreurs de l'article). E à 240 min : 0,161 % recalculé contre 0,15 %, écart mineur non signalé en problème.
- 11 mA cm⁻² = 51 % de 21,7 mA cm⁻², et non 45 % : `reserve`.
- Bain CdS : 0,12 M CdSO4 est presque sûrement la concentration de la solution mère ; laissé en `reserve` faute du texte de Neuschitzer 2015. Valeur du Ksp de Cd(OH)2 non utilisée car non vérifiée.
- Pression du Mo (0,06 Pa = 0,45 mTorr) sous les plages publiées (≈ 0,75–11 mTorr) : `reserve`, peut-être une pression de base.
- Sources dont le titre n'a pas été vu dans les résultats (deux articles d'Abutbul 2016) : le titre est marqué « non relevé » plutôt que reconstitué de mémoire.
- Recherches web : 11. Échecs : WebFetch (DNS) sur researchportal.bath.ac.uk, pmc.ncbi.nlm.nih.gov et tsi.com ; la spécification de pression du TSI 3076 n'a pas été trouvée.
- DOI repris d'extraits de recherche, non vérifiés sur Crossref : 10.1021/acs.chemmater.5b03220, 10.1039/c3dt50607j, 10.1126/science.1251428, 10.1039/c5ra23092f, 10.1039/c6ce00647g.
