# Hazard Cascades

## Purpose

A disaster is not always a single hazard. A primary event can trigger secondary hazards, technological failures, infrastructure failures, environmental damage and long-duration social consequences.

The Atlas therefore models disasters as **event chains**, not just isolated points on a map.

## Canonical distinction

- **Hazard** — physical, technological or other threatening phenomenon.
- **Event** — a specific occurrence of that hazard.
- **Consequence** — an impact produced by an event.
- **Relationship** — an evidence-backed causal or temporal connection between events.

## Examples

### Tohoku / Fukushima

```text
Earthquake
  -> Tsunami
  -> Coastal flooding
  -> Infrastructure damage
  -> Nuclear accident
  -> Evacuation / environmental consequences
```

The natural hazards and technological accident remain distinct events while their relationships preserve the cascade.

### Mariana

The 2015 Fundão dam failure is **not** classified as a natural flood. It is an infrastructure/technological failure that produced a tailings inundation/flood-like event and downstream environmental and social impacts.

```text
Infrastructure failure
  -> Dam failure
  -> Tailings inundation
  -> River contamination
  -> Community displacement
  -> Environmental / economic consequences
```

The secondary inundation may be represented with flood-like spatial geometry without changing the primary event class to `natural_hazard`.

## Design rules

1. Never force a compound disaster into one hazard label.
2. Keep causally distinct events as separate canonical entities when they have independent timing, location, sources or impacts.
3. Use `relationships` to represent causality, sequence and composition.
4. Every causal relationship should retain evidence source IDs when available.
5. Causality must be expressed conservatively: an association is not automatically a causal claim.
6. A modeled exposure is not an observed impact.
7. Direct, cascading and indirect impacts should remain distinguishable in later versions of the impact model.

## Why this matters

This model supports natural, technological and hybrid disasters without corrupting the historical record. It also enables future Atlas features such as event-chain visualization, cascading-risk analysis and reconstruction of complex disasters over time.
