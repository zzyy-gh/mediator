---
id: feed.fred
status: proposed
target_nodes:
  - graph/macro.md
cadence: daily (FRED publishes on its own cadences)
latency: minutes to days depending on series
quality:
  coverage: US macro authoritative; some global series
  accuracy: high (official sources)
  history: long
cost: free (API key required, free)
provenance:
  registered_by_inquiry: <pending>
  reviewed_at: null
---

# Feed — FRED

US Federal Reserve Economic Data via the `fredapi` package.

## Reads

FRED API; requires `FRED_API_KEY`.

## Writes

- `graph/macro.md` — rates (DGS10, DFF), inflation (CPIAUCSL, PCEPI), growth (GDPC1, payrolls), unemployment, fiscal aggregates, central-bank stance proxies.

## Implementation

`orchestrator/feeds/fred.py`. Series list configurable; default = a curated minimum macro panel. Each series writes a node with shape `discrete` or `bounded` distribution depending on series type.
