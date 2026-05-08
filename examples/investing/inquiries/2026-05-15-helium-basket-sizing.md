---
id: 2026-05-15-helium-basket-sizing
shape: convergent
collapse_flavour: capital
status: open
scope: "Sizing decision for helium pure-play basket + APD anchor under Type B archetype."
parent_inquiry: 2026-05-08-type-b-screen-v2
graph_snapshot: 2026-05-08T09:00Z
outcome_window: 2027-05-15
sections:
  scope: ready
  assumptions: ready
  graph_refs: ready
  intent: ready
  self: ready
  m_nodes: ready
  prediction: ready
  outcome: locked
  reflection: locked
owner: agent:either
---

# Inquiry: Helium basket sizing

## Scope

Decide capital allocation to helium sleeve. Vehicles: PLSR.V / DME.V / HE.V (microcap pure-plays, basket capped 1-2% NAV), APD (Air Products) as institutional-grade anchor. Surprise candidate from v2 Type B screen. Demand drivers: zero-substitution medical (MRI quench), semiconductor dry-etch, fiber-draw cooling. Supply bottleneck: 2024 BLM Federal Helium Reserve sale + Amur-2 ramp problems + geological scarcity. Microcap liquidity is gating constraint, not thesis quality.

In scope: pure-play basket sizing under microcap liquidity discipline, APD sizing as anchor, sensitivity to substitution/recycling, drawdown.
Out of scope: helium futures (no liquid contract), helium-3 separate market.

## Assumptions (load-bearing)

1. **Zero-substitution medical demand floor (MRI quench).** Installed-base MRI fleet (~50,000 units globally) requires periodic helium top-up + new-system fill; helium has no substitute below ~4K (superconducting magnet quench). Demand from medical cryogenics ~30% of total He market and price-inelastic on the timescale of this inquiry. Failure: large-scale rollout of "low-helium" or sealed-magnet MRI architectures (Philips BlueSeal, Siemens DryCool) replaces enough installed base within 24mo to break the demand floor narrative. Confidence 0.75; resolves on OEM platform-mix prints + hospital procurement surveys.

2. **Semiconductor demand growth (dry-etch + leak-test) tracks leading-edge node count.** Helium consumption per wafer rises with each node shrink (more etch + cooling + leak-test steps per layer); AI-driven leading-edge capex (TSMC N2 / Intel 18A / Samsung GAA) implies semi helium demand grows 6-9% YoY through 2027. Failure: AI-capex peaks inside 18 months (S4 in scenario set, p=0.20) and wafer-start growth flatlines — semi helium demand decel to ~2% YoY. Confidence 0.55 (linked to `themes.ai-capex-cycle` distribution).

3. **Fiber-draw cooling demand sustained by datacenter + 5G/6G buildout.** ~15% of He demand is fiber-optic draw (helium atmosphere prevents bubble defects). Hyperscaler optical interconnect + long-haul fiber refresh + 5G fronthaul keep fiber demand growing 3-5% YoY through 2027. Failure: hollow-core / air-cooled fiber draw process commercialised at scale → demand floor for this segment weakens. Confidence 0.60.

4. **BLM Federal Helium Reserve post-sale supply impact is structurally durable through 2027.** The 2024 BLM auction transferred reserve assets to private operators (primarily Messer); the buffer-of-last-resort that absorbed ~10% of US demand for two decades is gone. Crude helium spot has run 2-3x since 2023; private operators cannot replicate buffer behaviour because they face commercial-return constraints. Failure: if private operators behave as quasi-buffer (regulator pressure, long-term contract obligations) the supply tightness eases. Confidence 0.70; resolves on Messer / private-operator inventory disclosures.

5. **Amur-2 (Gazprom) ramp delay persists through 2027.** The Gazprom Amur-2 helium plant (designed nameplate ~60 mmcf/yr, ~25-30% of global capacity at full ramp) has missed every milestone since 2022 — fire damage 2023, sanctions on equipment, repeated production-pause announcements through 2025. Western OEM equipment reliance + sanctions regime makes a clean ramp implausible inside 24mo. Failure: rapid Russia-China commissioning workaround (Chinese cryogenic equipment substitution) brings nameplate online 2026-2027. Confidence 0.65; resolves on Gazprom production filings + Chinese cryogenic-OEM export disclosures.

6. **Qatar / Algeria capacity expansion is incremental, not buffer-replacing.** RasGas Helium-2/3 (Qatar) operates near nameplate but cannot expand without LNG-train debottlenecking; Skikda (Algeria) is reliable at ~2 bcf/yr but capex commitments for expansion are absent through 2027. Combined Middle East / North Africa supply growth is in low single digits, not enough to replace BLM + Amur shortfall. Failure: Qatar announces a third helium plant tied to North Field expansion (possible 2026-2027) — would price in 18-24mo before commissioning. Confidence 0.65.

7. **Helium recovery / recycling adoption is slow and partial.** On-site liquefaction recovery in semi fabs + MRI helium-recovery systems exist but adoption lags because capex / opex tradeoff vs purchased helium is marginal at <$300/Mcf wholesale and only crosses the line at $400+/Mcf sustained. Penetration <30% of installed base by 2027. Failure: a step-change in low-cost recycling tech (e.g., membrane-based mass-market recovery) accelerates adoption to >50% — cuts net demand growth in half. Confidence 0.65; this is the most thesis-fragile demand assumption.

8. **Microcap junior execution risk: geological discovery vs production gap is binding.** PLSR.V (Topaz, Minnesota — drilled but pre-production), DME.V (Holbrook Basin, Arizona — operating but small), HE.V (small Saskatchewan + Montana). Conversion of resource-on-paper to producing-and-cashflowing is the failure-point for ~70% of mining/extraction juniors historically (industry base rate). Single-asset, single-jurisdiction, microcap balance-sheet fragility, dilution-financing risk. Confidence 0.40 that any individual name reaches sustained positive cashflow inside 24mo; basket-level confidence ~0.70 that *at least one* converts.

9. **Recognition latency is asymmetric by vehicle.** Microcap basket recognition fires on first-major-offtake-contract or M&A (typical 12-30mo); APD anchor recognition fires on contract-renewal pricing flowing through industrial-gas margins (typical 6-18mo, smoother).

10. **Drawdown bound is 12-24mo worst-plausible.** Microcap basket -65% bounded at drilled-resource value at $200/Mcf (vs spot $400+) plus net cash; full-write-down possible on any single name (-90 to -100%) — basket diversification across 3 names mitigates but does not eliminate. APD -15% bounded by diversified industrial-gas earnings + dividend yield support.

**Feed-gap promotions to assumption (per `amendments.md` 2026-05-08 discipline):**

11. **No commodities futures-curve feed → helium spot/contract pricing approximated by industry-press spot prints + Linde/APD/Air Liquide earnings-call commentary.** No liquid futures exist for helium; price discovery is bilateral-contract-driven. Confidence haircut 0.20 on price-path forecasts. Resolves only if a private/exchange spot reference emerges (low probability inside outcome window).

12. **EDGAR stub → ex-US (Canadian / TSX-V) microcap filings unavailable in feed; rest on web_search of SEDAR.** Confidence haircut 0.25 on PLSR.V / DME.V / HE.V balance-sheet stress, dilution overhang, drilling progress validation. Resolves when EDGAR feed is extended to SEDAR or replaced.

13. **No flows / positioning feed → Canadian microcap basket positioning is unobservable.** Microcap reflexivity (retail flow, junior-mining-newsletter pump-dump cycles) is structurally invisible. Confidence haircut 0.25. Resolves on flows feed registration (architecture A3).

14. **FRED feed missing → real-rate sensitivity of long-duration microcap junior cashflow approximated by `macro.cfx_tlt` proxy.** Microcap juniors are duration-sensitive (negative cashflow now, positive later). Confidence haircut 0.20 on discount-rate path. Resolves when FRED hydrates.

## Graph references

Pulled from snapshot 2026-05-08T09:00Z (parent v2 + portfolio-architecture node):

**Strategy / portfolio:**
- `strategy.type-b.current_candidates_v2[rank=7]` — helium pure-plays + APD anchor; this inquiry is the child sizing.
- `strategy.portfolio-architecture.scenario_set` — helium wins in S2 (stagflation, p=0.18, real-asset bid), S5 (geopolitical, p=0.10, Russia-supply-shock leg amplified), partially S6 (reflation, p=0.08, semi capex re-accel). Holds in S1 (soft landing + AI capex extends, p=0.22, semi demand intact). Loses partially in S3 (recession, p=0.14, semi capex pause but medical floor holds) and S4 (AI capex peak <18mo, p=0.20, semi demand decel). Cumulative helium-positive scenario weight ≈ 0.50 (S1+S2+S5+S6); negative weight ≈ 0.34 (S3+S4); neutral ≈ 0.08 (S7); tail S8 ≈ 0.02 (microcap basket drawdown extreme).
- `strategy.portfolio-architecture.balance_assessment.concentrations` — helium adds to "supply-bottleneck industrial cluster" (REE + uranium + silver + grid + tankers + helium). Cluster cap context: REE 1.5% + uranium 4% + silver 4% = 9.5% Type B NAV; helium adds incrementally — sizing must respect cluster cap and avoid pushing the cluster total beyond an inferred 15-18% ceiling.
- `strategy.portfolio-architecture.holes.H1` — "no explicit tail hedge"; APD anchor partially serves as a quality-industrial defensive within the helium thesis (dividend-paying, diversified industrial gases) but does not close H1 broadly.

**Themes:**
- `themes.ai-capex-cycle` (p_peak_18mo 0.45 / p_18-36mo 0.35 / p_no_peak 0.20, conf 0.55) — load-bearing on semi-demand leg (assumption 2). The 0.45 weight on peak-within-18mo is the largest single-scenario haircut on this thesis. Critically: helium thesis is *less AI-capex-leveraged than grid/uranium* because the medical demand floor (assumption 1) is independent. Even if AI capex peaks, medical + fiber + leak-test pillars persist.

**Macro:**
- `macro.cfx_dbc` 30.25 — broad-commodity tape mid-vol; supportive backdrop for industrial-bottleneck thesis.
- `macro.cfx_tlt` 85.65 — duration / real-rate proxy (FRED-substitute); microcap junior duration sensitivity (assumption 14).
- `macro.cfx_uup` 27.41 — DXY steady; modest USD headwind absent.

**Technicals:**
- `technicals.spy` 731.58, vol 15.94% — broad-market regime mid-vol; tolerable backdrop for microcap-basket entry.
- `technicals.eem` last 66.59, vol 28.7% — EM tape live (relevant if Russia-supply-disruption scenario triggers helium re-pricing flows).

**Politics:**
- `politics.us-china-tariff-regime-2026` (escalation 0.35) — secondary-relevant; helium is not on tariff lists currently but Russia-supply leg is sanctions-conditional.
- No direct helium-policy node; Russia/Gazprom sanctions regime carried as background.

**Edges (relevant):**
- `edge.crowding-to-drawdown` — Canadian microcap basket positioning unobservable (assumption 13). Junior-mining sentiment cycles are reflexive and steep; cannot locate position on curve.
- Implicit edge candidate: `themes.ai-capex-cycle` → semi-helium demand (medium-strength, latency 1-2 quarters); could land as first-class edge via this inquiry's belief residue.

**Graph gaps actively limiting confidence (per amendments discipline):**
- No commodities futures-curve feed → assumption 11 (price-path forecast haircut 0.20).
- EDGAR stub for SEDAR microcaps → assumption 12 (balance-sheet haircut 0.25).
- No flows feed → assumption 13 (microcap reflexivity blind, haircut 0.25).
- FRED missing → assumption 14 (duration sensitivity haircut 0.20).

## Intent

Output sizing recommendation for helium sleeve, split between microcap basket (PLSR.V / DME.V / HE.V) and APD anchor, with E[R]/E[risk] for each leg, total sleeve NAV %, and brittle assumption + threshold. Confidence on Collapse recommendation: medium-low (0.50) — thesis quality is high but microcap data thinness and price-discovery opacity (no futures curve) cap confidence on precise sizing. Confidence higher (0.70) on the directional verdict that helium passes the "size something" gate at small NAV %; lower (0.40) on precise basket allocation among PLSR/DME/HE.

## Self

- **self.capability** — Vehicle-agnostic convergent sizing. Can run scenario-weighted return calc, drawdown bound from drilled-resource-floor logic for juniors and earnings-floor for APD, asymmetry ratio. Cannot compute live factor regression vs portfolio (no broker feed → portfolio.current empty); cannot price options-implied tail (no CBOE feed); cannot validate microcap balance-sheet stress directly (no SEDAR ingestion). Web_search available for Pulsar/Desert Mountain/Total Helium operating updates, BLM auction post-mortems, Amur-2 status, RasGas / Skikda capacity prints, OEM low-helium MRI rollout.
- **self.calibration** — No prior closed Type B sizing inquiries on this instance; no helium track record. Inherit parent's base-rate: Type B disciplined-screen hit-rate 0.30-0.40, payoff multiple on hits 3-8x. Apply additional haircut for microcap junior conversion-risk base rate (~30% reach sustained cashflow) — this is a structurally lower-confidence sleeve than silver or uranium even though thesis quality is comparable.
- **self.taste** — **Strong constraint flagged: high microcap-jurisdictional-risk taste constraint.** Bias against any single-name microcap exceeding 0.7% NAV; bias toward basket-only construction for the pure-play leg; bias toward APD-anchor-heavy mix when the demand-deduction chain is real-asset and the junior equities add operational + dilution + jurisdictional risk on top of commodity exposure. Bias against pure-play sleeve >2% NAV under any circumstance — a full write-down on the microcap basket should not move book P&L by more than ~1.5%. Bias toward respecting drawdown bounds *strictly under tail-risk*: assumption 10 admits -90 to -100% on individual juniors; sizing must internalise that. Bias against narrative-seduction on "next big helium discovery" — apply boring-story test: would I size this if the geological story were dull? If yes, only because the supply-side bottleneck (assumption 4-6) is independent of any single junior's success.

## M-nodes (sequence)

1. `m.probe.scope` — sharpened: convergent sizing, single Collapse output (capital), microcap basket + APD anchor split, with sensitivity. Out-of-scope held: helium futures (none liquid), He-3 separate market.
2. `m.probe.prior-art` — `methods.md` (Kelly with heavy haircut for microcap, drawdown bound, scenario stress, factor-exposure check); `blind-spots.md` (narrative seduction — boring-story test on helium juniors; tail neglect — full-write-down risk on single names; recency — last 12mo helium spot run-up; implicit factor — helium as semi/AI-capex tilt in disguise; survivorship — only-surviving juniors visible in current candidate pool); `strategies.md` Type B drawdown-bounded criterion; `amendments.md` 2026-05-08 factor-coverage and feed-gap-to-assumption disciplines applied throughout.
3. `m.probe.world` — graph snapshot read; web_search supplements: Messer / Linde / APD industrial-gas earnings-call helium commentary 2024-2026, BLM auction post-mortem analyses, Gazprom Amur-2 production filings + sanctions-equipment-supply-chain analyses, Pulsar Topaz drilling updates, Desert Mountain quarterly production, Total Helium Saskatchewan operations, RasGas / Skikda nameplate status, Philips BlueSeal / Siemens DryCool MRI rollout pace, semi fab helium-recovery adoption surveys.
4. `m.probe.edges` — **factor-coverage walk per amendments 2026-05-08 discipline:**
   - **macro (rates, growth, inflation, fiscal)** — duration sensitivity moderate (junior negative-cashflow now, levered to discount rate); FRED missing → assumption 14 with 0.20 haircut. Inflation regime supportive. Fiscal posture not load-bearing.
   - **geographic (jurisdiction, sanctions, trade)** — PLSR.V (Minnesota, US — favourable); DME.V (Arizona, US — favourable); HE.V (Saskatchewan + Montana — favourable). APD (US-listed, global ops). Russia sanctions regime affects supply (assumption 5) — supportive of thesis, not exposure. Qatar / Algeria stable. Microcap-jurisdictional risk is *low for this basket vs other resource juniors* — this is one of the relatively cleaner geographic profiles in the Type B candidate set.
   - **regime (vol, liquidity, dispersion)** — microcap vol high (PLSR/DME/HE individual vol >70% annualised typical); liquidity *poor* — daily $ volume on PLSR.V <$200k typical, DME.V similar, HE.V thinner. **This is the binding constraint per scope statement.** APD vol moderate (~22% annualised), liquidity ample. Dispersion across the basket is high — PLSR is pre-production, DME is producing, HE is exploration-tilted.
   - **correlation structure** — helium juniors correlate weakly to broad market (junior-mining-cycle dominant); APD correlates to industrial-gas peers (Linde, Air Liquide). Implicit factor bet: APD helium leg is a fraction of total APD revenue (~5-8%); APD position is mostly an industrial-gas-quality-anchor bet, not a pure helium bet — sizing must reflect that the leverage to helium thesis is much lower per dollar than the basket. **No double-counting of AI-capex factor**: helium thesis touches semi capex but the medical + fiber demand floors mean the per-dollar AI-capex factor loading is lower than for grid/uranium/REE.
   - **flows (positioning, crowding)** — H3 hole, assumption 13 with 0.25 haircut. Microcap junior flows particularly invisible.
   - **themes (narrative state, recognition stage)** — helium is *under-recognised* relative to thesis quality. Mainstream press has covered BLM sale + price spikes 2024-2025 but pure-play vehicle universe is thin and ignored. Recognition triggers: PLSR first major offtake announcement (Linde / APD / Air Liquide), DME quarterly production beat, M&A roll-up of pure-plays by majors, helium spot break >$500/Mcf sustained.
   - **reflexivity** — recognition reflexive: contract awards → cashflow → multiple expansion → secondary offerings deploy expansion capex → more production. Microcap dilution risk is real on the upside path (juniors typically issue equity to fund production ramps).
   - **liquidity / capacity** — **gating constraint.** Microcap basket cap 1-2% NAV total is a hard ceiling driven by exit-cost math, not Kelly. Realistic max single-name position $50k-$200k without moving market; basket of 3 names = $150k-$600k workable. APD has unlimited practical capacity for any reasonable book.
5. `m.reframe` — None. Scope held; sizing decision is right shape for Type B child convergent capital Collapse. Microcap-liquidity discipline forces a non-Kelly-derived sizing — accepted as binding upstream constraint, not a Reframe trigger.
6. `m.test.feasibility` — capability (sizing math executable) × constraint (drawdown bounds quantified incl. -100% tail on individual juniors) × budget (NAV % proposed within mandate-implicit cap and microcap-liquidity-implicit cap) × data-quality (medium-low; four feed gaps promoted to assumptions with explicit haircuts; SEDAR/EDGAR particularly thin). Feasibility: PASS for APD anchor; PASS-WITH-DISCIPLINE for microcap basket (size respects -100% single-name tail at basket level, not point-Kelly). Confidence haircut applied to final sizing.
7. `m.collapse` — capital: open helium sleeve at recommended NAV %, anchor-heavy split, with sensitivity threshold pre-registered as auto-resize trigger. Belief residue: candidate first-class edge `themes.ai-capex-cycle → semi-helium-demand` to land on Collapse.

## Prediction (convergent)

### Expected return — distribution sketch

Scenario-weighted, conditional on graph snapshot. Drawing on `strategy.portfolio-architecture.scenario_set`:

**12-month return distribution — microcap basket (PLSR.V + DME.V + HE.V, equal-weight at entry):**
- S1 (soft landing + AI capex extends, 0.22): -10% to +60%, mean +20% (semi demand intact, no recognition trigger guaranteed)
- S2 (stagflation lite, 0.18): +20% to +120%, mean +60% (real-asset bid + supply-bottleneck recognition)
- S3 (recession + faster cuts, 0.14): -45% to +10%, mean -25% (semi capex pause, junior-financing tightens, dilution risk fires)
- S4 (AI capex peak <18mo, 0.20): -35% to +20%, mean -10% (semi demand decel; medical/fiber floor partially compensates)
- S5 (geopolitical, 0.10): +30% to +200%, mean +90% (Russia supply shock amplifies pure-play thesis)
- S6 (reflation surprise, 0.08): +15% to +100%, mean +50% (semi capex re-accel)
- S7 (status quo drift, 0.06): -25% to +15%, mean -10% (no recognition trigger fires; junior bleed)
- S8 (tail / fat-left, 0.02): -70% to -40%, mean -55% (microcap drawdown extreme; financing window shut)

Weighted mean E[R] (12mo, basket) ≈ +17%
Weighted SD ≈ 55%
Approx quantiles (12mo, basket): P10 ≈ -45%, P50 ≈ +5%, P90 ≈ +90%

**12-month return distribution — APD anchor:**
- APD trades as quality industrial-gas; helium is ~5-8% of revenue but contract-renewal pricing flows through faster than mix implies (helium contracts are short-cycle vs LNG/atmospheric gases).
- S1: 0% to +15%, mean +7%; S2: +5% to +25%, mean +14%; S3: -15% to +5%, mean -5%; S4: -10% to +10%, mean +0%; S5: +5% to +20%, mean +12%; S6: +5% to +20%, mean +12%; S7: 0% to +10%, mean +5%; S8: -25% to -10%, mean -18%.
- Weighted mean E[R] (12mo, APD) ≈ +5.5%
- Weighted SD ≈ 11%
- Quantiles: P10 ≈ -10%, P50 ≈ +5%, P90 ≈ +18%

**24-month return distribution — basket:**
- Recognition window assumption 9 (12-30mo) implies bull paths largely realise across years 1-2 with M&A optionality. Junior conversion-risk (assumption 8) means basket-level outcome is bimodal: hits 3-5x; misses -50 to -100%.
- E[R] (24mo, basket) ≈ +35% (haircut for assumption 8 base rate already inside the bimodal mean)
- SD ≈ 90%
- Quantiles (24mo, basket): P10 ≈ -55%, P50 ≈ +10%, P90 ≈ +180%

**24-month return distribution — APD:**
- Helium contract-renewal cycle fully expressed by 24mo; multi-year capex bottleneck thesis priced into industrial-gas margins.
- E[R] (24mo, APD) ≈ +14%
- SD ≈ 18%
- Quantiles: P10 ≈ -10%, P50 ≈ +12%, P90 ≈ +38%

### Expected risk — drawdown distributions

**Microcap basket — 12mo drawdown:**
- Max plausible drawdown under thesis-failure (semi capex peak + Amur-2 ramp surprise + recycling acceleration + dilution shock): -65% basket-level (per parent screen + assumption 10).
- P(drawdown >25%) ≈ 0.45
- P(drawdown >45%) ≈ 0.25
- P(drawdown >65%) ≈ 0.10 (basket drawdown floor at drilled-resource value $200/Mcf + net cash)
- **Tail (single-name -100%)**: ≈ 0.20 chance of *any one of three* names full-writing-down inside 24mo (junior conversion-risk base rate). Basket diversification: P(all three full write-down) ≈ 0.05; P(at least one survives + delivers >2x) ≈ 0.55.
- Tail (basket >75% drawdown): ≈ 0.05 (would require simultaneous Amur-2 ramp + recycling step-change + financing-window-shut)

**APD anchor — 12mo drawdown:**
- Max plausible drawdown: -15% (per parent screen).
- P(drawdown >5%) ≈ 0.40
- P(drawdown >10%) ≈ 0.18
- P(drawdown >15%) ≈ 0.06 (capped by diversified industrial-gas earnings + dividend-yield support ~2.5%)
- Tail (drawdown >25%): ≈ 0.02 (would require broad industrial-gas recession + helium thesis collapse simultaneously)

### E[R] / E[risk] ratio

Define E[risk] = expected drawdown magnitude over 12mo (probability-weighted negative tail).

- **Microcap basket:** E[R] +17% / E[risk] ~22% = **0.77**
- **APD anchor:** E[R] +5.5% / E[risk] ~3.5% = **1.57**
- **Blended (recommended split below, ~67% anchor / 33% basket by NAV):** E[R] ~+9% / E[risk] ~9% = **1.0**

Type B archetype rough hurdle for sizing = 1.5; **APD anchor clears comfortably; microcap basket fails the standard hurdle on E[R]/E[risk] alone but passes on convex-asymmetry payoff structure** (P90 +90% basket vs P10 -45% basket = ~2:1 asymmetry, with tail optionality on M&A / discovery upside that Kelly-style E[R]/E[risk] understates). Blended sleeve sits at the hurdle, justified only by the convex-tail argument on the basket leg + the anchor-quality of APD. **This is a deliberately marginal sleeve — sizing reflects that.**

### Sensitivity — brittle assumption + threshold

**Most brittle: Assumption 7 (helium recovery / recycling adoption rate slow).**

If a step-change recycling technology (membrane-based mass-market recovery, or a major OEM low-helium MRI platform reaching >30% installed base inside 24mo) compresses net demand growth by half, the supply-bottleneck thesis loses its near-term price-tightness — helium spot retraces 30-50% from current $400+/Mcf, microcap pure-play valuations re-rate down sharply (-40 to -65% basket), and APD margin uplift fails to materialise (helium leg contributes 0% rather than +3pp to APD revenue growth). E[R]/E[risk] on the basket collapses to <0.3; APD ratio compresses to <1.0.

**Why assumption 7 over 4 (BLM) or 5 (Amur)**: BLM and Amur are *current-state observable* — supply tightness is in spot prints. Recycling/substitution is the only path that breaks the thesis from the *demand* side, and demand-side breaks are harder to monitor real-time than supply-side. Also: assumptions 4 + 5 are partially redundant (either alone is sufficient for tightness); assumption 7 is the only single-point-of-failure that breaks both the supply-tightness *and* the demand-growth legs simultaneously.

**Threshold for auto-resize trigger (registered with this Collapse):**
- Helium spot retraces below $300/Mcf for two consecutive months → halve microcap basket.
- Tier-1 MRI OEM (Philips / Siemens / GE) announces >$500m platform investment in low-helium architecture → halve basket; trim APD by 25%.
- Membrane-based helium recovery announcement at any tier-1 semi fab (TSMC / Intel / Samsung) → halve basket.
- Gazprom Amur-2 announces >50 mmcf/yr sustained production for 2 quarters → halve basket; hold APD.
- Any single microcap basket name draws down >50% from entry → liquidate that name; do NOT rebalance into the other two (single-name failure ≠ basket failure but redistribution is over-confident per assumption 8).
- AI-capex-cycle theme distribution shifts to peak_within_18mo > 0.65 (currently 0.45) → halve basket; trim APD by 15%.

**Second-tier sensitivity:** Assumption 8 (microcap junior execution risk). Already internalised in basket sizing via single-name caps and basket diversification, but a coordinated dilution event (two of three names doing simultaneous secondary offerings inside 6 months) would signal industry-wide funding stress — halve basket and reframe.

### Sizing — NAV % + basket vs anchor split rationale

**Recommended sleeve size: 4.5% NAV total (range 3.5-5.5%, confidence 0.50).**

**Split: 1.5% basket / 3.0% APD anchor (≈33% / 67%).**
- **Microcap basket: 1.5% NAV total** (within parent screen's 1-2% basket cap, sized at the conservative end given assumption 8 base-rate + feed-gap haircuts).
  - PLSR.V: 0.6% (cleanest pure-play, Topaz drilled, US jurisdiction, highest single-name confidence among basket).
  - DME.V: 0.6% (only operating producer, demonstrated cashflow path, smallest dilution risk).
  - HE.V: 0.3% (most exploration-tilted, highest conversion risk; minority weight).
- **APD anchor: 3.0% NAV** (institutional-grade industrial gas with diversified business, dividend support, modest helium-thesis leverage; sized to absorb thesis-failure path -15% as ~0.45% NAV impact on book).

**Total sleeve drawdown stress: full-write-down basket (-100%) + APD thesis-fail (-15%) = -1.5% - 0.45% = -1.95% NAV impact.** Inside the implied Type B per-thesis tolerance.

**Sizing derivation (Kelly with heavy haircut, sanity-checked by drawdown bound + microcap liquidity cap):**
- **Microcap basket fractional Kelly:** edge ~0.17 / vol² ~0.30 → 0.57x; quarter-Kelly ~0.14 of NAV at face. **Liquidity cap binds** before Kelly: realistic exit-cost-aware position is 1.5-2% NAV total. Apply assumption-8-haircut for microcap conversion risk (0.40 base survival probability) → effective recommended size ≈ 1.5%. Liquidity cap is the binding constraint, not Kelly.
- **APD fractional Kelly:** edge ~0.055 / vol² ~0.012 → 4.6x (low-vol, modest-edge → mathematically wants size). Quarter-Kelly ~1.15x of NAV — clearly absurd at face (concentration risk). Apply mandate-implicit anchor cap (no single anchor >5% NAV) and Type B-cluster cap from `strategy.portfolio-architecture.proposed_adjustments.A6` → 3.0% NAV.
- Total 4.5% sits inside an inferred Type B per-thesis cap of ~5% (no formal mandate cap yet — H8 hole in architecture; flagged).

**Anchor-heavy rationale:**
- Assumption 8 (microcap junior execution risk) means single-name full-write-down is in the realised distribution at ~0.20 per name over 24mo. Anchoring through APD captures the thesis without that tail.
- Feed gaps (assumptions 11-14) collectively bias toward institutional-grade vehicle that absorbs data-thinness via diversification. APD's helium leg may contribute only ~3-8% of revenue but the *information ratio per dollar deployed* is higher than the basket given data-quality.
- Microcap liquidity (regime probe) is poor — exit-cost math caps basket at <2% regardless of Kelly.
- Drawdown bound asymmetry: basket -65% (and -100% single-name tail) is substantially wider than APD -15%; sizing should reflect the asymmetry, not the central E[R] estimate.

**Why not zero basket exposure:** The *convex-tail upside* from microcap recognition / M&A / discovery-revaluation is uncapturable through APD alone. APD captures the helium contract-pricing leg cleanly; only the pure-plays capture the supply-discovery and recognition-rerating legs. Holding 1.5% in the basket preserves exposure to the +90% to +200% upper-tail scenarios (S2 + S5 + S6 combined weight 0.36) that justify the entire Type B archetype's existence on this thesis. Zero-basket would convert this from a Type B speculative bet into a Type A quality-anchor position with weak helium-leverage.

**Cluster check:** Sleeve adds to "supply-bottleneck industrial cluster" alongside REE 1.5% + uranium 4% + silver 4% = 9.5% Type B NAV pre-helium. Adding 4.5% helium → 14.0% cluster total. Inside the inferred 15-18% cluster ceiling, but **this cluster is approaching its discipline cap**. Subsequent Type B sizing (phosphate, EU defense, India infra, tin, lithium, frontier sov, JGB) must explicitly reduce or compete against this allocation; flag for the architect on Collapse to enforce A6 (cluster sizing discipline) before further Type B child-inquiry capital Collapses fire.

**Hedge note:** APD anchor itself partially serves as a quality-defensive within the helium thesis (dividend-paying, diversified industrial-gas earnings). Does not close H1 (no explicit tail hedge) at the portfolio level; defers to A1 child inquiry. The basket is *not* a hedge for anything — it is a convex-tail bet sized to be losable.

**Adversarial probe acknowledgement:** A parallel adversarial-probe inquiry is running on this thesis (likely targeting: substitution rate, OEM low-helium MRI roadmap aggressiveness, Qatar third-train probability, Amur-2 Chinese-OEM workaround, microcap dilution-cycle base rates). Findings will reconcile post hoc and may trigger one of the sensitivity thresholds above. This Collapse-recommendation represents best-effort priors; user gates the actual capital deployment with the adversarial-probe output in hand.

## Reconciliation (deep-dive vs adversarial probe + base-rate screen)

Reconciles `2026-05-15-helium-basket-sizing` (this file, deep-dive sizing) against `2026-05-08-helium-adversarial-probe.md` (devil's-advocate artifact) under the discipline of the 2026-05-08 amendment "story-stock / fraud / overinflation screen." Status remains `open`; sizing recommendation revised below.

### A. Assumption-set reconciliation

**Assumption 1 (zero-substitution medical demand floor, 0.75 → 0.45).** Probe's central insight: the deep-dive's framing was a *stock* claim (installed base of ~50,000 MRIs needs ongoing helium); the *flow* — marginal new + upgrade installs — has already inflected. BlueSeal-class + GE Helium-Zero + Philips Helium-Free at >55% of new high-field DM installs by 2026, with new-unit first-fill ~5-10% of legacy and a quench-loop top-up ~order-of-magnitude smaller. The claim "demand from medical cryogenics is price-inelastic on the timescale of this inquiry" is still *narrowly* true for the existing fleet (2-7 yr top-up cadence on legacy magnets), but the medical *growth* leg is structurally negative through the recognition window, not flat. The deep-dive priced this as a 24-mo-failure-mode ("if low-helium MRI gets to >30% of installed base"); the probe shows the failure mode has fired on *flow* already. **Confidence collapses 0.75 → 0.45.** The "demand floor" survives only as a slowly-depleting stock rather than as a price-supportive growth pillar; that's a much weaker leg than the deep-dive priced.

**Assumption 7 (helium recovery / recycling adoption slow, 0.65 brittleness → ~0.30 brittleness, i.e. failure largely realised).** The deep-dive flagged this as the most thesis-fragile demand assumption with a 0.65 confidence that adoption stays slow. Probe documents that recycling/substitution is not "future risk" but happening now: Lam/TEL argon-dominant cooling recipes (2022+), Corning/Sumitomo nitrogen-helium hybrid fiber-draw (-40 to -60% per km), helium intensity per leading-edge wafer declining ~3-4%/yr, MRI cryogen-recycling ramp on new builds. The brittle-event probability in the 12-24mo window rises materially — call it 0.55-0.65 that "step-change recycling/substitution" is far enough along to compress net helium demand growth by half through 2027, vs the deep-dive's implicit ~0.20-0.30. **The trigger condition for the deep-dive's "halve basket" auto-resize is closer to already-met than to a future contingency.**

**Assumption 2 (semi demand growth, 0.55 → 0.40).** Argon/krypton substitution at 0-15% process penalty + neon (not helium) for EUV pellicle/stage purge means the AI-capex narrative the deep-dive partially leaned on is mis-targeted at the wrong noble gas. Helium intensity per wafer is *declining* even as wafer-starts grow. AI-capex factor loading per dollar deployed in the helium thesis is therefore lower than the deep-dive's edge probe assumed.

**Assumption 4 (BLM buffer eliminated → structurally durable supply tightness, 0.70 → 0.50).** Probe correctly notes the molecules still flow under Messer; "buffer eliminated" is a rhetorical frame, not a flow-reduction. Tightness requires private operators not behaving as quasi-buffer; with 2027-window glut risk live, Messer has commercial-return incentive to *accelerate* monetisation, not hoard. Mildly bearish revision.

**Assumption 5 (Amur-2 ramp delay through 2027, 0.65 → 0.45).** Probe reports Amur-2 Train 2 at ~50-60% nameplate by Q1 2026; Train 3 on track 2027. This is a materially less-delayed picture than the deep-dive priced. Even if Western-market access remains constrained, fungibility (Russia → China/India displacing Qatari/Algerian molecules westward) means Russian de-risking ≠ supply removal.

**Assumption 6 (Qatar/Algeria incremental not buffer-replacing, 0.65 → 0.30).** Deep-dive missed Qatar Helium 3 commissioned 2024 at ~425 mmcf/yr nameplate ≈ 14% of global demand. This single fact materially weakens the deep-dive's supply-tightness edifice. Combined with Amur-2 ramp + Algeria Skikda restart + Riley Ridge expansion + LNG-byproduct latent capacity globally, the **probe's 2027-glut scenario** is not a tail — it is a coherent base case.

**Net: probe-reweighted 2027-glut probability ≈ 0.35-0.40.** Deep-dive's implicit P(thesis-failure on supply side) ≈ 0.10-0.15; probe argues it should be ≥0.25-0.35 standalone, and combined with demand-side substitution it is closer to 0.40 that *spot helium retraces meaningfully through 2027*, not the deep-dive's tail-only treatment.

### B. Story-stock / base-rate screen on the microcap basket

Per amendment 2026-05-08 ("story-stock / fraud / overinflation screen"). Bayesian, not gating: strong signals can overpower bad base rate. Walk each name against required signals.

**Cohort base rate (prior).** ~12 junior helium explorers 2017-2025; ~0 reached sustained commercial scale; -80 to -95% drawdowns are the modal outcome (Renergen, Helium One, Avanti). PLSR.V / DME.V / HE.V are statistical members of this cohort. **Prior P(any single name reaches sustained positive cashflow inside 24mo) ≈ 0.05-0.10**, materially worse than the deep-dive's 0.40 single-name confidence.

**PLSR.V (Pulsar Helium, Topaz Minnesota).**
- Binding offtake: NO. Public materials reference industry interest / discussions; no announced binding contract with Praxair / Linde / APD / Air Liquide.
- Audited reserves: PARTIAL. NI 51-101 resource reporting expected/in-progress; no booked reserves at probe time.
- Funded covenants / capex: NO. Capex to first commercial production estimated $60-80M; market cap $40-50M → capex-to-cap 1.5-2x, dilution forecast 50-200%.
- Insider $$$ buying: NOT VISIBLE in available filings.
- Pipeline / infrastructure: northern Minnesota; nearest helium-grade processing infrastructure hundreds of miles away.
- Story-stock markers: MOU-not-binding posture, retail-newsletter coverage typical of cohort.
- **Posterior: NOT lifted above prior. Signals do not overpower the cohort base rate.**

**DME.V (Desert Mountain Energy, Holbrook Basin Arizona).**
- Binding offtake: PARTIAL — has produced and sold helium at small scale; off-take terms historically opaque.
- Audited reserves: PARTIAL — reported production but limited independent reserve audit.
- Funded covenants: PARTIAL — has demonstrated cashflow path but persistent capex-funded-by-equity pattern.
- Insider $$$: small.
- Track record: only operating producer in the basket; smallest dilution risk among the three; but production scale is sub-commercial vs major-buyer thresholds.
- **Posterior: marginally lifted above cohort prior — call it 0.15 vs cohort 0.05-0.10. Better than peers, still well below deep-dive's 0.40.**

**HE.V (Total Helium, Saskatchewan + Montana).**
- Binding offtake: NO.
- Audited reserves: NO at scale; exploration-tilted.
- Funded covenants: NO.
- Insider $$$: NOT VISIBLE.
- Story-stock markers: most exploration-tilted of the three; weakest signal stack.
- **Posterior: NOT lifted above prior.**

**Honest verdict on the basket.** None of the three carries the signal stack that the amendment defines as capable of overpowering the cohort base rate (binding offtake, audited reserves, funded covenants, insider $$$, multi-year operational track record on prior assets). DME marginally; PLSR and HE not at all. The deep-dive's basket-level "0.70 that at least one converts inside 24mo" must be revised to **~0.30-0.35 at most** under base-rate-screened priors. Convex-tail upside is preserved (M&A roll-up by majors is a separate path), but the deep-dive over-priced the conversion path.

### C. Hedge-mechanic options walk

Per amendment menu (i)-(vi):

- **(i) Skip basket, hold APD only.** Probe's cleanest critique: APD helium <8% revenue; +50% helium re-pricing adds <2% to APD EPS. APD is hydrogen-capex execution risk + diversified industrial-gas beta, not a helium pure-play. Acceptable as "preserve some industrial-gas-quality exposure with zero microcap risk" but **does NOT meaningfully capture the asymmetric helium thesis**. Should not be sold internally as "helium exposure" — it is mostly a quality-anchor whose helium leg is incidental.

- **(ii) Diversified vehicle.** No clean helium ETF. Industrial-gas oligopoly (APD / Linde / Air Liquide) all have helium as a small revenue line. Same problem as (i) at lower idiosyncratic risk. Not materially better.

- **(iii) Anchor-plus-satellite at smaller satellite (APD 2.5% + basket 0.5% = 3.0%).** Preserves convex-tail optionality while cutting microcap exposure to ~⅓ of deep-dive. Reasonable middle path; basket sized to be losable (-100% basket = -0.5% NAV).

- **(iv) Skip helium entirely.** Once probe haircuts applied: E[R] basket falls (assumption 1+2+4+5+6 revisions reduce mean), 2027-glut scenario weight rises to ~0.35-0.40, microcap base rate ≈ 0.10-0.15 with no compensating signals. Deep-dive's E[R]/E[risk] of 0.77 on basket was already below the Type B 1.5 hurdle (justified only by convex-tail). Under reconciled priors: basket E[R] revises to ~0% to +5% (12mo); E[risk] unchanged or worse; **basket no longer clears even on convex-asymmetry argument** because the asymmetry itself compresses (fewer +180% paths once supply-glut weight rises).

- **(v) Staged sizing: placebo 0.25% basket + APD 1.5% NOW; scale on milestone.** Captures optionality at minimal cost. Milestones gate scale-up: binding offtake announced (PLSR or DME), drilling resource confirmed at NI 51-101 reserve standard, financing closed at non-dilutive terms. This is the textbook application of amendment hedge mechanic (vi) "staged sizing — placebo first, scale on milestone hits."

### D. Decision

**Selected: variant (v) staged sizing, with downsized anchor.**

Reconciled sleeve: **APD 1.5% NAV anchor + microcap basket 0.25% NAV placebo = 1.75% NAV total** (vs deep-dive 4.5%).

Microcap placebo split: PLSR 0.10% / DME 0.10% / HE 0.05%. (DME slightly favoured weight-equal with PLSR on marginal posterior lift; HE held to true placebo.)

**Justification against E[R]/E[risk] hurdle:**
- Probe-reweighted 2027-glut probability ~0.35-0.40 vs deep-dive's implicit ~0.10-0.15. This roughly halves bull-scenario weight (S2 + S5 + S6) and roughly doubles bear-scenario weight (S3 + S4 + new "supply-glut" sub-scenario splitting from S7).
- MRI demand inflection is structural and already-realised on flow; raises the probability of the assumption-7 trigger that the deep-dive itself defined as a halve-basket auto-resize. *We are at-or-past the trigger.*
- Microcap base-rate screen yields posterior 0.30-0.35 basket-level conversion (vs deep-dive 0.70) with no compensating signals visible (no binding offtakes, no audited reserves at production scale, no insider $$$, capex-to-cap 1.5-2x implying 50-200% dilution before first cashflow).
- Reconciled basket E[R] (12mo) ≈ +3-7%, E[risk] ≈ 25-30% → ratio ~0.20. Far below the 1.5 hurdle. Even the convex-tail argument compresses because P90 paths (>+150%) contract from probe's supply-glut weight.
- APD reconciled E[R]/E[risk] ≈ 1.0-1.2, also below hurdle but acceptable as quality-industrial defensive serving partial role on H1 and on broader cluster (it is not a helium-thesis vehicle but is a defensible position on its own merits). Sized down from 3.0% to 1.5% to reflect that we are NOT paying for helium-thesis exposure through APD.
- Microcap placebo (0.25%) is a pure call-option on milestone fire (binding offtake, M&A roll-up). Cost is bounded: -100% basket = -0.25% NAV on book. Convex-tail upside survives at minimal capital cost.

**Why not (iv) skip entirely.** The convex-tail M&A optionality is not zero, and the cost of preserving it at placebo size is small. Amendment is explicitly Bayesian-not-gating; we don't auto-zero a thesis with non-trivial residual asymmetry just because the central case is weak. But scale only on milestone-gated evidence.

**Cluster impact.** Sleeve drops from 4.5% to 1.75% → cluster total from 14.0% to 11.25% (REE 1.5% + uranium 4% + silver 4% + helium 1.75%). Eases pressure on the inferred 15-18% cluster ceiling and frees capacity for subsequent Type B child Collapses (phosphate, EU defense, India infra, tin) — most of which have their own base-rate screens to clear.

**Auto-resize triggers updated:**
- Scale-up to deep-dive sizing (basket 1.5% / APD 3.0%) gated on **all three**: (i) binding offtake announced for PLSR or DME (not MOU), (ii) NI 51-101 reserves booked at production scale on at least one name, (iii) financing closed at non-dilutive terms (debt or strategic equity, not microcap retail placement) on at least one name. Until then, hold at 1.75%.
- Scale-down to skip (variant iv) gated on: (a) helium spot below $300/Mcf for two consecutive months (deep-dive trigger holds), or (b) Tier-1 MRI OEM announces >$500m platform investment in low-helium *and* Qatar Helium 3 confirmed at full nameplate, or (c) any single basket name does dilutive secondary at >30% prior price → liquidate that name and reassess basket.
- Original deep-dive triggers retained as the broader sensitivity list.

### E. Top evidence items by E[VOI]

Ranked for VOI before any further capital Collapse.

1. **Helium spot price path (Q2 2026 → Q4 2026), private bilateral contract prints.** Resolves directly between probe's 2027-glut thesis and deep-dive's $400+ sustained thesis. If spot is drifting toward $300/Mcf, glut is real and active; if holding $400+ through 2026 in face of Qatar 3 + Amur-2, deep-dive priors partially restored. Highest VOI because it discriminates the dominant probe attack at the resolution timescale we care about. Source path: Praxair / Linde / Air Liquide / APD earnings-call commentary, industry-press spot prints (gasworld, CryoGas), Messer disclosures.

2. **Qatar Helium 3 actual production / utilisation (FY2025 nameplate-utilisation print and FY2026 H1 update).** ~14% of global demand at nameplate is the largest single number in the supply equation. Probe asserts it is online; need confirmation on actual run-rate vs nameplate. If running at 60-70% utilisation, glut weight reduces materially; if at 90%+ and ramping, supply-side bear case is confirmed. Source: ExxonMobil / RasGas operational filings, QatarEnergy disclosures.

3. **PLSR.V or DME.V binding-offtake or NI 51-101 reserve-booking event (or its absence through Q4 2026).** This is the milestone the staged-sizing decision is gated on. Each quarter without it accumulates evidence the cohort base rate is binding on these names too. With it, posterior single-name conversion lifts materially and the basket sizing scale-up trigger fires. Source: SEDAR filings (assumption 12 EDGAR-stub gap binds here), company press releases, technical reports on SEDAR+.

(Honourable mention 4: tier-1 MRI OEM platform-investment guidance on low-helium architecture, FY2026 capital markets days. Discriminates assumption 1 reconciliation. Lower VOI than items 1-3 because the *direction* is already established by probe; only the *pace* is at issue.)

### Reconciliation verdict

**CUT to staged.** From deep-dive 4.5% NAV (APD 3.0% + basket 1.5%) to **1.75% NAV (APD 1.5% + basket 0.25% placebo)**.

Brittle assumption(s) post-reconciliation: **#7 (recycling/substitution)** is no longer the brittle assumption — it has largely resolved unfavourably and is priced in. The new most-brittle assumption is **a composite: P(2027 supply glut) ≈ 0.35-0.40 combined with microcap conversion-without-binding-signals**. Threshold for full re-skip is items 1+2 in §E both confirming probe priors. Threshold for scale-up is all three milestones in §D (binding offtake + NI 51-101 reserves + non-dilutive financing) on at least one name.

## Outcome

_Locked until 2027-05-15._

## Reflection

_Locked._
