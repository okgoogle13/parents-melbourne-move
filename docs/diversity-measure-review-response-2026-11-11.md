# Response to the Argon diversity review, and what D2 adopted (11 Nov 2026)

Reviews answered: `docs/diversity-measure-review-gemini-4-argon-2026-11-10.md` (Argon), and Gemini's follow-up plan for exact SAL extraction (Antigravity `implementation_plan.md`, 11 Nov). Decisions are the user's (11 Nov), recorded in `Family conversations — before parents leave (Nov 2026).md` D-1 to D-7.

## Applied (D2, workbook sha `062052d7bcde`, pre-change copy `Archive/… (superseded 2026-11-11, before D2 community score P).xlsx`)
P = 50% food access (Indian grocery AY 35% + Indian restaurant AZ 15%; grocery stands in while AZ is blank) + 35% mix of cultures (AU: 0 at 5%, 10 at 20%) + 15% South Asian share (MAX(AQ, AR): 10 at 8%). Parameters: `Filters!A22:C29`. No hard filter.

## Point by point
| Review point | Verdict | Reason |
|---|---|---|
| No hard filter; diversity as a continuous part of P | Adopted | D-1: a strong preference, not a must |
| Cut the India-born term, use MAX(AQ, AR) | Adopted | D-2: Indian neighbours not the deciding factor; ancestry counts second-generation families |
| Parameters on Filters, Excel-compatible formula | Adopted | Same pattern as the beach bands (A15:C21) |
| Never substitute SA2 figures for suburb (SAL) figures | Adopted as a rule | The review's own checks: Upper Ferntree Gully and Berwick are off by 7–10 points at SA2 |
| 50/35/15 "derived from the survey" | Adopted as a judgement, not a derivation | The C1–C4 tally gives 50/29/21. 35/15 follows D-2 |
| Full marks at 30% "anchored to Greater Melbourne" | Rejected; full marks at 20% | 30% is Greater Melbourne's M3 (29.4%), not its AU (34.3%), and matches AX's interim "Medium" line. The family said a Ferntree Gully-level mix (AU 18.7%) is enough (D-3) |
| AU/(1−AP) stated-response correction | Rejected | AP is birthplace not stated, not language not stated. Without a filter, a 1-point shift moves X by about 0.02 |
| Italian/Greek speakers are "false positives"; score non-European diversity | Rejected | D-7: the parents like and value Southern European cultures, so AU counting them is correct |
| M3 (born overseas outside the main English-speaking countries) as the target measure | Kept as optional D2b, for a different reason | M3 keeps Italy- and Greece-born. Its value is counting English-speaking non-Anglo migrants (India, Sri Lanka, Philippines) that AU misses |
| "[Checked]" labels on post-2021 migration, NOM figures, design effect 2.5, confidence intervals, Heidelberg's and Rosanna's 15.0% non-European share | Downgraded to Estimate / recall | Not checked. Heidelberg and Rosanna share one SA2, so their identical figure breaks the review's own SA2 warning. Not used in col Z or reports |
| AX band rewrite, enclave cap, LBOTE/NOM adjustments, prudence triggers | Not adopted (scope) | AX is display-only; no ranked suburb is near enclave levels |
| §8 family questions | Q1 and Q2 answered by the user; Q3 moot (no filter); Q4 (Berwick north vs south) moved to property search (SL2) | |

## Gemini's 11 Nov extraction plan
- **Kept (task D2b):** a script that reads the ABS 2021 GCP SAL/GCCSA tables (G01, G09A–H, G13A–E) and writes `research/abs/sal_diversity_gcp_2021.csv`. Raw files are committed beside it. Before use, the values must reproduce workbook AL, AO, AU and AQ for all 69 rows within 0.1 point. The country list must include Northern Ireland, which Gemini's 9-country list omits.
- **Rejected:**
  - its 40/40/20 split, which raises the India-born term against D-2 and D-6;
  - the non-European options, against D-7;
  - full marks at the Greater Melbourne average;
  - saving cached values into the canonical workbook, against the recalc rule in `CLAUDE.md`;
  - a P formula that goes blank when the new column is blank;
  - notes for an "Instructions" tab that does not exist.
- Its rank table has duplicate ranks and is not used.

## Result (recalculated temp copy; 0 errors, 51 X numeric, 37 ranked)
New top 10: Frankston, Berwick, Ferntree Gully, Newport, Ringwood, Seaford, Rosanna, Croydon, West Footscray, Altona. Upper Ferntree Gully (10→12) and Upwey (9→13) leave it; Croydon (11→8) and Altona (13→10) join. Moves of 3+ places: Seaford 3→6, Upwey 9→13, Croydon 11→8, Altona 13→10. Figures: `scoring-model-pointer.md` change log, 11 Nov.

## Known limits
- AU misses English-speaking non-Anglo households. MAX(AQ, AR) covers this for Indian families; D2b would cover more.
- No adjustment for the 2021 Census being taken in lockdown.
- Comparators have no AY, so their P stays blank.
