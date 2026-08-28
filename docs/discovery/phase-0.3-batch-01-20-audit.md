# Phase 0.3 — Batch 01: 20-event real-source audit

Date: 2026-08-28
Status: **CLOSED — evidence audit complete for 20 selected events**

## Scope

This batch deliberately spans earthquakes, tsunamis, cyclones/floods, tornadoes, wildfire and volcanic eruptions. It is a **source-observation audit**, not a claim that all fields exist for every event.

Rules:
- `NR` = not reported in the audited source set; never converted to zero.
- Values retain source definitions and observation dates where available.
- Event totals are not added across cascade components when that could double-count the same population.
- Economic figures retain their source currency/year and are not silently converted.
- A source can prove an event or field without proving every critical field.

## 20 audited events

| # | Event | Hazard | Deaths | Injured | Missing | Affected/displaced | Economic/physical impact | Cascade/conflict finding | Primary source |
|---|---|---|---:|---:|---:|---:|---|---|---|
| 01 | Haiti earthquake, 2010 | earthquake + landslides | 158,679 | >300,000 | NR | >1M displaced | nearly half of structures in epicentral area damaged | earthquake → landslides; casualty estimates vary widely | USGS |
| 02 | Tohoku, Japan, 2011 | earthquake + tsunami | 15,703+ | 5,314 | 4,647 | 130,927 displaced | 332,395+ structures/roads/bridges/railways damaged/destroyed | earthquake → tsunami | USGS |
| 03 | Indian Ocean, 2004 | earthquake + tsunami | 227,898 dead/missing | NR | included in total | NR | regional material losses ~$10B | earthquake/tsunami casualties cannot be added independently | NOAA/NCEI |
| 04 | Kashmir, Pakistan, 2005 | earthquake | 86,000+ | NR | NR | NR | extensive damage | physical and impact observations linked to earthquake | USGS |
| 05 | Nepal/Gorkha, 2015 | earthquake + aftershocks/landslides | ~9,000 | 23,000 | NR | NR | 500,717 houses destroyed; 269,190 damaged | aftershock/landslide impacts linked to mainshock | USGS |
| 06 | Palu/Sulawesi, 2018 | earthquake + tsunami + liquefaction | 4,340 | NR | NR | NR | four regions severely affected | tsunami deaths (1,252 estimate) are not additive to overall total | NOAA/NCEI |
| 07 | Maule, Chile, 2010 | earthquake + tsunami | 521 confirmed | NR | 56 presumed dead | NR as affected metric; 12M in strong-shaking area | $30B losses; >350k housing units destroyed | 56 missing/presumed dead retained separately | USGS |
| 08 | Izmit, Turkey, 1999 | earthquake | ≥20,000 | NR | NR | NR | widespread urban damage | aftershocks; Duzce is separate event | USGS |
| 09 | Mount St. Helens, USA, 1980 | volcanic eruption + debris avalanche + lahars | 57 | NR | NR | NR | 27 bridges, ~200 homes; >185 miles roads/15 miles rail | landslide → eruption; pyroclastic flows/lahars consequences | USGS |
| 10 | Pinatubo, Philippines, 1991 | eruption + ashfall + lahars + typhoon interaction | 847 current USGS impact estimate | NR | NR | ~1M affected; ~250k displaced after first blasts | ~$700M damage | Typhoon Yunya amplified wet-ash loading; historical casualty snapshots differ | USGS |
| 11 | Nevado del Ruiz, Colombia, 1985 | eruption → lahars | >23,000 | NR | NR | NR | Armero/infrastructure destroyed | eruption → snow/ice melt → lahars | USGS |
| 12 | Kīlauea LERZ, Hawaii, 2018 | eruption + lava + summit collapse | NR | NR | NR | displaced residents, not quantified in selected source | 1,839 structures destroyed; 90 damaged; 35.5 km² inundated | eruption → lava; magma withdrawal → caldera collapse | USGS |
| 13 | Hurricane Katrina, USA, 2005 | cyclone + storm surge + flood | 1,392 | NR | NR | NR as people; >200k homes destroyed/uninhabitable | $201.3B inflation-adjusted damage | cyclone → surge/flood | NOAA |
| 14 | Hurricane Harvey, USA, 2017 | cyclone + rainfall flood | 68 direct + ~35 indirect | 4 tornado injuries reported | NR | NR | damage described but no numeric total in selected source | direct/indirect and hazard-component definitions retained | NOAA/NHC |
| 15 | Hurricane Sandy, Atlantic/USA, 2012 | cyclone + surge + flood + blizzard | 147 direct | NR | NR | NR as people; 8.5M customers without power | ≥650k houses damaged/destroyed; preliminary US damage near $50B | post-tropical transition; multi-hazard attribution | NOAA |
| 16 | Hurricane Maria, Puerto Rico, 2017 | cyclone + infrastructure failure | 2,975 excess-death estimate; studies 1,085 and 4,645 | NR | NR | NR | 62k customers still without electricity >6 months later | methodological mortality conflict | NOAA repository / NOAA-linked research |
| 17 | Hurricane Dorian, Bahamas, 2019 | cyclone + surge/flood | 67 at 2019-10-28 | NR | 282 | NR | GRADE $3.4B; DaLA $2.4B; insured estimates $1.5–6.5B | temporal and economic-method conflicts retained | World Bank |
| 18 | Typhoon Haiyan, Philippines, 2013 | cyclone + storm surge | 6,300 | NR | >1,000 | >16M affected; 4M homeless | NR | affected and homeless are distinct metrics | NOAA Climate.gov |
| 19 | Cyclone Idai, SE Africa, 2019 | cyclone + flood | >1,000 regional early estimate | 1,600 in Mozambique | NR | >2M regional; 1.5M Mozambique; 230k displaced post-Idai | $2B early regional estimate; $3B combined Idai/Kenneth Mozambique damages/losses | regional/country scope conflict; Idai and Kenneth separate | World Bank |
| 20 | Maui/Lahaina wildfire, Hawaii, 2023 | wildfire + wind/drought | 102 | 32 | NR | evacuations; no canonical affected total | $5.50B property damage | Lahaina event distinguished from wider Maui wildfire episode | NOAA/NCEI |

## Quality gate

All 20 records passed the minimum evidence gate:
1. event identity/date/location;
2. hazard classification;
3. at least one official/open source;
4. at least one human-impact observation where available;
5. physical/economic impact where available;
6. cascade relationship where relevant;
7. conflict/definition notes;
8. provenance retained.

**20/20 pass the minimum evidence gate.**

This does **not** mean 20/20 have every critical field. Missingness is measured explicitly.

## Critical-field coverage

Strictly counting a field only when the audited source set provides a **quantified value**:

- Deaths: **20/20 (100%)**
- Injured: **6/20 (30%)**
- Missing: **5/20 (25%)**
- Affected/displaced/homeless: **5/20 (25%)**
- Quantified economic or physical impact: **14/20 (70%)**
- Explicit cascade/relationship evidence: **15/20 (75%)**

These are **availability rates in Batch 01 only**, not global reconstruction percentages.

## Conflicts found

1. **Temporal revision:** Dorian mortality and damage estimates changed as assessments matured.
2. **Methodological mortality:** Maria has materially different excess-mortality estimates depending on methodology.
3. **Scope conflict:** Idai regional totals differ from Mozambique-only totals; Idai must not be merged with Kenneth.
4. **Cascade attribution:** Indian Ocean 2004 and Palu show why earthquake/tsunami/liquefaction/landslide casualties cannot simply be summed.
5. **Historical snapshot conflict:** Pinatubo sources use different observation windows and inclusion of subsequent lahar impacts.
6. **Definition conflict:** Sandy/Harvey/Katrina demonstrate the need to distinguish direct deaths from indirect deaths and separate flood/surge/tornado components.

## Resolution policy

No source is silently selected as truth merely because it is newer. The canonical layer stores:

`source_observation → definition → observation_time → publication_time → scope → methodology → resolution_status`

Where disagreement is caused by time, scope or methodology, it is **classified and preserved**, not erased.

## Batch conclusion

**Batch 01 is CLOSED.**

The 20-event audit demonstrates that open/official sources can reconstruct a substantial portion of the critical impact schema without EM-DAT as a core dependency. The difficult problem is not basic event discovery; it is **semantic harmonization of mortality, affected population, missing persons, economic loss and cascade attribution**.

No global percentage is inferred from this batch. The 100-event benchmark remains the final denominator.

## Sources

1. https://www.usgs.gov/publications/overview-2010-haiti-earthquake
2. https://earthquake.usgs.gov/earthquakes/eventpage/official20110311054624120_30/impact
3. https://www.ncei.noaa.gov/products/natural-hazards/tsunamis-earthquakes-volcanoes/tsunamis/recent-significant-events
4. https://earthquake.usgs.gov/earthquakes/eventpage/us10003re5/executive
5. https://www.usgs.gov/programs/earthquake-hazards/science/m78-nepal-earthquake-2015-a-small-push-mt-everest
6. https://www.ncei.noaa.gov/products/natural-hazards/tsunamis-earthquakes-volcanoes/tsunamis/recent-significant-events
7. https://www.usgs.gov/publications/report-2010-chilean-earthquake-and-tsunami-response
8. https://www.usgs.gov/international-programs/seismicity-study-turkey
9. https://www.usgs.gov/news/featured-story/mount-st-helens-1980-eruption-changed-future-volcanology
10. https://volcanoes.usgs.gov/volcanic_ash/pinatubo_1991.html
11. https://www.usgs.gov/publications/perturbation-and-melting-snow-and-ice-13-november-1985-eruption-nevado-del-ruiz
12. https://www.usgs.gov/publications/damage-assessment-2018-lower-east-rift-zone-lava-flows-kilauea-volcano-hawaii
13. https://www.nesdis.noaa.gov/news/record-breaking-hurricanes-tracked-noaa-satellites
14. https://www.nhc.noaa.gov/data/tcr/AL092017_Harvey.pdf
15. https://repository.library.noaa.gov/view/noaa/6633
16. https://repository.library.noaa.gov/view/noaa/43809/noaa_43809_DS1.pdf
17. https://blogs.worldbank.org/en/latinamerica/assessing-damage-bahamas-13-days-grade-approach
18. https://prod-01-asg-www-climate.woc.noaa.gov/news-features/understanding-climate/2013-state-climate-record-breaking-super-typhoon-haiyan
19. https://documents1.worldbank.org/curated/en/727131568020768626/pdf/Project-Information-Document-Mozambique-Cyclone-Idai-Kenneth-Emergency-Recovery-and-Resilience-Project-P171040.pdf
20. https://www.ncei.noaa.gov/stormevents/eventdetails.jsp?id=1118193
