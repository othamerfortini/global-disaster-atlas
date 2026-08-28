"""Deterministic quality/completeness score for canonical disaster events.

This score measures record quality, not disaster severity. It rewards temporal,
spatial and provenance completeness and gives partial credit for each critical
impact field. Unknown values receive no credit.
"""

CRITICAL_IMPACTS = ("deaths", "injured", "missing", "affected", "displaced", "economic_loss")


def _known_impact(value: dict | None, field: str) -> bool:
    if not isinstance(value, dict) or value.get("status") == "unknown":
        return False
    if field == "economic_loss":
        return value.get("amount") is not None
    return any(value.get(k) is not None for k in ("reported", "min", "max"))


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

    known_impacts = sum(_known_impact(event.get("impact", {}).get(k), k) for k in CRITICAL_IMPACTS)
    score += round(15 * known_impacts / len(CRITICAL_IMPACTS))

    relationships = event.get("relationships", [])
    if relationships:
        score += 10
        if all(r.get("evidence_source_ids") for r in relationships):
            score += 5

    return min(score, 100)


if __name__ == "__main__":
    print("quality_score.py loaded; import quality_score() from the ingestion pipeline")
