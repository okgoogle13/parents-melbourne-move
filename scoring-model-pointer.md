# Project Scoring Model — Local Source of Truth

**Canonical File:** `Our Next Home — Family Relocation Scoring Model.xlsx`  
**Location:** `/Users/okgoogle13/Projects/Parents Melbourne MOVE/Our Next Home — Family Relocation Scoring Model.xlsx`  
**Policy:** Local-only. All project work, analysis, scoring, and data reside exclusively in this local project folder on this computer. No Google Drive, Google Sheets connectors, or cloud dependencies.

---

## Authority Rule
Before answering anything about suburbs, scores, weights, filters, or family responses, read directly from the local workbook:  
`Our Next Home — Family Relocation Scoring Model.xlsx`

Do not attempt to read or reference Google Drive or external sheets. This local workbook is the authoritative, up-to-date version.

---

## Tab Map (10 Tabs)
- **StartHere**: Workflow steps and guide.
- **Settings**: Say-in-decision weights, max-2-Essential rule, purchase cost allowance, rating scales.
- **RawResponses**: Respondent submission records.
- **CleanedAnswers**: Latest survey responses per person (Mum, Dad, Me) and Essential-cap checks.
- **Filters**: Active hard filters. **This is the current family decision record.**
  - **Budget Cap:** $1,500,000 maximum purchase price (confirmed 27 Oct 2026).
  - **GW Drive Cap:** 90 min hard max (60 min preferred).
  - **ED Drive Cap:** 90 min hard max.
  - **Train Station:** Preferred, not a hard disqualifying filter.
  - **Stairs:** Allowed; single-level not required (corrected 27 Oct 2026 by NJD; survey answer kept in Filters!D6).
- **PriorityWeights**: Per-person Q15 scores, normalized and combined.
- **ForcedChoiceCorrections**: Trade-off adjustments (Q10–Q13) and final criteria weights.
- **SuburbScorecard**: 65 locations (63 candidate suburbs + 2 synthetic test rows; rows 57–66 added 27 Oct 2026 from the Listings collection) with published prices, drive times, transparent budget verification fields (Cols AE–AJ), criteria ratings, and hard filter status.
- **Listings** (added 27 Oct 2026): 32 properties from the realestate.com.au collection "Parents." (read 27 Oct). A–F, H–O, U, V are pasted values (agent guides, beds/baths/cars/land, status, inspection, agent, notes, listing URL). Column B addresses are clickable links to the listing (photos); V holds the raw URL; G and P–T are formulas: budget check vs Filters!B2 (purchase price), suburb-level GW/ED drive and train looked up from SuburbScorecard, Overall check. Refresh = re-read the collection and overwrite pasted columns only. Current result (27 Oct 2026): Pass 18, Pass if bought near low end 6, Fails budget 5, Fails GW drive 1 (Curlewis), Under offer 2. No Needs data.
- **DiscussionSummary**: Summary metrics, filter status counts, and decision logs.

---

## Active Status (verified against workbook 27 Oct 2026, 02:31 UTC; 65 rows, recalculated with 0 formula errors)
- **Active — provisional pass (26):** Ringwood, Heidelberg, Eltham, Upper Ferntree Gully, Diamond Creek, Mentone, Frankston, Altona, Kyneton, Woodend, Torquay, Upwey, Warragul, plus (27 Oct research pass) Warrandyte, Healesville, Macedon, Newtown (Geelong), Highton (Geelong), Belgrave, Tecoma, The Basin, Montrose, Mount Evelyn, Croydon, Mornington, Frankston South.
- **Provisional pass, Watchlist / open-mind (25):** Dromana, West Footscray, Rosanna, Seaford, Chelsea, McCrae, Mount Martha, Mordialloc, Newport, Arthurs Seat, plus Warburton, Olinda, Sassafras, Mount Dandenong, Emerald, Ferntree Gully, Berwick, Hurstbridge, Wonthaggi (88 min — 2 under the cap), Rosebud, Rye, Gisborne, Riddells Creek, Yarra Glen, Drouin.
- **Active — needs data (4):** Blackburn, Glen Waverley, Williamstown, Mount Eliza ($1.61M AVM). All over $1.5M; need a documented search for 3+ bed homes under the cap. realestate.com.au is blocked in the built-in browser, so this needs Claude in Chrome (see the prompt file, Task 4).
- **Needs data (0).**
- **Fails GW drive > 90 min (8):** Ocean Grove (92), Clifton Springs (95), Curlewis (104), Trentham (97), Inverloch (96), Ballarat (111), Castlemaine (114), Bendigo (140).
- **Fails budget (0).** **Excluded test rows (2):** rows 49–50.
- **Scores (cols M–V): none entered for any real suburb.** Only O (Hospital) auto-fills from ED drive time. No ranking exists yet.

## Change log
- **27 Oct 2026 (listing URLs):** Listings!V = realestate.com.au URL for all 32 listings (read from the collection page in Claude in Chrome), and each address in column B links to it. Each URL checked against its row's address before writing. Recalc check: 0 formula errors, Overall check unchanged (Pass 18, near low end 6, Fails budget 5, Fails GW 1, Under offer 2). Pre-change copy in Archive. Note: a Google Sheet copy of this model also exists and was edited in an earlier chat today; it is stale (budget still $1.25M) and is NOT a source.
- **27 Oct 2026 (02:30 UTC, research pass, "Claude in Chrome prompt" chat):** drive times + ED for 19 suburbs (Trentham, Olinda, Sassafras, Mount Dandenong, Emerald, Ferntree Gully, Berwick, Hurstbridge, Ballarat, Bendigo, Castlemaine, Wonthaggi, Inverloch, Rosebud, Rye, Gisborne, Riddells Creek, Yarra Glen, Drouin). Basis: Google Maps leave-now, 13:15–13:45 AEDT (midday, not peak). Control check: Woodend read 77 min today vs 68 on the sheet, so today's times run ~10% high. Gisborne measured from the post office (suburb pin gave a 2h+ route). 24-hr ED verified for Angliss (Eastern Health), Wonthaggi (healthdirect), West Gippsland (South Gippsland Shire directory); Casey, Northern, Ballarat Base, Bendigo, Sunshine, Maroondah from recall (major EDs). House prices for 32 suburbs: OnTheHouse/Cotality AVM as at 30 Sep 2026 (not sale medians), unit AVM and 12-month sales count in col H; under 40 sales flagged weak (Macedon, Tecoma, Olinda, Sassafras, Mount Dandenong). OnTheHouse returns the same AVM ($872,133) for Ferntree Gully and Upper Ferntree Gully — treat as postcode-level. Train Yes/No for the 17 blank rows from recall (marked "verify"). Column L re-evaluated for 34 rows. Pre-change copy in Archive.
- **27 Oct 2026 (02:30 UTC):** (1) CleanedAnswers A30:G39 = context answers Q1, Q2, Q8, Q9, Q13b, Q13c, Q14 + gap-form notes (not weighted; blanks show blank). (2) ForcedChoiceCorrections B6:B15 now = PriorityWeights K + editable shift in col C, renormalised; old typed weights kept in col E. SuburbScorecard X uses B6:B15, so suburb scores now follow the survey. Shifts carried over: Family +7.2/Nature −7.2, Shops +2.6/Village −2.6 — sized for the old weights; recompute after round 2. (3) DiscussionSummary F5:F14 linked to FCC; E17 living arrangement updated; D21:F29 location split (Q13b/Q13c) and Q14. (4) Questionnaire page republished (version 2, same artifact) as round 2: shows only Q13 + Q15 (max 2 Essentials enforced), saves with mode "round 2 (Q13, Q15)". Round-1 page in Archive. Import rule for round 2: new RawResponses row per person = their latest row (6 Dad, 7 Mum, 8 Me) + round-2 answers. Pre-change workbook in Archive.
- **27 Oct 2026 (02:20 UTC):** recalculation check (LibreOffice copy; workbook itself unchanged). CleanedAnswers latest rows = Mum 7, Dad 6, Me 8; PriorityWeights follows. Gaps: Q1, Q2, Q8, Q9, Q13b, Q13c, Q14 have no CleanedAnswers rows, so the new gap answers don't feed any weight yet. Mum still has 3 Essentials (cap 2). Blank answers display as 0 (e.g. Me budget).
- **27 Oct 2026 (02:12 UTC):** RawResponses rows 6–8 added from the questionnaire page (gap answers merged onto rows 5/4/3). Pre-change copy in Archive.
- **27 Oct 2026 (workbook repair):** removed all Google-only formulas so the file works in Excel. SuburbScorecard A–H and Z are now plain values (edit them directly; column AA is legacy text, not used). Blank price in G = not yet researched (previously showed 0). W (scores entered), X (weighted score) and Y (rank among *pass* rows) are now standard per-row formulas. CleanedAnswers B2:B4 use LOOKUP instead of XMATCH; Filters D4 rewritten without REGEXEXTRACT. Pre-fix copy in Archive. Code.gs (Google Form builder) moved to Archive — questionnaire will be a Claude-hosted form page.
- **27 Oct 2026:** drive times added for Warburton (65 GW / 53 ED, Maroondah) and Frankston South (31 / 4, Peninsula University Hospital), Google Maps leave-now. Column L still "Needs data" for both (price missing).
- **27 Oct 2026:** added West Footscray, Rosanna, Seaford, Chelsea, Curlewis, McCrae, Mount Martha, Mordialloc, Newport, Arthurs Seat (rows 57–66, Watchlist) and completed Dromana (row 45). (First write of rows 57–63 was overwritten by the parallel workbook repair at 01:53; re-applied on top of the repaired file.) Arthurs Seat price is a sale median from only 5 sales — weak. Mordialloc ED = Sandringham Hospital (24/7, Alfred Health). Drive times: Google Maps leave-now, by suburb name. Prices: OnTheHouse/Cotality AVM estimates, NOT sale medians. Train Yes/No from recall. P/Y fit and lens not assessed. L: Provisional pass for all except Curlewis (Fails: GW drive, 104 min). Rosebud Hospital ED confirmed 24/7 (Peninsula Health) but treats less serious cases; used for McCrae, Mount Martha, Dromana.

## Open work and owners (consolidated 27 Oct 2026)
Rule: one session edits the workbook at a time. Re-read the file immediately before writing and check its modified time hasn't changed.
- **Done:** Google-only formulas removed (workbook repair, 01:53); Code.gs to Archive; Listings tab (32 listings); 10 Watchlist suburbs added and Dromana completed; new Chrome research prompt saved; pointer counts corrected.
- **Research gaps:** drive times and prices DONE (02:30). Still open: (a) under-$1.5M searches for Blackburn, Glen Waverley, Williamstown, Mount Eliza and (b) train checks — realestate.com.au is blocked in the built-in browser, so run Tasks 4–5 of `Claude_in_Chrome_prompt — close research gaps.md` in Claude in Chrome. (c) Optional: re-run drive times at one consistent time for borderline rows (Wonthaggi 88, Torquay 88).
- **Criteria scores M–V for the 23 passing suburbs:** next, in one session, after the research writes land. Data-derived scores (GW drive, price, train, city trip) computed from columns; judgement scores (nature, village, beach, shops/doctor, Indian community) marked as estimates with basis in col Z.
- **Family survey responses:** round 1 gap answers recorded (rows 6–8). **Round 2 (Q13 + Q15) sent via the questionnaire page; awaiting answers.** Then: import, re-check Mum's Essentials, recompute forced-choice shifts.
- **Mum has 3 Essentials (cap is 2):** flagged in an earlier chat; not re-checked against CleanedAnswers today.
