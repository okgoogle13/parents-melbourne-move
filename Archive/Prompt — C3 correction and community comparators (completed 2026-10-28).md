# Correction to the C3 plan, and a new task: community comparator suburbs

Work on branch `claude/ecstatic-tesla-pzbg1v`. The user approved this on 28 Oct 2026.

Hard rules:
- Don't change family weights or the Filters tab.
- Keep checked facts and estimates separate.
- Record every source in the suburb's column-Z note.

## 1. C3: run it, with these corrections

Run the 13 N/R/V changes exactly as proposed.

**Keep P unchanged.** Don't redefine P as drive access alone.

Replace the plan's P paragraph with:

> "P is unchanged in C3. Its definition is pending a family decision. B4 measures drive minutes to the nearest Indian grocery, Hindu temple **and** church (generic nearest, not one institution). The ABS shares will feed a display-only Community comparison band (section 3)."

Why the change:
- Q13 was 2–1 (Mum A; Dad, Me B) and moved no weight under the model's own rule.
- Q13 never asked whether living among people of colour matters.
- A drive-access-only P would probably give almost every suburb a similar score.
- Mum's Q9 answer was "a church or place of worship nearby".

Also in C3:
- **Pointer change-log (step 4):** alongside rank movement, list the top 15 after recalc with % India-born (AQ) and % other language at home (AU) for each.
- **Fix the AK–AW header comments.** Each comment sits one column right of the column it describes (e.g. AP's comment defines AO; AW's describes AV). Move each one left, then check every comment against its header.
- **Update Task 7 in `Claude_in_Chrome_prompt — close research gaps.md`.** B4 must measure drive minutes to the nearest Indian grocery, Hindu temple and church. Add the comparator suburbs once they're approved.

## 2. Add Q13d to the questionnaire (a new question, not a replacement for Q13)

Add Q13d to `Our Next Home — questionnaire page (Claude artifact source).html` in the "Pick one" section, after Q13. Mark it as a round-4 gap question so it shows in "only the questions still needed" mode. Republish the artifact to the same URL.

Use this wording exactly (approved 28 Oct; the neighbour clause is what separates Q13d from Q13, so don't drop it):

> **Q13d.** If both options were within 30 minutes of family, which would you prefer for everyday living?
> A. A very green, peaceful village or bushland-edge suburb with trails and natural scenery nearby. Most neighbours would not share your background. Indian groceries, a Hindu temple, and churches would be about 30 minutes' drive away.
> B. A more multicultural neighbourhood where many neighbours are from Indian and other migrant backgrounds. Indian groceries, Hindu temples, and churches would be close by, but with fewer trees, trails, and natural views nearby.

Answer scale, one choice: **A strongly / A slightly / No strong preference / B slightly / B strongly**

Rules for Q13d:
- Keep Q13 and its existing answers exactly as they are.
- Q13d does **not** feed ForcedChoiceCorrections or any weight. That engine reads A/B answers; Q13d uses a 5-point scale and is reference-only until the user decides how to use it.
- **Don't add Q13d to the workbook yet.** The workbook stays frozen apart from C3 until the user approves the comparator list (section 3). Once approved, add Q13d as a new row in RawResponses and CleanedAnswers, and nothing else.

## 3. Community comparator suburbs: research, then STOP

**Goal:** a labelled set of high-diversity suburbs (low nature is fine) for the family to compare side by side with the leafy, low-diversity shortlist. They aren't meant to win the main rank, and they would lose it by design: Nature, Beach and Village carry about 44% of the weight.

**Target:** 6–8 comparators.
- About 4–5 "Diverse / lower-green".
- About 2–3 "Potential both".

**Anchors.** Also show the current top 3 passing suburbs from the recalculated C3 workbook as "Green / lower-diversity" anchors, using their existing workbook values. Anchors don't count toward the 6–8 and aren't proposed for adding. Rowville is the "Reference" row.

### 3a. Research

The ABS figures below are verified from the ABS 2021 GCP DataPack (SAL, VIC; tables G01, G02, G08, G09G, G14). Definitions match AO–AU, and Glen Waverley and Berwick match the workbook exactly. Corner labels here are starting hypotheses only.

| Suburb | SAL | Pop | Med age | 65+ | India-born | Indian anc. | Hindu | Sikh | Other lang. | Starting corner |
|---|---|---|---|---|---|---|---|---|---|---|
| Springvale | SAL22328 | 22,174 | 36 | 16% | 7.4% | 5.7% | 4.2% | 3.2% | 76% | Diverse / lower-green |
| Tarneit | SAL22451 | 56,370 | 30 | 4% | 28.8% | 27.0% | 21.1% | 13.6% | 64% | Diverse / lower-green |
| Clayton South | SAL20570 | 13,381 | 34 | 16% | 14.9% | 12.3% | 12.3% | 3.0% | 67% | Diverse / lower-green |
| Clayton | SAL20569 | 18,988 | 28 | 10% | 16.4% | 13.5% | 14.6% | 2.1% | 64% | Diverse / lower-green |
| Clyde North | SAL20582 | 31,681 | 30 | 5% | 18.2% | 18.4% | 12.2% | 10.2% | 54% | Diverse / lower-green |
| Keysborough | SAL21339 | 30,018 | 36 | 14% | 6.6% | 7.3% | 4.9% | 1.8% | 61% | Diverse / lower-green |
| Noble Park | SAL21952 | 32,257 | 35 | 15% | 9.8% | 7.4% | 4.9% | 4.8% | 64% | Diverse / lower-green |
| Point Cook | SAL22086 | 66,781 | 33 | 6% | 14.9% | 17.4% | 16.1% | 2.5% | 51% | Potential both |
| Mount Waverley | SAL21816 | 35,340 | 40 | 19% | 6.1% | 7.7% | 7.0% | 0.8% | 50% | Potential both |
| Wheelers Hill | SAL22766 | 20,652 | 48 | 29% | 4.1% | 5.6% | 4.5% | 0.7% | 46% | Potential both |
| Wantirna South | SAL22686 | 20,754 | 42 | 21% | 4.7% | 6.4% | 5.8% | 0.7% | 44% | Potential both |
| Endeavour Hills | SAL20871 | 24,455 | 39 | 17% | 4.6% | 5.9% | 3.8% | 0.8% | 51% | Potential both |
| Rowville | SAL22207 | 33,571 | 41 | 16% | 3.2% | 4.8% | 3.5% | 0.7% | 32% | Reference |

**Interim Community comparison band** (proposed; user to confirm). Use it in Output 1 now; it is display-only and is not a measure of belonging or community quality.
- **High:** AU ≥ 50% or AQ ≥ 8%
- **Medium:** AU 30–49% or AQ 4–7.9%
- **Low:** everything else
- B4 drive minutes will be added later; leave a placeholder.

Collect the following for every candidate.

1. **House price, with source and as-at date.**
   - Springvale is done: OnTheHouse "median value" as at 30 Sep 2026; houses $877,575, units $614,963.
   - Record the basis exactly ("median value", "sale median", or the source's own label). Don't mix bases silently.
   - Use only links returned by a search. **Don't type in hand-built OnTheHouse URLs** (the user rejected this). Statement of Information PDFs in search results give suburb medians with a period.
2. **Drive times.** Minutes to Glen Waverley (J) and to the nearest 24-hour public ED (K), on the Filters-tab basis (Google Maps, typical traffic).
   - If you can't check a time, mark it `Estimate`.
   - My unchecked estimates: Springvale ~15, Clayton ~10–15, Keysborough ~20, Wheelers Hill ~5–10, Clyde North ~35–40, Point Cook/Tarneit ~45–60.
3. **Hard filters.** Pass or fail on the $1.5M purchase cap and the 90-min drive to Glen Waverley. Drop any that fail.
4. **Evidence for "Potential both".** Label a suburb this only with sourced evidence of meaningful everyday access to both:
   - **Nature:** a named park, reserve, bushland, wetland or trail network in or next to the suburb, of real size. A C1-style source (Wikipedia, Victorian Places, Parks Victoria or council). Street trees alone don't count.
   - **Community infrastructure:** a named Indian grocery, Hindu temple or church in or near the suburb, sourced with its address.

   If either is missing, relabel it "Diverse / lower-green" or mark the trade-off "Needs verification". The candidate features (Jells Park, Point Cook wetlands/coast, Churchill/Lysterfield parks) are recall only until sourced.
5. **Grocery, temple and church drives.**
   - Every comparator needs at least one sourced community-infrastructure example.
   - Fill the three drive columns where you find a named place.
   - Otherwise write `Not yet checked (B4)`; B4 fills these later.
   - Never leave a cell blank or guessed.
6. **Nature-fit labels** ("Parents' nature fit", "My coastal-nature fit").
   - Use the same label scheme as SuburbScorecard columns D and E.
   - For new comparators, mark each label `Estimate` unless a nature source supports it.
   - For anchors, copy D and E from the workbook.

### 3b-format. Required comparator proposal format

When presenting the proposed comparators, provide two clearly separated outputs.

#### Output 1 — Compact discussion trade-off table

Use this exact column order:

```text
Location | Comparator corner | Parents' nature fit | My coastal-nature fit | Community band | India-born share (AQ) | Other language at home (AU) | Indian grocery drive | Hindu temple drive | Church drive | Glen Waverley drive | Public 24-hour ED drive | House price evidence | Budget result | Main trade-off | Evidence status
```

Comparator-corner labels:

```text
Green / lower-diversity
Diverse / lower-green
Potential both
Reference
```

Main-trade-off labels:

```text
Nature-first
Community-first
Potential balanced option
Needs verification
```

Rules:
- Do not declare a single overall winner. The purpose is to make the nature-versus-community trade-off visible.
- Keep checked facts and estimates visibly separate. Clearly label every unchecked drive time as an estimate.
- Do not treat ABS diversity shares as a measure of personal belonging or community quality.
- Do not allow Community to alter X, Y, or P's weight.
- Include a plain-English main trade-off for every row.

#### Output 2 — Detailed evidence table

Provide a spreadsheet-ready evidence table using this column order:

```text
Location | Comparator corner | Price basis | Price source | Price source URL | Price as-at date | Glen Waverley drive basis | Glen Waverley drive | Public 24-hour ED name | Public 24-hour ED drive basis | Public 24-hour ED drive | AQ | AQ source | AU | AU source | Nature evidence | Nature source | Community-infrastructure evidence | Community-infrastructure source | Community-infrastructure address | Hard-filter result | Column-Z note | Unresolved issues
```

Rules:
- Record the exact price basis: "median value", "sale median", or another exact label used by the source.
- Record the source name, URL, and as-at date for every price figure.
- Use only links returned by search; do not construct OnTheHouse URLs manually.
- Mark every unchecked drive time as `Estimate`. Mark every checked drive time as `Checked`, with the source and date checked.
- Keep checked facts and estimates visibly separate. Do not present an estimate as a verified fact.
- Do not modify the workbook in this stage.

### 3b. STOP and propose

Present 6–8 proposed comparators, plus the 3 anchors and the Rowville reference, in the two formats above.

- Include about 4–5 "Diverse / lower-green".
- Include about 2–3 "Potential both", but only where the sourced evidence supports the label.
- Drop any candidate that fails the $1.5M purchase cap or the 90-minute Glen Waverley drive filter.
- Keep Rowville as the reference, not as a comparator.

**Don't modify the workbook until the user approves the final comparator list.**

### 3c. After approval only (not now)

1. **Archive the workbook** as `Archive/Our Next Home — Family Relocation Scoring Model (superseded 2026-10-28, before community comparators).xlsx`.
2. **Add the approved suburbs as SuburbScorecard rows.**
   - Set `Shortlist Status (C) = Community comparator`.
   - Fill A–L, AB–AJ and AK–AW.
   - Give N–V judgement scores only where a source supports them. Mark the rest as estimates in Z.
3. **Add a "Community comparison band" column** at the end of SuburbScorecard.
   - Display-only: it must not feed X, and P's weight is unchanged.
   - Use the band thresholds the user confirms, with a placeholder for B4 drive minutes.
   - Header comment must say "Comparison band, not a liveability score", and give the thresholds.
4. **Update DiscussionSummary.**
   - Add a Nature (N) vs Community-band list, grouped by corner: Green / lower-diversity; Diverse / lower-green; Potential both.
   - Add this rule: "Viewing shortlist includes at least 2 Community comparators (proposed; family to confirm)".
5. **Add Q13d** as new rows in RawResponses and CleanedAnswers. It must not feed any weight.
6. **Recalc a copy (`recalc.py`).**
   - 0 errors.
   - A before/after diff shows only the new rows, the new column, the Q13d rows and DiscussionSummary changed.
   - Existing X/Y values do not move.
7. **Update `scoring-model-pointer.md`** (tab map and change-log) and the open-work file (new task row; B4 now covers church and the comparators).

## 4. Commit and report

Commit C3, Q13d and comparator research as separate commits, then push to `claude/ecstatic-tesla-pzbg1v`.

Tell the user:
- The local folder's `main` is behind this branch. They need to fast-forward the folder to the branch, which is the source of truth.
- Briefly: what changed; the top 15 with diversity shares; the two comparator tables; what is still an estimate.

## Open (for the user; don't decide these)
- Whether the Community band ever carries weight. Currently display-only, by decision.
- Band thresholds (interim proposal above).
- How Q13d answers will be used once collected.
- The viewing quota of 2 comparators is a proposal.
