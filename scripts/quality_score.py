"""Deterministic first-pass quality score for canonical disaster events.

This is intentionally conservative. It scores data completeness/provenance,
not the severity or scientific importance of an event.
"""


def quality_score(event: dict) -> int:
    score = 0

    time = event.get("time", {})
    location = event.get("location", {})
    sources = event.get("sources", [])

    if time.get("start"):
        score += 10
    if time.get("precision") not in (None, "unknown"):
        score += 10

    if location.get("latitude") is not None and location.get("longitude") is not None:
        score += 15
    if location.get("spatial_precision") not in (None, "unknown"):
        score += 5

    if sources:
        score += 15
    if len(sources) >= 2:
        score += 10

    impact = event.get("impact", {})
    if any(impact.get(k) for k in ("deaths", "injured", "missing", "affected", "displaced")):
        score += 15

    relationships = event.get("relationships", [])
    if relationships:
        score += 10
        if all(r.get("evidence_source_ids") for r in relationships):
            score += 5

    return min(score, 100)


if __name__ == "__main__":
    print("quality_score.py loaded; import quality_score() from the ingestion pipeline")
