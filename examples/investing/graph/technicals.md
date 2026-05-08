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

## Auto: feed.yfinance

<!-- BEGIN feed.yfinance -->
```yaml
- id: technicals.spy
  topic: technicals
  content: "SPY daily close + realised vol"
  last_close: 731.5800170898438
  vol_regime: {'realised_30d_pct': 15.94, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.qqq
  topic: technicals
  content: "QQQ daily close + realised vol"
  last_close: 694.9400024414062
  vol_regime: {'realised_30d_pct': 20.35, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.iwm
  topic: technicals
  content: "IWM daily close + realised vol"
  last_close: 282.260009765625
  vol_regime: {'realised_30d_pct': 21.22, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.efa
  topic: technicals
  content: "EFA daily close + realised vol"
  last_close: 102.88999938964844
  vol_regime: {'realised_30d_pct': 23.37, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.eem
  topic: technicals
  content: "EEM daily close + realised vol"
  last_close: 66.58999633789062
  vol_regime: {'realised_30d_pct': 28.72, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xlk
  topic: technicals
  content: "XLK daily close + realised vol"
  last_close: 169.69000244140625
  vol_regime: {'realised_30d_pct': 26.0, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xle
  topic: technicals
  content: "XLE daily close + realised vol"
  last_close: 55.95000076293945
  vol_regime: {'realised_30d_pct': 27.3, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xlf
  topic: technicals
  content: "XLF daily close + realised vol"
  last_close: 51.54999923706055
  vol_regime: {'realised_30d_pct': 15.75, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xlv
  topic: technicals
  content: "XLV daily close + realised vol"
  last_close: 144.72000122070312
  vol_regime: {'realised_30d_pct': 15.8, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xli
  topic: technicals
  content: "XLI daily close + realised vol"
  last_close: 174.0
  vol_regime: {'realised_30d_pct': 24.79, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xlu
  topic: technicals
  content: "XLU daily close + realised vol"
  last_close: 45.119998931884766
  vol_regime: {'realised_30d_pct': 16.23, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xly
  topic: technicals
  content: "XLY daily close + realised vol"
  last_close: 119.87999725341797
  vol_regime: {'realised_30d_pct': 22.21, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xlp
  topic: technicals
  content: "XLP daily close + realised vol"
  last_close: 83.9800033569336
  vol_regime: {'realised_30d_pct': 14.2, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xlb
  topic: technicals
  content: "XLB daily close + realised vol"
  last_close: 51.400001525878906
  vol_regime: {'realised_30d_pct': 17.07, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.xlre
  topic: technicals
  content: "XLRE daily close + realised vol"
  last_close: 44.400001525878906
  vol_regime: {'realised_30d_pct': 14.39, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.goog
  topic: technicals
  content: "GOOG daily close + realised vol"
  last_close: 395.29998779296875
  vol_regime: {'realised_30d_pct': 39.09, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.nvda
  topic: technicals
  content: "NVDA daily close + realised vol"
  last_close: 211.5
  vol_regime: {'realised_30d_pct': 39.81, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.tsla
  topic: technicals
  content: "TSLA daily close + realised vol"
  last_close: 411.7900085449219
  vol_regime: {'realised_30d_pct': 43.66, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.brk_b
  topic: technicals
  content: "BRK-B daily close + realised vol"
  last_close: 475.0799865722656
  vol_regime: {'realised_30d_pct': 12.08, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.gld
  topic: technicals
  content: "GLD daily close + realised vol"
  last_close: 431.67999267578125
  vol_regime: {'realised_30d_pct': 28.01, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.uso
  topic: technicals
  content: "USO daily close + realised vol"
  last_close: 134.97000122070312
  vol_regime: {'realised_30d_pct': 73.1, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.dbc
  topic: technicals
  content: "DBC daily close + realised vol"
  last_close: 30.25
  vol_regime: {'realised_30d_pct': 23.08, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.uup
  topic: technicals
  content: "UUP daily close + realised vol"
  last_close: 27.40999984741211
  vol_regime: {'realised_30d_pct': 5.87, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.tlt
  topic: technicals
  content: "TLT daily close + realised vol"
  last_close: 85.6500015258789
  vol_regime: {'realised_30d_pct': 8.55, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.hyg
  topic: technicals
  content: "HYG daily close + realised vol"
  last_close: 79.86000061035156
  vol_regime: {'realised_30d_pct': 5.37, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.lqd
  topic: technicals
  content: "LQD daily close + realised vol"
  last_close: 108.73999786376953
  vol_regime: {'realised_30d_pct': 6.01, 'n_obs': 122}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.btc_usd
  topic: technicals
  content: "BTC-USD daily close + realised vol"
  last_close: 79616.421875
  vol_regime: {'realised_30d_pct': 28.7, 'n_obs': 180}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"

- id: technicals.eth_usd
  topic: technicals
  content: "ETH-USD daily close + realised vol"
  last_close: 2280.1455078125
  vol_regime: {'realised_30d_pct': 39.48, 'n_obs': 180}
  provenance:
    source: feed.yfinance
    timestamp: 2026-05-08T05:15:19+00:00
  fuzz_halo: "yahoo data; occasional revisions"
```
<!-- END feed.yfinance -->

## Auto: feed.crypto

<!-- BEGIN feed.crypto -->
```yaml
- id: technicals.crypto_bitcoin
  topic: technicals
  content: "bitcoin spot via CoinGecko"
  price_usd: 79640
  market_cap_usd: 1594554780925.2573
  change_24h_pct: -1.8289230922149968
  provenance:
    source: feed.crypto
    timestamp: 2026-05-08T05:15:27+00:00

- id: technicals.crypto_cardano
  topic: technicals
  content: "cardano spot via CoinGecko"
  price_usd: 0.262007
  market_cap_usd: 9688015348.07361
  change_24h_pct: -1.466181522812678
  provenance:
    source: feed.crypto
    timestamp: 2026-05-08T05:15:27+00:00

- id: technicals.crypto_ethereum
  topic: technicals
  content: "ethereum spot via CoinGecko"
  price_usd: 2281.04
  market_cap_usd: 275197495484.13556
  change_24h_pct: -2.133915999717898
  provenance:
    source: feed.crypto
    timestamp: 2026-05-08T05:15:27+00:00

- id: technicals.crypto_ripple
  topic: technicals
  content: "ripple spot via CoinGecko"
  price_usd: 1.39
  market_cap_usd: 85591230893.89345
  change_24h_pct: -1.8419415660432759
  provenance:
    source: feed.crypto
    timestamp: 2026-05-08T05:15:27+00:00

- id: technicals.crypto_solana
  topic: technicals
  content: "solana spot via CoinGecko"
  price_usd: 88.22
  market_cap_usd: 50897081372.26579
  change_24h_pct: -0.3272878656722919
  provenance:
    source: feed.crypto
    timestamp: 2026-05-08T05:15:27+00:00
```
<!-- END feed.crypto -->
