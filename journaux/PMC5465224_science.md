# PMC5465224 : critique scientifique (journal de décisions)

- Bilan de soufre : 37,5 mg de TAA = 0,499 mmol, contre 4 mmol de Zn, soit S:Zn = 0,125. Cela explique ZnO > ZnS (ZnS ≤ 48,7 mg) ; jugé `ok`, même si les auteurs ne font pas ce lien.
- `probleme` sur le bilan acide-base : Zn2+ + H2S → ZnS + 2 H+, et l'acétate (pKb ≈ 9,25) ne compense qu'un H+ ; il reste ≈ +0,5 mmol H+ net. L'« hydrolyse de CH3COO− » ne peut donc pas fournir les OH− de ZnO et de Ni(OH)2.
- `probleme` sur le redox : H2S sur Ni0 donne un sulfure, pas Ni2+. Les auteurs obtiennent eux-mêmes « Ni3S2/Ni(OH)2 » avec TAA seul ; avec le zinc, Zn2+ en excès capte le sulfure.
- Mécanisme proposé à la place (hypothèse, notée comme telle) : oxydation du Ni de la mousse par NO3− ou O2, avec hausse locale du pH comme dans l'électrodépôt de ZnO à partir de nitrate (Izaki & Omi 1996, DOI de mémoire, non vérifié). La recherche web d'une source directe pour l'hydrothermie sans base n'a rien donné.
- `probleme` sur la capacité : 1173,8 F/g × 0,8 V = 939 C/g, alors que le Ni(OH)2 vaut au plus 1041 C/g. La fraction de Ni(OH)2 tirée de l'EDS (≈ 5,8 % en masse) limite la capacité à ≈ 75–120 F/g. Même avec la borne d'un tiers (Ni(OH)2 dernier des trois constituants de la Table S1), il faudrait ΔV ≤ 0,30 V. Source sur la contribution de la mousse : Gu et al., J. Mater. Chem. A 2014 (titre trouvé par recherche web, DOI 10.1039/c4ta00205a non vérifié).
- J'ai gardé l'EDS en lecture at.% et en lecture % massique, puisque l'unité n'est pas écrite ; les deux donnent ≈ 6 % de Ni(OH)2, la conclusion ne dépend donc pas de l'unité.
- Pic S 2p à 169,2 eV = sulfate (entrée ZnSO4 de la base XPS du NIST, 169,20 eV, lue dans un extrait de recherche : la page elle-même est bloquée par le proxy) → `reserve`, car ZnS reste attesté à 162,4 eV.
- Franges HRTEM : j'ai recalculé ZnO (a 3,2498, c 5,2066 Å) : (101) 0,2476 et (002) 0,2603 nm, contre 0,250 et 0,262 nm attribués à des plans de ZnS (fiche 89-2427 non consultable). Classé `reserve`, et non `probleme`, faute d'avoir la fiche du polytype.
- Brousse, Bélanger et Long 2015 cité pour la distinction batterie / pseudocapacité : auteurs et titre confirmés par la recherche, revue et DOI de mémoire, déclarés non vérifiés.
- Fenêtre 0–0,8 V contre ECS en KOH 3 M ≈ 1,90 V contre ERH : `reserve` et non `probleme`, puisque la fenêtre de la charge-décharge n'est pas donnée.
- `probleme` sur le témoin Ni(OH)2-6h : ΔG(Ni + 2 H2O → Ni(OH)2 + H2) ≈ +27 kJ/mol (ΔfG° de manuel, non relus) ; seul l'O2 du ciel gazeux (≈ 0,17 mmol) oxyde, donc pas de « Ni(OH)2 pur » sans oxydant. Fig. S5 absente.
- Ni(OH)2-12h/24h en `invérifiable` : aucun résultat dans le texte.
- Témoin ZnS/ZnO : sans mousse, la source d'OH− manque aussi ; il donne probablement surtout du ZnS. Nommé « /Ni foam » dans les Méthodes mais préparé sans mousse.
- Pression de l'autoclave : eau 1,0 MPa à 180 °C (valeur de manuel) ; pour l'éthanol, ordre de grandeur seulement (NIST WebBook bloqué par le proxy).
- Limites du réseau : WebFetch et curl sont bloqués (DNS ou proxy 403) vers rsc.org, nist.gov et webbook.nist.gov ; 9 recherches web, seuls les extraits ont servi.
- Rien n'a été ajouté à fondateurs.md ni à constantes.md (consigne : Crossref bloqué).
