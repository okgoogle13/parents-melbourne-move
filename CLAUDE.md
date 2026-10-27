# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Not a software project. It is the research record for choosing suburbs in or around Melbourne for the user's parents (and the user, who lives with them). The deliverables are an Excel scoring model, Markdown/PDF/HTML reports, a questionnaire page, and research prompts. There is no build, lint or test suite; the "test" is a clean workbook recalculation (below).

`PROJECT_INSTRUCTIONS.md` is the user's standing brief. Read it; it overrides anything here.

## Sources of truth (when files disagree)

1. `Our Next Home — Family Relocation Scoring Model.xlsx`: canonical for suburbs, scores, weights, filters, budget and family responses. The **Filters** tab is the family decision record.
2. `scoring-model-pointer.md`: tab map, current status counts and a reverse-chronological change log. Update it on every workbook change.
3. Other root files. `Open work — what runs where (27 Oct 2026).md` is the task list (C* = cloud session, B* = Claude in Chrome, P* = people).
4. `Archive/`: superseded. Never use as a source unless asked.

Read the workbook before answering anything about suburbs, scores, filters or responses. Don't answer from memory or from report files, which lag the workbook.

## Hard rules

- **No Google.** No Drive, Sheets, Docs or Forms, even if connectors exist. An old Google Sheet copy is stale and is not a source.
- **Never delete or overwrite without archiving.** Before changing a file, copy it to `Archive/` with a suffix like `(superseded 2026-10-27, before <change>)`, then edit the root file in place. No near-duplicate files in the root.
- **Checked vs estimate.** Every researched fact carries its source in SuburbScorecard col Z (and AC/AE–AJ where relevant). Label anything not checked as an estimate, in the workbook and in answers.
- **Family decisions are not Claude's.** Don't change weights (ForcedChoiceCorrections/PriorityWeights), the Filters tab, or the definition of score P (Indian community) without the user's explicit approval. Judgement scores change only with a cited source, logged in col Z.
- **Display-only stays display-only.** Col AX (Community comparison band), Q13d, the comparator rows (67+) and ABS demography (AK–AW) must never feed X, Y or any weight. Comparator rows' col L avoids the word "pass" so Y and the DiscussionSummary passing count ignore them.
- **One session edits the workbook at a time.** Re-read it immediately before writing.

## Git and branches

`main` mirrors the user's local Mac folder (`/Users/okgoogle13/Projects/Parents Melbourne MOVE/`), which they sync with `git pull` / `git merge --ff-only`. Cloud-session branches (`claude/*`) are often **ahead of `main`**, and a new session's branch may start from a stale `main`. Before editing the workbook, run `git fetch origin && git log --all --oneline -15` and check you're building on the latest workbook commit. Merge the newer branch in if needed rather than editing an old copy.

`.claude/handoffs/LATEST.md` is the latest session handoff (decisions, open bugs, next steps). Newer branches gitignore `.claude/handoffs/` and `.claude/handoff-nudge-state.json`; don't commit the nudge-state file.

## Workbook architecture

Ten tabs, flowing roughly left to right:

- **RawResponses** → **CleanedAnswers**: one row per questionnaire submission. CleanedAnswers pulls each person's *latest* row (Mum, Dad, Me) with `LOOKUP`, plus the Max-2-Essential check. Import rule: a new RawResponses row per person = their previous latest row + the new round's answers. Forced-choice answers are stored as full option text, because the engine reads the "A —"/"B —" prefix.
- **PriorityWeights**: per-person Q15 scores, normalised, combined by say-in-decision weights from **Settings**.
- **ForcedChoiceCorrections**: trade-off engine in H1:U5 (Q10–Q13). If the winner isn't 2 pts ahead, it moves `MIN(loser, (loser−winner+0.02)/2)` from loser to winner. Final criteria weights are in **B6:B15**, which SuburbScorecard X reads.
- **Filters**: hard caps (budget, Glen Waverley drive, ED drive) that drive SuburbScorecard col L status.
- **SuburbScorecard**: one row per location; rows 49–50 are synthetic test rows, excluded everywhere.
  - A–H, Z: plain values. J/K: drive minutes to Glen Waverley / nearest ED. L: filter status.
  - M–V: 0–10 criteria scores. M (near family), O (hospital) and T (price) are formulas; N, P, Q, R, S, U and V are judgement scores.
  - W/X/Y: scores-entered, weighted score, rank among pass rows only.
  - Z: sources and notes ("CHECKED …"). AC: train basis. AE–AJ: budget verification. AK–AW: ABS 2021 demography. AX: community band.
- **Listings**: realestate.com.au properties. Pasted columns hold values; G and P–T are formulas looking up Filters and SuburbScorecard. Refresh overwrites pasted columns only.
- **DiscussionSummary**: counts, decision log, comparator list.

The file must stay Excel-compatible: no Google-only functions (`XMATCH`, `REGEXEXTRACT`, `ARRAYFORMULA`, etc.).

## Editing and recalculating the workbook

Edit with `openpyxl` (preserves formulas; drops cached values). Then recalculate a copy in headless LibreOffice and check it:

```bash
S=<scratch dir>
soffice --headless --calc --convert-to xlsx --outdir "$S/out" "Our Next Home — Family Relocation Scoring Model.xlsx"
# then: openpyxl.load_workbook("$S/out/<file>.xlsx", data_only=True) and confirm
#  - zero cells with #REF!/#VALUE!/#NAME?/#DIV/0!/#N/A/#NUM!/#NULL!
#  - SuburbScorecard X/Y changed only where intended (diff against the pre-change copy)
#  - DiscussionSummary passing count as expected
```

Log every workbook change in the change log in `scoring-model-pointer.md`: what changed, which cells, sources, the recalc result ("0 errors; X/Y unchanged except …") and "Pre-change copy in Archive". Update status counts and the open-work file if they move.

## Other deliverables

- `Our Next Home — questionnaire page (Claude artifact source).html`: source of a published Claude artifact. It is always republished to the **same URL** (recorded in the pointer change log). Each new round shows only the "still needed" questions and saves with a mode label like `round 4 (Q13d)`. Archive the previous page before republishing.
- `Suburb shortlist foundation report` (.md + A4-landscape .pdf) and `Our Next Home — parent report (… ).html`: generated from the workbook at a named commit. When the workbook changes they go stale; refresh them, don't hand-edit numbers.
- `Claude_in_Chrome_prompt — close research gaps.md`: tasks that need the user's signed-in browser or live Google Maps.

## Research constraints in cloud sessions

- realestate.com.au is blocked; healthdirect and OpenStreetMap have been unreachable. Leave those tasks for Claude in Chrome (B* tasks) and say so in col Z.
- Don't WebFetch hand-built OnTheHouse URLs (the user rejected it); use links returned by search. Record price bases exactly (OnTheHouse "median value" AVM ≠ sale median; agent Statement of Information PDFs give suburb medians).
- Drive times must name their basis (e.g. "10:00 weekday, top of range" vs "08:00 peak"). J/K use one basis per row.
- ABS figures come from the 2021 GCP DataPack (SAL, VIC). Note small-population perturbation (< 2,500).
