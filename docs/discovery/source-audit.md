# Source Audit — Phase 0

## USGS

Primary role: earthquake observations.

Useful fields include event identifiers, origin time, coordinates, depth, magnitude and other event parameters depending on the catalog.

Access: public FDSN API with GeoJSON, CSV, XML/QuakeML and KML output options.

Commercial posture: USGS-produced data are generally public domain/CC0-compatible, subject to third-party material exceptions and dataset-specific notices. Preserve attribution and source URLs.

Decision: **primary source for earthquake event facts**.

## NOAA / NCEI

Primary role: tsunami, earthquake, volcanic and other natural-hazard historical datasets.

The Global Historical Tsunami Database provides event-source and runup-level information and extends into ancient history. Formats and access methods vary by dataset and include APIs/downloadable data.

Commercial posture: NOAA/NCEI data are generally openly accessible, but each dataset and third-party contribution must be checked before redistribution.

Decision: **primary source for tsunami/historical hazard facts**.

## GDACS

Primary role: global event discovery, alerts, exposure and modeled impact.

Access: public APIs and geospatial feeds, including GeoJSON/XML/KML depending on endpoint.

Commercial posture: data are publicly accessible with source attribution requirements; modeled results must be clearly labeled as modeled/estimated and not treated as observed facts.

Decision: **event discovery, exposure/modeling and relationship support**.

## DesInventar

Primary role: local and subnational disaster losses.

Access: downloadable country/region databases and associated data structures.

Commercial posture: the software is open source, but individual contributed databases may remain under the rights of their contributing institutions. Do not assume one universal redistribution license.

Decision: **local-impact enrichment, only where the specific dataset's rights permit intended use**.

## EM-DAT

Primary role: global disaster impact benchmark and harmonized disaster records since 1900.

Access: registration and data-access mechanisms; commercial use requires an applicable paid subscription/license.

Commercial posture: do not assume the commercial license permits redistribution of the raw/living dataset. Confirm current terms directly with EM-DAT before production use.

Decision: **benchmark/reference during discovery; not required for the first MVP**.

## Source hierarchy

1. Prefer primary scientific/official observations for physical event facts.
2. Use local/national sources for local impact where rights permit.
3. Use GDACS modeled values only as modeled values.
4. Use EM-DAT as a benchmark until commercial terms are justified.
5. Preserve provenance and license metadata at the source-record level.
