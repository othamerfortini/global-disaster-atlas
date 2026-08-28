# USGS adapter

Phase 0.3 role: ingest earthquake observations from the USGS FDSN Event Web Service / GeoJSON feeds.

The adapter must preserve the USGS event ID and original source properties before normalization. USGS documents GeoJSON as a programmatic interface and recommends real-time GeoJSON feeds for automated display use. The FDSN API supports custom queries and GeoJSON output. See the source audit for licensing/provenance rules.

Do not commit bulk raw responses to this repository. Raw data should remain in the local/CI ingestion workspace unless redistribution is permitted.
