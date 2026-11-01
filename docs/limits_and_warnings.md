<p align="center"><b>English</b> · <a href="limites_et_avertissements.md">Français</a></p>

# Limits and warnings

Figures as of 17 October 2026. Read before reproducing a synthesis from the database.

## 1. What the database guarantees, and what it does not

It guarantees that every value points to a quote found verbatim in the paper's text (47,059 quotes checked at the audits of batches 1–5, 100% exact), and it makes explicit what the paper does not say. It does **not** guarantee that a published protocol works, nor that the paper is right.

## 2. What a chemist should not believe without checking

- **Missing supplementary files.** Supporting Information is included only when `enrich.py` could retrieve it; the source files are not in the repository (`corpus/si/` is git-ignored, only their text is appended to `corpus/text/`). When a paper refers to a missing supplement, a `limite_reproductibilite` annotation starts with "Annexe absente du dépôt :": 78 such annotations, over 77 papers. An incomplete route keeps a low completeness score.
- **Papers' contradictions kept literally.** A strange or inconsistent value (a cobalt content heavier than pure cobalt, a "HeNe laser at 532 nm"…) is kept as written and flagged as `limite_reproductibilite`; it is never corrected. The science critique judged 1,581 routes: 617 consistent, 791 doubtful, 56 inconsistent, 117 unverifiable (`plausibility`). These problems come from the papers.
- **Mechanisms are hypotheses.** `mecanisme_analyse` annotations (476) are Claude's analyses, with web search; `mecanisme_auteurs` (434) reports what the authors propose, often undemonstrated too. Neither is a result of the database.
- **Safety.** `securite_analyse` annotations (350) are hazard reminders added by the analysis, not instructions validated by a safety officer. Papers often omit such precautions (`securite_auteurs`: only 39).
- **Values read off figures** (`from_figure`): approximate, 2 significant figures at most.
- **Branches describe differences only.** Parameters not redefined come from the parent route: use `v_route_complete`.
- **Unverified DOIs and sources.** Science critiques cite sources; the Crossref API is blocked from the cloud. 575 DOIs remain to be checked from a machine that can reach it: `audits/palier_002_doi_a_verifier.txt` (144), `palier_003` (123), `palier_004` (132), `palier_005` (176); in batch 1, 8 of 10 randomly drawn DOIs were confirmed by Crossref (`audits/palier_001_relecture.md`). Meanwhile every bibliographic link in a science critique is "to be checked". An invented source would be a blocking audit anomaly; two to three sources per batch were opened by hand and matched.
- **14 open doubts** (`doubts.status = 'open'`) and batch-6 papers still being critiqued (2 without critique on 2026-10-17): their sheets may change. Only batches 1–5 (250 papers) are audited.
- **Coverage.** 270 papers extracted out of a target of 500; 12 papers rejected at extraction (no usable synthesis). The database does not represent the whole literature.

## 3. Licences: open question

The papers are open access under Creative Commons licences, some NC (non-commercial) or ND (no derivatives). Of the 270 extracted papers: 191 CC BY, 49 CC BY-NC, 29 CC BY-NC-ND, 1 CC BY-NC-SA.

The repository also contains `corpus/` (≈ 368 MB, versioned: `text/`, `xml/`, `refs/`, `fig/`): flattened full texts, original XML, references and figures. These files stay under each paper's licence. Republishing them in a public repository raises two questions:

- **ND** texts were transformed (flattened, supplements appended); depending on the reading of the licence, a distributed adaptation is not permitted;
- **NC** texts cannot be redistributed in a commercial setting.

The quotes kept in the database are short excerpts (quotation use); `fiches/` and `synthese_dump.sql` reuse them.

**Proposal (not decided):** remove `corpus/` from the public repository (add `corpus/` to `.gitignore`, keep it locally or in a private repository) and provide a script that rebuilds it from Europe PMC (`fetch.py`, `sections.py`, `enrich.py`) from the PMCIDs. Trade-off: quote character positions depend on the flattened text, so the rebuild must be deterministic, and `load.py` could no longer check quotes without it. The other option is to keep only CC BY papers public. This decision belongs to the user; it is not taken here. This note is not legal advice.
