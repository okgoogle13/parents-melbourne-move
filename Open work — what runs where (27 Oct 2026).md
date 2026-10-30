# Open work: task register (the only list of open tasks; reviewed 28 Oct 2026)

**Now:** Done 30 Oct: N2 workbook intake. Awaiting your approval: G3 (M/O decoupling) and G1 (republish the questionnaire for rounds 5–6). P4 order is still your decision (plan recommends rounds 5–6 first). Done 29 Oct: workbook Glen Waverley median update (5704d65), reports refreshed. Blocked: P7 (waits on B4). Awaiting your approval: M1–M3 and M5 (proposed 29 Oct).
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
| C10 | **DONE 30 Oct (cloud, branch claude/n1-questionnaire-design): rounds 5–7 design doc; merged to main 30 Oct (7f7d1c6).** N1: rounds 5–7 questionnaire design doc, plus register and `PROJECT_STATE.md` updates. Documentation only | Plan: revision 3 + revision 4 routing (local `~/.claude/plans/`); prompt `cloud-kickoff-prompt-N1.md`. Review the branch locally before merging |

## Macro research integration (proposed 29 Oct 2026; awaiting approval)
Task 1 of the handover (local-only `research/inputs/parents-melbourne-move-handover.md`) is partly done: macro YAML, sources, snapshot, freshness rules, schemas, validator (`tools/validate_macro.py`, 0 errors 29 Oct) and the 5 Northam St summary. Still missing below. Only the PDF `research/inputs/Melbourne_Established_House_Buying_Summary.pdf` is a source; no new research.

| # | Task | Notes |
|---|---|---|
| M1 | `research/macro/macro-impact-review.md`: file-by-file consistency review of root reports, pointer, instructions and the 5 Northam St page against the macro YAML (statuses per handover §6). Proposes edits; changes nothing | Do first; M2–M3 use its findings |
| M2 | Parent-facing `research/macro/macro-market-conditions.md` + printable PDF built from the macro YAML (reuse `tools/build_pdf.sh`) | Before 3 Nov: freshness flips to review_due after the RBA decision; cloud credit ends 4 Nov |
| M3 | Agent ingestion note: a short "Macro data" section in `docs/workflow.md` (what is canonical, run the validator, freshness statuses), linked from CLAUDE.md "Read on demand" | Not a separate AGENTS.md |
| M4 | Re-check after the 3 Nov RBA decision: update `macro-market-conditions.yaml` + new snapshot only from a named source, or mark review_due | Trigger in `research/macro/freshness.yaml` |
| M5 | Decision: drop the handover's `research/suburbs/suburb-shortlist.yaml/.md` and Task 2 (full repo refactor). The suburb file would duplicate the workbook with conflicting PDF figures (e.g. Frankston $860k vs workbook $834,296); its modelled forecast ranges can be listed in M1 as display-only gaps | Recommended: drop both |

## Claude in Chrome (needs your signed-in browser or live Maps)
| # | Task |
|---|---|
| B1 | Task 1: realestate.com.au under-$1.5M searches (Williamstown, Blackburn, Glen Waverley, Mount Eliza; all four are "Active — needs data" rows) |
| B2 | Task 2: Google Maps "Depart at" drive times (10:00 and 08:00) |
| B3 | Task 6: VicPlan bushfire/flood overlays for 23 listing addresses |
| B4 | Task 7: nearest Indian grocery, Hindu temple **and** church with drive minutes (suburbs passing the approved filters, community comparators done 28 Oct for the 6 added rows; Wheelers Hill budget now Checked 28 Oct via Jellis Craig sold-results report; still open: Endeavour Spices and Shri Sanatan Dharam opening hours, both Needs verification and not counted). Feeds the P decision |
| B5 | Listings tab refresh from the "Parents." collection |
| B6 | Suitable-property checks for the 6 Community comparators |
| B7 | Comparator train access — recall-only check of train access for the six Community comparators. Distinct from C5, which covers train facts for passing suburbs |
| B8 | **DONE 29 Oct: a, b, d; c partial** (Jellis Craig report read; realestate.com.au and Domain profiles blocked from cloud). Results in the 5 Northam St YAML. Task 8 (added 28 Oct 2026): evidence on whether Glen Waverley is a family-and-school buyer market (ABS family composition, school zones for 5 Northam St, suburb-profile buyer types), plus a listing-facts check for 5 Northam St. Feeds P8; run before the 14 Nov auction |
| B9 | Floorplan/listing-fit fields for the 32 listings (Listings X–AG; design doc `Questionnaire redesign — rounds 5–7 (29 Oct 2026).md` section 5) |

## People, not Claude
| # | Task |
|---|---|
| P1 | Talk with Mum: is 25-35 min to Glen Waverley a limit or a preference? (Talking with Mum file). Decides whether coast/Macedon/Gippsland stay in → covered by rounds 5–7 (see P9 / G1 / G2 / G6) |
| P2 | Family decision: keep the 90-min cap, or make the 60-min preference a filter (it is a preference only now; 11 suburbs would go) → covered by rounds 5–7 (see P9 / G1 / G2 / G6) |
| P3 | Record answers in Filters; questionnaire page republish only if a new round is needed (needs the claude.ai Artifact tool) → covered by rounds 5–7 (see P9 / G1 / G2 / G6) |
| P4 | Family review of the parent report draft and the foundation report against the approved workbook. Nothing is published or distributed until the family approves |
| P5 | Q13d answers (reference-only; rows in RawResponses AN / CleanedAnswers 40) → covered by rounds 5–7 (see P9 / G1 / G2 / G6) |
| P6 | Point Cook travel decision (currently Conditional) |
| P7 | Definition of score P (needs the user's approval; waits on B4) → covered by rounds 5–7 (see P9 / G1 / G2 / G6) |
| P8 | **DONE 29 Oct: approved by the user.** Review and approve the 5 Northam St decision summary (C9) before the parents see it. Open points: (1)–(2) DONE 29 Oct: suburb-fit line reworded to the ABS 2021 and school-zone evidence; 52.3% reinstated. (3) DONE 29 Oct: Budget bullet uses the realestate.com.au 4-bed median $1,603,000; page table uses the realestate.com.au all-house median $1,675,000; workbook G7 updated to $1,675,000 29 Oct (5704d65; recalc passed; reports refreshed); (4) DONE 29 Oct: Statement of Information read: no comparable sales listed; land 677 m² vs listing 581 m² (verify); REIV median $1,750,000. (5) Signed off. Auction Sat 14 Nov 2026, 11:00 am |
| P9 | Family answers to rounds 5–6 (includes P5 Q13d) |

## Rounds 5–7 local steps (29 Oct 2026)
From `Questionnaire redesign — rounds 5–7 (29 Oct 2026).md` sections 6–7. Each gate is asked once, when its inputs exist.

| # | Change | When to ask | Depends on | Status |
|---|---|---|---|---|
| N2 | Workbook intake, one edit: RawResponses AO1:BE1 headers; CleanedAnswers rows 41–71; Settings A27:D39 (column B blank); Listings X1:AG1 headers plus AA/AG formulas filled down rows 2–33 (AG = "Pending rules"); SuburbScorecard AY1:BB1 and BF1 headers (empty); DiscussionSummary A40:F52 display block (no count). Recalc and diff | Not gated (intake) | None in the plan; G1 and G3 follow it | **DONE 30 Oct** (recalc and diff passed; see pointer change log) |
| N3 | Import round 5–6 answers per the design doc's Storage rule; recalc and diff | Not gated (intake); after all three answer | P9, N2 | not started, runs locally, needs approval where gated |
| N4 | Write `CleanedAnswers!H59`/`H61` and the DiscussionSummary counts; re-run the dry run with real E59/E61 | After N3, with approval | N3 | not started, runs locally, needs approval where gated |
| G1 | Republish the questionnaire (round-4 page archived first; R5/R6 items added; Q13d kept; Q4, Q4b, Q5, Q6, Q7, Q7b retired; R5.6, R5.7, R6.2 validation checks; mode label `round 5–6 (R5, R6, Q13d)`) | After N2 | N2 | not started, runs locally, needs approval where gated |
| G2a/G2b | `Filters!B4` / `Filters!B5`, incl. no-cap or backstop choice | After N4 | N4; G3 before G2 | not started, runs locally, needs approval where gated |
| G3 | M/O decoupling, Settings B38/B39 = 90 | After N2 (before G2) | N2 | not started, runs locally, needs approval where gated |
| G4 | L re-evaluation, plus any C status change (incl. R7.4 vetoes) | After G2 | G2a/G2b | not started, runs locally, needs approval where gated |
| G5 | Settings B28:B37 property thresholds | After N3 | N3 | not started, runs locally, needs approval where gated |
| G6 | Switch P to the design-doc formula, incl. the R5.7 church basis (closes P7) | After task B4 data is complete for surviving suburbs | B4 | not started, runs locally, needs approval where gated |
| G7 | Regenerate reports (`tools/report2.py`; `tools/found.py` needs fixing first) | Last | None stated; runs last | not started, runs locally, needs approval where gated |

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

