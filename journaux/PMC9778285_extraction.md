# Journal d'extraction PMC9778285

- Découpage : le gel séché (étapes 1 à 5 : mélange à 50 °C, TEA, micro-ondes, gélification, séchage 100 °C/24 h) est une voie `intermediate` (`MW_gel`), car l'ATD/ATG et l'IR des gels y sont rapportés (Table 1, Fig. 1-2) ; les poudres calcinées sont des voies à part (`MW@500` base, `MW@300`, `MW@650` en branches de température) qui prennent le gel comme réactif `intermediate`.
- Voie SG : `SG_gel` est une branche de `MW_gel` avec ses propres étapes (« the precursors were homogenized at 50 °C for two hours on a heated plate, without being exposed to microwaves ») ; les variations portent sur l'étape 3 micro-ondes (température, durée, puissance et fréquence « absent »). `SG@500` est branche de `MW@500` (réactif `MW_gel` remplacé par `SG_gel`), `SG@300` et `SG@650` en dérivent.
- Ajout de TEA et pré-mélange de 15 min pour SG : l'article ne les mentionne pas ; je n'ai pas copié ces étapes de MW (lecture littérale, une seule étape d'homogénéisation), signalé en doute.
- Pureté : la phrase « all of which were of reagent grade » couvre les quatre réactifs nommés ; elle sert de `supplier_quote`. Merck n'est donné que pour l'acétate de zinc.
- Quantités : aucune quantité absolue ; la TEA est en `amount_text` « ZnAc:TEA = 5:1 », le vanadium en « 2 mol% » sans référence (doute).
- Rangées de Table 2 : attribuées par le nom de l'échantillon écrit dans la rangée (MW@300 °C, etc.) ; les rangées « Zn3(VO4)2 | traces » n'ont pas de nom : celle de SG@650 citée par sa forme unique « … | traces | | | | - », celle de MW@650 remplacée par la phrase de conclusion « The powder thermally treated at 650 °C presented ZnO and traces of Zn3(VO4)2 ».
- Table 1 : seule la première rangée de chaque bloc nomme MW ou SG ; les autres rangées sont attribuées par position. « 404478 » lu comme deux effets (404 et 478 °C, d'après le texte).
- Tailles de grains 30–250 nm (MW) et 30–170 nm (SG) : attribuées à 500 °C par la position de la phrase.
- Fig. 4 : légende « 350 °C » contre 300 °C partout ailleurs et sur les étiquettes de l'image ; 300 °C retenu. Image regardée, aucune valeur lue (échelle seule, sans mesure fiable), donc 0 valeur `from_figure`.
- Contradiction non corrigée : cristallisation de ZnO « vers 800 °C » (ATD) alors que la DRX montre du ZnO dès 300 °C ; consignée en doute.
- Fiche ICDD 26-1451 (tableau) contre 36-1451 (texte) : doute, sans effet sur les valeurs.
- Pas de `method_sources` : la section Méthodes ne renvoie à aucune référence ; Williamson–Hall (B49) est une formule d'analyse de données, donc exclue.
- Annexes : aucune annexe citée dans l'article ; rien à signaler comme absent.
- Statut `succeeded` : renseigné seulement pour les voies de gel et de calcination à 500 °C ; les poudres à 300 et 650 °C ne sont pas déclarées échec par les auteurs.
