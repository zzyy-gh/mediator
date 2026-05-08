---
id: agent.probe-prior-art
purpose: Has this been solved or attempted before? What worked, what failed, what is the established literature?
default_owner: agent
reads:
  - methods.md
  - inquiries/*.md
  - graph/themes.md
  - graph/edges.md
writes:
  - inquiries/<self>.md#m_nodes
prerequisites:
  - sections.scope: ready
  - sections.assumptions: ready
tools:
  - web_search
---

# Probe — Prior Art

## Purpose

Before the inquiry treats anything as novel, find the existing literature, methods, and prior closed inquiries that touch the same territory.

## Inputs

- Scope and assumptions.
- `methods.md` — toolbox.
- Closed entries in `inquiries/`.
- `graph/themes.md`, `graph/edges.md` — running hypotheses.
- Web search.

## Process

1. Extract key concepts from scope.
2. Match against `methods.md` — which methods are candidate-relevant.
3. Search closed inquiries for similar scope or candidate.
4. Web search for academic and practitioner literature.
5. Summarise findings: what is solved, what is open, what specifically failed historically.

## Output

An `m.probe.prior-art` entry in the inquiry's `## M-nodes (sequence)` section. Three to seven bullets. Cite sources in provenance.

## Failure modes

- Reinvents wheel — flag if scope overlaps a closed inquiry within last 90 days.
- Cites without summarising — re-run with explicit "what specifically transfers".
