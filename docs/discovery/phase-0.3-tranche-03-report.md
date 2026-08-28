# Phase 0.3 — Tranche 03 Audit

## Scope

Three additional real events were added from primary/official public sources, deliberately expanding the hazard mix and testing cascades, source conflicts and semantic scope.

## Events

### 1. Nepal/Gorkha earthquake sequence — 2015

USGS reports about 9,000 fatalities, 23,000 injuries, 500,717 houses destroyed and 269,190 damaged. The sequence also included a Mw 7.3 aftershock and earthquake-triggered landslides/avalanches. Values are retained as source-specific observations rather than silently merged with later publications.

Primary source: https://www.usgs.gov/programs/earthquake-hazards/science/m78-nepal-earthquake-2015-a-small-push-mt-everest

### 2. Sulawesi/Palu earthquake sequence — 2018

USGS event impact data report at least 2,077 killed, 4,438 injured, 1,075 missing and 206,524 displaced. The same record describes the combined effects of earthquake, tsunami, liquefaction and landslides, including a 7 m observed tsunami and approximately USD 911 million damage.

Primary source: https://earthquake.usgs.gov/earthquakes/eventpage/us1000h3p4/impact

This is a critical cascade test: the casualty/damage values are for the combined disaster sequence and must not be added independently to separate tsunami/liquefaction/landslide records if those records describe the same affected population.

### 3. Hurricane Katrina — 2005

NOAA/NHC historical material reports approximately 1,200 deaths. An archived NHC summary reports an alternative estimate of approximately 1,500 U.S. deaths. The current NOAA/NCEI damage estimate is USD 125 billion in 2005 dollars, with a 90% confidence interval of USD 97.4–145.5 billion.

Primary sources:
- https://www.nhc.noaa.gov/outreach/history/
- https://www.nhc.noaa.gov/data/tcr/AL122005_Katrina.pdf

## New findings

1. **Cascade scope must be first-class metadata.** A value can describe a primary hazard alone or an entire compound sequence.
2. **Temporal source state matters.** Katrina shows that official estimates can change substantially over time.
3. **Confidence intervals must be preserved for economic estimates.** Replacing USD 125B with a single unqualified number loses material information.
4. **Approximate values must remain approximate.** `about 9,000` is not converted to `9000 exact` semantically; the stored numeric representation is accompanied by `status=estimated` and the source definition.
5. **Infrastructure and housing metrics belong in the critical physical-impact layer**, separate from human impacts and economic aggregates.

## Benchmark status

The tranche is added to the evidence layer. It does not by itself close the 100-event benchmark. Final benchmark metrics remain blocked until all selected events pass the audit gate and the denominator is frozen.
