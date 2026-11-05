# Project state

Read first. Baseline and next task ID only; open tasks live in the register, `Open work — what runs where (27 Oct 2026).md`. Updated 5 Nov 2026.

## Baseline

- `main` is the baseline. Unmerged `claude/*` branches hold doc-only commits; check `git branch -a --no-merged main` before relying on one.

| File | Version | Status |
|---|---|---|
| `Our Next Home — Family Relocation Scoring Model.xlsx` | Last changed 5 Nov (Nish's v16 answers imported; scores unchanged); sha `841c84acf860`. Scoring change 2 Nov (grocery filter 25 min, beach drive times, P = option B, U = beach drive, family-set weights, beach bands in Filters A15:C21) | Approved research baseline (28 Oct). Recalc test verified 5 Nov: 0 errors, 37 ranked rows. Currently stores no cached formula values |
| `Our Next Home — parent report v3 (29 Oct 2026).html` | Rebuilt 5 Nov from workbook sha `841c84acf860` by `tools/report2.py` (G7); previous copy in Archive | Draft: requires family review; not for publication or distribution |
| `Suburb shortlist foundation report.md` / `.pdf` | Numbers only refreshed 5 Nov from workbook sha `841c84acf860` (G7; narrative not edited, NEEDS REVIEW comments in the .md); previous copies in Archive | Awaiting human review |

Status counts, ranks and the change history are in `scoring-model-pointer.md`.

## Next task

**5 Nov 2026 (G7 done, PR open; awaiting the user):** parent report and foundation report rebuilt from the recalculated workbook (sha `841c84acf860`, 0 errors, 37 ranked) after the 2 Nov scoring change. `tools/report2.py` is fixed (unranked rows listed after ranked ones as "not ranked", counts derived from the workbook); `tools/found.py` was not fixed (targets the old 51-rank format), so the foundation report was refreshed by a one-off numbers script. Both reports stay Draft and need family review; nothing is distributed. Sentences the new numbers contradict are left unedited and flagged "NEEDS REVIEW" (list in the PR). Next: the user reviews the PR; narrative rewrite of the foundation report (weights section, executive summary) needs the user's approval.

Carried forward. Scoring (2 Nov, user-approved): grocery filter 25 min applied (15/30 backups shown), beach drive times added, P = option B, U = beach drive, family-set weights (5 priorities at 15%, Nature 10%, Price 1%, City 4%, rest 5%), beach full marks within 15 min (stepped bands Filters A15:C21). Survey (v16, live version 1793528975-9715, same URL): **link not yet sent**; Nish's v16 answers imported 5 Nov; Mum and Dad not submitted; survey answers no longer feed weights, so decide whether the survey priority questions are still needed. Import script `tools/import_v14.py` takes v14–v16 (usage in `docs/workflow.md`). Parents' 1 Nov WhatsApp house criteria go to the property search (B5), not the survey. Research gap: insurance/running costs for card B/C suburbs.

P9: family answers on survey code version 14 (round 8, `Questionnaire redesign — round 8 (31 Oct 2026).md`; later short survey v16: `Questionnaire redesign — round 9 short survey (1 Nov 2026).md`). Answers arrive by WhatsApp and are imported through the page's owner panel. N3 import must add RawResponses columns for Q3c and the R8 items. Bushfire screening B3-S done 31 Oct (`research/bushfire/`, Estimate, proposed thresholds); card facts `research/card-facts-check (31 Oct 2026).md`. Pending approvals: context-column flag, bushfire thresholds and display-only column spec, proposed AD/Z/AC cell edits. After the survey: a separate model spec (assumptions, sensitivity tests, impact on the top 10 and excluded suburbs) before any weight, filter, status or voting change. G3 (M/O decoupling, Settings B38/B39 = 90) needs the user's approval. P4 order still the user's decision.
