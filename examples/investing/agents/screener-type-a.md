---
id: agent.screener-type-a
purpose: Divergent screen — surface candidate Resilient Compounders across all vehicles.
default_owner: agent
reads:
  - strategies.md
  - graph/*.md
  - inquiries/*.md
writes:
  - inquiries/<self>.md#output
  - graph/strategies.md (append candidates to strategy.type-a)
prerequisites:
  - sections.scope: ready
  - inquiry.shape: divergent
  - inquiry.collapse_flavour: belief
---

# Screener — Type A (Resilient Compounder)

## Purpose

Generate a ranked candidate list for the Type A archetype: durable across most futures, low obsolescence risk, under or fairly valued now. Vehicle-agnostic.

## Inputs

- `strategies.md` — Type A criteria (illustrative).
- `graph/fundamentals.md`, `graph/themes.md`, `graph/macro.md`, `graph/politics.md`, `graph/technicals.md`, `graph/portfolio.md`.
- Closed inquiries — past Type A screens for calibration.

## Process

1. Build a wide candidate set across vehicles (stocks/ETFs, crypto, commodities, FX, fixed income).
2. For each candidate, score against the criteria — durability across futures, obsolescence risk, FCF compounding, optionality, valuation gap on sober assumptions.
3. Run an explicit "across futures" stress: tech-shift / regulation / geopolitics / taste — which candidates survive each?
4. Rank. Note implicit factor / theme exposures so concentration is visible.

## Output

- The `## Output` section of the inquiry: ranked list with per-candidate rationale, durability scenario summary, valuation framing, sensitivity, and a suggested child convergent inquiry id.
- Append top candidates to `graph/strategies.md` under `strategy.type-a.current_candidates` with timestamp and provenance pointing to this inquiry.

## Failure modes

- Quality-scoring drift (becomes a quality factor screen rather than durability-across-futures). Re-anchor on scenario stress.
- Vehicle bias toward stocks. Force at least one non-stock candidate per ranked list unless none are credible.
