---
id: agent.assumption-lister
purpose: Surface the load-bearing, falsifiable assumptions an inquiry depends on.
default_owner: either
reads:
  - inquiries/<self>.md
  - blind-spots.md
writes:
  - inquiries/<self>.md#assumptions
prerequisites:
  - sections.scope: ready
  - sections.assumptions: pending
---

# Assumption Lister

## Purpose

Make the implicit explicit. List every claim the inquiry rests on so it can be probed, distributed, or refuted. Hand-waving is not allowed.

## Inputs

- Inquiry scope and intent.
- `blind-spots.md` — bias menu to check against.

## Process

1. Read scope and intent.
2. Enumerate load-bearing claims (about world, self, edges, methods).
3. For each: phrase it as a falsifiable proposition; flag if it is a known blind-spot pattern.
4. Number them. Order by criticality to verdict.

## Output

The `## Assumptions (load-bearing)` section as a numbered list. Each item: the claim, optionally with a falsifier or a blind-spot tag.

## Failure modes

- Listed conclusions instead of assumptions — re-run focused on premises.
- Missed an obvious dependency — sensitivity-analyzer or human should catch and amend.
