"""Build SAL-level cultural diversity metrics from ABS 2021 Census GCP DataPacks.

Reads ABS 2021 Census General Community Profile (GCP) CSVs for Victoria (SAL and GCCSA:
tables G01, G09A-H, G13A-E) from research/abs/raw/, cross-checks against the canonical
workbook's SuburbScorecard columns AL (population), AO (% born overseas), AQ (% born in India),
and AU (% other language at home), and writes research/abs/sal_diversity_gcp_2021.csv
for all 69 suburbs in SuburbScorecard!AK plus Greater Melbourne (2GMEL).

Usage:
    .venv/bin/python -I tools/build_sal_diversity_gcp.py
"""
import csv
import glob
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "research" / "abs" / "raw"
WORKBOOK = ROOT / "Our Next Home — Family Relocation Scoring Model.xlsx"
OUT_CSV = ROOT / "research" / "abs" / "sal_diversity_gcp_2021.csv"

# Overseas Main English-Speaking Countries (MESC) in ABS 2021 GCP Table G09.
# Note: G09 has no separate Northern Ireland column (only P_England_Tot, P_Scotland_Tot,
# and P_Wales_Tot exist for the UK). Per ABS Table G09 footnote (d), Northern Ireland-born
# persons are aggregated inside P_Elsewhere_Tot ("Born elsewhere") and cannot be subtracted
# separately from G09.
MESC_OVERSEAS_DESIRED = [
    "P_England_Tot",
    "P_Scotland_Tot",
    "P_Wales_Tot",
    "P_N_Ireland_Tot",  # Checked against G09 header; absent in G09 (counted in P_Elsewhere_Tot)
    "P_Ireland_Tot",
    "P_New_Zealand_Tot",
    "P_USA_Tot",
    "P_Canada_Tot",
    "P_South_Africa_Tot",
]

# Record-only non-European breakdowns (never feed P; retained in CSV for research record only).
EURO_COB_COLS = [
    "P_Bosnia_Herzegov_Tot",
    "P_Croatia_Tot",
    "P_France_Tot",
    "P_Germany_Tot",
    "P_Greece_Tot",
    "P_Italy_Tot",
    "P_Malta_Tot",
    "P_Netherlands_Tot",
    "P_North_Macedonia_Tot",
    "P_Poland_Tot",
]

EURO_LANG_COLS = [
    "POL_Croatian_Tot",
    "POL_French_Tot",
    "POL_German_Tot",
    "POL_Greek_Tot",
    "POL_Italian_Tot",
    "POL_Macedon_Tot",
    "POL_Polish_Tot",
    "POL_Portuguese_Tot",
    "POL_Russian_Tot",
    "POL_Serbian_Tot",
    "POL_Spanish_Tot",
]


def load_gcp_raw(raw_dir: Path, geo_suffix: str):
    """Load G01, G09A-H, and G13A-E CSVs for a given geography suffix ('SAL' or 'GCCSA')."""
    data = {}
    g09_headers = []
    patterns = [f"2021Census_G01_VIC_{geo_suffix}.csv",
                f"2021Census_G09*_VIC_{geo_suffix}.csv",
                f"2021Census_G13*_VIC_{geo_suffix}.csv"]
    files = []
    for pat in patterns:
        files.extend(sorted( glob.glob(str(raw_dir / pat)) ))
    if not files:
        raise FileNotFoundError(f"No raw CSV files found for {geo_suffix} in {raw_dir}")

    for fn in files:
        is_g09 = "_G09" in Path(fn).name
        with open(fn, mode="r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            id_col = reader.fieldnames[0]
            if is_g09:
                for col in reader.fieldnames[1:]:
                    if col not in g09_headers:
                        g09_headers.append(col)
            for row in reader:
                code = row[id_col].strip()
                if code not in data:
                    data[code] = {}
                for k, v in row.items():
                    if k == id_col:
                        continue
                    try:
                        data[code][k] = int(v)
                    except ValueError:
                        data[code][k] = v
    return data, g09_headers


def compute_row_metrics(sal_code: str, suburb_name: str, d: dict, mesc_cols: list[str]):
    tot_p = d["Tot_P_P"]  # G01 total persons (identical to G09H P_Tot_Tot and G13E P_Tot_Tot)
    born_os_g01 = d["Birthplace_Elsewhere_P"]  # G01 overseas-born total (used by workbook AO)
    born_au_g01 = d["Birthplace_Australia_P"]
    born_ns_g09 = d["P_COB_NS_Tot"]
    born_os_g09 = d["P_Tot_Tot"] - d["P_Australia_Tot"] - born_ns_g09
    india_born = d["P_India_Tot"]
    lote_tot = d["Lang_used_home_Oth_Lang_P"]  # G01 LOTE total (identical to G13E POL_Tot_Tot)

    mesc_os_count = sum(d[c] for c in mesc_cols)
    euro_cob_count = sum(d[c] for c in EURO_COB_COLS)
    euro_lang_count = sum(d[c] for c in EURO_LANG_COLS)

    # M3_SAL = born overseas (G01 Birthplace_Elsewhere_P, matching workbook AO) minus overseas MESC
    m3_sal_count = born_os_g01 - mesc_os_count
    # Also record M3_SAL using G09 overseas residual (P_Tot_Tot - P_Australia_Tot - P_COB_NS_Tot)
    m3_sal_g09_count = born_os_g09 - mesc_os_count

    au_noneuro_count = lote_tot - euro_lang_count
    m3_noneuro_count = m3_sal_count - euro_cob_count

    return {
        "SAL_CODE_2021": sal_code,
        "suburb": suburb_name,
        "Tot_P": tot_p,
        "born_australia_count": born_au_g01,
        "born_overseas_count": born_os_g01,
        "born_overseas_g09_count": born_os_g09,
        "born_not_stated_count": born_ns_g09,
        "india_born_count": india_born,
        "mesc_overseas_count": mesc_os_count,
        "m3_sal_count": m3_sal_count,
        "m3_sal_g09_count": m3_sal_g09_count,
        "lote_count": lote_tot,
        "euro_lang_count": euro_lang_count,
        "au_noneuro_count": au_noneuro_count,
        "euro_cob_count": euro_cob_count,
        "m3_noneuro_count": m3_noneuro_count,
        "AO": round(born_os_g01 / tot_p, 6),
        "AQ": round(india_born / tot_p, 6),
        "AU": round(lote_tot / tot_p, 6),
        "M3_SAL": round(m3_sal_count / tot_p, 6),
        "M3_SAL_G09": round(m3_sal_g09_count / tot_p, 6),
        "AU_NonEuro": round(au_noneuro_count / tot_p, 6),
        "M3_NonEuro": round(m3_noneuro_count / tot_p, 6),
    }


def main():
    sal_data, g09_sal_headers = load_gcp_raw(RAW_DIR, "SAL")
    gcc_data, _ = load_gcp_raw(RAW_DIR, "GCCSA")

    # Verify MESC columns from actual G09 headers
    g09_p_tot_cols = [c for c in g09_sal_headers if c.startswith("P_") and c.endswith("_Tot")]
    mesc_present = [c for c in MESC_OVERSEAS_DESIRED if c in g09_p_tot_cols]
    mesc_missing = [c for c in MESC_OVERSEAS_DESIRED if c not in g09_p_tot_cols]

    # Read canonical workbook (read-only)
    wb = openpyxl.load_workbook(WORKBOOK, data_only=True, read_only=True)
    ws = wb["SuburbScorecard"]

    wb_rows = []
    for r_idx, row in enumerate(ws.iter_rows(min_row=2, max_row=72, values_only=True), start=2):
        suburb = row[0]   # Col A: Suburb
        sal_code = row[36]  # Col AK: ABS SAL code (2021)
        if not suburb or not sal_code:
            continue
        wb_rows.append({
            "excel_row": r_idx,
            "suburb": str(suburb).strip(),
            "sal_code": str(sal_code).strip(),
            "AL_pop": row[37],  # Col AL: Population (ABS 2021)
            "AO_os": row[40],   # Col AO: % born overseas (of all people)
            "AQ_ind": row[42],  # Col AQ: % born in India
            "AU_lote": row[46], # Col AU: % other language at home
        })
    wb.close()

    # Check 1: Missing SAL codes
    missing_sals = [r for r in wb_rows if r["sal_code"] not in sal_data]
    found_count = len(wb_rows) - len(missing_sals)

    # Compute rows and run Check 2 (reproduce AL, AO, AU, AQ within 0.1 percentage point)
    out_rows = []
    failing_rows = []
    max_diffs = {"AL": 0, "AO_pp": 0.0, "AQ_pp": 0.0, "AU_pp": 0.0}

    for r in wb_rows:
        code = r["sal_code"]
        if code not in sal_data:
            continue
        m = compute_row_metrics(code, r["suburb"], sal_data[code], mesc_present)
        out_rows.append(m)

        diff_al = abs(int(r["AL_pop"]) - m["Tot_P"])
        diff_ao_pp = abs(float(r["AO_os"]) - m["AO"]) * 100.0
        diff_aq_pp = abs(float(r["AQ_ind"]) - m["AQ"]) * 100.0
        diff_au_pp = abs(float(r["AU_lote"]) - m["AU"]) * 100.0

        max_diffs["AL"] = max(max_diffs["AL"], diff_al)
        max_diffs["AO_pp"] = max(max_diffs["AO_pp"], diff_ao_pp)
        max_diffs["AQ_pp"] = max(max_diffs["AQ_pp"], diff_aq_pp)
        max_diffs["AU_pp"] = max(max_diffs["AU_pp"], diff_au_pp)

        if diff_al > 0 or diff_ao_pp > 0.1 or diff_aq_pp > 0.1 or diff_au_pp > 0.1:
            failing_rows.append({
                "excel_row": r["excel_row"],
                "suburb": r["suburb"],
                "sal_code": code,
                "diff_AL": diff_al,
                "diff_AO_pp": diff_ao_pp,
                "diff_AQ_pp": diff_aq_pp,
                "diff_AU_pp": diff_au_pp,
            })

    # Append 2GMEL benchmark row
    gmel_metrics = compute_row_metrics(
        "2GMEL", "Greater Melbourne (GCCSA)", gcc_data["2GMEL"], mesc_present
    )
    out_rows.append(gmel_metrics)

    # Write output CSV
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(out_rows[0].keys())
    with open(OUT_CSV, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    # Print Acceptance Checks 1-4
    print("=== ACCEPTANCE CHECKS ===")
    print(f"Check 1 (Missing SAL codes): {len(missing_sals)} missing ({found_count} of {len(wb_rows)} found) -> {'PASS' if len(missing_sals) == 0 and found_count == 69 else 'FAIL'}")
    if missing_sals:
        for ms in missing_sals:
            print(f"  MISSING: row {ms['excel_row']} {ms['suburb']} ({ms['sal_code']})")

    print(
        f"Check 2 (Reproduce workbook AL, AO, AU, AQ within 0.1 pp across all 69 rows): "
        f"{len(failing_rows)} failing rows -> {'PASS' if len(failing_rows) == 0 else 'FAIL'}"
    )
    print(
        f"  Max absolute differences across 69 rows: "
        f"AL = {max_diffs['AL']} persons, "
        f"AO = {max_diffs['AO_pp']:.4f} pp, "
        f"AU = {max_diffs['AU_pp']:.4f} pp, "
        f"AQ = {max_diffs['AQ_pp']:.4f} pp"
    )
    if failing_rows:
        for fr in failing_rows:
            print(
                f"  FAIL row {fr['excel_row']} {fr['suburb']} ({fr['sal_code']}): "
                f"dAL={fr['diff_AL']}, dAO={fr['diff_AO_pp']:.4f}pp, "
                f"dAU={fr['diff_AU_pp']:.4f}pp, dAQ={fr['diff_AQ_pp']:.4f}pp"
            )

    print("Check 3 (MESC columns subtracted from Born Overseas, read from G09 header):")
    print(f"  Subtracted ({len(mesc_present)} columns): {mesc_present}")
    print(
        f"  Northern Ireland note: {mesc_missing} is absent from G09 headers. "
        "In ABS 2021 GCP Table G09, only England (P_England_Tot), Scotland (P_Scotland_Tot), "
        "and Wales (P_Wales_Tot) have separate UK columns; Northern Ireland-born persons are "
        "aggregated inside P_Elsewhere_Tot ('Born elsewhere', G09H) per ABS G09 footnote (d)."
    )

    print("Check 4 (Greater Melbourne 2GMEL figures):")
    print(
        f"  2GMEL Tot_P  = {gmel_metrics['Tot_P']:,}\n"
        f"  2GMEL AU     = {gmel_metrics['AU']*100:.2f}% ({gmel_metrics['lote_count']:,} / {gmel_metrics['Tot_P']:,})\n"
        f"  2GMEL M3_SAL = {gmel_metrics['M3_SAL']*100:.2f}% ({gmel_metrics['m3_sal_count']:,} / {gmel_metrics['Tot_P']:,})"
    )
    print(f"\nWrote {len(out_rows)} rows (69 SAL suburbs + 2GMEL) to {OUT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

