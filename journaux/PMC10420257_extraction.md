# Journal d'extraction PMC10420257 (ZnO par co-précipitation, PL QY)

- Découpage : une voie de base `ZnO_Ac_KOH4_water` (section 2.1 : acétate + 80 mmol KOH, 70 mL d'eau, « 4 KOH/Zn acetate » dans l'eau, choisie parce que l'eau est retenue pour toute la suite, § 3.1) ; sept branches pour les autres échantillons nommés (éthanol, 2 KOH, 2 et 4 LiOH sur acétate, 4 KOH / 2 LiOH / 4 LiOH sur sulfate). Le protocole n'est décrit qu'une fois, avec « replaced by » pour sulfate et LiOH : héritage accepté pour toutes les branches (pas de phrase « same procedure », signalé en doute).
- Échantillons au sulfate : rattachés à la voie de base avec deux variations (précurseur remplacé, KOH remplacé par LiOH) plutôt qu'en chaîne, pour ne pas hériter d'une absence de réactif en cascade.
- Quantités de LiOH : l'article ne donne que le rapport de volumes solution LiOH / zinc (2:1, 4:1) et les « eq. » ; pas de mmol. Mis dans `amount_text`, sans nombre ; sulfate de zinc sans quantité (`not_stated: amount`).
- Échantillon « 2 KOH/Zn acetate » : une seule phrase (§ 3.3, « oligomeric Zn(OH)x(OAc)y species ») ; voie créée avec `succeeded: false`, matériau de famille « autre » sans formule.
- Éthanol : « 70 mL of ethanol or water » et « an aqueous or ethanol solution containing 80 mmol of KOH » ; variation du solvant du zinc uniquement, solvant de la solution de KOH incertain (doute).
- Tableau 1 : colonnes KOH (4 eq.), LiOH 2 eq., LiOH 4 eq. ; rangée attribuée par l'en-tête. Tableau 2 : FWHM et tailles pour (101) et (002), la note « * » dit que 20 nm (101) est la taille retenue dans le texte ; les deux tailles sont extraites.
- Tableau 4 : une valeur `PL_QY` et une valeur de texte « positions des pics (aire %) » par échantillon ; la rangée 4 LiOH/Zn acetate porte « 566 * » (pics VO et VO++ fusionnés), recopié tel quel. Teneur en Oi (13,4 % et 33,7 %) tirée de la phrase du § 3.4 et rattachée à 4 LiOH/acétate et 4 LiOH/sulfate.
- Contradiction PL QY : texte « about 2% » (eau et éthanol) contre tableau 4 « 3 ± 1% » pour 4 KOH/Zn acetate ; les deux sont gardées, avec leurs citations (doute).
- Figure 3 : le texte dit aiguilles = 4 KOH, plaquettes = 4 LiOH, mais cite « needles in Figure 3a,c » alors que la légende place 4 LiOH en a et c ; lecture retenue : énoncé du texte et conclusion (doute).
- Figure 1 : seule figure ouverte ; les rapports Vis/UV (16 eau, 29 éthanol) sont imprimés sur la figure, donc lus sans estimation graphique. Les autres figures (XRD, TEM, Raman, spectres, camemberts) portent des résultats déjà dans les tableaux 1 à 4 ou qualitatifs.
- Température : « ambient conditions » (§ 3.4) retenu en `value_text` de l'étape d'agitation ; vitesse de centrifugation, nombre de lavages, volume et concentration des solutions de base déclarés non cités.
- Détection du lithium par NRA : phrase non rattachée à un échantillon précis, donc annotation d'article (`tendance_observee`) et non un résultat de voie.
- `method_sources` : seul De Mello et al. (B23, calcul de la PL QY) retenu en `autre` ; Spanhel (croissance préférentielle) et autres renvois sont du contexte.
- Annexe absente : Figure S1 (XRD eau/éthanol), annotation `limite_reproductibilite`.
