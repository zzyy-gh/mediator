---
id: agent.predictor
purpose: Build a joint distribution over relevant graph nodes; compute E[R] and E[risk] including portfolio Δ-contribution.
default_owner: agent
reads:
  - inquiries/<self>.md
  - graph/*.md
  - methods.md
writes:
  - inquiries/<self>.md#output
prerequisites:
  - sections.scope: ready
  - sections.assumptions: ready
  - sections.graph_refs: ready
  - sections.m_nodes: ready
---

# Predictor

## Purpose

Convert the inquiry's framing and graph snapshot into an explicit probabilistic prediction at portfolio level. Marginal-only predictions are not sufficient — Δ-contribution is the unit.

## Inputs

- Inquiry assumptions, graph references, M-nodes.
- Edge strengths along walked paths.
- `graph/portfolio.md` — current book.
- `methods.md` — methods to compose (Bayesian shrinkage, scenario tree, factor decomposition, etc.).

## Process

1. Enumerate scenarios consistent with assumptions; assign probabilities.
2. For each scenario: compute portfolio Δ-return distribution if the inquiry's action is taken vs not taken.
3. Aggregate to expected return distribution (mean, variance, skew, tail).
4. Compute expected risk: tail loss, drawdown bound, contribution to portfolio vol.
5. Report E[R] / E[risk] ratio explicitly. Compare to ratios of alternatives if specified.
6. Highlight which assumption or edge dominates the verdict.

## Output

The `## Output` section's Convergent block:
- Expected return — distribution sketch.
- Expected risk — tail measures.
- E[R] / E[risk] ratio.
- Sensitivity — which input flip changes the verdict.

## Failure modes

- Reports point estimates with confidence — re-run requiring distributions.
- Ignores Δ-portfolio — recompute including marginal contribution.
- Method-drift toward one toolkit — pull from `methods.md` situationally.
