# Task: one-page decision summary for 5 Northam Street, Glen Waverley

Work in the local folder `/Users/okgoogle13/Projects/Parents Melbourne MOVE/` (git origin `okgoogle13/parents-melbourne-move`, current branch `macro-research-integration`). Use plan mode: inspect, propose a short plan, stop for my approval, then build and verify.

## Goal

A parent-facing, one-page summary that makes my case for caution on this house, plus a matching YAML record. The position is set (see "Recommended position"). Your job is to make every fact in it correct, sourced and labelled. Do not change the position. If the evidence contradicts a sentence below, do not soften or delete it silently: flag it in the plan.

The page states its position openly. It is a decision framework, not a valuation or financial advice.

## Read first (only the parts you need)

1. `CLAUDE.md`, `PROJECT_STATE.md`, `PROJECT_INSTRUCTIONS.md`, `Open work — what runs where (27 Oct 2026).md`.
2. Workbook `Our Next Home — Family Relocation Scoring Model.xlsx`:
   - `Filters`: B2 (purchase cap), B3 (total ceiling incl. costs), B4 (max drive to GW), Q6 stairs row, Q7 garden row, drive-time basis row.
   - `SuburbScorecard` cols A, C, G, H, J, L for the seven suburbs in the table below.
   - `Listings`: headers and formula logic for cols G and T.
3. `research/inputs/Melbourne_Established_House_Buying_Summary.pdf`: macro outlook, the $1.5m scenario, and the suburb "advantage" wording.
4. `Suburb shortlist foundation report.md`: Glen Waverley median age 40 and 52.3% couples with children. Cite the section.

Authority: workbook > `scoring-model-pointer.md` > PDF and reports. Suburb prices, statuses and drive times come from the workbook. The PDF's suburb medians differ (e.g. Frankston $860k in the PDF, $834,296 in the workbook): use the workbook figures and list the differences in Gaps.

## Listing facts (agent claims unless stated)

- 5 Northam Street, Glen Waverley VIC 3150. House. Listing ID 152636156: https://www.realestate.com.au/property-house-vic-glen+waverley-152636156
- Listed 15 Oct 2026. Agents Natalie Visic and Alan Zhang, Jellis Craig Glen Waverley.
- Guide $1,550,000–$1,650,000. Auction Sat 14 Nov 2026, 11:00 am.
- 581 m² land. 4 bed, 2 bath, 2 car (double garage, internal access).
- Two-level: bedrooms upstairs (master with parents' retreat and ensuite, family bathroom), rumpus, lounge/dining, kitchen, laundry, ground-floor powder room.
- Covered alfresco, north-facing backyard, lawns, established gardens, irrigation. Ducted heating, evaporative cooling, split system, video intercom.
- Claims: "renovated"; close to Mount View Primary, Jells Park, Glen Waverley Station, The Glen, major roads.
- Not disclosed: floor area, year built, auction location, price history, solar, water tanks, vendor statement, renovation permits, building/pest report.

## Fact rules (the family decision record)

- **Budget:** `Filters!B2` is a confirmed **hard cap** of $1,500,000 purchase price (27 Oct), not "approximately". Bidding above it is a Filters change and needs the family's explicit approval.
- **Stairs are allowed** (Q6, corrected 27 Oct). Do not argue against the house on stairs or "ageing in place on two levels".
- **Family proximity:** the house is in Glen Waverley (0 min). State this once, as its main strength. Leaving it out would misstate the case.
- **Community access is secondary** in the brief. Keep the community bullet, but put it last.
- Label every number **Checked**, **Estimate**, **Needs verification** or **Needs data**, with its basis ("SOI median, 1 Jul 2025–30 Jun 2026"; "AVM, not a sale median"; drive times "Google Maps, typical traffic, 26 Oct 2026, not peak").
- Use "the listing claims", "evidence suggests", "requires verification". Do not say the house is overpriced: say the guide exceeds the cap and comparable sales are needed.
- No web research. Do not invent comparable sales, values, forecasts, sources, URLs or dates. Out of scope: ownership structure, title, duty, concessions, guarantors, Centrelink, CGT, estate planning.

## Output 1: `research/properties/5-northam-street-glen-waverley.md`

One A4 page when printed. Use this text. Confirm every number against its source first. `[brackets]` = fill from the source.

```markdown
# Property decision summary
## 5 Northam Street, Glen Waverley

**Price guide:** $1,550,000–$1,650,000
**Sale method:** Auction, Saturday 14 November 2026 at 11:00 am
**Property:** 4 bed, 2 bath, 2 garage, 581 m², two-level family house (renovated, as the listing claims)
**Parents' budget cap:** $1,500,000 purchase price (family decision, 27 Oct 2026)

## Bottom line

- **Budget:** The guide starts $50,000 above the parents' $1.5m cap and tops out $150,000 above it. Glen Waverley's house median is $1,763,500 [basis].
- **Market timing:** Evidence suggests Melbourne house prices will keep weakening into the first half of 2027, with a likely trough around mid-2027.
- **Suburb fit:** Glen Waverley is primarily a family-and-school market, so expect competition from school-motivated buyers at auction.
- **Location:** Its clear strength: the family is already in Glen Waverley.
- **Nature fit:** Jells Park is nearby, but Wheelers Hill shares it at a lower median, and Endeavour Hills, Frankston and Seaford offer stronger or more affordable nature access.
- **Community fit (secondary priority):** Glen Waverley has strong general amenities. Springvale, Clayton South, Keysborough and Endeavour Hills offer a stronger Indian-community connection.
- **Recommendation:** Do not bid at or above the guide unless independent comparable sales justify it and the family deliberately raises the cap.

## Why caution is warranted

The guide is above the cap before any auction competition. The buying summary's base case puts a $1.5m house at about $1.41m–$1.44m at the mid-2027 trough, a further fall of about 4–6%. The same fall on a $1.6m purchase is about $64,000–$96,000 (Estimate), against $60,000–$90,000 on a $1.5m one.

## Suburb and lifestyle fit

Glen Waverley's median age is 40, and 52.3% of families are couples with children [source]. It is primarily a family-and-school market. The house suits a family; the parents should ask whether a four-bedroom house with lawns and established gardens to maintain fits how they want to live for the next 10 years.

## Alternatives

| Suburb | Workbook status | House price (basis) | Drive to GW | Main advantage |
|---|---|---:|---:|---|
| Glen Waverley | Active shortlist | $1,763,500 (sale median) | 0 min | Family already here; amenity and schools |
| Wheelers Hill | Community comparator | $1,475,000 (SOI median) | 12 min | Family proximity and Jells Park |
| Endeavour Hills | Community comparator | $857,000 (SOI median) | 26 min | Bushland and community access |
| Frankston | Active shortlist | $834,296 (sale median) | 25 min | Beach, reserves and train access |
| Seaford | Watchlist | $861,235 (AVM, not a sale median) | 24 min | Coastal and wetland lifestyle |
| Springvale | Community comparator | $942,500 (SOI median) | 26 min | Strong Indian-community connection |
| Keysborough | Community comparator | $975,000 (SOI median) | 24 min | Community access and family housing |

Suburb medians are not like-for-like with one renovated house; they show where the budget goes further. Drive times: Google Maps, typical traffic, 26 Oct 2026, not peak.

## Decision test: proceed only if all are true

1. Independent settled comparable sales support a written walk-away price.
2. The family deliberately approves raising the $1.5m cap.
3. The house is genuinely better than realistic alternatives on the shortlist.
4. A building and pest inspection shows the renovation is more than cosmetic.
5. The Mount View Primary zone claim is independently verified.
6. Title, planning overlays, easements and the vendor statement show no material issues.
7. The parents are comfortable holding the property for at least 7–10 years.

## Recommended position

**Do not bid simply because the house is appealing.** Treat it as a high-discipline exception, not a default purchase. Set a hard walk-away price before auction day from recent settled comparable sales. If the house does not clearly beat realistic alternatives on price, nature access and long-term fit, keep searching: Wheelers Hill, Endeavour Hills, Frankston, Seaford and Springvale.

*Decision framework only, not a valuation or financial advice. Built from workbook commit [hash], 28 Oct 2026.*
```

## Output 2: `research/properties/5-northam-street-glen-waverley.yaml`

Valid YAML. Values must match the Markdown.

```yaml
meta:
  prepared_on: 2026-10-28
  workbook_commit: "<hash from git log>"
  status: draft_requires_family_review
  position: caution_set_by_author   # stance stated, not derived
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
  levels: two                      # agent description
  renovation: agent_claim_unverified

assessment:
  purchase_cap_aud: 1500000        # Filters!B2, hard cap
  guide_low_over_cap_aud: 50000
  guide_high_over_cap_aud: 150000
  budget_test: fail_at_advertised_guide
  drive_to_gw_min: 0
  stairs_filter: pass              # Filters Q6
  market_timing: further_weakness_plausible_into_h1_2027
  likely_trough: mid_2027
  suburb_fit:
    family_school_market: true
    retiree_led_market: false
    nature_access: good_but_not_superior     # judgement, not workbook-scored
    indian_community_fit: partial            # judgement; secondary priority
  recommendation: do_not_bid_at_or_above_guide_without_exceptional_justification
  approval_required: true

decision_tests: [comparable_sales_support_walk_away_price, filters_cap_raise_approved,
  property_superior_to_realistic_alternatives, building_and_pest_clear,
  school_zone_verified, title_planning_vendor_statement_clear, hold_7_to_10_years_ok]

alternatives:   # one entry per table row: suburb, workbook_status, price_aud, price_basis, drive_to_gw_min, advantage
gaps: []        # undisclosed listing items; PDF vs workbook differences; Vermont South not on scorecard
```

## Plan-mode deliverable (then stop)

- Confirm each file and workbook range exists.
- Table: every number in the draft text → its source cell or page → label. Mark any that don't match.
- List any sentence in the set text that the evidence contradicts, with the source.
- Approval item: whether to add this listing as a row in the `Listings` tab (no workbook write until I say yes).
- Then wait.

## After approval: build and verify

- Read computed cells from a recalculated temp copy (`docs/workflow.md`).
- `python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))"` on the YAML.
- Render the Markdown to an A4 PDF (pandoc, or a script in `tools/`) and confirm the page count is 1. If it runs over, trim "Suburb and lifestyle fit" first. Never trim the decision tests or the table.
- Add the task to the register and set the next task ID in `PROJECT_STATE.md`. Do not commit or push unless I ask.
- Finish with: files created, validation results (YAML parse, page count, number trace), gaps, approvals still needed. Not for distribution to the parents until I approve it.
