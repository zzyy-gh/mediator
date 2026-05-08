# Primitives

Core shapes. Pure data. Pure-function operations over them.

## Node (graph element)

```yaml
node:
  id: string                         # stable id, e.g. "macro.fed-stance" or "themes.ai-capex-cycle"
  topic: macro | flows | sentiment | technicals | fundamentals | themes | politics | portfolio
  content: string                    # natural-language description
  assumptions: [string]              # numbered, load-bearing claims
  distribution: optional             # use distributions where data permits
    shape: normal | lognormal | empirical | mixture | bounded | discrete
    params: object
  confidence: float                  # 0.0 - 1.0 — used when distribution is impractical
  resolution: low | medium | high
  provenance:
    source: string                   # feed id, paper, conversation, inquiry id
    timestamp: ISO8601
    derived_from: [node_id]
  fuzz_halo: string                  # residual uncertainty not captured above
  asset_class: optional string
  horizon: optional string
  expires_at: optional ISO8601       # for time-bounded nodes
```

## Edge (connection between nodes)

```yaml
edge:
  id: string
  from: node_id
  to: node_id
  type: causal | correlational | conditional | mechanical | reflexive
  strength: distribution             # not a single number
  latency: string                    # propagation delay
  conditions: [string]               # when this edge is active
  evidence: [provenance]
  fuzz_halo: string
  status: proposed | active | weakened | refuted
```

Edges decay, mutate, get refuted. Edge updates are first-class operations.

## Inquiry

```yaml
inquiry:
  id: string                         # YYYY-MM-DD-name
  shape: convergent | divergent
  collapse_flavour: capital | belief | feed
  status: open | snapshotted | probing | reframing | gating | closed | aborted
  scope: string
  parent_inquiry: optional inquiry_id  # if spawned by a divergent parent
  graph_snapshot: ref                  # frozen reference to graph state at open
  sections:
    scope: pending | ready | locked
    assumptions: pending | ready | locked
    intent: pending | ready | locked
    self: pending | ready | locked
    m_nodes: pending | ready | locked
    prediction: pending | ready | locked
    outcome: locked | pending | ready
    reflection: locked | pending | ready
  owner: human:<id> | agent:<name> | either
  outcome_window: optional ISO8601
```

## Operation (M-node)

```yaml
op:
  id: string
  kind: bound | connect | probe | collapse | reframe | zoom | compose | decompose | test | update | reflect
  inquiry: inquiry_id
  target: [node_id | edge_id]
  reversibility: low | medium | high
  latency: string
  layer: object | method | meta
  pre_state: ref
  post_state: ref
  rationale: string                  # first-principles reasoning
  feasibility_gate: optional
    capability_pass: bool
    constraint_pass: bool
    budget_pass: bool
```

## Composition

State is graph + open inquiries. Operations are pure functions:
`(state, op) → state'`. No hidden mutation. Every change traceable through provenance and inquiry refs.
