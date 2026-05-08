---
id: feed.edgar
status: proposed
target_nodes:
  - graph/fundamentals.md
cadence: event-driven (filing-day) plus weekly sweep
latency: minutes from filing
quality:
  coverage: US-listed companies, filings authoritative
  accuracy: high (source of truth for SEC filings)
  history: decades
cost: free
provenance:
  registered_by_inquiry: <pending>
  reviewed_at: null
---

# Feed — SEC EDGAR

SEC filings via the public EDGAR endpoints.

## Reads

EDGAR full-text search and structured submissions endpoints. No key required; obey rate limits and User-Agent policy.

## Writes

- `graph/fundamentals.md` — single-name fundamentals from 10-K / 10-Q / 8-K, including FCF, margins, segment detail.
- Optional: append filing summaries to `graph/sentiment.md` when material.

## Implementation

`orchestrator/feeds/edgar.py`. On-demand pulls for tickers referenced in active inquiries; weekly sweep for the watch universe in `graph/strategies.md`.
