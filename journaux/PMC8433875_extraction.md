# Journal d'extraction PMC8433875 (SnS par CVD à partir de [Sn(SBut)(tfb-dmeda)])

- Découpage : sept voies. `Sn(SBut)2` (kind `intermediate`, thiolyse du stannylène à 0 °C, aucune quantité donnée) et `Complex_1` (le précurseur 1, rendement 82 %, voie de base du matériau moléculaire) ; puis le dépôt CVD sur FTO (`SnS_FTO_350`, voie de base) et quatre branches sur Mo-SLG.
- `Complex_1` est gardé en `material` (c'est le produit caractérisé de l'article) bien qu'il soit réutilisé : dans le dépôt CVD il entre comme réactif de rôle `intermediate` qui nomme la voie.
- Stannylène [Sn{N(SiMe3)2}2] et ligand Htfb-dmeda : pas de voie propre, protocoles renvoyés aux réf. B35 et B34 (`method_sources`) ; `route: null` dans l'inventaire.
- Fournisseur du ligand : « provided by the working group members » est recopié tel quel (phrase citée), pureté non citée (« checked by NMR » n'est pas une pureté).
- Pureté des solvants : la phrase générale « Solvents were dried by refluxing over sodium and benzophenone… » vaut pour le toluène des deux synthèses (elle vise tous les solvants), recopiée comme pureté.
- Unité de la température d'ajout : « at 0° by cooling with crushed ice » lue en °C (doute noté) ; « T = 0 °C » pour Sn(SBut)2.
- Étapes à plage : sublimation « 90–100 °C, 10−3 mbar » en `value_text` (pas de nombre unique).
- Échantillon sur Mo-SLG de la figure 7 : durée non donnée. Plutôt que d'hériter les 30 min du FTO, la branche `SnS_Mo_350` porte une variation de durée en `value_text` « 15, 30, and 60 min » (règle des plages) ; les trois branches 15/30/60 min en héritent et fixent chacune leur durée.
- Épaisseurs 440 nm, 1 µm, 2 µm : attribuées dans l'ordre de « (15, 30, and 60 min) », confirmé par la légende de la figure 8 (a: 15 min, b: 30 min, c: 60 min). L'étiquette de la figure 8a semble lire 450 nm contre 440 nm dans le texte : texte retenu, doute noté.
- Vitesse de croissance de 33 nm/min : résultat de groupe, donc annotation `tendance_observee` et non valeur répétée sur chaque voie.
- Résumé : température de dépôt « 300–450 °C » et Tp « 90–130 °C » ne sont que des plages ; aucune branche créée, `limite_reproductibilite` ajoutée. Seul Ts = 350 °C a des résultats.
- Équipement CVD : le tube de quartz à porte-substrat de graphite et le réacteur « cold-wall » à p < 10−6 bar sont lus comme le même appareil ; les deux citations sont gardées.
- 119Sn : trois valeurs (−159, −157, et les entrées à 149,2 et 111,9 MHz) ; −159 retenue pour l'outcome, doute noté.
- Figures ouvertes : schéma 1, figures 6 et 8. Aucune valeur numérique supplémentaire lue (tout est dans le texte), donc pas de `from_figure`.
- Annexes absentes : tableaux S1, S2 et figures S1 à S7 (aucune section Supporting Information dans le fichier) ; annotation `limite_reproductibilite` d'article.
- [Sn(SBut)4], composé de comparaison en spectrométrie de masse : pas de voie (non synthétisé ici).
