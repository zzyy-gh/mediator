---
id: 2026-05-08-tech-sizing
shape: convergent
collapse_flavour: capital
status: open
scope: "Whether to scale tech allocation 18% → 25% NAV, or rebalance within sleeve"
parent_inquiry: null
graph_snapshot: snapshot.2026-05-08T09:00Z
outcome_window: 2026-08-08
sections:
  scope: ready
  assumptions: ready
  graph_refs: ready
  intent: ready
  self: ready
  m_nodes: ready
  prediction: ready
  outcome: locked
  reflection: ready
owner: human:zzyy
---

# Inquiry: Tech sector sizing under elevated vol

## Scope

Whether to scale equity tech allocation from 18% → 25% NAV, or rebalance within the existing 18% sleeve. Single-name selection within sleeve is in-scope; broader sector rotation is out-of-scope.

## Assumptions (load-bearing)

1. Q1 earnings dispersion is informative about Q2-Q3 (margin pressure carries across one quarter).
2. Prime-broker positioning ≈ true HF positioning (no major dark-pool offset).
3. Vol regime persists ±20% over the 3-month window (no major macro shock priced in).
4. Mandate permits up to 30% sector concentration without amendment.

## Graph references (from snapshot)

- `technicals.vol-regime` — VIX 22, 30d realized 19; lognormal median 21, IQR [18, 26].
- `fundamentals.tech-q1-earnings` — 68% beats, 22% guide-down; Q2 surprise N(0.01, 0.04).
- `flows.tech-positioning` — HF tech net long at 75th percentile.
- `macro.fed-stance` — pause; cut path data-dependent.
- `themes.ai-capex-cycle` — peak timing uncertain; 0.45 within 18mo.
- `portfolio.current` — 18% tech sleeve; factor exposure HML −0.4, MKT +1.1, MOM +0.3.
- `edges.crowding-to-drawdown` — P(forced unwind | sector dd >5%) ≈ 0.25.

## Intent

Move toward the portfolio with the highest E[R]/E[risk] available given current information. Confidence: 0.7.

## Self

- `self.capability` — 4 single-name tech convictions; no sector-level macro overlay.
- `self.calibration` — last 3 tech-sizing calls: +1, −1, +1; ≈ 0.55 on direction, ~0.4 on magnitude.
- `self.taste` — installed-base platforms; underweight thematic momentum.

## M-nodes (sequence)

1. `m.probe.scope` — sharpened from "size up tech" to "improve E[R]/E[risk] within tech exposure".
2. `m.probe.prior-art` — consulted `methods.md`. Factor exposure is already a tilt; size-up amplifies implicit factor bet.
3. `m.probe.world` — confirmed crowding via `flows.tech-positioning`.
4. `m.probe.edges` — walked `edges.crowding-to-drawdown`; conditional unwind probability material.
5. `m.reframe` — from "size up tech" to "concentrate within current sleeve in two highest-conviction names".
6. `m.test.feasibility` — capability ✓, constraint ✓, budget ✓ (no leverage). Pass.
7. `m.collapse` — capital commit: top 2 names 4% → 6% each, funded from low-conviction trim. Total tech sleeve unchanged at 18%.

## Output (convergent)

- **Expected return** (Δ vs alternative size-up to 25%): mean +30 bps over 3 months, sd 250 bps, slight positive skew.
- **Expected risk** (tech sleeve drawdown over 3 months): 90th pct ≈ 12%, 95th pct ≈ 18% reframed; ≈ 22% under size-up.
- **E[R] / E[risk]** (Δ mean / Δ 95th-pct drawdown):
  - Reframed: +30 / 180 ≈ 0.17.
  - Size-up unconditional: +50 / 220 ≈ 0.23.
  - Size-up conditional on unwind (P=0.25): −80 / 220 ≈ −0.36.
  - Probability-weighted size-up: 0.75·0.23 + 0.25·(−0.36) ≈ 0.08. **Reframed dominates once crowding-unwind probability is included.**
- **Sensitivity** — assumption 2 (positioning-data accuracy) is the brittle link. If crowding is overstated, size-up dominates.

## Outcome

_Pending. Fill on 2026-08-08._

- Realized state:
- Calibration delta:
- Edges affected:

## Reflection

The Reframe op was the value-add — it converted "size up tech" into a within-sleeve concentration once factor exposure and crowding were surfaced. Walking `edges.crowding-to-drawdown` did the heavy lifting. Candidate amendment: standardize an edge-walk step pre-Collapse for any sizing decision >2% NAV. Promote if the same pattern earns its keep across ≥3 inquiries.
