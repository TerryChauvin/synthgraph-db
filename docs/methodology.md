<p align="center"><b>English</b> · <a href="methodologie.md">Français</a></p>

# Methodology in brief

Short version. The full method, written as a "Materials and Methods" section (in French), is in [README.fr.md](../README.fr.md). Figures as of 17 October 2026; each source is cited.

## 1. The pipeline: four passes (plus automatic check)

| Pass | Who | Instruction file | Output |
|---|---|---|---|
| 1. Extraction | Sonnet agent, `high` effort, one paper each | `RUNBOOK.md` | `extractions/<PMCID>.json`: sample inventory, routes, branches, quotes, `not_stated`, figure readings |
| (check) | script `load.py check` / `load` | — | every quote found verbatim in `corpus/text/`, every number found in its quote; load into `synthese.db` |
| 2. Fidelity critique | Sonnet `high` agent, reads the paper **before** the extraction, no web | `CRITIQUE.md` | `critiques/<PMCID>.json`: findings `faux`, `attribution`, `deduit`, `manquant`, `non_cite_a_tort`, `mineur` |
| 3. Science critique | Opus `high` agent, with web search | `PLAUSIBILITE.md` | `critiques/<PMCID>_science.json`: stoichiometry, physico-chemical plausibility, sources, mechanisms, safety |
| 4. Correction | Sonnet `high` agent, the only one editing the JSON | `PROMPT_CORRECTION.md` | each finding marked `corrige` or `rejete` with a reason |

The orchestrator (Opus) settles doubts, sets decision rules and re-reads against the text. No agent checks its own work. Every 50 papers, `audit.py` writes a report (`audits/palier_NNN.md`) and the orchestrator writes `audits/palier_NNN_relecture.md`.

## 2. Invariants

- **The quote is the proof.** No value without an exact quote; mechanical check at every load.
- **No value inferred or converted on the authors' behalf.** SI conversion is done by `load.py` in a separate column (`value_si`, `unit_si`).
- **Absence is data**: `not_stated`.
- **Authors' inconsistencies are kept**, flagged as `limite_reproductibilite`, never "repaired".
- **Interpretations are separate** (`annotations` table, `source = 'claude'`).
- **A mistake seen twice becomes a rule** in `RUNBOOK.md`.
- Article texts are untrusted data: never executed, no instruction they contain is followed.

## 3. Measured error rates per batch

Source: `audits/palier_00N_relecture.md`. "Full re-read": the orchestrator compares every value of the paper with the text.

| Batch | Routes | Quotes exact at audit | Fidelity findings (median) | of which "faux" | Full re-read: papers / values / wrong |
|---|---|---|---|---|---|
| 1 | 609 | 8,712 (100%) | 526 (10) | 29 | 20 / 1,307 / 10 |
| 2 | 581 | 8,796 (100%) | 403 (8) | 7 | 9 / 776 / 0 |
| 3 | 556 | 10,050 (100%) | 435 (8.5) | 5 | 8 / 981 / 0 |
| 4 | 515 | 9,920 (100%) | 406 (8) | 7 | 5 / 529 / 0 |
| 5 | 466 | 9,581 (100%) | 428 (8) | 4 | 9 / 1,112 / 0 |
| **Total** | **2,727** | **47,059** | **2,198** | **52** | **51 / 4,705 / 10** |

Reading: all 10 wrong values are in the 10 calibration papers of batch 1; each became a rule. No open blocking anomaly in batches 1–5. Since batch 2, none of the "faux" findings re-read is a mis-copied number (see reports 2–5). The "1 error in 3,032 values after calibration" figure in the README covers batches 1–4; batch 5 adds 1,112 values with 0 errors, but this document does not recompute the bound.

Science critique over the whole database on 2026-10-17 (`plausibility` table, 1,581 judgements): 617 `coherente`, 791 `douteuse`, 56 `incoherente`, 117 `inverifiable` (both spellings combined). "douteuse" mostly means reservations; problems come from the papers, not the extractions.

## 4. Token costs

Source: `audits/jetons.csv` (agent tokens, orchestrator excluded): 221 papers, 139 M tokens. Medians per pass: extraction 164 k; fidelity critique 147 k; science critique ≈ 170–176 k (two labels in the file); correction 141 k. Per paper: ≈ 0.9 M in batch 1, 0.61–0.66 M afterwards (batch reports). A 5 h usage window lets ≈ 8–10 M agent tokens through (≈ 13 papers), which paces the work (CLAUDE.md).

## 5. What the method does not guarantee

Faithfulness to the source and explicit gaps, not that a published protocol works. See [limits_and_warnings.md](limits_and_warnings.md).
