# 2 Nov 2026: apply grocery-drive hard filter (25 min) + display-only backups (15, 30). Run from repo root on the canonical workbook (archive first).
import openpyxl, sys
from copy import copy
p = sys.argv[1]
wb = openpyxl.load_workbook(p)
f = wb["Filters"]; s = wb["SuburbScorecard"]; d = wb["DiscussionSummary"]
assert f["A11"].value is None and f["A12"].value is None and f["A13"].value is None
rows = [
 (11, "Max drive to nearest Indian grocery (APPLIED)", 25, "Family decision 2 Nov 2026 (NJD): hard limit 25 min to the nearest Indian grocery, top of the Google Maps 'typically' range, depart weekday 10:00 (SuburbScorecard AY, Checked 2 Nov 2026). Ranked rows with AY above this fail (SuburbScorecard BG) and drop out of the rank (Y)."),
 (12, "Grocery drive backup: stricter (not applied)", 15, "Backup limit for discussion only; SuburbScorecard BH shows In/Out. Change B11 to apply a different limit."),
 (13, "Grocery drive backup: looser (not applied)", 30, "Backup limit for discussion only; SuburbScorecard BI shows In/Out."),
]
for r, a, b, c in rows:
    for col, v in zip("ABC", (a, b, c)):
        cell = f[f"{col}{r}"]; cell.value = v; cell._style = copy(f[f"{col}5"]._style)
hdr = {"BG": "Grocery filter (applied, Filters B11)", "BH": "Grocery backup 15 min (display only, Filters B12)", "BI": "Grocery backup 30 min (display only, Filters B13)"}
for col, h in hdr.items():
    assert s[f"{col}1"].value is None, col
    s[f"{col}1"] = h; s[f"{col}1"]._style = copy(s["AY1"]._style)
    s.column_dimensions[col].width = 18
for r in range(2, 91):
    for col in hdr: assert s[f"{col}{r}"].value is None, (col, r)
    s[f"BG{r}"] = f'=IF(AY{r}="","",IF(AY{r}>Filters!$B$11,"Fails: grocery drive","OK"))'
    s[f"BH{r}"] = f'=IF(AY{r}="","",IF(AY{r}>Filters!$B$12,"Out","In"))'
    s[f"BI{r}"] = f'=IF(AY{r}="","",IF(AY{r}>Filters!$B$13,"Out","In"))'
    old = s[f"Y{r}"].value
    assert old == f'=IF(AND(ISNUMBER(SEARCH("pass",L{r})),ISNUMBER(X{r})),COUNTIFS(L$2:L$90,"*pass*",X$2:X$90,">"&X{r})+1,"")', (r, old)
    s[f"Y{r}"] = f'=IF(AND(ISNUMBER(SEARCH("pass",L{r})),ISNUMBER(X{r}),BG{r}<>"Fails: grocery drive"),COUNTIFS(L$2:L$90,"*pass*",BG$2:BG$90,"<>Fails: grocery drive",X$2:X$90,">"&X{r})+1,"")'
assert d["B15"].value == '=COUNTIF(SuburbScorecard!L:L, "*Pass*")'
d["A15"] = "Passing / Provisional Pass (after grocery filter)"
d["B15"] = '=COUNTIFS(SuburbScorecard!L:L,"*Pass*",SuburbScorecard!BG:BG,"<>Fails: grocery drive")'
for r, a, b in [(20, "Fails: grocery drive (Filters B11)", '=COUNTIF(SuburbScorecard!BG:BG,"Fails: grocery drive")'),
                (21, "Backup: would be out at 15 min", '=COUNTIFS(SuburbScorecard!L:L,"*Pass*",SuburbScorecard!BH:BH,"Out")'),
                (22, "Backup: would be out at 30 min", '=COUNTIFS(SuburbScorecard!L:L,"*Pass*",SuburbScorecard!BI:BI,"Out")')]:
    assert d[f"A{r}"].value is None and d[f"B{r}"].value is None
    d[f"A{r}"] = a; d[f"B{r}"] = b
    d[f"A{r}"]._style = copy(d["A19"]._style); d[f"B{r}"]._style = copy(d["B19"]._style)
wb.save(p); print("applied")
