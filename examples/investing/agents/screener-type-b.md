---
id: agent.screener-type-b
purpose: Divergent screen — surface Asymmetric Speculative candidates with deductively-likely undiscovered demand.
default_owner: agent
reads:
  - strategies.md
  - graph/*.md
  - inquiries/*.md
writes:
  - inquiries/<self>.md#output
  - graph/strategies.md (append candidates to strategy.type-b)
prerequisites:
  - sections.scope: ready
  - inquiry.shape: divergent
  - inquiry.collapse_flavour: belief
tools:
  - web_search
---

# Screener — Type B (Asymmetric Speculative)

## Purpose

Generate a ranked candidate list for the Type B archetype: future demand is great and likely by deduction, masses have not yet realised it, current price reflects little of it. Vehicle-agnostic.

## Inputs

- `strategies.md` — Type B criteria.
- `graph/themes.md` — running narrative arcs.
- `graph/fundamentals.md`, `graph/technicals.md`, `graph/macro.md`, `graph/politics.md`, `graph/sentiment.md`.
- Web search for emerging demand signals not yet in graph.

## Process

1. Generate hypotheses about future demand from first principles — physical needs, technological transitions, regulatory shifts, demographic curves, supply bottlenecks.
2. For each hypothesis, deductive chain: necessary causes, sufficient conditions, observable leading indicators.
3. Map each hypothesis to candidate vehicles that would benefit (the natural beneficiaries given supply structure).
4. Score: deductive strength, supply bottleneck quality, recognition-window narrowness, payoff asymmetry, drawdown bound under thesis-failure path.
5. Rank.

## Output

- Inquiry `## Output` section: ranked list with per-candidate explicit demand-deduction chain, supply bottleneck, recognition window, asymmetry, drawdown bound, suggested child convergent inquiry.
- Append candidates to `graph/strategies.md` under `strategy.type-b.current_candidates`.

## Failure modes

- Narrative chasing instead of deduction — re-run requiring a first-principles chain per candidate.
- Confuses "high vol" with asymmetric — drawdown bound must be quantified or candidate is rejected.
