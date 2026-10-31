# Project state

Read first. Baseline and next task ID only; open tasks live in the register, `Open work — what runs where (27 Oct 2026).md`. Updated 31 Oct 2026.

## Baseline

- `main` is the baseline. Unmerged `claude/*` branches hold doc-only commits; check `git branch -a --no-merged main` before relying on one.

| File | Version | Status |
|---|---|---|
| `Our Next Home — Family Relocation Scoring Model.xlsx` | Last changed 30 Oct (N2 rounds 5–7 intake: empty structure only; no score, weight, filter or status change); sha256 `29d9e37d…a33bfa` | Approved research baseline (28 Oct). Recalc test verified locally (30 Oct): 0 errors, 51 ranked rows. Currently stores no cached formula values |
| `Our Next Home — parent report (28 Oct 2026).html` | Rebuilt 29 Oct from workbook `5704d65` | Draft: requires family review; not for publication or distribution |
| `Suburb shortlist foundation report.md` / `.pdf` | Updated 29 Oct to workbook `5704d65` (Glen Waverley price only) | Awaiting human review |

Status counts, ranks and the change history are in `scoring-model-pointer.md`.

## Next task

P9: family answers on survey code version 14 (round 8 trade-offs survey, built 31 Oct; see `Questionnaire redesign — round 8 (31 Oct 2026).md`). **Published 31 Oct to the existing artifact URL; link not yet sent.** Republished 31 Oct after review: R8.6 bushfire question (B/C only), Q12 and card B/E wording. Awaiting the user's review of v14. Bushfire screening, the model spec and any weight, filter, status or voting change each need separate approval. Answers arrive by WhatsApp and are imported through the page's owner panel. N3 import must add RawResponses columns for Q3c and the R8 items (listed in the round 8 record). Bushfire screening B3-S done 31 Oct (see below). **Wait-period outputs (31 Oct, local, no workbook change; sha still `29d9e37d508c`):** N3 import prep `tools/import_v14.py` (tested on temp copies; usage in `docs/workflow.md`); card facts `research/card-facts-check (31 Oct 2026).md`; bushfire screening B3-S done, `research/bushfire/` (Estimate, proposed thresholds). Bushfire wording (cards B/C, R8.6 opener) republished 31 Oct, user-approved (live version 1793421274-e848). Pending approvals: context-column flag, bushfire thresholds and display-only column spec, proposed AD/Z/AC cell edits. After the survey: a separate model spec (assumptions, sensitivity tests, impact on the top 10 and excluded suburbs) before any weight, filter, status or voting change. G3 (M/O decoupling, Settings B38/B39 = 90) needs the user's approval. P4 order still the user's decision.
