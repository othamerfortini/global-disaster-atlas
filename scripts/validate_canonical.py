"""Validate canonical event records against the project schema and invariants.

The validator intentionally checks semantics that JSON Schema alone cannot enforce:
- unknown values are not zero;
- every critical impact value has provenance at event level;
- relationship targets are present in the same dataset when validating a collection;
- event dates use the canonical `time` structure rather than legacy `date`.
"""

from __future__ import annotations

from datetime import datetime
import math

CRITICAL_IMPACTS = ("deaths", "injured", "missing", "affected", "displaced")
ECONOMIC_FIELDS = ("damage", "loss", "combined", "reconstruction_needs")


def _has_numeric_range(value: object) -> bool:
    return isinstance(value, dict) and any(
        value.get(key) is not None for key in ("reported", "min", "max")
    )


def _has_economic_amount(value: object) -> bool:
    return (
        isinstance(value, dict)
        and value.get("status") != "unknown"
        and value.get("amount") is not None
    )


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
            except (AttributeError, ValueError):
                errors.append(f"{eid}: invalid time.start")

        location = event.get("location", {})
        lat, lon = location.get("latitude"), location.get("longitude")
        if lat is not None and not -90 <= lat <= 90:
            errors.append(f"{eid}: latitude out of range")
        if lon is not None and not -180 <= lon <= 180:
            errors.append(f"{eid}: longitude out of range")

        impact = event.get("impact", {})
        for field in CRITICAL_IMPACTS:
            value = impact.get(field)
            if value is None:
                continue
            if isinstance(value, dict) and value.get("status") != "unknown":
                if not event.get("sources"):
                    errors.append(f"{eid}: {field} has a value but no source")
                if not _has_numeric_range(value):
                    errors.append(f"{eid}: {field} status is known but numeric value is absent")

        economic = impact.get("economic", {})
        if isinstance(economic, dict):
            for field in ECONOMIC_FIELDS:
                value = economic.get(field)
                if value is None:
                    continue
                if isinstance(value, dict) and value.get("status") != "unknown":
                    if not event.get("sources"):
                        errors.append(f"{eid}: economic.{field} has a value but no source")
                    amount = value.get("amount")
                    if amount is None:
                        errors.append(
                            f"{eid}: economic.{field} status is known but amount is absent"
                        )
                    elif (
                        isinstance(amount, bool)
                        or not isinstance(amount, (int, float))
                        or (isinstance(amount, float) and not math.isfinite(amount))
                        or amount < 0
                    ):
                        errors.append(
                            f"{eid}: economic.{field} amount must be a finite non-negative number"
                        )

        # Accept the deprecated legacy field during migration, but do not require it.
        legacy_economic = impact.get("economic_loss")
        if legacy_economic is not None and _has_economic_amount(legacy_economic):
            if not event.get("sources"):
                errors.append(f"{eid}: economic_loss has a value but no source")

        for rel in event.get("relationships", []):
            target = rel.get("target_event_id")
            if target not in ids:
                errors.append(f"{eid}: relationship target '{target}' is missing from collection")

    return errors


if __name__ == "__main__":
    print("validate_canonical.py loaded; import validate_events() from the validation pipeline")
