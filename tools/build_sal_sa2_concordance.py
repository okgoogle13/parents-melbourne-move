"""Build a Victorian suburb (SAL 2021) -> SA2 2021 concordance from ABS ASGS Ed.3 allocation files.

Joins SAL_2021_AUST.xlsx and MB_2021_AUST.xlsx on MB_CODE_2021, then keys to the
workbook's SuburbScorecard column AK ("ABS SAL code (2021)"). Read-only on the workbook.

Weights (no population in either file):
  res_mb_share  = share of the suburb's *Residential* mesh blocks in each SA2 (primary;
                  mesh blocks are sized at roughly 30-60 dwellings, so this tracks people)
  area_share    = share of the suburb's total area in each SA2 (secondary)

Usage: .venv/bin/python tools/build_sal_sa2_concordance.py
Writes research/abs/sal_sa2_concordance_vic_2021.csv (all VIC suburb x SA2 pairs) and
research/abs/scorecard_sal_sa2_2021.csv (one row per scorecard suburb).
"""
import csv
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "2021_PEP_SA2_for_VIC_short-header" / "Metadata"
WORKBOOK = ROOT / "Our Next Home — Family Relocation Scoring Model.xlsx"
OUT = ROOT / "research" / "abs"
SINGLE_SA2_THRESHOLD = 0.90  # dominant SA2 holds >= 90% of residential mesh blocks


def rows(path):
    ws = openpyxl.load_workbook(path, read_only=True).worksheets[0]
    it = ws.iter_rows(values_only=True)
    hdr = next(it)
    for r in it:
        yield dict(zip(hdr, r))


def main():
    mb = {}
    for r in rows(META / "MB_2021_AUST.xlsx"):
        if r["STATE_CODE_2021"] == "2":
            mb[r["MB_CODE_2021"]] = (r["SA2_CODE_2021"], r["SA2_NAME_2021"], r["MB_CATEGORY_2021"])

    sal_name = {}
    # (sal, sa2) -> [mb_count, res_mb_count, area]
    pair = defaultdict(lambda: [0, 0, 0.0])
    unmatched = 0
    for r in rows(META / "SAL_2021_AUST.xlsx"):
        if r["STATE_CODE_2021"] != "2":
            continue
        hit = mb.get(r["MB_CODE_2021"])
        if hit is None:
            unmatched += 1
            continue
        sa2, sa2_name, cat = hit
        sal = r["SAL_CODE_2021"]
        sal_name[sal] = r["SAL_NAME_2021"]
        p = pair[(sal, sa2, sa2_name)]
        p[0] += 1
        p[1] += cat == "Residential"
        p[2] += r["AREA_ALBERS_SQKM"] or 0.0

    totals = defaultdict(lambda: [0, 0, 0.0])
    sa2_res = defaultdict(int)
    for (sal, sa2, _), (n, res, area) in pair.items():
        t = totals[sal]
        t[0] += n
        t[1] += res
        t[2] += area
        sa2_res[sa2] += res

    OUT.mkdir(parents=True, exist_ok=True)
    by_sal = defaultdict(list)
    with open(OUT / "sal_sa2_concordance_vic_2021.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["SAL_CODE_2021", "SAL_NAME_2021", "SA2_CODE_2021", "SA2_NAME_2021",
                    "mb_count", "res_mb_count", "area_sqkm", "res_mb_share", "area_share"])
        for (sal, sa2, sa2_name), (n, res, area) in sorted(pair.items()):
            t = totals[sal]
            res_share = res / t[1] if t[1] else None
            area_share = area / t[2] if t[2] else None
            by_sal[sal].append((res_share or 0.0, area_share or 0.0, sa2, sa2_name))
            w.writerow([sal, sal_name[sal], sa2, sa2_name, n, res, round(area, 4),
                        None if res_share is None else round(res_share, 4),
                        None if area_share is None else round(area_share, 4)])

    ws = openpyxl.load_workbook(WORKBOOK, read_only=True)["SuburbScorecard"]
    it = ws.iter_rows(values_only=True)
    hdr = next(it)
    ak = hdr.index("ABS SAL code (2021)")
    with open(OUT / "scorecard_sal_sa2_2021.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["suburb", "SAL_CODE_2021", "SAL_NAME_2021", "n_sa2",
                    "dominant_SA2_CODE_2021", "dominant_SA2_NAME_2021",
                    "dominant_res_mb_share", "dominant_area_share",
                    "suburb_share_of_dominant_sa2", "match_flag", "all_sa2"])
        for r in it:
            if not r[0]:
                continue
            code = str(r[ak]).removeprefix("SAL") if r[ak] else None
            parts = sorted(by_sal.get(code, []), reverse=True)
            if not parts:
                w.writerow([r[0], code, None, 0, None, None, None, None, None,
                            "NO_SAL_MATCH", None])
                continue
            res, area, sa2, sa2_name = parts[0]
            flag = "SINGLE_SA2" if res >= SINGLE_SA2_THRESHOLD else "SPLIT_SA2"
            if totals[code][1] == 0:
                flag = "NO_RESIDENTIAL_MB"
            # how much of the dominant SA2's residential mesh blocks this suburb supplies
            res_in_sa2 = pair[(code, sa2, sa2_name)][1]
            cover = round(res_in_sa2 / sa2_res[sa2], 4) if sa2_res[sa2] else None
            all_sa2 = "; ".join(f"{n} ({s:.0%})" for s, _, _, n in parts)
            w.writerow([r[0], code, sal_name[code], len(parts), sa2, sa2_name,
                        round(res, 4), round(area, 4), cover, flag, all_sa2])

    print(f"VIC mesh blocks: {len(mb)}; SAL rows with no MB match: {unmatched}")
    print(f"VIC suburbs: {len(totals)}; suburb x SA2 pairs: {len(pair)}")


if __name__ == "__main__":
    main()
