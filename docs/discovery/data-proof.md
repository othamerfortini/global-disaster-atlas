# Phase 0.2 — Data Proof

## Objective

Validate the canonical event model against a deliberately selected sample of real disasters before scaling the ingestion pipeline.

## Sample design

Target: **20 events** in the first proof set.

- 6 earthquakes
- 4 tsunamis
- 4 floods
- 3 cyclones/storms
- 3 volcanic events

Temporal coverage:

- 12 events from 2000–2026
- 5 events from 1900–1999
- 3 events before 1900

The sample should deliberately include:

1. multi-source events;
2. compound events such as earthquake → tsunami;
3. conflicting impact estimates;
4. events with incomplete impact data;
5. historical events with uncertain dates or casualty estimates.

## Data-proof questions

For every event:

- Can we identify the same physical event across sources?
- Can we preserve each source's original identifier?
- Can we normalize date and geographic information without losing precision?
- Can we distinguish reported, estimated and modeled impacts?
- Can we preserve conflicting values rather than silently selecting one?
- Can we trace every critical value to a source?
- Is the applicable source license compatible with our intended use?

## Acceptance criteria

- ≥95% of sample events have a usable date.
- ≥90% have usable geolocation.
- ≥90% have at least one traceable source.
- ≥80% can be resolved to a canonical event without ambiguity.
- ≥70% have at least one human-impact field when such information exists in the inspected sources.
- 100% of critical numeric facts retain provenance.
- 0 fabricated values.

## Important semantic rules

### Unknown is not zero

If a source does not report deaths, `deaths` remains unknown/null. It must never be converted to zero.

### Reported is not modeled

A modeled exposed-population estimate must not be presented as the number of people actually affected.

### Canonical values do not erase source values

The canonical layer may provide a normalized value or range, but the original source observations remain attached to the event.

## Benchmark

EM-DAT is used only as a benchmark during discovery. Its commercial licensing and redistribution restrictions must be respected. It is not assumed to be part of the production data pipeline.

## Next step

Collect the first 20 events and record raw source observations, mappings, entity matches, conflicts, and quality scores. Only after schema validation should the sample be expanded to 100 events.
