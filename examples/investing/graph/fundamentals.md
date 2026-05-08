# Fundamentals Nodes

Earnings, margins, capex, balance-sheet health, sector aggregates, single-name fundamentals. Updated by filings and earnings feeds.

## Example

```yaml
- id: fundamentals.tech-q1-earnings
  topic: fundamentals
  content: "Q1 2026 tech: 68% beats, 22% guide-down"
  distribution:
    shape: empirical
    params:
      beat_rate: 0.68
      guide_down_rate: 0.22
      next_q_surprise: { mean: 0.01, sd: 0.04 }
  confidence: 0.8
  provenance:
    source: feed.filings-aggregator
    timestamp: 2026-05-06T00:00:00Z
  fuzz_halo: "sector-aggregate masks dispersion"
```

_(Hydrate as feeds come online.)_
