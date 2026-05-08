---
id: feed.crypto
status: proposed
target_nodes:
  - graph/technicals.md
  - graph/flows.md
cadence: hourly for prices; daily for flows
latency: minutes for spot; hours for on-chain proxies
quality:
  coverage: BTC, ETH, top alts via CoinGecko; Binance public for liquidity
  accuracy: medium-high for spot; lower for derived flow metrics
  history: years
cost: free (public endpoints; respect rate limits)
provenance:
  registered_by_inquiry: <pending>
  reviewed_at: null
---

# Feed — Crypto

Public crypto data via CoinGecko and Binance public APIs.

## Reads

- CoinGecko REST — spot prices, market caps, volumes.
- Binance public REST — order book proxies, futures funding rates if needed.

## Writes

- `graph/technicals.md` — BTC, ETH, and configured alts: price, volume, vol regime.
- `graph/flows.md` — funding rates, large-coin dominance, exchange-balance proxies.

## Implementation

`orchestrator/feeds/crypto.py`. Universe configurable; default = BTC, ETH plus a small basket. On-chain feeds (Glassnode-style) deferred to a later feed-inquiry.
