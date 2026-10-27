# Claude in Chrome prompt — close research gaps (27 Oct 2026)

Replaces Downloads/Claude_in_Chrome_prompt.txt (Google Apps Script/Form install — no longer allowed under the local-only rule).
STATUS 27 Oct 02:30 UTC: Tasks 2 and 3 are DONE (written to the workbook). Task 1 was read earlier today. Only Tasks 4 and 5 are still needed — delete Tasks 1–3 before pasting.
Paste everything below the line into Claude in Chrome. It only collects facts; results come back as tables and are written into the workbook afterwards, with sources.

---

Research task for my parents' Melbourne move. You are collecting facts in the browser. Work in a new tab. Report back after each task, then continue.

RULES
- Read-only. Don't open, create or edit any Google Docs, Sheets, Forms or Drive files. Don't contact agents, enquire, save searches, or submit any form.
- I'm signed in to realestate.com.au. If any other site asks you to sign in, or shows a CAPTCHA, skip it and note it.
- Every value needs: source URL, date/time read, and a tag — Checked (read directly on the page) or Estimate (your inference). Never tag a guess as Checked.
- If you can't find a value in 2 tries, write "not found" and move on.
- Don't summarise or recommend suburbs. Just the data.

TASK 1 — realestate.com.au collection "Parents." (do this first; inspection times go stale)
Open my saved collection "Parents." For every property record:
Address | Suburb | Price guide as listed | Beds | Baths | Cars | Land m² | Status (for sale / under offer / sold / withdrawn / gone) | Next inspection | Agent | URL

TASK 2 — Drive times (Google Maps, Driving, "Leave now")
Start point: the suburb itself (search "<Suburb> VIC"). For Ballarat and Bendigo, use the city centre and say so.
a) to "Glen Waverley VIC 3150"
b) to the nearest public hospital with a 24-hour emergency department. Name the hospital and confirm the 24-hour ED on the hospital's own website (urgent care centres don't count).
Record the first time Maps shows in minutes, plus the range if shown (e.g. "35–50").
Suburbs: Trentham, Olinda, Sassafras, Mount Dandenong, Emerald, Ferntree Gully, Berwick, Hurstbridge, Ballarat, Bendigo, Dromana, Castlemaine, Wonthaggi, Inverloch, Rosebud, Rye, Gisborne, Riddells Creek, Yarra Glen, Drouin, West Footscray, Rosanna, Mordialloc, Seaford, Arthurs Seat, Curlewis, McCrae, Chelsea, Newport, Mount Martha.
Table: Suburb | Min to GW | Range | ED hospital | Min to ED | Range | Time of lookup | Map URL | Tag

TASK 3 — Median house price
Preferred source: OnTheHouse suburb page, house sale median, rolling 12 months. If unavailable, realestate.com.au suburb profile median house price (12 months). Also record the unit median if shown.
Suburbs: Warrandyte, Healesville, Macedon, Newtown (Geelong), Highton (Geelong), Belgrave, Tecoma, The Basin, Montrose, Mount Evelyn, Croydon, Mount Eliza, Mornington, Frankston South, Olinda, Sassafras, Mount Dandenong, Emerald, Ferntree Gully, Berwick, Hurstbridge, Ballarat, Bendigo, Dromana, Castlemaine, Wonthaggi, Inverloch, Rosebud, Rye, Gisborne, Riddells Creek, Yarra Glen, Drouin.
Table: Suburb | House median $ | Unit median $ | Period | No. of sales (if shown) | Source | URL | Tag

TASK 4 — Can we buy under $1.5M in pricey suburbs?
realestate.com.au Buy search, one suburb at a time (surrounding suburbs OFF), House + Townhouse, 3+ bedrooms, max price $1,500,000. Don't save the search.
Suburbs: Blackburn, Glen Waverley, Williamstown, Mount Eliza.
Record: number of results, then up to 5 listings: Address | Price guide | Beds | Land m² | Single or double storey (only if stated) | URL

TASK 5 — Train access (lowest priority)
On ptv.vic.gov.au (or vline.com.au for regional), find the nearest train station for each suburb in Tasks 2 and 3, plus: Blackburn, Ringwood, Heidelberg, Eltham, Upper Ferntree Gully, Glen Waverley, Diamond Creek, Mentone, Frankston, Altona, Williamstown, Kyneton, Woodend, Macedon, Torquay, Ocean Grove, Upwey, Croydon, Warragul, Clifton Springs, Warburton.
Table: Suburb | Station | Line | In suburb / within ~2 km / none nearby | URL | Tag

FINAL REPLY
All five tables as markdown pipe tables, then a short "Problems" list (skipped sites, not-found values, anything ambiguous).
