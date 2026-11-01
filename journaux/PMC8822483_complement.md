# Journal de la passe de complément — PMC8822483

Points de la sonde écartés
- rampe de chauffe (TGA, 5 °C/min sous N2 à 20 mL/min) : déjà présente dans `characterizations.conditions` des deux voies de base ; ce n'est pas un paramètre de synthèse, rien ajouté.
- rendement chiffré : les deux voies de base ont déjà `yield` (57 % et 50 %) ; les rendements des branches sont dans `outcomes` (Tableaux 1 et 2). Les voies in situ, le MgFe2O4 et le lit n'ont aucun rendement (« to yield a black powder » sans masse), `not_stated` conservé.
- échelle / lot : « future scale-up » est une perspective, pas une échelle. Les routes in situ n'ont pas de `scale` ajouté (le champ n'a pas de citation).
- VSM, ICP/EDS : conditions déjà présentes pour le lit (RIKEN DENSHI, température ambiante, 5 kOe). VSM du MgFe2O4 seul (Figure S21) : aucune valeur dans le texte, non ajouté.
- électrochimie : faux positif (« capacity », « potential » dans l'adsorption) ; rien à mesurer en électrochimie ici.
- catalyse / adsorption : les « catalytic » de l'introduction sont du contexte.

Rattachements non évidents
- Isothermes de vapeur et de N2 à 298 K (Micromeritics 3Flex) : l'échantillon n'est pas précisé dans l'article ; rangées dans le lit, comme les capacités d'équilibre déjà extraites (doute existant).
- MEB à 25 °C (50 nm) : Figure 3B ne dit pas R4 ou R5 ; portée sur les deux, avec un doute.
- Fraction 89/11 % UMCM-1/MOF-5 : estimation des auteurs, valable pour tous les échantillons ; mise sur la voie de base seulement. Diamètre de fibres 100 nm et TGA (150, 450 °C) aussi sur la base, 435 °C sur la base MUF-77-methyl.
- Scherrer et ajustements Avrami/Finke-Watzky : ajoutés comme caractérisations des deux voies in situ de base (facteur de forme 0.9, OriginPro 2018, ScatterBrain), la branche 80 °C en hérite.
- Densité de tassement du Tableau S6 recopiée avec l'unité de l'article (g/mm3), doute sur l'unité (≈ 0.15 g/cm3 d'après la masse et le volume du lit).
- Réaction 3 pour le lit : nombre de lots nécessaires non cité, `repetitions` ajouté en `not_stated` de la voie ; idem pour les deux voies de base (« average yield » sans nombre de répétitions).

Cases `not_stated` ajoutées (recherche dans tout le texte, annexes comprises)
- séchage sous N2 des voies de base : `gas_flow` ; étape react des voies de base : `mixer_type` (aucun mélangeur mentionné, seulement « roller mixer »).
- truxène (reflux) : `atmosphere`, `stirring_speed` ; MgFe2O4 (reflux) : `atmosphere`, `heating_rate`, `stirring_speed` ; séchage sous vide : `pressure`.
- lit, dispersion : `stirring_speed`.
- Aucune case `not_stated` retirée : aucune n'est contredite.

Autres ajouts : `cooling_mode` (truxène, « cooled and poured on ice »), `exchange_interval` (DCM renouvelé chaque jour, deux voies de base). Instrument et conditions du MEB du MgFe2O4 (JEOL 7001F FEGSEM, Ir) renseignés. Fréquence du champ alternatif, durée de régénération et pression du lit : consignées dans un doute, pas en `not_stated` (opération du dispositif, pas étape de la voie).
