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
