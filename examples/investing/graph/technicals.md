# Technicals Nodes

Price, volume, vol regime, breadth, term structure, intermarket relationships. Price is one node here, not privileged.

## Example

```yaml
- id: technicals.vol-regime
  topic: technicals
  content: "VIX 22, 30d realized 19, mid-elevated"
  distribution:
    shape: lognormal
    params:
      median: 21
      iqr: [18, 26]
      horizon: 90d
  confidence: 0.7
  provenance:
    source: feed.cboe
    timestamp: 2026-05-07T00:00:00Z
  fuzz_halo: "macro shock not priced"

- id: technicals.spx-price
  topic: technicals
  content: "SPX at level X, 50d above 200d, breadth fair"
  confidence: 0.95
  provenance:
    source: feed.market-data
    timestamp: 2026-05-08T00:00:00Z
```

_(Hydrate as feeds come online.)_
