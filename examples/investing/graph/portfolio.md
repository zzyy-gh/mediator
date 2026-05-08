# Portfolio Node

Live state of the book. Single canonical node, fed by execution. Used by feasibility-gate, predictor (marginal contribution), and reframer (implicit factor exposure).

## Current state

```yaml
- id: portfolio.current
  topic: portfolio
  content: "Live book"
  positions: []                      # filled by execution feed
  exposures:
    gross: null
    net: null
    by_sector: {}
    by_factor: {}                    # MKT, SMB, HML, MOM, ...
  risk:
    realized_vol_30d: null
    drawdown_from_peak: null
    var_95_1d: null
  provenance:
    source: feed.broker
    timestamp: null
  fuzz_halo: "intraday lag"
```

_(Hydrate when broker feed is wired up.)_
