# Session Handoff

- Generated: 2026-10-27T13:53:28Z (28 Oct 2026 AEDT)
- Working directory: /Users/okgoogle13/Projects/Parents Melbourne MOVE (claude.ai chat linked to this folder; ABS download done in cloud scratch)
- For: the Claude Code cloud session on branch `claude/ecstatic-tesla-pzbg1v` that proposed "C3: re-score N, R, V; defer P"

## Session goal
Critique the C3 plan's handling of the Indian community score (P), then turn the user's decisions into one paste-ready corrective prompt for the cloud session. That prompt covers C3, a new Q13d question, and research on community-comparator suburbs.

**The prompt is the working spec:** `Prompt — C3 correction and community comparators (for cloud session, 28 Oct 2026).md` in the folder root.

## Decisions (all approved by the user, 28 Oct)
- **C3 goes ahead, with P unchanged.** The 13 N/R/V changes run as proposed. P is not redefined as "drive minutes to Indian grocery/temple".
  - Alternative rejected: the plan's own version, which redefined P and left the ABS shares as zero-weight context.
  - Why: Q13 (Mum A; Dad, Me B) moved no weight under the model's rule and never asked about living among people of colour. A drive-access P would likely flatten, since most metro suburbs pass 30 min (inference). 14 of the current top 15 already have India-born below 2%.
- **B4 measures Indian grocery, Hindu temple and church.** Church was added because it was Mum's Q9 answer. Measure the generic nearest of each, not one named institution.
- **Community comparison band is display-only.**
  - Built from AU and AQ, with a placeholder for B4 drive minutes. It never feeds X, Y or P's weight, and is labelled "Comparison band, not a liveability score".
  - Interim thresholds, which the user still has to confirm:
    - High: AU ≥ 50% or AQ ≥ 8%
    - Medium: AU 30–49% or AQ 4–7.9%
    - Low: everything else
  - Alternatives rejected: a second "what-if" rank, a 50/50 P split, and paired viewings with no model change.
- **6–8 comparators.**
  - About 4–5 "Diverse / lower-green" and about 2–3 "Potential both".
  - "Potential both" needs sourced evidence of both a real nature feature and named community infrastructure. Without both, the suburb is relabelled or marked "Needs verification".
  - The current top 3 passing suburbs are shown as "Green / lower-diversity" anchors; Rowville is "Reference". Neither counts toward the 6–8.
- **Proposal format: two tables.** Output 1 is a compact trade-off table with no overall winner. Output 2 is a spreadsheet-ready evidence table. The exact column orders are in the prompt file.
- **Q13d is a new question, not a replacement for Q13.**
  - 5-point scale: A strongly / A slightly / No strong preference / B slightly / B strongly.
  - Reference-only; it doesn't feed ForcedChoiceCorrections.
  - Final wording keeps the neighbour clause, which is what separates it from Q13:
    - A: "Most neighbours would not share your background."
    - B: "many neighbours are from Indian and other migrant backgrounds"
  - The user rejected an earlier version that listed four benefits for B and one for A.
- **Fixed rules.** No changes to family weights or the Filters tab. Checked facts and estimates stay separate. Every source goes in column Z.
- **STOP before workbook edits.** After research, the cloud session presents the comparator tables. It changes the workbook only after the user approves the final list. C3 is the only workbook change allowed before then.

## Bugs / issues surfaced
- **The folder is behind the branch** (open).
  - Local `main` is e4c1c1b, and the workbook ends at column AJ. C1/C2 (AK–AW, commit 45aa38d onward) exist only on `origin/claude/ecstatic-tesla-pzbg1v`.
  - A fast-forward is confirmed clean (`git merge --ff-only`). It changes 5 files.
  - The user was given the Terminal commands and hasn't confirmed running them. Repeat the fast-forward after the cloud session pushes.
- **git can't delete files in the connected folder** (workaround in place).
  - Delete permission is off, so git leaves `.lock` files behind. `.git/objects/maintenance.lock` was moved to `.git/stale-maintenance-lock-20261027`.
  - Request delete permission before any merge from the device shell.
- **AK–AW header comments are offset one column to the right** (open; fix is in the prompt). For example, AP's comment defines AO and AW's describes AV.
- **Workbook column D is titled "Parents Inland/Bush Fit (P)"** (open, cosmetic). It is easily confused with score column P; rename it at the next workbook change.
- **`.claude/handoffs/` is gitignored on the branch** (commit 68edd94). This handoff won't travel via git; the user pastes the prompt file instead.
- **Price lookups.**
  - OnTheHouse now labels figures "median value", not "sale median"; record the basis exactly.
  - The user rejected WebFetch on hand-built OnTheHouse URLs. Use only links returned by search; Statement of Information PDFs give suburb medians.
  - The Clayton South OnTheHouse page returned no figures.

## Verified data
ABS 2021 GCP DataPack, SAL VIC (G01/G02/G08/G09G/G14). The figures match the workbook for Glen Waverley and Berwick. The full 13-suburb table is in the prompt file. Headline shares:

| Suburb | India-born (AQ) | Other language at home (AU) |
|---|---|---|
| Springvale | 7.4% | 76% |
| Tarneit | 28.8% | 64% |
| Clayton South | 14.9% | 67% |
| Clayton | 16.4% | 64% |
| Clyde North | 18.2% | 54% |
| Keysborough | 6.6% | 61% |
| Noble Park | 9.8% | 64% |
| Point Cook | 14.9% | 51% |
| Mount Waverley | 6.1% | 50% |
| Wheelers Hill | 4.1% | 46% |
| Wantirna South | 4.7% | 44% |
| Endeavour Hills | 4.6% | 51% |
| Rowville (reference) | 3.2% | 32% |

Price: only Springvale is done. OnTheHouse median value as at 30 Sep 2026: houses $877,575, units $614,963.

Drive times: all unchecked; the recall estimates are in the prompt.

## Next steps
1. **User:** fast-forward the folder.
   ```
   cd "/Users/okgoogle13/Projects/Parents Melbourne MOVE"
   git fetch origin
   git merge --ff-only origin/claude/ecstatic-tesla-pzbg1v
   ```
2. **User:** paste the prompt file into the cloud session.
3. **Cloud session:**
   - C3: 13 changes, then recalc; the pointer gets top-15 diversity shares; fix the AK–AW comments; Chrome Task 7 gets church.
   - Q13d: add it to the questionnaire HTML and republish to the same URL.
   - Comparator research: prices, drive times, filters, and both-evidence.
   - STOP and present Output 1 and Output 2.
4. **User:** approve the comparator list and the band thresholds.
5. **Cloud session, after approval:**
   - Archive the workbook.
   - Add the comparator rows (C = Community comparator), the band column, DiscussionSummary changes, and the Q13d rows in RawResponses and CleanedAnswers.
   - Recalc: 0 errors, and existing X/Y unchanged.
   - Update the pointer and open-work files, then push.
6. **User:** fast-forward the folder again.

## Files touched
- `Prompt — C3 correction and community comparators (for cloud session, 28 Oct 2026).md`: new. The corrective prompt, with all decisions, the ABS table, the two output formats and the balanced Q13d wording.
- `.claude/handoffs/LATEST.md` and `HANDOFF_*.md`: this handoff.
- `.git/objects/maintenance.lock`: moved to `.git/stale-maintenance-lock-20261027`; it was left by `git fetch` and couldn't be deleted.
- No workbook, pointer or open-work changes in this session.

## Open questions
- Band thresholds: the interim proposal needs the user to confirm it.
- Whether the Community band should ever carry weight. It is display-only by decision for now.
- How Q13d answers will be used once collected.
- Viewing quota: "at least 2 Community comparators" is a proposal; the family hasn't confirmed it.
