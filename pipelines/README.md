# Ingestion pipelines — Phase 0.3

Adapters are source-specific and must output source observations before canonicalization.

```text
source API/feed
   -> raw observation
   -> normalization
   -> candidate matching
   -> canonical event
   -> provenance + quality score
```

The canonical layer must never overwrite source observations.

## Initial adapters

- `usgs/` — earthquakes
- `gdacs/` — multi-hazard discovery and modeled impact/exposure
- `noaa/` — historical tsunami and hazard data (next adapter)
- `desinventar/` — local loss enrichment, subject to dataset rights (next adapter)

## Safety rules

- No source is treated as permission to redistribute raw data merely because it is publicly reachable.
- Every source observation gets a source identifier and retrieval timestamp.
- Unknown values remain null/unknown.
- Modeled exposure remains modeled.
