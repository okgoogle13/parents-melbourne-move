# Open work: task register (the only list of open tasks; reviewed 28 Oct 2026)

**Now:** Ready: P4. Pending: workbook G7/H7/Z7 Glen Waverley median update (from the P8 evidence). Blocked: P7 (waits on B4). Awaiting your approval: none.
When a task finishes, mark it here and set the next task ID in `PROJECT_STATE.md`.

Source: scoring-model-pointer.md, workbook headers, Claude_in_Chrome_prompt v2, foundation report, Talking with Mum.
Cloud = a claude.ai/code session on github.com/okgoogle13/parents-melbourne-move (uses the promo credit; expires 4 Nov 2026, 11:59 PM PT).
Rule: one session edits the workbook at a time. Commit and push before a cloud session; `git pull` locally after it.

## Cloud session (claude.ai/code)
| # | Task | Notes |
|---|---|---|
| C1 | **DONE 27 Oct (cloud): all 51 passing rows CHECKED; flags in pointer change log.** Finish suburb source runs (col Z, CHECKED): Sassafras, The Basin, Mount Evelyn, Warrandyte, Hurstbridge, Seaford, Mount Martha, Dromana, Torquay; then the rest of the 51 | 19 of 65 rows have CHECKED notes. ABS QuickStats, Wikipedia, healthdirect, shire sites |
| C2 | **DONE 27 Oct (cloud): SuburbScorecard cols AK–AW.** Demography + migrants: new columns from ABS 2021 QuickStats (median age, % 65+, % overseas-born, % India-born, Indian ancestry, Hinduism/Sikhism, top languages) | Not in the workbook today; only scattered in col Z. Fix the overseas-born definition issue (report item 11) |
| C3 | **DONE 28 Oct (cloud): 13 N/R/V changes; P unchanged pending family decision.** Re-check estimate scores N (nature), P (Indian community), R (village), V (city trip) against C1/C2 evidence | Change only with a source; log every change |
| C4 | ED facts (Chrome prompt Task 3) and "major ED" column for the Peninsula (report item 3). Status unverified — confirm before closing | Hospital websites are readable without Chrome |
| C5 | Train facts (Task 5a–c): station open, frequency, time to Southern Cross. Status unverified — confirm before closing | PTV / V/Line / Wikipedia |
| C6 | Price conflicts (Task 4) from PRD, property.com.au, Microburbs where readable. Status unverified — confirm before closing | realestate.com.au rows stay for Chrome |
| C7 | Rewrite the foundation report: it predates round 2/3, final weights and entered scores ("workbook has no scores" is now wrong). Add demography, prices, stations, ED, top-15 under final weights; .md + .pdf; old version to Archive. **Done 28 Oct:** aligned to workbook commit 7de29d5 (ranks, scores, final weights, top 15); three four-suburb viewing options (each meets the viewing-shortlist rule); drive bases labelled per row; Point Cook Conditional, Tarneit and Mount Waverley Excluded; previous .md/.pdf in Archive. Refreshed 28 Oct to the 10:00 comparator basis (workbook 387763a) | Done |
| C8 | Update scoring-model-pointer.md (stale lines: Mum's 3 Essentials resolved in round 2; status counts) | Every session |
| C9 | **DONE 28 Oct (cloud): draft built.** One-page decision summary and YAML record for 5 Northam St, Glen Waverley (`research/properties/5-northam-street-glen-waverley.md` / `.yaml`), from workbook 387763a and the buying summary PDF (d46e819). One A4 page via `tools/build_property_pdf.sh`. Not added to Listings (user decision). | Gaps in the YAML; review is P8 |

## Claude in Chrome (needs your signed-in browser or live Maps)
| # | Task |
|---|---|
| B1 | Task 1: realestate.com.au under-$1.5M searches (Williamstown, Blackburn, Glen Waverley, Mount Eliza; all four are "Active — needs data" rows) |
| B2 | Task 2: Google Maps "Depart at" drive times (10:00 and 08:00) |
| B3 | Task 6: VicPlan bushfire/flood overlays for 23 listing addresses |
| B4 | Task 7: nearest Indian grocery, Hindu temple **and** church with drive minutes (all passing suburbs, community comparators done 28 Oct for the 6 added rows; Wheelers Hill budget now Checked 28 Oct via Jellis Craig sold-results report; still open: Endeavour Spices and Shri Sanatan Dharam opening hours, both Needs verification and not counted). Feeds the P decision |
| B5 | Listings tab refresh from the "Parents." collection |
| B6 | Suitable-property checks for the 6 Community comparators |
| B7 | Comparator train access — recall-only check of train access for the six Community comparators. Distinct from C5, which covers train facts for passing suburbs |
| B8 | **DONE 29 Oct: a, b, d; c partial** (Jellis Craig report read; realestate.com.au and Domain profiles blocked from cloud). Results in the 5 Northam St YAML. Task 8 (added 28 Oct 2026): evidence on whether Glen Waverley is a family-and-school buyer market (ABS family composition, school zones for 5 Northam St, suburb-profile buyer types), plus a listing-facts check for 5 Northam St. Feeds P8; run before the 14 Nov auction |

## People, not Claude
| # | Task |
|---|---|
| P1 | Talk with Mum: is 25-35 min to Glen Waverley a limit or a preference? (Talking with Mum file). Decides whether coast/Macedon/Gippsland stay in |
| P2 | Family decision: keep the 90-min cap, or make the 60-min preference a filter (it is a preference only now; 11 suburbs would go) |
| P3 | Record answers in Filters; questionnaire page republish only if a new round is needed (needs the claude.ai Artifact tool) |
| P4 | Family review of the parent report draft and the foundation report against the approved workbook. Nothing is published or distributed until the family approves |
| P5 | Q13d answers (reference-only; rows in RawResponses AN / CleanedAnswers 40) |
| P6 | Point Cook travel decision (currently Conditional) |
| P7 | Definition of score P (needs the user's approval; waits on B4) |
| P8 | **DONE 29 Oct: approved by the user.** Review and approve the 5 Northam St decision summary (C9) before the parents see it. Open points: (1)–(2) DONE 29 Oct: suburb-fit line reworded to the ABS 2021 and school-zone evidence; 52.3% reinstated. (3) DONE 29 Oct: Budget bullet uses the realestate.com.au 4-bed median $1,603,000; page table uses the realestate.com.au all-house median $1,675,000; workbook G7 still $1,763,500 (update pending: G7/H7/Z7, recalc, report regeneration); (4) DONE 29 Oct: Statement of Information read: no comparable sales listed; land 677 m² vs listing 581 m² (verify); REIV median $1,750,000. (5) Signed off. Auction Sat 14 Nov 2026, 11:00 am |

## Phase 2 readiness (28 Oct 2026)

**Baseline:** the workbook approved 28 Oct 2026 (six Community comparator rows 67–72, display-only band AX), plus the Wheelers Hill budget update below. Phase 2 has not started; it waits for explicit approval of this workbook.

**Pre-Phase-2 checks**
- A. Wheelers Hill budget: **Checked.** The Jellis Craig Wheelers Hill Suburb Report (Sep 2026, data to 6 Sep 2026) lists houses sold under $1.5M, e.g. 8 Bottlebrush Ct, 4-bed, $1,215,000, 27 Aug 2026. It is an agency sold-results report, not a listing Statement of Information; the two listing SOIs still return HTTP 403.
- B. Endeavour Spices: **Needs verification.** No Google Maps or web listing found. Not counted as community access.
- C. Shri Sanatan Dharam opening hours: **Needs verification.** None published on Google or the web. The society's registered address is Narre Warren North, so the 4–6 min drive is an Estimate.

**Phase 2 rules:** use only approved workbook data; no substantial new research; no location status changes without approval; agree the report structure before building the print-friendly parent report.

**Carried-forward open items:** Now tracked as P2, P5–P7, B6 and B7.

## Comparator fixes (28 Oct 2026)

| Item | Status |
|---|---|
| Comparator J basis | Done: J67–J72 = top of 10:00 weekday range (26, 35, 24, 50, 26, 12); 08:00 kept in Z as peak, not used in J |
| Comparator K (ED) basis | No change needed: K67–K72 were already the top of the 10:00 range |
| Tarneit | Excluded — family decision 28 Oct 2026 (stated reasons: safety concerns and not enough going for it) |
| AX band | Done on every row with ABS data |
| Q13d | Rows added; answers pending |
| Reports | Parent report draft refreshed 28 Oct (comparator drives = workbook J/K, 10:00 basis; marked "Draft — requires family review; not for publication or distribution"). Foundation report (branch claude/inspiring-lovelace-cflq1z) refreshed 28 Oct to the same 10:00 workbook basis (commit 387763a) |

