# Politics Nodes

Regulation, geopolitics, election cycles, trade policy, sanctions. Updated by news, policy-tracker, and curated feeds.

## Example

```yaml
- id: politics.us-china-tariff-regime-2026
  topic: politics
  content: "Tariff escalation phase; expansion to additional categories possible"
  distribution:
    shape: discrete
    params:
      status_quo: 0.50
      escalation: 0.35
      partial_rollback: 0.15
  confidence: 0.5
  provenance:
    source: feed.policy-tracker
    timestamp: 2026-05-08T00:00:00Z
  fuzz_halo: "election-cycle pressure under-weighted"
```

_(Hydrate as feeds come online.)_
