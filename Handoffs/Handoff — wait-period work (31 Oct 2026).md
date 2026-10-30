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
- New (this handoff): `Handoffs/Handoff — wait-period work (31 Oct 2026).md`, `Handoffs/data/questionnaire-responses-export-2026-10-31.json`, `tools/questionnaire_tests/` (README plus three Playwright scripts used to test page v14; see its README)
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
- **Row rule:** one new RawResponses row per person per imported v14 record. Follow the documented Storage rule (rounds 5–7 design doc §3): the new row = the person's latest row (15 Mum, 13 Dad, 14 Me) carried forward, overwritten by the v14 answers, with a merge log entry in AM ("v14 <timestamp> merged onto row N").
  - **Exception: Q10 and Q13d are blanked** on the new row (round 8 note: not asked in v14, "columns stay, empty for v14"; the Q10 correction is a model-spec item). Today Q10 moves no weight (no transfer), so blanking shouldn't change the weights by itself; confirm this on the temp copy.
  - Context columns the v14 page no longer asks (e.g. Q1, Q2, Q8, Q9, Q13b, Q13c, Q10–Q13 notes) keep the carried-forward proxy values by default. List them and add a flag to blank them instead. Show in the report which DiscussionSummary/CleanedAnswers cells each choice affects. The user decides.
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
4. Confirm that nothing from the gated plan below was executed.
5. Report to the user, short:
   - what was done;
   - T2 test results (errors, diff, sha check);
   - T3 findings that would change a card or a workbook cell;
   - the B3-S table summary;
   - every decision now waiting on the user: context-column flag, bushfire thresholds, workbook column spec, proposed cell edits, any card wording.

---

# Gated plan: from real answers to a decision (planning only)

Step IDs here (A0–H2) are plan steps, not register task IDs. Register tasks are named as such (e.g. "register task B1").

**Nothing in this part runs during T0–T5.** It maps every step that changes the real workbook, the model, the filters, the shortlist, the voting, the page or the remote, so each one can be approved on its own. Each gate below = one explicit approval from the user. Steps can share a gate only when they're listed together.

## Standard procedure for every gated workbook step

1. Re-read the workbook and confirm its sha matches the last logged commit. One session edits it at a time.
2. Archive a pre-change copy: `Archive/… (superseded YYYY-MM-DD, before <change>)`.
3. Make the change. Excel-compatible formulas only; check row-1 headers before writing.
4. Run the recalc test (`docs/workflow.md`): 0 errors. Diff every pre-existing cell; the only changes allowed are the approved ones.
5. Log in the `scoring-model-pointer.md` change log: what changed, cells, recalc result, sha. Update the register and `PROJECT_STATE.md`.
6. Local commit (one per gate). Push is a separate gate (H).

Before approval, the user sees: the exact cells or formulas, the diff, and (from Phase B on) the effect on the top 10 and on excluded suburbs. Results are labelled "dry run" until approved.

## Order and dependencies

```
A0 answers final ─► A1 import (N3) ─► A2 tidy batch ─► A3 household rows (N4)
                                                  │
B1 model spec (doc) ─► B2 spec dry run + sensitivity ─► B3 apply weights
                                                  │
C1 G3 scaling ─► C2 drive filters (G2a/G2b) ─► C3 budget ─► C4 property rules (G5) ─► C5 stairs/living
                                                  │
D1 status re-check (G4) ─► D2 bushfire decision ─► D3 round 7 (page) ─► D4 vetoes ─► D5 viewing shortlist
E  voting check: before B3 (can run any time after A1)
F  page republish: whenever a page change is approved (cards, round 7)
G  reports (G7) ─► family review (P4)
H  push: after any commit batch the user wants on GitHub
```

B1 can be drafted while waiting for answers. B2 onwards needs A1. C1 must come before C2 (register: "G3 before G2").

## Phase A — real answers into the workbook

| Step | What | Depends on | User decides before approval | Owner |
|---|---|---|---|---|
| **A0** | Mum and Dad finish. Export the `responses` collection to `Handoffs/data/` (same format as the 31 Oct export). List each person's latest v14 record; flag duplicates, TEST records and the 30 Oct v10 test (`nwug61z2s5z001smvcwy`, excluded). | Link sent; answers in | **Gate A0:** "these three records are final" (Mum, Dad, Nish's 30 Oct v14 record or a newer one) | claude.ai (only it can read the page's database) |
| **A1** | **N3 import into the real workbook** with `tools/import_v14.py` (built and tested in T2). New RawResponses columns and rows; CleanedAnswers lookups; R8.6 backfill rule; Q10/Q13d blank; Q15 as bare letters. | A0, T2 | **Gate A1:** context-column flag (carry forward vs blank); approve the column/row diff. Parent proxies are replaced by real answers; Nish's answers stay his own input. | VS Code |
| **A2** | Tidy batch (can share Gate A1): Angliss notes (rows 6, 23, 24, 33), the approved T3 cell edits, B3-S display-only columns if approved (D2 spec). | T3, T4 | **Gate A2:** each proposed cell edit and the bushfire column spec | VS Code |
| **A3** | **N4:** write `CleanedAnswers!H59`/`H61` helpers and the DiscussionSummary "would pass" display (rounds 5–7 design §4). Shown as information only, never a decision on its own. | A1 | **Gate A3** | VS Code |

Expected after A1: CleanedAnswers E59 (GW firm limit) and E61 (ED limit) fill automatically, as the strictest of the three (MIN). Settings B28:B34 references (CleanedAnswers E64–E70) fill too. Nothing changes the filters or scores until C/G gates.

## Phase B — the model spec, then weights

**B1 Model spec (document; draft any time, approval needed to adopt).** File: `Model spec — v14 answers (DRAFT).md`. Contents, each with options and a recommendation:
1. **Proxies → real answers.** PriorityWeights recompute from the three real Q15 sets automatically. State the expected direction only after A1.
2. **Replace the Q10 correction with the R8.3 ladder.** Q15.1 still sets nature against the other criteria (decided 31 Oct); the ladder replaces only the nature-to-family relationship. Options:
   - (a) ForcedChoiceCorrections row 2 votes from R8.3: A–B → Near family, D–F → Nature, C → no vote;
   - (b) a transfer sized by the ladder's extra minutes;
   - (c) no correction (Q15 ratings alone).

   Say how a capped answer (R8.3c = Y) counts: it hit the firm limit, so treat it as at least the shown band. Guard against double counting with the M (near family) score.
3. **R8.1/R8.2 kinds of nature.** There is no per-suburb nature-type data yet ("Needs data"). Options:
   - (a) discussion only;
   - (b) collect per-suburb nature-type tags (sourced), then a small match bonus inside N.

   No invented values.
4. **R8.4/R8.5 area cards.** Discussion input for the 38 card suburbs only. **The 13-suburb rule holds:** profile answers never filter, rank, promote, demote or describe Ringwood, Croydon, Berwick, Newport, West Footscray, Newtown, Highton, Torquay, Wonthaggi, Warragul, Drouin, Hurstbridge or Frankston South. Options: (a) discussion only (recommended); (b) a status-review trigger for a "least wanted" card that all three share.
5. **R8.6 + B3-S bushfire.** Not a filter by default. Options:
   - (a) display only;
   - (b) a family-decision rule (e.g. if anyone answers A "only low risk", suburbs rated "most residential streets in BMO" go to Watchlist pending discussion).

   Any status effect goes through D2.
6. **Trade-off engine Q11–Q13** unchanged (binary, 2-point override margin `Settings!B7`). Note that Q12 B's wording changed on 31 Oct (station removed) and that the 27 Oct proxies answered the old wording.
7. **Scaling of M and O (G3).** Options:
   - (a) keep 90 min;
   - (b) scale to the household firm limits (E59/E61);
   - (c) fixed 60/45.

   Recommendation pending answers. No invented values.
8. **Score P (G6, closes P7).** Waits on B4 data. Keep the current P until then.
9. **Voting** (`Settings!B2:B4`, all 1 = equal say): unchanged unless Phase E decides otherwise.
10. **Sensitivity tests to run in B2:** each change alone and all together; weights ±20% for the top three criteria; with and without the Q10 replacement; with and without G3. For each: top 10 (rank, score, moves of 3+ places), suburbs that leave or join the passing list, and the score spread.
11. **Acceptance:** what the user must see to approve, and what would send it back.

| Step | What | Depends on | Gate |
|---|---|---|---|
| **B1** | Draft the spec above. Doc only. | none (better after A1 for item 1) | **Gate B1:** adopt spec (choose options) |
| **B2** | Implement the chosen options on a temp copy. Run the sensitivity tests. Present the impact on the top 10 and excluded suburbs, labelled dry run. | A1, B1 | (information for B3) |
| **B3** | Apply to the real workbook: ForcedChoiceCorrections rows/formulas, PriorityWeights if the spec changes them, `Settings!B38/B39` if G3 is chosen (or do G3 in C1). Recalc, diff, log. | B2, E | **Gate B3: weights change** |

## Phase C — filters (the Filters tab is the family decision record)

| Step | What | Depends on | User/family decides | Gate |
|---|---|---|---|---|
| **C1** | **G3** M/O scaling: `Settings!B38/B39` (currently 90/90), formulas M and O read them instead of `Filters!B4/B5`. Add the missing M and T formulas in rows 2, 7 and 13 only if those rows can pass (register task B1; see D5). | A1, B1 item 7 | Scale values | **Gate C1** |
| **C2** | **G2a/G2b** `Filters!B4` (GW cap, now 90) and `B5` (ED cap, now 90) from the household limits E59/E61. Show which passing suburbs would fail each option. | C1, A3 | Options: (a) strictest person's limit (MIN, as built); (b) majority; (c) keep 90 with the limits as preferences. "No cap" handling. Record the family decision in the Filters notes. | **Gate C2** |
| **C3** | Budget: Q3c answers. Change `Filters!B2` ($1.5m) only if the family agrees a new figure. | A1 | Keep or change | **Gate C3** |
| **C4** | **G5** property rules: `Settings!B28:B37` (separation floor/ceiling/importance, mobility, garden bands, front-door access; land bands 400/650/1000 from Settings C35:C37). Listings AA/AG then compute (32 listings). Check CleanedAnswers F65 (separation conflict). | A1 | Approve values; resolve any F65 conflict | **Gate C4** |
| **C5** | `Filters!B6` stairs (allowed since 27 Oct, NJD) against R6.4; `B7` living arrangement against Q7a/R6.1–R6.3; `B8` garden against R6.5a/b. | A1 | Keep or change each | **Gate C5** |

## Phase D — shortlist and status

| Step | What | Depends on | Gate |
|---|---|---|---|
| **D1** | **G4** re-evaluate L (hard filter status) for all rows under the new filters. Propose any C (shortlist status) changes with reasons. | C2–C5 | **Gate D1:** each status change |
| **D2** | Bushfire: read R8.6 answers against the B3-S table. Propose status effects only per the B1 item 5 option chosen. Add display-only workbook columns if approved (A2). | T4, A1, B1 | **Gate D2** |
| **D3** | **Round 7 page** (rounds 5–7 design §3): three "which would you visit first" pairs from surviving suburbs; R7.4 "definite no" veto per suburb; R7.5 airport frequency. Design, then page build and republish (Phase F). | D1 | **Gate D3a:** round 7 design; **D3b:** publish |
| **D4** | Import round 7; R7.4 vetoes become proposed status changes; airport is a tie-breaker only if "monthly or more". | D3 | **Gate D4** |
| **D5** | Viewing shortlist: apply the proposed rule (DiscussionSummary A38: at least 2 Community comparators, at least 1 nature-first anchor, …). Respect the 13-suburb rule. Include the four over-budget "needs data" suburbs only if register task B1 (Chrome under-$1.5m search) finds suitable homes. | D1, D2, D4 | **Gate D5:** adopt the rule and the list |

## Phase E — voting (Mum / Dad / Nish)

Current: `Settings!B2:B4` = 1, 1, 1 (equal say in PriorityWeights and the trade-off votes). The cap of 2 Top priorities per person (`B5`) also applies.

| Step | What | Gate |
|---|---|---|
| **E1** | After A1, show how each person's real answers pull the weights (per-person PriorityWeights columns) and where the three disagree most. Ask whether equal say stands. Options: (a) equal (status quo); (b) unequal weights; (c) equal weights plus a per-person veto at round 7 (R7.4 already gives this). | **Gate E1** (before B3) |

## Phase F — republishing the questionnaire page

Only the claude.ai session can publish (Artifact tool, same URL `https://claude.ai/artifact/9fbNBMzhdedGaYwQg3pnGo`, link-only, no sign-in).

Triggers: card wording changes from T3/T4 findings, round 7 (D3), fixes found while answers come in.

Procedure:
1. Archive the folder copy.
2. Edit the page source in the folder.
3. Run `tools/questionnaire_tests/` (all must pass; update expectations for new questions).
4. Phone/iPad checks.
5. Publish to the same URL.
6. Read back and confirm the live file's sha = the folder file's sha.
7. Update the change log, the design note and `PROJECT_STATE.md`.

**Version rule:**
- Since Nish has answered v14, any change to options or stored values on v14 needs `PAGE_VERSION` bumped. A bump changes the WhatsApp header, the draft key and the import check, and needs a new import script mapping.
- Wording-only changes can stay on v14 if logged.
- A change made after the link is sent must be weighed against answers already given.

| Step | What | Gate |
|---|---|---|
| **F1** | Any page change | **Gate F1** per change: approve the exact diff; send-link status unchanged unless the user says so |
| **F2** | Send the link to Mum and Dad (user does this) | User's call |

## Phase G — reports

| Step | What | Depends on | Gate |
|---|---|---|---|
| **G1r** | Fix `tools/found.py` (broken on the current report format) or keep editing the foundation report by script. | none | Routine (no gate) |
| **G2r** | Regenerate the parent report (`tools/report2.py` on a recalculated temp copy) and the foundation report from the approved workbook commit. Drafts, marked "requires family review". | B3, C2, D1 | **Gate G2r:** substantive report changes |
| **G3r** | Family review (P4). Nothing is published or distributed without approval. | G2r | User/family |

## Phase H — pushing to GitHub

Remote: `origin https://github.com/okgoogle13/parents-melbourne-move.git`. The user said not to push until approved; there's also an unmerged local branch `local-merge-backup`.

| Step | What | Gate |
|---|---|---|
| **H1** | Pre-push check. Confirm the GitHub repo is **private**. List commits since `origin/main`. Flag family personal data in them: the responses export in `Handoffs/data/`, RawResponses answers, notes. Confirm `.claude/settings.local.json`, downloaded GIS data and `research/inputs/parents-melbourne-move-handover.md` are not tracked (`.gitignore`). Run `.venv/bin/python tools/validate_macro.py`. Decide about `local-merge-backup` (keep local, don't push). | none |
| **H2** | `git push origin main` (no force). Verify `origin/main` = local `main`. | **Gate H2:** explicit "push" from the user |

## Approval checklist (for the user)

- A0 final records · A1 import + context flag · A2 tidy batch + bushfire columns · A3 household display
- B1 spec options · B3 weights
- C1 scaling · C2 drive filters · C3 budget · C4 property rules · C5 stairs/living/garden
- D1 status changes · D2 bushfire effect · D3a/D3b round 7 · D4 vetoes · D5 viewing shortlist
- E1 voting · F1 each page change · G2r reports · H2 push
