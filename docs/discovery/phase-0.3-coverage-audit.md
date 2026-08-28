# Phase 0.3 — Critical Impact Coverage Audit

## Scope

This audit uses the 20-event canonical proof set currently in the repository. It is **not** a claim of global coverage and must not be extrapolated to the planned 100-event sample.

## Event-level coverage without EM-DAT

A field counts as covered only when a numeric value/range is present in the canonical record. `unknown`, null and an empty status do not count.

| Critical field | Covered events | Coverage |
|---|---:|---:|
| Deaths | 15/20 | 75% |
| Injured | 4/20 | 20% |
| Missing | 4/20 | 20% |
| Affected | 4/20 | 20% |
| Displaced | 3/20 | 15% |
| Economic impact | 0/20 in canonical impact field | 0% |

### Important correction

The earlier 0% economic figure was a **data-model limitation**, not evidence that open/official sources lack economic data. The 2022 Pakistan flood source already cited in the seed set contains a World Bank assessment of US$14.9B damage, US$15.2B economic losses and US$16.3B reconstruction needs. The 2010 Pakistan floods also have official World Bank/ADB damage assessments around US$9.7B–US$10.1B depending on the assessment definition and publication. These values must be represented as separate `damage`, `loss`, and `reconstruction_needs` fields rather than collapsed into one number.

## What the audit proves

1. A substantial share of fatality data can already be reconstructed from open/official sources.
2. Injury, missing, affected and displacement fields are much more heterogeneous.
3. Economic information exists in specialized official assessments but requires semantic normalization: **damage != economic loss != reconstruction need**.
4. The current proof set contains multiple event chains where impact numbers must not be double-counted. Example: the Tohoku earthquake and Japan tsunami refer to the same disaster sequence; they cannot simply be summed as independent casualty totals.
5. The same event may have different casualty definitions and reporting dates. The Atlas must preserve source observations and definitions before producing a canonical aggregate.

## Source capability

USGS provides structured earthquake event data through the FDSN Event Web Service and GeoJSON/CSV/QuakeML feeds. NOAA/NCEI's Global Historical Tsunami Database contains source-event and runup records and, where available, fatalities, injuries, damaged/destroyed houses and damage estimates. GDACS exposes event lists and geospatial event data through its API. These sources demonstrate that an EM-DAT-independent Atlas is technically feasible, but coverage is hazard-specific rather than uniform.

## Required next correction before the 100-event claim

- Normalize all 20 records to the canonical schema.
- Replace all legacy `date`, `lat`, `lon` and scalar impact fields.
- Add explicit source-observation records instead of storing only source URLs.
- Add economic `damage`, `loss` and `reconstruction_needs` separately.
- Add definition metadata for affected/displaced/deaths where sources use different meanings.
- Resolve duplicate/cascade entities before calculating aggregate human impact.
- Run automated schema + semantic validation.
- Then expand to 100 source-enriched events.

## Current conclusion

**We can build the Atlas without making EM-DAT a technical dependency.** We cannot yet state a reliable worldwide percentage of recoverable critical fields. That percentage becomes defensible only after the 100-event source-enriched benchmark is completed using the same rules above.
