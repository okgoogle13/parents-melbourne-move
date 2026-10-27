# Handover: score the 51 passing suburbs

Written 2026-10-27 for another agent. Read this, then the workbook. Do not start from memory or from Archive/.

## Goal
Enter criteria scores (SuburbScorecard columns M–V) for all 51 suburbs whose Hard Filter Status (col L) is a pass, so the weighted score (X) and rank (Y) mean something. No scores exist yet for any suburb.

## Sources (in order)
1. `Our Next Home — Family Relocation Scoring Model.xlsx` (the workbook is the record).
2. `scoring-model-pointer.md` (tab map and status).
3. Do not use: Archive/, the Google Sheet copy (stale, $1.25M budget), or any other copy.

## Scope: the 51 rows
Filter: SuburbScorecard col L = "Active — provisional pass" (26) or "Provisional pass" (25).
Excluded: 8 "Fails: GW drive" rows; 4 "Active — needs data" rows (Blackburn, Glen Waverley, Williamstown, Mount Eliza); 2 test rows (49–50).

Note: pointer.md "Criteria scores" line says 23 passing suburbs. That count is stale; the workbook has 51. Fix the pointer when the workbook is next saved.

Workbook rows (sheet row numbers): 3,4,5,6,8,9,10,11,12,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,31,33,35,36,37,38,39,40,41,42,45,47,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66.

Priority order: start with the 26 "Active — provisional pass" rows (ranks 1–26 by shortlist), then the 25 Watchlist / open-mind rows.

## Scores to enter
Columns M–V, in this order:
- M Near family in GW
- N Nature
- O Hospital (formula fills from K. Do not overwrite.)
- P Indian community
- Q Shops & doctor
- R Village character
- S Train/bus
- T Price
- U Beach
- V City trip

Before scoring, read the Settings tab for the rating scale and any say-in-decision weights. Use that scale only.

## Method
- Data-derived (check from columns before typing): M from J (GW drive), T from G/I (price vs $1.5M cap), S from AB/AC (train Yes/No), V from distance/drive info if present, O from K.
- Judgement (nature, village, beach, shops & doctor, Indian community): estimate and give the basis in col Z. Label each as "estimate" in Z. Keep checked facts and estimates separate.
- Record any new source for a fact in that suburb's row, col Z.
- Do not change columns A–H or L unless the fact is wrong. If you think it is wrong, say so in your report and do not overwrite it.

## Known borderline and weak data (flag, do not fix silently)
- Torquay (88 min) and Wonthaggi (88 min) sit at the GW drive edge. Note this in Z.
- Wonthaggi is 2 minutes under the 90-min cap.
- Weak price evidence: Arthurs Seat (5 sales). Low sales counts: Macedon, Tecoma, Olinda, Sassafras, Mount Dandenong.
- Ferntree Gully and Upper Ferntree Gully share the same AVM ($872,133). Treat as postcode-level.
- Train Yes/No for many rows is from recall and marked "verify". Do not score train as checked unless verified.
- Drive times are midday leave-now estimates; today's times ran about 10% high against a control (Woodend 77 vs 68).

## Rules
- Re-read the workbook immediately before each write, and check its modified time. Only one session edits at a time.
- Never delete. Old versions go to Archive/ with "(superseded YYYY-MM-DD)" in the name before a major change.
- If the folder can't be reached, stop and say so.
- Recalc after writing. Check for formula errors. Expected: no errors; X and Y populate once M–V are filled.

## Done when
- All 51 rows have M–V filled (or an explicit "n/a" with reason in Z).
- Each judgement score has a basis in Z.
- X and Y calculate with 0 formula errors.
- Pointer updated: scores-entered status, the corrected count (51), and the change-log entry.
- Report back: top 10 by X, anything that changes the shortlist, and a list of unverified facts.

## Open items outside this task (do not start here)
- Blackburn, Glen Waverley, Williamstown, Mount Eliza under-$1.5M searches (Claude in Chrome, Tasks 4–5 of "Claude_in_Chrome_prompt — close research gaps.md").
- Train checks for the same rows.
- Family round 2 (Q13 + Q15) answers. Mum has 3 Essentials (cap 2). Weights shift once answers are imported, so re-check X after that.
