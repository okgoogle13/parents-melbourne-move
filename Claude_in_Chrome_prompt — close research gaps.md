# Claude in Chrome prompt — close research gaps (v2, 27 Oct 2026; Task 8 added 28 Oct 2026)

Replaces v1 (in Archive/). v1 Tasks 1–3 (collection read, drive times, prices) are DONE and already in the workbook; they are removed here.
v2 covers the gaps found by the 27 Oct research report ("Suburb shortlist foundation report.pdf"): property searches, ED/drive-time errors, price conflicts, train checks, hazard overlays, Indian grocery / worship access.
Paste everything below the line into Claude in Chrome. It only collects facts; results are written into the workbook afterwards, with sources. Run Tasks 1–3 first (they need realestate.com.au / Maps and go stale); 4–7 can follow.
Task 8 (added 28 Oct 2026, register B8) checks the 5 Northam St summary before the auction on Sat 14 Nov 2026; run it first if time is short.
Mount Eliza is no longer searched: the Parents. collection already holds 3 listings under $1.5M there (54 Granya Grove, 110 Koornalla Crescent, 1374 Nepean Highway).

---

Research task for my parents' Melbourne move. You are collecting facts in the browser. Work in a new tab. Report back after each task, then continue.

RULES
- Read-only. Don't open, create or edit any Google Docs, Sheets, Forms or Drive files. Don't contact agents, enquire, save searches, or submit any form.
- I'm signed in to realestate.com.au. If any other site asks you to sign in, or shows a CAPTCHA, skip it and note it.
- Every value needs: source URL, date/time read, and a tag: Checked (read directly on the page) or Estimate (your inference). Never tag a guess as Checked.
- If you can't find a value in 2 tries, write "not found" and move on.
- Don't summarise or recommend suburbs. Just the data.

TASK 1 — Can we buy under $1.5M? (realestate.com.au)
Buy search, one suburb at a time (surrounding suburbs OFF), House + Townhouse, 3+ bedrooms, max price $1,500,000. Don't save the search.
Suburbs: Williamstown, Blackburn, Glen Waverley.
Record: number of results, then up to 5 listings: Address | Price guide | Beds | Land m² | Single or double storey (only if stated) | URL

TASK 2 — Drive times at consistent times (Google Maps, Driving, "Depart at")
Set "Depart at" to the next weekday at 10:00 (off-peak) and again at 08:00 (peak). Start point: the suburb itself (search "<Suburb> VIC").
a) to "Glen Waverley VIC 3150" for: Wonthaggi, Torquay, Warburton, Healesville, Woodend, Mount Evelyn, Frankston South, Chelsea.
b) to the Peninsula's major 24-hour ED, "Frankston Hospital" (Peninsula Health), for: Rosebud, Rye, McCrae, Dromana, Mount Martha, Arthurs Seat, Mornington, Mount Eliza, Frankston South, Chelsea.
c) to "Maroondah Hospital" for Healesville, Yarra Glen, Warburton.
Record the first time Maps shows in minutes plus the range if shown.
Table: Suburb | Destination | Depart time | Min | Range | Map URL | Tag

TASK 3 — Emergency department facts (hospital's own website or health service page)
Confirm: is there a 24-hour emergency department, and what level of cases does it take? Hospitals: West Gippsland Hospital (Warragul), Rosebud Hospital, Frankston Hospital, Maroondah Hospital, Angliss Hospital, Casey Hospital, Wonthaggi Hospital, University Hospital Geelong, Bendigo Hospital. Urgent care centres don't count.
Table: Hospital | 24-hr ED yes/no | Notes (e.g. minor/moderate only) | URL | Tag

TASK 4 — Median house price conflicts (realestate.com.au suburb profile, 12-month house median; OnTheHouse if easier)
Suburbs: Highton, Woodend, Macedon, Newtown (Geelong), Ferntree Gully, Upper Ferntree Gully, Mount Eliza, Mornington, Warrandyte, Rosanna, Croydon, Hurstbridge, Belgrave, Tecoma.
Table: Suburb | House median $ | Unit median $ | Period | No. of sales | Source | URL | Tag

TASK 5 — Train access (ptv.vic.gov.au; vline.com.au for regional)
a) Is the station open and in service now? Croydon (level-crossing works), Gisborne (is there a station in Gisborne or only New Gisborne?), Riddells Creek, Macedon, Woodend, Kyneton, Drouin, Warragul.
b) For each V/Line station above: typical weekday trains per hour/day and journey time to Southern Cross.
c) Nearest station and line, and in suburb / within ~2 km / none nearby, for: Ferntree Gully, Mentone, Mordialloc, Chelsea, Seaford, Altona, Newport, West Footscray, Rosanna, Hurstbridge, Berwick.
Table: Suburb | Station | Line | In suburb / ~2 km / none | Weekday frequency | Min to Southern Cross | URL | Tag

TASK 6 — Bushfire and flood overlays (VicPlan, planning.vic.gov.au; "Planning Maps")
Look up each address below. Record whether it is in a Bushfire Management Overlay (BMO), a designated bushfire prone area, and any flood overlay (LSIO, FO, SBO). Read only; don't download certificates.
Addresses (from my saved listings): 67 Donna Buang Road Warburton; 24 Monbulk Road, 16 Forest Road, 3 Forest Road, 11 Dalkeith Crescent, 84 Belgrave Gembrook Road Belgrave; 7 Gordon Avenue and 85 Terrys Avenue Tecoma; 29 Campbell Street Diamond Creek; 28 Stradbroke Avenue, 2 Bader Court, 35 Mountain Avenue Frankston South; 54 Granya Grove, 110 Koornalla Crescent, 1374 Nepean Highway Mount Eliza; 4 McArthur Street Dromana; 36 Arthurs Avenue McCrae; 23 Sherwood Crescent Mount Martha; 6 Beales Street and 13 Harcombe Crescent Torquay; 1/192 Nepean Highway Seaford; 3 Fiocchi Avenue Frankston.
Table: Address | Suburb | BMO yes/no | Bushfire prone area yes/no | Flood overlay (type or none) | URL | Tag

TASK 7 — Community access (Google Maps search, Driving, "Leave now") [updated 28 Oct 2026]
For each suburb, search from the suburb centre and record the NEAREST of each, with name, address and drive minutes. Required for every suburb (all three):
a) "Indian grocery" b) "Hindu temple" c) "church"
Use the generic nearest result of each type, not one particular institution. Optional extras if quick: "Indian restaurant", "gurdwara".
Suburbs (start with these; then the rest of the passing rows in SuburbScorecard): Frankston, Mordialloc, Seaford, Mentone, Altona, Chelsea, Mornington, Newport, Berwick, Upwey, Rosebud, Belgrave, Rye, Dromana, Torquay, Upper Ferntree Gully, Eltham, Diamond Creek, Frankston South, Woodend, Highton, Warragul, Croydon, Sassafras, The Basin, Mount Evelyn, Warrandyte, Hurstbridge, Mount Martha.
Community comparator suburbs: to be added here once the family approves the comparator list (proposal in "Community comparators — research (28 Oct 2026).md").
Table: Suburb | Type | Nearest name | Address | Min drive | Map URL | Tag

TASK 8 — Is Glen Waverley a family-and-school buyer market? (5 Northam Street, Glen Waverley) [added 28 Oct 2026]
Collect evidence for or against this claim: "Glen Waverley is primarily a family-and-school market, so expect competition from school-motivated buyers at auction." Record what the pages say, including evidence against it.
a) ABS 2021 QuickStats, Glen Waverley (SAL21013): https://abs.gov.au/census/find-census-data/quickstats/2021/SAL21013 . Record: family composition (couple family with children, without children, one parent; % of families), % aged 0–14 and 5–19 if shown, median age, and the same measures for Greater Melbourne or Victoria shown on the page.
b) School zones, findmyschool.vic.gov.au: search "5 Northam Street, Glen Waverley VIC 3150" for the 2027 school year (or the latest shown). Record the zoned government primary and secondary schools. Is it in the Mount View Primary School zone? Is it in the Glen Waverley Secondary College zone?
c) Who buys in Glen Waverley: the realestate.com.au and Domain suburb profiles (household or demographic panels, e.g. family households, owner-occupiers, long-term residents), and an agency suburb report if one is easy to find (e.g. Jellis Craig Glen Waverley). Record any statement about buyer types or school-driven demand, quoted exactly.
d) Listing check, 5 Northam Street (realestate.com.au listing 152636156): https://www.realestate.com.au/property-house-vic-glen+waverley-152636156 . Confirm or correct: price guide $1,550,000–$1,650,000; auction Sat 14 Nov 2026, 11:00 am; 581 m²; 4 bed, 2 bath, 2 car; the exact school wording ("close to" or "zoned"). Record floor area, year built, auction location, and whether a Statement of Information or vendor statement is linked (read only; don't download anything that needs a sign-up or enquiry).
Table: Item | Value | Comparison (if any) | Quote (for c) | URL | Date read | Tag

FINAL REPLY
All eight tables as markdown pipe tables, then a short "Problems" list (skipped sites, not-found values, anything ambiguous).
