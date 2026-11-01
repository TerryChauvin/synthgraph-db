# PMC5680254 — critique scientifique (journal de décisions)

- Au_Si_substrate : `probleme` sur l'ordre de dépôt écrit (Au puis Ti « pour l'adhérence »). Une couche d'accroche ne peut être que sous l'or. Suivre le texte à la lettre donnerait une surface de Ti, pas l'or (111) de l'article. Jugement porté sur le protocole écrit, pas sur l'extracteur (qui l'a signalé en doute).
- ZnO_0mM : `probleme` sur le bilan, car aucune concentration de précurseur n'est donnée. Xu et al. 2008 (réf. 27 de l'article) montre que la densité sans germe dépend justement de cette concentration. DOI 10.1557/JMR.2008.0274 pris dans une liste de références d'un autre site, non vérifié sur Crossref.
- Mécanisme (`probleme`) : la phrase « peu d'espèces Zn(II) positives à pH 6,8 » contredit la spéciation à 85 °C, où [Zn(H2O)6]2+ domine sous pH ≈ 8 (Villafuerte et al. 2022, Nanoscale Adv., lu en résumé et en extraits). La phrase « plus de Zn(II) en solution → moins de solubilité » est contradictoire en soi.
- « Changement exponentiel » entre pH 6,8 et 7 recalculé : pente −2 de log[Zn2+] contre pH, soit un facteur 2,5 sur la solubilité. Classé `reserve` : le sens est défendable, le mot est exagéré.
- Amplitude de densité recalculée sur la Fig. 1f (image relue, lecture de l'extracteur confirmée) : 1,7 ordre entre 10 et 40 mM, facteur 2,5 entre 0 et 40 mM. `probleme` contre « two orders » / « more than two orders ». Le minimum à 10 mM porte toute l'amplitude ; `reserve` sur ZnO_10mM (pas de répétition).
- pH 7 à 40 mM : NH3 seul donnerait pH 10,9 ; le pH annoncé suppose environ 20 mM de Zn ou plus pour consommer NH3. Plausible mais invérifiable. pH 6,8 à 10 mM cohérent avec le pH propre de 6,6 d'un bain équimolaire (Amin 2011).
- Équation 10 (2πr²) : rayons recalculés à rebours à partir des moyennes de VTH et ne. Avec 2πr² : 137 / 212 / 90 nm, dans la plage pointe–base de la Table 1. Avec πr² : 213 / 333 / 140 nm, au-dessus du rayon de base à 20 et 40 mM. D'où `probleme` : ne est probablement sous-estimée d'un facteur 2 (calcul indicatif, sur des moyennes).
- Formule de référence πr²L : posée par définition (charge rapportée au volume du cylindre), car aucun extrait trouvé ne montrait le texte de la formule chez Goldberger 2005 ; cette source ne sert qu'aux ordres de grandeur (13 cm²/Vs, 5×10^17 cm−3, on/off 10^5–10^7). Noté dans `sources_not_found`.
- Mode « accumulation » avec VTH négative : signalé comme mode déplétion (`reserve`), sans conséquence sur les valeurs.
- Raman 332 cm−1 : c'est le mode à deux phonons E2(high)−E2(low) (Cuscó 2007), pas des « joints de phases » (`reserve`, vocabulaire).
- Rôle de coiffe du HMTA (annotation d'analyse) : réfuté par McPeak 2011 (ATR-FTIR) ; mécanisme proposé = HMTA régulateur de sursaturation.
- Défauts donneurs : les auteurs invoquent VO et Zni sans preuve discriminante ; l'alternative H et N (Villafuerte 2022) est sourcée. Le diamètre deux fois plus petit à 40 mM est un facteur de confusion pour la mobilité.
- Autoclave : P(H2O) ≈ 0,57 bar à 85 °C (Antoine NIST, paramètres de mémoire, non relus) ; pas de risque, aucune source web.
- 7 recherches web. Aucune référence ajoutée à fondateurs.md ni constantes.md (Crossref bloqué).
