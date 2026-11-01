# Journal d'extraction PMC7451673

- Article surtout biologique (rats diabétiques) : seule la synthèse verte des AgNPs (3 lignes de Méthodes) et la préparation de l'extrait de graines sont extraites. Pas de REJET car la synthèse est décrite avec quantités, température et vitesse d'agitation, même si elle est très incomplète.
- Deux voies de base indépendantes : `NS_extract` (kind `intermediate`, réactif réutilisé dans la synthèse) et `AgNP_NS` (matériau). L'extrait est aussi un traitement testé seul (groupe 4), ce qui justifie de le garder comme voie et non comme simple réactif.
- Contradiction « aqueous extract » (synthèse) contre Soxhlet à l'éthanol 70 % (extrait) : pas de correction, l'extrait Soxhlet est mis en réactif `intermediate` de la synthèse et le doute est noté.
- « 1 Mm » : unité recopiée telle quelle (`Mm`), lecture 1 mM signalée en doute et en limite.
- Étape « stirred continuously 120 rpm at 100 °C » : vitesse et température portées sur une étape `stir` ; durée déclarée non citée (seul « checked from time to time »). Aucune séparation, lavage ni séchage dans l'article : listés en `missing_fields`, pas inventés.
- Rendement 32 % : « The final extract yielded 32% » attribué à l'extrait (voie NS_extract) ; la base du pourcentage n'est pas dite.
- Groupe 3 (AgNPs par réduction chimique, Lee et Meisel) : aucune voie, protocole renvoyé à la référence b0195 sans quantité ; consigné en `method_sources` (route null) et en `sample_inventory`. Les groupes témoin et DN sont des groupes animaux sans voie.
- Rangée de tableau « Nigella sativa + A(combination) | 415 nm | 25.2 nm | 1.2 » : lue comme l'échantillon AgNP_NS (seule rangée).
- Fig. A (UV-Vis, gr1.jpg) : le maximum de la courbe est vers 350 nm, alors que le texte et la droite verticale disent 415 nm. J'ai gardé 415 nm (texte) et ajouté 350 nm en lecture de figure, en doute. Légende de Fig. A vide dans le texte : citation de la phrase des Méthodes qui renvoie à Fig. A (une légende de 6 caractères est refusée par le contrôle).
- Figures 1 à 4 (gr3 à gr6) : 14 valeurs du groupe « combination » (AgNPs vertes) lues sur les histogrammes à 2 chiffres significatifs ; les autres groupes non relevés (comparaison par groupe laissée à une annotation). Axes « Tissue » contre légende « serum » signalé. Fig. 5 (histologie) non lue : les scores sont dans la légende (texte), pris pour les groupes D (extrait) et E (AgNPs vertes).
- Doses (200 mg/kg « oral … ip », 0,25 mg/kg) et protocoles d'essai biologiques non extraits comme valeurs ; histologie (Yoo et Lee) et qPCR (Obata) absents de la liste de références, donc pas de `method_sources`.
- Aucune annexe citée dans l'article ; `## Supporting Information` absent du fichier : rien à signaler en annexe absente.
