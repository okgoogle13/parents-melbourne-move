# 2 Nov 2026 (user-approved): beach drive columns + U from beach drive; P = option B; family-set weights.
import openpyxl, sys, json, re
from copy import copy
from openpyxl.comments import Comment
p, beach_json = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(p); s = wb["SuburbScorecard"]; fc = wb["ForcedChoiceCorrections"]
beach = json.load(open(beach_json, encoding="utf-8"))
rows = {s.cell(r,1).value: r for r in range(2, 91) if s.cell(r,1).value}
# beach columns
for col, h in {"BJ":"Drive to nearest beach (min; 10:00 weekday, low end of range)","BK":"Drive to nearest beach (min; 10:00 weekday, top of range)"}.items():
    assert s[f"{col}1"].value is None
    s[f"{col}1"] = h; s[f"{col}1"]._style = copy(s["AY1"]._style); s.column_dimensions[col].width = 16
n = 0
for name, b, lo, hi, km in beach:
    if name not in rows: continue
    r = rows[name]; s[f"BJ{r}"] = lo; s[f"BK{r}"] = hi
    rng = f"{lo}–{hi}" if lo != hi else f"{lo}"
    note = f"Beach 2 Nov 2026: nearest beach {b}, {rng} min, {km} (Google Maps, depart Tue 3 Nov 2026 10:00, 'typically'; BJ low end feeds U; Checked)."
    z = s[f"Z{r}"].value or ""; s[f"Z{r}"] = (z + " | " + note) if z else note; n += 1
print("beach rows", n)
# P and U formulas
for r in rows.values():
    s[f"U{r}"] = f'=IF(BJ{r}="","",ROUND(MAX(0,MIN(10,10*(60-BJ{r})/50)),1))'
    s[f"P{r}"] = f'=IF(OR(AY{r}="",AQ{r}=""),"",ROUND(0.5*MAX(0,MIN(10,10*(30-AY{r})/25))+0.5*MAX(0,MIN(10,10*AQ{r}/0.08)),1))'
s["U1"].comment = Comment("Since 2 Nov 2026 (user-approved): calculated from BJ (drive to nearest beach, low end): 10 at 10 min or less, 0 at 60 min or more, straight line between. Previous judgement scores in Archive '(superseded 2026-11-02, before scoring change)'.", "Claude")
s["P1"].comment = Comment("Since 2 Nov 2026 (user-approved option B): half grocery drive (AY: 10 at 5 min or less, 0 at 30 min) + half share born in India (AQ: 10 at 8%, Glen Waverley's level, or more). Previous judgement scores in Archive '(superseded 2026-11-02, before scoring change)'.", "Claude")
# weights
W = {6:0.05, 7:0.05, 8:0.15, 9:0.15, 10:0.15, 11:0.05, 12:0.15, 13:0.05, 14:0.15, 15:0.05}
assert fc["G5"].value is None
fc["G5"] = "Family-set weight (2 Nov 2026; replaces survey-based weights)"; fc["G5"]._style = copy(fc["F5"]._style)
for r, w in W.items():
    assert fc[f"G{r}"].value is None
    fc[f"G{r}"] = w; fc[f"G{r}"]._style = copy(fc[f"F{r}"]._style)
    fc[f"B{r}"] = f"=G{r}"
fc["A20"] = "2 Nov 2026 (user instruction): weights set directly by the family in column G and B now equals G. Top priorities (15% each): Indian community, Hospital, Shops & doctor, Beach, Train/bus. Others 5% each. Earlier survey answers no longer feed the weights (columns C, D, F kept for reference). Previous formulas in Archive '(superseded 2026-11-02, before scoring change)'."
assert abs(sum(W.values()) - 1) < 1e-9
wb.save(p); print("saved")
