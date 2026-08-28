# Phase 0.3 — Scale & Validation

## Objective

Move from a hand-selected proof sample to a reproducible 100-event validation set and measure whether the canonical model survives real-world source heterogeneity.

## Scope

Target: **100 events**.

Recommended composition:

- 30 earthquakes
- 20 tsunamis
- 20 floods
- 15 tropical cyclones/storms
- 10 volcanic events
- 5 compound/technological cascade cases

Temporal distribution:

- 60 events: 2000–2026
- 25 events: 1900–1999
- 15 events: before 1900

The final selection must include deliberately difficult cases, including at least:

- earthquake → tsunami;
- natural hazard → technological accident;
- infrastructure failure → inundation;
- events with conflicting casualty estimates;
- historical events with uncertain dates;
- events with large spatial footprints;
- events with multiple source identifiers.

## Pipeline

```text
USGS / NOAA / GDACS / approved DesInventar datasets
                  |
                  v
          source observations
                  |
                  v
             normalization
                  |
                  v
          candidate matching
                  |
                  v
          canonical event graph
             /           \
      provenance       relationships
             \           /
                  v
             quality score
                  |
                  v
             validation report
```

## Entity resolution

A candidate match must consider, at minimum:

- temporal distance;
- geographic distance;
- hazard type/subtype;
- magnitude/severity;
- named location;
- source identifiers;
- known event relationships.

A match must be explainable. The system should retain the matching evidence and confidence rather than returning only a boolean.

## Quality score

The first deterministic score is implemented in `scripts/quality_score.py`. It measures completeness, source provenance and relationship evidence. It is **not** a disaster-severity score.

The score will be recalibrated after the 100-event benchmark.

## Phase gates

### Gate A — ingestion

At least three independent source adapters produce normalized source observations.

### Gate B — matching

≥80% of the 100-event sample resolves to a canonical event without unresolved ambiguity.

### Gate C — provenance

100% of critical numeric facts retain source provenance.

### Gate D — coverage

Measure actual coverage rather than setting a target and treating it as a result. Report coverage separately for date, location, deaths, injured, affected, displaced and economic loss.

### Gate E — licensing

Every redistributed field must have a documented usage basis. DesInventar rights remain dataset/contributor-specific; raw restricted data must not enter the public repository. GDACS attribution/terms must be preserved. USGS/NOAA terms must be checked for the exact dataset used.

## Deliverable

`reports/phase-0.3-results.md` will contain:

- source coverage;
- field coverage;
- entity-resolution accuracy;
- source disagreement rates;
- cascade detection results;
- quality-score distribution;
- licensing exceptions;
- gaps that require additional sources;
- recommendation on whether EM-DAT adds enough incremental value to justify licensing.

## Current status

**Infrastructure ready. Data collection and benchmark validation are the next execution step.**
