# Follow-up: comparator fixes after review (28 Oct 2026)

Work on branch `claude/ecstatic-tesla-pzbg1v`. The user's folder has merged this branch up to 7de29d5.

Same hard rules as before:
- Don't change family weights, the Filters tab or P.
- Keep checked facts and estimates separate.
- Every source goes in column Z.
- Archive the workbook before editing: `Archive/… (superseded 2026-10-28, before comparator fixes).xlsx`.

## 1. Glen Waverley drive basis (J) for rows 67–72

**Problem:** J holds the top of the **08:00** range, but every other row uses the midday "leave now" basis from the Filters tab. Springvale shows 35 min against Mordialloc's 28, although off-peak it is 10–26.

**Fix:**
- Set J67–J72 to the **top of the 10:00 range** you already checked:

  | Row | Suburb | J |
  |---|---|---|
  | 67 | Springvale | 26 |
  | 68 | Clayton South | 35 |
  | 69 | Keysborough | 24 |
  | 70 | Clyde North | 50 |
  | 71 | Endeavour Hills | 26 |
  | 72 | Wheelers Hill | 12 |

  Check each figure against the evidence table in `Community comparators — research (28 Oct 2026).md` before writing.
- Keep the 08:00 range in Z, labelled "peak (08:00), not used in J".
- Update the DiscussionSummary text if it quotes the 08:00 figures as the main drive.

## 2. Tarneit: excluded by family decision

The family has decided to **exclude Tarneit**. Don't add it to the scorecard.

In DiscussionSummary and in the research doc:
- Change the Tarneit reason to: "Excluded — family decision 28 Oct 2026 (stated reasons: safety concerns and not enough going for it)."
- Remove the peak-drive test as the reason. Tarneit passes the 90-min cap at 10:00 (50–80 min), so the 08:00 figure must not read as a filter failure.
- Don't add crime statistics or any claim about crime levels. The reason is recorded as the family's stated view, not a checked fact.

Point Cook stays "Conditional" (family decision on distance), unchanged.

## 3. Community band (AX) on every row

- Fill the AX formula down every SuburbScorecard row that has AU data. That means the 51 passing rows, the other non-passing candidate rows and rows 67–72; skip the 2 synthetic test rows.
- Leave AX blank where AU is blank.
- AX stays display-only: no reference to it from X, Y or any weight.
- In the pointer, add a one-line count of High / Medium / Low among the 51 passing rows, and the same count for the current top 15.

## 4. Add Q13d to RawResponses and CleanedAnswers

- Add Q13d as a new question row in CleanedAnswers, with Mum/Dad/Me answer cells empty until responses arrive. Add the matching column or row in RawResponses, following the sheet's existing layout.
- It must not feed ForcedChoiceCorrections, PriorityWeights or any formula.
- Record the scale (A strongly … B strongly) in a cell note.

## 5. Verify, log, push

- Recalc a copy with `recalc.py`: 0 errors.
- Diff before and after. Only these may have changed:
  - J67–J72 and the M/O values that depend on them (rows 67–72 stay unranked: X blank, Y blank);
  - Z67–Z72;
  - AX cells;
  - the Q13d rows;
  - DiscussionSummary text.
- **X/Y for rows 2–66 must not move.**
- Update `scoring-model-pointer.md` (change-log entry) and the open-work file.
- Commit and push to `claude/ecstatic-tesla-pzbg1v`.
- Then tell the user to merge the branch into their folder again.

## Report back, briefly
- The new J values.
- The AX counts for the passing rows and the top 15.
- Confirmation that X/Y are unchanged.
- Anything still an estimate.
