# Phase 0.3 — Audited Tranche 01

**Audit date:** 2026-08-28  
**Events:** 8  
**Sources:** USGS, NOAA/NCEI, World Bank/PDNA  
**Status:** audited tranche; not yet the 100-event final benchmark

## Method

Only values directly traceable to an official/primary source were counted as reconstructed. Unknown values were not treated as zero. `affected_exposed` is not counted as `affected`. Ranges remain ranges. Economic `damage`, `loss` and `reconstruction_needs` remain separate measures.

## Coverage of critical fields

| Field | Events with usable value | Coverage |
|---|---:|---:|
| deaths | 8/8 | 100.0% |
| injured | 4/8 | 50.0% |
| missing | 3/8 | 37.5% |
| affected | 2/8 | 25.0% |
| displaced | 3/8 | 37.5% |
| economic impact (damage/loss) | 4/8 | 50.0% |

These percentages describe this tranche only and must not be extrapolated to the global dataset.

## Provenance

All counted observations in `data/audit/phase-0.3-tranche-01-observations.json` contain source name, source URL, field, value/range, unit, status and a definition. **Value-level provenance for counted observations: 100%.**

This does not mean every event field has a value; it means every value we counted has an auditable source trail.

## Conflicts

The tranche contains semantic uncertainty and ranges, but no multi-source numeric conflict set has yet been formally resolved under the new `SourceObservation` model. Therefore **conflict-resolution percentage is intentionally reported as N/A**, not 100%.

Important examples:

- 1960 Chile: NOAA reports a 490–5,700 fatality range rather than a single point estimate.
- 2004 Indian Ocean: NOAA describes deaths/missing as a combined measure associated with the earthquake and subsequent tsunami.
- 2010 Chile: 12 million people were in areas that felt strong shaking; this is exposure, not the same as `affected`.
- 2022 Pakistan: damage, economic loss and reconstruction needs are distinct metrics.

## Audit conclusion

The tranche demonstrates that an open/official-source architecture can reconstruct substantial human and economic impact information without EM-DAT. However, coverage is highly field- and hazard-dependent. Deaths are much easier to reconstruct than injured, missing, affected or displaced populations.

The next tranche must deliberately include more floods, cyclones, wildfires, volcanoes, landslides and technological/compound disasters to avoid bias toward earthquake/tsunami records.

## Source capability evidence

USGS provides a programmatic earthquake catalog and GeoJSON feeds. NOAA/NCEI maintains global historical tsunami data containing event characteristics and impact information, including casualties and monetary damage. The World Bank provides disaster assessments containing human impacts and separate damage/loss/reconstruction metrics. GDACS provides global multi-hazard event feeds and impact/exposure products, but modeled values must remain labeled as modeled.
