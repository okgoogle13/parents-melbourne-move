"""B3-S bushfire screening: share of residentially zoned land in each SAL inside the BPA and the BMO.
Method: equal-area point sample on a GRID_M grid (stdlib only; no shapely available offline).
Usage: .venv/bin/python -I screen.py <datadir> <out.csv>"""
GRID_M = 50
import csv, datetime as dt, hashlib, json, sys, time, urllib.parse, urllib.request
from pathlib import Path
import math

SAL = {"Upper Ferntree Gully": "22614", "Upwey": "22620", "The Basin": "22496", "Tecoma": "22476", "Belgrave": "20188",
       "Montrose": "21736", "Warrandyte": "22702", "Mount Evelyn": "21795", "Sassafras": "22239", "Mount Dandenong": "21787",
       "Olinda": "22009", "Emerald": "20868", "Healesville": "21158", "Yarra Glen": "22910", "Warburton": "22689",
       "Macedon": "21562", "Woodend": "22833", "Gisborne": "21001", "Riddells Creek": "22172", "Kyneton": "21414",
       "Eltham": "20865", "Hurstbridge": "21223", "McCrae": "21625", "Mount Martha": "21803", "Arthurs Seat": "20072"}
CARD = {**{s: "B" for s in list(SAL)[:12]}, **{s: "C" for s in list(SAL)[12:20]}, **{s: "Plus" for s in list(SAL)[20:]}}
# Residential zones (Victoria Planning Provisions): GRZ, NRZ, RGZ, LDRZ, MUZ, TZ. RLZ reported separately.
RES = ("GRZ", "NRZ", "RGZ", "LDRZ", "MUZ", "TZ")
WFS = "https://opendata.maps.vic.gov.au/geoserver/wfs"
ABS = "https://geo.abs.gov.au/arcgis/rest/services/ASGS2021/SAL/MapServer/0/query"

data = Path(sys.argv[1]); data.mkdir(exist_ok=True)
log = []


def get(url, name):
    p = data / name
    if not p.exists():
        import subprocess  # curl: Python's resolver fails intermittently in this sandbox
        subprocess.run(["curl", "-sSf", "--retry", "20", "--retry-delay", "5", "--retry-all-errors", "-m", "300", "-o", str(p), url], check=True)
    b = p.read_bytes()
    log.append({"file": name, "url": url, "sha256": hashlib.sha256(b).hexdigest(), "bytes": len(b)})
    return json.loads(b)


def wfs(layer, bbox, name, cql=None):
    q = {"service": "WFS", "version": "2.0.0", "request": "GetFeature", "typeNames": f"open-data-platform:{layer}",
         "outputFormat": "application/json", "srsName": "EPSG:4326"}
    flt = f"BBOX(geom,{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]},'EPSG:4326')"  # lon/lat when the CRS is named in the filter (tested)
    q["cql_filter"] = flt + (f" AND {cql}" if cql else "")
    fc = get(WFS + "?" + urllib.parse.urlencode(q), name)
    if fc.get("numberMatched") != fc.get("numberReturned"):
        sys.exit(f"{name}: WFS paged ({fc.get('numberReturned')} of {fc.get('numberMatched')})")
    return fc


def polys(features):
    """[(bbox, [rings...])] for each polygon part; first ring outer, rest holes."""
    out = []
    for f in features:
        g = f.get("geometry")
        if not g: continue
        parts = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"] if g["type"] == "MultiPolygon" else []
        for rings in parts:
            xs = [p[0] for p in rings[0]]; ys = [p[1] for p in rings[0]]
            out.append(((min(xs), min(ys), max(xs), max(ys)), rings))
    return out


def in_ring(x, y, ring):
    c = False; n = len(ring); j = n - 1
    for i in range(n):
        xi, yi = ring[i][0], ring[i][1]; xj, yj = ring[j][0], ring[j][1]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            c = not c
        j = i
    return c


def inside(x, y, ps):
    for (x0, y0, x1, y1), rings in ps:
        if x0 <= x <= x1 and y0 <= y <= y1 and in_ring(x, y, rings[0]) and not any(in_ring(x, y, h) for h in rings[1:]):
            return True
    return False


rows = []
for sub, code in SAL.items():
    slug = sub.replace(" ", "_")
    q = {"where": f"sal_code_2021='{code}'", "outFields": "sal_code_2021,sal_name_2021", "outSR": "4326", "f": "geojson"}
    sal_fc = get(ABS + "?" + urllib.parse.urlencode(q), f"sal_{slug}.geojson")
    salp = polys(sal_fc["features"])
    lon0 = min(b[0] for b, _ in salp); lat0 = min(b[1] for b, _ in salp); lon1 = max(b[2] for b, _ in salp); lat1 = max(b[3] for b, _ in salp)
    bbox = (lon0, lat0, lon1, lat1)
    zones = wfs("plan_zone", bbox, f"zone_{slug}.json")["features"]
    resp = polys([f for f in zones if str(f["properties"]["zone_code"]).startswith(RES)])
    rlzp = polys([f for f in zones if str(f["properties"]["zone_code"]).startswith("RLZ")])
    bmo_f = wfs("plan_overlay", bbox, f"bmo_{slug}.json", "zone_code LIKE 'BMO%'")["features"]
    bpa_f = wfs("bushfire_prone_area", bbox, f"bpa_{slug}.json")["features"]
    bmop, bpap = polys(bmo_f), polys(bpa_f)
    dy = GRID_M / 111320; dx = GRID_M / (111320 * math.cos(math.radians((lat0 + lat1) / 2)))
    n = dict(sal=0, res=0, rlz=0, res_bpa=0, res_bmo=0, sal_bpa=0, sal_bmo=0)
    y = lat0 + dy / 2
    while y < lat1:
        x = lon0 + dx / 2
        while x < lon1:
            if inside(x, y, salp):
                n["sal"] += 1
                a, b = inside(x, y, bpap), inside(x, y, bmop)
                n["sal_bpa"] += a; n["sal_bmo"] += b
                if inside(x, y, resp):
                    n["res"] += 1; n["res_bpa"] += a; n["res_bmo"] += b
                elif inside(x, y, rlzp):
                    n["rlz"] += 1
            x += dx
        y += dy
    ha = GRID_M * GRID_M / 1e4
    pct = lambda k, base: round(100 * n[k] / n[base], 1) if n[base] else ""
    rows.append({
        "suburb": sub, "card": CARD[sub], "sal_code_2021": code,
        "sal_area_ha": round(n["sal"] * ha), "res_zoned_ha": round(n["res"] * ha), "rlz_ha": round(n["rlz"] * ha),
        "res_sample_points": n["res"],
        "res_share_in_bpa_pct": pct("res_bpa", "res"), "res_share_in_bmo_pct": pct("res_bmo", "res"),
        "sal_share_in_bpa_pct": pct("sal_bpa", "sal"), "sal_share_in_bmo_pct": pct("sal_bmo", "sal"),
        "bmo_schedules": ";".join(sorted({f["properties"]["zone_code"] for f in bmo_f})),
        "bpa_latest_gazettal": max((dt.datetime.strptime(f["properties"]["gazettal_date"], "%d/%m/%Y").date().isoformat() for f in bpa_f if f["properties"].get("gazettal_date")), default=""),
        "zone_codes_res": ";".join(sorted({f["properties"]["zone_code"] for f in zones if str(f["properties"]["zone_code"]).startswith(RES)})),
    })
    print(rows[-1], flush=True)

with open(sys.argv[2], "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
json.dump(log, open(Path(sys.argv[2]).with_suffix(".sources.json"), "w"), indent=1)
