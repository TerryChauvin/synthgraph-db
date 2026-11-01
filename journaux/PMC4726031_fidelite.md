# Journal critique de fidélité — PMC4726031

- Ma liste d'échantillons avant ouverture de l'extraction : LaFeO3/MMT, précurseur séché, LaFeO3 pur, MMT, LaCoO3/MMT, LaNiO3/MMT, La(FeCo)O3/MMT, La(FeNi)O3/MMT, La(CoNi)O3/MMT, LaFeO3/MMT-0.5, -2, témoins RhB seul et H2O2 seul. L'inventaire de l'extracteur est identique : aucun échantillon manquant, aucune branche inventée (9 voies).
- Tableau S1 aplati : j'ai relu rangée par rangée avec l'en-tête (La, Fe, Co, Ni, acide citrique, MMT) ; les huit rangées (dont -0.5 : 0,0025/0,0025/0,005 mol, et -2 : 0,010/0,010/0,020 mol) sont correctement recopiées. Pas de constat.
- Figure 3c ouverte (srep19723-f3.jpg) : LaFeO3/MMT à 15 min ≈ 56 %, LaFeO3 ≈ 29 %, écart avec les from_figure inférieur à 3 points ; valeurs à 30 min (81 et 59) cohérentes avec 81,16 et 58,96 % du texte. Pas de constat.
- Autres figures (1, 2, 4, 5) non ouvertes : toutes les valeurs extraites sont dans le texte, aucune from_figure ailleurs.
- Cases not_stated vérifiées (rendement, atmosphère de séchage et de calcination, vitesse d'agitation, puissance de sonication, vitesse de refroidissement) : toutes réellement absentes de l'article et de l'annexe ; l'air de l'ATG-DSC ne vaut pas atmosphère de calcination. Aucun non_cite_a_tort.
- Constat MMT (probable) : les valeurs du témoin MMT sont dans le texte mais sans voie ; je ne sais pas si le schéma prévoit où les ranger, d'où « probable » et non « sure ».
- Composition chimique de MMT : « sure », phrase explicite dans Materials, absente du JSON (grep 61.53 = 0).
- Bande interdite des mélanges et adsorption 10 à 15 % : « sure » pour les mélanges (phrase nominative), « probable » pour l'adsorption (la portée « All LaMO3/MMT » exclut peut-être les mélanges).
- Noms « LaFe0.5Co0.5O3-type » : déduits de Table S1, jamais écrits ; mineur, probable.
- Écarté : étape de chauffage de LaFeO3 pur (« mixture suspension » citée alors que sans MMT) ; l'article écrit « prepared in the same way without montmorillonite », donc l'héritage est fondé et l'extracteur l'a déjà signalé en doute.
- Écarté : volume de solvant des variantes -0.5 et -2 supposé 30 mL ; « same way » le permet, mais la concentration réelle est incertaine ; placé en lacune de reproductibilité, pas en constat.
- Sources de méthode : refs/PMC4726031.txt ne contient aucun renvoi dans une phrase de préparation (introduction seulement) ; method_sources vide est correct.
- Annotations relues : résumé, comparaison, tendance et mécanisme conformes au texte ; pas de danger évident omis.
