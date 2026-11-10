#!/usr/bin/env bash
# Recalc test: recalculates a temp copy of a workbook (never the file itself).
# Usage: bash tools/recalc_test.sh <workbook.xlsx>
# Prints errors, X and Y counts, canonical-unchanged, and the recalculated copy's path
# (keep it for tools/report2.py). Exit 0 = RECALC OK and canonical unchanged; 1 otherwise.
set -u
WB="${1:?usage: bash tools/recalc_test.sh <workbook.xlsx>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PY="$ROOT/.venv/bin/python"
SOFFICE=$(command -v soffice || echo /Applications/LibreOffice.app/Contents/MacOS/soffice)
[ -x "$SOFFICE" ] || { echo "LibreOffice not found: test cannot run"; exit 1; }
H0=$(shasum -a 256 "$WB")
T=$(mktemp -d); mkdir "$T/in" "$T/out"
# Resave to strip any cached values, forcing a full recalc.
"$PY" -I -c 'import openpyxl,sys; openpyxl.load_workbook(sys.argv[1]).save(sys.argv[2])' "$WB" "$T/in/wb.xlsx" || exit 1
"$SOFFICE" --headless --calc --convert-to xlsx --outdir "$T/out" "$T/in/wb.xlsx" >/dev/null 2>&1 || exit 1
"$PY" -I -c '
import openpyxl,sys
wb=openpyxl.load_workbook(sys.argv[1],data_only=True)
E={"#REF!","#VALUE!","#NAME?","#DIV/0!","#N/A","#NUM!","#NULL!"}
err=[(ws.title,c.coordinate) for ws in wb for r in ws.iter_rows() for c in r if c.value in E]
ws=wb["SuburbScorecard"]
num=lambda col:sum(isinstance(ws[f"{col}{r}"].value,(int,float)) for r in range(2,ws.max_row+1))
print("errors:",len(err),err[:10],"| X numeric:",num("X"),"| Y ranked:",num("Y"))
sys.exit(1 if err or not num("Y") else 0)' "$T/out/wb.xlsx"
RC=$?
[ $RC -eq 0 ] && echo "RECALC OK" || echo "RECALC FAILED"
if [ "$H0" = "$(shasum -a 256 "$WB")" ]; then echo "canonical unchanged"; else echo "CANONICAL CHANGED"; RC=1; fi
echo "recalculated copy: $T/out/wb.xlsx"
exit $RC
