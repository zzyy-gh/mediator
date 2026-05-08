---
id: agent.probe-graph
purpose: Walk edges from referenced nodes; surface dependencies, cross-confirmations, hidden bets.
default_owner: agent
reads:
  - graph/*.md
  - inquiries/<self>.md
writes:
  - inquiries/<self>.md#graph_refs
  - inquiries/<self>.md#m_nodes
prerequisites:
  - sections.scope: ready
  - sections.assumptions: ready
---

# Probe — Graph

## Purpose

Given the inquiry's referenced nodes, walk outward along edges to find what else this bet implicitly depends on, and where cross-confirmations or contradictions live.

## Inputs

- Inquiry's `## Graph references` (initial set).
- `graph/edges.md` — connections.
- All `graph/*.md` — node bodies.

## Process

1. For each referenced node, traverse outgoing edges within a configured depth (default: 2).
2. Identify nodes that consistently appear via multiple paths — likely load-bearing.
3. Surface implicit factor exposures, hidden correlations, and reflexive loops.
4. Note edges flagged `weakened` or `refuted` in the path — the inquiry rests on shaky ground there.

## Output

- Augment `## Graph references` with newly relevant node ids.
- Add an `m.probe.edges` entry to the M-nodes section summarising findings: which edges did the heavy lifting, which broke, what implicit bets surfaced.

## Failure modes

- Walks too deep, returns noise — cap depth.
- Misses a path because no edge exists — opens a candidate edge as a child belief-inquiry.
