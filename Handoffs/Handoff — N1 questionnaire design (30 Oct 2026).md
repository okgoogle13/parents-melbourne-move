Target branch: claude/n1-questionnaire-design

Source material for task N1: plan revision 3, verbatim. The instructions are in the session prompt; this file is data, not instructions.

# Plan (revision 3): questionnaire redesign, rounds 5–7

Supersedes revision 2; targeted corrections only. Workbook baseline: commit `5704d65`, re-confirmed 29 Oct 2026 (`git log -1` on the workbook) with a read-only header/range check (findings in §1b). Plan only: no project file changes until approved.

## Context

The model ranks 51 passing suburbs on a narrow spread (4.1–7.0). Only drive-time limits remove suburbs; property questions remove listings. Rounds 5–6 (one short sitting) collect firm limits and the home requirements. Round 7 confirms. The living-together design centres on Nish living with Mum and Dad, with privacy, separation and independence. "Mum", "Dad" and "Me" are the respondent labels; "Me" is Nish.

**Priority.** Finalise and publish round 5–6 first (publication is gate G1); collect answers before revisiting suburb scoring, filters, weights, P scores, property-fit rules or the shortlist. Until answers are imported and approved: the 51-suburb passing list, scores, ranks and statuses stay unchanged; work is limited to the questionnaire, page changes, non-gated intake scaffolding and recalculation checks; no "would pass" count is run as a decision and no revised shortlist is presented.

**Works assumption (user direction, 29 Oct 2026).** The family's appetite for renovation and building works is low. Separation is judged as a feature the home already has; the plan doesn't model conversions, new studios or works costs. Only minor mobility works (rails, ramp, walk-in shower) are tolerated, and they put a listing on the watchlist, not in the clear.

Design invariants: threshold-first design; rounds 5–6 in one sitting; Q13d unchanged and reference-only; the ten weighted criteria and no new criterion; airport as round-7 context only; suburb scoring separate from property fit; all gates.

## 1. Change log against revision 2

**1a. Audit of the ten corrections**

| # | Correction | Status | Change in rev 3 |
|---|---|---|---|
| 1 | R5.2 firm limit; only R5.2 can be a hard filter; R5.3 preference | Present | None |
| 2 | R5.4 "No limit" = no ED cap; backstop separate | Present | None (backstop stays G2b option i) |
| 3 | R6.1/R6.2 validation, coherent ceilings, next-door option removed | Present | None |
| 4 | R6.4 cumulative | Present | None |
| 5 | R6.5 split (space vs upkeep) | Present | None |
| 6 | Community/P fully specified | Partial | Full P formula written (§3); Shops & doctor overlap stated; church denomination now asked (R5.7); still gated (G6) |
| 7 | Examples illustrative, midday basis, property caveat | Partial | "Not recommendations" added to R5.2/R5.3 help text |
| 8 | R5.6 skip logic chosen and stored | Present | None (show to everyone + "Not applicable"); same pattern used for R5.7 |
| 9 | Conversion realism | **Superseded** | Replaced by the works assumption: conversion classes, feasibility notes, works cost, outlay-with-works and the conversion allowance gate are removed |
| 10 | Living together exclusion recorded | Present | None |

**1b. Plan corrections**

| Change | Detail |
|---|---|
| `[Name]` → **Nish** | All published wording; removed from Open questions |
| New R5.7 | Church denomination question (any / named / not applicable); replaces the "say so in the notes" route. RawResponses now AO–BE; CleanedAnswers rows 41–57; derived block moves down one row (header 58, rows 59–71) |
| R6.3 replaced | "Could the space be created within a year?" → "How important is it that the home already has this separation?" (Essential / Important / Nice to have) |
| Property-fit simplified | Listings fields cut from 15 to 9 (X–AG); home-fit rules cut from 9 to 8; Settings block A27:D39; CleanedAnswers row 66 = separation importance |
| Gate removed | Old G7 (conversion allowance above `Filters!B3`); report regeneration renumbered G7 |
| Design-doc structure | N1 doc = eight numbered sections (§6 N1) |
| "Would pass" count | Formula settled (§3) but **removed from N2**; written to the workbook only after N3 import and approval (step N4) |
| `"Pass*"` → `"*pass*"` | **Deviation from your instruction, verified.** No L value starts with "Pass": the 51 are "Active — provisional pass" (26) and "Provisional pass" (25). `"Pass*"` counts 0. `"*pass*"` matches exactly 51 in rows 2–48 + 51–66, and is the pattern `DiscussionSummary!B15` and Y already use |
| Row exclusion | COUNTIFS can't skip rows: two COUNTIFS (rows 2–48, 51–66) added together |
| ED "No cap" | Helper `H61`; GW uses the same helper `H59` |
| P formula | Written in full (§3); not implemented |
| Dry run | Counts only, labelled hypothetical; named suburb lists removed |
| Row-58 note | Rows 62, 63 and 71 have no household (E) value |
| G3 detail | Actual M/O formulas recorded; G3 must set Settings B38/B39 = 90 in the same edit (else M/O divide by blank) |
| Recalc tooling | Keep `uv run --no-project --with openpyxl python -I`; no `uv add`, no `pyproject.toml`/lockfile change |

## 2. Rounds 5–6 questionnaire (one sitting, about 10 minutes, all three people)

**General rules**
- Every question is single-choice radio and required, except the notes boxes.
- Answers are stored as the **full option text** with an `A — ` prefix (em dash), as rounds 1–4 were.
- New tags avoid the empty legacy headers `[Q16]`–`[Q21]` (RawResponses AG–AL).

**R5.1 How often do you want to be with the family in Glen Waverley in person?**
A — Several times a week · B — About once a week · C — Every two weeks · D — Monthly or less
*Context.*

**R5.2 What's the furthest drive from Glen Waverley you would not accept going beyond, even for a place that was right in every other way?**
A — No further than 25 min (e.g. Belgrave 21, Seaford 24, Frankston 25)
B — No further than 35 min (e.g. Mordialloc 28, Sassafras 29, Altona 35)
C — No further than 45 min (e.g. Mornington 40, Healesville 43)
D — No further than 60 min (e.g. Mount Martha 47, Rosebud 49, Warragul 58)
E — Up to 90 min: keep the current family limit (e.g. Macedon 62, Kyneton 77, Torquay 88)

Help text: *"This is your firm limit, not your ideal. Examples are illustrative only, not recommendations: Google Maps 'leave now' drive times around midday, 26–27 Oct 2026, from each suburb's centre to Glen Waverley. Peak hour is longer, and the drive from a particular house can be several minutes more or less."*
*Hard-filter candidate.*

**R5.3 And what drive would you be happiest with?** Same A–E text, with "Up to …" in place of "No further than …". Same help text, except the first sentence reads "This is your ideal, not a limit." *Preference tier only; never excludes.*

**R5.4 What's the furthest from a 24-hour public hospital emergency department you would not accept going beyond?** (Not an urgent-care clinic.)
A — 15 min · B — 20 min · C — 30 min · D — 45 min · E — No limit for me
*Hard-filter candidate. E = no cap.*

**R5.5 Which community place would you go to most regularly?**
A — Indian grocery · B — Hindu temple · C — Church · D — None regularly
Help text: *"If it's something else (restaurants, events), say so in the notes."*

**R5.6 For that place, what's the longest drive you'd make regularly?**
A — 10 min · B — 20 min · C — 30 min · D — 45 min · E — Not applicable (I chose "None regularly")
**Skip approach:** shown to everyone, with E. **Validation (page):** if R5.5 = D, R5.6 must be E; if R5.5 is A–C, R5.6 must be A–D. Otherwise save is blocked with: "Please match this to your answer above."

**R5.7 If you chose Church: does it need to be a particular denomination?**
A — Any church is fine · B — Yes, this one: [short text box, required when B is chosen] · C — Not applicable (I didn't choose Church)
**Skip approach:** shown to everyone, with C. **Validation (page):** if R5.5 = C, R5.7 must be A or B; otherwise R5.7 must be C; B with an empty text box is blocked. Same message as R5.6. **Storage:** B is stored as `B — Yes, this one: <typed name>`.

**Q13d** Unchanged text, options and storage (RawResponses AN, CleanedAnswers row 40). Reference-only.

**R5 Notes** (optional)

**R6.1 If we live together, what's the *least* separation between Nish's space and the rest of the home that would still work?**
A — Own bedroom; everything else shared
B — Own bedroom and own bathroom; kitchen and living shared
C — Own zone: bedroom, bathroom and a separate living room, at the other end of the house or on another level
D — Self-contained: own entrance, bathroom and kitchenette (studio, granny flat or dual-living layout), still part of the same household

**R6.2 What's the *most* separation that would still feel like one household to you?** Same A–D.
**Validation (page):** the R6.2 letter must be ≥ the R6.1 letter, else save is blocked with "Your 'most' can't be less separation than your 'least'." Every floor has a valid ceiling (A→A–D, B→B–D, C→C–D, D→D).
*Removed:* "a separate home on the same block or next door". Two dwellings within the $1.59M total acquisition ceiling (`Filters!B3` = `Filters!B2` × 1.06) are unlikely in the passing suburbs: the one checked inner-ring median, Glen Waverley, is $1.675M for a single house. **Reopen** if the budget rises or a dual-occupancy listing within the cap appears.

**R6.3 How important is it that the home already has the separation you chose above?**
A — Essential: I wouldn't buy without it · B — Important: I'd accept a little less for the right home · C — Nice to have

**R6.4 Thinking 10–15 years ahead, what must the home have?** (Each option includes the ones before it.)
A — No special requirement
B — A bedroom and full bathroom on the entry level
C — B, plus step-free access from the street to the entry-level bedroom, bathroom, kitchen and main living area
D — C, plus a fully single-level home with no steps inside

**R6.5a What outdoor space would you most like?**
A — Balcony or courtyard · B — Small garden · C — Medium garden · D — Large garden or bush block

**R6.5b Who would look after it, and how much?**
A — We can do very little ourselves (under 1 hour a week) · B — About 1–2 hours a week ourselves · C — Several hours a week ourselves · D — We'd pay for regular help with most of it

**R6.6 From the front door, what's OK for getting to the supermarket and GP?**
A — Must be able to walk (10 min or less) · B — A walk of up to 20 min would be nice; driving is fine · C — Driving is fine, up to 10 min · D — Driving is fine, up to 20 min

**R6.7 Which one thing matters most for privacy between us?**
A — Separate entrance · B — Own bathroom · C — Own living space · D — Sound separation · E — Space to have friends over privately

**R6 Notes** (optional)

**Storage.** Skipped notes → blank cell. "Not applicable" and "No limit" are stored as their option text; derived minutes → blank (meaning no limit or no feature). Import = new RawResponses row per person: their latest row (15 Mum, 13 Dad, 14 Me) plus the new columns. The row's AM merge log gets "Round 5–6 <timestamp> merged onto row N". CleanedAnswers B2:B4 (`LOOKUP` latest-row formulas) pick up the new rows automatically.

**"Prefer not to live together": excluded, and why.** RawResponses K13 (Dad), K14 (Me) and K15 (Mum) all read "A — Yes, living together" (27 Oct 2026, 06:33–06:40). **Reopen if** any round 5–6 note says otherwise, the household separation conflict (CleanedAnswers F65) can't be met by any layout, or the user asks. Recorded in the design doc and the pointer change log. Updating `Filters!B7` (living-arrangement text) is gated.

**Round 7 (unchanged):**
- Three "which would you visit first" pairs from the surviving suburbs, chosen where Q13d and R5.3 disagree.
- R7.4 "definite no" veto per suburb, which becomes a proposed status change (gated). Safety concerns land here.
- R7.5 airport frequency (optional). Only "monthly or more" makes airport drive a tie-breaker; it never changes weights.

## 3. Workbook cell map and suburb-level rules

**RawResponses** (headers in row 1, full text e.g. `[R5.2] GW drive: firm limit`; AO onward verified empty):

| Cols | Tags |
|---|---|
| AO–AV | R5.1, R5.2, R5.3, R5.4, R5.5, R5.6, R5.7, R5 Notes |
| AW–BE | R6.1, R6.2, R6.3, R6.4, R6.5a, R6.5b, R6.6, R6.7, R6 Notes |

**CleanedAnswers** (rows 41+ verified empty)
- **Rows 41–57:** one row per new column, in the order above.
  - Column A holds the full header text.
  - B–D are copies of the row-40 formula with every `$AN` widened to `$BE` (`RawResponses!$A:$BE`, `RawResponses!$A$1:$BE$1`).
  - E–G = `=LEFT(B41,1)` etc.
  - Existing rows 1–40 are untouched.
- **Row 58:** header "Derived (B–D per person; E household)". Rows 62, 63 and 71 have no E; row 71 reports per person in B–D.

| Row | Measure | Per person (B–D) | Household (E) |
|---|---|---|---|
| 59 | GW firm limit (min) | A25 B35 C45 D60 E90 | `MIN` = proposed `Filters!B4` |
| 60 | GW preferred (min) | same mapping | `MIN` = "Preferred" tier |
| 61 | ED firm limit (min) | A15 B20 C30 D45; E → blank | `IF(COUNT(B61:D61)=0,"No cap",MIN(B61:D61))` = proposed `Filters!B5` |
| 62 | Community place index | grocery 1, temple 2, church 3, none 0 | — |
| 63 | Community drive limit (min) | A10 B20 C30 D45; E blank | — |
| 64 | Separation floor | A–D → 1–4 | `MAX` |
| 65 | Separation ceiling | A–D → 1–4 | `MIN`; F65 = `IF(E64>E65,"CONFLICT: no layout suits everyone","OK")` |
| 66 | Separation importance | A3 (Essential), B2, C1 | `MAX` |
| 67 | Mobility must-have | A–D → 0–3 | `MAX` |
| 68 | Garden preferred band | 1–4 | `MEDIAN` |
| 69 | Garden capacity band | 1–4 | `MEDIAN` |
| 70 | Front-door access | A–D → 1–4 | `MIN` |
| 71 | Validation | "OK"/"Check" (R6.2 ≥ R6.1; R5.5/R5.6 consistent; R5.5/R5.7 consistent) | — |

- Mappings use `IF(code="","",CHOOSE(FIND(code,"ABCDE"),…))`, every cell wrapped in `IFERROR(…,"")`. (`…` here is the per-row value list from the table, written out in full in the workbook.)
- R5.7 has no derived row: the denomination text is read from CleanedAnswers row 47 (B–D) and shown in DiscussionSummary.
- Excel-safe: no XMATCH, LET, REGEX or ARRAYFORMULA.

**Future "would pass" count (settled now; written only at N4, after N3 import and approval; never a decision on its own)**
- Helpers in CleanedAnswers:
  - `H59` = `=IF(E59="","",IF(E59="No cap",9999,E59))`
  - `H61` = `=IF(E61="","",IF(E61="No cap",9999,E61))`
- GW + ED count (DiscussionSummary, display):
  `=IF(OR(CleanedAnswers!$H$59="",CleanedAnswers!$H$61=""),"",COUNTIFS(SuburbScorecard!$L$2:$L$48,"*pass*",SuburbScorecard!$J$2:$J$48,"<="&CleanedAnswers!$H$59,SuburbScorecard!$K$2:$K$48,"<="&CleanedAnswers!$H$61)+COUNTIFS(SuburbScorecard!$L$51:$L$66,"*pass*",SuburbScorecard!$J$51:$J$66,"<="&CleanedAnswers!$H$59,SuburbScorecard!$K$51:$K$66,"<="&CleanedAnswers!$H$61))`
- GW-only count: the same formula without the K criteria and the `H61` test.
- Rows 49–50 (synthetic) and 67–72 (comparators) are outside both ranges.
- Check at N4: with `H59` = 90 and `H61` = 9999 the count must equal 51.

**Suburb filters (gated)**
- **G2a:** `Filters!B4` ← E59.
- **G2b:** `Filters!B5` ← E61. If E61 = "No cap", the options are:
  - (i) leave `Filters!B5` at 90 as an explicitly approved **safety backstop**; or
  - (ii) set it to "No cap", which needs a guarded ED test in Listings T (`IF(ISNUMBER(Filters!$B$5),R2>Filters!$B$5,FALSE)` in place of `R2>Filters!$B$5`) and decoupled O (G3).

  Expected: the stored Q5 answers (Mum 20, Me 20) suggest a numeric cap is likely.
- **G3 (before G2): decouple M and O from the caps.** Today `M2 = IF(J2="","",ROUND(MAX(0,10*(1-J2/Filters!$B$4)),1))` and `O2 = IF(K2="","",ROUND(MAX(0,10*(1-K2/Filters!$B$5)),1))`. Change the divisors to `Settings!$B$38` (M scale) and `Settings!$B$39` (O scale), and set B38 = B39 = 90 in the same edit. Hypothetical effect at GW 35 / ED 20 if *not* decoupled: 8 of 27 survivors move 3 or more places; top-10 overlap 9/10. Recommendation: decouple.
- **G4:** L is a plain value. After G2, re-evaluate it by script for rows 2–66 (not 49–50 or comparators 67–72), using the existing labels ("Fails: GW drive", "Fails: ED drive").
- **R5.3:** DiscussionSummary only. No filter, no score.

**DiscussionSummary A40:F52 (display, not gated; verified empty)**
- Per-person firm and preferred limits, and the household E59/E60/E61.
- Per-person R5.7 church denomination answer.
- The separation conflict flag (F65).
- No "would pass" count until N4.

**P (Indian community) definition (gated, G6; closes P7)**
- **New SuburbScorecard columns (intake, empty until researched; AY–BF verified empty):**
  - AY: drive to nearest Indian grocery (min)
  - AZ: drive to nearest Hindu temple (min)
  - BA: drive to nearest church (min)
  - BB: community drive basis and evidence
  - BF: slope/stairs risk (display-only, Estimate; feeds nothing)
- **Basis:** **nearest qualifying place**, not "best".
  - Google Maps, depart 10:00 weekday, top of range, from the suburb centre (the same basis as comparator J/K).
  - Qualifying grocery: a dedicated Indian/South Asian grocery with published opening hours.
  - Qualifying temple: a Hindu temple open to the public with published hours.
  - Qualifying church: a church with weekly services, of the denomination named in any R5.7 "B" answer; any denomination if all R5.7 answers are A or C. If people name different denominations, BA uses the nearest church of any named denomination. The basis is confirmed in the G6 approval.
  - v1 scope: grocery, temple, church only; restaurants and events excluded (no drive data).
  - Labels in BB: **Checked** (route plus place page seen, dated); **Estimate**; **Needs verification** (hours not published, so the place isn't counted, as with Endeavour Spices).
- **Data source:** the register's task B4 (Claude in Chrome Task 7), scoped to suburbs that pass the approved filters. "task B4" always means the register task; the cell is always `Filters!B4`.
- **Per-person score, helpers BC (Mum), BD (Dad), BE (Me):**
  `=IF(OR(CleanedAnswers!B$62=0,CleanedAnswers!B$63=""),"",IF(INDEX($AY2:$BA2,CleanedAnswers!B$62)="","MISSING",ROUND(MAX(0,MIN(10,10*(2-INDEX($AY2:$BA2,CleanedAnswers!B$62)/CleanedAnswers!B$63))),1)))`
  (C$62/C$63 for Dad, D$62/D$63 for Me). s = 10 within the limit, falling linearly to 0 at twice the limit. Example: limit 20, nearest church 30 → s = 5. "None regularly" (index 0) → "" (no feature).
- **P (column P, replacing the judgement values), complete:**
  `=IF(COUNTIF(BC2:BE2,"MISSING")>0,"",IF(COUNT(BC2:BE2)=0,5,ROUND((IF(ISNUMBER(BC2),BC2*Settings!$B$2,0)+IF(ISNUMBER(BD2),BD2*Settings!$B$3,0)+IF(ISNUMBER(BE2),BE2*Settings!$B$4,0))/(IF(ISNUMBER(BC2),Settings!$B$2,0)+IF(ISNUMBER(BD2),Settings!$B$3,0)+IF(ISNUMBER(BE2),Settings!$B$4,0)),1)))`
  - Blank if any helper is "MISSING"; 5 if no one has a feature (constant, so ranks are unchanged); otherwise the say-weighted mean renormalised over the people with a score (Settings B2:B4 = say for Mum/Dad/Me, currently 1/1/1).
  - Not wrapped in IFERROR on purpose: a zero denominator (all scored people with say 0) shows as `#DIV/0!` and fails the recalc test instead of silently blanking P.
- **Switch rule:** P moves to the formula in one batch, and only when every row passing the approved filters has the needed AY–BA values. A blank P makes W < 10, so X blanks and the suburb drops out of the ranking. Until the switch, P keeps its current values.
- **Double counting:** the P weight (`ForcedChoiceCorrections!B9`) is unchanged; no new criterion; AX and ABS shares stay display-only. The "Shops & doctor" criterion (`ForcedChoiceCorrections!B10`) scores general shops and GP access, so a general supermarket never counts toward P and an Indian grocery never counts toward Shops & doctor.

**Unchanged:** `ForcedChoiceCorrections` (no new engine rows; `$Q$2:$Q$5` untouched), PriorityWeights, Settings B2:B25.

## 4. Property-fit rules and the Listings field spec

**Settings A27:D39** (rows 26+ verified empty). B = approved value (blank until G5); C = survey-derived reference formula; D = notes. Intake can't change any fit result.

| Row | Parameter | C (reference) |
|---|---|---|
| 28 | Separation floor (1–4) | CleanedAnswers!E64 |
| 29 | Separation ceiling (1–4) | E65 |
| 30 | Separation importance (3 Essential / 2 Important / 1 Nice to have) | E66 |
| 31 | Mobility must-have (0–3) | E67 |
| 32 | Garden preferred band | E68 |
| 33 | Garden capacity band | E69 |
| 34 | Front-door access | E70 |
| 35–37 | Land-size bands: courtyard ≤400, small ≤650, medium ≤1,000 m² | Estimate |
| 38 / 39 | M scale / O scale (min) | 90 / 90 (B set at G3) |

**Listings columns from X** (X onward verified empty). W1 already holds the source note. Manual columns are keyed to the listing URL in V so a refresh re-joins them. Column T (price and suburb check) is untouched and remains the only budget test.

| Col | Field | Values / rule |
|---|---|---|
| X | Separation tier now | A–D (R6.1 ladder) / Unknown, from the floorplan |
| Y | Mobility level met now | 0–3 / Unknown (R6.4 ladder) |
| Z | Mobility gap | None / Minor works (rails, ramp, walk-in shower) / Major / Unknown |
| AA | Garden band (formula) | From K against Settings B35:B37; photos override, noted in AF |
| AB / AC | Walk to supermarket / GP (min) | From the address; basis named |
| AD | Noise flag | Highway / Rail / Flight path / None |
| AE | Overlay | Bushfire / Flood / Heritage / None (task B3) |
| AF | Evidence basis + date | Floorplan seen / Photos only / Not checked |
| AG | Home fit (formula) | "Class: reason", first matching rule below |

**Home-fit rule (AG), applied in order:**
0. `Settings!B28` blank → **Pending rules** (the state throughout intake).
1. T is "Under offer" or starts "Fails" → **Not suitable: suburb/budget check**. Suburb filters win, even for a good house.
2. X blank/Unknown, or Y Unknown, or (Y < must-have and Z Unknown) → **Needs data: floorplan**.
3. tier(X) > ceiling → **Not suitable: more separation than wanted**.
4. tier(X) < floor and B30 = 3 → **Not suitable: not enough separation**.
5. Y < must-have and Z = Major → **Not suitable: mobility**.
6. Any of the following → **Watchlist: <first reason>**:
   - tier(X) < floor (importance below Essential) → "less separation than wanted"
   - Y < must-have and Z = Minor works → "minor mobility works"
   - T = "Pass if bought near low end"
   - AA > B33 (upkeep), or AA ≠ B32 by 2+ bands (outdoor space)
   - AD ≠ None
   - AE ≠ None
   - B34 = 1 and (AB or AC > 10)
7. Otherwise → **Strong fit**.

- R6.7 ranks listings within the same class (for example, separate entrance first).
- A property that passes the suburb filters but fails AG is Not suitable and doesn't change the suburb.

## 5. Illustrative suburb-count scenarios (hypothetical; deferred until real answers)

Not decisions and not a shortlist. Counts of the 51 that would remain under each pair of limits; current weights; recalculated copy at `5704d65`. Re-run with the real E59/E61 at N4 before any G2 request.

| GW limit \ ED limit | 15 | 20 | 30 | 45 | No cap |
|---|---|---|---|---|---|
| 25 | 14 | 15 | 15 | 15 | 15 |
| 35 | 21 | 27 | 28 | 28 | 28 |
| 45 | 23 | 29 | 32 | 33 | 33 |
| 60 | 29 | 36 | 39 | 40 | 40 |
| 90 (today) | 33 | 40 | 44 | 47 | 51 |

- Coupled vs decoupled M/O (rank moves of 3+ places among survivors): 25/20: 0; 35/20 and 45/30: 8, top-10 overlap 9/10; 60/no cap: 3.
- Outside the 51: all 4 "Active — needs data" rows fit 35/20; of the 6 comparators, 2 fit 25/20.

## 6. Implementation sequence

Every workbook step: re-read the workbook → archive to `Archive/` as `(superseded 2026-10-29, before <change>)` → edit with openpyxl → recalc test → pointer change log (`scoring-model-pointer.md`) → register (`Open work — what runs where (27 Oct 2026).md`) → `PROJECT_STATE.md`. On any failed check: restore the root workbook from the archive copy and report.

**Not gated (intake)**
- **N1.** Design doc `Questionnaire redesign — rounds 5–7 (29 Oct 2026).md` in root: unnumbered Context preamble (including the works assumption); then
  1. Executive summary of changes
  2. Audit of gaps, overlaps, and ambiguities
  3. Revised rounds 5–7 questionnaire
  4. Scoring, filter, and conversion rules (conversion: out of scope under the works assumption)
  5. Property shortlisting and Listings-tab rules
  6. Workbook implementation plan
  7. Gated-change register and approval sequence
  8. Verification and recalculation checklist

  then unnumbered Open questions. Register: add C10 (this work), P9 (family answers rounds 5–6), B9 (floorplan/listing-fit fields for the 32 listings, Claude in Chrome); re-scope task B4 to suburbs passing the approved filters; recommend rounds 5–6 **before P4**. Set the next task in `PROJECT_STATE.md`.
- **N2.** Workbook intake, one edit: RawResponses AO1:BE1 headers; CleanedAnswers rows 41–71; Settings A27:D39 (column B blank); Listings X1:AG1 headers plus AA/AG formulas filled down rows 2–33 (AG = "Pending rules"); SuburbScorecard AY1:BB1 and BF1 headers (empty); DiscussionSummary A40:F52 display block (no count). Recalc and diff (§7).
- **N3.** After all three answer: import per §2 Storage; recalc and diff.

**Gated (ask once each, when its inputs exist)**

| Gate | Ask when | Change |
|---|---|---|
| G1 | after N2 | Republish the questionnaire. Archive the round-4 page first; add R5/R6 items with `gap:true`; keep Q13d; mark Q4, Q4b, Q5, Q6, Q7, Q7b `retired:true` (not rendered; data stays); add the three validation checks (R5.6, R5.7, R6.2) to the save path; mode label `round 5–6 (R5, R6, Q13d)`; republish to `https://claude.ai/artifact/9fbNBMzhdedGaYwQg3pnGo` |
| N4 | after N3, with approval | Write `CleanedAnswers!H59`/`H61` and the DiscussionSummary counts; re-run the dry run with real E59/E61 |
| G3 | after N2 (before G2) | M/O decoupling, Settings B38/B39 = 90 |
| G2a/G2b | after N4 | `Filters!B4` / `Filters!B5`, incl. no-cap or backstop choice |
| G4 | after G2 | L re-evaluation, plus any C status change (incl. R7.4 vetoes) |
| G5 | after N3 | Settings B28:B37 property thresholds |
| G6 | after task B4 data is complete for surviving suburbs | Switch P to the §3 formula, incl. the R5.7 church basis |
| G7 | last | Regenerate reports (`tools/report2.py`; `tools/found.py` needs fixing first) |

## 7. Verification checklist

- **Recalc:** the `docs/workflow.md` test via `uv run --no-project --with openpyxl python -I`. Pass = `RECALC OK`, 0 formula errors on any sheet including new cells, `canonical unchanged`.
- **No-change diff (N2, N3, N4)** — a script compares pre- and post-change copies:
  - *Unrecalculated file:* every pre-existing cell's formula or value string identical, except intended new cells (catches formula edits that leave values unchanged).
  - *Recalculated copies:* `ForcedChoiceCorrections!B6:B15` (weights); SuburbScorecard C, J, K, L, M–V, X, Y identical; 51 rows with a numeric Y; `DiscussionSummary!B15` = 51; Settings B2:B25 and Filters B2:B8 identical; Listings A:W identical; AG = "Pending rules" on all 32 rows.
  - N3 only: CleanedAnswers B2:B4 and their dependent answers may change. Any round 5–6 answer touching Q15 or Q10–Q13 would move weights; the new questions don't touch those columns, so a weight difference means the import is wrong.
- **Import format (N3):** each new RawResponses row = the person's previous latest row plus AO–BE; every stored answer string matches a page option exactly (script vs the page's option arrays; R5.7 B matches the prefix `B — Yes, this one: ` followed by non-empty text); row 71 "OK" for all three; E59/E61 return minutes or "No cap".
- **Count formula (N4):** temp copy with H59 = 90, H61 = 9999 → 51.
- **P formula (before G6):** temp copy fixtures — all "None regularly" → 5; one MISSING → blank; one scorer → that score; say weights 2/1/1 → weighted mean. Discard copy.
- **AG fixtures:** temp copy only, test Settings values and one synthetic listing per rule 1–7; each returns its expected class; discard copy.
- **Page (after G1):** "Still needed" mode shows R5.1–R5.7, Q13d, R6.1–R6.7 and notes; retired items hidden; "Nish" appears in R6.1; R6.2 < R6.1 blocks saving; R5.5 = D with R5.6 ≠ E blocks saving; R5.5 ≠ Church with R5.7 ≠ C, and R5.7 = B with an empty name, both block saving; fallback copy text shows lines like `[R5.2] B — No further than 35 min …`.

## Open questions

None outstanding. The church denomination is now asked in R5.7.
