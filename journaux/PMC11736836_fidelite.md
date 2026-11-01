# Journal de la critique de fidélité, PMC11736836

- Ma liste d'échantillons avant l'extraction : sol vieilli 1 jour ; film sur quartz ; film sur Si (plasma O2) ; poudre séchée à 80 °C ; poudre à 450 °C ; sols dilués C0/10, C0/100, C0/200 (AFM) ; grille TEM ; couches simulées. Elle coïncide avec `sample_inventory` ; je ne signale aucun échantillon manquant en tant que voie.
- Sols dilués AFM (route null dans l'inventaire) : le motif « sans résultat de matériau » est inexact pour C0/10, car l'annexe 2.1 donne Sq = 455.5 pm et Sa = 353.2 pm. Constat `manquant`, `probable`, pas `sure`, parce que ce sont des échantillons de caractérisation et que l'extracteur pouvait les écarter sciemment.
- `method_sources` vide : [[ref43]] suit « The mixture was stirred for 2 h at 60 °C at 400 rpm. » dans corpus/refs. C'est une phrase de préparation du sol, donc `sure`.
- [[ref48]]/[[ref49]] (SAR avec lumière p-polarisée) : renvoi de mesure, mais proche d'une référence d'analyse de données ; `probable`. Écartés comme non-sources : ref45 (modèle de couche mince Hild), ref46 (Lorentz–Lorenz, formule), ref44 (contexte sur la sensibilité du pic Ti), ref22 (comparaison avec un travail antérieur).
- Tableaux 1 à 3 vérifiés rangée par rangée (quartz/Si, UV–vis/SAR/EP, rads/rdes) : aucune erreur d'attribution. La phrase « EP (52 nm) » du texte contre 50 nm au tableau 3 est déjà un doute traité par l'extracteur ; pas de constat.
- Composantes O 1s : seule celle à 530.0 eV est extraite ; 531.3 et 532.3 eV sont dans la même phrase, constat `sure` (le texte est explicite).
- Grille `not_stated` : 24 cases contrôlées (durée, ordre d'addition, immersion, humidité, atmosphère, vitesse de refroidissement, gas_flow du plasma…), aucune n'a de valeur dans l'article ni dans l'annexe. Incohérence seulement sur yield/scale entre voies (mineur, `probable` car l'héritage parent-fille peut l'expliquer).
- Aucune valeur `from_figure` : aucune image ouverte. Les figures 1 à 4 et SI ne portent aucun résultat chiffré absent du texte.
- Mauvais rattachement de la citation d'étape « age » (phrase du dépôt de film) et de la citation du réactif « sol » des poudres : acceptés (la phrase des poudres contient « 1-day aged precursor sols »), pas de constat.
- Eau « distilled » vs « ultrapure » : divergence interne de l'article déjà notée en doute ; non signalée de nouveau, ajoutée aux lacunes de reproductibilité.
- Sécurité : 2-propanol absent de l'annotation, `mineur`.
- Remarque scientifique laissée aux lacunes : l'eau de l'acide nitrique à 65 % n'est pas distinguée de l'eau ajoutée (ratio 0.82), ce qui change l'hydrolyse ; je ne l'ai pas posé en constat car aucun passage de l'article ne le dit.
