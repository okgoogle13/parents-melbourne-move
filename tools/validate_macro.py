"""Validate the macro layer: schemas, provenance, PDF quotes, source coverage, snapshot, freshness.

Usage (from repo root):
  .venv/bin/python tools/validate_macro.py                 # validate; exit 1 on any error
  .venv/bin/python tools/validate_macro.py --today 2026-11-04
  .venv/bin/python tools/validate_macro.py --write-snapshot   # create snapshots/<data_current_to>.yaml (never overwrites)
"""
import argparse, datetime as dt, json, re, subprocess, sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
MACRO = ROOT / "research/macro"
SNAPSHOT_KEYS = ["meta", "bottom_line", "indicators", "forecast", "scenarios", "hypothetical_house"]


class StrDateLoader(yaml.SafeLoader):
    """Keep dates as strings so JSON Schema and round-trips see exactly what is written."""


StrDateLoader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load(path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=StrDateLoader)


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def value_objects(node, path="$"):
    if isinstance(node, dict):
        if "provenance" in node:
            yield path, node
        for k, v in node.items():
            yield from value_objects(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from value_objects(v, f"{path}[{i}]")


def number_forms(v):
    a = abs(v)
    forms = {f"{a:g}", f"{a:,}", f"{a:,.0f}"}
    if a >= 1_000_000:
        forms |= {f"{a / 1e6:.2f}m", f"{a / 1e6:g} million"}
    return forms


def numbers_in(value):
    if isinstance(value, bool):
        return []
    if isinstance(value, (int, float)):
        return [value]
    if isinstance(value, dict) and {"low", "high"} <= value.keys():
        return [value["low"], value["high"]]
    return []


def status_for(rule, today):
    d = lambda s: dt.date.fromisoformat(s) if s else None
    if d(rule.get("historical_after")) and today > d(rule["historical_after"]):
        return "historical"
    if d(rule["stale_after"]) and today > d(rule["stale_after"]):
        return "stale"
    if d(rule["review_due_after"]) and today > d(rule["review_due_after"]):
        return "review_due"
    return "current"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--today", default=dt.date.today().isoformat())
    ap.add_argument("--write-snapshot", action="store_true")
    args = ap.parse_args()

    macro = load(MACRO / "macro-market-conditions.yaml")
    sources = load(MACRO / "sources.yaml")
    fresh = load(MACRO / "freshness.yaml")
    errors, info = [], []

    if args.write_snapshot:
        out = MACRO / "snapshots" / f"{macro['meta']['data_current_to']}.yaml"
        if out.exists():
            sys.exit(f"refusing to overwrite {out.relative_to(ROOT)}")
        header = (f"# Frozen snapshot of macro-market-conditions.yaml version {macro['meta']['version']}.\n"
                  "# Never edit. A refresh adds a new snapshot file and bumps meta.version.\n")
        out.write_text(header + yaml.safe_dump({k: macro[k] for k in SNAPSHOT_KEYS}, sort_keys=False,
                                               allow_unicode=True, width=100), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")

    # 1. Schemas
    schemas = {n: json.loads((MACRO / "schema" / f"{n}.schema.json").read_text()) for n in ("macro", "sources", "freshness")}
    for name, doc in (("macro", macro), ("sources", sources), ("freshness", fresh)):
        for e in Draft202012Validator(schemas[name], format_checker=Draft202012Validator.FORMAT_CHECKER).iter_errors(doc):
            errors.append(f"schema {name}: {'/'.join(map(str, e.absolute_path))}: {e.message}")
    vo_validator = Draft202012Validator({**schemas["macro"]["$defs"]["valueObject"], "$defs": schemas["macro"]["$defs"]})

    # 2. Value objects: shape, PDF quotes, numbers inside quotes, source resolution
    pdf_path = ROOT / sources["inputs"][0]["path"]
    pdf_text = norm(subprocess.run(["pdftotext", str(pdf_path), "-"], capture_output=True, text=True, check=True).stdout)
    src = {s["id"]: s for s in sources["sources"]}
    input_ids = {i["id"] for i in sources["inputs"]}
    used, counts = set(), {}
    for path, vo in value_objects(macro):
        for e in vo_validator.iter_errors(vo):
            errors.append(f"value {path}: {e.message}")
        counts[vo.get("provenance")] = counts.get(vo.get("provenance"), 0) + 1
        quote = vo.get("pdf_quote")
        if quote and norm(quote) not in pdf_text:
            errors.append(f"pdf_quote not found in PDF at {path}: {quote!r}")
        if vo.get("provenance") == "pdf" and quote:
            for n in numbers_in(vo.get("value")):
                if n != 0 and not any(f in norm(quote) for f in number_forms(n)):
                    errors.append(f"value {n} not in its pdf_quote at {path}")
        sid = vo.get("source_id")
        if sid is None:
            continue
        if sid in input_ids:
            continue
        if sid not in src:
            errors.append(f"unknown source_id {sid!r} at {path}")
            continue
        used.add(sid)
        s = src[sid]
        if not s["in_pdf"] and vo.get("source_attribution") != "handover":
            errors.append(f"{sid} is not in the PDF but {path} attributes it via {vo.get('source_attribution')!r}")
        if vo.get("source_attribution") == "pdf_source_log_match" and not s["in_pdf"]:
            errors.append(f"{path}: pdf_source_log_match to a source not in the PDF log")
        if s["status"] == "superseded":
            errors.append(f"{path} cites superseded source {sid}")

    # 3. Source coverage
    for s in sources["sources"]:
        if s["id"] not in used:
            info.append(f"unreferenced source: {s['id']} (in_pdf={s['in_pdf']})")
    for i in sources["inputs"]:
        p = ROOT / i["path"]
        if p.exists():
            got = subprocess.run(["shasum", "-a", "256", str(p)], capture_output=True, text=True).stdout.split()[0]
            if got != i["sha256"]:
                errors.append(f"input {i['id']} sha256 mismatch: {got}")
        elif i["committed"]:
            errors.append(f"committed input missing: {i['path']}")
        else:
            info.append(f"local-only input not present here: {i['path']}")

    # 4. Gaps referenced in notes exist
    gap_ids = [g["id"] for g in macro["gaps"]]
    if len(gap_ids) != len(set(gap_ids)):
        errors.append("duplicate gap ids")
    for ref in set(re.findall(r"\bG\d{2}\b", (MACRO / "macro-market-conditions.yaml").read_text())) - set(gap_ids):
        errors.append(f"gap {ref} referenced but not defined")

    # 5. Snapshot matches the live file while the version is unchanged
    snap_path = ROOT / macro["meta"]["snapshot"]
    if not snap_path.exists():
        errors.append(f"snapshot missing: {macro['meta']['snapshot']} (run with --write-snapshot)")
    else:
        snap = load(snap_path)
        if snap["meta"]["version"] == macro["meta"]["version"]:
            for k in SNAPSHOT_KEYS:
                if snap.get(k) != macro[k]:
                    errors.append(f"snapshot differs from live file in '{k}' at the same version")

    # 6. Freshness
    today = dt.date.fromisoformat(args.today)
    for name, rule in fresh["rules"].items():
        info.append(f"freshness {name}: {status_for(rule, today)} (as of {today})")

    print(f"value objects by provenance: {counts}")
    for m in info:
        print("INFO ", m)
    for m in errors:
        print("ERROR", m)
    print(f"{len(errors)} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
