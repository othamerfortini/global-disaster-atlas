# Audit Gate v1

An event is counted as AUDITED only after all applicable checks pass.

## Identity

- [ ] Event has a stable canonical ID.
- [ ] At least one authoritative source supports the event identity.
- [ ] Source record ID is preserved when available.

## Time and geography

- [ ] Start time/date has a precision classification.
- [ ] Location has a precision classification.
- [ ] Geometry is retained when the source provides it.

## Critical impacts

For each of deaths, injured, missing, affected, displaced, economic damage, economic loss and reconstruction needs:

- [ ] Value is present, or explicitly null/unknown.
- [ ] Unit is explicit.
- [ ] Definition/scope is explicit where needed.
- [ ] Reported/estimated/modeled status is explicit.
- [ ] Value-level provenance is present for populated values.

## Conflicts

- [ ] Material multi-source disagreement is represented as a conflict.
- [ ] Semantic differences are distinguished from numeric conflicts.
- [ ] Resolution rule is documented when resolved.
- [ ] Unresolved conflicts remain visible.

## Cascades

- [ ] Relationship type is explicit.
- [ ] Causal claims have evidence when available.
- [ ] Chain-level impact is not double-counted.

## Licensing

- [ ] Source access/redistribution status is recorded.
- [ ] Restricted raw data is not copied into the repository without permission.

## Final state

Only after all applicable checks pass:

`AUDITED`

Otherwise:

`AUDIT_EXCEPTION`
