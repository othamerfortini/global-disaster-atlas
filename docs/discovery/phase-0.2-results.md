# Phase 0.2 — Initial Data Proof Results

## Status

**Seed dataset created: 20 canonical event candidates.**

This is not yet the final verified impact dataset. The current purpose is to validate the schema, provenance structure and event relationships before automated ingestion.

## Initial findings

### 1. Physical event facts are comparatively strong

USGS provides structured earthquake records with origin time, coordinates, depth and magnitude. A single USGS event may also expose multiple origin/magnitude solutions, demonstrating why source-level observations must be preserved.

### 2. Compound events must be first-class

Tohoku and the 2004 Sumatra event demonstrate the need to represent an earthquake and its resulting tsunami as related but distinct hazard events.

### 3. Exposure is not impact

GDACS may expose population within a modeled radius or other modeled/exposure values. These must never be converted directly into `affected` or `deaths`.

### 4. Historical precision varies

Historical volcanic and tsunami records may have month/day/year uncertainty. The schema therefore carries explicit date precision.

### 5. Human-impact values require a second verification pass

The initial 20-event file deliberately leaves deaths/injuries/affected values unknown until they are verified against source records. This prevents accidental fabrication and lets the next pass measure actual field coverage.

## Current blockers

- Complete source-by-source impact extraction.
- Exact GDACS event IDs for all selected events.
- NOAA event/runup IDs for tsunami records.
- DesInventar local records and dataset-specific licensing review.
- Independent benchmark comparison against EM-DAT.

## Next action

Run a **verified enrichment pass** over these 20 events, collecting source-level impact values and identifiers. Then calculate coverage, source agreement, entity-match confidence and provenance completeness.
