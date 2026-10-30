# Workflow and workbook reference

Procedures loaded on demand from `CLAUDE.md`. Status counts, ranks and the change history live in `scoring-model-pointer.md`; this file covers structure and procedure only.

## Workbook structure

Ten tabs. Data flows roughly in this order:

- **RawResponses** → **CleanedAnswers**: one row per questionnaire submission. CleanedAnswers pulls each person's *latest* row (Mum, Dad, Me) with `LOOKUP`, plus the Max-2-Essential check. Context answers (not weighted) are in A30:G39; Q13d is RawResponses col AN and CleanedAnswers row 40 (reference-only).
- **PriorityWeights**: per-person Q15 scores, normalised and combined by the say-in-decision weights in **Settings**.
- **ForcedChoiceCorrections**: trade-off engine in H1:U5 (Q10–Q13). If the winner isn't 2 pts ahead, it moves `MIN(loser, (loser−winner+0.02)/2)` from loser to winner. C6:C15 hold the net corrections and col F manual tweaks. Final criteria weights are **B6:B15**, which SuburbScorecard X reads.
- **Filters**: hard caps (budget, Glen Waverley drive, ED drive; train preferred, not required). They drive SuburbScorecard col L.
- **SuburbScorecard**: one row per location.
  - Rows 49–50 are synthetic test rows, excluded everywhere.
  - Rows 67–72 are Community comparators: C = `Community comparator`, F = corner. Their L reads "Comparator: filters met (not ranked)" and avoids the word "pass", so Y and the DiscussionSummary passing count ignore them. N, P–S, U and V are blank, so they get no X.
- **Listings**: realestate.com.au properties. A–F, H–O, U and V are pasted values; G and P–T are formulas looking up Filters and SuburbScorecard. A refresh overwrites pasted columns only.
- **DiscussionSummary**: weights, status counts, decision log, comparator list (A31:B38).

### SuburbScorecard columns

| Cols | Content |
|---|---|
| A–H | Plain values: location, region, shortlist status, fit notes (D "Parents Inland/Bush Fit (P)" is not score P), investigation lens / comparator corner (F), published price (G; blank = not researched), price basis (H) |
| I | Price + est. 6% purchase costs |
| J / K | Drive minutes to Glen Waverley / nearest 24-hr public ED |
| L | Hard filter status |
| M–V | 0–10 criteria scores. M (near family: 10 at 0 min → 0 at 90 min), O (hospital, from K) and T (price: 10 at $500k → 0 at $1.5M) are formulas; N, P, Q, R, S, U, V are judgement scores |
| W / X / Y | Scores entered / weighted score / rank among pass rows only |
| Z | Sources and notes ("CHECKED …", "C3 28 Oct 2026: …") |
| AA | Legacy import text, unused |
| AB / AC | Train option (Yes/No) / station and basis |
| AD | ED used for K |
| AE–AJ | Budget verification: cap, basis, evidence type, evidence date, result, note |
| AK–AW | ABS 2021 demography (GCP DataPack, SAL VIC). Header comments define each measure; populations under 2,500 are perturbed by ABS |
| AX | Community comparison band (High/Medium/Low), display-only; "Comparison band, not a liveability score" |

## Editing the workbook

1. Read `PROJECT_STATE.md`, then re-read the workbook immediately before writing.
2. Copy the workbook to `Archive/` with a `(superseded YYYY-MM-DD, before <change>)` suffix.
3. Edit with `openpyxl` (keeps formulas). It saves without cached values; Excel and LibreOffice recalculate on open.
4. Run the recalc test below on the pre-change (Archive) and post-change files, then diff the recalculated values. Changes should appear only in the intended cells and their dependants (X/Y, passing count).

5. Add a change-log entry to `scoring-model-pointer.md`: what changed, which cells, sources, the recalc result, and "Pre-change copy in Archive". Update status counts, `Open work — what runs where (27 Oct 2026).md` and `PROJECT_STATE.md`.


### Recalc test

Recalculates a temporary copy; never the canonical file. Needs LibreOffice (`brew install --cask libreoffice`). Set `WB` to the file under test.

```bash
WB="Our Next Home — Family Relocation Scoring Model.xlsx"
SOFFICE=$(command -v soffice || echo /Applications/LibreOffice.app/Contents/MacOS/soffice)
[ -x "$SOFFICE" ] || echo "LibreOffice not found: test cannot run"
H0=$(shasum -a 256 "$WB")
T=$(mktemp -d); mkdir "$T/in" "$T/out"
python3 -I -c 'import openpyxl,sys; openpyxl.load_workbook(sys.argv[1]).save(sys.argv[2])' "$WB" "$T/in/wb.xlsx"   # strips any cached values -> full recalc
"$SOFFICE" --headless --calc --convert-to xlsx --outdir "$T/out" "$T/in/wb.xlsx"
python3 -I -c '
import openpyxl,sys
wb=openpyxl.load_workbook(sys.argv[1],data_only=True)
E={"#REF!","#VALUE!","#NAME?","#DIV/0!","#N/A","#NUM!","#NULL!"}
err=[(ws.title,c.coordinate) for ws in wb for r in ws.iter_rows() for c in r if c.value in E]
ws=wb["SuburbScorecard"]
num=lambda col:sum(isinstance(ws[f"{col}{r}"].value,(int,float)) for r in range(2,ws.max_row+1))
print("errors:",len(err),err[:10],"| X numeric:",num("X"),"| Y ranked:",num("Y"))
sys.exit(1 if err or not num("Y") else 0)' "$T/out/wb.xlsx" && echo "RECALC OK"
[ "$H0" = "$(shasum -a 256 "$WB")" ] && echo "canonical unchanged" || echo "CANONICAL CHANGED"
```

Pass = `RECALC OK` (0 errors, populated X/Y; Y ranked should match the count in `PROJECT_STATE.md`) and `canonical unchanged`. Log the result in `scoring-model-pointer.md`.

Survey import rule: a new RawResponses row per person = their previous latest row + the new round's answers. Store forced-choice answers as the full option text, because the engine reads the "A —"/"B —" prefix.

**v14 import (task N3):** `.venv/bin/python tools/import_v14.py <export.json> <in.xlsx> <out.xlsx> [--blank-context]`. Input is a page `responses` export (format of `Handoffs/data/questionnaire-responses-export-2026-10-31.json`). It never writes `<in.xlsx>` and refuses `out = in`. It takes each person's (Mum, Dad, Me) latest `pageVersion` 14 record and lists superseded ones. TEST and other versions are ignored. It appends any missing RawResponses columns BF–BR (Q3c, R8.1–R8.6), then one new row per person: the latest row carried forward, overwritten by the v14 answers. A v14 question left unanswered is blank, not carried forward. Q15 is stored as the bare letter, Q10 and Q13d are blanked, and the merge log goes in AM. `Q10-Q13c Notes` has no column and goes into AM as a labelled note. R8.6 backfill: if R8.4 is A, D or E, R8.6 is stored as X; if B or C, it stays blank and the run prints `FLAG … Needs data`. Columns v14 never asks (Q1–Q9, Q13b, Q13c, R5.1, R5.3, R6.7, Q16–Q21) are carried forward unless `--blank-context` is given. Those affect CleanedAnswers rows 7–14 and 32–37, DiscussionSummary E23:F25 and Filters D4/D6 (notes only), and no weight, filter value or score. CleanedAnswers lookups for the new columns are added at rows 73–87, below the derived block. The script exits 1 on an unmapped answer key, an `answeredCount` mismatch, an unexpected RawResponses BE1 header or a record already imported. Afterwards run the recalc test and the unrecalculated diff on `<out.xlsx>`; only the new headers, rows and CleanedAnswers rows 73–87 may differ.

## Other deliverables

- `Our Next Home — questionnaire page (Claude artifact source).html`: source of a published Claude artifact. Always republish to the same URL (in the pointer change log). Each round shows only the "still needed" questions and saves with a mode label like `round 4 (Q13d)`. Archive the previous page first.
- `Suburb shortlist foundation report` (.md + A4-landscape .pdf) and `Our Next Home — parent report (28 Oct 2026).html`: built from the workbook at a named commit. When the workbook changes, regenerate them from it; don't hand-edit numbers. Archive the previous version.
- `Claude_in_Chrome_prompt — close research gaps.md`: tasks that need the user's signed-in browser or live Google Maps (B* tasks in the open-work file).

## Research constraints (cloud sessions)

- realestate.com.au is blocked; healthdirect and OpenStreetMap have been unreachable. Leave those to Claude in Chrome and say so in col Z.
- Don't WebFetch hand-built OnTheHouse URLs (the user rejected it); use links returned by search. Agent Statement of Information PDFs give suburb medians.
- J and K use one drive-time basis per row; name it in col Z.

## Git and the local folder

`main` mirrors `/Users/okgoogle13/Projects/Parents Melbourne MOVE/`. Cloud sessions work on a `claude/*` branch and the result is fast-forwarded into `main`. The user then runs `git pull --ff-only` locally. `.claude/handoffs/LATEST.md` is committable; timestamped `HANDOFF_*` files and `.claude/handoff-nudge-state.json` (generated plugin state) are ignored. Cloud sessions see a handoff only after it is committed and pushed.
