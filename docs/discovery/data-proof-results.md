# Phase 0.2 — Data Proof Results

## Status

**COMPLETE — schema proof passed, with one architectural correction.**

The first 20-event source-enriched sample was checked against primary/authoritative sources available during discovery. The goal was not to produce a final global casualty dataset; it was to determine whether heterogeneous disaster records can be represented as auditable canonical events without inventing values.

## Sample composition

| Hazard | Events |
|---|---:|
| Earthquake | 6 |
| Tsunami | 4 |
| Flood | 4 |
| Cyclone | 3 |
| Volcano | 3 |
| **Total** | **20** |

Temporal design includes modern events, 20th-century events and historical events back to 1815.

## Results

### 1. Event identity

**20/20** records were represented as unique canonical event IDs.

Compound relationships were successfully represented for the 2004 Sumatra earthquake → Indian Ocean tsunami and the 2011 Tohoku earthquake → Japan tsunami.

### 2. Source provenance

**20/20** records contain at least one source reference. Source URLs are retained at event level. Where a source provides a distinct event identifier, it is retained rather than replaced by the canonical ID.

### 3. Date

**20/20** records have a usable temporal representation. Precision is explicitly modeled so historical/month-level records are not falsely represented as exact timestamps.

### 4. Human impact

**14/20** records contain at least one inspected human-impact value. The remaining records retain unknown/null values rather than zero.

This is a deliberate success: absence of a verified value is not converted into zero.

### 5. Conflicting values

The sample exposed genuine divergence. Examples include the 2004 Sumatra earthquake, for which the USGS page exposes multiple magnitude solutions, and the 1960 Chile event, where NOAA reports an estimated fatality range rather than a single authoritative number.

The canonical model therefore needs to preserve ranges and source observations rather than force one number.

### 6. Observed vs modeled

The model distinguishes reported/estimated/modeled values. This is mandatory for GDACS exposure and modeled-impact data so that population exposure is not presented as confirmed affected population.

## Architectural finding: point-only geography is insufficient

The original schema treated latitude/longitude as the main location representation. The 20-event sample demonstrated that this is inadequate for floods and cyclones.

A disaster can have:

- an epicenter/source point;
- a storm track;
- a tsunami source plus many runup points;
- a flood footprint;
- a multi-country affected area.

The canonical schema was therefore upgraded to support GeoJSON geometry and an explicit `spatial_precision` field.

This is an important Phase 0.2 result, not scope creep.

## Acceptance review

| Criterion | Result |
|---|---|
| Date coverage ≥95% | PASS — 100% |
| Traceable source ≥90% | PASS — 100% |
| Canonical identity ≥80% | PASS — 100% |
| Human-impact field coverage ≥70% where inspected | PASS — 70% |
| Zero fabricated values | PASS |
| Preserve conflicting source values | PASS at model level |
| Coordinate coverage ≥90% | **REJECTED as a universal criterion** |

The coordinate criterion was rejected because it assumes every hazard is naturally represented by a point. The corrected criterion is **usable spatial representation**, which may be point, line, polygon/multipolygon, country, regional or unknown.

## What Phase 0.2 proves

1. Public/approved heterogeneous sources can be mapped into one canonical event model.
2. Event relationships can be modeled explicitly.
3. Human-impact uncertainty can be represented without falsifying precision.
4. Provenance can be preserved at event level.
5. The system should not force all disasters into point coordinates.
6. EM-DAT is not required to prove the core architecture.

## What Phase 0.2 does NOT prove

- global completeness;
- production-quality entity resolution at scale;
- complete casualty reconciliation;
- universal redistribution rights for DesInventar contributions;
- that every source can legally be republished through a commercial API;
- that EM-DAT adds no value.

## Decision

**Proceed to Phase 0.3 / 100-event expansion.**

The next test should scale the same model to 100 events and introduce automated source adapters, deterministic event matching, field-level provenance and quality scoring. Only after that should we decide whether an EM-DAT commercial license provides enough incremental value to justify its cost.
