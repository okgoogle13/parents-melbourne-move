# Model spec D1: scenario weights, community rule, impact (10 Nov 2026)

Status: **draft for approval**. Display-only analysis from a recalculated temp copy of the workbook after N3b/N4 (commit `47fa215`; 0 errors, 37 ranked). No weight, filter, status or formula was changed. Adopting any scenario needs the user's explicit approval (weights are a gated item).

## Goal
Show how much the top 10 depends on whose weights are used, test the proposed community rule, and show what the grocery filter excludes.

## Method
- Scores M–V are taken as they are (recalculated values). Only the weights on them change: X = sum of score × weight. The family-set scenario reproduces the workbook's X for all 51 scored rows (0 mismatches), so the other scenarios use the same arithmetic.
- Survey weights follow the workbook's own rule: level points A=0, B=1, C=2, D=4, each person's points normalised, then averaged (`PriorityWeights`, `Settings!B2:B4` say = 1/1/1).
- Ranks are among the 37 rows that pass L and the grocery filter (Y). Basis: **Estimate** (judgement scores N, P–S, U, V are not all Checked).

## Scenarios (weights, %)
Survey scenarios use **v18 answers only**. v18 dropped Q15.3 (Indian community) and Q10–Q13, so the earlier workbook copied old answers forward; that was removed on 10 Nov (pointer change log). The Indian-community priority is now each person's highest C1–C4 rating.

| Priority | S1 Family-set (live) | S2 Survey v18, all equal say | S3 Survey v18, parents only | S4 Equal |
|---|---|---|---|---|
| Near family in GW | 5.0 | 7.8 | 11.7 | 10 |
| Nature | 10.0 | 15.8 | 12.7 | 10 |
| Hospital | 15.0 | 11.5 | 11.7 | 10 |
| Indian community | 15.0 | 11.5 | 11.7 | 10 |
| Shops & doctor | 15.0 | 11.5 | 11.7 | 10 |
| Village character | 5.0 | 3.0 | 4.5 | 10 |
| Train/bus | 15.0 | 11.5 | 11.7 | 10 |
| Price | 1.0 | 8.4 | 12.7 | 10 |
| Beach | 15.0 | 9.8 | 3.6 | 10 |
| City trip | 4.0 | 9.1 | 8.1 | 10 |

Biggest gaps between the family-set weights and the survey: Price (1% vs 8–13%), Beach (15% vs 3.6–10%), Nature (10% vs 13–16%), Near family in GW (5% vs 8–12%).

## Result 1: top 10 (37 ranked)
| Scenario | Overlap with live top 10 | Top 10 in order |
|---|---|---|
| S1 Family-set | 10 | Frankston, Berwick, West Footscray, Newport, Seaford, Altona, Heidelberg, Mentone, Ringwood, Rosanna |
| S2 Survey, equal say | 7 | Frankston, Berwick, Seaford, Ferntree Gully, Newport, Ringwood, Rosanna, West Footscray, Upwey, Upper Ferntree Gully |
| S3 Survey, parents only | 6 | Frankston, Berwick, Ringwood, Ferntree Gully, Croydon, Seaford, Upwey, Upper Ferntree Gully, Rosanna, Newport |
| S4 Equal | 8 | Frankston, Berwick, Newport, Seaford, West Footscray, Upwey, Ferntree Gully, Altona, Ringwood, Rosanna |

- **Stable:** Frankston #1 and Berwick #2 in every scenario; Seaford, Ringwood and Rosanna stay in the top 10 in all four.
- **Weight-sensitive:** Altona, Heidelberg and Mentone (live #6–8) drop to about #12–19 under survey weights; West Footscray falls from #3 to #8–11; Ferntree Gully (live #11) rises to #4. Hills suburbs (Ferntree Gully, Upwey, Upper Ferntree Gully, Croydon) gain; bayside and inner-west suburbs lose.
- Reason: the live weights give Beach 15% and Price 1%; coastal suburbs score high on Beach, and the survey weights give Beach less and Price much more.

## Result 2: parents' limits (GW ≤ 25, ED ≤ 20; 15 suburbs, as N4)
Top 5 among those 15: S1 Frankston, Berwick, Seaford, Heidelberg, Mentone. S2: Frankston, Berwick, Seaford, Ferntree Gully, Ringwood. S3: Frankston, Berwick, Ringwood, Ferntree Gully, Croydon. S4: Frankston, Berwick, Seaford, Upwey, Ferntree Gully. The top 2 hold under every scenario; places 3–5 depend on the weights.

## Result 3: community rule (adopted in the workbook 10 Nov as the way to avoid the stale Q15.3)
- Each person's highest C1–C4 rating is their Indian-community priority: Mum C, Dad B, Nish C (Nish's old Q15.3 answer was B). Effect on S2: Indian community 9.8% → 11.5%; top-10 membership unchanged, one or two neighbouring ranks swap. S3 (parents only) is unchanged.
- It has no effect while S1 is live (S1 fixes the weight at 15%). The all-"Not needed" case would score 0 for that person; no one chose it, so no default rule was written.
- C1–C4 are mostly B ("nice to have"), which fits the parents' R11.1/R11.2 answers (20–30 min drives).
- Not covered: P itself is unchanged, and the display-only community items (AX, Q13d, comparators) stay out of X and Y.

## Result 4: excluded suburbs (14 scored but not ranked, all "Fails: grocery drive")
If the 25-min grocery filter were off, the best of them would rank (out of 51): Rosebud #26, Dromana #31, Rye #32, McCrae #34 (S1); Rosebud #27, Dromana #32, McCrae #35 (S2); Rosebud #31, Hurstbridge #32, Emerald #34 (S3). None would enter the top 10 or top 25 under any scenario tested. Woodend and Healesville appear in S3 at #40–41. So the grocery filter does not hide a contender; the cutoff question is a values question, not a ranking one.

## Assumptions and what would change them
1. The 37 ranked rows' judgement scores (N, P–S, U, V) are correct enough. If a Nature or Village score moves a point, ranks 6–20 shuffle; ranks 1–2 would not.
2. Survey codes are the v18 answers (Q15.1, Q15.2, Q15.4–Q15.10 and C1–C4, checked against the export). Verified 10 Nov: Q15.3 and Q10–Q13 were the only weight-feeding answers v18 did not ask, and they are now blank in rows 17–19. Other unasked context answers (Q1–Q9, Q13b/c, R5.1/R5.3, R6.7, Q16–Q21, round 8 and timing columns) are still carried forward; they feed no weight, filter or score.
3. Equal 10% (S4) is a reference point, not a proposal.
4. Scenario weights ignore the old forced-choice corrections (column C of `ForcedChoiceCorrections`), which no longer feed B.

## Recommendation (your decision)
1. **Keep S1 as the live weights** unless you want price and beach weighted as the survey says. If so, S2 is the least arbitrary alternative (equal say, as `Settings` already has it); S3 shows what the parents alone would choose. Pick on whether 1% for Price is deliberate: the two parents' survey answers give it 8–13%.
2. The community rule is already in the workbook's survey-weight side and does not touch the live weights.
3. **Do not treat the top 10 as settled** beyond Frankston and Berwick until the weight question is answered; use the viewing-shortlist rule (≥2 comparators, ≥1 anchor, ≥1 Potential-both) to hedge.
4. G3 (M/O decoupling, Settings B38/B39 = 90) does not depend on this choice and can go ahead on its own approval.

## Not done
- No sensitivity test on individual judgement scores or on the beach bands (Filters A15:C21).
- No test of changing the 25-min grocery limit (15 and 30 are shown in the workbook as backups).
- The scenario script lives in the session scratchpad and is not saved in the repo. Numbers are reproducible from the formulas above.
