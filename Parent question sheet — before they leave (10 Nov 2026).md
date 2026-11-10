# Parent question sheet — before they leave (10 Nov 2026)

**Status: DRAFT (P10). Not sent.** Wording is in your voice; check it before use. Answers are recorded in `Family conversations — before parents leave (Nov 2026).md` (P11).

**Use this sheet, not the 6 Nov draft reports.** Those use the 2 Nov weights, which follow your answers more than Mum's and Dad's.

**Goal:** settle the few things that change which suburbs and houses make the shortlist, before they go overseas (mid-Nov).

## What you each already said (v18 survey, 6 Nov)

| Item | Mum | Dad | Nish |
|---|---|---|---|
| Longest drive to Glen Waverley | 25 min | 25 min | 90 min |
| Longest drive to hospital ED | 30 min | 20 min | 20 min |
| Budget (Q3c) | Lower | Lower | Higher, for the right place |
| Price matters | Nice to have | Important | Not needed |
| Beach matters | Nice to have | Not needed | Essential |
| Area types happy to view | Bayside, bush-edge hills, leafy | Leafy only | Bayside, bush-edge hills, peninsula |
| Nish's own space (R6.1) | Bedroom + bathroom | Bedroom + bathroom + sitting room | Bedroom + bathroom |
| Indian grocery, longest drive | 30 min | 20 min | 30 min |
| Train or bus for later (Q14) | Yes | Yes | Yes |

**Already agreed, don't re-ask:** train or bus for later; open to viewing other areas (even if it takes 2–3 months); hospital within 30 min at most; shops and doctor close by.

## Questions (ranked by how much they change the shortlist)

**1. Glen Waverley drive**
- *Ask:* "You both picked 25 minutes as the longest drive to Glen Waverley. Is that a firm no beyond 25, or just what you'd like? Would 35 be OK for the right place?"
- *Note for me:* 25 was the shortest choice on the survey, so it may be a floor, not a hard limit. At 25, 15 of 37 ranked suburbs survive (my count from typed inputs, not recalculated). Affects Filters B4 (G2), Settings B38/B39 (G3), `tools/shortlist.py` scenarios.

**2. Types of area**
- *Ask:* "Dad, you picked leafy suburbs only. Would you look at bush-edge hills or bayside if the house was right?"
- *Note for me:* no area type was ticked by all three. Mum and Dad share only "leafy established". Affects which suburbs are on the saved searches (SL2).

**3. Budget**
- *Ask:* "You both said the budget should be lower. What's the most you'd be comfortable spending?"
- *Note for me:* Filters B2 is $1.5M (B3 $1.59M with costs). Their number may sit well under that. Affects Price weight (T, currently 1%), A-14.

**4. 5 Northam St auction (Sat 14 Nov, 11:00)**
- *Ask:* "5 Northam St is guided at $1.55 to 1.65m. Is it worth bidding on above $1.5m, or do we leave it?"
- *Note for me:* the guide is $50k to $150k over the cap. Rates went up on 3 Nov (4.85%). Affects A-14. Needs a yes/no before Saturday.

**5. Dad's own space**
- *Ask:* "Dad, how much does a sitting room of your own matter, versus just a bedroom and bathroom?"
- *Note for me:* Dad picked bedroom + bathroom + sitting room; Mum and I picked bedroom + bathroom. Affects the floor-plan threshold in Settings B28:B37 (G5).

**6. Beach**
- *Ask:* "How much does being near the beach matter to you? Would you pick a place further from the sea if it was cheaper or closer to Glen Waverley?"
- *Note for me:* Beach is 15% of the score and follows my answers (Essential); Dad said Not needed. Affects U weight (D1 scenarios).

**7. The WhatsApp house list as minimums**
- *Ask:* "The WhatsApp list was 3 to 4 bed, 2.5 bath, no weatherboard, small yard fine. Is that the minimum for both of you? Are stairs OK?"
- *Note for me:* list is from Mum's WhatsApp of 31 Oct (`research/inputs/whatsapp-mum (31 Oct 2026).md`). She wrote "we want", not "minimum", and said nothing about stairs. Filters B6 already allows stairs. Affects G5 and the saved searches (SL2).

**8. Mixed area**
- *Ask:* "Tecoma got ruled out in the WhatsApp because of the mix of people there. Is a mixed area a must, or a strong preference? Is it the same for both of you?"
- *Note for me:* Mum's words (31 Oct): "population is almost 100% white. ( gone we think)". Nish says a diverse area is a must (10 Nov); check Dad agrees. Indian community is 15% of the score but all three rated the community questions mostly "Nice to have". In practice it acts like a veto. Affects P weight and the C-status of Tecoma and similar hills suburbs (any status change needs your approval).

## After the conversation
- Write each answer into the conversations file (question, who, date, their words, cell or task affected).
- Nothing changes in the workbook, weights or filters from this sheet alone. Each change goes through its own approval.
