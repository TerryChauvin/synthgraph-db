# Journal de correction PMC10523092

- Constat 1 (sol MTEOS/TEOS) : pureté 98,0 % et fournisseur ABCR renseignés sur le réactif « MTEOS/TEOS sol » avec la phrase de Materials en `supplier_quote`, cases `not_stated` retirées. Ces valeurs sont celles des silanes achetés, pas du sol préparé : doute posé. Pas d'ajout de MTEOS et TEOS comme réactifs séparés (quantités inconnues).
- Constat 2 : deux résultats ajoutés à TAA_only_series (hausse de l'intensité de PL avec le temps ; extinction possible si trop long), citations des deux phrases du corps de l'article, en mots de l'article.
- Constat 3 (EDX annexe) : rejeté par décision de l'orchestrateur ; attribution centre/bord incertaine. Mention en `limite_reproductibilite` (article et CdSe_CdS_triangles : S/Cd = 2,83 impossible, deux pointés insuffisants).
- Constat 4 : Fig. S5 retirée des `results_in` des branches 40 et 80 μl, nouvelle entrée d'inventaire (route null, quantités de TBAF non données) et doute.
- Constat 5 : THF du témoin : `amount`/`unit` retirés, `amount_text` « to a volume of 2 ml » conservé (comme la voie du verre) ; le volume final reste paramètre de l'étape.
- Constat 6 : `succeeded` de TAA_only_series passé de false à null (les auteurs ne parlent pas d'échec) ; doute explicite.
- Constat 7 : variation « duration » (étape 5, 72 h) supprimée ; durée de l'étape propre de la série déclarée `not_stated` (la série précède l'ajout de CdCl2/Cd(OL)2). Je n'ai pas rattaché la variation à l'étape 3 du parent (2 h), conformément à la décision.
- Constat 8 : JASCO V-770 / FLUOROLOG-3 / excitation 400 nm repris des Méthodes générales pour la caractérisation de la série, avec doute (l'article ne dit pas que la Fig. S1 a été mesurée autrement).
- Constat 9 : citation de TEM_intermediate_2h remplacée par la légende de la Fig. S1 « C) TEM image ... after 2 h) » (le contrôle normalise les espaces, la phrase coupe sur deux lignes du texte).
- Constat 10 : « 682 nm » retiré des noms de propriété ; le doute des figures lues précise la lecture au maximum à 682 nm sur l'axe.
- Constat 11 : doute ajouté (résumé : oxygène, Méthodes : atmosphère ambiante) ; valeur des Méthodes inchangée.
- Constat 12 : `repetitions` « repeated three times » ajouté aux étapes 6 et 8 en plus de la 7 ; doute sur trois cycles au total ou en plus du premier.
- Constat 13 : ordre des étapes conservé (suit le texte) ; descriptions des étapes 3 et 4 de CdSe_NPL précisent que l'injection à 205 °C a lieu pendant la montée vers 240 °C ; doute.
- Science : quatre points `probleme` et les réserves regroupés en huit annotations `limite_reproductibilite` par voie, sans importer de source web ni de DOI. `mecanisme_analyse` des triangles réécrit en hypothèse ; `securite_analyse` corrigée (retrait du « dégazage sous vide d'un mélange chaud » absent du texte, ajout de l'eau libérée à l'injection d'acétate hydraté et du thioacétamide cancérogène).
- `mecanisme_auteurs` des triangles : texte réduit à ce que sa citation dit (partie CdCl2/Cd(OL)2 déplacée dans une seconde annotation avec sa propre citation, sans le mot « anisotrope » que l'article n'écrit pas).
- Manques (oléate de Cd, composition du sol, quantités TBAF, THF, suspension verre, rendements, agitation, séchage 45/40 °C) : déjà en `not_stated` ou `missing_fields`, ajoutés aux annotations. Figures S1–S8 absentes : rien inventé.
