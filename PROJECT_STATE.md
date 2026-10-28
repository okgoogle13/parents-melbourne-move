# Project state

Read this first. Updated 28 Oct 2026 (lean config session).

## Baseline

- `main` is the consolidated baseline. Fully contained in it: `claude/inspiring-lovelace-cflq1z` (which includes the workbook and report work from `claude/ecstatic-tesla-pzbg1v`). Other branches hold unmerged doc-only commits; check with `git branch -a --no-merged main` before relying on one.
- Local sync, verified 28 Oct 2026: local `main` = `origin/main` = `b2f390e`; on-disk workbook sha256 matches the table below. The docs commit of 28 Oct (lean config) is local-only until pushed.

## Canonical versions

| File | Version | Status |
|---|---|---|
| `Our Next Home — Family Relocation Scoring Model.xlsx` | Last changed in commit `387763a` (comparator fixes); sha256 `d1b95d47…bcd88c` | Approved research baseline (28 Oct). Last recalc test (cloud session, 28 Oct): 0 errors, 51 ranked rows. Currently stores no cached formula values |
| `Our Next Home — parent report (28 Oct 2026).html` | Commit `7acd52f`, built from workbook `387763a` | Draft: requires family review; not for publication or distribution |
| `Suburb shortlist foundation report.md` / `.pdf` | Commit `5a23bd2`, aligned to workbook `387763a` | Awaiting human review |

Status counts, ranks and the change history are in `scoring-model-pointer.md`; open tasks are in `Open work — what runs where (27 Oct 2026).md`.

## Last completed

- 28 Oct 2026: consolidated `main` (fast-forward, no merge commit). Added the concise `CLAUDE.md`, `docs/workflow.md` and this file. Workbook, reports, weights, Filters and P unchanged.
- 28 Oct 2026: slimmed `CLAUDE.md` (files read on demand); moved the recalc test into `docs/workflow.md` with populated-result and unchanged-canonical checks. Pre-change copies in `Archive/`. Recalc test not run locally: LibreOffice is not installed on the Mac. Brief, workbook and reports unchanged.

## Next task

- **Human review of the reports**: the parent report draft and the foundation report, against the approved workbook. Nothing is published or distributed until the family approves.
- Still open after that (not blocking): P definition (B4 drive minutes), Q13d answers, suitable-property checks for the six comparators, Point Cook travel decision, whether the 60-min preference becomes a filter, the Claude in Chrome tasks B1–B5, and installing LibreOffice so the recalc test runs locally.
