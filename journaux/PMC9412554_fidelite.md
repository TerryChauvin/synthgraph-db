# Journal de la critique de fidélité — PMC9412554

- Ma liste d'échantillons avant ouverture de l'extraction : PAA (solution, fibres), PI, PI/TiO2, PI/TiO2@MoS2, plus PI/MoS2 cité seulement dans la légende de la figure 4. Identique à `sample_inventory` ; aucune branche manquante. PI/MoS2 sans préparation : absence de voie justifiée.
- `method_sources` vide : confirmé. Les 43 renvois de `corpus/refs` sont tous en introduction, en comparaison ou en mécanisme. B34 (« PAA was analyzed in our previous report ») concerne l'analyse du PAA, pas sa préparation : non retenu comme constat (mis en notes).
- Les quotes de l'extraction sont toutes des sous-chaînes du texte (contrôle par script).
- Valeurs `from_figure` (figure 8 droite, lue avec Read) : PI ≈ 0,91, PI/TiO2 ≈ 0,305, PI/TiO2@MoS2 ≈ 0,05 à 180 min ; écart < 0,01, bien sous les 10 %. Pas de constat sur les valeurs elles-mêmes.
- Constat « PI et PI/TiO2, conditions et citation » en `mineur`/`probable` : la légende citée ne nomme que PI/TiO2@MoS2 ; 0,02 g de catalyseur et 5 mg/L de MB ne sont écrits que pour le composite final. Ce n'est pas une erreur de valeur, seulement un appui faible.
- Sublimation d'ODA/PMDA : `sure`, la phrase est dans l'article et l'extraction ne la garde que dans `supplier_quote`, pas dans un champ exploitable.
- FTIR de PI : `probable` seulement, car les bandes 1720/1648/1498/1405/725 cm−1 suivent la phrase sur PI/TiO2 et la figure 6f est légendée « of the nanocomposite » ; l'attribution à PI est une lecture (« imidization was completed » parle forcément du polyimide). Même prudence pour la FTIR « In MoS2 » : échantillon ambigu.
- XRD de PI/TiO2 : `sure`, la légende de la figure 4 nomme les trois échantillons et l'image montre bien les pics rutile pour PI/TiO2 ; le texte ne donne de valeurs que pour le composite.
- Équipement d'électrofilage : « syringe pump » et « high-voltage supply » sont des rôles supposés d'après les noms d'appareils, pas écrits : `deduit`, `probable`.
- Sécurité : le dégagement de H2 dans l'autoclave scellé figure dans l'équation de l'article (`2Ti+6HCl→2TiCl3+3H2(g)`) mais pas dans `securite_analyse` : `mineur`, `probable`.
- Écarté comme non-constat : (210)/(310) de la figure 4 contre (220)/(301) du texte (l'extraction suit le texte) ; Mo 3d3/2 et 3d5/2 inversés par les auteurs (extraction fidèle) ; teneur en solide 25 % incohérente avec les masses (domaine de la critique scientifique) ; « Titania powder » contre « titanium powders » (déjà en doute chez l'extracteur, lecture littérale défendable).
- `not_stated` : une quarantaine de cases vérifiées (températures, atmosphères, rampes, volumes, durées de séchage, rendement) ; aucune n'est renseignée dans l'article.
