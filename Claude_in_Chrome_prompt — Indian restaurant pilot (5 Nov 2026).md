# Claude in Chrome prompt — Indian restaurant drive-time pilot (5 Nov 2026)

Research only. Nothing here changes the workbook or survey. Results are pasted back into a Claude session and checked before anything is written.

## Why this pilot
- Under the new priority (diverse suburb + nearby Indian groceries and restaurants), the model needs a restaurant measure. None exists today.
- Decision D6 (5 Nov): collect restaurant drive times for all suburbs, pilot 10 first. The pilot tests the method (search term, what counts as an Indian restaurant, drive-time basis) before the full run. It is not a go/no-go.
- Same basis as the grocery column AY, so the two can be compared: Google Maps, Driving, depart next weekday 10:00, top of the "typically" range, starting from the suburb centre.

## Decisions recorded 5 Nov 2026 (context for later sessions)
- D1 community weight (15%): decide after survey responses.
- D2 structure of the community score: wait for survey responses.
- D3: survey sets the split inside the community score (proposal 15A).
- D4: remove the temple/church survey questions (R5.5–R5.7 and the temple/church wording in Q15.3).
- D5: Mum, Dad and Nish count equally in the split.
- Survey: remove "Not sure" options where possible. A skipped answer still means that person is left out for that item; if all three skip, the default split applies.
- D6: restaurants collected for all suburbs; this 10-suburb pilot first.

## Pilot suburbs (chosen for spread)
Mix of grocery distance (AY 1–24 min) and diversity (AU, % other language at home, 5–32%). All pass the 25-min grocery filter. Known nearest grocer from col Z, for cross-checking afterwards (not needed in Chrome):

| # | Suburb | AY grocery (min) | AU | Nearest grocer (col Z, 2 Nov) | Why included |
|---|---|---|---|---|---|
| 1 | Heidelberg | 1 | 23.7% | Heidelberg Pickles and Pappads | Near + diverse |
| 2 | Ringwood | 4 | 31.6% | Om Sevvel Indian Store | Most diverse ranked row |
| 3 | Berwick | 7 | 28.7% | Budget Grocery | High Indian share |
| 4 | Frankston | 3 | 12.1% | Frankston Spices | Ranked 1st; near grocer, low diversity |
| 5 | Warragul | 3 | 6.8% | IGS Indian Grocery Store | Regional town |
| 6 | Newtown (Geelong) | 7 | 8.8% | Just Spice (Geelong) | Geelong |
| 7 | Upper Ferntree Gully | 14 | 8.3% | AR Groceries (Boronia) | Hills, mid distance |
| 8 | Torquay | 16 | 4.7% | Guru's Indian Groceries (Armstrong Creek) | Coast, low diversity |
| 9 | Mordialloc | 22 | 18.7% | Little India Mart (Clayton South) | Diverse but grocer far: restaurant may be closer |
| 10 | Eltham | 24 | 10.5% | Heidelberg Pickles and Pappads | Near the 25-min limit |

## After the pilot (in a normal Claude session, not Chrome)
1. Paste the Chrome reply into the session. Save it as `research/community/restaurant-pilot (5 Nov 2026).md`.
2. Check: did any rule below need a judgement call? Fix the rules before the full run.
3. Compare restaurant vs grocery minutes for the 10 rows (how often the restaurant is closer, by how much). Report only; no decision is attached.
4. Full run: same prompt, remaining passing rows plus comparators rows 67–72 and the 4 needs-data shortlist rows (Glen Waverley, Blackburn, Williamstown, Mount Eliza).
4a. Sensitivity check (report only, no decision): on a recalculated temp copy, score restaurant minutes on the same scale as the grocery part of P, then re-run the `community-proposals.md` item 12 rank test for the 37 ranked rows with restaurants in. Report any top-12 suburb that moves 3 or more places.
5. Workbook write-back (column AZ, repurposed from "Hindu temple") waits for approval of the workbook changes. Until then results stay in `research/`.

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
1. Search "<Suburb> VIC" and use the suburb pin as the start point (suburb centre).
2. Search "Indian restaurant near <Suburb> VIC". Look at the closest results on the map, not just the top of the list (the list is ranked by relevance, not distance).
3. For the 2 nearest places that count, get directions from the suburb pin: Driving, "Depart at" next weekday 10:00.
4. Record the "typically X–Y min" range and the top of the range (Y). If Maps shows one number, use it as both.
5. Also record the distance in km shown for that route.

SUBURBS
Heidelberg, Ringwood, Berwick, Frankston, Warragul, Newtown (Geelong), Upper Ferntree Gully, Torquay, Mordialloc, Eltham.

TABLE (one row per place; 2 rows per suburb)
Suburb | Rank (1 = nearest, 2 = second) | Restaurant name | Address | Depart (date, 10:00) | Range (min) | Top of range (min) | km | Map URL | Date/time read | Tag | Notes

FINAL REPLY
The table as a markdown pipe table, then a short "Problems" list: skipped sites, not-found values, places marked "unsure", and any rule above that was hard to apply.
