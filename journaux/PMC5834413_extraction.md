# Journal d'extraction PMC5834413

- Voie de base : R-2.3. L'article décrit une « typical synthesis » (20 mg de GO) sans la rattacher à un échantillon. Rapprochement fait par un calcul de stœchiométrie (20 mg de GO pour environ 0,84 g d'Ag3PO4 attendu, soit environ 2,3 %), qui n'est pas écrit dans l'article : consigné en doute plutôt que présenté comme un fait.
- R-1.5, R-2, R-2.5, R-3 : une branche chacune, variation sur le réactif « graphene oxide » en `value_text` (teneur théorique WrGO:Wcomposite), car la masse réelle de GO n'est pas donnée. L'article ne dit pas « same procedure » : héritage accepté par lecture littérale de la série, avec doute.
- Ag3PO4_QDs : « prepared under the same condition without GO ». Branche avec ses propres étapes (étape de dispersion du GO retirée, les autres recopiées et renumérotées). Je conserve la photoréduction ultrasonique faute de phrase contraire ; doute posé.
- Agitation classique à la place des ultrasons (Fig. S1, annexe absente) : branche R-2.3_stirring, variation rattachée à l'étape 9 (frequency) mais l'étape concernée n'est pas précisée (étape 5 ou 9) ; doute posé. Résultat qualitatif seulement.
- Série en masse de tensioactif (Fig. S3) : pas de branche, les masses ne sont pas listées (seul le seuil 0,5 g). Échantillon d'inventaire sans voie, avec raison, et annotation « Annexe absente du dépôt ».
- Étape 5 : « After 60 min, the precipitate was centrifuged » lu comme une durée sous ultrasons après l'ajout de Na2HPO4 (étape unique « sonicate »). Doute posé.
- Constantes k : lues sur Fig. 7b, valeurs imprimées sur le graphique, gardées avec leurs 4 chiffres car ce n'est pas une lecture graphique mais du texte de figure ; citation = légende de Fig. 7.
- C/C0 des essais de piégeage (Fig. 8b) : lecture graphique, 1 chiffre significatif (EDTA 0,6 ; p-benzoquinone 0,1) ; l'isopropanol n'est pas chiffré car son effet est dit « non évident » par les auteurs.
- Tensioactif : 2,2 mmol d'oléate de sodium correspond à environ 0,67 g alors que l'activité décroît au-delà de 0,5 g ; incohérence apparente non résolue, notée en doute sans corriger.
- GO et rGO de référence (XRD, FT-IR, Raman) : laissés sans voie dans l'inventaire (préparation Hummers renvoyée à CR33, rGO non décrit). Une entrée `method_sources` pour CR33, rôle protocole_adapte.
- 97,46 % dans le texte contre 97,5 % dans le résumé : arrondi, texte détaillé retenu, pas de doute.
- Pas de réactif « graphite naturel » : aucune quantité n'est donnée pour la préparation du GO, qui n'est pas décrite dans l'article.
