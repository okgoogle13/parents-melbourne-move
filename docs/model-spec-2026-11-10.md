# Model spec D1: scenario weights, community rule, impact (10 Nov 2026)

Status: **draft for approval**. Display-only analysis from a recalculated temp copy of the workbook after N3b/N4 (commit `47fa215`; 0 errors, 37 ranked). No weight, filter, status or formula was changed. Adopting any scenario needs the user's explicit approval (weights are a gated item).

## Goal
Show how much the top 10 depends on whose weights are used, test the proposed community rule, and show what the grocery filter excludes.

## Method
- Scores M–V are taken as they are (recalculated values). Only the weights on them change: X = sum of score × weight. The family-set scenario reproduces the workbook's X for all 51 scored rows (0 mismatches), so the other scenarios use the same arithmetic.
- Survey weights follow the workbook's own rule: level points A=0, B=1, C=2, D=4, each person's points normalised, then averaged (`PriorityWeights`, `Settings!B2:B4` say = 1/1/1).
- Ranks are among the 37 rows that pass L and the grocery filter (Y). Basis: **Estimate** (judgement scores N, P–S, U, V are not all Checked).

## Scenarios (weights, %)
| Priority | S1 Family-set (live) | S2 Survey, all equal say | S3 Survey, parents only | S4 = S2 + community rule | S5 = S3 + community rule | S6 Equal |
|---|---|---|---|---|---|---|
| Near family in GW | 5.0 | 7.8 | 11.7 | 7.8 | 11.7 | 10 |
| Nature | 10.0 | 16.3 | 12.7 | 15.8 | 12.7 | 10 |
| Hospital | 15.0 | 11.7 | 11.7 | 11.5 | 11.7 | 10 |
| Indian community | 15.0 | 9.8 | 11.7 | 11.5 | 11.7 | 10 |
| Shops & doctor | 15.0 | 11.7 | 11.7 | 11.5 | 11.7 | 10 |
| Village character | 5.0 | 3.0 | 4.5 | 3.0 | 4.5 | 10 |
| Train/bus | 15.0 | 11.7 | 11.7 | 11.5 | 11.7 | 10 |
| Price | 1.0 | 8.4 | 12.7 | 8.4 | 12.7 | 10 |
| Beach | 15.0 | 10.2 | 3.6 | 9.8 | 3.6 | 10 |
| City trip | 4.0 | 9.3 | 8.1 | 9.1 | 8.1 | 10 |

Biggest gaps between the family-set weights and the survey: Price (1% vs 8–13%), Beach (15% vs 3.6–10%), Nature (10% vs 13–16%).

## Result 1: top 10 (37 ranked)
| Scenario | Overlap with live top 10 | Top 10 in order |
|---|---|---|
| S1 Family-set | 10 | Frankston, Berwick, West Footscray, Newport, Seaford, Altona, Heidelberg, Mentone, Ringwood, Rosanna |
| S2 Survey, equal say | 7 | Frankston, Berwick, Seaford, Newport, Ferntree Gully, Ringwood, Upwey, Rosanna, Upper Ferntree Gully, West Footscray |
| S3 Survey, parents only | 6 | Frankston, Berwick, Ringwood, Ferntree Gully, Croydon, Seaford, Upwey, Upper Ferntree Gully, Rosanna, Newport |
| S4 S2 + community rule | 7 | Frankston, Berwick, Seaford, Ferntree Gully, Newport, Ringwood, Rosanna, West Footscray, Upwey, Upper Ferntree Gully |
| S5 S3 + community rule | 6 | same as S3 |
| S6 Equal | 8 | Frankston, Berwick, Newport, Seaford, West Footscray, Upwey, Ferntree Gully, Altona, Ringwood, Rosanna |

- **Stable:** Frankston #1 and Berwick #2 in every scenario; Seaford, Ringwood and Rosanna stay in the top 10 in all six.
- **Weight-sensitive:** Altona, Heidelberg and Mentone (live #6–8) drop to #12–19 under survey weights, and Ferntree Gully (live #11) rises to #4–5. West Footscray falls from #3 to #10–11 under S2/S3. Hills suburbs (Ferntree Gully, Upwey, Upper Ferntree Gully, Croydon) gain; bayside and inner-west suburbs lose.
- Reason: the live weights give Beach 15% and Price 1%; coastal suburbs score high on Beach, and the survey and parents-only weights give Beach little weight and Price a lot.

## Result 2: parents' limits (GW ≤ 25, ED ≤ 20; 15 suburbs, as N4)
Top 5 among those 15: S1 Frankston, Berwick, Seaford, Heidelberg, Mentone. S2, S4 and S6: Frankston, Berwick, Seaford, then Ferntree Gully (or Upwey in S6). S3, S5: Frankston, Berwick, Ringwood, Ferntree Gully, Croydon. So the top 2 hold under every scenario; places 3–5 depend on the weights.

## Result 3: community rule (proposal: use each person's highest C1–C4 rating as the Indian-community priority signal; all "Not needed" → defaults)
- Highest ratings: Mum C, Dad B, Me C. The current Q15 codes are Mum C, Dad B, Me **B**, so only Nish's signal moves (B→C).
- Effect: Indian community weight 9.8% → 11.5% in S2/S4. In the parents-only case (S3/S5) nothing changes (Mum and Dad's signals are the same). Top-10 membership is unchanged; one or two neighbouring ranks swap (e.g. Ferntree Gully #5→#4, West Footscray #10→#8).
- Under S1 the rule has no effect, since S1 fixes the weight at 15%.
- Judgement: the rule is low-stakes. It is cheap to adopt but changes nothing material. C1–C4 are mostly B ("nice to have"), which fits the parents' R11.1/R11.2 answers (20–30 min drives) rather than a strong community pull.
- Not covered: P itself (the 0.5/0.5 blend of grocery drive and Indian ancestry share) is unchanged, and the display-only community items (AX, Q13d, comparators) stay out of X and Y.

## Result 4: excluded suburbs (14 scored but not ranked, all "Fails: grocery drive")
If the 25-min grocery filter were off, the best of them would rank (out of 51): Rosebud #26, Dromana #31, Rye #32, McCrae #34 (S1); Rosebud #27, Dromana #32, McCrae #35 (S2); Rosebud #31, Hurstbridge #32, Emerald #34 (S3). None would enter the top 10 or top 25 under any scenario tested. Woodend and Healesville appear in S3 at #40–41. So the grocery filter does not hide a contender; the cutoff question is a values question, not a ranking one.

## Assumptions and what would change them
1. The 37 ranked rows' judgement scores (N, P–S, U, V) are correct enough. If a Nature or Village score moves a point, ranks 6–20 shuffle; ranks 1–2 would not.
2. Survey codes in `CleanedAnswers` rows 19–28 are the current priority answers. I did not verify that v18 re-asked the priority questions rather than carrying old answers forward; survey scenarios S2–S5 are only as current as those cells.
3. Equal 10% (S6) is a reference point, not a proposal.
4. Scenario weights ignore the old forced-choice corrections (column C of `ForcedChoiceCorrections`), which no longer feed B.

## Recommendation (your decision)
1. **Keep S1 as the live weights** unless you want price and beach weighted as the survey says. If so, S2 is the least arbitrary alternative (equal say, as `Settings` already has it). Pick on whether 1% for Price is deliberate: the two parents' survey answers give it 8–13%.
2. **Adopt the community rule** only if you want survey weights back; it has no effect while S1 is live.
3. **Do not treat the top 10 as settled** beyond Frankston and Berwick until the weight question is answered; use the viewing-shortlist rule (≥2 comparators, ≥1 anchor, ≥1 Potential-both) to hedge.
4. G3 (M/O decoupling, Settings B38/B39 = 90) does not depend on this choice and can go ahead on its own approval.

## Not done
- No sensitivity test on individual judgement scores or on the beach bands (Filters A15:C21).
- No test of changing the 25-min grocery limit (15 and 30 are shown in the workbook as backups).
- The scenario script lives in the session scratchpad and is not saved in the repo. Numbers are reproducible from the formulas above.
