# Journal d'extraction PMC11818718

- Découpage : une voie de base « Pure » (CuS par co-précipitation, seul protocole détaillé) et quatre branches « 2.5% Ba », « 5% Ba », « 7.5% Ba », « 10% Ba ». Le texte dit que « the same process described above » a été utilisé avec BaCl2 ajouté à la solution B, donc l'héritage des neuf étapes est fondé.
- Variation « dopant » : le Ba n'existe pas dans le parent, donc nom explicite, `parent_value: none`, valeur x = 0.025/0.05/0.075/0.1 (nombre présent dans la citation). Le lien x → « 2.5 % Ba »… vient des noms d'échantillons des Tableaux 1 à 4 ; l'article ne l'écrit pas mot pour mot. Avertissement de `load.py` sur ce nom conservé volontairement.
- Quantités : l'article écrit « 2 M of sodium sulfide hydrate was dissolved in 25 ml » et « 10 ml of distilled water was mixed with 2 M copper chloride » ; extrait tel quel (amount 2, unit M) et volume d'eau séparé, doute posé car ni masse ni moles ne sont données. Pas de conversion.
- Quantité de BaCl2 : seul x est donné, donc `amount` déclaré non cité et laissé hors du réactif ; non précisé si Cu est diminué de x (doute).
- Pureté : « ≥99 % », « ≥65 % » prises dans la phrase de la section Materials ; fournisseurs non cités (aucun dans l'article). La phrase « used without further purification » n'est pas une pureté.
- Durées en toutes lettres (« two hours », « three hours », « many times ») mises en `value_text`, sans nombre ; seuls « 20 minutes », « 1 hour », « 100 °C » sont numériques.
- Vieillissement : température non citée (ambiante seulement implicite) → `not_stated`.
- Tableau 1 : la rangée entière est citée pour chaque échantillon ; attribution par le nom (Pure, 2.5 % Ba…). Les valeurs a = 3.792 Å, c = 16.344 Å du texte ne sont pas extraites (elles semblent venir de la fiche JCPDS) ; doute posé.
- Tableau 2 (TXRF) : pas de Ba pour Pure (« — ») ; unité « % » non précisée (atomique ou massique).
- Figures lues : Fig. 10 (intensité PL au pic de 826 nm, ≈ 510, 300, 420, 460, 290 u.a., précision ≈ ±10) car le texte ne donne que des tendances ; Fig. 2 (marqueurs # BaS et ⊙ BaCu4S3 par échantillon). Les autres figures (4, 5–9, 11, 12) n'apportent pas de valeur absente du texte ou des tableaux (Fig. 11–12 redoublent le Tableau 4).
- Contradiction XRD : « no other phase was seen » puis pics d'impuretés à 24.3° et 43.5° quand Ba augmente ; les deux sont signalés, la figure tranche la présence par échantillon.
- Doxorubicine (Tableau 4) : médicament de référence, mis dans l'inventaire sans voie ; la valeur 4.12 μg ml−1 n'est pas un outcome d'une voie.
- Tests MTT : rangés en outcomes (IC50) de chaque voie, jamais en branches ; le protocole cellulaire n'est pas une voie matériau.
- `method_sources` vide : aucun renvoi bibliographique ne porte sur la préparation ni sur le protocole MTT (les renvois sont des formules d'analyse ou du contexte).
- Introduction : « lower temperature requirement (90 °C) » contredit « room temperature » ; non extrait, noté en doute.
