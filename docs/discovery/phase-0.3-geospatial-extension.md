# Phase 0.3 — Geospatial Evidence Extension

Date: 2026-08-28
Status: ADDED TO SPECIFICATION

## Purpose

The Atlas must represent not only event coordinates but the spatial footprint of observed, modelled and potentially affected areas.

## Spatial evidence classes

- `origin`: epicentre, source point, volcano vent, storm centre, fire origin, etc.
- `observed_impact_area`: polygon/multipolygon directly supported by evidence.
- `modelled_impact_area`: scientifically/modelled footprint such as shaking, inundation, flood extent or ashfall.
- `potential_impact_area`: exposure or hazard envelope where impact is possible but not individually confirmed.
- `evacuation_area`: documented evacuation/exclusion zone.
- `affected_location`: named locations confirmed as impacted.
- `uncertain_area`: geometry retained with explicit uncertainty rather than presented as confirmed impact.

## Provenance rule

Every geometry must carry its own provenance. A map polygon is not evidence merely because it visually surrounds an event.

Required metadata:

`geometry_id, event_id, geometry_type, geometry_format, source, source_record_id, observed_at, published_at, retrieved_at, spatial_resolution, methodology, confidence, provenance_url`

## Separation of fact and inference

The UI and data layer must distinguish:

1. Confirmed/observed impact.
2. Modelled or inferred impact.
3. Potential exposure.
4. Unknown/insufficient evidence.

These must never be silently merged into one 'affected area'.

## Cascade mapping

Each cascade component can have an independent geometry:

`earthquake -> tsunami -> inundation -> landslide -> infrastructure impact -> evacuation`

The user must be able to toggle components independently and inspect their evidence. Spatial overlap does not imply additive human impact.

## Source capability confirmed during Phase 0.3

GDACS exposes event geometry, polygons, affected locations, AOI, impact analysis, population-density analysis and flood/tsunami/storm-surge related endpoints. Its API also supports event search and archive queries. This makes it a useful source for the geospatial evidence layer and future operational map. citeturn0search0

NOAA/NCEI provides a Natural Hazards Interactive Map and data covering severe storms, flooding, tsunamis, earthquakes, volcanoes, wildfires and other hazards. citeturn0search2

USGS provides hazard datasets and mapping across earthquakes, floods, landslides, volcanoes, wildfires and other hazards, including earthquake maps/catalogues and hazard products. citeturn0search1turn0search4turn0search17

## Query model

The future Atlas map must support filters such as:

- hazard
- date/time
- country/administrative area
- cascade component
- confirmed vs modelled vs potential
- deaths / injured / missing / affected / displaced
- source
- evidence quality
- historical period

## Critical rule

No geometry is fabricated to fill a visual gap. If the historical evidence does not support a polygon, the Atlas may show a point, named locations, a documented boundary, or `unknown spatial extent`.

## Future real-time layer

The same schema can support real-time alerts. GDACS exposes latest/archive event endpoints and geometry/impact products; USGS provides real-time earthquake notifications and feeds. citeturn0search0turn0search17

Real-time status must remain separate from historical canonical evidence until the event is subsequently audited.
