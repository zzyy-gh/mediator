# Macro Nodes

Rates, growth, inflation, central-bank stance, fiscal posture, FX. Updated by macro feeds. Schema: `primitives.md` → node.

## Example

```yaml
- id: macro.fed-stance
  topic: macro
  content: "Fed in pause; rate-cut path data-dependent"
  distribution:
    shape: discrete
    params:
      cuts_in_2026: { 0: 0.25, 1: 0.40, 2: 0.25, 3+: 0.10 }
  confidence: 0.7
  resolution: medium
  provenance:
    source: feed.fed-watch
    timestamp: 2026-05-08T00:00:00Z
  fuzz_halo: "regime change risk if inflation re-accelerates"
```

_(Hydrate as feeds come online.)_

## Auto: feed.commodities-fx

<!-- BEGIN feed.commodities-fx -->
```yaml
- id: macro.cfx_gld
  topic: macro
  content: "GLD (commodities/FX/duration proxy)"
  last_close: 431.67999267578125
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"

- id: macro.cfx_uso
  topic: macro
  content: "USO (commodities/FX/duration proxy)"
  last_close: 134.97000122070312
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"

- id: macro.cfx_dbc
  topic: macro
  content: "DBC (commodities/FX/duration proxy)"
  last_close: 30.25
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"

- id: macro.cfx_uup
  topic: macro
  content: "UUP (commodities/FX/duration proxy)"
  last_close: 27.40999984741211
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"

- id: macro.cfx_eurusd_x
  topic: macro
  content: "EURUSD=X (commodities/FX/duration proxy)"
  last_close: 1.1737089157104492
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"

- id: macro.cfx_usdjpy_x
  topic: macro
  content: "USDJPY=X (commodities/FX/duration proxy)"
  last_close: 156.87399291992188
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"

- id: macro.cfx_gbpusd_x
  topic: macro
  content: "GBPUSD=X (commodities/FX/duration proxy)"
  last_close: 1.356704831123352
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"

- id: macro.cfx_tlt
  topic: macro
  content: "TLT (commodities/FX/duration proxy)"
  last_close: 85.6500015258789
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"

- id: macro.cfx_hyg
  topic: macro
  content: "HYG (commodities/FX/duration proxy)"
  last_close: 79.86000061035156
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"

- id: macro.cfx_lqd
  topic: macro
  content: "LQD (commodities/FX/duration proxy)"
  last_close: 108.73999786376953
  provenance:
    source: feed.commodities-fx
    timestamp: 2026-05-08T05:15:27+00:00
  fuzz_halo: "ETF / FX-cross proxy; not the underlying"
```
<!-- END feed.commodities-fx -->
