# Batch 03 — Events 41–60 Source Audit

**Status:** OPEN — evidence enrichment in progress
**Scope:** events 41–60 from `data/sample/events-100-registry.json`
**Policy:** no event is AUDITED/CLOSED until all 12 gates pass.
**EM-DAT:** excluded from reconstruction.

## Event set

41. GDA-FL-2013-CAN — 2013 Alberta floods
42. GDA-FL-2017-SLE — 2017 Sierra Leone mudslide and floods
43. GDA-FL-2018-JPN — 2018 Japan floods
44. GDA-FL-2020-CHN — 2020 China floods
45. GDA-FL-2021-EUR — 2021 Western Europe floods
46. GDA-FL-2022-PAK — 2022 Pakistan floods
47. GDA-FL-2023-LBY — 2023 Libya floods
48. GDA-FL-2024-BRA — 2024 Rio Grande do Sul floods
49. GDA-CY-1998-HND — 1998 Hurricane Mitch
50. GDA-CY-2005-USA — 2005 Hurricane Katrina
51. GDA-CY-2008-BGD — 2008 Cyclone Nargis
52. GDA-CY-2012-USA — 2012 Hurricane Sandy
53. GDA-CY-2013-PHL — 2013 Typhoon Haiyan
54. GDA-CY-2017-CAR — 2017 Hurricane Maria
55. GDA-CY-2017-USA — 2017 Hurricane Harvey
56. GDA-CY-2018-PHL — 2018 Typhoon Mangkhut
57. GDA-CY-2019-BAH — 2019 Hurricane Dorian
58. GDA-CY-2020-USA — 2020 Hurricane Laura
59. GDA-CY-2021-USA — 2021 Hurricane Ida
60. GDA-CY-2023-LBY — 2023 Storm Daniel

## Verified evidence captured in this audit pass

### 43 — 2018 Japan floods
Official/statistical evidence confirms municipality-level fatalities, injuries and economic-loss variables are reconstructable from prefectural technical disaster reports and Cabinet Office statistics. The national event requires aggregation across affected prefectures; therefore the canonical national totals remain OPEN until the underlying official records are collected and deduplicated.

### 44 — 2020 China floods
A source citing Ministry of Emergency Management data reports that by 13 August 2020 the floods had affected 63.46 million people, caused direct economic losses of CNY 178.96 billion, and left 219 people dead or missing; by end-June 744,000 people had been displaced. These are stage-specific observations and must not be collapsed into one final value without checking the publication date and definitions.

### 46 — 2022 Pakistan floods
World Bank/PDNA evidence: 33 million affected; 1,739 fatalities reported in the assessment; 8 million displaced; >US$14.9B damage; ~US$15.2B economic losses; ~US$16.3B recovery/reconstruction needs. A later World Bank publication describes the same 33M/8M figures and distinguishes damage from economic losses. These are separate metrics and must not be summed. Official/partner assessment provenance is strong; final license/redistribution status still requires a source-by-source rights check.

### 47 — 2023 Libya floods
World Bank/UN/EU produced a Rapid Damage and Needs Assessment. A UN-reported figure cited in later reporting gives at least 5,923 deaths and >40,000 internally displaced; the joint assessment reports US$1.65B in damage and losses. Because the event had an evolving death toll and conflicting/missing-person counts, the canonical value must preserve temporal stage and uncertainty.

### 48 — 2024 Rio Grande do Sul floods
State Civil Defense records provide dated snapshots. On 13 May 2024: 2,115,703 affected, 538,241 displaced, 806 injured, 127 missing, 147 confirmed deaths, 447 municipalities affected. On 28 May: 2,345,400 affected, 581,638 displaced, 806 injured, 50 missing, 169 confirmed deaths. Later state reporting/technical literature records further revisions. These observations demonstrate temporal revision and must be stored as separate observations, not overwritten.

### 50 — 2005 Hurricane Katrina
NOAA/NCEI currently reports 1,833 fatalities and approximately US$108B damage in unadjusted 2005 dollars. The NCEI Billion-Dollar Disaster dataset reports US$201.3B in 2025-dollar normalized damage. These are not conflicting values: they represent different monetary bases and must be stored with currency/year/normalization metadata.

### 52 — 2012 Hurricane Sandy
NOAA/NCEI reports 159 deaths, decomposed into 72 direct and 87 indirect, and US$88.5B damage. This is a high-quality cascade/attribution example and should retain the direct/indirect decomposition.

### 55 — 2017 Hurricane Harvey
NOAA Storm Events contains official NWS records at event/county level, including direct/indirect deaths, injuries, property and crop damage, coordinates, event narratives and episode relationships. The national canonical total requires aggregation across component records and explicit duplicate/cascade controls; it must not be inferred from a single county record.

### 58 — 2020 Hurricane Laura
NOAA/NCEI Billion-Dollar Disaster data report 42 deaths and US$23.2B in damage (with normalized estimate shown separately). NOAA Storm Events contains component records describing Category 4 landfall, storm surge, wind, rainfall and flooding. National aggregation remains OPEN pending reconciliation of component records.

## Structural findings

- NOAA Storm Events explicitly provides bulk CSV downloads and field documentation.
- NOAA notes that collection/processing methods changed substantially over time; this must be captured in source methodology metadata.
- NOAA records may separate a single tropical cyclone into hurricane, flood, tornado, storm surge and other component events; matching and cascade rules are therefore mandatory.
- USGS ComCat is the primary earthquake source, but it is not sufficient by itself for all human-impact metrics in flood/cyclone events.
- GDACS is a useful independent event/geospatial corroboration source but is not a substitute for primary national impact records.

## Current gate status

No event in 41–60 is declared AUDITED/CLOSED by this file. The following gates still require explicit per-event evidence records before closure: source-level provenance, license/redistribution determination, complete critical-field coverage, spatial evidence, conflict resolution, cascade graph, aggregation safety and quality score.

## Closure rule

`BATCH_03 = CLOSED` only when:

`20/20 events × 12/12 gates = PASS`

No partial closure is permitted.
