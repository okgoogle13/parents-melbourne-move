# Community-fit audit

Read-only audit, 2 Nov 2026. New priority: a multicultural/diverse suburb with nearby Indian groceries and restaurants matters more than a high Indian population.
Files: survey = `Our Next Home — questionnaire page v16 (Claude artifact source).html` (S1–S9); workbook = `Our Next Home — Family Relocation Scoring Model.xlsx` (W1–W27). Workbook read as stored formulas; it holds no cached values, so no number below comes from a recalculation (any computed score is my hand calculation from stored inputs, marked "hand-calc").

## Items

| # | File | Location | What it measures now | Feeds final score? | Problem under the new priority |
|---|---|---|---|---|---|
| S1 | Survey | Q15.3 "Indian/South Asian community" (help: "Indian groceries, restaurants, temple or church, people from our culture") | One 5-level rating bundling groceries, restaurants, temple/church and "people from our culture" | N now. Answers → CleanedAnswers row 21 → PriorityWeights row 4 → ForcedChoiceCorrections D9, which is reference only (B9 = G9 since 2 Nov) | Bundles the new priority (food access) with the old one (people from our culture). One answer cannot tell which the parents mean. Page rule "Top priority for no more than two" makes it compete with the other nine. No item asks about multicultural/diverse mix |
| S2 | Survey | R10.1 "How close do Indian grocery stores and restaurants need to be?" (walking / 5 / 10 / 20 / 30 min) | Required closeness of Indian groceries and restaurants | N. Header comment: "feed no weight, filter or score". No R10.1 column exists in RawResponses/CleanedAnswers yet; `tools/import_v14.py` would add one | Closest match to the new priority, but groceries and restaurants share one answer. Its scale (5/10/20/30) cannot express the 25-min grocery filter already set in the workbook. Not tied to any scorecard column |
| S3 | Survey | R5.5 "Community place used most" (grocery option hidden; temple / church / none) | Which community place they visit most | N. CleanedAnswers row 45, index in row 62; no formula uses either | Grocery was moved to R10.1, so this is now temple/church only. No matching scorecard metric (AZ/BA are empty) |
| S4 | Survey | R5.6 "Longest regular drive to that place" (10/20/30/45 min) | Drive tolerance to the S3 place | N. CleanedAnswers row 46, limit in row 63; unused | Tolerance refers to temple/church, not groceries or restaurants |
| S5 | Survey | R5.7 church denomination | Whether a specific church is needed | N. DiscussionSummary E42:E44 display only | Religious detail, not food or diversity. Needs no change for the new priority; listed because it touches community |
| S6 | Survey | R10.2 area cards A–E (CARDS text, lines 166–170) | Which area types they would view | N. Flagged "feed nothing" | Cards describe shops generically ("big shopping strips", "small village shops"). None says anything about cultural mix or Indian food. Parents cannot choose between area types on the new criterion |
| S7 | Survey | Q15.7 "Shops and doctor nearby" (supermarket, pharmacy, GP) | General shop/GP access | N now (→ PriorityWeights row 8 → FCC D10, reference only) | Generic shopping. Not separated from Indian grocery/restaurants, so the two can be double-counted in the parents' minds |
| S8 | Survey | Q15.8 "Village character" (quiet, friendly village feel) | Village feel | N now (→ PriorityWeights row 9) | Can pull against a multicultural/urban suburb. Not a community item as such; listed because it trades off against it |
| S9 | Survey | Q14 option B "Walk to the shops and doctor" | Later-life reliance on walkable shops | N. CleanedAnswers row 38 → DiscussionSummary only | Marginal: shops/GP, not food or culture |
| W1 | Workbook | SuburbScorecard P (col P, "Score: Indian community"), formula in all 71 rows | 50% grocery-drive score + 50% share born in India | **Y.** Raw score in X (weight 15%) | **Core problem.** Half the score is the Indian-born population share, the old priority |
| W2 | Workbook | SuburbScorecard AQ (% born in India, ABS 2021) | Population share | **Y**, 50% of P: `10*AQ/0.08`, capped at 10 (8% = Glen Waverley) | Old priority. Rewards a high Indian population. Capped at 8%, so any suburb at or above Glen Waverley's level scores the same |
| W3 | Workbook | SuburbScorecard AY (drive to nearest Indian grocery; 10:00 weekday, top of range) | Drive time to one Indian grocery | **Y**, 50% of P: `10*(30-AY)/25`, floor 0; also drives the filter (W4) | Closest to the new priority, but groceries only (no restaurants), nearest one only (no count or variety) and driving only (no walk). Filled for 51 of 71 rows. Blank in 20 rows including Glen Waverley, Blackburn and all 6 community comparators |
| W4 | Workbook | SuburbScorecard BG (grocery filter, "Fails: grocery drive" if AY > Filters B11); BH, BI | Hard pass/fail on AY | **Y.** Y3 rank formula excludes "Fails: grocery drive". BH/BI are display only | Right direction, but AY is counted twice (filter and 50% of P). The cut is 25 min while P reaches 0 at 30 min. The filter uses one grocery and no restaurants |
| W5 | Workbook | Filters B11 = 25, B12 = 15, B13 = 30 (notes C11:C13) | Grocery-drive limit and two backups | **Y** (B11 only, through BG → Y) | Matches the new priority. Basis noted (Maps, 10:00 weekday). Survey R10.1 cannot confirm it (S2) |
| W6 | Workbook | SuburbScorecard AX (community comparison band) | High/Medium/Low from AU ≥ 50% or AQ ≥ 8% (High); AU ≥ 30% or AQ ≥ 4% (Medium) | N (comment: not used in X, Y or any weight) | Nearest thing to a "diverse suburb" measure, but display-only. Still keyed to Indian share (AQ), and thresholds are interim |
| W7 | Workbook | SuburbScorecard AU (% other language at home), AV (top 3 non-English languages) | Language diversity | N | Diversity data exists but feeds nothing. AV lists top 3 only, so it shows what dominates, not how mixed a suburb is |
| W8 | Workbook | SuburbScorecard AO (% born overseas), AP (% not stated) | Overseas-born share | N | Not used. Overseas-born share shows mix size, not how many origins |
| W9 | Workbook | SuburbScorecard AR (% Indian ancestry), AS (% Hinduism), AT (% Sikhism) | Indian-specific ethnicity/religion shares | N | Old-priority data, display only. Reinforces a single-community view |
| W10 | Workbook | SuburbScorecard AZ (drive to nearest Hindu temple), BA (drive to nearest church), BB (community drive basis and evidence) | Planned temple/church drives and evidence column | N. All three are empty (0 of 71 rows) | Empty. Nothing for restaurants at all |
| W11 | Workbook | SuburbScorecard AW (demography source), AK–AN | ABS source and caveats, population, age | N | Source note only; not a community metric. Listed for completeness |
| W12 | Workbook | SuburbScorecard Q (Score: Shops & doctor), hand-entered 0–10 | General shops and GP, judgement score ("Estimate") | **Y**, weight 15% | Generic retail/GP. Not Indian food. Some of it may already be counted in P through AY |
| W13 | Workbook | SuburbScorecard R (Score: Village character), hand-entered | Village feel | **Y**, weight 5% | Can score high for places that are low on diversity |
| W14 | Workbook | SuburbScorecard X (weighted score) | Sum of M..V × ForcedChoiceCorrections B6:B15, needs W ≥ 10 scores | **Y.** The final score | P is blank (so X is blank, so no rank) when AY or AQ is missing. 20 rows are unrankable on community grounds alone |
| W15 | Workbook | SuburbScorecard Y (rank, passing only) | Rank among "pass" rows with grocery filter OK | **Y** | Removes AY > 25, so excludes diverse suburbs far from an Indian grocery regardless of other merit. Also needs X, hence AQ |
| W16 | Workbook | SuburbScorecard W (scores entered) | COUNT(M:V) | **Y** (gate) | P being blank drops W below 10 and blocks X |
| W17 | Workbook | ForcedChoiceCorrections G9 (15%), B9 (=G9) | Family-set weight for "Indian community" | **Y.** Multiplies P in X | The weight is attached to the P score (half population share). Raising the weight raises the old priority too |
| W18 | Workbook | ForcedChoiceCorrections G10 (15%), B10 | Weight for "Shops & doctor" | **Y.** Multiplies Q | See W12 |
| W19 | Workbook | ForcedChoiceCorrections C9, D9, E9, F9; Q13 matchup row 5 (Indian community vs Nature, H5:U5) | Survey weight, trade-off correction, old typed weight, manual tweak | N since 2 Nov (B = G) | Old survey-based chain, kept for reference. Still says "Indian community" |
| W20 | Workbook | ForcedChoiceCorrections B11 (Village character 5%) | Weight | **Y** | See W13 |
| W21 | Workbook | PriorityWeights row 4 (Indian community) and row 8 (Shops/doctor), cols B–K | Survey ratings → combined weight | N (feeds FCC D only) | Dormant. Still uses Q15.3 and Q15.7 |
| W22 | Workbook | CleanedAnswers A21 (Q15.3), A25 (Q15.7), A18 (Q13), A40 (Q13d), A45–A47 (R5.5–R5.7), A55 (R6.6), rows 62–63 | Survey answers pulled into the model | N (except as above) | Q13 and Q13d ask green village versus Indian community / multicultural neighbourhood (cell comment: "reference-only") |
| W23 | Workbook | RawResponses X1, AB1, AN1 (Q13d), AS1–AU1, BC1 (R6.6) | Stored raw answers | N | AN1 text: "Green village vs multicultural neighbourhood (reference-only)". No R10 columns |
| W24 | Workbook | Settings B16:B25 ("Draft Baseline Weights"); DiscussionSummary D5:E12 | Old draft weights (Indian community 0.18, Shops 0.09) next to current weights | N (display) | Stale: shows Indian community at 18%, not the current 15% |
| W25 | Workbook | DiscussionSummary rows 31–38 (community comparators; viewing-shortlist rule); B15, B20 | Comparator suburbs, the rule that shortlists must include ≥ 2 comparators, grocery-filter counts | N (shortlist rule, not a formula) | Comparators are described as "Diverse / lower-green" and "not included for diversity figures alone". They have no P score (AY blank), so the model cannot rank them |
| W26 | Workbook | Listings AB, AC (walk to supermarket / GP), AG (home-fit rule) | Per-listing walk times | **Y** only if Settings B34 = 1; B34 is blank, so inactive | Generic, not Indian food. Dormant |
| W27 | Workbook | SuburbScorecard Z (evidence notes), AA (frozen legacy text); P1 and AX1 cell comments | Text citing overseas-born %, non-English households and the P definition | N | Notes still describe community in population terms (e.g. Z3: "35.7% overseas-born, 33.3% non-Eng HH") |

Items found: 36 (9 survey, 27 workbook). Several rows cover a group of cells (for example AK–AN, AR–AT, the four `Filters` cells).

## Scoring chain

Final score X (SuburbScorecard col X, 0–10, requires W ≥ 10):
`X = M·B6 + N·B7 + O·B8 + P·B9 + Q·B10 + R·B11 + S·B12 + T·B13 + U·B14 + V·B15`, with B = ForcedChoiceCorrections B6:B15, which equal column G, the family-set weights from 2 Nov.

Community-related terms:
- **P, "Indian community", weight B9 = 15%:** `P = ROUND(0.5·MAX(0,MIN(10,10·(30−AY)/25)) + 0.5·MAX(0,MIN(10,10·AQ/0.08)),1)`; blank if AY or AQ is blank.
  - Grocery half: 10 at AY ≤ 5 min, 0 at ≥ 30 min.
  - Population half: 10 at AQ ≥ 8% born in India.
  - Constants (30, 25, 0.08) are inside the formula, not in a config cell.
  - Hand-calc: Berwick (AY 7, AQ 6.1%) = 8.4; Ringwood (4, 3.2%) = 7.0; Eltham (24, 0.7%) = 1.6; McCrae (35, 0%) = 0.
  - Because the population half is capped at 10 from 8%, a suburb with a high Indian share and an AY of 30 or more would still score 5.0.
- **Q, "Shops & doctor", weight B10 = 15%:** hand-entered 0–10 Estimate; not tied to Indian grocery.
- **R, "Village character", weight B11 = 5%:** hand-entered.

Filter and rank:
- BG = `IF(AY>Filters!B11,"Fails: grocery drive","OK")`, with B11 = 25. Y (rank) counts only rows with "pass" in L, BG ≠ "Fails: grocery drive" and a numeric X.
- AY therefore affects the outcome twice: pass/fail (BG → Y) and 7.5 percentage points of weight (half of P's 15%).

Not in the chain (display only): AX, AO, AP, AR–AV, AZ–BB, BH, BI, Q13/Q13d, community comparator rows, ABS columns AK–AW.

Survey link: survey answers do **not** reach X. Q15.3 and Q15.7 flow CleanedAnswers → PriorityWeights → ForcedChoiceCorrections D, which is reference only since 2 Nov. R10.1–R10.3 are unmapped. Per `PROJECT_STATE.md` the survey's priority questions no longer feed weights.

Net of the chain: the model's only measures of "community" are the Indian-born share (old priority), and the nearest Indian grocery drive. No measure of diversity or restaurants feeds the score.

## Not checked / uncertain

- No cached formula values, so no formula was recalculated. P values above are my hand calculation from stored AY and AQ. The pointer's "37 ranked" was not reproduced.
- `AY` values and the drive-time basis were not verified against Google Maps; I took Filters C11 and the P1 comment as stated.
- The live survey is "live version 1793528975-9715" per `PROJECT_STATE.md`. I read the local v16 source file only, not the published page.
- `tools/import_v14.py` was only grepped, not read in full. I did not check where R10.1–R10.3 would land in the workbook.
- Archive files and `reference/` were not read (project rules). Earlier P definitions were not compared.
- The `ForcedChoiceCorrections` scan excluded array formulas in CleanedAnswers rows 15–28 (openpyxl returned objects); I took their purpose from labels, not formula text.
- Whether the parents read Q15.3 as "food access" or "community of Indian people" can't be determined from the files.
- "Diverse/multicultural" is not defined anywhere in the files. I treated AU, AV, AO and AX as the closest candidates but did not judge them as measures.
- Report files (parent report v3 HTML, foundation report) are said to be out of date and were not audited.
- Z-column notes were sampled (row 3) not fully read for community statements; other rows may also quote old-style community figures.
