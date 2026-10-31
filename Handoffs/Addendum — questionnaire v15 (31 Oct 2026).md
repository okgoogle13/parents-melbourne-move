# Handoff addendum — questionnaire v15 (31 Oct 2026)

From the claude.ai session. Supplements `Handoffs/Handoff — wait-period work (31 Oct 2026).md`.

## What happened

- The user approved v15 on 31 Oct 2026. It adds a new part, "Timing" (Part 11 of 12, before Priorities), and on-screen "Question n" numbers within each part. The numbers are display only; tags are unchanged.
- **Published** to the same artifact URL as version id `1793422020-3c29`. The live page sha256 is `8cc44f4d64d1`, identical to `Our Next Home — questionnaire page v15 (Claude artifact source).html` (added to the root by this session).
- `PAGE_VERSION = 15`, MODE "v15 trade-offs survey with timing (31 Oct 2026)", draft key `onh-v15-draft-`. The import panel now rejects v14 messages; no parent had a v14 draft or message (link not sent).
- Built from the live v14 (sha `c7547bc46138`, which includes the bushfire wording committed in `f3deeda`).
- When v15 was published, another session had uncommitted work in progress: staged renames (page → "page v14", parent report → "v3") and edits to PROJECT_STATE, the pointer, the round 8 note, `docs/workflow.md` and the tests README. This session did **not** touch those files. It only added new files: the v15 page source, `tools/questionnaire_tests/timing.test.js`, and updated `regression.test.js` / `import.test.js` (expectations moved to v15, plus a "v14 rejected" check).

## New questions (stored values)

| Tag | Plain name | Options (stored text) | Shown |
|---|---|---|---|
| R9.1 | When to have moved by | A — Within 3 months / B — 3–6 months / C — 6–12 months / D — Over a year / E — When the right place comes up | always |
| R9.2 | If prices fell after we bought | A — Fine, we're staying long term / B — Uneasy but OK / C — Very unhappy (question text includes "about $75,000 on a $1.5m home") | always |
| R9.3 | Sell Beachmere first or buy first | A — Sell first / B — Buy first / C — At the same time / D — Not sure | always |
| R9.4 | Where to live until we buy | A — Stay in Beachmere / B — Rent in Melbourne / C — Stay with family in Glen Waverley / D — Not sure / X — Not asked (didn't choose sell first or at the same time) | only if R9.3 = A or C; otherwise X stored automatically |
| R9 Notes | Notes on timing | free text: "Is there anything that means we must move by a certain date?" | always (optional) |

Purpose: each person's private view on urgency and sequence, for the market-timing note. These answers feed no weight, filter or score.

Nish answered v14 (30 Oct) and has no R9 answers. The user may give them in chat; record them at import as source "chat".

## Checks run (claude.ai, headless Chromium, phone width)

- `regression.test.js`: FAILS 0. Ladder paths, branching, one question per screen, export→import round trip (44 answers), v13 rejected, v14 rejected.
- `r86.test.js`: FAILS 0.
- `timing.test.js`: FAILS 0.
  - R9.4 is asked for A/C and stored as X for B/D.
  - It isn't stored while R9.3 is blank, and switches to X if R9.3 changes away.
  - Numbering reads "Question 1–4" (R9.4 unnumbered when hidden); Priorities are numbered 1–10.
  - The notes round trip works; no sideways scroll.
- `import.test.js`: WhatsApp prefixes, invisible characters and backticks all import (45 answers); v13 and v10 are rejected.

## To do (VS Code session, after the in-progress work is committed)

1. **Archive v14:** move `Our Next Home — questionnaire page v14 (Claude artifact source).html` to `Archive/… (superseded 2026-10-31, v14 before timing part).html`, keeping the "page vN" naming the other session introduced.
2. **Docs:** pointer change log entry; round 8 design note (or a short "round 9" section) with the table above; `PROJECT_STATE.md` (survey now v15; link still not sent); register; `tools/questionnaire_tests/README.md` (add `timing.test.js`; expectations now v15).
3. **Import script:** extend `tools/import_v14.py`, or add v15 support. Accept pageVersion 14 and 15. Add RawResponses columns R9.1, R9.2, R9.3, R9.4, R9 Notes with CleanedAnswers lookups (same pattern as BF–BR / rows 73–87). Leave v14 records' R9 columns blank (or fill from chat answers, flagged). Re-run the T2 tests on a temp copy. The canonical workbook stays untouched (gated step A1).
4. **Gated plan:** in Phase A0, the export must include both v14 (Nish) and v15 (Mum, Dad) records. Phase F's version rule now applies from v15.
5. **Commit locally.** The user is fine with pushing being public, but a push still needs their explicit "push" (gate H2).

## Separate, not in the survey: money conversation checklist

The user is to talk this through with their parents and keep the answers out of the public repo (e.g. a git-ignored file):
1. Beachmere: a recent estimate of its value, and how much is owing.
2. Cash for the deposit, Victorian stamp duty and the interstate move.
3. Loan: needed? how much? pre-approval? what a lender says about loan term or an exit plan at their age.
4. Nish's contribution, or being on the title.
5. Age Pension or concession card: sale proceeds held in cash may count after an exemption period (to verify).
6. Any date that forces a move.
