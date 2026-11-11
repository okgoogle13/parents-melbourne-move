# D2b Comparison: Live `AU` vs Exact SAL `M3_SAL` Under Approved Score `P` (11 Nov 2026)

This note executes the second half of **Task D2b** (`Open work — what runs where (27 Oct 2026).md`) using the Phase 1 dataset ([`research/abs/sal_diversity_gcp_2021.csv`](file:///Users/okgoogle13/Projects/Parents%20Melbourne%20MOVE/research/abs/sal_diversity_gcp_2021.csv)) and the current canonical workbook (`Our Next Home — Family Relocation Scoring Model.xlsx`, SHA-256 prefix `b6851f3580e5`, after `D2`, `D2c`, and the `11 Nov AZ correction`).

All scores and ranks below were recalculated in headless LibreOffice (`tools/recalc_test.sh` temp-copy method). **No workbook edits were made** to the canonical file.

---

## 1. Formula & Anchors Compared (`35/15/35/15` Score `P`)

Both runs use the live `D2` structure in `Filters!A22:C29` and live `AZ` restaurant drives:
- `35%` Indian grocery drive (`AY`: `10` at $\le 5$ min, `0` at $\ge 30$ min)
- `15%` Indian restaurant drive (`AZ`: same scale)
- `35%` Multicultural mix:
  - **Live Canonical (`AU`):** `% other language at home` (`G01`), floor `5.0%` (`Filters!B27`, Tecoma `4.5%`), full marks `20.0%` (`Filters!B28`, Ferntree Gully `18.7%`). Counts Southern European households (`D-7`).
  - **`D2b` Temp Copy (`M3_SAL`):** `% born overseas outside MESC` (`G01 Birthplace_Elsewhere_P` minus `8` G09 overseas MESC columns, `Tot_P_P` denominator). Keeps Italy, Greece, and all other non-Anglo countries (`D-7`); excludes UK (England, Scotland, Wales; Northern Ireland is inside `P_Elsewhere_Tot` in G09), Ireland, NZ, USA, Canada, and South Africa. Floor = Tecoma `M3_SAL` (`6.83%` / `0.068314`), full marks = Ferntree Gully `M3_SAL` (`18.40%` / `0.183955`).
- `15%` South Asian share (`MAX(AQ, AR)`: `10` at `8.0%`, Glen Waverley benchmark).

---

## 2. Headline Findings (**Checked**, LibreOffice Temp Copies)

- **Recalc status:** `0` formula errors on both runs (`51` numeric `X`, `37` ranked `Y`; canonical SHA unchanged `b6851f3580e5`).
- **Spearman rank correlation (`n = 37`):** $\rho = 0.9981$.
- **Top 10, Top 12, and Top 15 membership:** **100% unchanged** (zero suburbs enter or leave).
- **Moves of `3+` places:** **0** across all `37` ranked suburbs. Largest rank shift is **`Altona` (`#8` $\rightarrow$ `#10`, `-2` places)** inside a `0.01`-point cluster (`Croydon 7.02`, `West Footscray 7.01`, `Altona 7.01`).
- **Maximum score shifts:** `max |dP| = 0.70` (`Newport`, `7.7` $\rightarrow$ `7.0`, stays `#4`); `max |dX| = 0.0805` out of `10` (`Newport`, `7.23` $\rightarrow$ `7.15`).
- **Rounded-anchor sensitivity:** Testing rounded `Filters!B27:B28` (`0.070` / `0.185`, analogous to `0.05 / 0.20` for `AU`) keeps `X` within `0.01` across all 37 rows and produces identical Top 15 membership.

---

## 3. Full 37-Suburb Recalculated Comparison (`Y_AU` Order)

| Suburb | `AY` | `AZ` | `AQ` | `AR` | `AU` | `M3_SAL` | `P` (`AU`) | `P` (`M3`) | `X` (`AU`) | `X` (`M3`) | Rank (`AU`) | Rank (`M3`) | Shift |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Frankston** | 3 | 2 | 1.1% | 1.4% | 12.1% | 12.6% | 6.9 | 7.0 | 7.66 | 7.67 | `#1` | `#1` | `0` |
| **Berwick** | 7 | 1 | 6.1% | 7.4% | 28.7% | 26.1% | 9.6 | 9.6 | 7.27 | 7.27 | `#2` | `#3` | `-1` |
| **Ferntree Gully** | 8 | 3 | 2.3% | 3.1% | 18.7% | 18.4% | 8.4 | 8.7 | 7.24 | 7.28 | `#3` | `#2` | `+1` |
| **Newport** | 9 | 5 | 1.1% | 1.8% | 17.6% | 14.1% | 7.7 | 7.0 | 7.23 | 7.15 | `#4` | `#4` | `0` |
| **Seaford** | 8 | 5 | 0.6% | 1.0% | 9.6% | 9.9% | 5.8 | 5.7 | 7.14 | 7.13 | `#5` | `#6` | `-1` |
| **Ringwood** | 4 | 2 | 3.2% | 3.7% | 31.6% | 29.8% | 9.2 | 9.2 | 7.14 | 7.14 | `#6` | `#5` | `+1` |
| **Rosanna** | 6 | 1 | 2.8% | 3.8% | 23.5% | 20.7% | 9.1 | 9.1 | 7.13 | 7.13 | `#7` | `#7` | `0` |
| **Altona** | 9 | 5 | 1.4% | 1.9% | 19.6% | 17.8% | 8.2 | 8.1 | 7.02 | 7.01 | `#8` | `#10` | `-2` |
| **Croydon** | 1 | 2 | 2.3% | 2.9% | 18.9% | 17.7% | 8.8 | 8.8 | 7.02 | 7.02 | `#9` | `#8` | `+1` |
| **West Footscray** | 7 | 7 | 3.7% | 3.6% | 32.0% | 27.7% | 8.8 | 8.8 | 7.01 | 7.01 | `#10` | `#9` | `+1` |
| **Heidelberg** | 1 | 1 | 3.0% | 3.5% | 23.7% | 21.5% | 9.2 | 9.2 | 6.99 | 6.99 | `#11` | `#11` | `0` |
| **Upper Ferntree Gully** | 14 | 1 | 1.0% | 1.4% | 8.3% | 10.2% | 4.8 | 5.0 | 6.90 | 6.92 | `#12` | `#12` | `0` |
| **Upwey** | 16 | 3 | 0.6% | 1.0% | 6.3% | 7.8% | 4.0 | 4.0 | 6.88 | 6.88 | `#13` | `#13` | `0` |
| **Mentone** | 16 | 2 | 1.9% | 2.5% | 19.8% | 18.6% | 7.4 | 7.4 | 6.83 | 6.83 | `#14` | `#14` | `0` |
| **Mordialloc** | 22 | 3 | 1.4% | 2.2% | 18.7% | 16.2% | 6.2 | 5.9 | 6.76 | 6.73 | `#15` | `#15` | `0` |
| **Chelsea** | 20 | 1 | 1.4% | 1.8% | 14.7% | 14.6% | 5.5 | 5.6 | 6.59 | 6.60 | `#16` | `#16` | `0` |
| **Belgrave** | 24 | 2 | 0.4% | 0.9% | 7.0% | 8.0% | 3.0 | 2.9 | 6.55 | 6.54 | `#17` | `#17` | `0` |
| **Eltham** | 24 | 2 | 0.7% | 1.3% | 10.5% | 10.0% | 3.9 | 3.5 | 6.49 | 6.44 | `#18` | `#19` | `-1` |
| **Tecoma** | 20 | 1 | 0.3% | 0.9% | 4.5% | 6.8% | 3.1 | 3.1 | 6.48 | 6.48 | `#19` | `#18` | `+1` |
| **Frankston South** | 8 | 4 | 0.9% | 1.3% | 9.0% | 9.7% | 5.8 | 5.7 | 6.27 | 6.26 | `#20` | `#20` | `0` |
| **Diamond Creek** | 22 | 2 | 0.7% | 1.1% | 8.7% | 8.0% | 3.7 | 3.2 | 6.19 | 6.13 | `#21` | `#22` | `-1` |
| **Highton (Geelong)** | 7 | 4 | 2.4% | 2.7% | 13.0% | 12.7% | 7.1 | 7.0 | 6.16 | 6.15 | `#22` | `#21` | `+1` |
| **Newtown (Geelong)** | 7 | 3 | 1.3% | 1.6% | 8.8% | 8.8% | 5.9 | 5.6 | 5.95 | 5.92 | `#23` | `#24` | `-1` |
| **Warragul** | 3 | 2 | 1.0% | 1.3% | 6.8% | 8.0% | 5.7 | 5.6 | 5.95 | 5.94 | `#24` | `#23` | `+1` |
| **The Basin** | 8 | 5 | 0.2% | 0.9% | 8.2% | 9.3% | 5.5 | 5.5 | 5.88 | 5.88 | `#25` | `#25` | `0` |
| **Mornington** | 22 | 12 | 0.4% | 0.5% | 5.6% | 7.4% | 2.4 | 2.5 | 5.80 | 5.81 | `#26` | `#26` | `0` |
| **Warrandyte** | 18 | 2 | 0.7% | 1.5% | 13.0% | 12.2% | 5.3 | 5.1 | 5.77 | 5.75 | `#27` | `#27` | `0` |
| **Montrose** | 10 | 7 | 0.4% | 0.7% | 4.8% | 6.6% | 4.3 | 4.3 | 5.66 | 5.66 | `#28` | `#28` | `0` |
| **Mount Evelyn** | 16 | 2 | 0.2% | 0.5% | 4.2% | 5.4% | 3.6 | 3.6 | 5.51 | 5.51 | `#29` | `#29` | `0` |
| **Sassafras** | 20 | 7 | 0.0% | 0.6% | 7.2% | 9.3% | 3.4 | 3.6 | 5.44 | 5.47 | `#30` | `#30` | `0` |
| **Torquay** | 16 | 2 | 0.2% | 0.4% | 4.7% | 5.1% | 3.5 | 3.5 | 5.43 | 5.43 | `#31` | `#31` | `0` |
| **Drouin** | 12 | 3 | 0.5% | 0.8% | 4.9% | 6.3% | 4.2 | 4.2 | 5.40 | 5.40 | `#32` | `#32` | `0` |
| **Olinda** | 22 | 3 | 0.2% | 0.8% | 7.1% | 8.2% | 3.3 | 3.2 | 5.33 | 5.32 | `#33` | `#33` | `0` |
| **Gisborne** | 14 | 2 | 0.6% | 0.7% | 5.3% | 6.3% | 3.9 | 3.9 | 5.28 | 5.28 | `#34` | `#34` | `0` |
| **Mount Dandenong** | 20 | 4 | 0.6% | 0.8% | 5.6% | 8.0% | 3.2 | 3.4 | 5.04 | 5.07 | `#35` | `#35` | `0` |
| **Riddells Creek** | 16 | 1 | 0.3% | 0.3% | 3.5% | 4.3% | 3.5 | 3.5 | 4.67 | 4.67 | `#36` | `#36` | `0` |
| **Macedon** | 20 | 9 | 0.2% | 0.4% | 3.9% | 4.8% | 2.7 | 2.7 | 4.47 | 4.47 | `#37` | `#37` | `0` |

*Note on the 14 unranked grocery-fail suburbs (with numeric `X`) and 6 comparators:* Only `Warburton` (`P 1.6 -> 2.0`), `Kyneton` (`1.7 -> 1.6`), `Dromana` (`2.6 -> 2.4`), `Rosebud` (`1.9 -> 1.7`), and `Rye` (`2.2 -> 2.0`) shift on `P`, moving `X` by at most `0.04`. All 6 comparators stay blank on `P` (`AY` is blank) and sit far above `20%` on both `AU` (`46.0%–75.6%`) and `M3_SAL` (`41.7%–64.5%`).

---

## 4. Conceptual Trade-Off & Recommendation for `D2b`

1. **What `M3_SAL` adds vs what `AU` already captures:**
   - `M3_SAL` captures English-speaking non-Anglo first-generation migrants (e.g., English-speaking households born in India, Sri Lanka, Singapore, Malaysia, Philippines) that `AU` misses.
   - `AU` captures Australian-born second-generation households speaking another language at home (explaining why `Newport` is `17.6% AU` vs `14.1% M3_SAL`).
   - Meanwhile, the `15%` South Asian term `MAX(AQ, AR)` already covers Indian-origin families who speak English at home, and under the `35%` mix weight anchored to Tecoma and Ferntree Gully, both metrics produce **identical Top 10, Top 12, and Top 15 lists** ($\rho = 0.9981$).
2. **Recommended decision:** Either option is robust (`±1` swap at most outside `#8–#10`). Keeping live `AU` avoids an unnecessary workbook formula churn before `R1` (foundation report refresh); switching to `M3_SAL` is straightforward via column `BC` if explicitly approved.

