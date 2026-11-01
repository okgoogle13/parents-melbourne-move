# Questionnaire redesign — round 9: short survey (1 Nov 2026)

Design record for survey **code version 16** ("v16 short survey"). Requested by the user 1 Nov 2026: "Republish a short 10-question survey, but retain 1 question re: nature." Supersedes round 8 (v14/v15) for what is asked; round 8 answers and tags stay in the data.

**Status:** published 1 Nov 2026 to the existing artifact URL (version id 1793528975-9715; sharing: anyone with the link, so no sign-in needed to answer). Link NOT yet sent. **The model is unchanged:** no change to weights, filters, shortlist status, scores or the Mum/Dad/Nish voting.

## Why

- The parents' WhatsApp of 1 Nov 2026 already answered many v15 items (house features; close to Indian shops and restaurants; Tecoma ruled out on demographics; liked 5 Northam St; want to move soon), and the 15–20 minute survey was causing friction.
- The user wants one nature question kept, to capture Nish's own view and a possible Mum/Dad difference.

## Question set (6 parts, about 11 questions + 10 priority ratings, about 5–8 minutes)

| Part | Tag | Question | Status |
|---|---|---|---|
| 1 Money and timing | Q3c | Budget up to $1.5m right? Help adds: typical Glen Waverley house about $1.68m over the past year (realestate.com.au median $1,675,000, workbook G7, 29 Oct 2026, Checked) | Kept; help line new |
| | R10.3 | Look at homes in a few different areas before buying? A yes even if 2–3 months / B only a few weeks / C no, buy as soon as we find a good home | New |
| 2 Drives | R5.2 | Longest drive to Glen Waverley | Kept |
| | R5.4 | Longest drive to 24-hour ED | Kept |
| 3 Indian shops and community | R10.1 | How close Indian grocery and restaurants need to be: A walking / B 5 / C 10 / D 20 / E 30 min drive | New |
| | R5.5 | Place gone to most often; choice A (Indian grocery) hidden because R10.1 now covers shops | Kept, A hidden |
| | R5.6, R5.7 | Drive to that place; which church | Kept (same skip logic) |
| 4 Nature and kinds of area | R8.1 | Kind of nature most wanted (G = none matters much) | Kept: the one nature question |
| | R10.2 | Kinds of area happy to go and look at: tick any of the five round 8 cards (A–E) or F none; stored as the chosen option texts joined by "; ", sent as letters (e.g. ACD) | New (replaces R8.4/R8.5) |
| 5 The home and later on | R6.1 | Least separation for Nish's space (always asked; Q7a cut) | Kept |
| | Q14 | If driving became hard | Kept |
| 6 Priorities | Q15.1–Q15.10 | Same ten ratings, same scale and "no more than two Top priority" rule | Kept |
| | R10 Notes | Anything else (optional) | New |

**Cut** (earlier answers stay in the data): Q7a, R8.2–R8.6, R8.3 ladder (R8.3-30/20/45/60/75, R8.3, R8.3c), Q11, Q12, Q13 and notes, R5 Notes, R6.2–R6.6 and R6 Notes, R9.1–R9.4 and R9 Notes, Q15 Notes.

House features from the WhatsApp (3/4 bed, 2.5 bath, no weatherboard, heating/cooling, double glazing preferred, double garage with internal access preferred, covered outdoor area with room for an outdoor cooking area, small yard fine) are **property search criteria**, not survey items.

## Import (task N3)

- `tools/import_v14.py` now accepts versions 14, 15 and 16. For v16 it writes only the kept tags plus R10.1, R10.2, R10.3, R10 Notes (new RawResponses columns, added after R9 Notes). Round 8 and timing columns that v16 doesn't ask are carried forward (blanked with `--blank-context`); no R8.6 or R9 flags for v16.
- Tested 1 Nov 2026 on a temp copy with a synthetic Dad v16 record: 23 answers written; LibreOffice recalc 0 errors, 51 ranked rows. Input workbook untouched.
- Known limit: the CleanedAnswers code column for R10.2 takes only the first letter (LEFT); read the answer column for all ticked areas.
- New items (R10.1–R10.3) feed no weight, filter or score. Using them needs a separate model change and approval.

## Checks run (1 Nov 2026, headless browser at 390 px, `#test`)

Full fill → WhatsApp text → import round trip identical apart from notes newlines (by design); a v15 message is rejected; R10.2 "AF" (area plus None) rejected; ticking None clears other areas and vice versa; draft restore keeps ticked areas; R5.5 = None stores R5.6/R5.7 "Not applicable"; no sideways scroll; no console errors. Progress shows 20 required at start (22 if church chosen).
