-- Base de voies de synthese de materiaux extraites de la litterature open access.
-- Toute donnee extraite porte sa citation verbatim (quote) et sa position dans
-- le texte normalise de l'article (corpus/text/<PMCID>.txt).

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS papers (
    id            INTEGER PRIMARY KEY,
    pmcid         TEXT NOT NULL UNIQUE,
    doi           TEXT,
    title         TEXT,
    authors       TEXT,
    journal       TEXT,
    year          INTEGER,
    license       TEXT,
    url           TEXT,
    family_query  TEXT,               -- famille de la requete qui a trouve l'article
    text_chars    INTEGER,
    param_score   REAL,               -- indice d'etude parametrique (sections.py) : sert a ordonner la file
    pdf_path      TEXT,               -- corpus/pdf/<PMCID>.pdf si le PDF a pu etre telecharge
    -- fetched | queued | in_progress | extracted | rejected
    status        TEXT NOT NULL DEFAULT 'queued',
    reject_reason TEXT,
    seq           INTEGER,            -- rang d'extraction (1, 2, 3...) -> palier = (seq-1)/50+1
    palier        INTEGER,
    -- none | doubts | full  (niveau de relecture par l'orchestrateur)
    review_level  TEXT NOT NULL DEFAULT 'none',
    review_errors INTEGER,            -- nb de valeurs corrigees lors d'une relecture integrale
    review_values INTEGER,            -- nb de valeurs controlees lors de cette relecture
    fetched_at    TEXT,
    extracted_at  TEXT
);

CREATE TABLE IF NOT EXISTS materials (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    formula     TEXT,
    family      TEXT,                 -- MOF, nanoparticule, perovskite, oxyde, zeolithe, batterie, 2D...
    phase       TEXT,
    morphology  TEXT,
    UNIQUE (name, formula, phase, morphology)
);

-- Une voie = un protocole. Les branches pointent vers leur parent et ne
-- stockent que ce qui differe (route_variations) ; une branche sans etapes
-- herite des etapes de son ancetre le plus proche qui en possede.
CREATE TABLE IF NOT EXISTS synthesis_routes (
    id                 INTEGER PRIMARY KEY,
    paper_id           INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    material_id        INTEGER REFERENCES materials(id),
    parent_route_id    INTEGER REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    branch_label       TEXT NOT NULL,     -- nom d'echantillon dans l'article, unique par article
    is_baseline        INTEGER NOT NULL DEFAULT 0,
    method             TEXT,
    scale              TEXT,
    yield_value        REAL,
    yield_unit         TEXT,
    yield_quote        TEXT,
    succeeded          INTEGER,           -- 1 produit vise obtenu, 0 echec rapporte, NULL non precise
    missing_fields     TEXT,              -- JSON : informations absentes de l'article
    completeness_score REAL,
    quote              TEXT NOT NULL,
    section            TEXT,
    char_start         INTEGER,
    char_end           INTEGER,
    UNIQUE (paper_id, branch_label)
);

CREATE TABLE IF NOT EXISTS route_variations (
    id            INTEGER PRIMARY KEY,
    route_id      INTEGER NOT NULL REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    parameter     TEXT NOT NULL,      -- meme nom que parameters.name ou reagents.name du parent
    step_order    INTEGER,            -- etape du parent concernee (NULL si reactif / global)
    value_num     REAL,
    value_text    TEXT,
    unit          TEXT,
    parent_value  TEXT,
    quote         TEXT NOT NULL,
    section       TEXT,
    char_start    INTEGER,
    char_end      INTEGER
);

CREATE TABLE IF NOT EXISTS reagents (
    id          INTEGER PRIMARY KEY,
    route_id    INTEGER NOT NULL REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    name        TEXT NOT NULL,
    formula     TEXT,
    role        TEXT,                 -- precurseur, solvant, tensioactif, reducteur, base, ...
    amount      REAL,
    unit        TEXT,
    amount_text TEXT,                 -- quantite telle qu'ecrite si non numerique
    purity      TEXT,
    supplier    TEXT,
    supplier_quote TEXT,              -- citation de la purete / du fournisseur s'ils sont donnes ailleurs
    quote       TEXT NOT NULL,
    section     TEXT,
    char_start  INTEGER,
    char_end    INTEGER
);

CREATE TABLE IF NOT EXISTS steps (
    id          INTEGER PRIMARY KEY,
    route_id    INTEGER NOT NULL REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    step_order  INTEGER NOT NULL,
    action      TEXT NOT NULL,        -- dissolve, mix, heat, age, wash, dry, calcine, ...
    description TEXT,
    quote       TEXT NOT NULL,
    section     TEXT,
    char_start  INTEGER,
    char_end    INTEGER,
    UNIQUE (route_id, step_order)
);

CREATE TABLE IF NOT EXISTS parameters (
    id          INTEGER PRIMARY KEY,
    step_id     INTEGER NOT NULL REFERENCES steps(id) ON DELETE CASCADE,
    name        TEXT NOT NULL,        -- temperature, duration, heating_rate, pH, atmosphere, ...
    value_num   REAL,
    value_text  TEXT,
    unit        TEXT,                 -- unite telle qu'ecrite dans l'article
    value_si    REAL,                 -- valeur normalisee (K, s, Pa, K/s, rad/s...) quand calculable
    unit_si     TEXT,
    quote       TEXT NOT NULL,
    section     TEXT,
    char_start  INTEGER,
    char_end    INTEGER
);

CREATE TABLE IF NOT EXISTS equipment (
    id          INTEGER PRIMARY KEY,
    step_id     INTEGER NOT NULL REFERENCES steps(id) ON DELETE CASCADE,
    type        TEXT NOT NULL,
    detail      TEXT,
    quote       TEXT NOT NULL,
    section     TEXT,
    char_start  INTEGER,
    char_end    INTEGER
);

CREATE TABLE IF NOT EXISTS characterizations (
    id          INTEGER PRIMARY KEY,
    route_id    INTEGER NOT NULL REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    technique   TEXT NOT NULL,
    result      TEXT,
    quote       TEXT NOT NULL,
    section     TEXT,
    char_start  INTEGER,
    char_end    INTEGER
);

-- Grille de reproductibilite : informations attendues que l'article ne donne pas.
-- Une ligne = un « trou » declare explicitement par l'extracteur apres avoir cherche
-- (information absente ou seulement implicite). Jamais de valeur supposee.
CREATE TABLE IF NOT EXISTS not_stated (
    id          INTEGER PRIMARY KEY,
    route_id    INTEGER NOT NULL REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    scope       TEXT NOT NULL,        -- route | step | reagent
    step_order  INTEGER,              -- pour scope = step
    reagent     TEXT,                 -- pour scope = reagent
    name        TEXT NOT NULL,        -- temperature, duration, amount, purity, yield, ...
    status      TEXT NOT NULL DEFAULT 'non_cite'
);
CREATE INDEX IF NOT EXISTS ix_ns_route ON not_stated(route_id);

-- Publications que les auteurs citent comme source de leur methode (« as reported previously »).
-- status : listee | en_file (article source telecharge, a extraire) | extraite | non_libre | introuvable
CREATE TABLE IF NOT EXISTS method_sources (
    id            INTEGER PRIMARY KEY,
    paper_id      INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    route_id      INTEGER REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    ref_id        TEXT NOT NULL,       -- identifiant de la reference dans corpus/refs/<PMCID>.json
    role          TEXT,                -- protocole_complet | protocole_adapte | precurseur | autre
    authors       TEXT, title TEXT, journal TEXT, year TEXT, doi TEXT, pmid TEXT,
    source_pmcid  TEXT,                -- PMCID de l'article source s'il est en acces libre
    status        TEXT NOT NULL DEFAULT 'listee',
    quote         TEXT NOT NULL,       -- phrase de l'article qui renvoie a cette reference
    section       TEXT, char_start INTEGER, char_end INTEGER
);

-- Valeurs de la litterature citees par l'article pour situer ses resultats (tableaux de comparaison,
-- « reported values ») : jamais des resultats de l'article. Ajoute le 28/10/2026.
CREATE TABLE IF NOT EXISTS comparisons (
    id          INTEGER PRIMARY KEY,
    paper_id    INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    route_id    INTEGER REFERENCES synthesis_routes(id) ON DELETE CASCADE,  -- voie de l'article comparee
    material    TEXT NOT NULL,        -- materiau de la litterature
    property    TEXT NOT NULL,
    value_num   REAL,
    value_text  TEXT,
    unit        TEXT,
    conditions  TEXT,                 -- conditions de la mesure citee, telles qu'ecrites
    ref_id      TEXT,                 -- identifiant dans corpus/refs/<PMCID>.json si l'article le donne
    quote       TEXT NOT NULL,
    section     TEXT, char_start INTEGER, char_end INTEGER
);

-- Ce que chaque voie / branche a donne : permet de comparer les variations.
CREATE TABLE IF NOT EXISTS outcomes (
    id          INTEGER PRIMARY KEY,
    route_id    INTEGER NOT NULL REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    property    TEXT NOT NULL,        -- particle_size, bet_surface_area, phase, purity, capacity...
    value_num   REAL,
    value_text  TEXT,
    unit        TEXT,
    quote       TEXT NOT NULL,
    section     TEXT,
    char_start  INTEGER,
    char_end    INTEGER
);

-- Annotations de comprehension : interpretations redigees par Claude, a ne pas
-- confondre avec les donnees extraites. quote = passage d'appui (facultatif).
CREATE TABLE IF NOT EXISTS annotations (
    id          INTEGER PRIMARY KEY,
    paper_id    INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    route_id    INTEGER REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    -- resume | objectif_etude | pourquoi_ces_donnees | comparaison_branches |
    -- tendance_observee | conclusion_auteurs | limite_reproductibilite
    type        TEXT NOT NULL,
    text        TEXT NOT NULL,
    source      TEXT NOT NULL DEFAULT 'claude',
    quote       TEXT,
    section     TEXT,
    char_start  INTEGER,
    char_end    INTEGER
);

-- Points que l'extracteur n'a pas voulu trancher seul.
CREATE TABLE IF NOT EXISTS doubts (
    id          INTEGER PRIMARY KEY,
    paper_id    INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    location    TEXT,
    issue       TEXT NOT NULL,
    resolution  TEXT,                 -- renseigne par l'orchestrateur
    status      TEXT NOT NULL DEFAULT 'open'   -- open | resolved
);

CREATE TABLE IF NOT EXISTS audit_findings (
    id          INTEGER PRIMARY KEY,
    palier      INTEGER NOT NULL,
    check_type  TEXT NOT NULL,        -- citation | physique | chimie | coherence
    severity    TEXT NOT NULL,        -- bloquant | avertissement | info
    paper_id    INTEGER REFERENCES papers(id) ON DELETE CASCADE,
    route_id    INTEGER,
    target      TEXT,
    description TEXT NOT NULL,
    status      TEXT NOT NULL DEFAULT 'ouvert',   -- ouvert | corrige | accepte
    note        TEXT,
    created_at  TEXT
);

CREATE INDEX IF NOT EXISTS ix_routes_paper  ON synthesis_routes(paper_id);
CREATE INDEX IF NOT EXISTS ix_routes_parent ON synthesis_routes(parent_route_id);
CREATE INDEX IF NOT EXISTS ix_steps_route   ON steps(route_id);
CREATE INDEX IF NOT EXISTS ix_params_step   ON parameters(step_id);
CREATE INDEX IF NOT EXISTS ix_reag_route    ON reagents(route_id);
CREATE INDEX IF NOT EXISTS ix_out_route     ON outcomes(route_id);
CREATE INDEX IF NOT EXISTS ix_var_route     ON route_variations(route_id);

-- Chaine d'ancetres de chaque voie (depth 0 = la voie elle-meme).
CREATE VIEW IF NOT EXISTS v_ancestors AS
WITH RECURSIVE a(route_id, ancestor_id, depth) AS (
    SELECT id, id, 0 FROM synthesis_routes
    UNION ALL
    SELECT a.route_id, r.parent_route_id, a.depth + 1
    FROM a JOIN synthesis_routes r ON r.id = a.ancestor_id
    WHERE r.parent_route_id IS NOT NULL AND a.depth < 20
)
SELECT route_id, ancestor_id, depth FROM a;

-- Ancetre le plus proche qui possede des etapes : source du protocole.
CREATE VIEW IF NOT EXISTS v_step_source AS
SELECT a.route_id, a.ancestor_id AS source_route_id
FROM v_ancestors a
WHERE EXISTS (SELECT 1 FROM steps s WHERE s.route_id = a.ancestor_id)
  AND a.depth = (SELECT MIN(a2.depth) FROM v_ancestors a2
                 WHERE a2.route_id = a.route_id
                   AND EXISTS (SELECT 1 FROM steps s2 WHERE s2.route_id = a2.ancestor_id));

-- Protocole complet reconstitue : etapes heritees + parametres, la valeur
-- d'une variation declaree (la plus proche dans la chaine) remplacant celle du parent.
CREATE VIEW IF NOT EXISTS v_route_complete AS
SELECT
    r.id            AS route_id,
    p.pmcid,
    r.branch_label,
    m.name          AS material,
    r.method,
    s.step_order,
    s.action,
    s.description,
    s.quote         AS step_quote,
    pa.name         AS parameter,
    COALESCE(v.value_num,  pa.value_num)  AS value_num,
    COALESCE(v.value_text, CASE WHEN v.id IS NULL THEN pa.value_text END) AS value_text,
    COALESCE(v.unit, pa.unit)             AS unit,
    COALESCE(v.quote, pa.quote)           AS quote,
    CASE WHEN v.id IS NOT NULL THEN 1 ELSE 0 END AS overridden_by_branch
FROM synthesis_routes r
JOIN papers p            ON p.id = r.paper_id
LEFT JOIN materials m    ON m.id = r.material_id
JOIN v_step_source src   ON src.route_id = r.id
JOIN steps s             ON s.route_id = src.source_route_id
LEFT JOIN parameters pa  ON pa.step_id = s.id
LEFT JOIN route_variations v ON v.id = (
    SELECT rv.id
    FROM route_variations rv
    JOIN v_ancestors a ON a.ancestor_id = rv.route_id AND a.route_id = r.id
    JOIN v_ancestors sa ON sa.route_id = r.id AND sa.ancestor_id = src.source_route_id
    WHERE rv.parameter = pa.name
      AND (rv.step_order IS NULL OR rv.step_order = s.step_order)
      AND a.depth < sa.depth
    ORDER BY a.depth LIMIT 1);

-- Arbre des branches par article.
CREATE VIEW IF NOT EXISTS v_branches AS
SELECT p.pmcid, r.id AS route_id, r.branch_label, pr.branch_label AS parent_label,
       r.is_baseline, r.method, m.name AS material, r.succeeded,
       (SELECT COUNT(*) FROM route_variations v WHERE v.route_id = r.id) AS n_variations,
       (SELECT COUNT(*) FROM outcomes o WHERE o.route_id = r.id)         AS n_outcomes
FROM synthesis_routes r
JOIN papers p ON p.id = r.paper_id
LEFT JOIN synthesis_routes pr ON pr.id = r.parent_route_id
LEFT JOIN materials m ON m.id = r.material_id;

-- Parametre varie <-> resultat obtenu, pour comparer les branches d'un article.
CREATE VIEW IF NOT EXISTS v_comparaison AS
SELECT p.pmcid, pr.branch_label AS parent_label, r.branch_label,
       v.parameter, COALESCE(CAST(v.value_num AS TEXT), v.value_text) AS branch_value,
       v.unit AS variation_unit, v.parent_value,
       o.property, COALESCE(CAST(o.value_num AS TEXT), o.value_text) AS outcome_value,
       o.unit AS outcome_unit, v.quote AS variation_quote, o.quote AS outcome_quote
FROM route_variations v
JOIN synthesis_routes r  ON r.id = v.route_id
JOIN papers p            ON p.id = r.paper_id
LEFT JOIN synthesis_routes pr ON pr.id = r.parent_route_id
LEFT JOIN outcomes o     ON o.route_id = r.id;

-- Architecture v2 (format 3, 28/10/2026) : méthodes d'une voie (vocabulaire contrôlé) et réglages structurés des mesures.
CREATE TABLE IF NOT EXISTS route_methods (
    route_id    INTEGER NOT NULL REFERENCES synthesis_routes(id) ON DELETE CASCADE,
    method      TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS char_settings (
    id                  INTEGER PRIMARY KEY,
    characterization_id INTEGER NOT NULL REFERENCES characterizations(id) ON DELETE CASCADE,
    name        TEXT NOT NULL,       -- réglage du vocabulaire (vocab.py, type reglage)
    value_num   REAL,
    value_text  TEXT,
    unit        TEXT,
    from_figure TEXT,
    quote       TEXT NOT NULL,
    section     TEXT, char_start INTEGER, char_end INTEGER
);
