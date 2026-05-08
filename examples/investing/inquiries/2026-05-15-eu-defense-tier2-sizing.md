---
id: 2026-05-15-eu-defense-tier2-sizing
shape: convergent
collapse_flavour: capital
status: open
scope: "Sizing decision for EU defense second-tier sleeve under Type B archetype."
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

# Inquiry: EU defense second-tier sizing

## Scope

Decide capital allocation to European defense second-tier sleeve. Vehicles: Hensoldt (HAG.DE — sensors pure-play), Kongsberg (KOG.OL — NSM + maritime), Saab (SAAB-B.ST — Gripen + AESA), Leonardo (LDO.MI — conglomerate value), Thales (HO.PA — diversified). Ranked #2 in v2 Type B screen. Demand: NATO 2.5%+ floor, German fiscal-rule special-fund, backlog 2.8-4.5x revenue at second-tier. Recognition gap: EUR-investor familiarity gap; primes already re-rated. Recognition window 12-24mo. Drawdown bound −35%.

In scope: name selection, vehicle mix, sizing, drawdown, asymmetry, sensitivity, EUR/USD overlay note.
Out of scope: US defense primes (already-recognized comp set).

## Assumptions (load-bearing)

Numbered, falsifiable. "Verdict-flipping" tags on assumptions whose failure collapses the recommendation rather than degrading it gradually. Per amendment 2026-05-08 (factor-coverage + feed-gap-promotes-to-assumption), feed-gap proxies are promoted to load-bearing assumptions with explicit confidence haircut.

**Demand-side**

1. **NATO 2.5%+ floor sustained through 2027.** The post-2022 commitment by NATO members to spend ≥2.5% GDP on defense (Hague summit declarations, Nordic accession-driven refreshes, Polish 4.5% baseline) holds through outcome window. Probability ≥0.75 across any plausible US-administration mix because EU members have explicitly de-risked from US-conditional protection. Failure → backlog growth slows but does not reverse; second-tier still has 2-3yr revenue visibility. **Non-flipping** but tail-narrowing.

2. **German Sondervermögen continuation.** The €100bn special fund commits ≥€90bn through 2028; CDU/SPD coalition has signaled successor-fund discussion for 2027-2030 frame; constitutional debt-brake reform momentum is real (2024-2025 amendments carved out defense). Probability of continuation in *some* fiscal-rule-compatible form ≥0.70. Failure (debt-brake hard-snaps back AND no successor fund) → German orderbook for HAG specifically de-rates 25-35% on 2027-2028 visibility. **Verdict-flipping for HAG concentration; non-flipping for diversified basket.**

3. **EU re-armament political durability across election cycles.** EDIS (European Defense Industrial Strategy) procurement-preference for EU-domiciled suppliers survives French legislative cycles, Italian government reshuffles, and any Hungary/Slovakia-style spoilers through 2027. Probability ≥0.65. Failure (procurement-preference watered down to "neutral on origin") → multiple-convergence thesis weakens but backlog economics intact for 24-36mo. **Non-flipping** but recognition-window stretches.

4. **Backlog-to-revenue conversion at second-tier.** Hensoldt 2.8x, Kongsberg 4.5x, Saab ~3.5x, Leonardo ~2.0x, Thales ~2.5x. Conversion proceeds at 28-35% of opening backlog per year (industry norm for defense electronics) without major contract cancellations. Probability ≥0.70. Failure (any one prime cancels a flagship program — IRIS-T, NSM, Gripen-E to a major customer — OR working-capital chokes ramp) → that single name draws down 30-40%; basket -15-20%. **Non-flipping** at basket level.

5. **Recognition-trigger plausibility inside 12mo.** At least one of: (a) US-investor large-cap-fund initiation coverage of HAG / KOG, (b) MSCI Europe defense-sub-index reweighting that pulls passive flows, (c) tier-2 multiple convergence within 25% of prime multiple (currently 14-18x fwd EBIT vs primes 22-28x), or (d) US-Europe interoperability mandate elevating EU sensor/seeker procurement. Probability ≥0.50. Failure → recognition window slides right; **non-flipping**, duration mismatch.

**Risk / context-side**

6. **EUR-denominated entry FX risk (USD-investor lens).** EUR/USD 1.1737 at snapshot. Over 12mo: USD strengthens to 1.05 with probability ~0.20, holds 1.10-1.20 with probability ~0.55, weakens to 1.25+ with probability ~0.25. EUR-side equity returns translate at FX state. Failure (USD strengthens to 1.00-1.05 on US safe-haven bid) → muting of USD returns by 8-12%; structural negative correlation EUR/risk-off mostly offset by defense-name idiosyncratic bid. **Non-flipping** but real drag in S3 / S8.

7. **US-investor familiarity gap is the recognition mechanic.** The 14-18x vs 22-28x multiple gap reflects (a) US-fund mandate restrictions on non-USD primary listings, (b) thinner sell-side coverage, (c) lower passive-vehicle inclusion. The gap closes via US-fund initiation, ADR/dual-listing announcements (Saab USOTC presence already; HAG no ADR yet), and index inclusions — these are slow, structural, observable. Probability that *some* gap-closure trigger fires inside 24mo ≥0.55. Failure → multiple expansion deferred; backlog-burn earnings still grow 12-18%/yr providing fundamental drift. **Non-flipping**; this is the *core* recognition thesis.

8. **Liquidity at sleeve size.** HAG.DE >€8M/day average, KOG.OL >NOK 200M/day (~$18M USD), SAAB-B.ST >SEK 400M/day (~$36M USD), HO.PA >€80M/day, LDO.MI >€60M/day. All clear sleeve sizing at <20bps slippage. Failure → cap individual name allocation; no thesis change.

**Feed-gap-promoted assumptions** (per amendment 2026-05-08 feed-gap-promotes-to-assumption)

9. **Macro proxy (FRED missing).** Assume EU rates / German Bund / EUR-IG-spread regime is approximated by `macro.cfx_eurusd_x` (1.1737), `macro.cfx_tlt` (85.65), `macro.cfx_hyg` (79.86 — credit tight), `macro.cfx_lqd` (108.74), and the news-summarizer FOMC distribution (`politics.fomc_rate_path_may2026`, hold-through-June p≈0.55) as cross-DM proxy. Confidence haircut **−25%** on macro-conditional sub-claims (FX overlay #6 specifically). Resolves when FRED + ECB-equivalent feed hydrates.

10. **Fundamentals proxy (EDGAR stub; ex-US filings unavailable).** Assume HAG / KOG / SAAB / LDO / HO financial fundamentals (backlog disclosure, margin, working-capital trajectory) approximated by Q1 2026 web-search-grade reports + investor-day disclosures. Confidence haircut **−20%** on backlog-conversion claim (assumption 4) and on the multiple-gap measurement (assumption 7). Resolves when ASE/Frankfurt/Oslo/Stockholm/Paris/Milan filings feed registers.

11. **Crowding proxy (no flows feed).** Assume US-fund and EU-pension positioning approximated by first-principles + observable: US-listed defense ETFs (ITA, XAR) hold zero direct EU defense; iShares STOXX Europe 600 Aerospace+Defense ETF (EXX5.DE) AUM ~€1.5bn (vs ITA $7bn) — small relative allocation; HANetf Future of Defence (NATO.L) AUM ~$700M growing fast in 2024-2025; explicit "EU defense" thematic flow trend is positive but not crowded. Confidence haircut **−15%** on recognition-narrowness (assumption 5/7). Resolves when flows / 13F-equivalent feed registers (architect adjustment A3).

12. **No live broker / FX-rate feed.** Assume entry executes within ±3% of HAG.DE €60-65, KOG.OL NOK 1300-1400, SAAB-B.ST SEK 450-480, LDO.MI €40-44, HO.PA €260-280 reference levels at EUR/USD 1.17. Confidence haircut **−10%** on entry-price assumption. Resolves when broker feed wires.

**Drawdown-bound construction** (per parent assumption #10 and amendment 2026-05-08)

13. **Drawdown bound is forward thesis-failure path** = max plausible 12-month decline conditional on assumption (2) [German Sondervermögen failure] OR (4) [backlog cancellation event] failing severely, weighted by joint probability and macro-S3 stress overlay. Quantified: −35% sleeve-aggregate; −45% HAG.DE worst-case (most German-dependent); −35% KOG.OL (most diversified second-tier with offshore/maritime); −35% SAAB-B.ST; −40% LDO.MI (Italian-political tail); −30% HO.PA (largest, most diversified). Honoured at sleeve level.

## Graph references

Pulled from snapshot 2026-05-08T09:00Z. One-line relevance each.

**Strategy**

- `strategy.type-b.current_candidates_v2[rank=2]` — this inquiry's parent claim; carries demand-chain (German Sondervermögen, Polish 4.5% GDP, EDIS procurement preference), bottleneck (skilled-labour + classified-clearance + ASIC fab access; backlog 2.8-4.5x revenue), recognition window 12-24mo, asymmetry ~3:1, drawdown bound −35%, demand-floor-recession=true.
- `strategy.portfolio-architecture.scenario_set` — sleeve mapping across S1-S8: defense second-tier wins under S2 (stagflation, p=0.18, real-asset / commodity bid lifts pricing power), S5 (geopolitical escalation, p=0.10, direct demand expansion), S6 (reflation, p=0.08, cyclical multiple expansion). Mildly negative under S3 (recession + cuts, p=0.14, but demand-floor-recession=true caps drawdown), S4 (AI capex peak, p=0.20, neutral — no tech-cycle dependence), S7 (status quo, p=0.06, fundamental drift only). S8 tail (p=0.02) — defense is partial safe-bid but tier-2 small/mid-cap gaps. Sleeve-weighted scenario expectation positive and largely macro-insensitive.
- `strategy.portfolio-architecture.balance_assessment.holes[H3]` — no flows feed; reflexivity probe blind. Drives haircut #11.
- `strategy.portfolio-architecture.balance_assessment.holes[H7]` — no FX/USD-funding-shock exposure tracked; drives FX-overlay framing in assumption #6.
- `strategy.portfolio-architecture.proposed_adjustments[A6]` — tighten Type B sizing discipline (cluster cap). Cluster context: REE 1.5% + uranium 4% + silver 4% = 9.5% of NAV already in Type B. EU defense + phosphate (#1 v2) must respect ~8-10% incremental cap unless explicitly raised. This sleeve sizes inside that cap.

**Themes**

- `themes.ai-capex-cycle` — not load-bearing here. Defense second-tier is one of the few Type B candidates with **no** AI-capex factor exposure, which is portfolio-balance-positive (closes part of architect hole H2: AI-capex factor over-concentration).
- `themes.capital_framework_overhaul` — not load-bearing.
- `themes.enforcement_normalization` — not load-bearing.

**Politics**

- `politics.us-china-tariff-regime-2026` (status-quo p=0.50, escalation p=0.35, partial-rollback p=0.15) — escalation indirectly supports the EU-defense thesis via increased pressure on European strategic-autonomy spending. Not load-bearing but directionally supportive.
- `politics.regulatory_deregulation_posture` — neutral; EU defense procurement is driven by EU-level EDIS rather than US Fed posture.
- `politics.fomc_rate_path_may2026` (hold-through-June p=0.55, fuzz_halo VERY HIGH) — neutral for sleeve directly; matters only via FX path (assumption 9 proxy).
- **Gap (load-bearing):** no `politics.eu-defense-budget-trajectory` or `politics.german-fiscal-rule-2026-2030` node in graph. Web-search supplements; lower provenance weight. Promoted to assumption #2 with no separate haircut beyond #10.

**Macro**

- `macro.cfx_eurusd_x` 1.1737 — load-bearing. Defines FX overlay risk for USD investor (assumption #6).
- `macro.cfx_uup` 27.41, vol 5.9% — DXY proxy steady; no acute USD-strength regime; supports the 1.10-1.20 base FX path.
- `macro.cfx_tlt` 85.65 — long-duration soft, supports "no acute recession pricing" (S3 not modal); consistent with backlog-burn thesis getting fundamental drift.
- `macro.cfx_hyg` 79.86, vol 5.37% — HY spreads tight; backdrop benign for industrial/defense capex.
- `macro.cfx_lqd` 108.74 — IG credit firm; corporate-cost-of-capital benign for sleeve.
- `macro.cfx_dbc` 30.25 — broad commodities mid-vol; consistent with no acute supply-shock regime.

**Sentiment**

- `sentiment.fed_policy_stance` (mean +0.05, sd 0.25, fuzz_halo HIGH) — neutral; folds into haircut #9.

**Technicals**

- `technicals.spy` 731.58, vol 15.94% — broad equity vol modest; no immediate market-stress liquidation risk.
- `technicals.iwm` 282.26, vol 21.22% — small-cap vol elevated; KOG.OL and HAG.DE behave with mid-cap beta in EU peer set.
- `technicals.eem` 66.59, vol 28.7% — EM tape live; not directly relevant but supports "global risk-on backdrop."
- No `technicals.exx5_de` (STOXX Europe Aerospace+Defense ETF) feed yet; web-search reference: ~+45% YoY 2025, primes-driven; tier-2 lagging.

**Fundamentals**

- `fundamentals.*` — stub only. Drives haircut #10. HAG / KOG / SAAB / LDO / HO fundamentals qualitative-only at this snapshot.

**Graph gaps that limit confidence (carried + new)**

- FRED missing — assumption #9.
- EDGAR / EU-filings stub — assumption #10.
- No flows feed — assumption #11.
- No EU-budget / German-fiscal-rule node in `politics/` — assumption #2 carries the load (no separate haircut beyond #10).
- No CBOE / EUREX options feed — implied vol on HAG / KOG / HO unknown; option-overlay sizing deferred.
- No live FX-cross feed — entry FX assumption #12 holds the load.

## Self

- **self.capability** — Vehicle-aware sizing on EU-listed defense second-tier within Type B. Web-search and graph snapshot available; no live broker, options, EU-filings, or flows feed. Cannot run live factor regression, FX-hedge-overlay attribution, or EUR-IG-spread-driven discount-rate sensitivities from this seat. Can construct a forward thesis-failure drawdown distribution + scenario-weighted return distribution + a coarse FX overlay.
- **self.calibration** — **No prior closed Type B inquiries on this instance**; no track record. Industry prior: Type B hit-rate ~0.30-0.40, payoff multiple 3-8x. EU-defense second-tier has additional informational disadvantage relative to US-listed equivalents (US-investor seat); apply an extra **−0.10 calibration haircut** on multiple-expansion timing. Treat all numbers as priors awaiting outcome data; E[R]/E[risk] is a *relative ranking signal*, not a precise expectation.
- **self.taste** — Bias toward demand-floor theses surviving recession (assumption: defense-budget commitments are stickier than consumer discretionary cycles); bias against single-name execution risk under stub fundamentals (drives basket of 4-5 names rather than HAG concentration); bias against EUR/USD timing trades (FX overlay framed as risk, not expression); bias against narrative-only theses (passes boring-story test: backlog conversion is dull mechanical accounting); bias against any sleeve concentration that adds materially to existing implicit factor bets — and EU defense is *factor-orthogonal* to existing AI-capex / US-mega-cap tilts, which is portfolio-positive.

## M-nodes (sequence)

1. **`m.probe.scope`** — sharpened: 4-name basket (HAG / KOG / SAAB / LDO / HO with one of LDO/HO held back); sizing as NAV % range with confidence; drawdown distribution as forward thesis-failure path; FX-overlay note required; brittle-assumption identification mandatory; cluster-cap discipline binds.
2. **`m.probe.prior-art`** — methods.md (Kelly with haircut, drawdown bound, scenario stress, factor exposure, vol-targeting per name), blind-spots.md (narrative seduction → boring-story test passes; recency → primes already re-rated, second-tier may be next-cycle not this-cycle; tail neglect → German fiscal-rule binary; implicit factor bets → defense-tier-2 partly is a "EU strategic autonomy" factor; crowding → structurally blind, haircut applied), strategies.md Type B criteria (all five hard gates passed at parent v2).
3. **`m.probe.world`** — graph snapshot 2026-05-08T09:00Z; FRED gap → haircut #9; EU-filings stub → haircut #10; flows missing → haircut #11; FX feed missing → haircut #12. Web-search supplements: NATO Hague communiqué 2025-2026, German Sondervermögen disbursement schedule (BAAINBw), Saab Q1 2026 backlog disclosure (SEK ~190bn), Hensoldt FY25 backlog (~€7.5bn) and FY26 guide, Kongsberg KDA backlog (NOK ~120bn), Leonardo Eurofighter / EuroMALE updates, Thales Q1 sensors revenue mix, EXX5.DE / NATO.L AUM trajectory.
4. **`m.probe.edges`** — factor-coverage walk (per amendment 2026-05-08 factor-coverage-checklist):
   - **macro (rates / growth / inflation / fiscal)** — proxy via `macro.cfx_*`. Sleeve mildly positively exposed to fiscal-expansion regime (defense procurement is fiscal); negatively exposed to acute EUR-IG-spread blowout (corporate cost-of-capital). Net: macro-secondary; haircut #9 applied. Status: probed.
   - **geographic (jurisdiction / sanctions / trade)** — load-bearing. Direct exposure to German Sondervermögen continuation (assumption 2), EDIS procurement preference (assumption 3), French/Italian political continuity. Indirect tailwind from US-EU strategic-autonomy spending. **Verdict-flipping factor for HAG concentration sits here.** Status: probed; load-bearing.
   - **regime (vol / liquidity / dispersion)** — `technicals.iwm` vol 21.22% suggests EU mid-cap defense behaves with mid-cap beta. Sleeve realised vol historically 22-30% per name; basket-level 18-22% expected. Status: probed.
   - **correlation structure** — sleeve correlates positively with: EU industrials, USD weakness (negative for USD-investor return), US defense primes (RTX/LMT) on geopolitical-spike days. Correlates negatively with: long-duration (S3 path), AI-mega-cap (uncorrelated within noise — *factor-orthogonal*, the desired property). At portfolio level, sleeve adds a **EU-fiscal / strategic-autonomy** factor not currently held in book; closes part of architect hole H2 (AI-capex over-concentration) by being orthogonal. Status: probed; portfolio-positive.
   - **flows (positioning / crowding / fund flows)** — **structurally blind**; haircut #11 applied. First-principles: US-fund mandate constraints keep allocation low; EU-pension allocation rising 2024-2025 from low base; thematic ETFs (NATO.L, EXX5.DE) growing AUM but absolute size small. Crowding probability low-to-moderate; the *recognition mechanic* relies on positioning increasing, so sizing must respect that the gap-closure path is itself the flow event. Status: probed with structural blindness flag.
   - **themes (narrative state / recognition stage)** — primes already recognised (Rheinmetall +5x off 2022 base; BAE +2.5x); second-tier partial recognition (HAG +3x off 2022 IPO base, but multiple gap to primes still 30-40%). Recognition stage = mid-early for tier-2; the wedge is multiple-convergence, not a fundamental discovery. Status: probed; consistent with narrow-window gate (12-24mo).
   - **reflexivity (positioning ↔ price ↔ narrative)** — moderate. Recognition trigger is positively reflexive (US-fund initiation → multiple expansion → index inclusion → passive flows → more analyst coverage). Symmetric on the downside (Ukraine-ceasefire narrative → tactical risk-off → tier-2 derates faster than primes despite better fundamentals due to liquidity). Sleeve at *mid-cycle* recognition point; less reflexive than REE pre-cascade but more reflexive than recognised primes. Status: probed.
   - **liquidity / capacity** — all five names clear $8-50M USD/day; sleeve at 2-4% NAV well within capacity. Assumption #8 holds. Status: probed; not load-bearing.
5. **`m.reframe`** — not invoked; scope held. (One reframe candidate considered and rejected: "treat sleeve as a EUR-equity expression with defense-narrative wrapper" — declined because the multiple-gap-closure mechanism is name-specific and would not survive an EXX5.DE ETF wrapper that includes already-recognised primes.)
6. **`m.test.feasibility`** — capability OK (within seat); constraint OK (no mandate against EU-listed sleeves at <5% NAV; broker access assumed via global-equity desk); budget OK (sleeve fits within ~8-10% Type B incremental cap; current cluster at 9.5% means EU defense + phosphate must respect tightened budget); data quality MEDIUM (four feed-gap haircuts applied); FX risk identified and bounded. Feasible to size.
7. **`m.collapse`** — **propose for human gate**. Recommended: capital Collapse at sleeve = **3.0% NAV** (range 2.0-4.0%) split across 4 of 5 names (drop LDO; concentrate on HAG / KOG / SAAB / HO). Do NOT execute Collapse from this section; status remains `open` until human gate.

## Prediction (convergent)

Distributions are sleeve-aggregate (proposed weights HAG 30% / KOG 25% / SAAB 25% / HO 20%; LDO excluded from primary sleeve, see name-mix rationale below) unless noted. All numbers are priors with feed-gap haircuts already folded in; treat as ranking signal, not precise expectation. EUR-side returns; USD-investor view applied separately under FX overlay.

### Expected return — 12 month (EUR-side, USD-translated)

- **Shape:** moderately right-skewed unimodal (less bi-modal than REE because the recognition trigger is multi-trigger and continuous rather than binary). Modes near +12-18% drift case and +35-45% multiple-convergence case.
- **Mean (EUR):** +18%
- **SD (EUR):** ~26%
- **Quantiles (EUR):**
  - p05: −24%
  - p25: 0%
  - p50: +17%
  - p75: +34%
  - p95: +58%
- **USD-translation overlay:** mean USD return ≈ +16% (EUR mean ≈ +18% × FX expectation 0.985); p05 widens to −28% (FX adds 2-4pp left tail under USD-strength path); p95 narrows to +56%. **FX overlay decision: leave UNHEDGED**. Rationale below.
- **Probability of multiple-convergence trigger inside 12mo (assumption 5):** 0.50 → conditional return given trigger ≈ +34% (sleeve-aggregate, EUR); conditional return given no trigger ≈ +9% (drift case from 12-18% earnings growth + small multiple drift).

### Expected return — 24 month (EUR-side, USD-translated)

- **Shape:** still right-skewed, modes diverging; tails wider but less than REE (asymmetry ~3:1 vs REE's ~7:2).
- **Mean (EUR):** +38%
- **SD (EUR):** ~42%
- **Quantiles (EUR):**
  - p05: −32%
  - p25: +6%
  - p50: +35%
  - p75: +62%
  - p95: +98%
- **USD-translation:** mean USD ≈ +35% (FX expectation drift toward 1.15-1.20 base path); p95 USD ≈ +103% if EUR firms toward 1.25.
- **Probability of multiple-convergence trigger inside 24mo:** 0.72. Conditional given trigger ≈ +52% sleeve EUR; conditional given no trigger ≈ +18-22% (pure backlog-burn earnings compounding).

### Expected risk — drawdown distribution (forward, thesis-failure-conditional)

Drawdown = max peak-to-trough sleeve return over 12-month window (NOT historical realised drawdown; per parent assumption #10).

- **p50 drawdown:** −12% (typical realised path includes a ~10-15% pullback even on the winning thesis from generic risk-off / Ukraine-ceasefire-headlines volatility)
- **p90 drawdown:** −28%
- **p95 drawdown:** −35% (matches parent drawdown bound at sleeve level)
- **p99 drawdown:** −45%
- **Tail behaviour:** left tail is moderately fatter than Gaussian but **less fat than REE or tin** because (a) backlog-with-cancellation-penalties provides revenue floor, (b) defense-budget commitments are politically stickier than commodity-price cycles, (c) basket diversification across 4 names + 4 EU jurisdictions reduces single-name event tail. Joint failure of assumption 2 (Sondervermögen) AND a Ukraine-ceasefire-driven budget pause inside 12mo has probability ≈ 0.06 and conditional drawdown ≈ −40-50% sleeve-aggregate.
- **Single-name worst-case drawdowns under thesis-failure path:** HAG.DE −45% (most German-dependent), KOG.OL −35% (NSM + maritime diversification softens), SAAB-B.ST −35% (Gripen-E backlog plus AESA), HO.PA −30% (largest, most diversified, partial civilian / cyber offset), LDO.MI −40% (excluded from primary sleeve due to Italian-political tail).
- **Basket vs concentrated comparison.** A HAG-concentrated sleeve (60%+ HAG) would have p90 drawdown ~ −35%; the diversified 4-name basket reduces p90 to −28% with only ~3pp upside reduction in p95. Diversification value clearly positive.

### E[R] / E[risk] ratio

- **Definition used:** E[R, 12mo, USD] / E[|drawdown|, p90] = +16% / 28% = **0.57**
- **Alternative (24mo numerator):** +35% / 28% = **1.25**
- **Kelly-style heuristic check:** with edge ≈ 0.18 and variance ≈ 0.26², full-Kelly fraction ≈ edge / variance ≈ 2.66, but Kelly assumes well-estimated distribution. Per methods.md Kelly cautions: apply 0.25× Kelly haircut + 0.5× first-Type-B-on-instance haircut + 0.85× EU-data-thinness haircut (extra). Result: ≈ 0.28× of NAV ≈ 28% (gross Kelly with three haircuts). **Drawdown discipline + cluster cap binds well before Kelly** (cluster cap leaves ~5-7% NAV for EU defense + phosphate combined; phosphate ranked #1 v2 takes priority share).
- **Comparison to siblings:** REE reconciled ratio 0.20-0.25 (12mo), 0.85 (24mo); EU defense 0.57 (12mo), 1.25 (24mo). **EU defense ranks better on 12mo than REE post-reconciliation** because the recognition mechanic is multi-trigger and continuous rather than binary, and the drawdown is less fat-tailed. Within the v2 set, EU defense ratio is competitive with phosphate (#1 v2).
- **Verdict:** ratio is favourable on both horizons; sleeve is sizeable within cluster cap.

### Sensitivity — the SINGLE brittle assumption

**Assumption #2 — German Sondervermögen continuation in some fiscal-rule-compatible form through 2028.**

This is the brittle assumption rather than #1 (NATO floor) because: (a) NATO 2.5% is now broadly priced and politically stickier across multiple member states; (b) Sondervermögen is single-jurisdiction and depends on a constitutional debt-brake reform path that is binary; (c) HAG concentration has direct exposure where SAAB / KOG / HO have only second-order exposure.

- **Threshold value:** P(Sondervermögen non-continuation AND no successor fund inside outcome window) > **0.30**.
- At P(non-continuation) = 0.20 (current prior, complement of 0.80 implied by assumption #2's ≥0.70), E[R, 12mo, USD] ≈ +16%, sleeve sizing 3.0% NAV stands.
- At P(non-continuation) = 0.30, E[R, 12mo, USD] drops to ≈ +6%, p90 drawdown widens to −34%, ratio drops to ~0.18 → cut sleeve to 1.5-2.0% NAV and over-weight away from HAG.
- At P(non-continuation) = 0.45, E[R, 12mo, USD] turns negative ≈ −5%, p90 drawdown −38%; **verdict flips → cut HAG entirely; reduce sleeve to ≤1.0% NAV concentrated in KOG + SAAB (least German-dependent)**.

**Assumption #1 (NATO 2.5% floor) is not the brittle assumption** — failure is non-flipping at basket level given backlog-with-cancellation-penalties; degrades the recommendation gradually rather than flipping it.

**Trip-wires (close monitoring required, not waiting for outcome window):**
- German Bundestag debate on debt-brake amendment expiry / Sondervermögen successor → assumption #2 stress test.
- Major Ukraine ceasefire announcement with EU budget-pause language → assumption #1 stress test.
- French / Italian government collapse with anti-EDIS rhetoric → assumption #3 stress test.
- HAG / KOG / SAAB Q2/Q3 2026 earnings showing book-to-bill < 1.0 → assumption #4 stress test.
- US-fund initiation report on HAG / KOG → confirms recognition mechanic (assumption #5/#7); upward re-rate.
- EUR/USD breaks above 1.25 or below 1.05 → FX overlay sensitivity (assumption #6).

### Sizing recommendation

**Recommended sleeve size: 3.0% NAV (range 2.0-4.0%, confidence ~0.55).**

**Cluster discipline check.** Existing Type B cluster: REE 1.5% (post-reconciliation cut from 2.5%) + uranium ~4% + silver ~4% = 9.5%. v2 candidates incremental cap ~8-10% NAV total. Phosphate (#1 v2) deserves first claim on incremental capacity (~3.5-4% NAV). EU defense (#2 v2) at 3.0% NAV brings v2-incremental to ~6.5-7%, leaving small residual for India infra / helium / others. **Within cluster cap; phosphate + EU-defense is the load-bearing pair of the v2 sleeve.**

Vehicle (name-mix) split rationale:

| Vehicle | NAV % (mid) | Range | Rationale |
|---|---|---|---|
| HAG.DE (Hensoldt) | 0.90% | 0.50-1.30% | Cleanest sensors pure-play; highest torque to multiple-convergence; **but** highest German-Sondervermögen concentration so capped sub-1.0%. Recognition trigger most likely to fire here first (US-fund initiation, ADR consideration). |
| KOG.OL (Kongsberg) | 0.75% | 0.40-1.10% | NSM (Naval Strike Missile) + maritime + space; 4.5x backlog/revenue (highest in basket); diversified end-markets including offshore O&G optionality. Lower German-fiscal-tail beta than HAG. NOK-denominated adds modest FX diversification within EUR-defense thesis. |
| SAAB-B.ST (Saab) | 0.75% | 0.40-1.10% | Gripen-E + AESA + Carl-Gustaf + GlobalEye AEW&C. SEK-denominated. Smallest German exposure in basket; political-tail diversification. Some US-investor familiarity via existing OTC presence — partial recognition already. |
| HO.PA (Thales) | 0.60% | 0.30-0.90% | Largest, most diversified (defense + civilian aerospace + cyber + ground transportation). Lowest single-name execution risk; lowest torque to recognition trigger. Acts as basket "anchor" reducing realised vol. |
| LDO.MI (Leonardo) | **0.0% (excluded from primary sleeve)** | 0.0-0.50% | Excluded from primary basket. Italian political-tail risk + holding-company complexity (DRS US-listed sub, AgustaWestland exposure to civilian helo cycle). Multiple gap exists but is partly a *deserved* discount. Optional 0.25-0.50% add only if dedicated probe closes the political-tail and conglomerate-discount questions. |

**Confidence:** ~0.55 sleeve recommendation; ~0.50 vehicle-split mid-points.

**EUR/USD overlay note — UNHEDGED rationale.** Recommend leaving the sleeve unhedged for the following reasons:
1. **FX-thesis correlation.** EU defense is a EUR-fiscal-expansion thesis; EUR-strength is a *complementary* expression of the same regime, not a separate risk. Hedging the EUR exposure removes part of the bet.
2. **Hedge cost.** EUR/USD 12mo forward implies ~150-180bp annual carry against the USD investor (US rates > EU rates currently); systematic hedging burns ~150-180bp/yr on a thesis where 12mo expected return is ~16-18%. Net hedge-adjusted return reduces by ~10% of expected return.
3. **Asymmetric FX-tail behavior.** Under stress regimes that hurt the equity thesis (Ukraine ceasefire → EU-defense-budget pause), EUR typically also weakens — i.e., the FX moves *with* the equity loss, partially natural-hedging. Conversely, EUR-strength regimes (ECB hawkish, EU growth surprise) typically coincide with positive equity moves. The sleeve already has a soft natural hedge.
4. **Sizing discipline as primary risk control.** At 3.0% NAV, even a 12-15pp adverse FX move adds at most −0.45% to total NAV — within drawdown budget without explicit hedge.
- *Trip-wire to revisit*: if EUR/USD breaks above 1.25 (significant USD-side gain) consider partial 30-50% hedge to lock translated gains; if below 1.05 (USD safe-haven flight) **do not** hedge — by then the FX move has happened, and the unhedged position becomes the recovery vehicle.

**Cluster constraint (per architect proposed-adjustment A6).** Verified above: 9.5% existing + ~3.5-4% phosphate + 3.0% EU defense = ~16% Type B total, of which v2-incremental is ~6.5-7%. **Within ~8-10% v2-incremental cap.** Architect must explicitly raise the cap before adding India-infra / helium / others at meaningful size; this inquiry takes its 3.0% under that interpretation.

**Do NOT collapse here.** Status remains `open` until human gate. Recommendation packaged for the architect / human principal at Collapse.

## Outcome

_Locked until 2027-05-15._

## Reflection

_Locked._
