# Plan — IDE phases (10 Nov 2026)

After approval, copy to `docs/plan-2026-11-ide.md`. `docs/` has no naming convention; root files use "Topic — subtitle (D Mon YYYY).md".

**Goal (one line):** get from "survey complete, not imported" to a reproducible shortlist that produces saved-search criteria, with every filter and weight change approved by the user.

## 1. Summary

**Readiness:** ready to start. The environment works (`.venv/bin/python` imports openpyxl, yaml, jsonschema and weasyprint, contrary to the handoff). The export exists, and every v18 key is mapped in `tools/import_v14.py`. The blocker is a decision, not tooling.

**Top 3 risks**
1. **The weights follow your answers, not your parents'.** Beach 15% and Price 1% match "Me": Beach Essential, Price Not needed, budget higher. Both parents want a lower budget, Dad rates Price Important, and Dad rates Beach Not needed. Indian community at 15% gets only "Nice to have" ratings on C2–C4, but Mum's 31 Oct WhatsApp rejects Tecoma as "almost 100% white" and asks for Indian grocery stores and restaurants. So in practice it works like a veto, not a low priority; resolve it with §4b Q8 rather than cutting the weight. The Beach and Price weights are confirmation bias built into the model.
2. **Glen Waverley within 25 min is the constraint that actually binds.** I counted from the typed inputs (not a recalculation): 37 suburbs rank today, 15 survive a 25-min limit (14 with Dad's 20-min grocery and ED limits). The handoff says 16; I haven't reconciled the difference. ED limits of 20–30 min remove at most one more suburb.
3. **5 Northam St** has a guide of $1.55–1.65M (`research/properties/5-northam-street-glen-waverley.yaml`). That is above Filters!B2 ($1.5M) and B3 ($1.59M including costs). Both parents answered Q3c "budget should be lower". The RBA rate in `research/macro/macro-market-conditions.yaml` is labelled Needs verification and dates from before the 3 Nov decision.

**This week:** ask your parents the questions in §4b (in person, before mid-Nov), decide on the auction before Sat 14 Nov 11:00, and do the M4 refresh or label it unverified.

## 2. Findings

### 2.1 Environment and Claude Code setup

| # | Item | Serves | Effort | Standing / one-off |
|---|---|---|---|---|
| S1 | Skip `/init`; there is already a good CLAUDE.md | — | 0 | — |
| S2 | Fast-forward `origin/claude/claude-md-fixes` (`2ef2157`: CLAUDE.md line 15 bullet fix, "weasyprint" → Playwright `render.js`, untrack `tools/__pycache__`). Delete both branches on origin (needs a push, gated) | Housekeeping | 5 min | One-off |
| S3 | Then run `claude-md-management:claude-md-improver`, limited to: `import_v14.py` usage pointer, `Handoffs/` convention, cloud-credit note, `found.py` date | All | 15 min | Standing (CLAUDE.md) |
| S4 | `.claude/settings.json` (tracked; currently `{"enabledPlugins":{}}`): add a read-only allowlist built with the `fewer-permission-prompts` skill (`.venv/bin/python tools/validate_macro.py`, recalc script, `git status/log/diff`, `soffice --headless`). `settings.local.json` is already ignored by global git (not untracked), so leave it | All | 10 min | Standing |
| S5 | `tools/recalc_test.sh <wb>`: the `docs/workflow.md` recalc block as a script. Exit 0 or 1; prints errors, X count, Y count and canonical-unchanged. Keep the temp copy for `report2.py` | Every workbook task (N3, N4, G2–G5, G7) | 20 min | Standing tool |
| S6 | SessionStart hook: `.venv/bin/python tools/validate_macro.py` (prints review_due/stale INFO) | M4, auction | 10 min | Standing (settings.json) |
| S7 | `claude-code-setup:claude-automation-recommender`: run once after S2–S6 and adopt only what isn't covered | — | 10 min | One-off |
| S8 | Skills doctor: not installed as a skill. The claude-code-guide agent mentions a `/skill-doctor` report, which may be built in; verify before relying on it | — | 2 min | One-off |
| — | **Cut:** a survey-import skill (`import_v14.py` + `docs/workflow.md` already cover it), a hook guarding xlsx writes (edits go through openpyxl scripts, so the hook would match badly), scheduled cloud routines (credit ended 4 Nov) | | | |
| S9 | Dataviz (`dataviz` skill): one alignment chart only, used in the parent question sheet if wanted | P-conversations | 20 min | One-off |

### 2.2 Status review

**Survey to N3** (`Handoffs/data/questionnaire-responses-export-2026-11-10.json`)
- Latest v18 records: Mum #19 (24 answers), Dad #18 (24), Me/Nish #20 (25). RawResponses currently ends at row 16; the latest earlier rows are Mum 15, Dad 13, Me 16.
- The importer adds CB–CH (C1–C4, R11.1–R11.3), rows 17–19, and CleanedAnswers rows 97–103 (`tools/import_v14.py:60-66`).
- **B71:D71, not B71:C71.** The current formula requires R5.5–R5.7 and R6.2, which v18 doesn't ask. D71 (Me) already shows "Check". Rewrite all three so they check R6.1 is answered (RawResponses AW → CleanedAnswers row 49) and drop the R5.5–R5.7/R6.2 conditions.
- `--blank-context` choice: without it, Me's row 19 carries forward stale v16 R5.5–R5.7 and Q15.3, and Mum's and Dad's carry round-1–3 context. None of these feed a weight, filter or score (`docs/workflow.md:75`). **Default: no flag** (keeps history; the merge log in AM marks stale fields).
- v18 asks no house-criteria questions (R6.2–R6.7) and no timing questions (R9), so G5 has R6.1 plus the parents' 1 Nov WhatsApp criteria only.

**Scoring vs stated priorities** (weights `ForcedChoiceCorrections!B6:B15` = G6:G15, family-set 2 Nov)

| Criterion (col) | Weight | Mum / Dad / Me rating | Fit |
|---|---|---|---|
| Near GW (M) | 5% | Important / Nice / Not needed; firm limits 25 / 25 / 90 | Weight low, but the parents' hard limits are tight. M = 10·(1−J/Filters!B4), so setting B4 to 25 also rescales M. This is why G3 (Settings B38) must come first |
| Nature (N) | 10% | Nice / Important / Essential | Partly fits; follows Me |
| Hospital (O) | 15% | Important / Nice / Important; firm 30 / 20 / 20 | Fits. B5 = 90 vs all three ≤30, so G3 applies to O too |
| Indian community (P) | 15% | C2 Important / Nice / Nice; C3–C4 all Nice | **Too high for all three**; brief says "secondary" |
| Shops & doctor (Q) | 15% | Important / Nice / Important | Fits |
| Village (R) | 5% | Not needed / Nice / Not needed | Fits survey; contradicts brief "Priority 1" |
| Train/bus (S) | 15% | Important / Nice / Important; Q14 all "C: train or bus" | Fits (shared) |
| Price (T) | 1% | Nice / **Important** / Not needed; Q3c lower / lower / higher | **Doesn't fit the parents** |
| Beach (U) | 15% | Nice / Not needed / Essential; full marks at 30 / >60 / 20 min | **Follows Me**; bands A15:C21 (10 at ≤15 min) are stricter than all three |
| City (V) | 4% | Nice / Nice / Important | Fits |

- Grocery filter (Filters!B11 = 25) sits between the firm limits 30 / 20 / 30. Fine as a compromise; Dad's 20 removes Belgrave.
- **SuburbScorecard L is typed text in all 71 rows**, so changing Filters B4/B5 changes no pass/fail status. Y excludes BG grocery fails via formula.
- Settings B28:B39 are blank (G3 and G5 not done).

**Project records:** see §5. Most of what's stale is in the register (the "Now" line dates from 30 Oct), plus the handoff's own errors.

### 2.3 Alignment map

| Priority | Mum | Dad | Me | Status |
|---|---|---|---|---|
| ED drive limit | 30 | 20 | 20 | **Aligned** (all ≤30) |
| Shops & doctor | Imp | Nice | Imp | Aligned |
| Train/bus, future transport (Q14) | Imp, C | Nice, C | Imp, C | **Aligned** |
| Open to viewing other areas (R10.3) | A | A | A | Aligned |
| Village character | Not needed | Nice | Not needed | Aligned (low) |
| Indian community C2–C4 | mostly Nice | Nice | Nice | Aligned (low) |
| Indian grocery limit | 30 | 20 | 30 | Partly |
| Mix of cultures (C1) | Nice | Nice | Imp | Partly |
| GW drive limit | 25 | 25 | 90 | **Conflict** (parents vs Me) |
| Budget (Q3c) / Price | lower / Nice | lower / Imp | higher / Not needed | **Conflict** |
| Beach | Nice, 30 min | Not needed | Essential, 20 min | **Conflict** |
| Nature type (R8.1) | leafy streets | leafy streets | coast | Conflict |
| Area types (R10.2) | Bayside, Bush hills, Leafy | Leafy only | Bayside, Bush hills, Peninsula | **No type acceptable to all three** |
| Your living space (R6.1) | B bed+bath | C +sitting room | B | Partly (Dad wants more) |
| Near GW rating vs limit | Imp / 25 | **Nice / 25** | — | Dad's answers don't match each other |

**Core shared criteria (proposed):** ED within ~20–30 min; shops and doctor nearby; train or bus available now and for later; open to a range of areas. Village and Indian community count for little.

**Mitigations**
- GW 25 vs 90: display-only "parents' limits" view (§2.5, `tools/shortlist.py`) first. Change Filters B4 only after G3 and approval.
- Price and beach: scenario weights in the model spec (family-set vs parents-only vs equal say), showing changes to the top 10. No live weight change.
- Area types: ask (Q2 below). Until then, tag each shortlist suburb with its area card and show which person each one satisfies.

**Recording:** one root file, `Family conversations — before parents leave (Nov 2026).md`. Each answer gets: question, who answered, date, verbatim answer, and the cell or task it would affect. Approved outcomes then go into the DiscussionSummary decision log, the Filters C notes and the `scoring-model-pointer.md` change log.

### 2.4 Data gaps

| Gap | Affects | Candidate source (verify first) | Deep research? |
|---|---|---|---|
| AY (grocery) blank in 14 real rows, BJ (beach) in 13, M/T in 12. W<10 means no X and no rank | Y, ranking coverage | Chrome B4/B2 drive times | No — Chrome task |
| ABS 2021 only (AK–AW); 8 rows under 2,500 population (perturbed) | P (AQ % Indian ancestry), AX | ABS Census 2026 first release (timing unverified; likely 2027), ABS Regional Population ERP by SA2, Vic Govt *Victoria in Future* | No: wait for Census 2026; note as Estimate |
| Diversity is shown only through AK–AW and AX | C1 (Me Important) | Same as above | No |
| RBA cash rate 4.60%, Needs verification; `rba_next_move` predates 3 Nov; market data review_due after 3 Nov (validator prints INFO only, never fails) | M4, auction decision | RBA media release 3 Nov 2026; RBA cash rate table | No: a 15-min lookup |
| Clearance rates and summer listings | M1–M2 | CoreLogic / Domain weekly clearance | No |
| Insurance and running costs for card B/C suburbs | Price realism | Insurer quote tools, council rates pages | Maybe later |
| Indian restaurant drives (R11.2 firm limits 30 / 25 / 20) | Possible new filter | B10 pilot (Chrome) | No |

### 2.5 Path to automated shortlisting

Pipeline: export JSON → `import_v14.py` (N3) → recalc (S5) → **`tools/shortlist.py <recalculated wb> <config.json> <out dir>`**.
- **Config** `config/shortlist.json`: scenarios (family-set, parents' limits), thresholds and price bands. Static config, per house rules.
- **Logic:** reads J/K/AY/G/X/Y plus the area card. Computes filter status itself from the config, so it never writes L. Outputs `research/shortlist/shortlist-<date>.{json,md}`: suburb, rank per scenario, which person's limits it meets, price band, and property thresholds (from Settings B28:B37 after G5).
- **Saved searches:** from that JSON, per portal: suburbs, price max, bedrooms, bathrooms, land size. The user, or Chrome (B1), enters them into realestate.com.au and Domain, because realestate.com.au is blocked from scripts.
- **Optional, needs approval:** make L a formula from Filters so the workbook and the script agree.

## 3. Phased plan

Handoff steps → disposition:
1. Housekeeping: **reordered and changed** (Phase 1; drop `uv sync`).
2. 25 vs 90 decision: **kept**, after the parent conversation (Phase 0 → 3).
3. N3: **kept** (Phase 2), with the fix widened to B71:D71.
4. N4 / G5 / model spec / G4 / G7: **kept** (Phases 3–4).
5. M4: **moved to Phase 0**.
6. Chrome tasks: **kept** (Phase 4, parallel).
7. Other approvals: **merged** into the gates list (Phase 3).

| ID | Goal | Inputs | Done when | Deps | Approval | Model / effort | Support |
|---|---|---|---|---|---|---|---|
| **Phase 0: this week** | | | | | | | |
| P10 (new) | Parent question sheet (§4b) | export JSON, §2.3 | File exists in root; questions ranked | — | N (draft); Y to send | Opus / **high**: alignment design | dataviz (optional), my-writing-style |
| P11 (new) | Hold the conversation; record answers | P10 | `Family conversations…md` filled, one line per answer, each tagged with the cell or task it affects | P10 | — | User | — |
| P12 (new) | Capture Mum's 31 Oct WhatsApp: verbatim source `research/inputs/whatsapp-mum (31 Oct 2026).md`; extracted lines (with cell/task tags) in the conversations file | message text | Both files exist; each line tagged to G5 / SL2 / D1 / C-status / A-14 | — | N (Tecoma status change = Y) | Haiku | quick-worker |
| M4 | Record the 3 Nov RBA decision (rate, URL, date, Checked) on `research/properties/5-northam-street-glen-waverley.yaml`; leave the macro YAML at review_due (its validator rejects non-PDF sources, `tools/validate_macro.py:155`) | RBA release | Northam YAML has the 3 Nov entry; `git diff --stat` touches only that file; validator still exits 0 | — | Y (M-series) | Sonnet / low | — |
| M4b (new, later) | Schema/validator support for post-PDF sources + version bump + `--write-snapshot` | — | Validator exits 0 with a new source | M4 | Y | Sonnet | — |
| A-14 (new) | Auction go/no-go note: guide vs B2/B3, parents' budget answer | Northam YAML, P11 | User decision recorded before Sat 11:00 | P11, M4 | Y | User | — |
| **Phase 1: housekeeping** | | | | | | | |
| H1 | Fast-forward `claude/claude-md-fixes`; delete `origin/claude/claude-md-fixes` and `origin/claude/ecstatic-tesla-pzbg1v` (same commit) | origin branch | `git merge-base --is-ancestor main origin/claude/claude-md-fixes` passes, then `git merge --ff-only`; push and delete both remote branches | — | **Y** (push and delete) | Haiku | — |
| H2 | S3–S8 setup | §2.1 | Allowlist works; SessionStart prints macro status | H1 | N | Sonnet | claude-md-improver, fewer-permission-prompts, update-config |
| H3 | `tools/recalc_test.sh` | workflow.md | `bash tools/recalc_test.sh "Our Next Home — Family Relocation Scoring Model.xlsx"` → RECALC OK, Y=37, canonical unchanged | — | N | Sonnet | — |
| H4 | Records corrections (§5) | §5 | Register, PROJECT_STATE and pointer updated; B9 split into B9 / B12 | — | N | Haiku | quick-worker |
| **Phase 2: N3 import** (one workbook session) | | | | | | | |
| N3a | Test import into scratch | export, wb | `.venv/bin/python tools/import_v14.py Handoffs/data/questionnaire-responses-export-2026-11-10.json "Our Next Home — Family Relocation Scoring Model.xlsx" <scratch>/out.xlsx` exit 0; rows 17–19; CB–CH | H3 | N | Sonnet | — |
| N3b | Archive, import to canonical, rewrite B71:D71 (R6.1 only) | N3a | Recalc OK, 37 ranked, B71:D71 = "OK"; diff shows only the new headers, rows and CleanedAnswers rows 97–103 plus B71:D71; pointer log entry | N3a | Y (A1 gate) | Sonnet | recalc_test.sh |
| N4 | H59/H61 and counts; report both L-only and L+BG counts | N3b | Recalc OK; both counts logged | N3b | **Y** (register line 72) | Sonnet | — |
| **Phase 3: decisions and model spec** | | | | | | | |
| D1 (spec) | Model spec: scenario weights (family-set / parents-only / equal), community rule (highest C1–C4), impact on top 10 and excluded suburbs | N3b, P11 | Spec .md with scenario tables from a temp copy | N3b | Y to adopt | Opus / **high**: scoring method | — |
| G3 | M/O decoupling (Settings B38/B39 = 90) | spec | Recalc OK, X unchanged | D1 | **Y** | Sonnet | recalc_test.sh |
| G2a/b | Filters B4/B5 per decision | G3, P11 | Recalc OK; L rebuilt or regenerated; count logged | G3 | **Y** | Sonnet | — |
| G4 | L re-evaluation / L as formula | G2 | Recalc OK | G2 | **Y** | Sonnet | — |
| Gates | M1–M3, M5, bushfire thresholds and display column, AD/Z/AC edits, B11, P4 order, P6 Point Cook | — | Each approved or rejected in the register | — | **Y** each | — | — |
| **Phase 4: shortlist automation** | | | | | | | |
| G5 | Property thresholds Settings B28:B37 (R6.1 Dad C vs B, land bands) | P11, N3b | Recalc OK | N3b | **Y** | Sonnet | — |
| SL1 (new) | `tools/shortlist.py` + `config/shortlist.json` (display-only) | recalc copy | Run on the recalc copy outputs 37 rows for family-set, and the parents'-limits count matches the §1 count (15) or explains the difference | H3 | N | Sonnet | — |
| SL2 (new) | Saved-search criteria per portal | SL1, G5 | `research/shortlist/saved-searches-<date>.md` | SL1, G5, D1, G2a/b, G4 | Y before entering | Sonnet | — |
| B1, B2, B4, B10, B12 | Chrome research | prompts file | Col Z sourced; register updated | — | N | Sonnet | claude-in-chrome |
| G7 | Regenerate reports | recalc copy | `report2.py` output rebuilt; Draft | G2–G5 | Y to distribute | Sonnet | — |
| Final | Plan critique before Phase 3 | this plan | Findings resolved | — | — | Opus / **high** | critique-plan |

## 4. Open questions

### 4a. For you (ranked)
1. Do the weights deliberately follow your priorities? If not, approve the scenario comparison in D1 before G2.
2. Your parents rate Glen Waverley as a hard limit (25 min). Treat it as a filter (G2) or a display-only view first? (Recommendation: view first, then decide after P11.)
3. 5 Northam St is above budget, and both parents said the budget should be lower: go, no-go, or raise B2?
4. PROJECT_INSTRUCTIONS calls village feel Priority 1 and regional areas up to 1.5 hr in scope; the v18 answers contradict both. Update the brief?
(Former Q5 removed: `--blank-context` is not allowed for v18. It blanks Q15.3 and puts #N/A into PriorityWeights row 4 (`tools/import_v14.py:6-9`). N3 runs without it until D1 replaces row 4.)

### 4b. For Mum and Dad (ranked by shortlist impact; wording draft, to be put in your voice in P10)
1. "Is 25 minutes to Glen Waverley a firm no beyond that, or what you'd like? Would 35 be OK for the right place?" (Keeps 15 suburbs vs 37.)
2. "Dad, you picked leafy suburbs only. Would you look at bush-edge hills or bayside if the house was right?" (No area type suits all three.)
3. "You both said the budget should be lower. What's the most you'd be comfortable spending?" (Price weight, auction.)
4. "Is 5 Northam St worth bidding on above $1.5m?" (Saturday.)
5. "Dad, how important is my own sitting room versus just a bedroom and bathroom?" (G5 floor-plan threshold.)
6. "How much does being near the beach matter to you?" (15% weight.)
7. Confirm Mum's 31 Oct list as minimums: 3–4 bed, 2.5 bath, no weatherboard, small yard fine; stairs OK (Filters B6 allows stairs)? (G5, SL2.)
8. "Tecoma was 'gone' because of the population. Is a mixed area a must, or a strong preference?" (P weight, C-status of Tecoma and similar hills suburbs.)

Use the P10 sheet, not the 6 Nov draft reports, in this conversation: the reports reflect the unaligned 2 Nov weights.

## 5. Record corrections after approval

- **Handoff (10 Nov):** `.venv` works (not broken); `settings.local.json` is ignored, not untracked; B71:C71 → B71:D71; "16 of 37" not reconciled (15 counted from inputs).
- **Register:** "Now" line (30 Oct) → 10 Nov; P9 done 6 Nov; G7 merged 6 Nov; cloud section: credit ended 4 Nov; M2 past due; M4 overdue; second B9 (floorplan fields) → B12; add D1–D3 rows; add P10, P11, A-14, SL1, SL2; G2 stays G2a/G2b.
- **PROJECT_STATE:** "link not yet sent" → survey complete 6 Nov; next task ID; date.
- **CLAUDE.md:** via H1 + H2.
- **PROJECT_INSTRUCTIONS:** only if you answer 4a Q4.

## Verification
- After H3: `bash tools/recalc_test.sh "<canonical>"` → RECALC OK, Y=37, canonical unchanged.
- Each workbook task: recalc on the archive and on the new file, diff the changed cells, log in the pointer.
- `.venv/bin/python tools/validate_macro.py` exit 0 after M4.
- Not tested in planning: the import dry run (blocked by plan mode), the 15-vs-16 count (proxy from typed L and AY, not a recalculated Y).
