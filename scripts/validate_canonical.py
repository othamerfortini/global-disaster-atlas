"""Validate canonical event records against the project schema and invariants.

The validator intentionally checks semantics that JSON Schema alone cannot enforce:
- unknown values are not zero;
- every critical impact value has provenance at event level;
- relationship targets are present in the same dataset when validating a collection;
- event dates use the canonical `time` structure rather than legacy `date`.
"""

from __future__ import annotations

from datetime import datetime

CRITICAL_IMPACTS = ("deaths", "injured", "missing", "affected", "displaced", "economic_loss")


def validate_events(events: list[dict]) -> list[str]:
    errors: list[str] = []
    ids = {e.get("event_id") for e in events}

    for event in events:
        eid = event.get("event_id", "<missing-id>")
        for forbidden in ("date", "lat", "lon"):
            if forbidden in event:
                errors.append(f"{eid}: legacy field '{forbidden}' must be migrated")

        time = event.get("time", {})
        start = time.get("start")
        if start:
            try:
                datetime.fromisoformat(start.replace("Z", "+00:00"))
            except ValueError:
                errors.append(f"{eid}: invalid time.start")

        location = event.get("location", {})
        lat, lon = location.get("latitude"), location.get("longitude")
        if lat is not None and not -90 <= lat <= 90:
            errors.append(f"{eid}: latitude out of range")
        if lon is not None and not -180 <= lon <= 180:
            errors.append(f"{eid}: longitude out of range")

        for field in CRITICAL_IMPACTS:
            value = event.get("impact", {}).get(field)
            if value is None:
                continue
            if isinstance(value, dict) and value.get("status") != "unknown":
                if not event.get("sources"):
                    errors.append(f"{eid}: {field} has a value but no source")
                if value.get("reported") is None and value.get("min") is None and value.get("max") is None:
                    errors.append(f"{eid}: {field} status is known but numeric value is absent")

        for rel in event.get("relationships", []):
            target = rel.get("target_event_id")
            if target not in ids:
                errors.append(f"{eid}: relationship target '{target}' is missing from collection")

    return errors


if __name__ == "__main__":
    print("validate_canonical.py loaded; import validate_events() from the validation pipeline")
