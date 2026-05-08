---
id: agent.outcome-recorder
purpose: At outcome window, record realized state, calibration delta, and which edges held or broke.
default_owner: agent
reads:
  - inquiries/<self>.md
  - graph/*.md
writes:
  - inquiries/<self>.md#outcome
  - graph/edges.md (update edge strengths)
  - graph/themes.md (update theme confidence)
  - graph/portfolio.md (if capital Collapse)
prerequisites:
  - inquiry.status: closed (post-Collapse)
  - current_date >= inquiry.outcome_window
---

# Outcome Recorder

## Purpose

Close the loop. Record what actually happened, compute calibration delta vs prediction, and propagate updates to edges and themes that the inquiry walked.

## Inputs

- The closed inquiry's prediction.
- Current graph state (technicals, fundamentals, portfolio, etc.).
- Edges and themes referenced during the inquiry.

## Process

1. Pull realized values for the prediction targets at outcome_window.
2. Compute calibration delta — predicted distribution vs realized.
3. For each walked edge: did it fire as predicted under the conditions present? Update strength distribution; mark `weakened` or `refuted` if it failed.
4. For each referenced theme: confidence update; flag regime change if material.
5. Update `self.calibration` track-record nodes for this kind of inquiry.

## Output

- `## Outcome` section filled: realized state, calibration delta, edges affected, themes updated.
- Inline updates to `graph/edges.md` and `graph/themes.md` with provenance pointing back to this inquiry.
- If capital Collapse: append realized P&L to portfolio history.

## Failure modes

- Outcome data unavailable — leave pending and re-try later; do not fabricate.
- Records realized but does not update graph — re-run with explicit propagation step.
