# Bushfire screening B3-S (31 Oct 2026)

Task B3-S, run as T4 of `Handoffs/Handoff — wait-period work (31 Oct 2026).md`. This is a research output only.

**It is not a filter.** It changes no status, score, rank, card or workbook cell. Every value is an **Estimate**: a desk GIS screen using thresholds the user hasn't approved yet. A property's own VicPlan report is still the authority for any one address.

Files:
- table (one row per suburb): `bushfire-screening (31 Oct 2026).csv`
- method script: `screen.py`
- source URLs and sha256 of every downloaded file (100 files): `bushfire-screening sources (31 Oct 2026).json`

The downloaded GIS data is not in git.

## Method

1. **Suburb** = ABS 2021 Suburbs and Localities (SAL) polygon, from the ABS ASGS 2021 SAL map service (`geo.abs.gov.au/arcgis/rest/services/ASGS2021/SAL/MapServer/0`), by SAL code. The codes match the workbook's ABS references, e.g. Upwey 22620 and Warburton 22689.
2. **Residential land** = Vicmap Planning zones (`open-data-platform:plan_zone`, DataVic open WFS `opendata.maps.vic.gov.au`) with codes GRZ, NRZ, RGZ, LDRZ, MUZ or TZ, inside the SAL. Rural Living (RLZ) is reported separately and not counted. Measuring residential land avoids national park and farmland swamping the shares.
3. **Bushfire Prone Area (BPA)** = Vicmap `open-data-platform:bushfire_prone_area`. Gazettal dates in the downloaded features run to 16 Jun 2026.
4. **Bushfire Management Overlay (BMO)** = Vicmap `open-data-platform:plan_overlay` where `zone_code LIKE 'BMO%'` (all schedules).
5. **Measurement:** shares are measured on a 50 m point grid: one point = 0.25 ha, about 300–5,700 residential points per suburb. That's a stdlib method, because no GIS library was installable in this session. The grid's sampling error is well under 1 percentage point for these sample sizes. Edge effects at zone boundaries matter more near the thresholds, so those rows are flagged.
6. **Exception:** Sassafras, Mount Dandenong and Olinda have under 2 ha of residential zoning. Their housing sits in Green Wedge A, Public Conservation and Tourism zones. For these three the whole suburb is used, and it is 100% inside the BPA and the BMO on every zone, so the result doesn't depend on that choice.

Read 31 Oct 2026. Both services are open, with no sign-in. DNS to the Vicmap host failed intermittently; curl retries recovered every file, and none came from a mirror or cache.

## Proposed thresholds (for the user to approve)

| Measure | Value | Rule (share of residentially zoned land) |
|---|---|---|
| Bushfire Prone Area | Yes | ≥ 90% |
| | Partly | > 0% and < 90% |
| | No | 0% |
| BMO | most residential streets | ≥ 50% |
| | edges only | > 0% and < 50% |
| | none | 0% |

"Near threshold" flags rows where the BMO share is 40–60%, or the BPA share is 85–90%. A small boundary change could flip those labels.

## Results (Estimate)

| Suburb | Card | BPA | BMO | % res. land in BPA / BMO | Near threshold |
|---|---|---|---|---|---|
| Upper Ferntree Gully | B | Partly | most residential streets | 78 / 57 | Yes |
| Upwey | B | Yes | most residential streets | 100 / 100 | |
| The Basin | B | Partly | most residential streets | 61 / 52 | Yes |
| Tecoma | B | Yes | most residential streets | 100 / 100 | |
| Belgrave | B | Yes | most residential streets | 100 / 100 | |
| Montrose | B | Partly | edges only | 77 / 45 | Yes |
| Warrandyte | B | Yes | most residential streets | 100 / 68 | |
| Mount Evelyn | B | Yes | most residential streets | 100 / 99 | |
| Sassafras | B | Yes | most residential streets | 100 / 100 (whole suburb) | |
| Mount Dandenong | B | Yes | most residential streets | 100 / 100 (whole suburb) | |
| Olinda | B | Yes | most residential streets | 100 / 100 (whole suburb) | |
| Emerald | B | Yes | most residential streets | 100 / 100 | |
| Healesville | C | Yes | most residential streets | 100 / 99 | |
| Yarra Glen | C | Partly | none | 19 / 0 | |
| Warburton | C | Yes | most residential streets | 100 / 100 | |
| Macedon | C | Yes | most residential streets | 100 / 100 | |
| Woodend | C | Partly | edges only | 74 / 15 | |
| Gisborne | C | Partly | none | 27 / 0 | |
| Riddells Creek | C | Partly | edges only | 88 / 13 | Yes |
| Kyneton | C | Partly | none | 41 / 0 | |
| Eltham | Plus | Partly | edges only | 53 / 19 | |
| Hurstbridge | Plus | Yes | most residential streets | 100 / 100 | |
| McCrae | Plus | Partly | edges only | 68 / 26 | |
| Mount Martha | Plus | Partly | edges only | 59 / 19 | |
| Arthurs Seat | Plus | Yes | most residential streets | 100 / 100 | |

Summary:
- **Card B:** 9 of 12 have most residential streets under the BMO. The other three are Upper Ferntree Gully, The Basin and Montrose, all near the threshold.
- **Card C:** split. Healesville, Warburton and Macedon have most residential streets under the BMO. Woodend and Riddells Creek have it at the edges only. Yarra Glen, Gisborne and Kyneton have no BMO on residential land.
- **The five extra suburbs:** Hurstbridge and Arthurs Seat are BMO on most residential streets. Eltham, McCrae and Mount Martha are edges only.

Hurstbridge is one of the 13 suburbs that profile answers must never describe or move. This screen is site data, not a profile answer, so it may be listed. It must not be read against R8.4–R8.6 answers.

## Caveats

- The BMO marks land where bushfire hazard is high enough for planning controls. The BPA triggers the building standard (BAL assessment). Neither is a risk rating for a particular house. Both lag the latest planning amendments; zone and overlay data are as served on 31 Oct 2026. Every downloaded zone and BMO feature has `zone_status` = "g" (gazetted); no proposed controls are included.
- The BMO share is an area share, not a count of streets or homes. "Most residential streets" is a proxy.
- Card E suburbs other than McCrae, Mount Martha and Arthurs Seat (Mornington, Dromana, Rosebud, Rye) were not in scope. The same goes for cards A and D apart from Eltham.
- The VicPlan address fallback was not needed and not run.

## Proposed workbook columns (separate approval; display-only, feeds nothing)

SuburbScorecard, appended after the last used column. Check the row-1 headers first.

| Header | Allowed values | Notes |
|---|---|---|
| `Bushfire Prone Area (B3-S, display only)` | Yes / Partly / No / Needs data | Rows for the 25 screened suburbs. All other rows: Needs data |
| `Bushfire Mgmt Overlay (B3-S, display only)` | most residential streets / edges only / none / Needs data | As above |
| `Bushfire basis (B3-S)` | Text: "Estimate: GIS screen 31 Oct 2026, % res. land BPA x / BMO y; thresholds <approved version>" | Source in col Z as well, per the evidence rule |

Rules: no formula may reference these columns (X, Y, L, weights, filters). Add them to the CLAUDE.md "Display-only" list when approved.

## Card wording ("Parts are bushfire-prone (early check, still being confirmed)")

- **Card B: understates.** Most of its suburbs are bushfire-prone and under the BMO across most residential land. Proposed wording: "Most homes here are in bushfire-prone areas with bushfire building and planning rules (early check)."
- **Card C: fits roughly.** Results vary by town. Proposed wording: "Bushfire risk varies: some towns have bushfire planning rules across most streets, others only at the edges (early check)."

**Applied 31 Oct 2026 (user-approved)**, with R8.6 reworded to "Some or most of the kind of area you chose is bushfire-prone". Nish answered R8.4 = E, so his answers are unaffected. Page log: `scoring-model-pointer.md`.

## Use with R8.6

R8.6 is asked only when R8.4 is B or C. Answers will be read against this table at gated step D2. Nish wasn't asked (R8.4 = E, stored X).
