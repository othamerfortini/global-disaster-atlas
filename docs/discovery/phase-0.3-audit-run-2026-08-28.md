# Phase 0.3 — Quantitative Audit Run — 2026-08-28

## Scope

This run audits the real-source evidence currently documented in `docs/discovery/phase-0.3-real-audit.md` and the verified observation tranche in `data/audit/verified-observations-tranche-02.json`.

It is **not** the final 100-event benchmark. The repository currently contains an audited tranche, not 100 audited events.

## Event status

- 6 events are classified as verified in the real-source audit document.
- 1 additional event (Pakistan floods 2010) is explicitly pending direct source verification.
- 3 further events (Nepal 2015, Sulawesi 2018, Katrina 2005) are present in draft PR work and are excluded from the main-branch benchmark until merged and independently audited.

## Verified event set

1. GDA-EQ-2010-HTI — Haiti earthquake
2. GDA-EQ-2011-JPN — Tohoku earthquake
3. GDA-TS-2004-IO — Indian Ocean tsunami
4. GDA-TS-2011-JPN — Japan tsunami
5. GDA-TS-1960-CHL — Chile earthquake/tsunami
6. GDA-FL-2022-PAK — Pakistan floods

## Critical-field audit

The audit denominator is an **event-field pair**, not merely events. A field is counted as reconstructed only when a populated value is explicitly supported by an identifiable source and its definition/status can be preserved.

For the six verified events documented in the audit report:

- Deaths: evidence exists for all six event records, but Tohoku/Japan-tsunami and Indian-Ocean tsunami values are linked-chain observations and must not be summed. Haiti has materially conflicting official estimates. Chile is a range. Therefore coverage is not equivalent to a single canonical-number success rate.
- Injured: explicitly verified for Haiti and present in the current canonical Tohoku record; not yet verified for every event.
- Missing: explicitly present in the current canonical Tohoku record; not yet verified across the set.
- Affected: explicitly verified for Pakistan 2022.
- Displaced: explicitly verified/qualified for Haiti and Pakistan 2022; Indian Ocean tsunami has multiple NOAA definitions/figures that remain separate observations.
- Economic damage: explicitly verified for Pakistan 2022.
- Economic loss: explicitly verified for Pakistan 2022.
- Reconstruction needs: explicitly verified for Pakistan 2022.

## Provenance result

All populated values promoted to the verified observation tranche contain source organization, dataset, URL, definition, unit and status. The Pakistan 2022 PDNA values are independently corroborated by the World Bank/PDNA publication and the UNDP-hosted PDNA report. The World Bank states 33 million affected, more than 1,730 deaths, more than 8 million displaced, USD 14.9B damage, USD 15.2B economic loss and USD 16.3B reconstruction needs. The PDNA semantics keep damage, loss and needs separate.

## Conflict result

Known material conflicts are preserved rather than silently resolved:

- Haiti 2010: materially different official casualty estimates.
- Indian Ocean 2004: NOAA records contain different killed/missing and displaced figures depending on record/definition.
- Chile 1960: fatality range 490–5,700 rather than an invented point estimate.
- Tohoku/Japan tsunami: linked event-chain counts must not be double-counted.

Current conflict resolution status: **unresolved but explicitly represented** where the evidence does not justify a single canonical value.

## Audit gate outcome

**PASS for the audited observations.**

**FAIL for final 100-event benchmark completion** because the denominator is not yet 100 events and several critical fields remain unverified.

## Required next tranche

Expand to diverse hazard classes before calculating a headline percentage:

- tropical cyclone
- wildfire
- volcanic eruption
- landslide
- drought
- severe storm/tornado
- extreme temperature
- technological/industrial cascade
- compound flood/storm-surge event
- earthquake-triggered cascade

The benchmark must then freeze its event denominator and calculate coverage, value-level provenance, conflict rate, resolution rate, and cascade integrity separately.
