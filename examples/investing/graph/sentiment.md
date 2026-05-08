# Sentiment Nodes

Surveys, news tone, social signal, analyst tone, narrative momentum. Updated by sentiment feeds (LLM summarization or scored feeds).

## Example

```yaml
- id: sentiment.tech-narrative
  topic: sentiment
  content: "AI capex enthusiasm cooling but still positive net"
  distribution:
    shape: bounded
    params:
      range: [-1, 1]
      mean: 0.3
      sd: 0.2
  confidence: 0.5
  provenance:
    source: feed.news-summarizer
    timestamp: 2026-05-08T00:00:00Z
  fuzz_halo: "narrative-shift risk on next print"
```

_(Hydrate as feeds come online.)_

## Auto: feed.news-summarizer

<!-- BEGIN feed.news-summarizer -->
```yaml
```yaml
- id: sentiment.fed_policy_stance
  label: "Fed monetary policy stance"
  distribution:
    type: bounded_continuous
    range: [-1, 1]  # -1 = max dovish, +1 = max hawkish
    mean: 0.05
    sd: 0.25
  rationale: >
    Two FOMC statements (Mar 18, Apr 29) issued on normal cadence.
    No emergency actions. Discount rate minutes released routinely.
    Neutral-to-slight-hawkish prior — no cuts signaled but no tightening either.
  fuzz_halo: HIGH — summaries contain zero rate/guidance detail; mean is placeholder from cadence inference only
  provenance:
    - url: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm
      timestamp: 2026-04-29
    - url: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260318a.htm
      timestamp: 2026-03-18
    - url: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260318b.htm
      timestamp: 2026-03-18
    - url: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260414a.htm
      timestamp: 2026-04-14

- id: sentiment.bank_regulatory_climate
  label: "Bank regulatory environment tightness"
  distribution:
    type: bounded_continuous
    range: [-1, 1]  # -1 = max easing, +1 = max tightening
    mean: -0.15
    sd: 0.20
  rationale: >
    Mixed signals net slightly accommodative. Community bank leverage ratio eased (Apr 23).
    Capital framework modernization NPR (Mar 19) — direction unknown but "modernize" framing
    suggests simplification intent. Goldman/Crédit Agricole/Mega enforcement terminations
    signal resolved issues. Multiple individual enforcement actions routine, not systemic.
    M&A approvals flowing normally (OceanFirst, Burke & Herbert, BCP, Morgan Stanley 23A).
  fuzz_halo: MEDIUM — capital framework proposal could be tightening or easing; title alone ambiguous
  provenance:
    - url: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260423a.htm
      timestamp: 2026-04-23
    - url: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260319a.htm
      timestamp: 2026-03-19
    - url: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260409a.htm
      timestamp: 2026-04-09

- id: sentiment.bank_ma_activity
  label: "Bank M&A approval flow"
  distribution:
    type: bounded_continuous
    range: [-1, 1]  # -1 = frozen, +1 = wide open
    mean: 0.25
    sd: 0.15
  rationale: >
    Four approval/order items in 5-week window. Domestic (OceanFirst, Burke & Herbert),
    cross-border (Banco de Credito del Peru), and special exemption (Morgan Stanley 23A).
    Healthy pipeline. No denials visible.
  fuzz_halo: LOW — approvals are binary facts
  provenance:
    - url: https://www.federalreserve.gov/newsevents/pressreleases/orders20260424a.htm
      timestamp: 2026-04-24
    - url: https://www.federalreserve.gov/newsevents/pressreleases/orders20260424b.htm
      timestamp: 2026-04-24
    - url: https://www.federalreserve.gov/newsevents/pressreleases/orders20260410a.htm
      timestamp: 2026-04-10
    - url: https://www.federalreserve.gov/newsevents/pressreleases/orders20260326a.htm
      timestamp: 2026-03-26
```
```
<!-- END feed.news-summarizer -->
