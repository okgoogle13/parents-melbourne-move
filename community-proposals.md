<details>
<summary>Prompt that produced this file</summary>

````text
## Goal
Propose changes to the parents' suburb survey and workbook so they capture a shifted priority. After talking with my parents, living in a multicultural or diverse suburb, with nearby access to Indian groceries and restaurants, matters more than living somewhere with a high Indian population. An audit of where the files still reflect the old priority is already done.

Files:
- Audit: @community-audit.md
- Survey: @</Users/okgoogle13/Projects/Parents Melbourne MOVE/Our Next Home — questionnaire page v16 (Claude artifact source).html>
- Workbook: @</Users/okgoogle13/Projects/Parents Melbourne MOVE/Our Next Home — Family Relocation Scoring Model.xlsx>


## Phase 1 — Check the audit
Input: audit file, survey, workbook.
Task: Read the audit, then spot-check it against the workbook formulas and survey. The audit was made in a separate session, and missed items lead to fixes being missed.
The workbook stores no calculated values, so sample scores in the audit are hand calculations. If LibreOffice is available, recalculate a temporary copy (headless, outside the project folder) and check a few audit scores against it; otherwise mark all scores as unverified. Never recalculate or save the original.
Output: a short list in your reply of any items or scoring links the audit missed or got wrong (or "audit confirmed"), plus whether scores were verified by recalculation.
Done when: every row in the audit's "Scoring chain" and "Not checked / uncertain" sections has been checked against the source files.

## Phase 2 — Propose changes
Input: the audit plus your Phase 1 corrections.
Task: For each problem, propose a concrete fix. Cover:
1. Survey: reword or add questions so my parents can say how much each of these matters to them separately: (a) overall diversity, (b) access to Indian groceries, (c) access to Indian restaurants, (d) Indian population share. Separating them stops one answer standing in for another. Q15.3 currently mixes several of these; split it.
2. Workbook metrics: how to measure (a)–(c) per suburb. For each metric, name the data source, the unit (e.g. % born overseas, number of birthplace groups, drive time in minutes to nearest Indian grocer), and how reliable it is. If you have web search, confirm each source exists and is current. Note where existing display-only columns (other-language-at-home, overseas-born share, top languages) could be reused.
3. Workbook scoring: the community score (scorecard column P) is half Indian-born share and half grocery drive time, weighted 15% of the final score. Propose how to reweight so diversity and access outrank Indian population share, without dropping Indian population share entirely unless you argue it should go. Give 2–3 options (e.g. replace, reweight, threshold-plus-access), with the trade-off of each.
4. Grocery distance is used twice (25-min pass/fail filter and half of the community score). Propose whether to keep both, and why.
5. Survey answers should feed the final score again. Propose how, starting with R10.1 (grocery and restaurant closeness) and the new diversity item. Give 2–3 options for the link (e.g. survey importance ratings set the community weights directly; survey answers adjust default weights within set bounds; survey answers act as filters or thresholds only), with the trade-off of each. For each option, name the cells or formulas that would change, and how a blank or "don't know" answer is handled.
6. 20 rows have no community score (blank grocery drive), including Glen Waverley, Blackburn and all 6 comparator suburbs. For every metric you propose, state what data must be collected, for how many rows, and how unscored suburbs should be handled in the ranking meanwhile.
7. Temple/church/community-evidence columns are empty (0 of 71 rows) and should be removed. List every formula, filter, chart or named range that references them, and the survey items that mention temple or church (including the temple/church part of Q15.3), so nothing breaks or is left orphaned when they go.
Output: a numbered list of proposed changes, each with: location, current, proposed, reason.
Done when: every audit problem (including Phase 1 corrections) and items 1–7 above have a proposed fix or a stated reason to leave it.

## Phase 3 — Stop and report
Once the Phase 2 list is complete, show it to me and stop. Wait for my approval before editing either file.

## Constraints
- Do not edit the survey or workbook until I approve; I need to check the changes fit how my parents think about this.
- Do not invent suburb data, statistics or data sources. If you could not verify a source, say so and mark it "to verify".
- Keep existing criteria (budget, distance to family, transport, hospital access, lifestyle) unchanged unless a community change directly affects their weighting; flag any such knock-on effect.
- Point out where "diversity" and "access to Indian food" could pull in different directions (e.g. a diverse suburb with no Indian grocer), and how the scoring handles that.
- The audit read the local survey file, not the live survey. Confirm whether they match before proposing survey edits; if you can't, say so and flag every survey proposal as based on the local file.
- Reply length: Phase 1 list, then the proposal list; no preamble or recap.

````

</details>

# Community-fit: audit check and proposed changes

5 Nov 2026. Companion to `community-audit.md` (2 Nov, not edited). Proposals only: the survey and workbook are unchanged and nothing here is approved.
Baseline: workbook sha `841c84acf860` (Nish's v16 import, 5 Nov, uncommitted); survey v16 live version 1793528975-9715.

## Phase 1: audit check

**Scores verified by recalculation.** Temporary LibreOffice copy in the scratchpad: 0 errors, 37 ranked, original's hash unchanged. Berwick 8.4, Ringwood 7.0, Eltham 1.6 and McCrae 0 match the audit.

**Live vs local survey:** the `<script>` blocks are byte-identical (local file sha `b8884baad772`). Survey proposals are not "local file only".

### Corrections to the audit

1. **The 20 unscored rows (W3, W14) are mis-explained.** Filling AY would rank none of them. None has "pass" in L, and W is 0, 4 or 8.
   - 2 are synthetic test rows.
   - 8 fail the drive-to-Glen-Waverley filter.
   - 6 are comparators, unranked by design.
   - 4 are shortlist rows with no other scores (Blackburn, Glen Waverley, Williamstown, Mount Eliza).
   - All 51 passing rows already have AY and AQ.
2. **Comparator grocery drives already exist in the notes.** Z67–Z72 give 2–12 min (e.g. Springvale, India Town, 4 min) but AY is blank. Basis is not stated as 10:00 weekday.
3. **The audit predates today's import (S2, W23).** R10.1 now has RawResponses BX (BX–CA cover R10.1–R10 Notes) and CleanedAnswers rows 93–96. Nish answered "E: up to 30 min". It still feeds nothing.
4. **BH and BI feed DiscussionSummary B21 and B22** (31 and 9). They are not "feeding nothing".
5. **Survey weight vs family weight.** FCC D9 (survey) is 7.7%; G9 (family-set, in use) is 15%. Q15.3: Mum Important, Dad Nice to have, Nish Nice to have.
6. **Temple/church links missed:**
   - CleanedAnswers row 71 (validation) reads E45:E47.
   - RawResponses column N (old Q9) has "A church or place of worship nearby" in rows 7, 9, 12, 15. Rows 12 and 15 are Mum's, row 15 her latest. CleanedAnswers row 35 reads it; nothing depends on row 35.
7. **CleanedAnswers rows 21 and 25 are plain INDEX formulas**, not array formulas. That uncertainty is resolved.
8. **Listings AG** is gated first by Settings B28 (blank), not B34. Same result: inactive.
9. **Z notes:** 62 of 71 mention community figures (the audit sampled row 3). Z21 has a to-do for "Indian grocer/temple". Z67–Z72 hold temple and church research.
10. **Confirmed unchanged:** P, X, Y and BG formulas; Filters B11–B13; FCC B6:B15 = G. AZ–BB are empty and nothing references them (no names, charts, validation or conditional formats).

### Data findings that shape the proposals

- Across the 51 scored rows, other-language-at-home (AU) and India-born share (AQ) correlate **0.89**. Swapping AQ for AU will barely reorder the ranking; access is the real lever.
- Diversity and food access pull apart **the other way** from the obvious worry: no suburb has AU ≥ 25% with AY > 15, but 8 have a grocer within 10 min and AU under 15% (Frankston ranked 1 with AU 12%, Newtown, Highton, The Basin, Montrose, Warragul, Frankston South, Seaford).
- AU on ranked rows runs 2%–32%. Glen Waverley is 61% and the AX "Medium" band starts at 30%, so any scale anchored to Glen Waverley gives almost every candidate a low score.

## Phase 2: proposed changes

### Survey (v17)

1. **Page version.** v16 → v17, new tags for new items, no old tag reused with a new meaning. Reason: stored v16 answers stay valid; Mum and Dad have not been sent the link, so change is cheap now.
2. **Q15.3** (now one rating bundling groceries, restaurants, temple/church, "people from our culture"). Remove from Priorities; add a separate "Community and food" block, same scale plus "Not sure":
   - C1 A mix of cultures: "Living among people from many different backgrounds."
   - C2 Indian groceries nearby: "An Indian grocery store within easy reach."
   - C3 Indian restaurants nearby: "Indian restaurants and takeaway within easy reach."
   - C4 Many Indian families nearby: "A large Indian community in the suburb itself."

   Reason: one answer can no longer stand in for another. A separate block keeps community from taking four of the Q15 slots and keeps the "Top priority for no more than two" rule meaningful.
3. **R10.1** (now one closeness answer for groceries and restaurants: walk / 5 / 10 / 20 / 30). Split into R11.1 (groceries) and R11.2 (restaurants), each: walking / 10 / 15 / 20 / 25 / 30 min / "Doesn't matter much". Reason: current steps cannot express the 25-min filter; restaurants may matter at a different distance.
4. **R5.5–R5.7** (temple/church place, drive, denomination). Remove, with the "temple or church" wording in Q15.3, the R5.7 text box and check (lines 260–261, 315–316) and the header comment (lines 143–144). **Check with Mum first:** her Q9 answer chose "a church or place of worship nearby". Keeping R5.5 alone would keep that signal.
5. **Q15.7 help text** ("Supermarket, pharmacy and GP"): add "(Indian groceries are asked separately)". Reason: stops double counting in the parents' heads.
6. **R10.2 area cards, Q15.8, Q14:** leave. Cards describe area types, not suburbs, and diversity ranges would need suburb-level figures. Village vs diversity is a real trade-off, handled in scoring (item 19).
7. **`tools/import_v14.py`:** must learn the new tags (it exits 1 on an unmapped key). New columns RawResponses CB–CG, CleanedAnswers rows 97–102. Do in the implementation session.

### Workbook metrics

8. **Diversity (a):** use AU (% other language at home) as the input. Source: ABS 2021 Census (tables G13/G14, per AW note, downloaded 27 Oct). Unit %. Filled 69 of 71 rows. Label Checked. Scale: 0 at 5%, 10 at 30%. (Anchoring at Glen Waverley's 61% would cap every candidate at 5.3 or less.) Optional: birthplace diversity index from table G09, counting origins; DataPack not in repo (to verify); AO correlates 0.93 with AU so it adds little. 2026 Census first release is due June 2027; refresh then.
9. **Restaurants (c):** reuse empty AZ as "Drive to nearest Indian restaurant (min; 10:00 weekday, top of range)". Source: Google Maps (approved). Label Estimate (listings change). OSM `cuisine=indian` exists, but Melbourne coverage is unknown (to verify); cross-check only.
10. **Groceries (b):** keep AY. Copy comparator drives from Z67–Z72, labelled Needs verification, or recheck at 10:00.
11. **AX, AR–AT, AO, AV, AK–AN:** stay display-only. When P changes, drop the AQ clause from AX so the band means diversity only (today it mixes old and new priorities).

### Scoring

12. **P (15% of X).** Now 50% grocery drive + 50% India-born share. Options, pick first:
    - **A. Reweight (pick):** grocery 35%, diversity (AU) 30%, restaurants 20%, India-born 15%. Meets "access and diversity outrank Indian share". Because AU and AQ correlate 0.89, the India-born 15% is largely symbolic.
    - **B. Replace:** grocery 40%, diversity 35%, restaurants 25%, India-born 0% (AQ kept for display). Cleanest; nothing left if the parents later want Indian neighbours to count.
    - **C. Threshold plus access:** access only (grocery 60%, restaurants 40%), P capped at 5 if AU < 15%. Makes diversity a requirement; arbitrary cliff hitting the 8 near-grocer, low-diversity suburbs.

    Rough test (hand calc, no restaurant data: grocery 50 / diversity 35 / India-born 15): Frankston stays 1st; Ringwood 9th → 5th; Seaford 5th → 9th; nothing else in the top 12 moves more than one place.
13. **Constants in P** (30, 25, 0.08 are typed in the formula): move to a "Community score parts" block on Filters (rows 23–28), P reading those cells. Reason: house rule, and needed for 15A. Needs approval (Filters tab, definition of P).
14. **Grocery distance used twice** (BG filter + half of P): keep both. The filter is a hard limit removing 14 suburbs (all AU ≤ 9%); the score ranks the 37 that pass. The double count touches only passing suburbs, and option A cuts the grocery share from 50% to 35%. No restaurant filter; score restaurants only. R11.1 answers go to Filters D11 (reference) as a check on B11, not applied automatically.
15. **Survey → score.** Options, pick first:
    - **A. Survey sets the split inside P; G9 stays 15% (pick).** New CleanedAnswers rows read C1–C4; Filters D23:D26 average Mum's and Dad's ratings, normalised, each part limited to 5–50%; Filters B23:B26 = D if present, else the item 12 defaults (C23:C26). Blank or "Not sure": that person is left out for that part; both blank → default. No knock-on to other criteria.
    - **B. Survey moves all ten weights within ±5 points.** FCC B6:B15 = G + gap to D (PriorityWeights K), limited, renormalised. **Knock-on:** every criterion moves (e.g. Indian community 15% → 10%, Shops 15% → 19.4%, Nature 10% → 15%, Beach 15% → 10%). PriorityWeights blank handling unverified (to check).
    - **C. Filters only.** R11.1/R11.2 feed reference cells (Filters D11, a new restaurant In/Out display column); no weight changes. Safest; the survey still does not touch the score. Blank: B11 unchanged.

    Recommend A plus C. **Decision for you:** PriorityWeights counts Nish ("Me"); the goal is the parents' priorities, so use Mum and Dad only for C1–C4.

### Missing data (item 6)

16. | Metric | Rows to collect | Source / label |
    |---|---|---|
    | AU diversity | 0 (69 of 71 filled) | ABS 2021, Checked; refresh June 2027 |
    | AY grocery | 6 comparators (copy from Z) + 4 needs-data shortlist rows; skip 2 test rows and 8 that fail the Glen Waverley drive | Google Maps, Needs verification |
    | AZ restaurant (new) | 51 passing rows (37 minimum) + the same 10 | Google Maps, Estimate |
    | Birthplace index (optional) | 69 | ABS G09, DataPack to re-download |

    Meanwhile: keep the current P until AZ is filled for all 51 passing rows, then switch P in one change and diff the recalculations. Do not rescale P over whichever parts are present (incomparable scores). Unscored rows stay unranked; of the 20, only the 4 needs-data rows could ever rank, and they need 8 other scores first.

### Removing temple/church (item 7)

17. **AZ, BA, BB** (empty): retire in place. AZ becomes the restaurant drive (item 9); BA blank, marked "retired"; BB becomes "Grocery/restaurant drive basis and evidence". Deleting the columns would shift BC–BK left; openpyxl does not rewrite references, so it would break U (71 cells, reads BJ), Y (89 cells, reads BG), BG/BH/BI and DiscussionSummary B15, B20–B22. `tools/report2.py` reads only up to AX (safe either way).
18. **Dependants to retire** (archive copy first; stored answers stay): CleanedAnswers rows 45–47, 62, 63; row 71's E45:E47 part; DiscussionSummary E41:E44. Keep RawResponses AS–AU and N as history. Leave Z21, Z67–Z72 notes as evidence. Survey side: see item 4.

### Other

19. **Q (Shops & doctor), R (Village):** leave, no weight change. A shift toward diversity gently trades against village feel; show the parents the item 12 test before approving.
20. **Stale labels:** FCC C–F and PriorityWeights row 4 say "Indian community"; Settings B16:B25 and DiscussionSummary D5:E12 show the old 18% draft. Rename the row "Community and food", mark drafts superseded. Labels only.
21. **P1 and AX1 comments, Z notes, pointer:** rewrite when P changes; log in `scoring-model-pointer.md`.
22. **Listings AB, AC, AG:** leave; inactive and unrelated.
23. **Comparators:** stay unranked by design. With AY filled they get a display-only P for the "Diverse / lower-green" contrast.

## Approvals needed before any edit

- Definition of P and its weights (12).
- Filters block (13).
- Survey-to-score link (15).
- Removing R5.5–R5.7 after checking with Mum (4).
- Whether Nish's ratings count (15).

## Sources

- [ABS 2026 Census topics and data release plan](https://www.abs.gov.au/statistics/research/2026-census-topics-and-data-release-plan)
- [ABS 2026 Census product guide](https://www.abs.gov.au/census/guide-census-data/2026-census-product-guide/2026)
- [OSM wiki: Tag:cuisine=indian](https://wiki.openstreetmap.org/wiki/Tag:cuisine%3Dindian)
- [OSM help: tags for ethnic grocery shops](https://help.openstreetmap.org/questions/23811/correct-tags-for-ethnic-grocery-shops/)

Restaurant data sources are community-maintained and unverified for Melbourne coverage ("to verify").
