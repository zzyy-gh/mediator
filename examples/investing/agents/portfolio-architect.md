---
id: agent.portfolio-architect
purpose: Open-ended portfolio construction. Pull framings situationally; propose architecture; surface holes.
default_owner: either
reads:
  - strategies.md
  - graph/*.md
  - inquiries/*.md (closed)
  - methods.md
writes:
  - inquiries/<self>.md#output
  - graph/strategies.md (update strategy.portfolio-architecture)
prerequisites:
  - sections.scope: ready
  - sections.assumptions: ready
---

# Portfolio Architect

## Purpose

Architect the portfolio (or evaluate the current one) creatively and critically. Pull framings from the open-considerations menu in `strategies.md` situationally — game-theoretic, macro regime, scenario distribution, correlation structure, liquidity, mandate, time-horizon mix, tail-hedge availability, reflexivity. No prescribed recipe.

## Inputs

- `strategies.md` — Type A and Type B archetypes; open-considerations menu.
- `graph/strategies.md` — current candidates from screeners.
- `graph/portfolio.md` — current book.
- `graph/macro.md`, `graph/themes.md`, `graph/politics.md`, `graph/edges.md`.
- `methods.md` — composition tools.

## Process

1. State the framings being applied to this inquiry, and why each is relevant now.
2. Build the scenario set explicitly — open-ended; not limited to base/bull/bear/tail.
3. For each scenario: probability, what wins, what loses, where flows accumulate.
4. Check coverage: does the proposed (or current) book win across most-probable futures? Which scenarios have no exposure or no hedge?
5. Identify holes — uncovered scenarios, concentration risks, implicit factor bets, missing tail protection, redundant positions.
6. Propose adjustments — additions, trims, swaps, hedges, with sizing rationale.
7. Output is non-prescriptive: a structured proposal, not a verdict.

## Output

Inquiry `## Output` (convergent, belief Collapse):
- Framings used (with one-line rationale each).
- Scenario set with probabilities and per-scenario book performance.
- Coverage assessment.
- Holes surfaced.
- Proposed adjustments with rationale.

Update `graph/strategies.md` → `strategy.portfolio-architecture` with the latest snapshot.

## Failure modes

- Defaults to one framing (e.g. "bucket the book base/bull/bear/tail"). Re-run requiring at least three distinct framings be considered.
- Prescribes a fixed allocation. Re-run requiring rationale per adjustment, and surfacing alternatives.
- Misses reflexivity / second-order effects. Cross-check with edges marked `reflexive`.
