# Model spec D1: scenario weights, community rule, impact (10 Nov 2026)

Status: **S2 adopted 10 Nov 2026 (user-approved)**: live weights `ForcedChoiceCorrections!B6:B15` now = D (survey v18, equal say); workbook sha `1ebecdf1d816`, recalc OK, 0 errors, 37 ranked. The diversity filter below is a **draft, not applied** (needs approval). Scenario figures are from a recalculated temp copy after the 10 Nov stale-answer cleanup (`2a20168`).

## Goal
Show how much the top 10 depends on whose weights are used, test the proposed community rule, and show what the grocery filter excludes.

## Method
- Scores M–V are taken as they are (recalculated values). Only the weights on them change: X = sum of score × weight. The family-set scenario reproduced the pre-change workbook's X for all 51 scored rows (0 mismatches), and S2 reproduces the current X, so the other scenarios use the same arithmetic.
- Survey weights follow the workbook's own rule: level points A=0, B=1, C=2, D=4, each person's points normalised, then averaged (`PriorityWeights`, `Settings!B2:B4` say = 1/1/1).
- Ranks are among the 37 rows that pass L and the grocery filter (Y). Basis: **Estimate** (judgement scores N, P–S, U, V are not all Checked).

## Scenarios (weights, %)
Survey scenarios use **v18 answers only**. v18 dropped Q15.3 (Indian community) and Q10–Q13, so the earlier workbook copied old answers forward; that was removed on 10 Nov (pointer change log). The Indian-community priority is now each person's highest C1–C4 rating.

| Priority | S1 Family-set (live until 10 Nov) | S2 Survey v18, all equal say | S3 Survey v18, parents only | S4 Equal |
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
| Scenario | Overlap with S1 top 10 | Top 10 in order |
|---|---|---|
| S1 Family-set (live until 10 Nov) | 10 | Frankston, Berwick, West Footscray, Newport, Seaford, Altona, Heidelberg, Mentone, Ringwood, Rosanna |
| S2 Survey, equal say (**live from 10 Nov**) | 7 | Frankston, Berwick, Seaford, Ferntree Gully, Newport, Ringwood, Rosanna, West Footscray, Upwey, Upper Ferntree Gully |
| S3 Survey, parents only | 6 | Frankston, Berwick, Ringwood, Ferntree Gully, Croydon, Seaford, Upwey, Upper Ferntree Gully, Rosanna, Newport |
| S4 Equal | 8 | Frankston, Berwick, Newport, Seaford, West Footscray, Upwey, Ferntree Gully, Altona, Ringwood, Rosanna |

- **Stable to weights:** Frankston #1 and Berwick #2 in every scenario; Seaford, Newport, Ringwood and Rosanna stay in the top 10 in all four. Not stable to judgement scores: see Assumption 1.
- **Weight-sensitive:** Altona, Heidelberg and Mentone (S1 #6–8) drop to about #12–19 under survey weights; West Footscray falls from #3 to #8–11; Ferntree Gully (S1 #11) rises to #4. Hills suburbs (Ferntree Gully, Upwey, Upper Ferntree Gully, Croydon) gain; bayside and inner-west suburbs lose.
- Reason: the family-set weights give Beach 15% and Price 1%; coastal suburbs score high on Beach, and the survey weights give Beach less and Price much more.

## Result 2: parents' limits (GW ≤ 25, ED ≤ 20; 15 suburbs, as N4)
Top 5 among those 15: S1 Frankston, Berwick, Seaford, Heidelberg, Mentone. S2: Frankston, Berwick, Seaford, Ferntree Gully, Ringwood. S3: Frankston, Berwick, Ringwood, Ferntree Gully, Croydon. S4: Frankston, Berwick, Seaford, Upwey, Ferntree Gully. The top 2 hold under every scenario; places 3–5 depend on the weights.

At GW ≤ 35 (P11 #1: "35 mins would be OK for the right place"), ED ≤ 20: **27 suburbs**. Top 5: S1 Frankston, Berwick, Newport, Seaford, Altona. S2: Frankston, Berwick, Seaford, Ferntree Gully, Newport. S3: Frankston, Berwick, Ringwood, Ferntree Gully, Croydon.

## Result 3: community rule (adopted in the workbook 10 Nov as the way to avoid the stale Q15.3)
- Each person's highest C1–C4 rating is their Indian-community priority: Mum C, Dad B, Nish C (Nish's old Q15.3 answer was B). Effect on S2: Indian community 9.8% → 11.5%; top-10 membership unchanged, one or two neighbouring ranks swap. S3 (parents only) is unchanged.
- With S2 live, the rule now feeds the live Indian-community weight (11.5%). The all-"Not needed" case scores 0 for that person; all four C answers blank gives #N/A in `PriorityWeights` row 4. No one has either, so no default rule was written.
- C1–C4 are mostly B ("nice to have"), which fits the parents' R11.1/R11.2 answers (20–30 min drives).
- Not covered: P itself is unchanged, and the display-only community items (AX, Q13d, comparators) stay out of X and Y.

## Result 4: excluded suburbs (14 scored but not ranked, all "Fails: grocery drive")
If the 25-min grocery filter were off, the best of them would rank (out of 51): Rosebud #26, Dromana #31, Rye #32, McCrae #34 (S1); Rosebud #28, Dromana #34, McCrae #36 (S2); Rosebud #31, Hurstbridge #32, Emerald #34 (S3). None would enter the top 10 or top 25 under any scenario tested. Woodend and Healesville appear in S3 at #40–41. So the grocery filter does not hide a contender; the cutoff question is a values question, not a ranking one.

## Draft: "a diverse multicultural area is a must" (P11 #8; **not applied**, needs approval)
**Superseded 10 Nov (phone call, `Family conversations…md` D-1 to D-6):** diversity is a strong preference, not a must; Dad doesn't care much; "mix of many cultures"; Tecoma too white, Ferntree Gully-level mix is OK; shops and food matter more than who lives there. **No hard filter recommended.** Diversity moves to D2 (a component of the community score P). The options below are kept for the record.

**Measure.** % of people using a language other than English at home (SuburbScorecard AU, ABS 2021 Census, suburb level; **Checked** as data, the cut-off is a proposal). AU counts every language, so it fits "diverse multicultural" better than India-born (AQ, which P already uses) or born overseas (AO, which counts UK and NZ-born and is high in the hills). Mum's own test case (31 Oct WhatsApp): Tecoma, "almost 100% white (gone)", AU 4.5%.

| Option | Rule | Ranked suburbs kept (of 37) | Leaves the S2 top 10 |
|---|---|---|---|
| **A (my pick)** | AU ≥ 10% | 16 | Seaford (9.6%), Upwey (6.3%), Upper Ferntree Gully (8.3%) |
| B | AU ≥ 15% | 11 | as A, plus Frankston (12.1%) |
| C | Community band AX Medium or High (AU ≥ 30% or India-born ≥ 4%) | 3: Berwick, Ringwood, West Footscray | 7 of 10 |

- Under A the top 10 becomes Frankston, Berwick, Ferntree Gully, Newport, Ringwood, Rosanna, West Footscray, Croydon, Heidelberg, Altona. Also out: Belgrave, Tecoma, Frankston South, Diamond Creek, Warragul, Newtown, The Basin, Mornington, Montrose, Mount Evelyn, Torquay, Drouin, Sassafras, Gisborne, Olinda, Mount Dandenong, Riddells Creek, Macedon.
- **Why A, and its limit.** A removes the Tecoma-like suburbs the family named and keeps the nature-first anchor Frankston. It is a floor, not proof of "multicultural": 16 suburbs at 10–36% are still well below the six Community comparators (AU 46–76%). The Greater Melbourne figure is **Needs data** (check ABS 2021 QuickStats, area 2GMEL, before using it as an anchor). Seaford at 9.6% vs a 10% cut-off is within noise; a round-number cut-off is a values choice.
- **The bigger point.** The ranked list was built around nature; the diverse suburbs are the comparators, which are unranked. If "must" means B or C, the comparators should be scored (N, P–S, U, V) and ranked. That is adding locations to the ranked set (C status), a gated change.
- **Data limits.** 2021 Census, suburb-wide averages (a street can differ); ABS perturbs populations under 2,500.

**Where it would live (if approved).** Filters row 14: "Min % other language at home (APPLIED)", B14 = 0.10, C14 = decision note and date. New SuburbScorecard column BL "Diversity filter (applied, Filters B14)": `=IF(AU2="","Needs data",IF(AU2>=Filters!$B$14,"Pass","Fails: diversity"))`. Y adds `BL2<>"Fails: diversity"` to its IF and `BL$2:BL$90,"<>Fails: diversity"` to its COUNTIFS. One DiscussionSummary count row. `CLAUDE.md` says ABS demography (AK–AW) never feeds X or Y; that is already untrue for AQ (feeds P since 2 Nov), so the rule needs rewording for AQ now and for AU under this draft. Check: recalc test, ranked = 16 under A.

## Assumptions and what would change them
1. The 37 ranked rows' judgement scores (N, P–S, U, V) are correct enough. They are Estimates, and ranks 1–2 are **not** robust to them: moving one score (N, P–S, U or V; P and U are formulas, the rest judgement) of one top-3 suburb by ±1 changes #1 or #2 in 9 cases (S1), 8 (S2) and 10 (S3). In S3 a −1 on Frankston's Nature, Indian community, Shops or Train score puts Berwick #1. Ranks 9–12 sit within 0.06–0.2 points of each other. Read the list as "Frankston and Berwick lead", not as fixed ranks.
2. Survey codes are the v18 answers (Q15.1, Q15.2, Q15.4–Q15.10 and C1–C4, checked against the export). Verified 10 Nov: Q15.3 and Q10–Q13 were the only weight-feeding answers v18 did not ask, and they are now blank in rows 17–19. Other unasked context answers (Q1–Q9, Q13b/c, R5.1/R5.3, R6.7, Q16–Q21, round 8 and timing columns) are still carried forward; they feed no weight, filter or score.
3. Equal 10% (S4) is a reference point, not a proposal.
4. Forced-choice corrections (column C of `ForcedChoiceCorrections`) are 0: v18 did not ask Q10–Q13 and the carried-forward answers were blanked on 10 Nov. Before the cleanup they would have moved S2 (Newport #2, Berwick #4, Altona in, Ringwood out).

## Decision (10 Nov 2026) and remaining recommendations
1. **S2 is live** (user-approved 10 Nov). It follows the 10 Nov decision that weights reflect the family's collective survey priorities (`Family conversations — before parents leave (Nov 2026).md`, decisions 1) and P11 #6 (beach lower, with a share kept for Nish). Not modelled: Mum said her beach "Nice to have" is for Nish; setting her beach answer to "Not needed" gives Beach 7.4% and a top 10 9/10 the same as S2 (Ringwood, Croydon, Ferntree Gully up; West Footscray out). That would change her recorded answer, so it needs her own confirmation.
2. The community rule (highest C1–C4) now feeds the live weights.
3. **Do not treat the top 10 as settled**: the weights are now decided, but ranks move with single score changes (Assumption 1); use the viewing-shortlist rule (≥2 comparators, ≥1 anchor, ≥1 Potential-both) to hedge.
4. G3 (M/O decoupling, Settings B38/B39 = 90) does not depend on this choice and can go ahead on its own approval.

## Not done
- Judgement-score sensitivity: tested for #1–#2 only (Assumption 1); no test of the beach bands (Filters A15:C21).
- No test of changing the 25-min grocery limit (15 and 30 are shown in the workbook as backups).
- The scenario script lives in the session scratchpad and is not saved in the repo. Numbers are reproducible from the formulas above.
