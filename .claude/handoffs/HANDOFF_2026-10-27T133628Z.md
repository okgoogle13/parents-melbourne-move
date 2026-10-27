# Session Handoff

- Generated: 2026-10-27T13:36:28Z (28 Oct 2026 AEDT)
- Working directory: /Users/okgoogle13/Projects/Parents Melbourne MOVE (claude.ai chat linked to this folder; cloud scratch for ABS download)
- For: the Claude Code cloud session on branch `claude/ecstatic-tesla-pzbg1v` that proposed "C3 — re-score N, R, V; defer P"

## Session goal
Critique the C3 plan's handling of the Indian community score (P), checking whether it dilutes the value of living near people of colour. Then start option 1 (chosen by the user): add a labelled set of high-diversity / low-nature suburbs (e.g. Springvale, Tarneit) to compare side by side against the leafy, low-diversity shortlist.

## Decisions
- **C3's 13 N/R/V changes are fine to run as proposed.** The sources are adequate. Keeping P unchanged during C3 does not dilute anything.
- **Rejected: redefining P as "drive minutes to an Indian grocery/temple" (B4), with the ABS shares left as zero-weight "context".**
  - Q13 (Mum A; Dad B; Me B) moved no weight under the model's own rule. It never asked about living among people of colour, so using it to redefine P is an interpretation that overrides the only dissenter (Mum).
  - A drive-access score probably flattens: most metro and regional-centre suburbs pass 30 min (inference, unverified).
  - The top 15 are already low-diversity: 14/15 have India-born under 2%, and 8/15 have under 10% speaking another language at home. Only Berwick is diverse.
- **Chosen: option 1, a community comparison set** (over option 2, a second "what-if" rank, and option 3, paired viewings with no model change).
  - Add 6–8 suburbs with `Shortlist Status = Community comparator`, chosen by ABS India-born and other-language share, that still pass the $1.5M and 90-min filters.
  - Add one Community column: B4 drive access plus ABS banding (AU other-language, AQ India-born).
  - Leave the family weights unchanged.
  - Show a Nature (N) vs Community view, and pick viewings from each corner: green/low-diversity, diverse/low-green, and both.
  - Viewing quota: at least 2 from the community corner, so comparators aren't dropped on rank.
- **The user approved option 1 only.** Not approved: splitting P 50/50 between access and diversity, or a new Q13d family question. Both are still open.
- **B4 scope must include church**, not just grocery/temple. Mum's Q9 answer was "a church or place of worship nearby". Apply this to the C3 plan text and to Task 7 in `Claude_in_Chrome_prompt — close research gaps.md`. Measure the nearest place of worship generically, not one institution (per project instructions).
- **No workbook edits until the user approves the 6–8 comparator suburbs.**

## Bugs / issues surfaced
- **The folder is behind the branch** (open). Local `main` (e4c1c1b) has the workbook ending at column AJ. C1/C2 (cols AK–AW, commit 45aa38d) exist only on `origin/claude/ecstatic-tesla-pzbg1v`. Per the project rules the folder is the source of truth, so merge the branch into the folder before C3.
- **AK–AW header comments are shifted one column right** (open).
  - Examples: AP's comment describes AO (overseas-born definition); AQ's describes AP (not-stated); AS's describes AR (Indian ancestry); AW's describes AV (G13 language caveat).
  - Re-anchor each comment one column left.
- **git in the connected folder can't delete its lock files** (workaround in place). Deletion permission is off, so `git fetch` left `.git/objects/maintenance.lock`; it was moved to `.git/stale-maintenance-lock-20261027`. The merge or commit will hit this again; request delete permission first (device_request_delete_permission) or move locks aside.
- **Handoff files are gitignored on the branch** (`.claude/handoffs/`, commit 68edd94). This file won't travel via git; paste it into the cloud session or read it from the folder.
- **Price lookup is limited.**
  - The OnTheHouse suburb page worked for Springvale (a link from search results).
  - The Clayton South page returned no figures.
  - The user rejected WebFetch on hand-built OnTheHouse URLs. Don't construct URLs; use links from search results (Statement of Information PDFs carry suburb medians with period) or ask the user.
- **OnTheHouse now labels figures "median value" (as at 30 Sep 2026)**, not "sale median, rolling 12m" as in col H. Record the basis exactly; don't mix the two silently.

## Verified data (ABS 2021 GCP DataPack, SAL VIC, tables G01/G02/G08/G09G/G14)
Same definitions as cols AO–AU: share of all people. Checked against the workbook: Glen Waverley and Berwick match exactly.

| Suburb | SAL | Pop | Med age | 65+ | India-born | Indian anc. | Hindu | Sikh | Other lang. | Corner |
|---|---|---|---|---|---|---|---|---|---|---|
| Springvale | SAL22328 | 22,174 | 36 | 16% | 7.4% | 5.7% | 4.2% | 3.2% | 76% | community |
| Tarneit | SAL22451 | 56,370 | 30 | 4% | 28.8% | 27.0% | 21.1% | 13.6% | 64% | community |
| Clayton South | SAL20570 | 13,381 | 34 | 16% | 14.9% | 12.3% | 12.3% | 3.0% | 67% | community |
| Clayton | SAL20569 | 18,988 | 28 | 10% | 16.4% | 13.5% | 14.6% | 2.1% | 64% | community |
| Clyde North | SAL20582 | 31,681 | 30 | 5% | 18.2% | 18.4% | 12.2% | 10.2% | 54% | community |
| Keysborough | SAL21339 | 30,018 | 36 | 14% | 6.6% | 7.3% | 4.9% | 1.8% | 61% | community |
| Noble Park | SAL21952 | 32,257 | 35 | 15% | 9.8% | 7.4% | 4.9% | 4.8% | 64% | community |
| Point Cook | SAL22086 | 66,781 | 33 | 6% | 14.9% | 17.4% | 16.1% | 2.5% | 51% | both? (wetlands/coast) |
| Mount Waverley | SAL21816 | 35,340 | 40 | 19% | 6.1% | 7.7% | 7.0% | 0.8% | 50% | both? |
| Wheelers Hill | SAL22766 | 20,652 | 48 | 29% | 4.1% | 5.6% | 4.5% | 0.7% | 46% | both? (Jells Park) |
| Wantirna South | SAL22686 | 20,754 | 42 | 21% | 4.7% | 6.4% | 5.8% | 0.7% | 44% | both? |
| Endeavour Hills | SAL20871 | 24,455 | 39 | 17% | 4.6% | 5.9% | 3.8% | 0.8% | 51% | both? |
| Rowville (ref) | SAL22207 | 33,571 | 41 | 16% | 3.2% | 4.8% | 3.5% | 0.7% | 32% | reference |

- The "both?" nature claims (Jells Park, Point Cook wetlands/coast, Churchill/Lysterfield parks) are recall. They need a C1-style source before any N score.
- Price checked so far: Springvale houses **$877,575**, units $614,963 — OnTheHouse "median value" as at 30 Sep 2026 (onthehouse.com.au/property/vic/springvale-3171).
- Drive times to Glen Waverley are all unchecked. Recall estimates: Springvale ~15 min, Clayton ~10–15, Keysborough ~20, Wheelers Hill ~5–10, Clyde North ~35–40, Point Cook/Tarneit ~45–60. Treat as estimates.

## Next steps
1. **Sync the folder.** Get the user's OK to merge `origin/claude/ecstatic-tesla-pzbg1v` into local `main` in the connected folder. Handle git lock files first: request delete permission, or move locks aside.
2. **Finish prices for the 13 candidates above.** Use house sale medians, with the source and as-at date. Search-result links only; no hand-built URLs. Flag anything over $1.5M (likely Mount Waverley, possibly Wheelers Hill and Point Cook — unverified).
3. **Propose 6–8 comparators to the user.**
   - Aim for 4–5 community-corner and 2–3 "both"-corner suburbs, with checked versus estimate columns kept separate.
   - Drop any that fail $1.5M or 90 min.
   - Wait for approval.
4. **Once approved, change the workbook.**
   - Archive it as `Archive/… (superseded 2026-10-2X, before community comparators).xlsx`.
   - Add rows with `C = Community comparator` and AK–AW filled from the table above.
   - Add the Community column and the quota note (Filters or DiscussionSummary).
   - Recalc: 0 errors; diff shows only the new rows and columns.
   - Update `scoring-model-pointer.md` and the open-work file.
5. **Run C3 as proposed, with the plan text amended.**
   - Remove "P should measure drive access … ABS shares stay as context". Replace it with "P/Community definition pending; B4 measures grocery, temple and church drive minutes".
   - After the recalc, report top-15 diversity (India-born and other-language share) alongside rank movement.
6. **Fix the AK–AW comment offset.**
7. **Update Task 7 in the Chrome prompt** to include church and the comparator suburbs.

## Files touched
- `.git/objects/maintenance.lock` → moved to `.git/stale-maintenance-lock-20261027` (left by `git fetch`; couldn't be deleted).
- `.claude/handoffs/LATEST.md` and `HANDOFF_2026-10-27T133628Z.md` — this handoff (gitignored on the branch).
- No workbook, pointer or open-work changes in this session.

## Open questions
- Which 6–8 comparators (user approval pending)?
- How the Community column is built.
  - Proposal: 50% B4 drive access (grocery, temple, church) + 50% diversity band from AU and AQ.
  - Band thresholds are not set.
  - Is it scored inside P's 7.9% weight, or display-only? The user approved only the comparison set, not a weight change.
- Ask the family a Q13d question ("very green village, one of very few Indian families" vs "slightly less green, mixed multicultural neighbourhood", community 30 min away in both)?
  - Nobody was asked whether living near people of colour matters.
  - The user's own answers (Q9 D "friendly neighbours of any background", Q13 B) point away from it; Mum's (Q9 A church, Q13 A, Q15.3 C) point toward it.
- Viewing quota size: 2 from the community corner is a proposal, not decided.
