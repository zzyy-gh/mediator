---
id: feed.commodities-fx
status: proposed
target_nodes:
  - graph/macro.md
  - graph/technicals.md
cadence: daily
latency: end-of-day to next-open
quality:
  coverage: gold, oil, broad commodities index, DXY, major FX crosses
  accuracy: medium-high (FRED + free price providers)
  history: long
cost: free
provenance:
  registered_by_inquiry: <pending>
  reviewed_at: null
---

# Feed — Commodities & FX

Free price series for commodities and FX via FRED (where available) and yfinance for ETF / futures proxies.

## Reads

- FRED series for gold, WTI, broad commodity index where published.
- yfinance for proxies: GLD, USO, DBC, UUP, EURUSD=X, USDJPY=X, etc.

## Writes

- `graph/macro.md` — DXY, real rates, oil, gold (as macro signals).
- `graph/technicals.md` — single-vehicle price/vol nodes.

## Implementation

`orchestrator/feeds/commodities_fx.py`. Universe configurable. Treat ETF proxies as approximations and tag fuzz_halo accordingly.
