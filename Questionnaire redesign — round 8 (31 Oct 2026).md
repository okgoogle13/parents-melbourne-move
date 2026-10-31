# Questionnaire redesign — round 8 (31 Oct 2026)

Design record for survey **code version 14** ("v14 trade-offs survey"). Approved by the user 31 Oct 2026 (Option C). Page source: `Archive/Our Next Home — questionnaire page v14 (superseded 2026-10-31, before timing v15).html` (now superseded by v15). Previous source in Archive as `(superseded 2026-10-31, before trade-offs v14)`.

**Status:** published 31 Oct 2026 to the existing artifact URL (live copy verified identical to this source; PAGE_VERSION 14). Link NOT sent. Awaiting the user's review. **The model is unchanged:** no change to weights, filters, shortlist status, P scores, the 51-suburb list or the Mum/Dad/Nish voting.

## Purpose

To measure, from Mum's and Dad's own answers, (1) what "nature" means to each of them and (2) how much extra drive to family in Glen Waverley each would accept for it. Timing is a secondary constraint (target about 15 minutes); the core nature and family measurement is not to be weakened to meet it.

Why: v13 rated importance with no cost attached, asked one fixed nature-versus-family choice (Q10), and no longer asked what kind of nature (Q8 was cut in v10). On the current list the nature score is uncorrelated with drive to GW (r = −0.01, Computed from estimates), so the trade-off that matters is measured directly here.

## Final question set (11 parts)

1. Living together: Q7a
2. Budget: Q3c
3. Drive limits: R5.2, R5.4
4. **Kinds of nature (one question per screen):** R8.1, R8.2
5. **Kinds of area (one question per screen):** R8.4, R8.5, R8.6 (only if R8.4 is B or C)
6. **Family drive (one question per screen):** R8.3 ladder
7. Pick one: Q11, Q12, Q13, notes
8. Community: R5.5–R5.7, notes
9. The home: R6.1–R6.6, notes
10. Later on: Q14
11. Priorities: Q15.1–Q15.10, notes

Removed: **Q10** (replaced by the R8.3 ladder) and **Q13d** (fed nothing; Q13 covers community versus bush). Earlier answers to both stay in the data.

## Stored values and branching

| Tag | Asked when | Stored |
|---|---|---|
| R8.1 Kind of nature most wanted | always | A bush and forest walks / B hills and long views / C creek, river or lake / D leafy streets and parks / E own garden / F coast and beach / G none matters much |
| R8.2 Kind of nature second | R8.1 isn't G | A–F with the R8.1 pick hidden, G "nothing else"; **X** if R8.1 = G |
| R8.4 Kind of area most wanted | always | A–E (cards below) |
| R8.5 Kind of area least wanted | always | A–E with the R8.4 pick hidden, F "happy in any of them" |
| R8.6 Bushfire risk (added 31 Oct 2026) | only if R8.4 = B or C; otherwise stored X automatically | A only low risk / B some risk OK with bushfire building rules and leaving early on bad fire days / C wouldn't stop me / X not asked. Feeds nothing |
| R8.3-30 | R5.2 limit 35 min or more | A green street / B leafy street; **L** if the limit is 25 |
| R8.3-20 | answered leafy at 30, or the limit is 25 | A/B; otherwise **X** |
| R8.3-45 | green at 30 and limit 45 or more | A/B; **L** if green at 30 but limit 35; otherwise **X** |
| R8.3-60 | green at 45 and limit 60 or more | A/B; **L** if green at 45 but limit 45; otherwise **X** |
| R8.3-75 | green at 60 and limit 90 | A/B; **L** if green at 60 but limit 60; otherwise **X** |
| R8.3 (worked out, never asked) | ladder finished | A under 5 / B 5–15 / C 15–30 / D 30–45 / E 45–60 / F 60+ extra minutes accepted |
| R8.3c (worked out, never asked) | ladder finished | Y capped by the firm limit / N not capped |

X = not on this person's path. L = not shown because it is over their firm limit (R5.2: A 25, B 35, C 45, D 60, E 90 min).

Ladder wording: two homes the same in every way (price, house, shops, hospital) except the street and the drive. Green street: "tall bush, forest trails from your door, [N] min drive to family". Leafy street: "some trees, a park nearby, 15 min drive to family". The drive times are stated to be made up.

| Path | R8.3 |
|---|---|
| 30 leafy → 20 leafy | A |
| 30 leafy → 20 green | B |
| 30 green → 45 leafy | C |
| 30 green → 45 green → 60 leafy | D |
| … → 60 green → 75 leafy | E |
| … → 75 green | F |

## Area cards (R8.4)

Figures are ranges for the suburbs each card stands for, from SuburbScorecard J (drive to GW), K (drive to 24-hour ED), G (price) and AB (train), read 31 Oct 2026 from workbook sha `29d9e37d508c`. Drive times: Google Maps leave-now, 26 Oct (Checked). ED times and prices are shown on the page as estimates; prices are mostly automated valuations. Descriptions are Claude's characterisation (Estimate). The bushfire lines are marked preliminary on the page until the screening below is done.

| Card | Suburbs (internal only, never shown) | GW drive | ED drive | Train | Price shown |
|---|---|---|---|---|---|
| A Bayside suburb | Mentone, Frankston, Seaford, Chelsea, Mordialloc, Altona | 24–35 | 4–19 | 6 of 6 | roughly $850k–$1.5m |
| B Bush-edge hills | Upper Ferntree Gully, Upwey, The Basin, Tecoma, Belgrave, Montrose, Warrandyte, Mount Evelyn, Sassafras, Mount Dandenong, Olinda, Emerald | 16–35 | 2–22 | 4 of 12 | mostly roughly $850k–$1m, some higher |
| C Country town | Healesville, Yarra Glen, Warburton, Macedon, Woodend, Gisborne, Riddells Creek, Kyneton | 43–77 | 30–60 | 5 of 8 | roughly $700k–$1.15m |
| D Leafy established suburb | Eltham, Rosanna, Diamond Creek, Heidelberg, Ferntree Gully | 14–34 | 4–19 | 5 of 5 | roughly $850k–$1.45m |
| E Peninsula seaside | Mornington, Mount Martha, Dromana, McCrae, Rosebud, Rye, Arthurs Seat | 40–61 | 3–19 | 0 of 7 | roughly $750k–$1.45m |

Known weak points: ~~Angliss Hospital's 24-hour ED status is unverified (card B)~~ resolved 31 Oct 2026: Eastern Health site says "Emergency department 24 hours a day, 7 days a week" (caveat removed from card B; workbook col Z notes on rows 6, 23, 24, 33 still say "verify", tidy with N3); the Macedon Ranges ED times use Bendigo, not confirmed as nearest (card C); most peninsula times are to Rosebud, a smaller ED that treats less serious cases (card E now says so); train Yes/No is partly recall.

## Rule: profile answers and the 13 uncovered suburbs

R8.4 and R8.5 answers apply only to the 38 suburbs listed against the cards above, and even there only as discussion input until a model spec is approved. The **13 suburbs not covered by any card are never filtered, ranked, promoted, demoted or described using profile answers**: Ringwood, Croydon, Berwick, Newport, West Footscray, Newtown (Geelong), Highton (Geelong), Torquay, Wonthaggi, Warragul, Drouin, Hurstbridge, Frankston South.

Middle-ground test: if nobody picks card D as "most" but nobody picks it as "least" either, it is a compromise, not a preference.

## Bushfire screening gate (task B3-S, not started)

Before any of these 25 suburbs changes status, joins a viewing set, or moves up through new nature weights, record per suburb: Bushfire Prone Area (Yes / Partly / No), Bushfire Management Overlay (most residential streets / edges only / none), source and date; "Needs data" until checked. Suburbs: all of cards B and C, plus Eltham, Hurstbridge, McCrae, Mount Martha, Arthurs Seat. Sources to confirm: VicPlan property reports; better, DataVic overlay data against ABS suburb boundaries. The screening is not a filter; whether high risk rules an area out is a family decision. Since 31 Oct 2026, R8.6 records each person's bushfire tolerance when their most-wanted area is B or C; it is input to that decision and feeds no formula. Adding workbook columns for it needs separate approval.

## For the model spec (not active)

- **Q15.1 (decided 31 Oct 2026):** Q15.1 continues to set nature against the other eight criteria. The R8.3 ladder replaces only the nature-to-family relationship. Q15.1 wording is unchanged on the page.
- Once Mum and Dad answer, their real answers replace the parent proxies; Nish's answers remain Nish's own input. Final household weighting is decided separately.
- With Q10 no longer asked, the current Q10 correction would rest on Nish's Q10 answer alone after the proxies are replaced. The model spec must replace it.
- The ladder-to-weight conversion assumes "very green street" vs "ordinary leafy street" is about 4 nature points (Estimate).
- No convenience or beach ladders as weighting inputs yet (their measures are judgement scores).

## Import (task N3, not active)

New RawResponses columns needed: R8.1, R8.2, R8.3-20, R8.3-30, R8.3-45, R8.3-60, R8.3-75, R8.3, R8.3c, R8.4, R8.5, R8.6 (plus the pending Q3c). Store Q15.1–Q15.10 as the bare letter (A–D), as RawResponses rows 9–15 do; CleanedAnswers C2:C4 counts exact "D". Q10 and Q13d columns stay, empty for v14. TEST records are ignored.

## Other v14 page changes

- Q15.5 label "Emergency department nearby"; help "A quick drive to a public hospital emergency department (open 24 hours)."
- R6.1/R6.2 option D: "Self-contained: own entrance, bathroom, small kitchen and living area (like a granny flat or separate unit), still one household".
- R5.2 help: range wording, no suburb names ("about 10 minutes to about 1½ hours … about half 35 minutes or less; about a third 45 minutes or more").
- Code version 14 everywhere: `PAGE_VERSION = 14`, MODE "v14 trade-offs survey (31 Oct 2026)", draft key `onh-v14-draft-`, WhatsApp header `ONH v14`; other versions are rejected on import.
- Intro: "about 15 minutes".
- Carried over from the live page (it was missing from the folder copy): the signed-in wording ("they save here when you finish"; "Nothing else to do").
- CSS: the hidden attribute now always wins over display rules, so the local copy matches the live page.

## Change after review (31 Oct 2026, user-approved: Gemini review items 1, 2, 3 and bushfire option B)

- R8.6 bushfire question added (above). Q12 B now "A busier street, walking to the shops and doctor" (station removed: it pulled train access into a Village vs Shops & doctor trade-off). Card B: Angliss caveat removed. Card E: "mostly a smaller hospital that treats less serious cases".
- Stored letters for existing questions, branching and PAGE_VERSION 14 unchanged; no v14 answers existed, so no version bump. Live artifact version 1793385715-e1ca, identical to this folder's page source (sha256 5e43c79c8eff).
- Checks: regression suite 0 fails (round trip now 40 answers with R8.6 asked); R8.6 asked only for B/C, stored X for A/D/E, not stored while R8.4 is blank, X when R8.4 changes away from B/C; one question on screen with Back/Next; draft restore on iPhone 13 and iPad (portrait, landscape), no sideways scroll; WhatsApp prefix/invisible-character imports still pass (41 answers when R8.6 is X); v13/v10 still rejected.
- Rebutted review items and reasons: see the chat of 31 Oct 2026 (Card F, About-equal options, length/notes cuts, WhatsApp line hiding, slope question, Q3c wording, townhouse, multiple venues, 60/45-min rescaling, Q15 ranges).

## Bushfire wording (31 Oct 2026, user-approved)

- From bushfire screening B3-S (`research/bushfire/bushfire-screening (31 Oct 2026).md`, Estimate): card B "Most homes here are in bushfire-prone areas with bushfire building and planning rules (early check)"; card C "Bushfire risk varies: some towns have bushfire planning rules across most streets, others only at the edges (early check)"; R8.6 now opens "Some or most of the kind of area you chose is bushfire-prone" (was "Parts of …", which contradicted the new card B).
- Code version 14, stored letters and branching unchanged. Live artifact version 1793421274-e848 (folder source sha256 c7547bc46138). Checks: regression 0 fails, import no errors, R8.6 0 fails; the R8.6 legend still contains "bushfire-prone".

## Checks run (31 Oct 2026, local copy, headless browser at phone width)

All 35 combinations of firm limit and ladder answer gave the expected R8.3, R8.3c and step codes; X/L codes correct; changing an earlier ladder answer re-routes; R8.2 and R8.5 hide and clear the earlier pick; R8.2 stores X when R8.1 = G; one question on screen in parts 4–6 with Back/Next; "I've finished" jumps to the first missing step; skipped questions hidden on screen; WhatsApp export → import round trip identical (39 answers); a v13 message is rejected; no console errors.

## Review round 2 (31 Oct 2026, v15, user-approved Option B)

- Gemini and Perplexity reviewed v15. Applied: intro "about 15–20 minutes"; R8.5 shows the cards again; R6.6 "both the supermarket and the GP". Stored values, branching, PAGE_VERSION 15 unchanged. Live version 1793424601-d805.
- Rebutted (verified against workbook/page): Nish excluded from corrections (false: col M); Q15.2/Q15.10 zero weight (false: Settings B16:B25 unused); R5.2 vs ladder conflict (ladder skips rungs over limit); "D — Essential" breaks COUNTIF (import stores the letter); R8.6 for cards D/E; reorder Priorities first; WhatsApp number; cutting Timing; splitting Q11–Q13; extra gap questions.
- Deferred to the model spec: Q10 row in ForcedChoiceCorrections, wiring R8/Q3c/R5.2/R5.4, 2–1 vote swing size, household weighting.
- To do before import: update `tools/import_v14.py` for v15 (R9 tags); CleanedAnswers B71/E64:E66 when Q7a = B.
