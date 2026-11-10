# Family conversations — before parents leave (Nov 2026)

**Status: DRAFT.** P12 done. P11 table filled 10 Nov from answers Nish relayed in chat (not yet confirmed directly with Mum and Dad; Q3 and Q7 still open). A-14 is a prefilled note; the decision is the user's.

## A-14 — Auction go/no-go: 5 Northam St, Glen Waverley (auction Sat 14 Nov 2026, 11:00 AEDT)

Facts from `research/properties/5-northam-street-glen-waverley.yaml` (all property fields: agent claims, Needs verification):

| Item | Value | Label |
|---|---|---|
| Price guide | $1,550,000 to $1,650,000 | Checked (what the listing and Statement of Information say) |
| Filters!B2 (hard cap) | $1,500,000 | Checked |
| Filters!B3 (cap incl. costs) | $1,590,000 | Checked (Filters!C3 note: =B2 × 1.06) |
| Guide over B2 | $50,000 (low) to $150,000 (high) | Checked (arithmetic) |
| Budget test | Fails at advertised guide | Checked |
| Stated position (28–29 Oct, P8-approved) | `do_not_bid_at_or_above_guide_without_exceptional_justification` | Author judgement |
| Comparable sales in the agent's statement | None listed | Checked |
| Land size | 581 m² (listing) vs 677 m² (statement) | Needs verification |
| Decision tests still open | comparable sales support walk-away price; filters cap raise approved; better than realistic alternatives; building and pest clear; school zone verified; title, planning and vendor statement clear; 7–10 year hold OK | Needs data |
| RBA cash rate | 4.85% from 4 Nov 2026 (+0.25 from 4.60%; decided 3 Nov) | Checked once M4 is approved and written |
| Parents' budget answer (Q3c) | Both: "Lower: I'd rather spend less". Dollar amount: **blank, filled by P11 question 3** | Needs data |

**Decision (user, before Sat 14 Nov 11:00):** ☑ **No-go** ☐ Go ☐ Raise Filters!B2
**Decided by / date / reason:** Nish, 10 Nov 2026. "Overpriced, they agree" (guide $50k–$150k over the $1.5M cap). Northam St is out; no bid on 14 Nov. Parents' agreement is as relayed by Nish.

## P12 — Mum's WhatsApp lines (done 10 Nov)

Verbatim source: `research/inputs/whatsapp-mum (31 Oct 2026).md` (two messages, 31 Oct 17:46 and 17:58, plus one 1 Nov line on budget). Sender: Mum. The earlier repo note dating it "1 Nov" was wrong; the 1 Nov message is a separate one about Lansell Road.

| # | Line (Mum's words) | Tag |
|---|---|---|
| 1 | "3/4 bedroom house" | G5, SL2 |
| 2 | "no weatherboard" | G5, SL2 |
| 3 | "heating/cooling system" | G5 |
| 4 | "double glazing preferably" | G5 (preference) |
| 5 | "double garage with access to the house preferably" | G5 (preference) |
| 6 | "Two and a half bathrooms" | G5, SL2 |
| 7 | "covered outside area, enough room to convert into a cooking place" | G5 (preference) |
| 8 | "Close to markets and other and Indian grocery stores and restaurants" | D1, SL2 (community, AY, Filters B11) |
| 9 | Tecoma: "population is almost 100% white. ( gone we think)" | C-status (Tecoma, similar hills suburbs), D1. Status change not made; needs approval |
| 10 | "We liked the Northam street house because it has most of the things we want" | A-14 (closed, no-go) |
| 11 | "we don't need a big yard" | G5 land bands, SL2 |
| 12 | "we want to move as soon as possible" | D1 (timing; v18 has no timing question) |
| 13 | "access to public transport, proximity to health care" | D1 (S and O weights) |
| 14 | "We are moving for YOU so we hope that eventually you will live with us." | G5 (living arrangement, R6.1) |
| 15 | 1 Nov: "13 Lansell Road, Glen Waverley. The view is very nice. Outside our price range." | Q3 budget, SL2 price max |

Mum did not say "minimum", and did not mention stairs.

## P11 — Answers (from the P10 sheet)

| # | Question | Who | Date | Their words | Cell or task affected |
|---|---|---|---|---|---|
| 1 | Glen Waverley 25 firm? 35 OK? | Parents (relayed by Nish) | 10 Nov | "35 mins would be OK for the right place" | Filters B4, G2, G3: run the parents' view at 25 and 35 |
| 2 | Area types (Dad: leafy only) | Dad (relayed) | 10 Nov | "Yes" (would look at bush-edge hills or bayside) | SL2: bayside, bush-edge and leafy are now acceptable to all three |
| 3 | Most they'd spend | Parents (relayed by Nish) | 10 Nov | "Willing to spend 10–20% for the right place"; base is $1.5M (Nish, 10 Nov). Nish set the planning figure to **15% above base = $1,725,000** for the right place (the parents' own range was 10–20%, $1.65M–$1.8M); $1.5M otherwise | Price bands in `config/shortlist.json` (SL1); Filters B2 stays $1.5M unless you approve a change (G2) |
| 4 | Northam St: bid above $1.5m? | Parents (relayed) | 10 Nov | "No" | A-14: closed, no-go |
| 5 | Dad: own sitting room? | Nish (relayed) | 10 Nov | "Treat it as nice to have" | G5: sitting room is a nice-to-have, not a minimum |
| 6 | Beach | Nish (relayed) | 10 Nov | Beach matters to Nish. Mum told Nish by phone that her "Nice to have" is because she knows it matters to Nish (Mum's words, relayed). Dad doesn't care | U weight, D1: lower the collective weight but keep a component for how much it matters to Nish |
| 7 | House list as minimums; stairs | Parents (relayed by Nish) | 10 Nov | Stairs OK. Min 3 bedrooms, ideally 4+. Min 2 bathrooms, ideally 2.5 or 3. Weatherboard is a preference: they'd compromise for the right place but prefer not | G5, SL2: see criteria below |
| 8 | Mixed area: must or preference | Parents / Nish (relayed) | 10 Nov | "A diverse multicultural area is a must" | P weight, C-status (Tecoma and similar). A must acts as a filter: needs approval and a definition (D1) |

## Decisions from Nish, 10 Nov 2026 (answers to plan §4a)
1. Weights should be updated to reflect the **collective** priorities in the survey, not Nish's. Route: D1 scenario comparison, then approval before any change.
2. Glen Waverley limit: **display-only view first**, decide after P11 (35 min is OK for the right place).
3. Northam St: dropped.
4. `PROJECT_INSTRUCTIONS.md`: update to match the v18 answers (village feel is no longer Priority 1; regional 1.5 hr is no longer in scope). Not done yet.
5. M4 (RBA refresh on the Northam YAML): **skipped** (Nish, 10 Nov). The macro refresh, with the 4.85% rate from 3 Nov, goes to M4b later.

## Property criteria from Q7 (inputs for G5 and SL2; not applied, G5 needs approval)

| Criterion | Minimum | Ideal | Source |
|---|---|---|---|
| Bedrooms | 3 | 4+ | Q7, 10 Nov (Mum's 31 Oct "3/4 bedroom" is now min 3, ideal 4+) |
| Bathrooms | 2 | 2.5 or 3 | Q7, 10 Nov (Mum's 31 Oct "two and a half" is now the ideal, not the minimum) |
| Weatherboard | Allowed | Avoid | Preference only, not a filter; search without excluding it |
| Stairs | OK | — | Q7; Filters B6 already allows stairs |
| Land | Small yard fine | — | Mum, 31 Oct |
| Sitting room for Dad | Nice to have | — | Q5, 10 Nov |
Saved searches (SL2) should use 3+ bedrooms and 2+ bathrooms, so 2.5 is not a cut-off.
