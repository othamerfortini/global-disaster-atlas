#!/usr/bin/env python3
"""Compute coverage, provenance and conflict metrics for evidence records.

The script is intentionally conservative: null is never counted as a reconstructed
value and event-level provenance is not sufficient for value-level provenance.
"""
import json
import sys
from collections import defaultdict

CRITICAL = [
    "deaths", "injured", "missing", "affected", "displaced",
    "economic.damage", "economic.loss", "economic.reconstruction_needs",
]


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(path):
    records = load(path)
    events = sorted({r["event_id"] for r in records})
    by_field = defaultdict(list)
    for r in records:
        by_field[r["field"]].append(r)

    result = {"events": len(events), "fields": {}, "overall": {}}
    reconstructed = 0
    evaluable = 0
    provenance = 0
    conflicts = 0
    resolved = 0

    for field in CRITICAL:
        rows = by_field.get(field, [])
        event_ids = {r["event_id"] for r in rows}
        values = [r for r in rows if r.get("normalized_value") is not None and r.get("raw_value") is not None]
        prov = [r for r in values if r.get("source", {}).get("source_id") and r.get("source", {}).get("url")]
        result["fields"][field] = {
            "events_with_observation": len(event_ids),
            "reconstructed": len(values),
            "provenance_auditable": len(prov),
            "coverage_pct": round(100 * len(values) / len(events), 2) if events else None,
            "provenance_pct": round(100 * len(prov) / len(values), 2) if values else None,
        }
        reconstructed += len(values)
        evaluable += len(event_ids)
        provenance += len(prov)

    conflict_groups = defaultdict(list)
    for r in records:
        if r.get("conflict_id"):
            conflict_groups[r["conflict_id"]].append(r)
    conflicts = len(conflict_groups)
    resolved = sum(1 for rows in conflict_groups.values() if any(r.get("resolution_id") for r in rows))

    result["overall"] = {
        "field_instances_reconstructed": reconstructed,
        "field_instances_with_observation": evaluable,
        "coverage_pct_of_observed_event_fields": round(100 * reconstructed / evaluable, 2) if evaluable else None,
        "value_level_provenance_pct": round(100 * provenance / reconstructed, 2) if reconstructed else None,
        "conflict_groups": conflicts,
        "conflict_groups_resolved_or_explained": resolved,
        "conflict_resolution_pct": round(100 * resolved / conflicts, 2) if conflicts else None,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: audit_critical_fields.py <evidence.json>", file=sys.stderr)
        raise SystemExit(2)
    main(sys.argv[1])
