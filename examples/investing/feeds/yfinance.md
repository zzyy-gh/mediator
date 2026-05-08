---
id: feed.yfinance
status: proposed
target_nodes:
  - graph/technicals.md
  - graph/fundamentals.md
cadence: daily (after US close)
latency: ~24h
quality:
  coverage: broad — global equities, ETFs, indices
  accuracy: medium — Yahoo-sourced; occasional revisions
  history: decades for major names
cost: free
provenance:
  registered_by_inquiry: <pending>
  reviewed_at: null
---

# Feed — yfinance

Daily price, volume, and basic fundamentals via the `yfinance` Python package (Yahoo backend).

## Reads

Yahoo-hosted endpoints; no API key.

## Writes

- `graph/technicals.md` — price, volume, simple vol regime measures (per ticker or index).
- `graph/fundamentals.md` — basic ratios (PE, PS, FCF yield) when available.

## Implementation

`orchestrator/feeds/yfinance.py`. Universe configurable; default to a curated short list of indices and high-coverage names. Append-only writes with timestamp; latest snapshot replaces stale entries by id.
