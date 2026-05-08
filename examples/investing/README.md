# Investing Instance

Concrete instance of the [mediator framework](../../README.md), tuned for one objective: **favourable expected return relative to expected risk**. The world is treated as a connected graph; everything (price, macro, flows, sentiment, fundamentals, themes, politics, portfolio) is an equal-weight node. See `architecture.md` for the shape and flow.

## Layout

| File / dir | Role |
|------------|------|
| `objective.md` | Sole goal, operating principles, invariants. |
| `architecture.md` | Graph + inquiry + Collapse + outcome loop. **Read this first.** |
| `strategies.md` | Two committed archetypes (Type A, Type B) and the menu of open considerations. |
| `primitives.md` | Schemas: node, edge, inquiry, operation. |
| `methods.md` | Toolbox: sizing, risk, return-modelling, behavioural. Available, not required. |
| `blind-spots.md` | Known biases and failure modes; adversarial probes pre-Collapse. |
| `template-inquiry.md` | Inquiry shape: scope, assumptions, graph refs, distributions, sensitivity. |
| `amendments.md` | Append-only log of proposed and accepted changes. |
| `graph/` | Persistent connected world: macro, flows, sentiment, technicals, fundamentals, themes, politics, portfolio, strategies, edges. |
| `inquiries/` | Open-ended, ranked, or actionable inquiries. |
| `agents/` | Agent specs (markdown). One file per agent. Owner field on any section can swap in a human. |
| `feeds/` | Data-source specs; each feed registered via a feed-flavour inquiry. |
| `orchestrator/` | Python runner using the Claude Agent SDK. Watches inquiries, dispatches agents, runs feeds. |
| `taste/` | Private, gitignored. Revealed-preference log. |

## How to run

1. Open an inquiry: copy `template-inquiry.md` to `inquiries/YYYY-MM-DD-name.md`. Choose `shape` (convergent | divergent) and `collapse_flavour` (capital | belief | feed).
2. Sharpen scope. List load-bearing assumptions.
3. Snapshot graph state. Reference relevant nodes by id.
4. Run M-nodes: probe scope, prior art, world, edges; reframe if needed; feasibility-gate.
5. Collapse (human gate). Output:
   - **capital** — position change.
   - **belief** — graph node or edge added / strengthened / refuted.
   - **feed** — new data source registered in `feeds/`.
6. On outcome window, fill realized values, calibration delta, edges affected.
7. Reflect. If a pattern recurs across ≥3 inquiries, promote to `amendments.md`.

## Plug-in rule

Every section / file declares an owner: `human | agent | either`. Orchestrator dispatches by status. Sections write only to themselves. Swap actors via the owner field; no code change.
