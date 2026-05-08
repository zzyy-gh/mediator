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

## Auto: feed.news-summarizer

<!-- BEGIN feed.news-summarizer -->
```yaml
```yaml
- id: politics.fomc_rate_path_may2026
  label: "FOMC rate decision trajectory post-Apr 29 statement"
  distribution:
    type: discrete
    outcomes:
      - label: hold_through_june
        probability: 0.55
        reasoning: "Two statements with no emergency language. Normal cadence = no urgency to move."
      - label: cut_25bp_june
        probability: 0.20
        reasoning: "Possible if March SEP showed dovish dots. No confirming signal in titles."
      - label: cut_50bp_june
        probability: 0.05
        reasoning: "Would require macro deterioration not visible in this feed."
      - label: hike_25bp_june
        probability: 0.05
        reasoning: "Unlikely given capital easing and no hawkish emergency signals."
      - label: hold_then_cut_h2
        probability: 0.15
        reasoning: "Gradual easing bias consistent with capital framework loosening."
  fuzz_halo: VERY HIGH — zero actual policy language in summaries; distribution is prior + cadence inference
  provenance:
    - url: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm
      timestamp: 2026-04-29
    - url: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260318b.htm
      timestamp: 2026-03-18

- id: politics.regulatory_deregulation_posture
  label: "Fed regulatory stance under current administration"
  distribution:
    type: discrete
    outcomes:
      - label: moderate_easing
        probability: 0.50
        reasoning: >
          Community bank leverage ratio eased. Capital framework "modernization."
          M&A approvals flowing. Enforcement terminations for major banks.
          Consistent with deregulatory tilt.
      - label: status_quo
        probability: 0.30
        reasoning: >
          Could be routine. Enforcement actions still issuing. "Maintain strength"
          language hedges against pure deregulation read.
      - label: significant_easing
        probability: 0.15
        reasoning: >
          If capital modernization NPR substantially reduces requirements,
          combined with leverage ratio changes = meaningful shift.
      - label: tightening
        probability: 0.05
        reasoning: "Contradicted by most signals but possible if capital NPR increases requirements."
  fuzz_halo: MEDIUM — directional signal clear but magnitude uncertain without proposal details
  provenance:
    - url: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260319a.htm
      timestamp: 2026-03-19
    - url: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260423a.htm
      timestamp: 2026-04-23
    - url: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20260409a.htm
      timestamp: 2026-04-09

- id: politics.fednow_intermediary_rule
  label: "FedNow intermediary access finalization"
  distribution:
    type: discrete
    outcomes:
      - label: finalized_with_minor_changes
        probability: 0.50
        reasoning: "Fed clearly wants broader adoption; proposal likely proceeds."
      - label: finalized_substantially_revised
        probability: 0.25
        reasoning: "Bank lobbying on intermediary liability/compliance could force revisions."
      - label: withdrawn_or_indefinitely_delayed
        probability: 0.10
        reasoning: "Low — Fed invested in FedNow success."
      - label: expanded_scope
        probability: 0.15
        reasoning: "Comments could push Fed to broaden beyond intermediaries to direct non-bank access."
  fuzz_halo: LOW-MEDIUM — proposal existence firm; outcome probabilities are standard rulemaking priors
  provenance:
    - url: https://www.federalreserve.gov/newsevents/pressreleases/other20260408a.htm
      timestamp: 2026-04-08
```

**Integrity notes:**
- Source feed = Fed press releases only. No market data, no FOMC statement text, no dot plot values. Sentiment means carry wide SDs for reason.
- Biggest gap: FOMC statement + SEP content unknown. Rate path node is near-uninformative — flag before downstream use.
- Enforcement terminations for Goldman/Crédit Agricole most actionable signal in batch — concrete regime change for those entities.
```
<!-- END feed.news-summarizer -->
