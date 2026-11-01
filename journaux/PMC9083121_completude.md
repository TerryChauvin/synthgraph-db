# Journal du test de complétude — PMC9083121

- Lecture intégrale du texte (corps, légendes, annexe de 8 pages) et de l'extraction avant toute édition ; la liste A (9 nombres) et la sonde (3 points) ont été traitées, puis une recherche des informations sans nombre.
- Les 9 éléments de A sont tous pertinents : aucun écarté. 1,84 eV, 4,9 et 5,6 eV sont des valeurs de référence : placés dans de nouvelles entrées de `characterizations` (les `conditions` existantes n'ont pas été touchées, règle « ajouter seulement »), avec des noms de technique distincts pour éviter de recouper les entrées déjà présentes.
- 595 nm, 14 nm, 70 pm et 95 pm sont des valeurs rappelées pour interpréter, sans renvoi identifiable : `comparisons` sans `ref_id`, avec un doute.
- Pic EDS « 2.3 eV » : recopié en eV comme écrit (aucune conversion) ; doute noté car l'axe de la Fig. S6 est en keV.
- Tension de retour STM « 3.0 V » (SA3) : signe peut-être perdu à l'extraction du texte ; `value_text` et doute, pas de `value_num`.
- Valeurs « pour tous les échantillons » (pic à 397 nm, émission à 574 nm) : recopiées dans chaque échantillon concerné comme l'extraction d'origine le faisait pour XRD et Scherrer. Pour SA5, l'excitation à 397 nm est citée sur la phrase de l'effet des micro-ondes (valeur propre à SA5).
- Éléments communs à toutes les branches (constantes du calcul de taille, K de Scherrer) : placés une seule fois sur SA1, voie de base. Les branches SA5_noMW et SA5_pH_series ont leurs propres copies d'étapes 1 à 5 : je n'y ai pas répété les modes d'addition (ajoutés sur SA1 uniquement).
- `not_stated` ajoutés seulement après recherche de flask, beaker, vial, container, cool, batch dans le texte : aucun résultat, d'où `vessel`, `cooling_mode`, `repetitions`.
- Poole–Frenkel : l'article n'en donne pas de paramètres chiffrés (φB, pente) ; seuls le mécanisme et la linéarité sont enregistrés. Pente d'ajustement de la Fig. 5b déjà en doutes.
- Non ajouté : valeurs de VTh de SA2, SA4, SA5 (figures S8, S9 absentes), durée de vie « de l'ordre de la nanoseconde » (générale), nombre de particules comptées en TEM (non donné), diamètre critique propre à CdSe au-delà de la phrase citée.
- Avertissements du contrôle (5) : tous antérieurs, aucun lié aux ajouts.
