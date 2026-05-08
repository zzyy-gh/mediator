---
id: 2026-05-15-india-infra-sizing
shape: convergent
collapse_flavour: capital
status: open
scope: "Sizing decision for India infrastructure mid-cap sleeve under Type B archetype."
parent_inquiry: 2026-05-08-type-b-screen-v2
graph_snapshot: 2026-05-08T09:00Z
outcome_window: 2027-11-15
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

# Inquiry: India infra mid-cap sizing

## Scope

Decide capital allocation to India infrastructure mid-cap sleeve. Vehicles: SMIN (small/mid-cap ETF, diversified), L&T (LT — liquid single-name execution), Siemens India (SIEMENS.NS — execution premium), ABB India (ABB.NS — automation). Ranked #3 in v2 Type B screen. Demand drivers: demographic + electrification + capex push (rail, power T&D, water). Recognition gap: foreign holding share at 15-yr low, under-owned. Recognition window 18-36mo. Drawdown bound −40%.

In scope: ETF vs single-name mix, sizing, INR currency overlay note, sensitivity.
Out of scope: India large-caps (already recognized), India IT services (different cycle).

## Assumptions (load-bearing)

Per amendment `2026-05-08-feed-gap-promotes-to-assumption`, feed gaps are promoted into named assumptions with explicit confidence haircuts. Per amendment `2026-05-08-factor-coverage-checklist`, factor coverage is explicit on `m.probe.edges`. Recognition window inherits from parent (#3, 18-36mo) which is longer than the parent screen's modal window — sizing math uses the longer window.

1. **India fiscal trajectory holds capex share through 2026-2028 election cycle.** Capex share of central + state budgets remains within −10% of FY25 level through Indian general elections (next due 2029; key state cycles 2026-2027) and through any post-election expenditure rebalancing. Failure path: populist transfer rotation diverts 15-25% of infra capex to direct income support; mid-cap infra de-rates 25-35% on multiple compression alone. Confidence 0.60 (parent assumed 0.65; haircut 0.05 for FRED gap on Indian CPI/IIP/fiscal-deficit verification).
2. **Capex allocation persistence across the three pillars (rail, power T&D, water).** Each of (a) dedicated freight corridors + electrification, (b) inter-state HV transmission + distribution loss reduction, (c) Jal Jeevan + urban-water remains a named line-item through outcome window. Failure of any single pillar haircuts thesis 30%; failure of two breaks it. Confidence 0.65 — three-pillar design is the structural feature; not a single bet.
3. **Demographic dividend timing.** Urbanization rate moves from 36% toward 50% on a multi-decade path; the relevant window for this inquiry is the *first derivative* — net rural-to-urban migration sustains 1.0-1.5%/yr through 2027 (no migration shock), with associated electricity-per-capita growth of 6-9% YoY. Failure (migration stall, formal-employment ceiling) is slow-burn, not outcome-window-relevant; confidence 0.75 within window.
4. **INR currency path: depreciation bounded.** USD/INR moves within a band of roughly 84-92 over the outcome window (currently ~85-86). Tail path of disorderly depreciation to >95 is bounded by RBI FX reserves (~$650bn, ~10mo import cover) and by RBI's revealed willingness to lean against speed of move. Base case: 2-4%/yr structural depreciation against USD; this haircuts USD returns on local-listed names by 4-12% cumulative over 36mo. Confidence 0.60 (FRED gap on EM-DM real-rate differential haircuts this further; promoted from feed gap, see assumption 10).
5. **Foreign-holding mean-reversion is the recognition mechanic.** FII holding share in Indian equity is at a 15-year low after 2024-2025 outflows (per parent screen). The recognition mechanic is *flow-driven re-rating*, not earnings surprise: a sustained 6-month FII inflow turn re-rates the mid-cap basket 25-40% via multiple expansion before earnings even confirm. Failure path: FII allocations stay routed to China-recovery / Korea-AI / Japan-corporate-reform alternatives; recognition window slides past 36mo. Confidence 0.55 — this is the *most contingent* assumption because it depends on relative attractiveness of EM ex-India alternatives, not on India fundamentals.
6. **Recession pass-through (S3 survival).** Indian infra capex is fiscally driven, not export-driven; merchandise exports are ~13% of GDP and concentrated in services. In a global S3 (developed-market recession, China growth <3%), Indian fiscal capex *continues* (counter-cyclical political logic), but (a) mid-cap valuations compress 25-35% via global EM beta, (b) FII inflows pause, sliding recognition window. The thesis survives S3 on cash-flow but the recognition window stretches by 12-18mo. Confidence 0.65.
7. **Local execution risk in mid-caps.** Cummins India / ABB India / Siemens India are listed Indian subsidiaries of multinationals — governance and disclosure are higher than median Indian mid-cap, but corporate-action risk (parent buy-in / delisting, related-party pricing) and execution slippage on multi-year EPC tenders remain real. ETF (SMIN) caps single-name idiosyncratic risk. Confidence 0.70 on basket-level execution; 0.55 on any single-name execution.
8. **Recognition latency 18-36mo for this sleeve.** Parent screen modal window for #3 is 18-36mo (longer than the 12-24mo modal for #1 phosphate / #2 EU defense), reflecting that the recognition mechanic is foreign-flow-driven rather than earnings-surprise-driven. Outcome window of 2027-11-15 (~30mo from snapshot) sits inside the upper half. Confidence 0.60.
9. **Drawdown bound −40% on basket.** Parent screen quantified −40% on small/mid-cap basket and −35% on L&T at ~18x sober earnings on confirmed backlog. We adopt −40% as the basket bound; ETF route caps single-name risk at −40%. Confidence 0.70.
10. **(Feed gap → assumption) FRED feed missing — Indian CPI/IIP/fiscal-deficit/REER are approximated by news-summarizer prints + RBI press releases via web_search.** Confidence haircut on macro-conditional claims (assumptions 1, 4, 6): −20%. Resolves when FRED hydrates Indian series.
11. **(Feed gap → assumption) No live EM-flows / FII tracking feed.** FII flow turn (assumption 5) is the recognition mechanic but the feed for monitoring it is absent — NSDL / SEBI flow data via web_search only, lagged 1-2 days. Confidence haircut on recognition-timing claim: −15%. Resolves when an EM-flows feed (NSDL / SEBI proxy or aggregator) is registered.
12. **(Feed gap → assumption) EDGAR stub-only — single-name fundamentals on LT.NS / SIEMENS.NS / ABB.NS rest on web_search and BSE/NSE filings.** Valuation framing for single-names is qualitative + price-action. Confidence haircut on single-name vs ETF valuation differentiation: −15%. Resolves when a BSE/NSE filings feed (or extended EDGAR) hydrates.
13. **No India-INR FX hedge available at retail-mandate cost.** USD/INR forwards / NDF carry is structurally negative (INR rate > USD rate); 12mo NDF forwards imply ~3.5-4.5%/yr depreciation already priced. Hedging at cost ≥ assumed structural depreciation eliminates the carry but not the tail-shock optionality. Confidence 0.70 on the cost-benefit framing.

## Graph references

Pulled from snapshot 2026-05-08T09:00Z (inherits parent v2 snapshot 2026-05-08T05:15Z + portfolio-architecture extensions):

- `graph/strategies.md#strategy.type-b.current_candidates_v2[rank=3]` — India infra mid-caps; vehicles `["LT.NS", "SIEMENS.NS", "ABB.NS", "CUMMINSIND.NS", "SMIN", "INDA"]`; geography India; macro_conditional true; demand_floor_recession true; child_inquiry this entry.
- `graph/strategies.md#strategy.type-b.current_candidates_v2[rank=1]` (phosphate) and `[rank=2]` (EU defense tier-2) — referenced as cluster siblings for cross-sleeve correlation framing.
- `graph/strategies.md#strategy.type-b.current_candidates` (v1) — REE 1.5%, uranium 4%, silver 4% sized sleeves (cluster context — supply-bottleneck industrial cluster from v1).
- `graph/macro.md#macro.cfx_eurusd_x` 1.1737 — EUR firmer; not India-load-bearing but indicates broad USD-DXY softness, which historically supports EM-equity flows.
- `graph/macro.md#macro.cfx_usdjpy_x` 156.87 — extreme yen weakness; relevance is *negative* (yen carry has been an alternative EM-funding route; carry unwind would re-route flows but ambiguously to / from India).
- `graph/macro.md#macro.cfx_dbc` 30.25 — broad commodity tape mid-vol; commodity-import-burden proxy for India CAD.
- `graph/macro.md#macro.cfx_uup` 27.41 — DXY proxy; flat-to-soft DXY supports the FII-inflow-turn recognition mechanic (assumption 5).
- `graph/macro.md#macro.cfx_tlt` 85.65 — duration cheap; relevant because Indian mid-cap multiples move inversely to global long rates via EM-equity discount-rate channel.
- `graph/technicals.md#technicals.eem` 66.59, vol 28.7% — EM equity tape live; vol regime sets a floor on India basket realised vol assumption.
- `graph/technicals.md#technicals.efa` 102.89, vol 23.4% — DM-ex-US comp; spread vs EEM informs EM-DM rotation context.
- `graph/themes.md#themes.ai-capex-cycle` — supports Indian data-center demand pillar (5-7 GW by 2030); not the central thesis driver but a tailwind.
- `graph/politics.md#politics.us-china-tariff-regime-2026` (escalation 0.35, from parent v2) — indirect tailwind for India as China+1 supply-chain beneficiary; not load-bearing.
- `inquiries/2026-05-08-portfolio-architecture.md` — assumption 2 (FRED gap → −30% macro haircut), assumption 4 (no flows feed → −25% reflexivity haircut), proposed adjustment A6 (Type B cluster cap discipline). This sleeve interacts with A6 — see cluster context below.
- `inquiries/2026-05-09-silver-sizing.md`, `2026-05-09-uranium-sizing.md`, `2026-05-09-lynas-sizing.md` — sized v1 Type B sleeves (REE 1.5% / uranium 4% / silver 4%); cluster context for the cap framing.

**Graph gaps that limit confidence (carried from parent + new):**
- FRED Indian series gap (assumption 10).
- No EM-flows / FII feed (assumption 11) — directly bites on the *recognition mechanic*.
- EDGAR stub for ex-US filings (assumption 12).
- No INR forwards / NDF curve feed → hedge-cost framing (assumption 13) rests on web_search.

**Cluster context (cross-sleeve correlation framing).** The v1 Type B sleeve cluster of REE 1.5% + uranium 4% + silver 4% = 9.5% NAV is a *supply-bottleneck industrial cluster* — common factor exposure to (i) global industrial cycle, (ii) commodity-cluster correlation in stress, (iii) physical-supply-chain reflexivity. India infra is **partially exempt** from this cluster framing because:
- *Supply mechanic differs.* India infra demand is fiscal-policy-driven (capex line items), not commodity-deficit-driven. The supply bottleneck is *Indian engineering capacity* (L&T duopoly, Siemens India HV automation IP) not global commodity scarcity.
- *Geographic correlation.* India is geographically uncorrelated to North American REE / Australian uranium / global silver — political and currency shocks affect the sleeves on different paths.
- *Recession pass-through.* Indian fiscal capex is counter-cyclical (assumption 6); supply-bottleneck commodities are pro-cyclical at the industrial-demand layer. Cluster correlation in S3 is meaningfully <1.
- **But not full exemption:** all four sleeves share *EM-equity beta* and *DXY direction* exposure. In a true USD-strength + global-risk-off, all four de-rate together.

Net: India infra counts toward overall Type B *NAV concentration* discipline (A6 portfolio architecture cap on aggregate Type B sleeve), but does *not* aggregate into the supply-bottleneck cluster sub-cap. Flag this distinction at Collapse.

## Intent

Output a sizing recommendation in NAV %, vehicle mix (ETF vs single-name with explicit weights), E[R] / E[risk] ratio, brittle assumption with threshold, and INR hedge stance, for the India infra mid-cap sleeve over a 30mo outcome window (to 2027-11-15). Confidence 0.55 on the precise NAV %; 0.65 on the directional verdict that the sleeve passes the "size something" gate; 0.50 on the optimal ETF vs single-name split (the more contingent piece given EDGAR stub).

## Self

- **self.capability** — Vehicle-agnostic convergent sizing. Can run scenario-weighted return calc, fractional Kelly with haircut, drawdown-bound discipline, asymmetry ratio. Cannot run live factor regression on India basket vs portfolio.current (broker feed empty); cannot price options-implied tail (no CBOE feed, and India options are in any case retail-illiquid for foreign accounts); cannot directly read BSE/NSE filings (EDGAR stub). Web_search available for RBI prints, NSDL FII data, Indian budget documents.
- **self.calibration** — No prior closed Type B sizing inquiries on this instance; no track record. Inherit parent's base-rate: Type B disciplined-screen hit-rate 0.30-0.40, payoff multiple on hits 3-8x. Apply additional haircut for (a) geographic data thinness on India (parent v2 calibration haircut 0.10), (b) longer 18-36mo recognition window vs the 12-24mo norm of v1 sized sleeves — more time for thesis-violating regime change.
- **self.taste** — Bias toward ETF over single-name when EDGAR stub blinds single-name valuation differentiation; bias toward demand-floor theses surviving S3 (parent screen taste, applies here); bias against any thesis where the recognition mechanic depends on a flow turn we cannot monitor (assumption 11 is uncomfortable). Counter-bias on this inquiry: prefer the ETF *too aggressively* — must give single-name execution-premium thesis (Siemens India / L&T) fair weight.
- **Bias probes for this run.**
  - *Narrative seduction:* would I size this if the "demographic dividend" framing were boring? Probed — the load-bearing piece is the fiscal-capex line item structure (rail / T&D / Jal Jeevan) and the foreign-holding mean-reversion mechanic, both vehicle-agnostic. Demographic dividend is supporting context, not the bet. Survives.
  - *Recency:* am I overweighting 2024-2025 FII outflows as the recognition setup? Yes, somewhat — the 15-year-low foreign holding share is real but the *mean-reversion timing* is genuinely under-determined by the data we have. Reflected in assumption 5 confidence (0.55, lowest among load-bearing).
  - *Implicit factor bet:* this sleeve is partly an EM-equity-beta tilt + partly a DXY-soft tilt + partly an industrials-factor tilt. The execution-premium edge over a generic EEM position is the demand-pillar specificity (rail / T&D / water) and the recognition mechanic. Sizing must net against any incremental EEM exposure to avoid double-counting.
  - *Tail neglect:* INR disorderly-depreciation tail to >95 is bounded by RBI reserves but real; assumption 4 confidence 0.60 reflects this. Hedge-stance section addresses.

## M-nodes (sequence)

1. `m.probe.scope` — sharpened: convergent capital sizing, ETF + single-name mix, with INR overlay note. Out-of-scope held: India large-caps and IT services framing deferred.
2. `m.probe.prior-art` — `methods.md` (fractional Kelly, scenario stress, drawdown bound, factor exposure); `blind-spots.md` (narrative seduction, recency, implicit factor, tail neglect, regime change blindness — INR regime); `strategies.md` Type B drawdown-bounded criterion; `amendments.md` (factor-coverage checklist + feed-gap-to-assumption + world-frame-first); parent v2 (#3 specifications); sibling sized sleeves (silver/uranium/REE) for cluster framing; portfolio-architecture A6.
3. `m.probe.world` — graph snapshot read; web_search for FY26 Indian Union budget capex line items, RBI April 2026 policy review, NSDL/SEBI Q1 2026 FII flow prints, USD/INR NDF curve, L&T order book latest, Siemens India backlog.
4. `m.probe.edges` — **factor-coverage walk** (per amendment):
   - **macro (rates, growth, inflation, fiscal)** — Indian fiscal stance is the load-bearing macro factor (assumption 1, 2). Global rates secondary via duration → EM multiple channel (TLT proxy). Confidence-haircut applied (assumption 10, FRED gap).
   - **geographic / FX** — INR is part of *macro/geographic factor* (assumption 4); India sovereign + corporate-tax stability; no sanctions exposure. INR FX is the largest single haircut on USD-investor returns.
   - **regime (vol, liquidity, dispersion)** — EM equity vol regime mid-elevated (EEM 28.7%); SMIN historical realised vol 22-28% in normal regimes, 35-45% in stress; liquidity ample on SMIN/INDA, ample on LT.NS / SIEMENS.NS / ABB.NS at retail size, thinner on CUMMINSIND.NS.
   - **correlation structure** — India infra correlates to (a) EM equity beta (~0.7 to EEM), (b) global industrials via L&T / Siemens India / ABB India earnings, (c) DXY direction (negative). Correlation to v1 supply-bottleneck cluster <0.4 — partial exemption from cluster cap (see Graph references). Implicit factor bet flagged: this sleeve adds EM-beta exposure; if the book already carries EEM, deduct that to avoid double-counting.
   - **flows (positioning, crowding, fund flows)** — FII flow turn IS the recognition mechanic (assumption 5). Crowding *low* — that is the setup. Confidence haircut (assumption 11, no flows feed).
   - **themes (narrative state, recognition stage)** — narrative state is *neglected*: India is under-owned in EM ex-China benchmarks; recognition stage = pre-recognition (matches Type B archetype). `themes.ai-capex-cycle` provides tailwind via data-center demand pillar.
   - **reflexivity (positioning ↔ price ↔ narrative)** — flow turn is reflexive: FII inflows → mid-cap re-rating → INR firms → USD-investor returns improve → more FII inflows. The reflexive loop is intact but cannot be directly monitored (assumption 11). Confidence haircut (portfolio-architecture A4, no flows feed → −25%).
   - **liquidity / capacity** — SMIN / INDA: ample at retail. LT.NS ADR (LTOUF, illiquid) or local via international broker access. SIEMENS.NS / ABB.NS: ample at retail size, foreign account access via broker (FPI route or international brokerage). No capacity issue at proposed sleeve size; exit cost on single-names somewhat higher than ETF.
5. `m.reframe` — None. Scope held; convergent capital-Collapse sizing is the right output shape.
6. `m.test.feasibility` — capability (sizing math executable) × constraint (drawdown bound −40% quantified) × budget (NAV % within Type B aggregate cap from A6) × data-quality (medium-low; four feed gaps promoted to assumptions; Indian-specific data coarser than US-listed sleeves). Feasibility: PASS, with confidence haircut applied to final NAV %.
7. `m.collapse` — capital: open India infra sleeve at recommended NAV %, ETF-dominant mix, with sensitivity threshold (FII flow turn signal) pre-registered as the auto-resize trigger.

## Prediction (convergent)

### Expected return — distribution sketch (USD returns to a USD-investor, unhedged unless noted)

Three horizons because parent screen specifies recognition window 18-36mo, longer than the 12-24mo norm of v1 sized sleeves. Distributions are scenario-weighted across {S1 soft-landing+EM-rotation 0.25, S2 muddle-through 0.35, S3 global recession 0.20, S4 India-fiscal-disappointment 0.15, S5 INR shock 0.05}. Quantiles approximate; central tendency more reliable than tails.

**12-month (recognition not fully realised; mostly carry + early re-rating):**

| Vehicle | P10 | P50 | P90 | Mean | Comment |
|--------|-----|-----|-----|------|---------|
| SMIN (ETF) | −22% | +6% | +28% | +5% | Diversified; INR drag ~3-4% baked in |
| LT.NS | −28% | +9% | +38% | +7% | Backlog visibility supports floor |
| SIEMENS.NS | −30% | +12% | +45% | +9% | Higher beta, execution-premium re-rating optionality |
| ABB.NS | −32% | +10% | +42% | +7% | Highest single-name vol, narrowest moat |
| **Basket (proposed mix)** | **−25%** | **+8%** | **+33%** | **+7%** | Mix detailed in sizing |

**24-month (mid-window; recognition partially realised in base case):**

| Vehicle | P10 | P50 | P90 | Mean | Comment |
|--------|-----|-----|-----|------|---------|
| SMIN | −30% | +22% | +58% | +18% | Re-rating + earnings compounding |
| LT.NS | −35% | +35% | +75% | +28% | Parent screen: +60-100% top end aligns |
| SIEMENS.NS | −38% | +48% | +95% | +36% | Execution-premium tail visible |
| ABB.NS | −38% | +38% | +82% | +28% | Tracks Siemens India with wider band |
| **Basket** | **−32%** | **+30%** | **+68%** | **+24%** | Mix detailed in sizing |

**36-month (full recognition window; thesis confirmed or rejected):**

| Vehicle | P10 | P50 | P90 | Mean | Comment |
|--------|-----|-----|-----|------|---------|
| SMIN | −35% | +38% | +85% | +32% | Parent screen: +40-70% bracketed by P50/P90 |
| LT.NS | −38% | +60% | +120% | +50% | Parent screen: +60-100% tracks P50-P90 |
| SIEMENS.NS | −40% | +85% | +160% | +70% | Parent screen: +80-130% midpoint |
| ABB.NS | −40% | +60% | +130% | +52% | |
| **Basket** | **−36%** | **+52%** | **+105%** | **+42%** | Mix detailed in sizing |

### Expected risk — drawdown distribution

12mo worst-plausible drawdown (per Type B drawdown-bounded discipline):

| Vehicle | DD bound | Floor logic |
|---------|----------|-------------|
| SMIN | −40% | Diversified small/mid-cap basket; ETF caps single-name idiosyncratic risk |
| LT.NS | −35% | ~18x sober earnings on confirmed backlog (parent screen) |
| SIEMENS.NS | −45% | Higher beta; execution-premium narrative compresses fast in stress |
| ABB.NS | −45% | Same logic, narrower moat than Siemens India |
| **Basket** | **−40%** | Aligned with parent screen quantification |

INR-shock tail (S5, p=0.05): additional −8 to −12% USD-return haircut on top of any local-currency drawdown, partly offset by RBI intervention dampening in 6-12mo window.

### E[R] / E[risk] ratio

Using 24mo mean E[R] vs 12mo drawdown bound (the natural Type B ratio per silver-sizing precedent):

| Vehicle | E[R] 24mo | DD bound | E[R]/DD |
|---------|-----------|----------|---------|
| SMIN | +18% | 40% | 0.45 |
| LT.NS | +28% | 35% | 0.80 |
| SIEMENS.NS | +36% | 45% | 0.80 |
| ABB.NS | +28% | 45% | 0.62 |
| **Basket** | **+24%** | **40%** | **0.60** |

Using 36mo mean (the recognition-window-matched ratio):

| Vehicle | E[R] 36mo | DD bound | E[R]/DD |
|---------|-----------|----------|---------|
| SMIN | +32% | 40% | 0.80 |
| LT.NS | +50% | 35% | 1.43 |
| SIEMENS.NS | +70% | 45% | 1.56 |
| ABB.NS | +52% | 45% | 1.16 |
| **Basket** | **+42%** | **40%** | **1.05** |

For comparison, Type B archetype rough hurdle for sizing E[R]/E[risk] = 1.0 (per silver-sizing precedent, where 1.5 was the v1-cluster bullion bar). At the 36mo recognition-matched horizon, basket clears 1.0; LT.NS and SIEMENS.NS clear comfortably. At the 24mo horizon, single-names clear but basket sits at 0.60 (below hurdle on the shorter horizon — this is why the longer recognition window is structurally required for this sleeve).

**Verdict on the "size something" gate:** PASS at 36mo; CONDITIONAL at 24mo (sleeve passes only if outcome window is allowed to run the longer recognition path). This is consistent with assumption 8 and the parent screen 18-36mo window.

### Sensitivity — brittle assumption + threshold

**Brittle assumption: A5 (foreign-holding mean-reversion is the recognition mechanic).** Confidence 0.55 — the lowest among load-bearing — and the *most contingent* on factors outside India fundamentals (relative attractiveness of EM ex-India alternatives).

**Threshold for thesis violation:** if cumulative net FII flow into Indian equity is *negative* over any rolling 12-month window inside the outcome horizon (i.e., the 2024-2025 outflow pattern persists beyond mid-2026), the recognition mechanic is broken. Specifically:
- 6-month window: net FII flow must be > −$5bn (mild outflow tolerable as setup).
- 12-month window: net FII flow must be > 0 (positive net inflow required to support thesis).
- Pre-registered auto-resize trigger: if 12-month net FII flow < $0bn at any monthly review, downsize sleeve by 50% (move from recommended to floor sizing).
- Hard exit trigger: if 12-month net FII flow < −$10bn AND USD/INR > 92 simultaneously (combined flow + currency shock), close sleeve.

**Secondary brittle assumption: A1 (fiscal trajectory holds).** Threshold: if Indian Union or major-state budget reduces capex share by >15% in any annual budget through outcome window, halve the sleeve.

**Tertiary brittle assumption: A4 (INR path).** Threshold: USD/INR > 92 sustained 30 days. Trigger: implement NDF hedge on 50% of remaining sleeve notional regardless of carry cost.

### Sizing — NAV % + ETF / single-name mix + INR hedge note

**Recommended sleeve size: 4.0% NAV (range 3.0-5.0%, confidence 0.55).**

Mix (within sleeve):
- **SMIN (ETF, diversified): 2.4% NAV** (60% of sleeve). Default vehicle given EDGAR stub on single-names; lowest single-name idiosyncratic risk; INR exposure unavoidable but transparent.
- **LT.NS (single-name liquid): 0.8% NAV** (20% of sleeve). Execution-premium torque; backlog visibility justifies separating from ETF.
- **SIEMENS.NS (execution premium): 0.5% NAV** (12.5% of sleeve). Highest E[R]/DD on 36mo basis; size disciplined for higher single-name vol.
- **ABB.NS (automation): 0.3% NAV** (7.5% of sleeve). Smallest because narrower moat than Siemens India and highest single-name vol; included for diversification within the single-name tilt.

(CUMMINSIND.NS dropped from sizing despite being in candidate vehicles — liquidity thinner at retail size and adds genset-cycle exposure that is not core to the rail/T&D/water demand-pillar thesis.)

**Sizing rationale:**
- Fractional Kelly on the basket: edge ≈ 0.42 (36mo mean) / vol² (36mo basket vol ≈ 35% annualised → ~0.123 var) → ~3.4x Kelly. Haircut to 1/4-Kelly per Type B discipline → ~0.85 of NAV at face value.
- Apply confidence haircut for: FRED gap (−20%, A10), no flows feed (−15%, A11), EDGAR stub (−15%, A12), longer 18-36mo window vs sized peers (−10% behavioral haircut on novelty). Compound haircut ≈ 0.55. → ~0.47 of NAV at face value reduces to ~4.7% NAV.
- Apply portfolio-architecture A6 Type B aggregate cap discipline: existing v1 sized Type B sleeves (REE 1.5% + uranium 4% + silver 4%) total 9.5% NAV; if A6's aggregate Type B cap is, say, 20-25% NAV (per portfolio-architecture proposal), India infra at 4% brings the total to 13.5% NAV which sits inside the cap.
- **Cluster cap context:** REE / uranium / silver share the supply-bottleneck industrial cluster framing. India infra is geographically and mechanically uncorrelated to that cluster (see Graph references) — *partial exemption from supply-bottleneck cluster sub-cap*. India infra counts toward overall Type B NAV concentration but does *not* aggregate into the supply-bottleneck cluster sub-cap. If A6 has been structured with a tighter supply-bottleneck-cluster sub-cap separate from overall Type B cap, India infra sits in a different bucket. **Flag for Collapse.**
- 4.0% (vs the haircut-derived 4.7%) reflects an additional tier-3 caution on the longer outcome window — the sleeve sees one more election cycle of fiscal-trajectory risk than v1 sized peers.
- Floor (3.0% NAV): if (a) FII 12mo net flow turns mildly negative but not breaking threshold, OR (b) USD/INR breaks 90 without breaking 92.
- Ceiling (5.0% NAV): if (a) FII 6mo net flow turns positive and sustains for 2 consecutive quarters, OR (b) RBI starts a rate-cut cycle confirming dovish-monetary tailwind to mid-cap multiples.

**INR hedge stance: UNHEDGED at base sizing.**

Rationale:
- INR forwards / NDF carry is structurally negative; 12mo NDF implies ~3.5-4.5%/yr depreciation already priced (assumption 13). Hedging at cost ≥ assumed structural depreciation eliminates carry-equivalent without removing tail-shock risk.
- Position size (4% NAV) is small enough that INR drag on USD returns (4-12% cumulative over 36mo per assumption 4) is accommodated within the E[R] distribution shown — distributions above are *unhedged*.
- ETF dominant mix means hedge would need to be done at the portfolio level (USD/INR forward / NDF), not at the security level — operationally heavier for marginal benefit.
- **Conditional hedge trigger:** if USD/INR breaks 92 on 30-day-sustained basis (per A4 threshold), implement NDF hedge on 50% of remaining sleeve notional. This is a tail-protective hedge, not a carry-neutralising hedge.
- Alternative for small-account principals: tilt mix toward SMIN (which holds USD-denominated ADR-like exposure where applicable) and away from local-listed single-names; this is a soft hedge via vehicle selection, not a derivative hedge.

### Collapse

This Prediction section contains the proposed Collapse output. Per `architecture.md`, the user is the principal at Collapse. The recommended capital-Collapse:

- **Open India infra sleeve at 4.0% NAV** with mix SMIN 2.4% / LT.NS 0.8% / SIEMENS.NS 0.5% / ABB.NS 0.3%.
- **INR unhedged at base sizing** with conditional NDF hedge trigger at USD/INR > 92 sustained 30 days.
- **Pre-register auto-resize trigger:** 12mo net FII flow < $0bn → downsize 50%; combined < −$10bn AND USD/INR > 92 → close.
- **Cluster cap framing:** counts toward overall Type B aggregate NAV cap (A6); does *not* count toward supply-bottleneck cluster sub-cap (geographically and mechanically uncorrelated to v1 REE / uranium / silver).
- **Outcome window:** 2027-11-15 (~30mo from snapshot, sits in upper half of 18-36mo recognition range).

## Outcome

_Locked until 2027-11-15._

## Reflection

_Locked._
