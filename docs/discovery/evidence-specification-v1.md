# Evidence Specification v1.0

## Status

Normative specification for the Global Disaster Atlas evidence layer.

## Objective

Every published critical value must be traceable to one or more source observations. The Atlas preserves original observations and does not silently overwrite disagreement.

## Core entities

### Source

A publisher or dataset endpoint.

Required concepts:
- source_id
- publisher
- dataset
- access URL
- license/terms status
- retrieval timestamp

### SourceObservation

An atomic claim extracted from a source.

Required concepts:
- observation_id
- event candidate / resolved event ID
- field path
- raw value
- normalized value
- unit
- definition
- status: reported | estimated | modeled | unknown
- source_id
- source record ID when available
- source URL
- retrieved_at

### Event

The canonical historical occurrence after entity resolution. An event may be natural, technological, infrastructure, biological, social, environmental, or compound.

### Conflict

Two or more observations that cannot safely be treated as identical without a documented decision. Conflicts include value, unit, definition, timing, geography, attribution and scope conflicts.

### Resolution

The explicit decision applied to a conflict. A resolution must preserve all relevant observations and state the rule/evidence used.

### CanonicalValue

The normalized value exposed to downstream analytics. It must point back to its supporting observations and resolution where applicable.

### AuditRecord

A reproducible record of validation: who/what checked it, when, checks performed, result, and any exceptions.

## Critical fields

- deaths
- injured
- missing
- affected
- displaced
- economic damage
- economic loss
- reconstruction needs

Additional impact fields may be added without redefining the critical-field denominator.

## Null and zero policy

`0` means the source establishes zero.

`null` means unknown, unavailable, not reported, or not safely inferable.

A missing source value must never be converted to zero.

## Value semantics

Never collapse these without explicit justification:

- deaths vs deaths + missing;
- exposed vs affected;
- displaced vs homeless;
- damage vs economic loss;
- reconstruction needs vs damage/loss;
- event-level impact vs disaster-chain impact.

## Ranges

If a source reports a range, preserve the range. Do not manufacture a point estimate unless a documented analytical method requires one.

## Provenance requirement

A critical canonical value is auditable only if a third party can identify the source observation and retrieve the source record or document under the recorded access conditions.

Event-level provenance alone is insufficient for a value-level provenance claim.

## Conflict policy

1. Preserve every material observation.
2. Identify whether disagreement is actually semantic rather than numeric.
3. Prefer authoritative final/official values only when authority and definition match the field.
4. Do not resolve a conflict merely by majority vote.
5. If no defensible resolution exists, retain a range or unresolved conflict.
6. Record the resolution rationale and evidence IDs.

## Cascade policy

Causal relationships are evidence-bearing claims. A chain may contain multiple events:

`earthquake -> tsunami -> flooding -> infrastructure failure -> technological accident`

Impacts must not be summed across chain nodes unless overlap has been assessed. Chain-level totals must be deduplicated where possible.

## Audit gates

An event can be `AUDITED` only when:

- identity is supported by evidence;
- time and geography are sufficiently specified;
- every populated critical field has value-level provenance;
- status and units are explicit;
- conflicts are recorded;
- resolutions are documented or marked unresolved;
- cascade relationships have supporting evidence when claimed;
- no missing value is silently represented as zero.

Possible states:
- `DRAFT`
- `SOURCE_VERIFIED`
- `AUDITED`
- `AUDIT_EXCEPTION`

## Metrics

### Coverage

`reconstructable critical field instances / evaluable critical field instances`

### Provenance

`critical canonical values with value-level provenance / reconstructed critical values`

### Conflict resolution

`conflicts resolved or explicitly explained / conflicts identified`

### Auditability

`published values reproducible from recorded evidence / published values`

Metrics must be reported globally and by disaster class, time period and source family.

## Source licensing

Public accessibility does not imply redistribution rights. Raw restricted datasets must not be copied into the repository unless their terms permit it. Where redistribution is not permitted, store metadata, identifiers, derived facts where legally allowed, and retrieval instructions instead.

## Non-negotiable rule

**No important number without an evidence chain.**
