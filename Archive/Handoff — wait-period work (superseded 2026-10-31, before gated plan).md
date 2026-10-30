# Handoff — wait-period work (31 Oct 2026)

For: a Claude Code session in VS Code, on the local Mac repo (`/Users/okgoogle13/Projects/Parents Melbourne MOVE/`).
From: the claude.ai session that built and published questionnaire v14 (31 Oct 2026).
User's choice: **Option B**, given 31 Oct 2026. Run it while Mum and Dad fill in the survey.

## Kickoff prompt (paste into Claude Code)

> Read `CLAUDE.md`, `PROJECT_STATE.md`, then `Handoffs/Handoff — wait-period work (31 Oct 2026).md`. Do tasks T0–T5 in order. The approvals listed in that file are mine (31 Oct 2026); anything not listed still needs my approval. Do not push. Stop and ask if a stop condition in the file is hit. Finish with the short report described in T5.

---

## Approvals given (31 Oct 2026) and limits

Approved:
- **T1** One local commit of the uncommitted work listed below (the claude.ai session was told not to commit). **No push.**
- **T2** Prepare the workbook import for v14 answers (task N3), **on a temporary copy only**.
- **T3** Fact checks behind the v14 area cards (open tasks C4/C5, narrowed). Research note only.
- **T4** Bushfire screening, task **B3-S** (25 suburbs). Research outputs only.

Still needs separate approval (do not do):
- Any edit to the canonical workbook `Our Next Home — Family Relocation Scoring Model.xlsx`, including new columns, col Z notes and the N3 import itself.
- Weights, Filters, shortlist status (C), hard filter status (L), score P, the Mum/Dad/Nish voting, the model spec.
- Republishing the questionnaire page or sending its link (only the claude.ai session can publish it).
- `git push`.

Permanent rules from `CLAUDE.md` apply: archive, never delete; Excel-compatible formulas only; no Google Drive/Sheets/Docs/Forms; label every value Checked / Estimate / Needs verification / Needs data / N/A; never invent a figure.

## Baseline (check in T0)

| Item | Expected |
|---|---|
| Branch / last commit | `main` @ `17f003a` |
| Workbook sha256 prefix | `29d9e37d508c` (unchanged since 30 Oct) |
| Page source sha256 prefix | `5e43c79c8eff` = live artifact version `1793385715-e1ca` (published 31 Oct) |
| Survey | code version 14; R8.6 bushfire question added 31 Oct; link not sent |

Uncommitted work at handoff (from `git status`, 31 Oct):
- Modified: `Our Next Home — questionnaire page (Claude artifact source).html`, `PROJECT_STATE.md`, `Questionnaire redesign — round 8 (31 Oct 2026).md`, `scoring-model-pointer.md`
- New: `Archive/Our Next Home — questionnaire page (superseded 2026-10-31, before exported-artifact version).html`, `Archive/Our Next Home — questionnaire page (superseded 2026-10-31, v14 before bushfire question).html`, `Archive/PROJECT_STATE (superseded 2026-10-31, before bushfire question).md`, `Archive/Questionnaire redesign — round 8 (superseded 2026-10-31, before bushfire question).md`, `Archive/scoring-model-pointer (superseded 2026-10-31, before bushfire question).md`
- New (this handoff): `Handoffs/Handoff — wait-period work (31 Oct 2026).md`, `Handoffs/data/questionnaire-responses-export-2026-10-31.json`
- **Do not commit** `.claude/settings.local.json` (local settings).

## Stop conditions

Stop and report (don't work around) if:
- The workbook or page sha differs from the baseline, or `git status` shows changes not listed above.
- A task would need any of the "still needs approval" items.
- A source is blocked or needs a sign-in. Record it as Needs verification, say which source, and move on. Don't use mirrors or caches to get around a block.

---

## T0 — Pre-flight

1. `git status`, `git log -1`, sha256 of the workbook and page source; compare with the baseline.
2. Read `docs/workflow.md` (recalc test, column map), the round 8 design note (`Questionnaire redesign — round 8 (31 Oct 2026).md`: stored values, N3 column list, B3-S gate, weak points) and the Storage rule in `Questionnaire redesign — rounds 5–7 (29 Oct 2026).md`.

## T1 — Local commit (approved; no push)

Stage exactly the files listed under "Uncommitted work" (excluding `.claude/settings.local.json`). Suggested message:

```
Questionnaire v14 after review: R8.6 bushfire question, Q12 and card B/E wording; handoff for wait-period work

- R8.6 asked only if R8.4 is B or C, else stored X; feeds nothing
- Q12 B drops "and station"; card B drops Angliss caveat (24-hr ED confirmed); card E notes the smaller hospital
- Live artifact version 1793385715-e1ca = page source sha 5e43c79c8eff; workbook unchanged
- Responses export (17 records) for N3 import prep
```

## T2 — N3 import prep, on a temporary copy only

Goal: when Mum and Dad answer, importing is one checked step. Build and test now; **do not write to the canonical workbook.**

Input: `Handoffs/data/questionnaire-responses-export-2026-10-31.json`. It's an export of the page's `responses` collection: 17 records. 15 are 27 Oct proxy rounds (already in RawResponses rows 3–15). One is a **v10 test** by the user (`id nwug61z2s5z001smvcwy`, "Mum", 30 Oct 10:50 UTC); exclude it. One is **Nish's real v14 answers** (`id mj7crn0qy5hf52p9pqsb`, person "Me", 30 Oct 15:59 UTC, 39 answers). The page's database is only reachable from claude.ai, so later answers will arrive as a fresh export in the same format.

Build `tools/import_v14.py` (run with `.venv/bin/python`):
- Select records with `pageVersion == 14` and person in Mum / Dad / Me. Ignore TEST and every other version. If a person has several v14 records, use the latest `savedAt` and list the others in the output.
- **R8.6 backfill:** records saved before the 31 Oct republish have no R8.6. If R8.4 is A, D or E, store `X — Not asked (most-wanted area wasn't B or C)`. If R8.4 is B or C, leave it blank and flag "Needs data: answered before R8.6 existed". Nish: R8.4 = E, so X.
- **New RawResponses columns:** check row-1 headers first (N2 ended at BE `[R6 Notes]`; confirm). Append, in this order, any not already present: Q3c, R8.1, R8.2, R8.3-30, R8.3-20, R8.3-45, R8.3-60, R8.3-75, R8.3, R8.3c, R8.4, R8.5, R8.6. Use the existing header style.
- **CleanedAnswers:** add per-question lookup rows for the new columns, following the N2 pattern (rows 41–57). Widen the latest-row formula range to the new last column. Excel-compatible only.
- **Value format:** match the existing rows. Q15.1–Q15.10 are stored as the **bare letter** (A–D), as in rows 9–15; CleanedAnswers C2:C4 counts an exact "D". Q11–Q13 keep the full option text (ForcedChoiceCorrections reads "A —"/"B —"). For everything else, check what rows 9–15 hold and match it.
- **Row rule:** one new RawResponses row per person per imported v14 record.
  - **Q10 and Q13d stay blank** (round 8 note: not asked in v14; the Q10 correction is a model-spec item).
  - Context columns the v14 page no longer asks (e.g. Q1, Q2, Q8, Q9, Q13b, Q13c, R5.1, R5.3, R6.7): list them. Implement both "blank" and "carry forward from the person's latest row" behind a flag, default **blank**. Show in the report which DiscussionSummary/CleanedAnswers cells each choice affects. The user decides.
- Notes fields: keep the text; the page flattens newlines to " / " only in WhatsApp messages.

Test (all in a temp directory, never the repo copy):
1. Run the import on a temp copy with Nish's record only. Recalc per `docs/workflow.md`. Expect 0 formula errors. Every pre-existing cell's formula/value string should be identical except the new headers, new rows and widened ranges (diff and list them). Nish's new row should match the export field by field.
2. Add synthetic Mum/Dad records, marked synthetic and kept out of the repo: one with R8.4 = B (R8.6 answered); one pre-R8.6 with R8.4 = C (blank + flag); ladder capped and uncapped; 2 Top priorities. Check the outputs.
3. Re-hash the canonical workbook at the end: still `29d9e37d508c`.
4. **Do not present weights, scores, ranks or a "would pass" count from the dry runs.** Report only that the recalc works and the diff is clean.

Deliverables: `tools/import_v14.py`; a usage paragraph in `docs/workflow.md`; the test results in the T5 report.

## T3 — Card fact checks (research note only)

The v14 area cards (round 8 note, "Area cards") show ranges from the workbook. Known weak points:

1. **Card C hospital basis.** For each card C suburb (Healesville, Yarra Glen, Warburton, Macedon, Woodend, Gisborne, Riddells Creek, Kyneton): what's the nearest **public hospital emergency department open 24 hours**? That excludes urgent-care centres; it's the R5.4 definition. Is the workbook's K hospital the right one? (Macedon Ranges times currently use Bendigo, not confirmed as nearest.) Use health service and healthdirect pages, citing URL and date. Only take drive minutes from Google Maps ("Depart at" 10:00 weekday, top of range) if you can reach it. Otherwise give the hospital only and mark the minutes Needs verification.
2. **Train Yes/No marked "recall" or "verify"** in AB/AC for the 38 card suburbs. Check them against PTV, V/Line or Wikipedia station pages.
3. **Angliss Hospital:** the Eastern Health site states "Emergency department 24 hours a day, 7 days a week" (read 31 Oct 2026, https://www.easternhealth.org.au/locations/eastern-health-angliss/). Workbook notes on SuburbScorecard rows 6, 23, 24 and 33 still say "verify". Draft replacement text.

Output: `research/card-facts-check (31 Oct 2026).md`. One row per finding: suburb, workbook cell, current value, finding, label, source and date, proposed cell edit. Then a closing section on whether any **card range on the page** would change. If one would, give proposed card wording (no suburb names on cards). The page itself is republished from claude.ai, not here.

## T4 — Bushfire screening B3-S (approved; research outputs only)

Scope (from the round 8 note), 25 suburbs:
- Card B (12): Upper Ferntree Gully, Upwey, The Basin, Tecoma, Belgrave, Montrose, Warrandyte, Mount Evelyn, Sassafras, Mount Dandenong, Olinda, Emerald
- Card C (8): Healesville, Yarra Glen, Warburton, Macedon, Woodend, Gisborne, Riddells Creek, Kyneton
- Plus (5): Eltham, Hurstbridge, McCrae, Mount Martha, Arthurs Seat

For each suburb record:
- Bushfire Prone Area: Yes / Partly / No
- Bushfire Management Overlay: most residential streets / edges only / none
- Method, source, dataset date, read date; "Needs data" until checked

Preferred method: DataVic / Vicmap layers for the Bushfire Prone Area and the planning-scheme BMO, intersected with ABS 2021 suburb (SAL) boundaries. Measure the share of **residentially zoned land** in each layer, not total suburb area, because national park would swamp the figures (Vicmap Planning zones). Propose thresholds and state them, e.g. BMO "most residential streets" ≥ 50% of residential land, "edges only" > 0 and < 50%, "none" = 0. Flag them as proposals for the user. Keep downloaded datasets **out of git** (record URL, date and sha256 instead). Fallback if the GIS route fails: VicPlan property reports for 2–3 sample addresses per suburb (town centre plus edge), labelled Estimate with the addresses listed.

This is **not a filter**. Change no status, score, rank or card. Deliverables:
- `research/bushfire/bushfire-screening (31 Oct 2026).md` (method, thresholds, table, caveats) and `.csv` (one row per suburb)
- A proposed workbook column spec (headers, allowed values, display-only, feeds nothing) for separate approval
- One line on whether the cards' "Parts are bushfire-prone (early check, still being confirmed)" still fits, with proposed wording if not
- Context: R8.6 answers (bushfire tolerance, B/C pickers only) will be read against this table. Nish wasn't asked (R8.4 = E).

## T5 — Close-out

1. Register (`Open work — what runs where (27 Oct 2026).md`): add or mark rows for N3 prep, card facts (C4/C5 narrowed), B3-S, with status and output paths.
2. `PROJECT_STATE.md`: next task stays P9 (waiting on Mum and Dad); note the outputs. Archive both files first per the rules.
3. Second local commit for T2–T5 outputs. **No push.**
4. Report to the user, short:
   - what was done;
   - T2 test results (errors, diff, sha check);
   - T3 findings that would change a card or a workbook cell;
   - the B3-S table summary;
   - every decision now waiting on the user: context-column flag, bushfire thresholds, workbook column spec, proposed cell edits, any card wording.
