# Claude in Chrome prompt — Indian restaurant drive times (5 Nov 2026; batch plan rewritten 11 Nov 2026)

Research only. Nothing here changes the workbook or survey. Results are pasted back into a normal Claude session and checked before anything is written. Task B10 in the register.

## How to read this file

| Marker | Meaning | Paste into Chrome? |
|---|---|---|
| `[OPERATOR NOTE]` | Background and state. | No |
| `[BATCH SPEC]` | Which suburbs are in which batch. | No |
| `[BATCHING INSTRUCTIONS]` | The run order and rules for whoever drives the run (you, or a normal Claude session). | No |
| `[GATE]` | A pause. Nothing after it starts until the named approver says go. Approver is **User** (decision) or **Advisor** (`/advisor`, mechanical check; escalates to User on any failure). | No |
| `[EXECUTION PROMPT]` | The text for Claude in Chrome, in a fenced block. Only fenced blocks are ever pasted. | **Yes** |

Run settings for the Chrome session: model Sonnet 5.5, effort `medium` (the guide's start value for well-specified multi-step tool work). Medium can stop to ask questions mid-task, so the prompt tells it to finish and log problems instead.

---

## [OPERATOR NOTE] Why and state

- Food and shops nearby are Mum's top community priority (10 Nov call, D-6; survey C2 groceries and C3 restaurants). Since 11 Nov (D2), score P gives food access 50 of its 100 points: Indian grocery drive (AY) 35 and Indian restaurant drive (AZ) 15. Until AZ is filled, the grocery drive stands in for the restaurant drive.
- AZ uses the same basis as AY so the two compare: Google Maps, Driving, depart 10:00 on a weekday, top of the "typically" range, from the suburb pin (the same start point as AY). Same scale: 10 points at 5 min or less, 0 at 30 min.
- P's structure is settled (D2; `Filters!A22:C29`). Weights are the survey v18 answers, equal say (S2). Details: `scoring-model-pointer.md`.
- AZ is empty; its header is "Drive to nearest Indian restaurant". BB holds the basis and evidence.
- All 37 ranked suburbs need a value before AZ is written. A Top-15-only run would score ranks 16–37 on a different basis (`community-proposals.md` line 137).
- **Assumption:** every batch uses one fixed depart date, **Tue 17 Nov 2026 10:00**, so all 37 rows share a basis. Change the date in the BASE prompt below if you want another weekday; change it once, before Batch 1.

## [BATCH SPEC] Batches

| Batch | Suburbs | Purpose |
|---|---|---|
| 1 (10) | Heidelberg, Ringwood, Berwick, Frankston, Warragul, Newtown (Geelong), Upper Ferntree Gully, Torquay, Mordialloc, Eltham | Method check, chosen for spread (grocery 1–24 min, AU 5–32%). Includes a calibration stop after suburb 2. |
| 2 (14) | Seaford, Ferntree Gully, Newport, Rosanna, West Footscray, Upwey, Croydon, Altona, Mentone, Belgrave, Tecoma, Chelsea, Frankston South, Highton (Geelong) | Rest of the current top 20 |
| 3 (13) | Diamond Creek, The Basin, Mornington, Montrose, Warrandyte, Mount Evelyn, Drouin, Sassafras, Gisborne, Olinda, Mount Dandenong, Riddells Creek, Macedon | Rest of the 37 ranked |
| 4 (optional, 24) | 14 rows failing the grocery limit (Healesville, Kyneton, Woodend, Warburton, Emerald, Hurstbridge, Dromana, Wonthaggi, Rosebud, Rye, Yarra Glen, McCrae, Mount Martha, Arthurs Seat); 6 comparators (Springvale, Clayton South, Keysborough, Clyde North, Endeavour Hills, Wheelers Hill); 4 needs-data rows (Glen Waverley, Blackburn, Williamstown, Mount Eliza) | Not needed for ranking: unranked rows use the grocery drive in place of AZ |

**Batch 1 cross-check — NOT pasted into Chrome** (nearest grocer from col Z, 2 Nov; used only at Gate 2): Heidelberg 1 min Heidelberg Pickles and Pappads; Ringwood 4 Om Sevvel Indian Store; Berwick 7 Budget Grocery; Frankston 3 Frankston Spices; Warragul 3 IGS Indian Grocery Store; Newtown 7 Just Spice; Upper Ferntree Gully 14 AR Groceries (Boronia); Torquay 16 Guru's Indian Groceries (Armstrong Creek); Mordialloc 22 Little India Mart (Clayton South); Eltham 24 Heidelberg Pickles and Pappads.

## [BATCHING INSTRUCTIONS]

1. **One batch per Chrome chat.** Open a new Chrome chat for each batch so context from earlier batches can't leak in. Never run two batches in one chat.
2. **One message = BASE + BATCH.** Paste the BASE prompt first, then that batch's prompt block directly under it, as a single message. The BASE is identical every time; never edit it between batches except through Gate 2 (rule fixes), and then re-check all later batches use the same text.
3. **Order is fixed:** Batch 1 → Gate 2 → Batch 2 → Gate 3 → Batch 3 → Gate 4 → (Batch 4 only if Gate 5 says yes) → Gate 6.
4. **Advisor vs User.** Advisor checks mechanical things against the stated criteria. User decides rule changes, whether to continue after a failed check, Batch 4, and write-back. If the Advisor finds any failure, stop and hand to the User; don't fix and continue.
5. **Save as you go.** After each batch, save the reply to `research/community/indian-restaurant-drives (<date>) batch N.md` before starting the next gate.
6. **If Chrome fails** (tool errors, no response, page not loading, 2–3 attempts): stop, keep the rows already posted, and report to the User. Don't restart the batch from the top; resume from the next unfinished suburb in a new chat.
7. **Nothing in Chrome writes to the workbook.** All writes happen in a normal session, only at Gate 6.

---

## [GATE 1] Before Batch 1 — Approver: User

Confirm:
- [ ] Depart date in the BASE prompt (Tue 17 Nov 2026) is the one you want for all 37 rows.
- [ ] Claude in Chrome is running Sonnet 5.5 at medium effort, in a new tab, signed in to nothing it doesn't need.
- [ ] Previous Chrome chats are closed.

Go → paste BASE + Batch 1.

---

## [EXECUTION PROMPT] BASE — paste first, every batch

````
<task>
Research task for my parents' Melbourne move. Collect Google Maps drive times from each suburb pin to the 2 nearest Indian restaurants. Work in a new tab. The suburbs to cover are in the batch block that follows this text.
</task>

<rules>
- Read-only. Don't open, create or edit any Google Docs, Sheets, Forms or Drive files. Don't sign in, review, save places, book, order or submit any form.
- If a site asks you to sign in or shows a CAPTCHA, skip it and note it.
- Every value needs: Map URL, date/time read, and a tag: Checked (read directly from Google Maps) or Estimate (your inference). Never tag a guess as Checked.
- If you can't find a value in 2 tries, write "not fo
und" and move on.
- Don't summarise or recommend suburbs. Just the data.
- Don't ask me questions. If something is unclear, apply the closest rule, record it in Notes, and list it under Problems. The only place you may stop and wait is where the batch block says STOP.
- Keep working until every suburb in the batch is done.
- Work quietly: no step-by-step narration. The only text you write before the final reply is the progress tables the batch block asks for. Prefer reading page text over screenshots.
</rules>

<definition name="Indian restaurant">
- Counts: a restaurant, cafe or takeaway whose main cuisine is Indian, including regional Indian (South Indian, Punjabi, Gujarati, Indo-Chinese run as an Indian restaurant), and Indian sweets shops that serve meals.
- Doesn't count: a grocery shop with a small hot-food counter (note it in Notes instead); pan-Asian or "curry house" menus where Indian is one option among many; food trucks with no fixed address; anything marked "Permanently closed" or "Temporarily closed".
- Sri Lankan, Nepalese, Pakistani or Bangladeshi restaurants: don't count as the nearest, but if one is closer than the nearest Indian restaurant, note it in Notes.
- If unsure whether a place counts, record it anyway with "unsure" in Notes.
</definition>

<method>
Use Google Maps, desktop, for every suburb:
1. Search "<Suburb> VIC" and use the suburb pin as the start point (suburb centre). Use the same pin every time; it is also the start point for the grocery drives.
2. Search "Indian restaurant near <Suburb> VIC". Look at the closest results on the map, not just the top of the list (the list is ranked by relevance, not distance).
3. For the 2 nearest places that count, get directions from the suburb pin: Driving, "Depart at" Tuesday 17 Nov 2026, 10:00.
4. Record the "typically X–Y min" range and the top of the range (Y). If Maps shows one number, use it as both.
5. Also record the distance in km shown for that route.
</method>

<table>
One row per place; 2 rows per suburb. Columns, in this order:
Suburb | Rank (1 = nearest, 2 = second) | Restaurant name | Address | Depart (date, 10:00) | Range (min) | Top of range (min) | km | Map URL | Date/time read | Tag | Notes
If a suburb has no qualifying place, write one row with "not found" in Restaurant name and the reason in Notes.
</table>

<final_reply>
Before replying, check: every suburb has 2 rows (or one "not found" row), and every row with a value has a Map URL and a Tag.
Then reply with: the full table as a markdown pipe table, then a short "Problems" list: skipped sites, not-found values, places marked "unsure", and any rule above that was hard to apply.
</final_reply>
````

---

## Batch 1

### [EXECUTION PROMPT] Batch 1 — paste directly under BASE

````
<batch>
BATCH 1 of 4 (10 suburbs): Heidelberg, Ringwood, Berwick, Frankston, Warragul, Newtown (Geelong), Upper Ferntree Gully, Torquay, Mordialloc, Eltham.
For Newtown (Geelong) search "Newtown VIC 3220".

STOP 1 (calibration): after Heidelberg and Ringwood, post their rows as a markdown pipe table, then write exactly "CALIBRATION STOP — reply 'continue' to proceed" and wait. Don't start Berwick until I reply.
After I reply "continue": do the other 8 suburbs. After Frankston and again after Mordialloc, post the rows so far as a markdown pipe table and keep going without waiting.
Then give the FINAL REPLY for all 10 suburbs.
</batch>
````

### [GATE 1b] Calibration stop (inside Batch 1) — Approver: Advisor, then User

At "CALIBRATION STOP", read the 4 rows. Advisor checks each row: Map URL present; Depart is Tue 17 Nov 2026 10:00; Top of range is a number; Tag is Checked only if it came from Maps; restaurant isn't a grocery counter or pan-Asian place. User replies `continue` to Chrome only if all pass. If the method is wrong (wrong pin, wrong depart time, grocery counted as restaurant), close the chat, fix the BASE text, restart Batch 1.

### [GATE 2] After Batch 1 — Approver: Advisor (checks), User (rule decisions)

Do in a normal Claude session, not Chrome:
1. Save the reply as `research/community/indian-restaurant-drives (<date>) batch 1.md`.
2. **Advisor checks:** 20 rows (or documented not-found); every row has Map URL, time read, Tag; no Checked without a URL; Problems list read in full.
3. **Cross-check (display only, no decision attached):** put each suburb's restaurant top-of-range beside the grocer figure in the Batch 1 cross-check line above, and list the suburbs where they differ markedly, for the User to eyeball. Report how often the restaurant is nearer than the grocer, and by how much.
4. **User decides:** did any rule need a judgement call (Problems list)? If yes, edit the BASE text above, archive the old version per project rules, and note the change here. Batch 1 rows stay if the fix doesn't change them; otherwise rerun the affected suburbs.

Go → Batch 2.

---

## Batch 2

### [EXECUTION PROMPT] Batch 2 — paste directly under BASE

````
<batch>
BATCH 2 of 4 (14 suburbs): Seaford, Ferntree Gully, Newport, Rosanna, West Footscray, Upwey, Croydon, Altona, Mentone, Belgrave, Tecoma, Chelsea, Frankston South, Highton (Geelong).
For Highton (Geelong) search "Highton VIC 3216".

No STOP in this batch. After every 5 suburbs (after the 5th and 10th), post the rows so far as a markdown pipe table and keep going without waiting.
Then give the FINAL REPLY for all 14 suburbs.
</batch>
````

### [GATE 3] After Batch 2 — Approver: Advisor (checks), User only if a check fails

1. Save the reply as `research/community/indian-restaurant-drives (<date>) batch 2.md`.
2. **Advisor checks:** 28 rows (or documented not-found); the same mechanical checks as Gate 2; spot-check 3 rows chosen by the Advisor by opening their Map URLs.
3. Any failure → User. Otherwise → Batch 3.

---

## Batch 3

### [EXECUTION PROMPT] Batch 3 — paste directly under BASE

````
<batch>
BATCH 3 of 4 (13 suburbs): Diamond Creek, The Basin, Mornington, Montrose, Warrandyte, Mount Evelyn, Drouin, Sassafras, Gisborne, Olinda, Mount Dandenong, Riddells Creek, Macedon.

No STOP in this batch. After every 5 suburbs (after the 5th and 10th), post the rows so far as a markdown pipe table and keep going without waiting.
Then give the FINAL REPLY for all 13 suburbs.
</batch>
````

### [GATE 4] After Batch 3 — Approver: Advisor (merge and checks), User (go/no-go)

1. Save the reply as `research/community/indian-restaurant-drives (<date>) batch 3.md`.
2. Merge batches 1–3 into `research/indian-restaurant-drives (<date>).json` in the grocery file's format (`[suburb, top-of-range min, evidence note]`, as in `research/indian-grocery-drives (2 Nov 2026).json`).
3. **Advisor checks:** 37/37 ranked rows have a value, or "not found" with a reason; same mechanical checks as Gate 2; spot-check 3 rows from batch 3.
4. **User decides** on Batch 4 at Gate 5 and on write-back at Gate 6.

---

## Batch 4 (optional)

### [GATE 5] Before Batch 4 — Approver: User

Not needed for ranking: unranked rows use the grocery drive in place of AZ. Run only if you want the 24 extra rows. Default: skip.

### [EXECUTION PROMPT] Batch 4 — paste directly under BASE

````
<batch>
BATCH 4 of 4 (24 suburbs): Healesville, Kyneton, Woodend, Warburton, Emerald, Hurstbridge, Dromana, Wonthaggi, Rosebud, Rye, Yarra Glen, McCrae, Mount Martha, Arthurs Seat, Springvale, Clayton South, Keysborough, Clyde North, Endeavour Hills, Wheelers Hill, Glen Waverley, Blackburn, Williamstown, Mount Eliza.

No STOP in this batch. After every 6 suburbs (after the 6th, 12th and 18th), post the rows so far as a markdown pipe table and keep going without waiting.
Then give the FINAL REPLY for all 24 suburbs.
</batch>
````

After it: save as `... batch 4.md`, run the Gate 3 checks, add rows to the JSON.

---

## [GATE 6] Write-back (task D2c) — Approver: User (explicit approval required)

One change, after all 37 are in. Needs approval because it edits the canonical workbook.
1. Archive the workbook as `(superseded <date>, before AZ restaurant drives)`.
2. Re-read the workbook just before writing. Write AZ (minutes), BB (basis and evidence) and a col Z source note per row. P switches to 35 grocery + 15 restaurant with no formula change.
3. Run `bash tools/recalc_test.sh <wb>` and compare values; report top-12 moves of 3+ places.
4. Rebuild the parent report from the recalc temp copy: `.venv/bin/python tools/report2.py <recalculated wb> <out.html>`.
5. Update the register (B10, D2c), `scoring-model-pointer.md` and `PROJECT_STATE.md` (next task ID).
