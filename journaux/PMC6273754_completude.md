# Journal du test de complétude — PMC6273754

- Extraction d'origine déjà très complète : 60 nombres de tableaux et 8 de la partie expérimentale couverts à 100 %. Les manques sont tous dans le texte des Résultats et dans les valeurs de comparaison.
- Bord d'absorption 511 → 505 nm : le texte ne nomme pas les échantillons. Attribution aux bornes de la série en température (CdS-120 puis CdS-190), signalée en doute. Le sens « croissant avec la température » est écrit dans la phrase citée.
- « Around 510 nm » est attribué à CdS-1.3 et CdS-3.0 seulement ; CdS-2.0 est CdS-120 (même échantillon), qui garde 511 nm. Pas de doublon.
- Rapports Cd/S : valeurs du texte conservées (0,85 et 0,90, en `value_text` « close to »), bien que le tableau 1 donne 0,93 (CdS-150) et 0,88 (CdS-3.0) ; écart noté en doute, aucun résultat existant modifié.
- Les constats qualitatifs de DRX (intensité de (002)) et de HRTEM sont rattachés à chaque échantillon par leur citation ; pour CdS-120 et CdS-150, la phrase qui les groupe est citée deux fois (une par voie).
- Pas de voie `calcul` : l'article n'a aucun calcul DFT ni simulation.
- Conditions de mesure : TXRF ajouté dans deux nouvelles entrées (profondeur sondée, détecteur) plutôt qu'en prolongeant la chaîne `conditions`. Le point « électrochimie » de la sonde est un faux positif (comparaison absorbance/activité), le point « atmosphère » (séchage sous vide) est déjà extrait (`pressure`, « under vacuum »).
- Comparaisons : 2,40 eV et 515 nm pour le CdS massif, rayon de Bohr 2,5 nm. Pas de `ref_id` : les renvois sont multiples ([B31], [B32] pour 515 nm) ou groupés ; B31 et B32 sont cités dans `conditions` pour 515 nm. La valeur 2,4 eV de l'introduction est un doublon de 2,40 eV, non ajoutée.
- Ajout d'une annotation `mecanisme_auteurs` pour la photocatalyse (réaction globale écrite dans l'article), la seule déjà présente portant sur la synthèse.
- Aucune figure ouverte : les résultats chiffrés absents du texte étaient déjà lus (Fig. 8, 9, 11) dans l'extraction d'origine.
- Les conditions absentes (facteur K de Scherrer, type de transition de Tauc, tension du MEB, flux lumineux, répétitions) sont dans `doubts`, pas dans `not_stated`. Aucun fichier de relecture par les pairs dans le texte.
