# Journal d'extraction PMC13516552

- Découpage en quatre voies : Poly-CoPc (voie de base, matériau), Poly-CoPc/SWCNT (voie de base indépendante, car protocole propre avec ses étapes ; le Poly-CoPc y entre comme réactif `intermediate`), et deux voies `device` (électrode + pile bouton). L'article ne balaie aucune condition de synthèse : pas de branche de synthèse.
- Électrode du composite = branche de l'électrode Poly-CoPc (« same » formulation 8:1:1 décrite pour « Poly-CoPc or Poly-CoPc/SWCNT composite » en 2.5) ; seule variation : le matériau actif, déclaré par remplacement du réactif parent (valeur `replaced by`).
- Température de synthèse : Méthodes « 175–180 °C … 10–12 h », Résultats 3.1 « 185 °C for 10–12 h » (et « solvothermal ») : valeur des Méthodes retenue en `value_text` (plage, pas de branche par borne), contradiction en doute.
- Quantités des réactifs du Poly-CoPc : seul le rapport molaire 2:1:6:12 est donné ; `amount` déclaré non cité pour chaque réactif et le rapport porté en paramètre `molar_ratio` de l'étape de broyage (texte). Molybdate « small amount » : paramètre `amount` en `value_text`, amount du réactif non cité.
- Fournisseur : la phrase « All chemicals were purchased from Sigma-Aldrich or TCI … » est appliquée aux réactifs de 2.1 et à Super P/PAA/éthanol ; pas appliquée au cuivre, lithium, Celgard, LiPF6 (non listés en 2.1) ; aucune pureté (« used without further purification » n'est pas une pureté).
- Tableau 3 (efficacité coulombique, 10 cycles) : chaque rangée a deux colonnes (Poly-CoPc, Poly-CoPc/SWCNT), attribuées par l'en-tête de colonnes « Poly-CoPc | Poly-CoPc/SWCNT » ; la rangée entière est citée pour chaque valeur. Le 58,30 % du texte correspond au 58,29749 du tableau : tableau retenu.
- Tableau 4 : 855 mA g−1 à 0,5 A g−1 (texte, composite) contre 847 mAh g−1 (tableau) : les deux gardées sous des noms de propriété distincts, doute noté. Deuxième colonne « 0,1 A g−1 » du tableau = retour à 0,1 A g−1 (`rate_capacity_back_at_0.1_A_g-1`).
- Tableau 6 (EIS) : C1 du Poly-CoPc (1,386 × 10−7) et C2 du composite (8,892 × 10−8) en `value_text` car l'exposant ne se cite pas comme nombre JSON.
- Table 5 (comparaison à la littérature) : non extraite, rangées « This work » identiques à la Table 2 ; échantillon d'inventaire sans voie (matériaux d'autres publications).
- Unités : capacités en « mA g−1 » dans le texte et la Table 2 recopiées telles quelles, « mAh g−1 » pour la Table 4 ; doute noté.
- Raman : bandes D et G données seulement pour le composite ; rien inventé pour le Poly-CoPc.
- BET « at 100 K » recopié tel quel (77 K attendu) en condition de caractérisation et doute.
- Figures : dossier corpus/fig/PMC13516552 vide, aucune valeur lue sur figure (Fig. 3b, 7, 8a-f, 9) ; noté en `limite_reproductibilite`. Aucune annexe n'est citée ni présente.
- Sources de méthode : B27 et B28 (« method adopted from earlier works ») en `protocole_adapte` ; les autres renvois sont du contexte.
- Le rendement du composite n'est pas donné : `yield` en `not_stated`.
