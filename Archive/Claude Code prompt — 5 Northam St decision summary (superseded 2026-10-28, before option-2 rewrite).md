# Task: one-page decision summary for 5 Northam Street, Glen Waverley

Work in the local folder `/Users/okgoogle13/Projects/Parents Melbourne MOVE/` (git origin `okgoogle13/parents-melbourne-move`, current branch `macro-research-integration`). Use plan mode: inspect, propose a short plan, stop for my approval, then build and verify.

## Goal

A neutral, parent-facing decision summary for one listing, plus a matching YAML record. It tests the house against the family's recorded decisions. It is a decision framework, not a valuation or financial advice. Do not start from a verdict; let the tests produce it.

## Read first (only the parts you need)

1. `CLAUDE.md`, `PROJECT_STATE.md`, `PROJECT_INSTRUCTIONS.md`, `Open work — what runs where (27 Oct 2026).md`.
2. Workbook `Our Next Home — Family Relocation Scoring Model.xlsx`:
   - `Filters`: B2 (purchase cap), B3 (total ceiling incl. costs), B4 (max drive to GW), B5 (max drive to ED), Q6 stairs row, Q7 garden row.
   - `SuburbScorecard` cols A, C, G, H, J, K, L, AB for: Glen Waverley, Wheelers Hill, Endeavour Hills, Frankston, Seaford, Springvale, Keysborough.
   - `Listings`: headers and formula logic for cols G and T (budget and overall check).
3. `research/inputs/Melbourne_Established_House_Buying_Summary.pdf` — macro outlook and the $1.5m scenario only.
4. `Suburb shortlist foundation report.md` — Glen Waverley demographics (median age, couples-with-children share). Cite the section.

Authority when sources disagree: workbook > `scoring-model-pointer.md` > the PDF and reports. Suburb prices, statuses and drive times come from the workbook, with their price basis. Use the PDF only for the macro outlook. Where the PDF and workbook differ, use the workbook figure and list the difference in Gaps.

## Listing facts (agent claims unless stated)

- 5 Northam Street, Glen Waverley VIC 3150. House. Listing ID 152636156: https://www.realestate.com.au/property-house-vic-glen+waverley-152636156
- Listed 15 Oct 2026. Agents Natalie Visic and Alan Zhang, Jellis Craig Glen Waverley.
- Guide $1,550,000–$1,650,000. Auction Sat 14 Nov 2026, 11:00 am.
- 581 m² land. 4 bed, 2 bath, 2 car (double garage, internal access).
- Two-level layout: bedrooms upstairs (master with parents' retreat and ensuite, family bathroom), rumpus, lounge/dining, kitchen, laundry, ground-floor powder room. No ground-floor bedroom or full bathroom is listed.
- Covered alfresco, north-facing backyard, lawns, established gardens, irrigation.
- Ducted heating, evaporative cooling, split system, video intercom.
- Claims: "renovated"; close to Mount View Primary, Jells Park, Glen Waverley Station, The Glen and major roads.
- Not disclosed: floor area, year built, auction location, price history, solar, water tanks, vendor statement, renovation permits, building/pest report.

## Framing rules (these come from the family decision record)

- **Budget is a hard cap.** `Filters!B2` is a confirmed $1.5m maximum purchase price, not a preference. Report the guide against it in dollars. Going above it is a change to the Filters tab, which needs the family's explicit approval. Present it as that, not as "a deliberate budget revision".
- **Stairs are allowed** (Q6, corrected 27 Oct). Do not treat two storeys as a failure. You may note, as a consideration only, that there is no ground-floor bedroom or full bathroom.
- **Family proximity is a hard filter and this house is in Glen Waverley.** State that plainly as its main strength. Every alternative shows its drive to GW.
- **Nature is priority 1; cultural or community access is secondary** (20–35 min drive is fine). Do not frame any alternative around one community or institution.
- Glen Waverley's buyer mix (family and school market) is context for auction competition and resale. It is not a suitability verdict.
- Every number carries a label: **Checked**, **Estimate**, **Needs verification** or **Needs data**, and its basis ("SOI median, 1 Jul 2025–30 Jun 2026"; "AVM, not a sale median").
- Allowed phrasing: "the listing claims", "evidence suggests", "requires verification". Do not say the house is overpriced. Do not invent comparable sales, values, forecasts, sources, URLs or dates.
- Out of scope: ownership structure, title, stamp duty, concessions, guarantors, Centrelink, CGT, estate planning.
- No web research. If a gap needs research, list it; do not fill it.

## Outputs

Create these two files, and only these:

### 1. `research/properties/5-northam-street-glen-waverley.md`

One A4 page when printed. Plain English for my parents. Sections:

1. **Header:** address, guide, auction date and time, configuration, parents' cap (`Filters!B2`).
2. **Bottom line (5–6 bullets):** budget (guide vs cap in $, with the Listings check result); family proximity; nature (Jells Park, compared with the alternatives); market timing (PDF base case, one line); buyer competition; one-line position that follows from the tests.
3. **Market timing (2–3 sentences):** the PDF's $1.5m → ~$1.41m–$1.44m base case (about 4–6%). Apply the same percentage to $1.55m and $1.65m, show the arithmetic, and label it **Estimate**.
4. **Alternatives table**, from the workbook. Columns: Suburb | Workbook status | House price (basis) | Drive to GW | Main advantage | Main trade-off. Rows: Glen Waverley (the suburb, as baseline), Wheelers Hill, Endeavour Hills, Frankston, Seaford, Springvale, Keysborough. Show the status as it is recorded ("Community comparator", "Watchlist") and do not imply these are ranked shortlist picks. No "likely outcome" column: comparing one listing with suburb medians is not like-for-like, so say that in a one-line note under the table.
5. **Decision tests (proceed only if all are true):**
   1. The family approves a change to `Filters!B2` above the guide's low end.
   2. Independent settled comparable sales support a written walk-away price.
   3. Building and pest inspection shows the renovation is more than cosmetic.
   4. Title, planning overlays, easements and vendor statement show no material issues.
   5. The Mount View Primary zone claim is verified (resale relevance only).
   6. The parents are comfortable holding for 7–10 years.
   7. The house beats realistic alternatives on the family's recorded priorities, not only on location.
6. **Gaps:** undisclosed items, PDF–workbook figure differences, Vermont South (in the brief but not on the scorecard), anything labelled **Needs data**.
7. One-line footer: "Decision framework only, not a valuation or financial advice. Built from workbook commit `<hash>` on 28 Oct 2026."

### 2. `research/properties/5-northam-street-glen-waverley.yaml`

Valid YAML. Values must match the Markdown.

```yaml
meta:
  prepared_on: 2026-10-28
  workbook_commit: "<hash from git log>"
  status: draft_requires_family_review
  property_decision: requires_further_evidence_before_bidding
  sources:
    - id: realestate_listing_152636156
      url: https://www.realestate.com.au/property-house-vic-glen+waverley-152636156
    - id: melbourne_established_house_buying_summary_pdf
      path: research/inputs/Melbourne_Established_House_Buying_Summary.pdf
    - id: scoring_workbook
      path: "Our Next Home — Family Relocation Scoring Model.xlsx"
    - id: suburb_shortlist_foundation_report
      path: Suburb shortlist foundation report.md

property:
  address: 5 Northam Street, Glen Waverley VIC 3150
  listing_id: "152636156"
  property_type: house
  price_guide_aud: {low: 1550000, high: 1650000}
  sale_method: auction
  auction: 2026-11-14T11:00:00+11:00
  land_m2: 581
  bedrooms: 4
  bathrooms: 2
  car_spaces: 2
  levels: two            # agent description; exact count not disclosed
  ground_floor_bedroom: not_listed
  renovation: agent_claim_unverified

assessment:
  purchase_cap_aud: 1500000            # Filters!B2, hard cap
  guide_low_over_cap_aud: 50000
  guide_high_over_cap_aud: 150000
  listings_budget_check: over_cap      # matches Listings col G logic
  drive_to_gw_min: 0
  stairs_filter: pass                  # Filters Q6: stairs allowed
  market_outlook: further_weakness_into_h1_2027_trough_mid_2027   # PDF base case
  buyer_market: family_and_school
  recommendation: do_not_bid_above_cap_without_approved_filters_change
  approval_required: true

decision_tests: [filters_cap_change_approved, comparable_sales_support_walk_away_price,
  building_and_pest_clear, title_planning_vendor_statement_clear,
  school_zone_verified, hold_7_to_10_years_ok, beats_realistic_alternatives]

alternatives:   # one entry per table row: suburb, workbook_status, price_aud, price_basis, drive_to_gw_min, advantage, trade_off
gaps: []        # mirror the Markdown Gaps section
```

## Plan-mode deliverable (then stop)

- Confirm each file and workbook range above exists. List any that do not.
- Show the values you will use, each with its cell reference and label.
- List PDF–workbook conflicts and how you will resolve each one.
- Approval items: (a) whether to add this listing as a row in the `Listings` tab (no write until I say yes); (b) any wording that reads as a recommendation to the parents.
- Then wait.

## After approval: build and verify

- Recalculate on a temp copy (see `docs/workflow.md`) to read the computed cells. Do not edit the workbook unless approved in (a).
- `python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))"` on the YAML.
- Render the Markdown to an A4 PDF (pandoc, or an existing script in `tools/`) and confirm it is one page by page count. Trim the wording, not the decision tests, if it runs over.
- Cross-check every number in both files against its source. Report any number you could not trace.
- Add the task to the register and set the next task ID in `PROJECT_STATE.md`. Do not commit or push unless I ask.
- Finish with: files created, validation results (YAML parse, page count, number trace), open gaps, approvals still needed. Nothing is for distribution to the parents until I approve it.
