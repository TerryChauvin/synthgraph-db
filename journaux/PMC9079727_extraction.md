# Journal d'extraction PMC9079727

- Découpage : une voie de base (LLZALO-1, 1100 °C × 20 h, premier échantillon du tableau 1) et quatre branches (LLZALO-2 à 5). Le protocole n'est décrit qu'une fois pour tous les échantillons, le tableau 1 donne seulement le couple température/durée de frittage ; les branches ne varient donc que sur l'étape 8 (sinter).
- LLZALO-4 (1210 °C × 15 h) et LLZALO-5 (1220 °C × 10 h) portent deux variations chacune (température et durée), citées avec la rangée entière du tableau 1. LLZALO-2 et 3 ne varient que la température (durée 20 h identique au parent).
- Héritage des étapes 1 à 7 accepté : l'article parle d'un seul protocole pour « all samples » (naming convention du tableau 1). Noté en doute.
- Plage de frittage « 1100–1230 °C » (Méthodes) contre 1220 °C maximum au tableau 1 : le tableau est retenu, pas de branche à 1230 °C (valeur non listée explicitement).
- Excès de 10 wt% de Li2CO3 : base du pourcentage non précisée, mis en `amount_text` sans conversion ; les autres précurseurs en « stoichiometric amounts » (`amount_text`) car aucune masse n'est donnée.
- Prétraitement de La2O3 (900 °C, 10 h) : étape 1 à part (action heat), puisqu'il s'applique à un réactif avant le mélange ; atmosphère et vitesse de chauffe non citées.
- Séchage à 65 °C : durée non citée ; incertitude si le séchage a aussi lieu après le second broyage avec PVB (étape 6 sans séchage déclaré).
- Frittage : atmosphère, vitesse de chauffe, four non cités (« in air » ne concerne que le broyage). Le creuset en MgO avec lit de poudre est consigné en équipement de l'étape 8 et en `mecanisme_auteurs`.
- Résultats : chaque rangée des tableaux 1 et 3 est attribuée par le nom de l'échantillon (jamais par position) ; propriétés en `outcomes` de chaque voie. Résultat de groupe (phase cubique pour tous) laissé en caractérisation de la voie de base et annotation `tendance_observee`.
- Fig. 3d : les valeurs de conductivité lues graphiquement (LLZALO-4 ≈ 3 × 10−4, LLZALO-1 ≈ 1,2 × 10−4 S cm−1) ne concordent pas avec le tableau 3 (2,10 × 10−4 ; 8,78 × 10−5). Aucune valeur extraite de la figure ; le tableau, plus détaillé et repris dans les conclusions, fait foi. Fig. 3a-c, 1, 2, 4 lues ou jugées sans résultat chiffré absent du texte : 0 valeur `from_figure`.
- Échantillon « LLZO » de la Fig. 4 : sans voie (diagramme de comparaison, synthèse non décrite).
- Aucune source de méthode : le texte de la synthèse ne contient aucun renvoi bibliographique (les [[cit]] sont dans l'introduction et la discussion, contexte). Pas de Supporting Information dans le fichier et aucun renvoi à une annexe.
- Coquille « LLZAO-4 » du texte lue comme LLZALO-4 (échantillon de conductivité maximale, tableau 3).
