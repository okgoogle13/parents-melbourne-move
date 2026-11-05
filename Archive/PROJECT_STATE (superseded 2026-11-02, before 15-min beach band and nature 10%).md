# Project state

Read first. Baseline and next task ID only; open tasks live in the register, `Open work — what runs where (27 Oct 2026).md`. Updated 31 Oct 2026.

## Baseline

- `main` is the baseline. Unmerged `claude/*` branches hold doc-only commits; check `git branch -a --no-merged main` before relying on one.

| File | Version | Status |
|---|---|---|
| `Our Next Home — Family Relocation Scoring Model.xlsx` | Last changed 30 Oct (N2 rounds 5–7 intake: empty structure only; no score, weight, filter or status change); sha256 `29d9e37d…a33bfa`; 31 Oct parents-only validation fix (CleanedAnswers B71:D71, E64:E66), sha `1a16d34de6f2` | Approved research baseline (28 Oct). Recalc test verified locally (30 Oct): 0 errors, 51 ranked rows. Currently stores no cached formula values |
| `Our Next Home — parent report v3 (29 Oct 2026).html` | Rebuilt 29 Oct from workbook `5704d65` | Draft: requires family review; not for publication or distribution |
| `Suburb shortlist foundation report.md` / `.pdf` | Updated 29 Oct to workbook `5704d65` (Glen Waverley price only) | Awaiting human review |

Status counts, ranks and the change history are in `scoring-model-pointer.md`.

## Next task

**2 Nov (beach bands):** U uses stepped bands in Filters A15:C21 (10/20/30/45/60 min → 10/8/6/4/2, over 60 → 0). Workbook sha `25c6e9659d24`; recalc 0 errors, 37 ranked.

**2 Nov (latest, scoring change):** grocery filter 25 min applied (15/30 backups shown), beach drive times added, P = option B, U = beach drive, family-set weights (5 priorities at 15%, rest 5%). 37 ranked; workbook sha `73d9c412903d`. Next: parent report and foundation report are now out of date (rebuild with tools/report2.py on a recalculated copy, needs approval to distribute); survey (v16) answers no longer feed weights; decide whether the survey priority questions are still needed.

**2 Nov (latest):** AY (drive to nearest Indian grocery, 10:00 top of range) filled for 51 ranked rows; workbook sha `1794f0841640`; recalc 0 errors, 51 ranked. Next: user picks a grocery-drive limit for the Filters tab (approval needed), then apply and recalc. Then P9 survey answers and the model spec (option 1).

**1 Nov (latest):** survey is now v16, a short version (about 5–8 minutes; see `Questionnaire redesign — round 9 short survey (1 Nov 2026).md`), live version 1793528975-9715, same URL; **link not yet sent**. Import script takes v14–v16 (tested on a temp copy). Next: user reviews v16 and sends the link (P9); then N3 import (needs approval). Parents' 1 Nov WhatsApp house criteria go to the property search (B5), not the survey.

**31 Oct (latest):** survey page is v15 (Timing part, dark look, review wording fixes), live version 1793424601-d805; link still not sent. Import script now takes v14 and v15 (`tools/import_v14.py`, tested 31 Oct on temp copies: recalc 0 errors, 51 ranked). CleanedAnswers parents-only fix done 31 Oct (B71:D71, E64:E66; workbook sha `1a16d34de6f2`). Research gap: insurance/running costs for card B/C suburbs.

P9: family answers on survey code version 14 (round 8 trade-offs survey, built 31 Oct; see `Questionnaire redesign — round 8 (31 Oct 2026).md`). **Published 31 Oct to the existing artifact URL; link not yet sent.** Republished 31 Oct after review: R8.6 bushfire question (B/C only), Q12 and card B/E wording. Awaiting the user's review of v14. Bushfire screening, the model spec and any weight, filter, status or voting change each need separate approval. Answers arrive by WhatsApp and are imported through the page's owner panel. N3 import must add RawResponses columns for Q3c and the R8 items (listed in the round 8 record). Bushfire screening B3-S done 31 Oct (see below). **Wait-period outputs (31 Oct, local, no workbook change; sha still `29d9e37d508c`):** N3 import prep `tools/import_v14.py` (tested on temp copies; usage in `docs/workflow.md`); card facts `research/card-facts-check (31 Oct 2026).md`; bushfire screening B3-S done, `research/bushfire/` (Estimate, proposed thresholds). Bushfire wording (cards B/C, R8.6 opener) republished 31 Oct, user-approved (live version 1793421274-e848). Pending approvals: context-column flag, bushfire thresholds and display-only column spec, proposed AD/Z/AC cell edits. After the survey: a separate model spec (assumptions, sensitivity tests, impact on the top 10 and excluded suburbs) before any weight, filter, status or voting change. G3 (M/O decoupling, Settings B38/B39 = 90) needs the user's approval. P4 order still the user's decision.
