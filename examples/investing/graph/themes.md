# Theme Nodes

Long-lived narratives that span many inquiries. Examples: AI capex cycle, energy transition, tariff regime, demographic shifts, deglobalization. Themes carry their own assumption sets and probability of regime change.

## Example

```yaml
- id: themes.ai-capex-cycle
  topic: themes
  content: "AI infrastructure capex elevated; peak timing uncertain"
  assumptions:
    - "Hyperscaler capex tracks token-demand within 2 quarters."
    - "Power constraint binds before chip supply by 2027."
  distribution:
    shape: discrete
    params:
      peak_within_18mo: 0.45
      peak_18_to_36mo: 0.35
      no_peak_36mo: 0.20
  confidence: 0.55
  provenance:
    source: inquiry.2026-04-12-ai-capex-thesis
    timestamp: 2026-04-12T00:00:00Z
  fuzz_halo: "model-efficiency breakthrough could compress timeline"
```

_(Themes accumulate as belief-Collapses land in the graph.)_
