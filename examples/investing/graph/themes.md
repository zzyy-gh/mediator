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

## Auto: feed.news-summarizer

<!-- BEGIN feed.news-summarizer -->
```yaml
```yaml
- id: themes.payments_infrastructure_expansion
  label: "FedNow ecosystem broadening"
  status: developing
  arc: >
    Fed proposing intermediary access to FedNow — would let banks/CUs use
    third-party connectors instead of direct integration. Lowers barrier
    for small institutions. Signals Fed competing harder with private
    instant-payment rails (Zelle, RTP).
  assumptions:
    - FedNow adoption still below critical mass, motivating access expansion
    - Intermediary model implies Fed comfortable with delegated compliance layer
    - Public comment period = 6-12 month lag before implementation
  implications:
    - Positive for fintech intermediaries positioning as FedNow connectors
    - Competitive pressure on TCH/RTP network
    - Community banks gain instant payment capability without build cost
  fuzz_halo: LOW — proposal existence is fact; adoption inference is moderate confidence
  provenance:
    - url: https://www.federalreserve.gov/newsevents/pressreleases/other20260408a.htm
      timestamp: 2026-04-08

- id: themes.capital_framework_overhaul
  label: "Basel III endgame / capital modernization"
  status: active_rulemaking
  arc: >
    Agencies requesting comment on proposals to modernize regulatory capital
    framework while "maintaining strength." Likely next iteration of
    Basel III endgame after prior pushback. Dual framing (modernize + strength)
    suggests compromise approach.
  assumptions:
    - Prior Basel III endgame proposals drew significant industry opposition
    - "Modernize" implies reduced complexity or recalibration
    - "Maintain strength" is political cover — net capital impact likely neutral-to-lower
    - Community bank leverage ratio easing (Apr 23) is companion piece, carving out small banks
  implications:
    - Large bank capital requirements trajectory still uncertain
    - Community banks get relief regardless of large-bank outcome
    - Extended comment period = no final rule before late 2026 at earliest
  fuzz_halo: HIGH — "modernize" is maximally ambiguous without proposal text
  provenance:
    - url: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260319a.htm
      timestamp: 2026-03-19
    - url: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260423a.htm
      timestamp: 2026-04-23

- id: themes.enforcement_normalization
  label: "Post-crisis enforcement wind-down"
  status: mature
  arc: >
    Termination of enforcement actions against Goldman Sachs, Crédit Agricole,
    Mega International — legacy compliance issues resolved. Simultaneous
    routine individual employee actions (Ally, Regions, Equity, First Financial,
    United Bank, Community Bankshares) show enforcement still active but
    shifting from institutional to individual targets.
  assumptions:
    - Terminated actions were post-2008/post-AML era legacy items
    - Individual employee actions = fraud/misconduct, not systemic risk
    - Pattern suggests large-bank supervisory posture softening
  implications:
    - Reduced compliance burden for named large banks
    - No new systemic enforcement wave visible
  fuzz_halo: MEDIUM — termination reasons not in summaries; could be remediation or political
  provenance:
    - url: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260409a.htm
      timestamp: 2026-04-09
    - url: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260416a.htm
      timestamp: 2026-04-16
    - url: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260422a.htm
      timestamp: 2026-04-22
```
```
<!-- END feed.news-summarizer -->
