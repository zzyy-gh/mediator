# Flows Nodes

Positioning, fund flows, prime-broker data, options skew, ETF creations/redemptions. Updated by flow feeds.

## Example

```yaml
- id: flows.tech-positioning
  topic: flows
  content: "HF tech net long elevated"
  distribution:
    shape: empirical
    params:
      percentile: 75
      historical_mean_pct: 50
  confidence: 0.65
  provenance:
    source: feed.prime-broker
    timestamp: 2026-05-07T00:00:00Z
  fuzz_halo: "dark-pool offset not measured"
```

_(Hydrate as feeds come online.)_
