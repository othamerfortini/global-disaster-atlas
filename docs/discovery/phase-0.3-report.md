# Phase 0.3 — 100 Event Data Proof

## Status

**100-event evaluation set selected. Enrichment and independent verification remain staged; the registry itself must not be confused with a fully verified 100-row impact dataset.**

## Evaluation design

The evaluation set is drawn from a 101-row registry. One duplicate compound representation (`GDA-CMP-2022-TON`) is excluded from the evaluation set because the underlying Hunga Tonga event is already represented by the primary volcanic event and tsunami relationship. The resulting evaluation set contains exactly 100 distinct test records.

Coverage intentionally includes:

- earthquakes;
- tsunamis;
- floods;
- tropical cyclones/storms;
- volcanic eruptions;
- extreme heat;
- wildfires;
- landslides;
- technological/infrastructure failures;
- compound/cascade events.

## What has been demonstrated

### 1. Source availability

USGS exposes a programmatic earthquake catalog with query parameters and GeoJSON/CSV/QuakeML outputs. This is suitable for deterministic earthquake ingestion and geographic normalization.

NOAA/NCEI's Global Historical Tsunami Database covers historical tsunami source events and runups from antiquity to the present, with event-level and runup-level impact fields when available.

GDACS exposes a public API for event discovery, search, statistics and geospatial event data. Its API documentation explicitly supports earthquake, tropical cyclone and flood searches.

### 2. Canonical representation

The schema supports:

- temporal precision;
- point and footprint geometry;
- source identifiers;
- reported/estimated/modeled impacts;
- uncertainty;
- event relationships;
- causal confidence;
- evidence source IDs.

### 3. Event matching

Matching must be evidence-based. Candidate matches should use time proximity, spatial distance, hazard type, magnitude/physical parameters and source identifiers. A name match alone is insufficient.

### 4. Conflicts

Conflicting source observations are retained as source observations. The canonical layer must not silently overwrite disagreement.

### 5. Cascades

The model now handles chains such as:

`earthquake -> tsunami -> flooding -> technological accident`

and infrastructure-driven disasters such as:

`dam failure -> tailings inundation -> environmental/social consequences`.

### 6. Quality score

The existing deterministic quality score measures completeness and provenance rather than severity. It rewards time, location, source count, impact coverage and documented relationships.

## Critical limitation

A 100-event registry is **not** equivalent to 100 fully source-enriched records. The next ingestion pass must populate each record from the approved source adapters and produce a machine-readable observation ledger. Until that happens, no aggregate death/affected totals from this registry should be presented as an Atlas statistic.

This distinction is deliberate: the project will not manufacture completeness merely to satisfy a milestone.

## Preliminary answer to the EM-DAT question

The evidence from the first proof phases is already sufficient to establish that EM-DAT is **not a prerequisite for the Atlas core**.

USGS can provide strong physical-event coverage for earthquakes; NOAA provides unusually deep historical tsunami coverage including runups and impact fields; GDACS provides multi-hazard event discovery, geospatial data and modeled exposure. Additional official/national sources can enrich floods, storms, fires, heat, landslides and technological events.

However, the 100-event proof must be fully enriched before making a defensible percentage for global human-impact coverage. Physical-event coverage and casualty/affected-population coverage are different metrics.

Therefore the correct Phase 0.3 conclusion is:

> **The Atlas can be built without EM-DAT as a core dependency. The remaining question is how much impact-data completeness and harmonization can be achieved from openly accessible sources.**

## Next gate

Complete the source-observation ledger for all 100 evaluation records, run deterministic entity resolution, record conflicts, calculate quality scores, and publish coverage statistics by field and hazard type.
