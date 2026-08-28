# Global Disaster Atlas

Global historical atlas of natural disasters, combining geospatial, temporal, physical-impact, human-impact, provenance, and event-chain data.

## Project status

**Phase 0 — Discovery / Data Proof**

The first objective is to prove that heterogeneous public disaster sources can be normalized into a single auditable canonical event model without inventing precision or violating source licensing.

## Initial sources

- USGS — earthquakes
- NOAA/NCEI — tsunamis, earthquakes, volcanoes and natural-hazard datasets
- GDACS — global disaster events, alerts, exposure and modeled impact
- DesInventar — local disaster losses, subject to dataset-specific rights
- EM-DAT — benchmark/reference source; commercial licensing must be evaluated before production use

## Principles

1. Preserve source provenance for every important fact.
2. Never turn unknown values into zero.
3. Preserve conflicting source values instead of silently overwriting them.
4. Distinguish observed/reported data from modeled estimates.
5. Represent uncertainty explicitly.
6. Treat event relationships (for example earthquake → tsunami) as first-class data.
7. Do not redistribute source data unless its applicable license permits it.
8. Prefer simple architecture until the data model is proven.

## Phase 0.2 target

Build and validate a 20-event sample before scaling to 100 events.

Success criteria include reliable date/geolocation coverage, source traceability, entity matching, impact-field coverage, and zero fabricated values.
