# Claude in Chrome prompt — Indian restaurant drive times (5 Nov 2026; batch plan 11 Nov 2026)

Research only. Nothing here changes the workbook or survey. Results are pasted back into a Claude session and checked before anything is written. Task B10 in the register.

## Why
- Food and shops nearby are Mum's top community priority (10 Nov call, D-6; survey C2 groceries and C3 restaurants). Since 11 Nov (D2), score P gives food access 50 of its 100 points: Indian grocery drive (AY) 35 and Indian restaurant drive (AZ) 15. Until AZ is filled, the grocery drive stands in for the restaurant drive.
- AZ uses the same basis as AY so the two compare: Google Maps, Driving, depart next weekday 10:00, top of the "typically" range, from the suburb pin (the same start point as AY). Same scale: 10 points at 5 min or less, 0 at 30 min.

## State on 11 Nov 2026
- P's structure is settled (D2; `Filters!A22:C29`). Weights are the survey v18 answers, equal say (S2). Details: `scoring-model-pointer.md`.
- AZ is empty; its header is "Drive to nearest Indian restaurant". BB holds the basis and evidence.
- All 37 ranked suburbs need a value before AZ is written. A Top-15-only run would score ranks 16–37 on a different basis (`community-proposals.md` line 137).

## Batches (tell Chrome which batch to run)
| Batch | Suburbs | Purpose |
|---|---|---|
| 1 (10) | Heidelberg, Ringwood, Berwick, Frankston, Warragul, Newtown (Geelong), Upper Ferntree Gully, Torquay, Mordialloc, Eltham | Method check, chosen for spread (grocery 1–24 min, AU 5–32%). **Stop after this batch** and review the rules in a normal session |
| 2 (14) | Seaford, Ferntree Gully, Newport, Rosanna, West Footscray, Upwey, Croydon, Altona, Mentone, Belgrave, Tecoma, Chelsea, Frankston South, Highton (Geelong) | Rest of the current top 20 |
| 3 (13) | Diamond Creek, The Basin, Mornington, Montrose, Warrandyte, Mount Evelyn, Drouin, Sassafras, Gisborne, Olinda, Mount Dandenong, Riddells Creek, Macedon | Rest of the 37 ranked |
| 4 (optional, 24) | 14 rows failing the grocery limit (Healesville, Kyneton, Woodend, Warburton, Emerald, Hurstbridge, Dromana, Wonthaggi, Rosebud, Rye, Yarra Glen, McCrae, Mount Martha, Arthurs Seat); 6 comparators (Springvale, Clayton South, Keysborough, Clyde North, Endeavour Hills, Wheelers Hill); 4 needs-data rows (Glen Waverley, Blackburn, Williamstown, Mount Eliza) | Not needed for ranking: unranked rows use the grocery drive in place of AZ |

Batch 1 cross-check (nearest grocer from col Z, 2 Nov; not needed in Chrome): Heidelberg 1 min Heidelberg Pickles and Pappads; Ringwood 4 Om Sevvel Indian Store; Berwick 7 Budget Grocery; Frankston 3 Frankston Spices; Warragul 3 IGS Indian Grocery Store; Newtown 7 Just Spice; Upper Ferntree Gully 14 AR Groceries (Boronia); Torquay 16 Guru's Indian Groceries (Armstrong Creek); Mordialloc 22 Little India Mart (Clayton South); Eltham 24 Heidelberg Pickles and Pappads.

## After each batch (in a normal Claude session, not Chrome)
1. Paste the Chrome reply; save it as `research/community/indian-restaurant-drives (<date>) batch N.md`.
2. After Batch 1 only: did any rule need a judgement call? Fix the rules here before Batch 2.
3. Report (no decision attached): how often the restaurant is nearer than the grocer, and by how much.
4. After Batch 3: merge into `research/indian-restaurant-drives (<date>).json` in the grocery file's format (`[suburb, top-of-range min, evidence note]`, as in `research/indian-grocery-drives (2 Nov 2026).json`). Check that 37/37 ranked rows have a value, or "not found" with a reason.
5. Write-back is task **D2c** and needs approval: one change after all 37. Archive the workbook; write AZ (minutes), BB (basis and evidence) and a col Z source note per row. P switches to 35 grocery + 15 restaurant with no formula change. Run the recalc test, compare values, report top-12 moves of 3+ places, rebuild the parent report, update the records.

---

Paste everything below the line into Claude in Chrome.

---

Research task for my parents' Melbourne move. You are collecting drive times in the browser. Work in a new tab. Report back once at the end.

RULES
- Read-only. Don't open, create or edit any Google Docs, Sheets, Forms or Drive files. Don't sign in, review, save places, book, order or submit any form.
- If a site asks you to sign in or shows a CAPTCHA, skip it and note it.
- Every value needs: Map URL, date/time read, and a tag: Checked (read directly from Google Maps) or Estimate (your inference). Never tag a guess as Checked.
- If you can't find a value in 2 tries, write "not found" and move on.
- Don't summarise or recommend suburbs. Just the data.

WHAT COUNTS AS AN INDIAN RESTAURANT
- Counts: a restaurant, cafe or takeaway whose main cuisine is Indian, including regional Indian (South Indian, Punjabi, Gujarati, Indo-Chinese run as an Indian restaurant), and Indian sweets shops that serve meals.
- Doesn't count: a grocery shop with a small hot-food counter (note it in Notes instead); pan-Asian or "curry house" menus where Indian is one option among many; food trucks with no fixed address; anything marked "Permanently closed" or "Temporarily closed".
- Sri Lankan, Nepalese, Pakistani or Bangladeshi restaurants: don't count as the nearest, but if one is closer than the nearest Indian restaurant, note it in Notes.
- If unsure whether a place counts, record it anyway with "unsure" in Notes.

METHOD (Google Maps, desktop)
1. Search "<Suburb> VIC" and use the suburb pin as the start point (suburb centre). Use the same pin every time; it is also the start point for the grocery drives.
2. Search "Indian restaurant near <Suburb> VIC". Look at the closest results on the map, not just the top of the list (the list is ranked by relevance, not distance).
3. For the 2 nearest places that count, get directions from the suburb pin: Driving, "Depart at" next weekday 10:00.
4. Record the "typically X–Y min" range and the top of the range (Y). If Maps shows one number, use it as both.
5. Also record the distance in km shown for that route.

SUBURBS
Run only the batch I name below. For Newtown (Geelong) and Highton (Geelong), search "Newtown VIC 3220" and "Highton VIC 3216".
- Batch 1: Heidelberg, Ringwood, Berwick, Frankston, Warragul, Newtown (Geelong), Upper Ferntree Gully, Torquay, Mordialloc, Eltham.
- Batch 2: Seaford, Ferntree Gully, Newport, Rosanna, West Footscray, Upwey, Croydon, Altona, Mentone, Belgrave, Tecoma, Chelsea, Frankston South, Highton (Geelong).
- Batch 3: Diamond Creek, The Basin, Mornington, Montrose, Warrandyte, Mount Evelyn, Drouin, Sassafras, Gisborne, Olinda, Mount Dandenong, Riddells Creek, Macedon.
- Batch 4: Healesville, Kyneton, Woodend, Warburton, Emerald, Hurstbridge, Dromana, Wonthaggi, Rosebud, Rye, Yarra Glen, McCrae, Mount Martha, Arthurs Seat, Springvale, Clayton South, Keysborough, Clyde North, Endeavour Hills, Wheelers Hill, Glen Waverley, Blackburn, Williamstown, Mount Eliza.

Batch to run now: Batch 1

TABLE (one row per place; 2 rows per suburb)
Suburb | Rank (1 = nearest, 2 = second) | Restaurant name | Address | Depart (date, 10:00) | Range (min) | Top of range (min) | km | Map URL | Date/time read | Tag | Notes

FINAL REPLY
The table as a markdown pipe table, then a short "Problems" list: skipped sites, not-found values, places marked "unsure", and any rule above that was hard to apply.
