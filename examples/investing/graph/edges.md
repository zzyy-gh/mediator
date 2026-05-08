# Edges

Connections between nodes. First-class. Carry weight, latency, conditional dependence, evidence. Schema: `primitives.md` → edge.

Edges decay, mutate, get refuted. Edge updates are first-class operations from inquiries.

## Example

```yaml
- id: edge.crowding-to-drawdown
  from: flows.tech-positioning
  to: technicals.tech-sleeve-drawdown
  type: causal
  strength:
    shape: bounded
    params:
      range: [0, 1]
      mean: 0.25
      sd: 0.10
    interpretation: "P(forced unwind in 3mo | sector drawdown >5%)"
  latency: "0–14 days from drawdown trigger"
  conditions:
    - "positioning percentile > 70"
    - "vol regime mid-elevated or higher"
  evidence:
    - { source: "2018-Q4 unwind", weight: 0.6 }
    - { source: "2020-03 unwind", weight: 0.7 }
  fuzz_halo: "regime-conditional; weakens in low-vol"
  status: active
```

_(Edges accumulate as belief-Collapses land in the graph.)_
