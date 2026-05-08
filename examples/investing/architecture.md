# Architecture

## Premise

The investing world is a connected graph. Risk, return, macro, flows, sentiment, fundamentals, themes, politics, portfolio, **and price** all sit as equal-weight nodes. Edges between them carry weight, latency, and conditional dependence. The objective is **favourable expected return relative to expected risk** of the portfolio. Every component serves this.

## Three things at any moment

```
┌──────────────────────────────────────────────────┐
│                    GRAPH                         │
│  always-on, always updating                      │
│                                                  │
│  nodes: macro · flows · sentiment · technicals   │
│         fundamentals · themes · politics         │
│         portfolio                                │
│  edges: connections between them                 │
└──────────────────────────────────────────────────┘
       ▲                                ▲
       │ feeds tick (continuous)        │ outcomes feed back
       │                                │
       ▼                                │
┌──────────────────────┐         ┌──────┴──────────┐
│ open inquiry A       │         │ closed inquiry  │
│  (capital question)  │         │  (outcome →     │
└──────────────────────┘         │  graph updates) │
┌──────────────────────┐         └─────────────────┘
│ open inquiry B       │
│  (belief question)   │
└──────────────────────┘
┌──────────────────────┐
│ open inquiry C       │
│  (feed question)     │
└──────────────────────┘
```

**Graph** = the living memory. **Inquiries** = open questions in flight. **Outcomes** = the loop that feeds learning back.

## What an inquiry looks like

```
inquiry opens (anyone, anytime)
        │
        ▼
   snapshot graph                ← freeze the world for reproducibility
        │
        ▼
   ┌────────────┐
   │ scope      │   ← actors (human or agent) fill sections
   │ probe      │     each section has owner: human | agent | either
   │ reframe    │
   │ feasibility│
   └────────────┘
        │
        ▼
   COLLAPSE  (human gate)
        │
        ▼
   commits ONE of three things:
     • capital   (open / close / resize position)
     • belief    (add / strengthen / refute graph edge or node)
     • feed      (register / replace data source)
        │
        ▼
   outcome eventually arrives
        │
        ▼
   GRAPH updated (edges, themes, calibration, taste)
```

One lifecycle. Three Collapse flavours. Same machinery underneath.

## Convergent and divergent inquiries

Inquiries differ only in the **shape of output**, not in lifecycle:

- **Convergent** — picks one answer.
  *Examples: "Should I buy NVDA?" "Is this edge real?" "Add this feed?"*
- **Divergent** — picks a set or ranking.
  *Examples: "Top 10 high E[R]/E[risk] combinations." "What is most undervalued?" "Map future demand vs supply for lithium."*

A divergent inquiry's Collapse outputs a structured artifact (list, ranking, scenario tree) that lands in the graph. That artifact often **spawns child convergent inquiries** on its top candidates. Children inherit the parent's snapshot and reasoning chain.

## Hypothesis lifecycle (no separate machinery)

A hypothesis is just an inquiry with a belief-Collapse. It can ripen over many loops:

```
vague seed → researched → cross-confirmed by edges → sensitivity-bounded
   → portfolio-fit checked → capital-Collapse warranted
```

Same inquiry, more iterations. "Actionable" is a phase along this spectrum, not a category.

## Three actor classes (interchangeable)

- **Feeds** — push external observation into graph nodes. Run continuously, async.
- **Operators** — probe, reframe, predict, reflect over graph + inquiry sections.
- **Humans** — set intent, gate Collapse, approve high-impact graph or objective changes.

Any role can be filled by human or agent. Status fields on files dispatch the next actor. Sections write only to themselves — no merge conflicts.

## Closure (the loop)

When an inquiry closes, three things happen:

1. **Record reality** — log the outcome.
2. **Compare prediction vs reality** — calibration delta.
3. **Push the lesson back into the graph** — edges strengthen or weaken; themes update; self-calibration adjusts; taste log appends; recurring patterns surface as `amendments.md` candidates.

Every closed inquiry leaves the graph slightly smarter. The next inquiry starts from a better-informed state. **The loop is the learning.**

## What the framework is opinionated about

Only three things:

- **The objective** — favourable E[R] / E[risk].
- **The shape** — graph + inquiry + Collapse + outcome loop.
- **The two strategy archetypes** — Type A (resilient compounder) and Type B (asymmetric speculative). See `strategies.md`.

Everything else (methods, sizing, risk measures, data sources, vehicles, agent implementations, portfolio architecture) is up for grabs by the user and agents, chosen per inquiry, and evolved by amendments.

## Agents and orchestrator

Agent specs live in `agents/<name>.md` — single-purpose, stateless functions over graph + inquiries. The orchestrator (`orchestrator/`) is a small Python runner using the Claude Agent SDK. It watches `inquiries/` for section-status changes and dispatches the matching agent (or notifies a human if the section's owner is `human`). Sections write only to themselves; cross-inquiry work runs in parallel.

## Why flat and abstract

Because nothing is prescribed:
- **First principles** is forced — no method to lean on by default.
- **Assumptions and distributions are explicit** — no hand-waving allowed by the template.
- **Edges and their evidence are visible** — every causal chain is auditable.
- **Recombination is free** — any node can connect to any node; any method can compose with any other.

Innovation, critical analysis, and probabilistic rigour are emergent properties of this discipline.
