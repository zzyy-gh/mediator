---
id: agent.probe-world
purpose: Identify which graph nodes the inquiry needs but does not yet have; spawn feed-inquiries on gaps.
default_owner: agent
reads:
  - graph/*.md
  - inquiries/<self>.md
  - feeds/*.md
writes:
  - inquiries/<self>.md#m_nodes
spawns:
  - feed-inquiry
prerequisites:
  - sections.scope: ready
  - sections.assumptions: ready
---

# Probe — World

## Purpose

Diff what the inquiry needs to reason well against what the graph currently holds. When a needed node is missing or stale, propose a feed (or escalate if no feasible source).

## Inputs

- Scope, assumptions, graph references.
- Current graph state across `graph/*.md`.
- Active feeds in `feeds/`.

## Process

1. List the nodes the inquiry would benefit from (by topic).
2. For each: present in graph? freshness within tolerance? confidence sufficient?
3. For gaps: identify candidate feeds. If a feed already exists, request a refresh. If not, draft a feed-flavour inquiry via `feed-prospector`.
4. Record the diff and resolution path in the inquiry.

## Output

- Updated graph references on the inquiry.
- An `m.probe.world` entry summarising the gap diff.
- If gaps require new feeds, child feed-inquiry id(s) referenced.

## Failure modes

- Asks for everything — restrict to load-bearing gaps only.
- Spawns feed-inquiry for a vehicle the user does not trade — confirm before spawning.
