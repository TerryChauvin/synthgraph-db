# Journal d'extraction PMC7344730 (LiFePO4–PANI, cathode Li-ion)

- Découpage : deux voies de base (PANI, section 2.1 ; LFP-PANI, section 2.2), puis deux voies `device` (électrode, section 2.4, et cellule de test). Aucune branche : l'article ne balaie aucun paramètre de synthèse (un seul rapport 75/25, une seule température, 300 °C).
- PANI classée `intermediate` car elle est réutilisée (« 0.25 g of synthetized PANI (i.e., EB) ») mais elle est aussi testée seule (capacité, EIS, DRX) ; ses résultats restent sur sa voie. Dans LFP-PANI elle figure en réactif de rôle `intermediate`.
- LiFePO4 commercial : échantillon de l'inventaire sans voie (aucun protocole, acheté enrobé de 2 % de C). Ses résultats (120 mAh g−1, Rct 178 Ω, 300 nm) sont cités seulement dans l'annotation `tendance_observee`, pas recopiés sur une voie qu'il n'a pas.
- Rendement : Méthodes « 99.98% » contre Prime Novelty « 99.99% » ; valeur des Méthodes (section la plus détaillée), autre valeur en doute.
- Capacité à 1 C : seule valeur de texte = 120 mAh g−1 dans la déclaration de nouveauté ; la Fig. 18 donne ≈ 117. Texte retenu, figure en doute. La Fig. 18 n'est lue que pour ce qui n'est écrit nulle part : 0.5 C (≈ 130) de l'hybride et 0.2 C (≈ 60) de PANI. Les points de PANI à 1 C et 5 C valent 0 sur la figure : non extraits (aucun commentaire des auteurs, probablement non mesurés).
- Tenue en cyclage : « 0.2% capacity fade over 50 cycles » (Résultats) et « 99.0% capacity retention » (Novelty) sont deux valeurs légèrement incompatibles ; les deux sont gardées avec leur citation et un doute.
- Fenêtre de potentiel : 2.5–4.2 V (Méthodes) pour la cellule ; 2.4–4.2 V dans les Résultats ; 2.5–3.9 V pour PANI seul (annexe). Lecture des Méthodes sur la voie cellule, autres en doute.
- Type de cellule : trois appellations (bottom-type, button-type, pouch). Aucune n'est mise en paramètre ; équipement = « bottom-type test cell » des Méthodes.
- Chauffage à 300 °C : action `heat` (pas `calcine`) car les auteurs parlent de « thermal treatment » d'un mélange polymère/sel de lithium ; atmosphère en paramètre texte ; vitesses de chauffe et de refroidissement et débit de gaz déclarés non cités. Le four vient du résumé (« in a furnace »).
- Électrode : rapport « 80:10:10 » avec « respectively » dans la phrase : ordre actif / Super P / PVDF écrit, donc 80/10/10 attribués par `amount_text` ; seule l'électrode LFP–PANI est décrite (rien pour PANI ni LiFePO4 seuls : signalé en limite de reproductibilité).
- Rôle des citations : valeurs de tableau 1 attribuées par le nom de la rangée (« PANI as assembled (OCV) », « LiFePO4–PANI as assembled (OCV) »), jamais par position.
- `method_sources` vide : les renvois B12, B15 (réticulation), B11 sont des interprétations ou du contexte, aucun protocole à refaire n'est délégué à une référence.
- Annexes : le fichier contient les légendes S1 à S10 (figures sans valeur supplémentaire hors EDS de PANI, non reprise, et PANI à 95 mAh g−1 reprise) ; aucune annexe absente.
- Figures ouvertes : Fig. 18 (lue), Fig. 17 et 15 (vérifications sans extraction ; PANI plateau ≈ 91 contre 95 du texte : doute).
