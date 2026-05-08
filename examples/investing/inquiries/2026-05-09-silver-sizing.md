---
id: 2026-05-09-silver-sizing
shape: convergent
collapse_flavour: capital
status: open
scope: "Sizing decision for silver sleeve (industrial-deficit thesis) under Type B archetype."
parent_inquiry: 2026-05-08-type-b-screen
graph_snapshot: 2026-05-08T09:00Z
outcome_window: 2027-05-09
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

# Inquiry: Silver sizing (industrial-deficit thesis)

## Scope

Decide capital allocation to silver sleeve. Vehicles: PSLV (allocated bullion) > SLV (liquidity); SIL for miner torque if drawdown bound respected. Ranked #3 in 2026-05-08 Type B screen. Demand drivers: solar PV (TOPCon/HJT loading 2–3x PERC, ~20% of demand growing), AI datacenter electrification, EV power electronics, 5G. 4-year structural deficit (150–200 Moz/yr). Supply rigidity: ~70% byproduct of base metals, no rapid response to price.

In scope: bullion vs miner mix, sizing, drawdown, asymmetry, sensitivity.
Out of scope: gold-correlation overlay (deferred).

## Assumptions (load-bearing)

1. **Solar PV growth trajectory.** Global PV installations grow ≥12% YoY 2026–2027 (base case 14%; bear 6%). Failure (PV growth <8% sustained) collapses the dominant industrial demand pillar — silver industrial demand reverts to flat/declining. Confidence 0.65; resolves on H1 2026 IEA/SPE installation prints.
2. **TOPCon/HJT cell-mix evolution + thrifting cap.** TOPCon + HJT combined share of new cell shipments rises from ~70% (2025) to ≥85% by 2027, with per-cell silver loading remaining ≥1.8x PERC baseline net of incremental thrifting. Failure path: a thrifting breakthrough (copper plating commercialised at scale, or silver-loading reduction >40% on TOPCon) compresses per-watt silver content faster than installation growth. Confidence 0.55; resolves on Silver Institute / CRU loading surveys + cell-maker capex disclosures.
3. **Silver Institute deficit estimate accuracy (±25%).** 2026 deficit lands in 100–230 Moz/yr range (point 165). Estimate is informed by industry survey + ETF flows; methodology has historically mis-estimated above-ground stocks by ~15–20%. Failure: deficit revised below 80 Moz on stock revisions or demand softening — recognition trigger fails to fire. Confidence 0.60.
4. **Base-metal byproduct supply elasticity is low.** ~70% of mine silver is byproduct of Pb/Zn/Cu/Au; capex response to silver price is structurally weak (host-metal economics dominate). Even at $40+/oz, primary supply uplift is <5% over 24 months. Failure: a Pb/Zn/Cu price cycle independently lifts host-metal capex and pulls silver supply with it — supply rigidity assumption breaks. Confidence 0.75.
5. **Gold-correlation regime stability.** Silver retains its conditional-on-gold beta (β≈1.5–2.0 in gold up-regimes; correlation 0.7–0.85). With GLD vol 28% and at all-time highs (`technicals.gld` 431.68), silver's expected pull-forward via the gold/silver ratio remains intact. Failure: gold tops or de-correlates; silver loses its monetary tailwind and trades on pure industrial fundamentals. Confidence 0.55; this is the most fragile macro link.
6. **Recognition latency 3–12 months** (per Type B screen assumption #9, narrowed for silver given partial recognition already in tape). Confidence 0.55.
7. **Drawdown bound is 12-month worst-plausible** (per Type B screen assumption #10). PSLV/SLV bounded at −25% (cash-cost floor ~$15/oz top-quartile); SIL bounded at −45% (miner book value at depressed silver). Confidence 0.70.
8. **Liquidity is sufficient** at PSLV/SLV/SIL for $50k–$5m position sizing without material slippage (per Type B screen assumption #8). Confidence 0.85.

**Feed-gap promotions to assumption (per `amendments.md` 2026-05-08 discipline):**

9. **FRED feed missing → assume real rates path approximated by `macro.cfx_tlt` + `sentiment.fed_policy_stance` proxies.** Real-rate sensitivity of silver is high; without TIPS / 10Y real-yield data, the macro overlay carries a confidence haircut of 0.30. Resolves when FRED hydrates.
10. **No flows / positioning feed → assume crowding is moderate and silver-ETF positioning approximated by inferred GLD/SLV inflow asymmetry.** Reflexivity probe is structurally blind. Confidence haircut 0.25. Resolves when flows feed registers (`A3` in portfolio architecture).
11. **EDGAR feed stub → SIL miner balance-sheet stress assumed approximated by qualitative 2024–2025 industry reports + price action.** Confidence haircut 0.20 on miner-specific drawdown floor. Resolves when EDGAR hydrates.
12. **No CBOE / options feed → assume implicit tail-hedge availability via PSLV (allocated, NAV-floored) rather than explicit options.** Confidence haircut 0.15 on tail-risk handling. Resolves when CBOE feed registers.

## Graph references

Pulled from snapshot 2026-05-08T09:00Z (delta from parent 2026-05-08T05:15Z is portfolio-architecture node):

**Technicals (silver-relevant):**
- `technicals.gld` 431.68, vol 28.0% — gold at all-time highs; silver/gold ratio extended → mean-reversion pull-forward.
- `technicals.dbc` 30.25, vol 23.1% — broad-commodity tape mid-vol, supportive.
- `technicals.uup` 27.41, vol 5.9% — DXY steady; weak-USD tailwind absent (mild negative).
- `technicals.tlt` 85.65, vol 8.6% — long-duration proxy soft; real-rate environment moderately silver-supportive but FRED gap caps confidence.
- `technicals.xlb` 51.40, vol 17.1% — materials sleeve quiet; SIL miners would be more torque-y than tape suggests.
- `technicals.xli` 174.00, vol 24.8% — industrial demand backdrop intact.

**Macro:**
- `macro.cfx_gld` 431.68 — duplicate of GLD as commodities proxy; reinforces gold leg.
- `macro.cfx_dbc` 30.25 — broad commodity proxy.
- `macro.cfx_uup` 27.41 — USD proxy.
- `macro.cfx_tlt` 85.65 — duration / real-rate proxy (FRED-substitute).

**Themes:**
- `themes.ai-capex-cycle` (p_peak_18mo 0.45 / p_18-36mo 0.35 / p_no_peak 0.20, conf 0.55) — datacenter electrification powers an independent industrial silver demand floor; if AI capex peaks <18mo (S4 in scenario set) silver industrial demand softens at the margin but does NOT collapse (PV remains dominant).

**Sentiment:**
- `sentiment.fed_policy_stance` mean 0.05, sd 0.25, fuzz HIGH — neutral-slight-hawkish prior; treat any rate-conditional silver lift as low confidence.

**Politics:**
- `politics.fomc_rate_path_may2026` — discrete distribution: hold-through-June 0.55, cut-25bp-June 0.20, hold-then-cut-H2 0.15. Real-rate path is mildly silver-supportive in the H2-cut leg.

**Strategy / portfolio:**
- `strategy.type-b.current_candidates[rank=3]` — silver entry; this inquiry is the child sizing.
- `strategy.portfolio-architecture.scenario_set` — silver wins in S2 (stagflation, p=0.18), S5 (geopolitical, p=0.10), S6 (reflation, p=0.08). Loses in S3 (recession + faster cuts, p=0.14) and partially S4 (AI capex peak, p=0.20). Cumulative silver-positive scenario weight ≈ 0.36; silver-negative ≈ 0.34; rest neutral.
- `strategy.portfolio-architecture.holes.H6` — "no copper / industrial-metal convex exposure"; silver partially closes this hole as a base-metal-byproduct-rigidity play.
- `strategy.portfolio-architecture.balance_assessment.concentrations` — silver does NOT add to AI-capex factor (uncorrelated mechanism) NOR to US-mega-cap factor (commodity vehicle); it adds to the "supply-bottleneck industrial cluster" (4 of 5 Type B). This is a flagged concentration — sizing must respect cluster cap (A6).

**Edges (relevant):**
- `edge.crowding-to-drawdown` (silver-ETF analogue) — strength bounded mean 0.25; silver positioning unobservable without flows feed (H3 / assumption 10).
- Implicit edge: gold → silver beta conditional on monetary regime; not yet first-class in `graph/edges.md` (candidate to land via this inquiry).

**Graph gaps actively limiting confidence (per amendments discipline):**
- FRED missing (real rates) → assumption 9.
- Flows missing (crowding/positioning) → assumption 10.
- EDGAR stub (miner balance sheets) → assumption 11.
- CBOE missing (options/tail) → assumption 12.

## Intent

Output sizing recommendation, vehicle mix (bullion / miner split), E[R]/E[risk], brittle assumption. Confidence: medium (0.55) on the Collapse recommendation; higher (0.65) on the directional verdict that silver passes the "size something" gate; lower (0.45) on precise NAV %.

## Self

- **self.capability** — Vehicle-agnostic convergent sizing. Can run scenario-weighted return calc, drawdown bound from physical-floor logic, asymmetry ratio. Cannot run live factor regression on silver vs portfolio (no broker feed → portfolio.current empty); cannot price options-implied tail (no CBOE feed). Web_search available for recent silver-loading studies and Silver Institute prints.
- **self.calibration** — No prior closed Type B sizing inquiries on this instance; no track record. Inherit parent's base-rate assumption: Type B disciplined-screen hit-rate 0.30–0.40, payoff multiple on hits 3–8x. Apply additional haircut on silver-specific given gold-correlation fragility (assumption 5).
- **self.taste** — Bias toward bullion-heavy mix when the demand-deduction chain is real-asset and the miner equity adds operational/jurisdictional risk on top of commodity exposure. Bias against miner-heavy when EDGAR feed is stub (cannot validate balance-sheet stress). Bias toward respecting drawdown bounds *strictly* — sizing is the only invariant under the Type B archetype that prevents thesis-failure breaking the book. Bias against treating silver as a pure monetary trade given assumption 5 fragility — the industrial leg must carry weight.

## M-nodes (sequence)

1. `m.probe.scope` — sharpened: convergent sizing, single Collapse output (capital), bullion+miner split, with sensitivity. Out-of-scope held: gold-correlation overlay deferred to a separate inquiry.
2. `m.probe.prior-art` — `methods.md` (Kelly with haircut, drawdown bound, scenario stress, factor-exposure check); `blind-spots.md` (narrative seduction — boring-story test on silver; tail neglect — fat-tail in miner; recency — last 12mo silver tape; implicit factor — silver as gold-beta in disguise); `strategies.md` Type B drawdown-bounded criterion; `amendments.md` 2026-05-08 factor-coverage and feed-gap-to-assumption disciplines applied.
3. `m.probe.world` — graph snapshot read; web_search supplements: Silver Institute 2025 World Silver Survey deficit estimate, TOPCon/HJT silver-loading studies (Fraunhofer / ITRPV), copper-plating commercialisation status, Pan American / Hecla / First Majestic 2025 production guidance.
4. `m.probe.edges` — **factor-coverage walk per amendments 2026-05-08 discipline:**
   - **macro (rates, growth, inflation, fiscal)** — real-rate sensitivity high; FRED missing → assumption 9 with 0.30 haircut. Inflation regime moderately supportive (S2 stagflation 0.18). Fiscal posture not load-bearing for silver.
   - **geographic (jurisdiction, sanctions, trade)** — Mexico is largest producer (~25% mine supply); cartel/security risk on Mexican primary miners (First Majestic) is non-trivial. China is largest fabricator; tariff regime affects industrial offtake margins. Not trade-sanction-driven the way REE is.
   - **regime (vol, liquidity, dispersion)** — silver vol regime mid-elevated (proxied by GLD 28% + materials cluster); liquidity ample on PSLV/SLV; dispersion across miners is high (SIL constituents range from cash-cost-protected to leveraged-and-stressed).
   - **correlation structure** — gold-correlation regime stability is assumption 5 (most fragile). Silver also correlates to industrial cluster (XLB, copper) in industrial-led rallies and to GLD in monetary-led rallies — different regimes, different beta. **Implicit factor bet flagged**: silver position is partly a gold-beta tilt; sizing must net against any GLD position to avoid double-counting.
   - **flows (positioning, crowding)** — H3 hole, assumption 10 with 0.25 haircut. ETF inflows have been muted vs gold; positioning likely under-crowded relative to gold but unverifiable.
   - **themes (narrative state, recognition stage)** — silver is partially recognised; Silver Institute deficit narrative is in trade press, less so in mainstream. Recognition triggers (assumption 6): gold/silver ratio compression <70x, ETF flow break above 2020 levels, LBMA delivery stress.
   - **reflexivity** — recognition-window thesis is reflexive: ETF inflows pull above-ground stock down → spot price up → more ETF inflows. With flows feed missing, cannot locate position on curve.
   - **liquidity / capacity** — assumption 8 affirmed; PSLV/SLV liquid; SIL adequate; single-name primary miners (PAAS, HL, AG) are size-constrained at >$5m.
5. `m.reframe` — None. Scope held; sizing decision is the right shape of output for a Type B child convergent capital Collapse.
6. `m.test.feasibility` — capability (sizing math executable) × constraint (drawdown bounds quantified) × budget (NAV % proposed within mandate-implicit cap, see flag) × data-quality (medium; four feed gaps promoted to assumptions with explicit haircuts). Feasibility: PASS, with confidence haircut applied to final sizing.
7. `m.collapse` — capital: open silver sleeve at recommended NAV %, bullion-heavy split, with sensitivity threshold pre-registered as the auto-resize trigger.

## Prediction (convergent)

### Expected return — distribution sketch

Scenario-weighted, conditional on graph snapshot. Drawing on `strategy.portfolio-architecture.scenario_set`:

**12-month return distribution — PSLV/SLV (bullion):**
- S1 (soft landing + AI capex extends, 0.22): −5% to +8%, mean +1%
- S2 (stagflation lite, 0.18): +35% to +85%, mean +55%
- S3 (recession + faster cuts, 0.14): −15% to +20%, mean +2% (silver caught between cyclical pain and rate-cut tailwind)
- S4 (AI capex peak <18mo, 0.20): −10% to +15%, mean +2%
- S5 (geopolitical, 0.10): +25% to +60%, mean +40%
- S6 (reflation surprise, 0.08): +40% to +95%, mean +60%
- S7 (status quo drift, 0.06): −5% to +15%, mean +5%
- S8 (tail / fat-left, 0.02): −20% to +30%, mean +5% (silver split between monetary bid and industrial dump)

Weighted mean E[R] (12mo, bullion) ≈ +18%
Weighted SD ≈ 27%
Approx quantiles (12mo, bullion): P10 ≈ −12%, P50 ≈ +12%, P90 ≈ +55%

**12-month return distribution — SIL (miners):**
Operational-leverage multiplier ~2.0–2.5x silver moves, asymmetric (downside compressed by cash-cost floor; upside levered).
- E[R] (12mo, miners) ≈ +35% (haircut for EDGAR-stub uncertainty: assumption 11 → −5pp), so adjusted ≈ +30%
- SD ≈ 50%
- Approx quantiles (12mo, miners): P10 ≈ −30%, P50 ≈ +20%, P90 ≈ +110%

**24-month return distribution — bullion:**
- Assumption-weighted compounding on the 12mo distribution + recognition-window assumption 6 (3–12mo) implies the bull scenarios largely realise in year 1 with consolidation in year 2.
- E[R] (24mo, bullion) ≈ +30%, SD ≈ 35%
- Quantiles: P10 ≈ −10%, P50 ≈ +25%, P90 ≈ +85%

**24-month return distribution — miners:**
- E[R] (24mo, miners) ≈ +60%, SD ≈ 75%
- Quantiles: P10 ≈ −35%, P50 ≈ +45%, P90 ≈ +175%

### Expected risk — drawdown distributions

**PSLV/SLV (bullion) — 12mo drawdown:**
- Max plausible drawdown under thesis-failure (PV thrifting + weak host metals + gold de-correlation): −25% (per parent screen + assumption 7).
- P(drawdown >10%) ≈ 0.40
- P(drawdown >20%) ≈ 0.20
- P(drawdown >25%) ≈ 0.08 (capped by all-in cash-cost floor of top-quartile primary mines ~$15/oz)
- Tail (drawdown >30%) ≈ 0.03 (would require simultaneous gold de-correlation + PV demand shock + dollar surge)

**SIL (miners) — 12mo drawdown:**
- Max plausible drawdown: −45% (per parent screen, slightly tighter than the −55% Centrus comparator in uranium because primary silver miners are less single-asset).
- P(drawdown >20%) ≈ 0.40
- P(drawdown >35%) ≈ 0.20
- P(drawdown >45%) ≈ 0.10 (capped by miner book value at depressed silver $18–20/oz)
- Tail (drawdown >55%) ≈ 0.04 (Mexican single-name jurisdictional shock or balance-sheet event on a SIL constituent)

### E[R] / E[risk] ratio

Define E[risk] = expected drawdown magnitude over 12mo (probability-weighted negative tail).

- **Bullion:** E[R] +18% / E[risk] ~6% = **3.0**
- **Miner:** E[R] +30% / E[risk] ~13% = **2.3**
- **Blended (70/30 bullion/miner):** E[R] ~+22% / E[risk] ~8% = **2.75**

For comparison, Type B archetype rough hurdle for sizing = 1.5; bullion comfortably clears, miner clears, blend clears.

### Sensitivity — brittle assumption + threshold

**Most brittle: Assumption 5 (gold-correlation regime stability).**

If gold tops in the next 6 months (technicals.gld breaks below its 200d by >5% with vol spike) AND silver loses its conditional gold-beta (rolling 60d correlation drops below 0.50), the bullion E[R] re-prices toward the industrial-only leg: ~+8% mean instead of +18%; E[R]/E[risk] drops below 1.5 — at that point the position should be resized down or closed.

**Threshold for auto-resize trigger (registered with this Collapse):**
- Gold 60d realised vol >35% AND GLD off >10% from peak → halve silver sleeve.
- Silver/gold 60d correlation <0.50 sustained 30d → close miner sleeve, hold bullion only.
- Silver Institute revises 2026 deficit to <80 Moz/yr → halve sleeve, reframe.
- Copper-plating commercial scale-up announcement (any tier-1 cell maker) → halve miner sleeve, hold bullion at half size.

**Second-tier sensitivity:** Assumption 2 (TOPCon/HJT mix + thrifting cap). A copper-plating breakthrough or accelerated thrifting beyond 40% on TOPCon would degrade the per-watt silver demand and remove the structural deficit story over 18–24 months. Slower-burning trigger, but watch quarterly cell-maker earnings calls.

### Sizing — NAV % + bullion/miner split rationale

**Recommended sleeve size: 4.0% NAV (range 3.0–5.0%, confidence 0.55).**

**Split: 70% bullion (PSLV preferred over SLV) / 30% miner (SIL).**
- Bullion: 2.8% NAV in PSLV (allocated, lower counterparty risk than SLV; modest premium acceptable for thesis horizon).
- Miner: 1.2% NAV in SIL (basket; avoids single-name jurisdictional/balance-sheet risk given EDGAR stub).

**Sizing derivation (Kelly with haircut, sanity-checked by drawdown bound):**
- Bullion fractional Kelly: edge ≈ 0.18 / vol² ≈ 0.073 → 2.5x; haircut to 1/4-Kelly per discipline → ~0.6 of NAV at face. Apply mandate-implicit Type B-cluster cap from `strategy.portfolio-architecture.proposed_adjustments.A6` (sizing discipline + concentration cap across Type B candidates) → 2.8% NAV.
- Miner fractional Kelly: edge ≈ 0.30 / vol² ≈ 0.25 → 1.2x; haircut to 1/4-Kelly → ~0.3; further haircut for EDGAR stub (assumption 11) and Mexican-jurisdiction risk → 1.2% NAV.
- Total 4.0% sits inside an inferred Type B per-thesis cap of ~5% (no formal mandate cap yet — H8 hole in architecture; flagged).

**Bullion-heavy rationale:**
- Assumption 5 (gold-correlation) is the most fragile. Bullion captures the monetary leg cleanly; miners add operational and jurisdictional risk on top of the same commodity exposure.
- EDGAR stub (assumption 11) means miner balance-sheet stress is qualitatively assessed only — confidence on miner drawdown floor is haircut.
- Bullion drawdown bound (−25%) is tighter and physically anchored (cash-cost floor); miner drawdown bound (−45%) widens the tail.
- Recognition trigger (gold/silver ratio compression) is captured equally well by either vehicle on the upside; bullion gives up some torque but reduces the path-dependency.

**Why not zero miner exposure:** If recognition fires sharply (ratio breaks below 65x), miner operational leverage delivers meaningfully more upside (+110% P90 vs +55% bullion P90). Holding 30% in SIL preserves the asymmetry while respecting the haircuts. SIL basket dilutes single-name balance-sheet/jurisdiction risk.

**Cluster check:** Sleeve adds to "supply-bottleneck industrial cluster" (REE + uranium + silver + grid + tankers). Per architecture A6 proposal, total cluster size should be capped (not yet formalised). Silver at 4% alongside REE + uranium recommended sizes (pending those child inquiries) should keep the cluster within an implied 15–20% NAV cap; flag for the architect to enforce on Collapse.

**Hedge note:** No explicit tail hedge in this sleeve. The bullion split serves as a partial hedge against the miner sleeve and against the broader portfolio's AI-capex-factor concentration (closes part of H1 / H6 in architecture). Aligns with the architecture's `tail-hedge availability` framing.

## Outcome

_Locked until 2027-05-09._

## Reflection

_Locked._
