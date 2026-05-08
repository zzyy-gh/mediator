# Constitution — Investing Instance

Inherits the root constitution. Adds investing-specific invariants. Changes here require explicit user input, impact analysis, and propagation to schemas, registry, and active ledger entries.

## Inherited from framework

- User-as-principal at every Collapse.
- Provenance preservation on every S-node.
- Append-only ledger.
- Human-in-loop at Collapse.

## Instance-specific

- **Position sizing** — confidence-haircut Kelly. No full-Kelly without explicit amendment.
- **Drawdown stop** — hard exit at thesis-specific level, set at entry, logged in the ledger entry.
- **No leverage** without explicit amendment plus propagation to risk registry.
- **Calibration window** — every prediction carries an explicit outcome window. No open-ended bets.
- **Reframe before averaging down** — losing positions trigger Reframe, not auto add.
- **Prior-art Probe before novel thesis** — search `registry/tools.md` and external literature before treating an idea as original.
- **Crowding check** before any sizing decision >2% NAV.
