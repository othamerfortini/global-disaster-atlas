# Phase 0.3 — Batch Audit Plan: 20 Events

Date: 2026-08-28

## Objective

Execute the Phase 0.3 evidence audit in batches of 20 events rather than one event at a time. Each batch must be fully source-enriched, matched, conflict-checked, cascade-checked, and quality-scored before being counted toward the 100-event benchmark.

## Batch gates

A batch is complete only when every event has:

- verified identity, date and geography;
- at least one authoritative source;
- source-level provenance for every populated critical impact field;
- explicit semantics for deaths, injured, missing, affected and displaced;
- separate economic damage, economic loss and reconstruction needs where available;
- uncertainty/ranges preserved;
- event-chain relationships represented;
- source conflicts retained and resolution state recorded;
- deterministic quality score;
- audit status.

## Critical rule

The 100-event registry is not counted as an audited dataset until enrichment and independent verification are complete. Unknown is never zero, and linked cascade impacts are never added blindly.

## Execution sequence

1. Audit events 1–20.
2. Freeze batch 01 evidence ledger.
3. Calculate field coverage/provenance/conflict/resolution/cascade metrics.
4. Repeat for batches 02–05.
5. Only after batch 05 calculate the final 100-event headline metrics.

## Required output per batch

- event count audited;
- event count pending/rejected;
- critical-field coverage by field;
- provenance completeness;
- conflict count and resolution rate;
- cascade integrity rate;
- quality-score distribution;
- coverage by hazard class;
- evidence ledger with source IDs and retrieval dates.
