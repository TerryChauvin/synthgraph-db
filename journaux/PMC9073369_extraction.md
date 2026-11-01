# Journal d'extraction PMC9073369 (Fe2Ni MOF sur mousse de nickel)

- Voie de base : « Fe2Ni MOF/NF » (seul protocole décrit en entier, Experimental). Les étapes comprennent le nettoyage de la mousse (étape 1) car la phrase de préparation fait partie du protocole ; durée et concentration d'HCl déclarées « non citées ».
- « Fe(NO)3·9H2O » : coquille de l'article, formule enregistrée Fe(NO3)3·9H2O ; vérifié par la masse (0,2828 g ≈ 0,7 mmol de nitrate nonahydraté). Citation inchangée, doute posé.
- « After 30 minutes » : lu comme 30 min d'agitation avant transfert ; étape stir distincte de l'étape transfert, les deux citent la même phrase. Doute posé.
- Fe MOF/NF et Ni MOF/NF : branches de la voie de base (« synthesized in the same way ... respectively »), variation = réactif absent. Je n'ai pas inventé de nouvelle quantité de métal ; le point est en `missing_fields` et en doute.
- Fe:Ni=7:3 fusionné avec Fe2Ni MOF/NF : mêmes valeurs dans les tables S1 et S2 (222 mV, 42.4 mV dec−1) et mêmes quantités 0,7/0,3 mmol. Identité non écrite par l'article, doute posé ; l'échantillon d'inventaire Fe:Ni=7:3 pointe sur la voie de base.
- Fe:Ni=5:5 et 3:7 : rattachés comme branches (variations sur les deux sels, valeur en `value_text` = rapport écrit) bien que l'article ne dise pas qu'ils suivent la même procédure. Raison : le RUNBOOK exige des étapes pour une voie de base, et la seule information de l'article est le rapport. Choix signalé en doute et en `limite_reproductibilite` ; le critique peut préférer une autre lecture.
- Résultats des rangées de tables S1/S2 : citations multi-lignes (cellules sur des lignes séparées dans le texte, collées par le contrôle) attribuées par le nom de l'échantillon écrit dans la rangée, jamais par position.
- Tafel 42.39 (texte) retenu pour Fe2Ni plutôt que 42.4 (tableau S1) : texte et tableau concordent à l'arrondi.
- Surpotentiel lu sur la courbe de retour du CV (« inverse curve of CV »), pas sur le LSV : noté en doute, la valeur 222 mV est celle des auteurs.
- Stabilité : le texte dit « current densities increased by 3.7% » alors que la Fig. 4d porte un potentiel ; valeur du texte retenue, contradiction en doute.
- Blank NF et Fe2Ni MOF/NF après stabilité : dans l'inventaire sans voie (témoin non synthétisé, même échantillon). Les valeurs de la mousse nue sont dans l'annotation comparaison_branches.
- Figures : Fig. 4 et 5 (et Fig. 2) ouvertes ; toutes les valeurs sont déjà dans le texte ou les tableaux S1/S2, donc aucune valeur lue sur figure (`from_figure` : 0). Rct de l'EIS non chiffré dans l'article, non extrait.
- Annexes : texte du SI présent (légendes, tableaux S1 à S3), donc pas d'« annexe absente » ; en revanche numérotation des figures d'annexe du texte ≠ SI, et composition EDX (encart de Fig. S6c) visible seulement sur image absente : signalé en `limite_reproductibilite`.
- `method_sources` vide : les renvois de l'article (MIL-88B, CCDC) servent à l'attribution de phases, pas à une méthode de préparation.
