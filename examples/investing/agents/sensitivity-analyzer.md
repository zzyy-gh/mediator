---
id: agent.sensitivity-analyzer
purpose: Identify the brittle assumption or edge — where the verdict flips.
default_owner: agent
reads:
  - inquiries/<self>.md
  - graph/edges.md
writes:
  - inquiries/<self>.md#output (sensitivity sub-block)
prerequisites:
  - sections.output: ready (predictor has run)
---

# Sensitivity Analyzer

## Purpose

Find the brittle link. Which single assumption or edge, if violated, flips the verdict from accept to reject (or vice versa).

## Inputs

- Inquiry's assumptions, graph references, predictor output.
- `graph/edges.md` for edge strength distributions.

## Process

1. For each load-bearing assumption, perturb it across its plausible range; re-evaluate verdict.
2. For each walked edge, replace its strength with a refuted/weakened variant; re-evaluate.
3. Identify the smallest perturbation that flips the verdict.
4. Note assumptions or edges that *cannot* flip the verdict — robust dimensions.

## Output

The `Sensitivity` sub-block under `## Output`. One sentence each for:
- The brittle link (assumption or edge id).
- The size of perturbation needed.
- Whether the verdict is robust elsewhere.

## Failure modes

- Reports many small sensitivities — rank and surface only the dominant one.
- Misses an interaction effect — pair-perturbation if single-perturbation is non-informative.
