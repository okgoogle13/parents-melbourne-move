# Handoff — IDE start (10 Nov 2026)

Status review for moving work into Claude Code in the IDE. Read with `PROJECT_STATE.md` and the task register. Nothing in the project was changed by this review.

## Repo state (checked 10 Nov)
- `main` = `origin/main`, last commit `536e29a` (6 Nov). Only untracked file: `.claude/settings.local.json`.
- Workbook sha256 matches `841c84acf860` (PROJECT_STATE baseline). 37 ranked rows at last recalc (5 Nov, 0 errors).
- Unmerged: `claude/claude-md-fixes` and `claude/ecstatic-tesla-pzbg1v` hold the same single commit `2ef2157` (fixes the broken PDF-tool bullet in CLAUDE.md; ignores `__pycache__`).
- **`.venv` is broken:** `.venv/bin` has no `python`, so every `tools/` command fails. Fix: `uv sync` from the repo root.
- `tools/found.py` still broken on the current foundation-report format.

## Done since 2 Nov
- 2 Nov: scoring change (user-approved): grocery filter 25 min, beach drive times + stepped bands, P = option B, U = beach drive, family-set weights (Nature 10%, Price 1%, City 4%). Indian-grocery drives (AY) for all 51 rows.
- 5 Nov: survey v18 published (same URL, wording only). Nish's v16 answers imported (scores unchanged). Temple/church questions dropped (D4). Diversity ideas parked (K1). Indian-restaurant pilot prompt written (B10).
- 6 Nov: **survey complete — all three v18 responses saved** in the survey database (artifact `9fbNBMzhdedGaYwQg3pnGo`, collection `responses`): Mum and Dad (WhatsApp import, 24 answers each), Me (page, 25 answers). Duplicate "Me" records removed. **Not yet imported into the workbook** (RawResponses still ends at row 16, Nish's v16). Exported 10 Nov to `Handoffs/data/questionnaire-responses-export-2026-11-10.json` (all 21 records); test import on a temp copy passed (exit 0; Mum row 17, Dad row 18, Me row 19, new cols CB–CH, CleanedAnswers 97–103).
- 6 Nov: read-only check of parents' answers: **both Mum and Dad stated a 25-min max drive to Glen Waverley**, versus the 90-min hard cap in Filters. With 25-min GW + hospital + grocery limits, 16 of 37 ranked suburbs survive. Mum and Dad differ on nature, price, beach and living-space separation. Current weights (Beach and Indian community 15%, Price 1%) look closer to Nish's priorities than the parents' stated ones — worth a direct conversation. Options offered; recommended a display-only "parents' limits" view before changing filters. **Decision pending.**
- 6 Nov: G7 — parent report v3 and foundation report rebuilt from workbook `841c84acf860`, merged to main. Both still Draft, not distributed.

## Stale or inconsistent records
- PROJECT_STATE and register (P9) still say the survey link was never sent — wrong since 6 Nov.
- Register "Now" line dates from 30 Oct; G7 row still says "awaiting review" though merged; ID B9 used twice.
- Register "Cloud session" section: promo credit ended 4 Nov.
- M2 was due before 3 Nov; M4 (RBA re-check after 3 Nov) is now overdue — macro data likely `review_due`.

## Time-sensitive
- 5 Northam St, Glen Waverley auction: **Sat 14 Nov, 11:00 am.**
- Parents overseas mid-Nov 2026 to mid-Feb 2027: any follow-up questions to them in person need to happen this week.

## Next steps (in order)
1. **Housekeeping (IDE):** `uv sync`; run `tools/validate_macro.py` and the recalc test (`docs/workflow.md`); merge one CLAUDE.md branch, delete both; update PROJECT_STATE, register "Now", P9 (done 6 Nov), G7, cloud note.
2. **User decision: the 25-min vs 90-min conflict.** How to treat the parents' 25-min Glen Waverley limit (display-only "parents' limits" view first, or change Filters B4/B5 — G2, needs approval; G3 comes before G2).
3. **N3 import of Mum's, Dad's and Nish's v18 records** with `tools/import_v14.py` (accepts v18), input `Handoffs/data/questionnaire-responses-export-2026-11-10.json`. First fix CleanedAnswers B71:C71 to check R6.1 only. One workbook session at a time; recalc after.
4. **Then:** N4, G5 (property thresholds), the model spec (community split from C1–C4 answers, highest rating as overall signal; community weight set after responses), G4 status changes, regenerate reports (G7 again).
5. **Before 14 Nov (if wanted):** M4 macro refresh from a named source, or mark review_due.
6. **Chrome tasks:** B10 Indian restaurant pilot, B1, B2, B4 remainder.
7. **Other approvals pending:** M1–M3 and M5, bushfire thresholds + display-only column, AD/Z/AC edits, P4 review order, P6 Point Cook, B11 new columns.
