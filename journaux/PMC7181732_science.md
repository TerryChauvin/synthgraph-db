# PMC7181732 — critique scientifique (journal de décisions)

- Tableau 1 : le « C/O » se recalcule exactement comme 1/(C-OH&C-O-C + C=O + O=C-OH), avec COOH compté une fois (1,95 ; 4,18 ; 8,85). C'est donc un rapport carbone total / carbone oxygéné, pas un rapport atomique : noté en `reserve` sur GO, et non en `probleme`, car l'ordre de grandeur reste juste.
- rGO-Am : les composantes du tableau 1 somment à 0,982. Le 1,8 % qui manque est sans doute la composante C-N (285,8 eV) citée dans le texte. Or N = 5,5 % at. demande au moins 0,065 de C-N : les carbones C-N sont comptés ailleurs (`reserve`).
- C/O corrigé de 5,02 : il faut retirer x = 0,040 C-Br par carbone. Avec 3,96 % at. de C-Br et C ≈ 76 % at., on trouve ≈ 5,3. Je signale seulement l'origine introuvable du « 3,4 % at. », sans affirmer quel calcul les auteurs ont fait.
- Test CuCl/HCl (`probleme`) : 50 mg de rGO-Am portent ≈ 0,16 mmol de NH2 (masse moyenne de 12,64 g/mol par atome lourd, tirée de C/O 8,85 et de N 5,5 %) contre ≈ 11 mmol de Cl− par moitié de solution, soit 1,4 %. L'explication par le tétraammine est écartée parce que NH4+ a un pKa de 9,25 dans HCl 1 M. Le témoin change aussi l'agitation.
- rGO-Am-Benz (`probleme`) : 100 µL de triéthanolamine = 0,753 mmol, soit 2,26 mmol d'OH, contre 0,391 mmol de chlorure d'acyle (densités des fiches Sigma-Aldrich). J'ai posé la question d'une confusion triethanolamine / triethylamine sans la trancher : l'article écrit bien « triethanolamine ».
- Rendement de couplage : 2,8/3,96 = 70,7 %, et ≈ 94 % avec la correction de dilution (9 atomes vus en XPS par groupe greffé). Les 74 % ne se retrouvent pas. Classé `reserve`, car l'écart brut est faible.
- Mécanisme rGO-Am jugé `a_revoir` : une SN2 sur un carbone sp3 du plan basal est impossible, et l'ouverture des époxydes par NH3 à température ambiante est une alternative connue (Chem. Commun. 2019, 10.1039/c9cc05693a). Je n'ai trouvé que le résumé de cet article, pas son titre : la page RSC est injoignable et cela est dit dans `sources_not_found`.
- N1s : la composante de 399,8 eV coïncide avec la position souvent donnée au N pyrrolique. Source : Artyushkova 2013 (Chem. Commun., CC-BY), retrouvée par la recherche ; la page elle-même n'a pas pu être ouverte.
- Vocabulaire : « electron-withdrawing » (introduction) contre « electron-donating » (discussion). J'ai cité σp(NH2) = −0,66 depuis une table secondaire qui renvoie à Hansch, Leo et Taft 1991 ; le DOI n'est pas vérifié.
- « Taille moléculaire » C-NH2 = 0,197 nm : une liaison C-N mesure ≈ 0,147 nm (chimie générale). Classé `reserve`, car cela ne touche que l'interprétation des bosses.
- Pei et al. 2010 (HBr, réducteur plus faible que HI) : la référence n'a été trouvée que dans une liste de références d'une annexe RSC, et le DOI n'est pas donné, faute de vérification.
- rGO-HT : à 600 °C sous air, le rGO brûle. L'atmosphère, non précisée, est donc décisive : `reserve`.
- Rien n'a été ajouté à fondateurs.md ni à constantes.md, conformément à la consigne (Crossref bloqué).
- Recherches web : 10, plus une lecture de page en échec (pubs.rsc.org injoignable).
