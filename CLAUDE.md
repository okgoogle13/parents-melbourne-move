# CLAUDE.md

Research record for choosing a suburb in or around Melbourne for the user's parents (the user lives with them). Not software. `main` is the baseline; `PROJECT_STATE.md` records when it was last verified against the local Mac folder.

## Read on demand
- Always: `PROJECT_STATE.md` (baseline, next task ID).
- Open tasks, owners, blockers: `Open work — what runs where (27 Oct 2026).md` (the only task register).
- Research, reports, scoring or interpreting results: `PROJECT_INSTRUCTIONS.md` (the family brief; overrides this file).
- Editing the workbook, column map, recalc test, research blockers: `docs/workflow.md`.
- Status counts, ranks, change log: `scoring-model-pointer.md`.
- `reference/`: background only; read when asked.

## Sources (when they disagree)
1. `Our Next Home — Family Relocation Scoring Model.xlsx`: canonical for suburbs, scores, weights, filters, budget, responses. **Filters** tab = family decision record.
2. `scoring-model-pointer.md`.
3. Other root files. Reports are built from the workbook at a named commit and lag it.
4. `Archive/`: never a source unless asked.

Answer suburb, score, filter and response questions from the workbook, not memory or reports. Read only the tabs/ranges needed; never dump whole sheets. Currently the file stores no cached formula values, so computed cells (I, M, O, T, X, Y) read as `None`; take them from a recalculated temp copy.

## Permanent rules
- No Google Drive, Sheets, Docs or Forms, even if connectors exist. Approved Google Maps drive-time research is fine.
- Archive, never delete: copy to `Archive/` as `(superseded YYYY-MM-DD, before <change>)`, then edit the root file in place. No near-duplicates in root.
- One session edits the workbook at a time. Re-read it just before writing; run the recalc test after.
- Excel-compatible only: no `XMATCH`, `REGEXEXTRACT`, `ARRAYFORMULA`.

## Needs the user's explicit approval
- Weights (PriorityWeights, ForcedChoiceCorrections), the Filters tab, the definition of score P.
- SuburbScorecard C (shortlist status) and L (hard filter status); adding or removing locations. Check row-1 headers before writing.
- Substantive report changes (findings, numbers, recommendations) and any publication or distribution. Routine formatting within approved scope doesn't need it.

Display-only, never feeding X, Y or any weight: AX (community band), Q13d, Community comparator rows, ABS demography (AK–AW).

## Evidence
- Source every researched fact in SuburbScorecard col Z (plus AC, AE–AJ where relevant).
- Label values **Checked**, **Estimate**, **Needs verification**, **Needs data** or **N/A**, in the workbook and in answers.
- Judgement scores (N, P–S, U, V) change only with a cited source, logged in Z. A source supports a judgement; it doesn't make it Checked.
- State the basis of each drive time ("10:00 weekday, top of range") and price (OnTheHouse AVM ≠ sale median).

## Closing and compaction
- When a task is finished: mark it in the register, then set the next task ID in `PROJECT_STATE.md`.
- On compaction keep: task, branch, canonical file commits, changed files, approvals given, blockers, next action. Drop superseded plans, logs and file dumps.
