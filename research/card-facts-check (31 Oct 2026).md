# Card facts check — v14 area cards (31 Oct 2026)

Task T3 of `Handoffs/Handoff — wait-period work (31 Oct 2026).md` (register C4/C5, narrowed). Research note only: **no workbook cell, card or page was changed.** The workbook was read at sha256 `29d9e37d508c`. Every proposed edit below needs the user's approval (gated plan step A2).

Labels: **Checked** = read on the cited page on the date given. **Needs verification** = not settled from an official or primary page. A source supports an entry; it doesn't make a judgement score Checked.

**Drive minutes were not measured.** The handoff asks for Google Maps "Depart at" 10:00 on a weekday. That needs the signed-in Chrome route, which this session didn't run. Every new minute figure is therefore **Needs verification**, and this note names hospitals only.

## 1. Card C: nearest 24-hour public hospital emergency department (R5.4 definition)

R5.4 definition: a public hospital emergency department open 24 hours. Urgent-care centres don't count.

| Suburb | Cell | Current value | Finding | Label | Source (read 31 Oct 2026) | Proposed cell edit |
|---|---|---|---|---|---|---|
| Healesville (row 14) | AD14 / K14 = 33 | Maroondah Hospital ED | Correct. The Eastern Health page says: "If you require urgent care – please call 000 or present to the nearest Emergency Department at Eastern Health Maroondah". The nearest urgent care centres it lists are in Bayswater and Lilydale, open 8am–10pm. Maroondah's ED is 24/7 (see Yarra Glen). | Checked (hospital) | Eastern Health, Healesville GP Clinic patient information, https://www.easternhealth.org.au/healesville-gp-clinic/patient-information-2/ | AD14: append "nearest ED Checked 31 Oct 2026 (Eastern Health: Healesville has no ED; nearest Maroondah)". K unchanged |
| Yarra Glen (row 55) | AD55 / K55 = 30 | Maroondah Hospital ED (24-hr: recall) | Maroondah's ED is open 24 hours: "Emergency department 24 hours a day, 7 days a week". Eastern Health names it as the nearest ED for the Healesville area. | Checked | Eastern Health, Maroondah, https://www.easternhealth.org.au/locations/eastern-health-maroondah/ | AD55: replace "24-hr: recall (major metro ED)" with "24-hr: Checked 31 Oct 2026, Eastern Health site" |
| Warburton (row 33) | AD33 / K33 = 53 | Maroondah Hospital ED ("Angliss may be closer, 24-hr status unverified") | Angliss's 24-hour ED is now confirmed (§3). It isn't settled whether Angliss is closer by road than Maroondah. | Checked (Angliss 24-hr); Needs verification (which is nearer) | Eastern Health Angliss page (§3) | AD33: replace "Angliss may be closer, 24-hr status unverified" with "Angliss ED is 24-hr (Checked 31 Oct 2026, Eastern Health); whether Angliss is nearer by road: Needs verification (Google Maps, 10:00 weekday)" |
| Macedon (row 17) | AD17 / K17 = 60 | Bendigo Hospital ED (nearest ED not confirmed; Northern Hospital Epping not tested) | **Bendigo is probably not the nearest.** Macedon is on the Bendigo line 5.6 km past Gisborne. The workbook already uses Sunshine Hospital for Gisborne, at 34 min. Northern Hospital (Epping) runs a 24-hour ED. Sunshine (Western Health, St Albans) is listed as 24-hour only by search summaries; its own page returned 403. Sunbury has only a day hospital and an urgent care clinic. | Checked (Northern 24-hr). Needs verification (Sunshine 24-hr: page blocked). Estimate (Sunbury has no ED; Sunshine nearer than Bendigo). Needs verification (minutes) | Western Health, Sunshine Hospital, https://westernhealth.org.au/location/sunshine-hospital ; Northern Health, Urgent and Emergency Care, https://www.nh.org.au/urgent-and-emergency-care/ ; Bendigo line station distances, https://en.wikipedia.org/wiki/Bendigo_railway_line ; Sunbury urgent care clinic, https://www.health.gov.au/ministers/the-hon-mark-butler-mp/media/medicare-urgent-care-clinic-opens-in-sunbury | AD17: "Nearest ED to confirm: Sunshine (likely) vs Northern vs Bendigo. Google Maps 10:00 weekday, top of range: Needs verification." K17: re-time once measured |
| Woodend (row 16) | AD16 / K16 = 55 | Bendigo Hospital ED (nearest ED not confirmed) | Same as Macedon. Woodend is 8.3 km further up the line than Macedon. Sunshine is probably nearer than Bendigo, but by less. | Estimate; Needs verification (minutes) | As Macedon | AD16: as AD17. K16: re-time once measured |
| Gisborne (row 53) | AD53 / K53 = 34 | Sunshine Hospital ED (24-hr: recall) | Search results quote Western Health saying Sunshine's ED is open 24 hours. The page itself returned HTTP 403 to this session, so the wording wasn't read. | Needs verification (source blocked) | Western Health, https://westernhealth.org.au/location/sunshine-hospital (403, 31 Oct 2026) | AD53: replace "24-hr: recall (major metro ED)" with "24-hr: Needs verification (Western Health page blocked 31 Oct 2026)". Read it in Chrome |
| Riddells Creek (row 54) | AD54 / K54 = 38 | Sunshine Hospital ED (24-hr: recall; Northern 45 min) | Northern's ED treats "adults and children, 24 hours a day", so the 45-min alternative is a valid ED. Sunshine as for Gisborne. | Checked (Northern); Needs verification (Sunshine) | Northern Health, https://www.nh.org.au/urgent-and-emergency-care/ ; Western Health (403) | AD54: "Sunshine 24-hr: Needs verification (page blocked 31 Oct 2026); Northern Hospital ED 24-hr Checked 31 Oct 2026 (Northern Health)" |
| Kyneton (row 15) | AD15 / K15 = 47 | Bendigo Hospital ED ("local 24-hr urgent care is not an ED") | The Kyneton note is correct. Central Highlands Rural Health runs a **24/7 urgent care centre** in Kyneton, not an ED. It isn't settled whether **Castlemaine Health** (Cornish St, about 33 km by rail from Kyneton) runs a full ED or an urgent care centre: one directory lists "Emergency Medical", while a PHN listing mentions "urgent care". If Castlemaine has an ED, it may be nearer than Bendigo. Sunshine is another candidate. | Checked (Kyneton is urgent care only). Needs verification (Castlemaine's status; nearest ED) | Central Highlands Rural Health business listing, Tarrangower Times directory ("Our Urgent Care Centres in Daylesford and Kyneton are here for you 24/7, however for emergencies, it is best to call 000"), https://tlnews.com.au/business_directory/central-highlands-rural-health/ ; healthdirect Castlemaine Health listing, https://www.healthdirect.gov.au/australian-health-services/search/castlemaine-3450-vic/hospitals/1223151000168101 ; VAHI Castlemaine Health page returned 403 (blocked) | AD15: append "Castlemaine Health ED vs urgent care: Needs verification; Sunshine also to test (31 Oct 2026)" |

## 2. Train Yes/No marked "recall", "verify" or "per sheet note" (card suburbs)

AB values are unchanged in every case. Each row upgrades the AC basis to Checked.

| Suburb (row) | AB | Finding | Source (Wikipedia, read 31 Oct 2026) | Proposed AC edit |
|---|---|---|---|---|
| Upper Ferntree Gully (6), Tecoma (24) | Yes | Station on the Belgrave line | [Belgrave line](https://en.wikipedia.org/wiki/Belgrave_railway_line) | Replace "(per sheet note)" with "(checked: Wikipedia Belgrave line, 31 Oct 2026)" |
| Ferntree Gully (39) | Yes | Station on the Belgrave line | Belgrave line | Replace "(recall; verify)" with "(checked: Wikipedia Belgrave line, 31 Oct 2026)" |
| The Basin (25), Sassafras (36), Mount Dandenong (37), Olinda (35) | No | No station on the Belgrave or Lilydale lines | Belgrave line; [Lilydale line](https://en.wikipedia.org/wiki/Lilydale_railway_line) | Replace "(recall; verify)"/"(per sheet note)" with "(checked: not on Belgrave or Lilydale line station lists, 31 Oct 2026)". The Basin's "bus link unverified" stays |
| Montrose (26), Mount Evelyn (27) | No | Not a Lilydale line station; the nearest stations are Mooroolbark and Lilydale | Lilydale line | As above |
| Warrandyte (8) | No | No suburban line serves it | Lilydale line; [Hurstbridge line](https://en.wikipedia.org/wiki/Hurstbridge_railway_line) | As above; "bus 906" stays unverified |
| Emerald (38) | No | Only Puffing Billy (tourist). The Belgrave line article mentions Emerald only as a proposed Gembrook-extension rebuild | Belgrave line | Replace "(recall; verify)" with "(checked: Wikipedia Belgrave line, 31 Oct 2026)" |
| Healesville (14), Yarra Glen (55), Warburton (33) | No | The Healesville and Warburton branches are closed. Lilydale is the terminus | Lilydale line | Replace "(recall; verify)" with "(checked: Wikipedia Lilydale line, 31 Oct 2026)" |
| Macedon (17), Riddells Creek (54), Kyneton (15) | Yes | V/Line Bendigo line stations | [Bendigo line](https://en.wikipedia.org/wiki/Bendigo_railway_line); [Gisborne station](https://en.wikipedia.org/wiki/Gisborne_railway_station) (adjacent-station listings) | Replace "(recall; verify)"/"(per sheet note)" with "(checked: Wikipedia Bendigo line, 31 Oct 2026)" |
| Gisborne (53) | Yes | Station on Station Road, New Gisborne. Bendigo, Echuca and Swan Hill V/Line services | Gisborne station | Replace "(recall; verify)" with "(checked: Wikipedia Gisborne station, Station Rd New Gisborne, 31 Oct 2026)" |
| Eltham (5), Rosanna (58), Heidelberg (4) | Yes | Hurstbridge line stations | Hurstbridge line | Replace "(recall; verify)" with "(checked: Wikipedia Hurstbridge line, 31 Oct 2026)" |
| Mount Martha (63), Dromana (45), McCrae (62), Arthurs Seat (66) | No | No passenger line south of Frankston on that side. The Stony Point line runs Frankston to Stony Point; the Mornington branch closed in 1981 | [Stony Point line](https://en.wikipedia.org/wiki/Stony_Point_railway_line) | Replace "(recall; verify)" with "(checked: Wikipedia Stony Point line, 31 Oct 2026)" |

Not covered: service frequency (e.g. Woodend weekday trains) and bus links. These are still Needs verification. Rosebud (51) says "not individually checked"; it's covered by the Stony Point finding and gets the same AC edit.

## 3. Angliss Hospital wording

Eastern Health's Angliss page says "Emergency department 24 hours a day, 7 days a week". It was read on 31 Oct 2026 at https://www.easternhealth.org.au/locations/eastern-health-angliss/ and is **Checked**.

The handoff names rows 6, 23, 24 and 33. The workbook text is wider than that:

| Cell | Current text (excerpt) | Proposed replacement |
|---|---|---|
| AD6, AD22, AD23, AD24, AD25 | "Angliss Hospital ED (24-hr status still to verify)" | "Angliss Hospital ED (24-hr: Checked 31 Oct 2026, Eastern Health site)" |
| Z6 | "10-min walk/bus 732 to Angliss Hospital (verify 24-hr ED status & drive)" | "10-min walk/bus 732 to Angliss Hospital (24-hr ED Checked 31 Oct 2026, Eastern Health site; walk/bus time not checked)" |
| AD33 | "…Angliss may be closer, 24-hr status unverified" | See §1, Warburton |
| Z23, Z24 | No Angliss text. Their "verify" refers to the train S score | No Angliss edit. The §2 train edits cover the "verify" |

AD22 (Belgrave) and AD25 (The Basin) aren't in the handoff's list but carry the same "still to verify" text.

## 4. Would any card range on the page change?

- **Card C, "ED drive 30–60": likely yes, once the minutes are measured.**
  - The 60 is Macedon to Bendigo. If Macedon and Woodend re-time to Sunshine and both come in under Warburton's 53, the range becomes about 30–53.
  - If Warburton re-times to Angliss and that's shorter, the top could fall further.
  - None of this is measured yet, so **no card wording is proposed now.**
  - The card already shows ED times as estimates. The page change waits for the measured minutes (gated step F1).
  - Proposed wording once measured, no suburb names: "ED drive: about 30–[new max] min (estimate)".
- **Card C, "Train 5 of 8": no change** (all eight Checked).
- **Card B, ED "2–22" and "4 of 12" train: no change.** Angliss confirmation removes a caveat but changes no figure.
- **Cards A, D, E: no change** from this check.

## Open items (for the Chrome/Maps task list)

1. Google Maps "Depart at" 10:00 weekday, top of range:
   - Macedon to Sunshine, Northern and Bendigo
   - Woodend to Sunshine, Northern and Bendigo
   - Kyneton to Sunshine, Bendigo and Castlemaine
   - Warburton to Angliss and Maroondah
2. Castlemaine Health: does it run an ED or an urgent care centre? Check its own site or VAHI; VAHI returned 403 to this session.
3. Sunshine Hospital 24-hour wording: the Western Health page returned 403 to this session; read it in Chrome.
