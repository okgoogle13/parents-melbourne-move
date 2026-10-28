# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Start here

1. Read `PROJECT_STATE.md`: current baseline, canonical file versions, next task.
2. Read `PROJECT_INSTRUCTIONS.md`: the user's standing brief. It overrides this file.
3. For workbook structure, editing procedure and research method, read `docs/workflow.md`.

This is not a software project. It is the research record for choosing suburbs in or around Melbourne for the user's parents (and the user, who lives with them). `main` is the consolidated baseline and mirrors the user's local Mac folder. Work from it. Inspect other branches only if `PROJECT_STATE.md` disagrees with the files on `main`, or a canonical file it names is missing.

## Canonical files (when sources disagree)

1. `Our Next Home — Family Relocation Scoring Model.xlsx`: canonical for suburbs, scores, weights, filters, budget and family responses. The **Filters** tab is the family decision record.
2. `scoring-model-pointer.md`: tab map, status counts and the workbook change log.
3. Other root files. Reports (`Suburb shortlist foundation report.*`, `Our Next Home — parent report (…).html`) are derived from the workbook at a named commit and lag it.
4. `Archive/`: superseded. Never a source unless the user asks.

Read the workbook before answering anything about suburbs, scores, filters or responses. Don't answer from memory or from the reports.

## Permanent rules

- **No Google.** No Drive, Sheets, Docs or Forms, even if connectors exist. An old Google Sheet copy is stale and not a source.
- **Archive, never delete.** Before changing a file, copy it to `Archive/` with a suffix such as `(superseded 2026-10-28, before <change>)`, then edit the root file in place. No near-duplicates in the root.
- **One session edits the workbook at a time.** Re-read it immediately before writing.
- **Keep it Excel-compatible.** No Google-only functions (`XMATCH`, `REGEXEXTRACT`, `ARRAYFORMULA`).
- **Reports are drafts until the family approves them.** Don't publish or distribute them.

## Approval boundaries (need the user's explicit approval)

- Family weights (PriorityWeights, ForcedChoiceCorrections), the Filters tab, and the definition of score P (Indian community).
- Any location status change (SuburbScorecard col L), adding or removing locations, and approved report content.
- Display-only items stay display-only: col AX (community band), Q13d, the Community comparator rows and ABS demography (AK–AW) never feed X, Y or any weight.

## Evidence standards

- Every researched fact gets its source in the suburb's SuburbScorecard col Z (and AC or AE–AJ where relevant).
- Label every value **Checked** or **Estimate**, in the workbook and in answers. Judgement scores change only with a cited source, logged in col Z.
- State the basis for every drive time (e.g. "10:00 weekday, top of range") and price (e.g. OnTheHouse "median value" AVM ≠ sale median).

## Recalculation check (run after any workbook change)

Never recalculate the canonical file in place. Work on a temporary copy:

```bash
T=$(mktemp -d); mkdir "$T/in" "$T/out"
python3 -I -c 'import openpyxl,sys; openpyxl.load_workbook(sys.argv[1]).save(sys.argv[2])' \
  "Our Next Home — Family Relocation Scoring Model.xlsx" "$T/in/wb.xlsx"   # strips cached values -> forces full recalc
soffice --headless --calc --convert-to xlsx --outdir "$T/out" "$T/in/wb.xlsx"
```

Then load `$T/out/wb.xlsx` with `openpyxl` (`data_only=True`) and check for zero error values (`#REF!`, `#VALUE!`, `#NAME?`, `#DIV/0!`, `#N/A`, `#NUM!`, `#NULL!`). Check that SuburbScorecard X/Y and the passing count change only where intended. Diff against a recalculated pre-change copy; the canonical file stores no cached values. Log the result in `scoring-model-pointer.md` (details in `docs/workflow.md`).

# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
