# Handover: is "% speaking a language other than English at home" a good measure of diversity? (10 Nov 2026)

**For:** an independent reviewer (agent) with no prior context. **Goal:** an objective second opinion on the *method*, the *measure* and the *calculation*. The author is not confident the measure is the best one. Attack it.

**Update, 10 Nov 2026 (phone call, after this doc was drafted; `Family conversations — before parents leave (Nov 2026).md` D-1 to D-6).** This changes the task:
- Diversity is **a strong preference, not a must**: "if a suburb was great in every other way, they would consider living there". So **no hard filter**. The question is now which measure should feed a *diversity part of the community score* (P), and on what scale.
- Meaning: "**mix of many cultures** ideally". Mum: being around Indian people is **not** the deciding factor.
- Anchors: Tecoma (AU 4.5%, born overseas 17.0%) "looks too white"; "a mixed area is enough", and a Ferntree Gully-level mix (AU 18.7%, born overseas 25.3%) is OK. Caution: "a quarter non-Anglo" was Nish's description of Ferntree Gully, taken from its born-overseas share (which includes UK/NZ-born), not a measured non-Anglo share.
- Dad doesn't care much about diversity. Mum: **shops and food** nearby matter more than who lives in the street.
- Read sections 1–5 with this in mind: question 4 (filter or not) is answered (not a filter); questions 1–3 and 5 still stand, now for a score component with a 0–10 scale. Points 4 and 5 in section 3 (Indian presence; overlap with the grocery filter) matter more now.

**Status of what is being reviewed:** a *draft* filter (now dropped as a filter; the measure question stands). Nothing below is applied to the workbook. Do not edit the workbook, `Filters`, `CLAUDE.md` or any file other than your own output file.

## 1. The decision being supported
A family of three (Mum, Dad, and Nish, the adult child who will live with the parents) is choosing a suburb in or around Melbourne for the parents to move to. Suburbs are ranked by a weighted score; hard filters remove suburbs outright. On 10 Nov 2026 the parents said (relayed by Nish, not confirmed directly with Mum and Dad):

> "A diverse multicultural area is a must."

That is a *must*, so it would act as a **hard filter** (a suburb that fails is removed from the ranking), not just a weight. A filter that removes suburbs needs a measure, a threshold and a defensible reason for both.

What the family has actually said about diversity (all of it):
- Mum, WhatsApp 31 Oct 2026, about one suburb (Tecoma): *"population is almost 100% white. ( gone we think)"*. Mum, same message: wants to be *"Close to markets and other and Indian grocery stores and restaurants"*.
- Nish, 10 Nov: the "diverse multicultural" must (above).
- Survey answers (rating scale: Not needed / Nice to have / Important / Essential). v18, 6 Nov, C1–C4 "how much does it matter that…":

| Item | Mum | Dad | Nish |
|---|---|---|---|
| C1 a mix of cultures | Nice to have | Nice to have | Important |
| C2 Indian groceries nearby | Important | Nice to have | Nice to have |
| C3 Indian restaurants nearby | Nice to have | Nice to have | Nice to have |
| C4 many Indian families nearby | Nice to have | Nice to have | Nice to have |

- Older green-village vs community trade-offs (27–30 Oct; v18 did not re-ask them, so they are history, not current answers). Q13 "very green, community 30 min away" vs "community in your own suburb, less green": Mum chose community in suburb (27 Oct) then green with community 30 min away (30 Oct); Dad and Nish chose green. Q13d, a 5-point scale from green village (A) to multicultural neighbourhood (B): Dad "A slightly" (green), Nish "A strongly" (green), Mum "B slightly" (27 Oct) then "B strongly" (30 Oct) (multicultural).
- Dad's v18 area choices: area type "Leafy established suburb" only; firm limit on drive to an Indian grocery 20 min (R11.1) and to an Indian restaurant 25 min (R11.2); Mum accepts 30 min for both. Dad's 20-min grocery limit is tighter than the 25-min hard filter in the workbook. Mum's area types: bayside, bush-edge hills, leafy.

**Tension to note.** Dad's own survey answers point *away* from a diversity "must": "a mix of cultures" is only Nice to have (all four community items), he leans to green over multicultural on Q13d (slightly) and Q13, and he chose leafy suburbs only. Mum is the only parent whose answers lean multicultural (Q13d, Indian groceries "Important"), and even she rated "a mix of cultures" Nice to have. Nish rated "a mix of cultures" Important. So the "must" (10 Nov, relayed by Nish) is stronger than any parent's written answer. What Dad has **not** been asked is the "must" statement itself (the parent question sheet has "check Dad agrees"); his written answers suggest he may not rank it that high, or may read it as access to Indian shops rather than neighbourhood mix.
**Undefined in the family's words:** diverse in *which* sense. Many cultures? Not predominantly Anglo? South Asian presence? People who "look like us"? The measure choice depends on this and nobody has pinned it down.

## 2. The proposal under review
**Measure:** AU = share of the suburb's people who use a language other than English at home. ABS 2021 Census, General Community Profile, Suburbs and Localities (SAL), Victoria, table G13 (workbook column `SuburbScorecard!AU`). Place of usual residence. Downloaded 27 Oct 2026.
**Rule (option A, the author's pick):** a ranked suburb passes if AU ≥ 10%.

| Option | Rule | Ranked suburbs kept (of 37) | Leaves the current top 10 |
|---|---|---|---|
| A | AU ≥ 10% | 16 | Seaford (9.6%), Upwey (6.3%), Upper Ferntree Gully (8.3%) |
| B | AU ≥ 15% | 11 | as A, plus Frankston (12.1%) |
| C | Community band AX = Medium or High (AU ≥ 30% or India-born ≥ 4%) | 3 (Berwick, Ringwood, West Footscray) | 7 of 10 |

Implementation sketch (not built): `Filters` row 14 holds the cut-off; new `SuburbScorecard` column "Diversity filter" = `IF(AU="","Needs data",IF(AU>=cutoff,"Pass","Fails: diversity"))`; rank column Y excludes "Fails: diversity".
Full context: `docs/model-spec-2026-11-10.md` ("Draft: a diverse multicultural area is a must").

### Why the author chose it, and why that is weak
- **Available, not best.** AU was already in the workbook (it feeds a display-only comparison band, AX). The author did not start from "what is the best measure of diversity".
- **The cut-off was set after looking at the sorted list.** 10% was chosen partly because it keeps Frankston (12.1%, the current #1) and removes Tecoma-like hills suburbs. That is reasoning backwards from the answer. Seaford at 9.6% vs a 10% line is inside measurement noise.
- **Not a calibrated threshold.** The 6 community comparators sit at 46–76%; the 37 ranked suburbs at 3.5–32%. Nothing ties 10% to "diverse".

## 3. Known weaknesses of AU (author's list; add yours)
1. **It is mostly a proxy for "born overseas".** On the 37 ranked suburbs AU correlates 0.94 with born-overseas share (AO), 0.88 with India-born share (AQ) and 0.88 with Indian ancestry (AR). (Computed 10 Nov from the recalculated workbook, n = 37; an earlier note gave 0.89 for AU–AQ on 51 rows.) If it tracks other columns this closely, it adds little.
2. **Language is not ethnicity.** Second-generation Australians usually speak English at home, so an established community looks less diverse than it is. Conversely, older European migrants (Italian, Greek, German) raise AU without making an area what Mum described as "not white". E.g. Rosanna's top languages are Mandarin 4.1% and Italian 4.1%.
3. **Breadth vs concentration is invisible.** 25% speaking one language and 25% spread over 15 languages score the same. Springvale (Vietnamese 25.2%) vs Clyde North (Punjabi 11.5%, Sinhalese 7.9%, Malayalam 3.7%): both pass easily but are different kinds of place.
4. **It cannot say whether the *family's own* community is present.** Newport (AU 17.6%, Arabic/Greek/Italian, India-born 1.1%) passes; Croydon (AU 18.9%, India-born 2.3%) passes. Whether that satisfies "multicultural" for an Indian family depends on the unresolved definition in section 1. The Indian-community items (grocery drive AY, India-born AQ) are already in the score (P) and a separate hard filter (grocery ≤ 25 min).
5. **Possible redundancy with the existing grocery filter.** The 25-min Indian-grocery hard limit already removes 14 suburbs, and AU and grocery drive correlate −0.5 (n = 37). Check how much a second filter adds, and who it removes that the first did not (e.g. Seaford: grocery 8 min, AU 9.6%).
6. **Suburb averages hide local variation.** A suburb at 10% can have a 30% street.
7. **Data quality and age.** ABS 2021; perturbation applies below ~2,500 people (Sassafras 970, Tecoma 2,064, Mount Dandenong 1,271, Macedon 2,073, Olinda 1,773). The Census was on 10 Aug 2021 during Melbourne's lockdown with borders closed, which may have depressed migrant and student counts (**recall, not checked**). The next Census data is 2026 (not yet released).
8. **Denominator not verified.** Whether AU divides by total persons or by persons who stated a language is not recorded in the workbook (the raw SAL DataPack is not in the repo). Not-stated responses could move small suburbs by a point or two.

## 4. Alternative measures to evaluate
Judge each on: does it capture what the family means (once you propose a reading of it), can it be computed from data we have, is it robust at suburb level, does it add information beyond AU.

| # | Measure | Source / availability | Note |
|---|---|---|---|
| M1 | AU (current) | SAL G13; in workbook | |
| M2 | Born overseas (AO) | SAL G01; in workbook | r = 0.94 with AU; includes UK, NZ, South Africa-born |
| M3 | **Born overseas excluding English-speaking countries** (UK, Ireland, NZ, USA, Canada, South Africa) | SAL G09 (not in repo; re-download) or SA2 P09 (in repo, place of enumeration) | Closer to "not Anglo" than M2 |
| M4 | **Ancestry: share not Anglo-Celtic/Australian** | SAL G08 (not in repo); two responses allowed per person | Captures second generation, which M1 and M2 miss; "Australian" self-identification is a known problem |
| M5 | **Breadth index** (Simpson/entropy/ethnolinguistic fractionalisation) over country of birth or language | G09/G13 or SA2 P09/P13 (in repo) | Separates "one big group" from "many groups". Needs a decision on how to treat the English-only/Australia-born majority |
| M6 | South Asian presence (AQ India-born, AR ancestry, AS+AT Hindu/Sikh) | in workbook | Directly the family's community; already half of score P |
| M7 | Two-part rule, e.g. M3 above a floor **and** M5 above a floor | derived | Guards against both "all one group" and "mostly Anglo" |
| M8 | No census filter; use access instead (Indian grocery, temple, restaurants within N min) | AY, AZ, BA in workbook | Treats "diverse area" as access to community, not neighbourhood mix |

**Data in the repo:** `2021_PEP_SA2_for_VIC_short-header/` holds ABS 2021 census tables at **SA2** level (Place of Enumeration, not usual residence): P08 ancestry, P09 country of birth, P13 language, P14 religion. `research/abs/scorecard_sal_sa2_2021.csv` maps each suburb to its SA2(s) with a `match_flag` (SINGLE_SA2 or SPLIT_SA2; e.g. Frankston is 66% Frankston SA2, 34% Frankston North). SA2 ≠ suburb and PEP ≠ usual residence, so SA2 results are an approximation to cross-check, not a replacement for the SAL figures. The SAL General Community Profile that produced AU is **not** in the repo.

## 5. Questions for the reviewer
1. Given only the family's words in section 1, what is the most defensible reading of "a diverse multicultural area is a must"? State it as a one-line definition. List the questions you would ask the family to settle it.
2. Is AU a good measure for that definition? Which of the weaknesses in section 3 actually matter, and which are noise?
3. Which of M1–M8 (or another) would you use, and why? If a combination, give the rule.
4. **Is a hard filter the right tool?** Alternatives: a weight, a "must" test on the final shortlist only, a flag (display-only) beside each suburb, or no census filter (M8).
5. Threshold: is there a principled way to set it (a benchmark such as the Greater Melbourne figure, the comparators, a natural break in the data) instead of picking by eye? The Greater Melbourne AU is **Needs data** (not in the workbook; ABS QuickStats, area 2GMEL).
6. Check the arithmetic: recompute AU-based pass/fail counts for options A, B, C from the table in the appendix, and spot-check 3 suburbs against ABS (SAL codes in `SuburbScorecard!AK`).
7. What would change your recommendation? What evidence would settle the measure choice?

## 6. Constraints (project rules)
- Local only. No Google Drive/Docs/Sheets/Forms. Do not edit the workbook; read tabs/ranges needed, never dump whole sheets. The workbook stores no cached formula values, so read computed cells (X, Y, P) from a recalculated temp copy: `bash tools/recalc_test.sh "Our Next Home — Family Relocation Scoring Model.xlsx"` prints the temp copy's path (does not change the canonical file). Run Python with `.venv/bin/python -I`.
- Label every fact **Checked**, **Estimate**, **Needs verification**, **Needs data** or **N/A**, and say what is recalled vs verified. Cite sources for any outside fact (ABS page, method note).
- Weights, the Filters tab and the definition of score P need the user's explicit approval. You are advising; do not change them.
- Excel-compatible formulas only if you propose any (no XMATCH, REGEXEXTRACT, ARRAYFORMULA).

## 7. Deliverable
Write one file: `docs/diversity-measure-review-<your-model>-2026-11-10.md`. Lead with: (a) your one-line definition of the family's intent, (b) verdict on AU (keep / replace / combine), (c) recommended measure and rule or "use no filter", (d) the three biggest problems with the author's proposal. Then your reasoning, your recomputed numbers, and open questions for the family. Short and plain. Tell the author where they are wrong.

## Appendix: data snapshot
Source: recalculated temp copy of the canonical workbook, 10 Nov 2026, workbook sha `1ebecdf1d816` (live weights = survey v18, equal say; 0 errors, 37 ranked). "S2 rank" is the current rank among the 37 suburbs that pass the hard filters. Percentages are of all people, ABS 2021 Census, SAL, place of usual residence (**Checked** as workbook data; ABS source not re-verified this session). AY = minutes' drive to the nearest Indian grocery, 10:00 weekday, top of range. AX = display-only band (High/Medium/Low). Comparators are unranked reference suburbs chosen for large communities.

| S2 rank | Suburb | Pop | AU other lang % | AO born overseas % | AQ India-born % | AR Indian ancestry % | Hindu+Sikh % | Top 3 non-English languages (AV) | Grocery drive (AY) | AX band |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Frankston | 37331 | 12.1 | 22.5 | 1.1 | 1.4 | 0.9 | Mandarin 1.4%; Greek 1.0%; Russian 0.6% | 3 | Low |
| 2 | Berwick | 50298 | 28.7 | 34.2 | 6.1 | 7.4 | 6.8 | Mandarin 4.0%; Sinhalese 3.8%; Hindi 1.5% | 7 | Medium |
| 3 | Seaford | 17215 | 9.6 | 19.9 | 0.6 | 1.0 | 0.8 | Greek 0.9%; Russian 0.7%; Mandarin 0.7% | 8 | Low |
| 4 | Ferntree Gully | 27398 | 18.7 | 25.3 | 2.3 | 3.1 | 2.8 | Mandarin 3.7%; Cantonese 1.5%; Sinhalese 1.2% | 8 | Low |
| 5 | Newport | 13658 | 17.6 | 23.2 | 1.1 | 1.8 | 1.0 | Arabic 2.4%; Greek 2.4%; Italian 1.5% | 9 | Low |
| 6 | Ringwood | 19144 | 31.6 | 35.7 | 3.2 | 3.7 | 3.4 | Mandarin 9.0%; Cantonese 3.2%; Persian 1.5% | 4 | Medium |
| 7 | Rosanna | 8616 | 23.5 | 26.6 | 2.8 | 3.8 | 2.7 | Mandarin 4.1%; Italian 4.1%; Cantonese 1.4% | 6 | Low |
| 8 | West Footscray | 11729 | 32.0 | 33.5 | 3.7 | 3.6 | 3.9 | Vietnamese 8.2%; Italian 1.8%; Cantonese 1.6% | 7 | Medium |
| 9 | Upwey | 6818 | 6.3 | 16.9 | 0.6 | 1.0 | 0.3 | Mandarin 0.5%; Italian 0.4%; Russian 0.4% | 16 | Low |
| 10 | Upper Ferntree Gully | 3417 | 8.3 | 19.2 | 1.0 | 1.4 | 0.3 | German 1.2%; Greek 0.8%; Mandarin 0.7% | 14 | Low |
| 11 | Croydon | 28608 | 18.9 | 25.4 | 2.3 | 2.9 | 2.7 | Mandarin 3.5%; Cantonese 1.2%; Hindi 0.8% | 1 | Low |
| 12 | Heidelberg | 7360 | 23.7 | 28.1 | 3.0 | 3.5 | 3.1 | Italian 2.7%; Mandarin 2.7%; Greek 1.8% | 1 | Low |
| 13 | Altona | 11490 | 19.6 | 28.3 | 1.4 | 1.9 | 1.4 | Italian 1.6%; Greek 1.4%; Mandarin 1.4% | 9 | Low |
| 14 | Mentone | 13197 | 19.8 | 28.8 | 1.9 | 2.5 | 1.9 | Greek 3.5%; Mandarin 3.0%; Russian 1.5% | 16 | Low |
| 15 | Belgrave | 3894 | 7.0 | 18.6 | 0.4 | 0.9 | 0.2 | German 0.8%; Mandarin 0.6%; French 0.5% | 24 | Low |
| 16 | Tecoma | 2064 | 4.5 | 17.0 | 0.3 | 0.9 | 0.7 | German 0.7%; Italian 0.5%; Hindi 0.4% | 20 | Low |
| 17 | Mordialloc | 8886 | 18.7 | 28.3 | 1.4 | 2.2 | 1.5 | Greek 2.9%; Mandarin 2.3%; Italian 1.5% | 22 | Low |
| 18 | Chelsea | 8347 | 14.7 | 24.4 | 1.4 | 1.8 | 1.0 | Greek 1.8%; Russian 1.1%; Mandarin 1.1% | 20 | Low |
| 19 | Eltham | 18847 | 10.5 | 18.5 | 0.7 | 1.3 | 0.7 | Mandarin 1.6%; Italian 1.0%; Greek 0.9% | 24 | Low |
| 20 | Frankston South | 18801 | 9.0 | 21.6 | 0.9 | 1.3 | 0.4 | Mandarin 1.2%; Greek 1.0%; Malayalam 0.8% | 8 | Low |
| 21 | Highton (Geelong) | 20736 | 13.0 | 19.4 | 2.4 | 2.7 | 2.3 | Mandarin 1.9%; Italian 0.8%; Arabic 0.7% | 7 | Low |
| 22 | Diamond Creek | 12503 | 8.7 | 14.6 | 0.7 | 1.1 | 0.9 | Italian 1.2%; Greek 0.7%; Mandarin 0.7% | 22 | Low |
| 23 | Warragul | 19856 | 6.8 | 14.0 | 1.0 | 1.3 | 1.1 | Mandarin 0.8%; Punjabi 0.4%; Italian 0.3% | 3 | Low |
| 24 | Newtown (Geelong) | 10445 | 8.8 | 14.5 | 1.3 | 1.6 | 1.4 | Mandarin 1.3%; Italian 0.6%; Croatian 0.5% | 7 | Low |
| 25 | The Basin | 4497 | 8.2 | 17.0 | 0.2 | 0.9 | 0.5 | German 1.8%; Mandarin 1.1%; Italian 0.5% | 8 | Low |
| 26 | Mornington | 25759 | 5.6 | 21.2 | 0.4 | 0.5 | 0.4 | Italian 0.7%; Greek 0.6%; Spanish 0.4% | 22 | Low |
| 27 | Montrose | 6900 | 4.8 | 14.5 | 0.4 | 0.7 | 0.3 | German 0.5%; Greek 0.3%; Italian 0.3% | 10 | Low |
| 28 | Warrandyte | 5541 | 13.0 | 20.2 | 0.7 | 1.5 | 1.1 | Mandarin 2.9%; Greek 1.7%; Italian 1.6% | 18 | Low |
| 29 | Mount Evelyn | 9799 | 4.2 | 12.7 | 0.2 | 0.5 | 0.2 | Italian 0.4%; German 0.2%; French 0.2% | 16 | Low |
| 30 | Torquay | 18534 | 4.7 | 13.4 | 0.2 | 0.4 | 0.2 | German 0.5%; Italian 0.5%; French 0.4% | 16 | Low |
| 31 | Drouin | 15287 | 4.9 | 13.1 | 0.5 | 0.8 | 0.6 | Mandarin 0.3%; German 0.3%; Afrikaans 0.2% | 12 | Low |
| 32 | Sassafras | 970 | 7.2 | 19.6 | 0.0 | 0.6 | 0.0 | German 1.0%; Japanese 0.9%; Russian 0.7% | 20 | Low |
| 33 | Gisborne | 10142 | 5.3 | 13.4 | 0.6 | 0.7 | 0.7 | Italian 0.6%; Punjabi 0.4%; Spanish 0.4% | 14 | Low |
| 34 | Olinda | 1773 | 7.1 | 18.6 | 0.2 | 0.8 | 0.6 | French 1.5%; Mandarin 0.8%; Japanese 0.5% | 22 | Low |
| 35 | Mount Dandenong | 1271 | 5.6 | 19.0 | 0.6 | 0.8 | 0.2 | German 0.9%; Afrikaans 0.9%; Spanish 0.6% | 20 | Low |
| 36 | Riddells Creek | 4390 | 3.5 | 11.3 | 0.3 | 0.3 | 0.0 | Italian 0.4%; Mandarin 0.3%; Greek 0.3% | 16 | Low |
| 37 | Macedon | 2073 | 3.9 | 13.2 | 0.2 | 0.4 | 0.2 | French 0.5%; Polish 0.4%; Italian 0.3% | 20 | Low |
| comp. | Springvale | 22174 | 75.6 | 66.3 | 7.4 | 5.7 | 7.4 | Vietnamese 25.2%; Mandarin 6.7%; Cantonese 6.3% | None | High |
| comp. | Clayton South | 13381 | 67.1 | 62.8 | 14.9 | 12.3 | 15.3 | Mandarin 10.7%; Greek 9.3%; Vietnamese 4.5% | None | High |
| comp. | Keysborough | 30018 | 61.1 | 54.1 | 6.6 | 7.3 | 6.7 | Vietnamese 11.5%; Khmer 9.7%; Mandarin 6.8% | None | High |
| comp. | Clyde North | 31681 | 53.6 | 50.7 | 18.2 | 18.4 | 22.4 | Punjabi 11.5%; Sinhalese 7.9%; Malayalam 3.7% | None | High |
| comp. | Endeavour Hills | 24455 | 51.3 | 49.2 | 4.6 | 5.9 | 4.6 | Mandarin 4.3%; Sinhalese 3.6%; Arabic 3.1% | None | High |
| comp. | Wheelers Hill | 20652 | 46.0 | 46.3 | 4.1 | 5.6 | 5.2 | Mandarin 15.4%; Cantonese 4.7%; Greek 4.5% | None | Medium |

Files: `Our Next Home — Family Relocation Scoring Model.xlsx` (SuburbScorecard AK–AX), `docs/model-spec-2026-11-10.md`, `research/abs/`, `2021_PEP_SA2_for_VIC_short-header/`, `community-audit.md`, `community-proposals.md` (earlier work on the community score, including an item that proposed AU as a diversity input to P), `Family conversations — before parents leave (Nov 2026).md`, `research/inputs/whatsapp-mum (31 Oct 2026).md`.
