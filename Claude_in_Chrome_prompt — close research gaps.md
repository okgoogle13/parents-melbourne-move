# Claude in Chrome prompt — close research gaps (v2, 27 Oct 2026)

Replaces v1 (in Archive/). v1 Tasks 1–3 (collection read, drive times, prices) are DONE and already in the workbook; they are removed here.
v2 covers the gaps found by the 27 Oct research report ("Suburb shortlist foundation report.pdf"): property searches, ED/drive-time errors, price conflicts, train checks, hazard overlays, Indian grocery / worship access.
Paste everything below the line into Claude in Chrome. It only collects facts; results are written into the workbook afterwards, with sources. Run Tasks 1–3 first (they need realestate.com.au / Maps and go stale); 4–7 can follow.
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

TASK 7 — Community access (Google Maps search, Driving, "Leave now")
For each suburb, search from the suburb centre and record the nearest of each, with name and drive minutes:
a) "Indian grocery" b) "Indian restaurant" c) "Hindu temple" or "gurdwara" d) "church"
Suburbs: Upwey, Belgrave, Upper Ferntree Gully, Eltham, Diamond Creek, Frankston South, Mornington, Woodend, Highton, Warragul, Croydon, Berwick, Sassafras, The Basin, Mount Evelyn, Warrandyte, Hurstbridge, Seaford, Mount Martha, Dromana, Torquay.
Table: Suburb | Type | Nearest name | Min drive | Map URL | Tag

FINAL REPLY
All seven tables as markdown pipe tables, then a short "Problems" list (skipped sites, not-found values, anything ambiguous).
