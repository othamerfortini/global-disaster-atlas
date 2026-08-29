# Global Quantitative Evidence Report — Status

Date: 2026-08-29

## Final audit state

The 100-event registry is present, but the global quantitative report cannot be truthfully closed from the repository state currently available.

### Batch state

- Batch 01: CLOSED; 20/20 events audited.
- Batch 02: HISTORICAL AUDIT ARTIFACT NOT RECOVERED. Events 21–40 are identifiable from the canonical registry and may be reconstructed from primary sources, but this is `RECONSTRUCTED_FROM_PRIMARY_SOURCES`, not `RECOVERED_FROM_AUDIT_ARTIFACT`.
- Batch 03: CLOSED; 20/20 events; 12 gates determined per event.
- Batch 04: CLOSED; 20/20 events; 12 gates determined per event.
- Batch 05: CLOSED; 20 effective events; 12 gates determined per event. Registry correction preserved separately.

## Critical blockers

1. No canonical B02 audit artifact exists in the repository history currently accessible.
2. Therefore no canonical B02 quality-score dataset exists.
3. The repository contains two quality-score conventions: the deterministic `scripts/quality_score.py` model and the auxiliary operational v0.1 score used by Batch 05. These must not be silently mixed in a global statistic.
4. Batch 01 contains coverage metrics but does not contain per-event deterministic scores in its closure artifact.
5. Consequently a global 100-event score distribution or global coverage percentage cannot be calculated without reconstructing the missing canonical observation-level records.

## Required next state

`B02-RECONSTRUCTED` must be materialized as a separate artifact from primary/open sources, with every event carrying explicit states for all 12 gates. Then the canonical quality-score method must be selected and applied consistently. Only after that can the 100-event validation and Global Quantitative Evidence Report be closed.

## Non-negotiable semantics

- ZERO, NOT_REPORTED, UNKNOWN and CONFLICTING remain distinct.
- Estimates are never promoted to official counts.
- Conflicting observations remain preserved with scope, temporal stage and methodology.
- Cascade impacts are not automatically summed.
- Source-specific redistribution restrictions remain explicit.
- EM-DAT is excluded from the primary reconstruction.

## Status

`GLOBAL_QUANTITATIVE_EVIDENCE_REPORT = BLOCKED`

This is a data/provenance blocker, not a missing-analysis blocker. No global number is fabricated to force closure.
