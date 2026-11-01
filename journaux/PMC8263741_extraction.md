# Journal d'extraction PMC8263741 (Li4PS4I, trois voies de synthèse)

- Découpage : deux voies `intermediate` (Li3PS4·DME ; verre broyé 1.5Li2S–0.5P2S5–LiI) car elles sont préparées par les auteurs puis réutilisées : le verre sert à la fois à la voie solide et au pressage à chaud, d'où une voie propre plutôt qu'une étape dupliquée. Trois voies de base matériau (Solvent_175, SolidState_175, HotPress_175), chacune avec deux branches en température (200 et 250 °C).
- Voie de base = l'échantillon à 175 °C, première valeur de la liste « 175, 200 or 250 °C » dans chaque protocole des Méthodes ; les branches ne varient que le paramètre `temperature` de l'étape de recuit ou de chauffage (« annealed at 175, 200 or 250 °C », « heated to the target temperature (175, 200 or 250 °C) »).
- Solvent_*, étape 1 : « added to a solution of 247.7 mg LiI … in 10 mL DME » lu comme dissolution de LiI puis ajout de Li3PS4·DME ; l'article ne sépare pas les deux gestes (doute consigné).
- Pression du pressage à chaud : 176 MPa (Results) contre 173 MPa (Methods et expérience in situ). Valeur des Méthodes retenue ; la citation de la voie garde la phrase des Résultats (176) pour la description générale.
- Conductivités ≥ 1×10−3 S cm−1 (verre, HotPress_175 et 200) : écrites en `value_text` car le contrôle ne retrouve pas la notation « 2.6×10−3 » pour value_num au-dessus de 1e-3 ; les valeurs en dessous (6.6×10−4, 1.7×10−5…) sont numériques.
- « respectively » : « 1.5×10−4 and 6.4×10−5 S cm−1 at 200 and 250 °C, respectively » (200 puis 250) ; « LiI and Li6PS5I … ~ 0.4 and 14.1 wt.% » (LiI 0.4, Li6PS5I 14.1) ; pour le pressage à chaud, « LiI and Li6PS5I as minor (~ 1.6 wt.%) and major (~ 13.4 wt.%) » (LiI 1.6, Li6PS5I 13.4).
- Densités du solide : « from 2.07 to 2.65 g cm−3 … from 175 to 250 °C (2.58 g cm−3 at 200 °C) » attribuées 175 / 250 / 200. Les valeurs de la Fig. 3b (ouverte) concordent avec le texte.
- Conductivité du verre : ~1.2×10−3 (voie solide) et 1.1×10−3 S cm−1 (mesure in situ 76 Ω, et Arrhenius) ; les deux sont gardées en outcomes de la voie Glass, avec un doute.
- Expérience pTR in situ (Fig. 4) : rangée dans les caractérisations et résultats de HotPress_250 (même chauffage 500 °C h−1 jusqu'à 250 °C), sans voie propre, mais l'inventaire la liste séparément. Palier 5.5 h (Results) contre 5 h (Methods) en doute.
- Phases pour 175/200 °C en pressage à chaud : une seule phrase pour les deux (« at 175 and 200 °C, virtually no crystallization ») ; recopiée dans les deux voies avec la mention de phrase commune.
- Phases de la voie solide à 200 °C : Li6PS5I « appeared » sans température dite ; rattachée à 200 °C par la formulation « on increasing the annealing temperature », avec doute.
- Annexes : section SI présente (légendes S1 à S5, Table S1 sur Rwp et χ2) ; aucune annexe absente, mais les spectres d'impédance et la modélisation JMAK ne sont que des légendes (annotation limite_reproductibilite). Fig. S1/S2/S5 non utilisables numériquement.
- Pas de valeur lue sur figure : tout est dans le texte. Seule la Fig. 3 a été ouverte, pour vérification croisée.
- `method_sources` : CR29 (voie solvant), CR31 (montage de pressage à chaud) ; CR25, CR52 (FullProf), CR53, CR54 (VESTA) ignorés : contexte, logiciel ou analyse.
- Sécurité : Li2S/P2S5 → H2S ; DME inflammable ; ampoule scellée sous vide ; pressage à chaud (analyse, sans citation).
