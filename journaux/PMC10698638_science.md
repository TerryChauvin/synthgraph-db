# PMC10698638 — critique scientifique (journal)

- Charge 15,56 % en `probleme` : ZIF-8 max = 0,198 mmol × 227,6 g/mol = 45,1 mg ; + 9,8 mg de CRL = 54,9 mg ; 15,56 % exigerait 63 mg. Hypothèses laissées ouvertes (charge rapportée à la protéine Bradford, composite non séché), car la base de calcul n'est pas écrite.
- Fiche Sigma L1754 : le lactose est le support de la poudre de lipase (extrait de recherche ; la page n'a pas pu être ouverte, DNS refusé). Gardé en `reserve` : les 10 mg ne sont pas 10 mg de protéine, et la poudre apporte du lactose, substrat de la réaction étudiée.
- « 0.86 Å » et diffusion du lactose et de l'acide dans les pores : `probleme`. Fenêtre de ZIF-8 ≈ 3,4 Å (Park 2006, déjà dans fondateurs.md) ; enzyme ≈ 5 nm (PDB 1CRL, cité sans chiffre de dimension vérifié : je reprends seulement les 5,2 nm des auteurs).
- Estérification en `probleme` (preuve non discriminante) : 20 mg de catalyseur ≈ 74 µmol de Zn(mIm)2 basique contre 4,64 µmol d'acide caprique. La conversion repose uniquement sur la disparition de l'acide, et aucun témoin sans enzyme n'est fait. Aucune source trouvée sur ZIF-8 + acides gras : l'argument reste acido-basique général, ce qui est écrit dans `sources_not_found`.
- L'extraction au n-hexane d'un « ester pur » est mise en `reserve` et non en `probleme` : une recherche sur la purification des esters de sucres au n-hexane n'a rien donné de direct.
- IC50 : 49,6/496,54 = 99,9 µM. L'erreur d'un facteur 1000 inverse la comparaison du Tableau 2 (cisplatine 8,4–10,8 µM) : `probleme`.
- Stabilité au pH en `probleme` : incubation à pH 2 dans du PBS 50 mM, puis dosage en tampon phosphate. Velásquez-Hernández 2019 (dégradation de ZIF-8 en PBS) et la dissolution de ZIF-8 en milieu acide font douter que la charpente soit intacte. DOI tiré de la recherche, non vérifié sur Crossref.
- Vmax rapporté au mg d'enzyme : 1,90e-3 contre 1,40e-3, soit un rapport de 0,74, cohérent avec 72,4 %. C'est donc une `reserve` de vocabulaire (« improved »), pas une incohérence des données.
- Zaidan 2012 (Food Chem.) : même optimum, 2:1 et 48 h (à 55 °C). Il sert de comparaison d'échelle, pas de preuve de la réaction.
- Liang 2015 (Nat. Commun.) sert pour le mécanisme de minéralisation biomimétique. DOI tiré de la recherche, non vérifié sur Crossref.
- Le pH ≈ 11 de la solution de Hmim est une estimation (pKa 7,86 de mémoire, source PubChem indiquée, page non ouverte) : marqué comme estimation.
- Rien n'est ajouté à fondateurs.md ni à constantes.md (Crossref est bloqué).
