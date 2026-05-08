# Objective

The sole objective of this instance is **favourable expected return relative to expected risk** of the portfolio. Every node, edge, inquiry, and method exists to serve this. If it does not, drop it.

## Operating principles

- **First principles** — derive from base reasoning. Methods are tools, never commitments.
- **Probabilistic** — distributions and confidences, not point estimates dressed as facts.
- **Assumptions explicit** — every load-bearing claim listed, numbered, falsifiable.
- **Connected** — everything is graph-resident; price is one node, not the centerpiece.
- **Situational** — same problem in different contexts demands different methods.
- **Smart scoping** — frame the problem sharply before reaching for tools.
- **Evolution** — what works gets kept; what does not gets dropped via amendments.
- **Method-flexibility** — pull what is useful (Kelly, factor models, regime detection, options pricing, ...). Drop what is redundant. Use because useful, not because common.

## Invariants

- User-as-principal at every Collapse.
- Provenance preservation on every node, edge, and inquiry.
- Append-only `inquiries/`.
- Human-in-loop at Collapse (capital, belief, or feed).
- Explicit outcome window on every inquiry.
- Reframe before averaging down on losers.

## What this instance does NOT prescribe

Sizing, risk measure, style, horizon, data sources, vehicles — all chosen per inquiry. Surfaced in `methods.md` as available, not required.

## Strategies

Two committed archetypes, declared in `strategies.md`:

- **Type A — Resilient Compounder** — durable across most futures, under or fairly valued now.
- **Type B — Asymmetric Speculative** — deductively-likely large future demand, undervalued pre-recognition.

Portfolio architecture, macro overlays, scenario balancing, money-flow logic, cross-asset structure are **open considerations** — pulled situationally, never prescribed.

## Change process

Changes here require explicit user input plus a propagation pass across:
`architecture.md`, `strategies.md`, `primitives.md`, `methods.md`, `template-inquiry.md`, `blind-spots.md`, `graph/*`, `feeds/*`, `agents/*`, and active entries in `inquiries/`.
