"""Reproducible audit for critical-impact field coverage.

Coverage means a numeric scalar or a numeric range is present. Unknown/null
values do not count. This measures data availability, not truth, severity,
or completeness of the historical record.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

FIELDS = (
    "deaths",
    "injured",
    "missing",
    "affected",
    "displaced",
)


def numeric_impact_value(value: object) -> bool:
    if not isinstance(value, dict):
        return False
    for key in ("reported", "min", "max"):
        candidate = value.get(key)
        if isinstance(candidate, (int, float)) and not isinstance(candidate, bool):
            return True
    return False


def economic_value(value: object) -> bool:
    if not isinstance(value, dict):
        return False
    return isinstance(value.get("amount"), (int, float)) and not isinstance(value.get("amount"), bool)


def audit(dataset: dict) -> dict:
    events = dataset.get("events", [])
    total = len(events)
    covered = Counter()
    by_class = defaultdict(lambda: {field: 0 for field in FIELDS + ("economic",)})
    source_names = set()
    provenance_ready = 0

    for event in events:
        event_class = event.get("event_class", "unknown")
        impact = event.get("impact", {})
        for source in event.get("sources", []):
            if source.get("name"):
                source_names.add(source["name"])
        if event.get("sources"):
            provenance_ready += 1

        for field in FIELDS:
            if numeric_impact_value(impact.get(field)):
                covered[field] += 1
                by_class[event_class][field] += 1
        if economic_value(impact.get("economic_loss")):
            covered["economic"] += 1
            by_class[event_class]["economic"] += 1

    result = {
        "scope": "current canonical proof set",
        "events": total,
        "source_families_observed": sorted(source_names),
        "source_family_count": len(source_names),
        "events_with_at_least_one_source": provenance_ready,
        "coverage": {
            field: {
                "covered_events": covered[field],
                "total_events": total,
                "percentage": round((covered[field] / total * 100), 2) if total else 0,
            }
            for field in FIELDS + ("economic",)
        },
        "coverage_by_event_class": {
            event_class: {
                field: {
                    "covered_events": count,
                    "total_events_in_class": sum(1 for e in events if e.get("event_class", "unknown") == event_class),
                    "percentage": round((count / sum(1 for e in events if e.get("event_class", "unknown") == event_class) * 100), 2)
                    if sum(1 for e in events if e.get("event_class", "unknown") == event_class) else 0,
                }
                for field, count in fields.items()
            }
            for event_class, fields in sorted(by_class.items())
        },
        "limitations": [
            "This audit measures field presence, not source correctness.",
            "The current proof set is not a representative global sample.",
            "Economic coverage remains zero until economic damage/loss/reconstruction fields are normalized.",
            "Cascade duplicates must be resolved before aggregate casualty totals are calculated.",
        ],
    }
    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", type=Path)
    args = parser.parse_args()
    data = json.loads(args.dataset.read_text(encoding="utf-8"))
    print(json.dumps(audit(data), indent=2, ensure_ascii=False))
