# Project state — handoff (27 Oct 2026)

## Current task
Comparator drives on the 10:00 basis in both reports: **complete.** 08:00 appears only as context labelled "Peak (08:00), not used in the workbook J/K figures", plus the approved Point Cook wording. Nothing published or sent.

## Branches
| Branch | Latest commit | Holds |
|---|---|---|
| `claude/ecstatic-tesla-pzbg1v` | this commit (after 7acd52f) | workbook, parent report draft, this file |
| `claude/inspiring-lovelace-cflq1z` | 5a23bd2 | all of 7acd52f plus the refreshed foundation report |

The open-work "Reports" row here is stale (says 08:00); merging inspiring-lovelace fixes it.

## Canonical workbook
`Our Next Home — Family Relocation Scoring Model.xlsx` at **387763a**, identical on both branches.
- Recalculated with 0 errors.
- Passing = 51.
- Rows 67–72 are unranked.

Tab map and change log: `scoring-model-pointer.md`.

## Reports
| File | Commit | Source |
|---|---|---|
| `Our Next Home — parent report (28 Oct 2026).html` | ecstatic 7acd52f | Workbook 387763a; marked "Draft — requires family review; not for publication or distribution" |
| `Suburb shortlist foundation report.md` / `.pdf` | inspiring-lovelace 5a23bd2 | Workbook 387763a |
| Prior versions | `Archive/` | "(superseded 2026-10-28, …)" |

Evidence: `Community comparators — research (28 Oct 2026).md`, workbook column Z.

## Approved decisions
Detail: pointer change log.
- Comparators: Springvale, Clayton South, Keysborough, Clyde North, Endeavour Hills, Wheelers Hill. Drives = workbook J/K, 10:00 weekday.
- Point Cook: Conditional, not a comparator. "fails the verified 90-minute Glen Waverley journey at 08:00 peak."
- Tarneit: "Excluded — family decision 28 Oct 2026 (stated reasons: safety concerns and not enough going for it)". Not a filter failure; no crime data.
- Mount Waverley: Excluded. Rowville: Reference only. Frankston, Mordialloc and Seaford are the nature-first anchors.
- Q13d: reference-only; it feeds no formula, weight, rank or score.
- Wheelers Hill budget: Checked (Jellis Craig sold results). Suitable-property check still outstanding.
- Endeavour Spices and Shri Sanatan Dharam: Needs verification. Shrinathji Haveli is the confirmed temple.
- Never call a suburb "suitable". Comparator column L never says "pass".

## Remaining blockers
1. Neither branch is in the local folder yet.
2. The parent report needs family review before any use.
3. P1/P2 (Mum's Glen Waverley limit; the 90-min cap) undecided; see `Talking with Mum — how far from Glen Waverley.md`.
4. Three items are pending:
   - B4 (community drive minutes), which decides how P is defined
   - suitable-property checks for the six comparators
   - Q13d answers
5. The anchors are timed "leave now"; the comparators at 10:00. Re-time the anchors (B2).
6. Two wording flags:
   - Option B's "Hills / forest" label doesn't fit its suburbs.
   - DiscussionSummary B38 says "verified"; the reports say "checked".
7. Report build scripts are not committed; lost when this cloud session ends.

Full task list: `Open work — what runs where (27 Oct 2026).md`.

## Next task
In the local folder:
`git fetch origin && git merge origin/claude/inspiring-lovelace-cflq1z && git merge origin/claude/ecstatic-tesla-pzbg1v`
Then recalculate the workbook in Excel and confirm Passing = 51.
