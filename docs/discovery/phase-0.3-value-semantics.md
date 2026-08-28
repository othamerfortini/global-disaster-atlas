# Phase 0.3 — Value Semantics Extension

Date: 2026-08-28
Status: ADDED TO SPECIFICATION

## Critical impact values

The Atlas must preserve the epistemic status of every reported value.

Allowed `value_type`:

- `exact`
- `estimate`
- `range`
- `minimum`
- `maximum`
- `unknown`
- `conflicting`

The original source expression must be retained. The canonical layer must not convert an estimate into an exact value or replace a range with its midpoint.

## Multiple observations

A field may contain multiple source observations:

`source -> value -> definition -> scope -> observation_time -> publication_time -> methodology -> value_type`

Conflicting observations remain available through the source view and are resolved only when the conflict is demonstrably temporal, semantic, scope-based or methodological.

## Cascade filters

Human-impact totals must be queryable by cascade component where evidence permits:

- primary hazard
- secondary hazard
- tertiary consequence
- direct impact
- indirect impact
- evacuation/displacement
- infrastructure/economic consequence

Component totals must never be automatically summed when overlap can cause double counting.

## User-facing filters

The future Atlas should support:

- exact only
- estimates included
- ranges only
- all source observations
- canonical resolved values
- conflicting observations
- direct impacts
- cascade-inclusive impacts
- individual cascade component

This allows a user to distinguish 'what a source reported' from 'what the Atlas can defensibly resolve'.

## Reporting rule

Coverage metrics must distinguish:

1. field exists in at least one source;
2. field has provenance;
3. field is semantically normalized;
4. field is conflict-resolved;
5. field is suitable for canonical aggregation.

A non-null value alone does not equal reconstructability.
