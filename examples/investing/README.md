# Investing Instance

Concrete instance of the [mediator framework](../../README.md) applied to investing decisions. Treat as a worked example of the §11 layout, not a prescription.

## Layout

- `constitution.md` — instance-level invariants (inherits root constitution; adds investing-specific limits).
- `schemas/` — S-node and M-node shapes for this instance.
- `registry/` — tools, prior art, and known blind spots in the investing domain.
- `ledger/` — append-only record of decisions: framing, S-nodes, M-nodes, predictions, outcomes.
- `amendments/` — proposed and accepted changes to primitives, heuristics, schemas.
- `taste/` — private (gitignored). Revealed-preference log: what was considered, dismissed, chosen, and why.

## How to use

1. Open a live decision in `ledger/YYYY-MM-DD-name.md`.
2. Frame in S-nodes (Intent / World / Self) and M-nodes (Probe, Reframe, Test, Collapse, ...).
3. Probe gaps; consult `registry/tools.md` before reinventing.
4. Run the feasibility gate before Collapse.
5. Log a prediction with an explicit outcome window. On outcome, append calibration delta.
6. If a reflection recurs across ledger entries, promote it to `amendments/`.
