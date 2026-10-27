# Project state

Read this first. Updated 28 Oct 2026 (consolidation session).

## Baseline

- `main` is the single consolidated baseline and mirrors the local Mac folder. On 28 Oct 2026 it was fast-forwarded from `f7ac8c6` to `5a23bd2` (`claude/inspiring-lovelace-cflq1z`, which already contained `claude/ecstatic-tesla-pzbg1v`). The docs commit with this file sits on top.
- Superseded branches: `claude/ecstatic-tesla-pzbg1v`, `claude/inspiring-lovelace-cflq1z` (fully in `main`) and `claude/compassionate-wright-lvhyzm` (its CLAUDE.md was rewritten into `main`; its base is old). `claude/local-project-migration-eddwy2` holds only a `.gitignore` change already in `main`. Nothing on these branches needs merging.

## Canonical versions

| File | Version | Status |
|---|---|---|
| `Our Next Home — Family Relocation Scoring Model.xlsx` | Last changed in commit `387763a` (comparator fixes); sha256 `d1b95d47…bcd88c` | Approved research baseline (28 Oct). Recalc on a temp copy: 0 errors, 51 ranked rows. The file stores no cached formula values; Excel/LibreOffice recalculate on open |
| `Our Next Home — parent report (28 Oct 2026).html` | Commit `7acd52f`, built from workbook `387763a` | Draft: requires family review; not for publication or distribution |
| `Suburb shortlist foundation report.md` / `.pdf` | Commit `5a23bd2`, aligned to workbook `387763a` | Awaiting human review |

Status counts, ranks and the change history are in `scoring-model-pointer.md`; open tasks are in `Open work — what runs where (27 Oct 2026).md`.

## Last completed

- 28 Oct 2026: consolidated `main` (fast-forward, no merge commit). Added the concise `CLAUDE.md`, `docs/workflow.md` and this file. Workbook, reports, weights, Filters and P unchanged.

## Next task

- **Human review of the reports**: the parent report draft and the foundation report, against the approved workbook. Nothing is published or distributed until the family approves.
- Still open after that (not blocking): P definition (B4 drive minutes), Q13d answers, suitable-property checks for the six comparators, Point Cook travel decision, whether the 60-min preference becomes a filter, and the Claude in Chrome tasks B1–B5.
