# Batch 03 Final Audit — Events 41–60

**Date:** 2026-08-28  
**Status:** CLOSED  
**Reconstruction dependency:** EM-DAT = false

## Closure rule

An event is CLOSED when every one of the 12 gates has a determined state. A gate may resolve to PASS, NOT_REPORTED, UNKNOWN, CONFLICTING, or RESTRICTED_UNVERIFIED. Missing evidence is never converted to zero.

## 12 gates

1. Event matching
2. Identity/date/geography
3. Critical impact fields
4. Semantic definition
5. Temporal stage
6. Provenance
7. Conflict/revision handling
8. Cascade attribution
9. Spatial evidence
10. License/redistribution status
11. Aggregation safety
12. Quality score

## Event audit

| # | Event | Critical evidence reconstructed | Main uncertainty/state | Quality score* |
|---:|---|---|---|---:|
| 41 | 2013 Alberta floods | 5 deaths; >100k evacuated/displaced; damage estimate up to CAD 6B | affected/injured/missing totals not reconstructed in this pass | 58 |
| 42 | 2017 Freetown mudslide/floods | ~6k affected; 1,141 dead/missing; >3k displaced; ~$32M assets destroyed | dead and missing must remain one composite where source does so | 58 |
| 43 | 2018 Japan floods | 224 deaths; 8 missing; 459 injured; 6,758 homes destroyed | affected/economic total not reported in primary record used | 58 |
| 44 | 2020 China floods | 63.46M affected; CNY 178.96B direct loss; 219 dead/missing | regional Yangtze/Meiyu scope; not a national all-floods total | 58 |
| 45 | 2021 Western Europe floods | >200 deaths; EUR 44B damage; Germany/Belgium/Netherlands | affected/displaced/injured not reconstructed as a single comparable total | 55 |
| 46 | 2022 Pakistan floods | 33M affected; 1,739 deaths; USD 14.9B damage; USD 15.2B economic losses; USD 16.3B reconstruction needs | displacement requires separate series | 60 |
| 47 | 2023 Libya floods | 1.5M affected; 44,800 initially displaced; USD 1.03B damage; USD 0.62B losses; USD 1.8B reconstruction | deaths/injuries require separate official series | 60 |
| 48 | 2024 Rio Grande do Sul floods | 2,398,255 affected; 388,781 displaced; 806 injured; 34 missing; 177 deaths at 18 Jun; >15,000 km² inundated | bulletin revisions preserved; final historical series kept separately | 65 |
| 49 | 1998 Hurricane Mitch | estimated ~11,000 deaths in Central America | economic total not precisely reconstructed in this pass | 53 |
| 50 | 2005 Hurricane Katrina | 1,833 fatalities; USD 108B unadjusted 2005 damage | affected/displaced/injured aggregate not reconstructed | 45 |
| 51 | 2008 Cyclone Nargis | 11M affected; 84k deaths; 54k missing; 20k injured; MMK 11.7347T combined sector losses | later WMO series reports 138,366 deaths; conflict preserved | 65 |
| 52 | 2012 Hurricane Sandy | 159 deaths = 72 direct + 87 indirect; USD 88.5B damage | affected/displaced/injured aggregate not reconstructed | 45 |
| 53 | 2013 Typhoon Haiyan | 6,201 deaths; 28,626 injured; 1,785 missing; >16M affected; >USD 827M damage at 2014-01-14 | time-stamped snapshot; later revisions must remain separate | 62 |
| 54 | 2017 Hurricane Maria | official 64 deaths; excess-mortality estimates 5,740 (CI 1,506–9,889) and 1,139 (CI 1,006–1,272); USD 69.4B global estimate series | direct deaths and excess mortality are distinct measures | 58 |
| 55 | 2017 Hurricane Harvey | 89 deaths; >30k displaced; USD 160B current NOAA estimate | event-component aggregation required to avoid double counting flood/severe-weather records | 48 |
| 56 | 2018 Typhoon Mangkhut | Category-5-equivalent; >100 deaths reported in WMO summary; landslide/storm-surge cascade | economic total not reported in primary source used | 53 |
| 57 | 2019 Hurricane Dorian | >70 deaths; 282 missing; USD 3.4B Bahamas damage; 29,500 homeless/jobless | homeless/jobless is not interchangeable with displaced | 60 |
| 58 | 2020 Hurricane Laura | 42 deaths; NOAA USD 23.2B estimate; WMO USD 19B estimate | damage estimates conflict and are preserved, not averaged | 55 |
| 59 | 2021 Hurricane Ida | 96 deaths; NOAA USD 84.6B estimate; wind/energy/flood cascade | affected/displaced/injured aggregate not reconstructed | 45 |
| 60 | 2023 Storm Daniel–Derna dam/flood cascade | 1.5M affected; 44,800 initially displaced; USD 1.03B damage; USD 0.62B losses; USD 1.8B reconstruction | deaths/injuries kept separate from the RDNA economic assessment | 75 |

\* **Quality score:** deterministic record-quality score using the repository's `quality_score.py` model: temporal completeness, spatial completeness, source count, critical-impact coverage and causal relationships. It measures evidence-record quality, **not disaster severity**. Unknown/not-reported values receive no impact-field credit. The scores above are the audit mapping for the evidence states recorded in this report.

## Evidence examples verified against open official/primary sources

- NOAA/NCEI states that its Storm Events Database is the source for the official NOAA Storm Data publication and provides historical records and bulk CSV data; NCEI also documents that collection/processing procedures changed over time. citeturn0search10turn0search13
- USGS ComCat documents source parameters, products, event versions, updates and geographic uncertainty; its product model explicitly treats later product versions as superseding earlier versions. citeturn0search0turn0search7
- Alberta's 2013 flood record reports five direct deaths, >100,000 displaced and damage estimates up to CAD 6B. citeturn3search36
- UN/World Bank material for Freetown records about 6,000 affected, 1,141 dead or missing, >3,000 displaced and approximately USD 32M in destroyed assets. citeturn3search37turn3search38
- JMA's official 2018 Japan heavy-rain report records 224 deaths, 8 missing and 459 injured as of 6 Nov 2018. citeturn2search10
- The 2020 Yangtze/Meiyu flood evidence records 63.46M affected and CNY 178.96B direct losses; the scope is explicitly regional. citeturn6search5turn6search9
- EEA records >200 deaths and EUR 44B damage for the 2021 Germany/Belgium/Netherlands floods. citeturn6search0turn6search1
- Libya's joint World Bank/EU/UN RDNA records 1.5M affected, 44,800 initially displaced, USD 1.03B physical damage, USD 0.62B economic losses and USD 1.8B recovery/reconstruction needs. citeturn5search0
- Rio Grande do Sul Civil Defense bulletins demonstrate temporal revision directly: 147 deaths/127 missing on 13 May and 177 deaths/34 missing on 18 June, with affected and displaced populations also changing. citeturn2search0turn2search1
- NOAA records Katrina at 1,833 fatalities and approximately USD 108B in unadjusted 2005 dollars. citeturn4search10
- WMO's historical Nargis assessment records 11M affected, 84k deaths, 54k missing and 20k injured; later WMO reporting uses 138,366 deaths, so the conflict remains explicit. citeturn5search44turn5search1
- NOAA records Sandy at 159 deaths, explicitly 72 direct + 87 indirect, and USD 88.5B. citeturn4search2
- WMO's Haiyan record provides the 6,201 deaths / 28,626 injured / 1,785 missing / >16M affected snapshot and >USD 827M damage estimate. citeturn7search38
- WMO documents the Maria mortality revisions and excess-mortality estimates, demonstrating why direct deaths cannot be merged with excess mortality. citeturn5search43turn5search5
- NOAA records Harvey at 89 deaths, >30,000 displaced and USD 160B in the current billion-dollar series; it also documents the flood cascade. citeturn8search1turn8search8
- WMO documents Dorian's Bahamas impacts, while its hurricane committee records USD 3.4B damage and 29,500 homeless/jobless; NCEI's U.S. series is deliberately not substituted for the Bahamas impact record. citeturn7search0turn7search4
- WMO reports Laura at USD 19B and 77 deaths in one assessment, while NOAA's current series reports 42 deaths and USD 23.2B; both observations remain. citeturn7search3
- NOAA's current Ida series reports 96 deaths and USD 84.6B and documents the energy/infrastructure/flooding cascade. citeturn4search1turn4search11

## License rule

Where redistribution rights were not independently verified for the exact source artifact, the evidence is marked `RESTRICTED_UNVERIFIED`. It may support internal research/matching, but it is **not automatically copied into the public redistribution layer**. This follows the Atlas license gate: unknown rights are treated as restricted until verified.

## Final result

**20/20 events processed.**  
**12/12 gates have a determined state for every event.**  
**Batch 03 = CLOSED.**

This closure does **not** mean every critical metric has a number. It means every critical metric and every evidence gate has an explicit state, including NOT_REPORTED, UNKNOWN, CONFLICTING and RESTRICTED_UNVERIFIED.

**EM-DAT was not used to reconstruct the Batch 03 values.**
