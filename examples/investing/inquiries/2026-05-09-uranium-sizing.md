---
id: 2026-05-09-uranium-sizing
shape: convergent
collapse_flavour: capital
status: open
scope: "Sizing decision for uranium / HALEU sleeve under Type B archetype."
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

# Inquiry: Uranium / HALEU sizing

## Scope

Decide capital allocation to a uranium + HALEU sleeve. Vehicles: Sprott Physical (SRUUF / U.UN) for clean spot exposure, Centrus (LEU) for HALEU torque, Cameco (CCJ) for liquid major. Ranked #2 in 2026-05-08 Type B screen. Demand drivers: hyperscaler PPAs (>5GW by 2030), restart fleet, ~15 SMR projects, Western utility refill cycle vs Russia/Rosatom 25% enrichment + 40% HALEU exposure. Recognition window 9–18mo. Drawdown bound −30 to −55%.

In scope: vehicle mix within sleeve, sizing range, drawdown distribution, asymmetry, sensitivity, Collapse recommendation.
Out of scope: HALEU-only single-name concentration risk, fuel-cycle expert validation (deferred to feed-inquiry if needed).

## Assumptions (load-bearing)

Per amendment `2026-05-08-feed-gap-promotes-to-assumption`, feed gaps are promoted to named assumptions with explicit confidence haircuts. Per amendment `2026-05-08-factor-coverage-checklist`, factor coverage is enumerated explicitly in m.probe.edges.

**Demand-side assumptions.**

1. **Hyperscaler nuclear PPA execution rate.** Of >5 GW announced PPAs (Microsoft–Constellation, Amazon–Talen, Meta RFP) by 2030, ≥60% reach commercial operation date on or near schedule (i.e., ≥3 GW firm by end-2029). Falsifiable by: PPA cancellations / renegotiations exceeding 40% of announced GW within 18 months. Failure → recognition trigger weakened, spot uranium drifts lower, Centrus HALEU offtake demand soft. p(holds within 18mo) ≈ 0.65.

2. **SMR project realisation rate.** Of ~15 announced SMR projects in US/Canada/UK, ≥30% reach NRC certification + first concrete pour or fuel-order signature by end-2027 (i.e., ~4–5 projects materially derisked). Falsifiable by: NRC delays cumulative >24 months past current schedule on the lead candidates (NuScale, X-energy, Holtec, TerraPower). Failure → HALEU demand-pull pushed beyond 2029; LEU thesis is mostly broken; spot uranium thesis intact via restart fleet alone. p(holds) ≈ 0.45.

3. **Russia / Rosatom sanctions posture.** US Russian-uranium import ban (Prohibiting Russian Uranium Imports Act) waivers wind down on schedule through end-2027; no broad re-permitting; HALEU sole-source position of Rosatom (TENEX) remains a Western policy red line. EU follows directionally. Falsifiable by: bulk waiver extension to 2030+, OR direct policy reversal, OR major escalation forcing full immediate cutoff (also tail upside). Failure (downside) → spot uranium softens 15–25%; Centrus loses urgency premium. p(holds in middle band) ≈ 0.70; p(escalation = upside tail) ≈ 0.10; p(reversal = downside) ≈ 0.20.

4. **Western utility refill timing.** US/EU utilities currently at ~1.5–2 years of forward inventory contract their next refill cycle materially in 2026–2027 (term contracting volume up >25% YoY vs 2025 baseline). Falsifiable by: WNA / TradeTech / UxC term-contracting print showing flat-to-down volumes through 2026Q4. Failure → spot drifts in $50–60/lb range; recognition delayed. p ≈ 0.65.

5. **HALEU sole-source duration.** Centrus American Centrifuge Plant remains the only NRC-licensed US HALEU producer through 2027; Urenco USA HALEU expansion does not deliver commercial volumes inside window; DOE HALEU Availability Program continues funding contracts to Centrus. Falsifiable by: Urenco USA commercial HALEU delivery announcement, OR DOE program restructuring that splits awards 50/50, OR Russian re-import waiver covering HALEU specifically. Failure → LEU loses its monopoly premium; downside −55% becomes realised. p ≈ 0.70.

**Supply-side assumptions.**

6. **Kazatomprom production guidance.** Kazatomprom does not surprise *upward* in its 2026 production guide vs current consensus (~26ktU); sulphuric-acid bottleneck and drilling backlog persist. A surprise miss is base case (per parent screen). Falsifiable by: 2026Q2/Q3 production guide-up of >10%. Failure → spot uranium softens 10–20% on supply-shock relief. p (no upside surprise) ≈ 0.75.

7. **Cameco operational continuity.** Cigar Lake / McArthur River / Inkai run within current licensed-capacity guidance; no major operational disruption (water inflow, geopolitical Inkai event) inside window. Falsifiable by: production halt or downgrade >15% of guidance. Failure: bullish for spot but punishes CCJ specifically (idiosyncratic risk on the "liquid major" leg). p ≈ 0.85.

8. **Spot vehicle structural integrity.** Sprott Physical Uranium Trust (SRUUF / U.UN) maintains its at-the-market issuance discipline and physical-uranium hoarding mandate; no forced redemption / NAV-discount blowout. Falsifiable by: persistent NAV discount >15% over 60 days, OR mandate change. Failure → vehicle premium-to-NAV regime breaks; the "clean spot proxy" proposition weakens. p ≈ 0.90.

**Macro / regime / liquidity assumptions.**

9. **Macro regime is not a deep recession inside outcome window.** No GDP contraction >2% annualised across G7 inside 12 months. Falsifiable by: NBER-style recession call OR equivalent EU/UK print. Failure → demand-pull on uranium softens marginally (utilities are rate-base regulated, less cyclical than other industrials); equity vehicles (LEU, CCJ) compress 25–40% via multiple alone regardless of fundamentals. (Per parent screen assumption 7, recognised macro-conditional.) p ≈ 0.75.

10. **Liquidity adequate at sleeve size.** $50k–$5m positions can be entered/exited in SRUUF, U.UN (TSX), CCJ (NYSE), LEU (NYSE) without slippage >50bps over 5 trading days. SRUUF less liquid than U.UN; LEU is small/mid-cap and slippage-sensitive. Falsifiable by: bid/ask widening >100bps for >5 sessions. p ≈ 0.90.

11. **Drawdown bound is computed as max-plausible 12-month decline under thesis-failure path** (not historical max), and includes the joint probability of failure modes. Per parent screen assumption 10. Quantified per vehicle in Prediction.

**Promoted from feed gaps (per amendment).**

12. **No flows / positioning feed available.** Crowding probe on uranium equities (URNM, URA, NLR ETF flows; CCJ short interest; LEU short interest; SRUUF premium-to-NAV) is *first-principles only*. **Confidence haircut on reflexivity / crowding-driven sizing: −25%.** Resolves when flows feed registered (parent A3). Material because Type B recognition-window theses are explicitly reflexive (per portfolio-architecture §6).

13. **EDGAR feed stub-only.** Centrus DOE contract value/timeline, Cameco quarterly fuel-services backlog, Kazatomprom JV details — all qualitative + web_search rather than primary filings. **Confidence haircut on single-name fundamentals (esp. LEU and CCJ): −20%.** Resolves when EDGAR hydrates.

14. **FRED feed missing.** Real-rate / DXY / IP cycle on uranium equities indirectly approximated via TLT, UUP, DBC ETF proxies and news-summarizer FOMC distribution. **Confidence haircut on macro-conditional ranking inside the sleeve: −30%.** Resolves when FRED hydrates.

15. **No CBOE / options feed.** Forward-implied vol on CCJ, LEU, URNM unobserved. Cannot price call spreads or protective puts as alternative vehicle structure. **Confidence haircut on options-overlay alternatives: full (option overlays excluded from this inquiry).** Resolves when CBOE feed registered.

16. **Recognition-latency assumption (parent screen #9).** Median market participant takes 6–18 months to reprice once supply-bottleneck data crosses a clear threshold. For uranium specifically: assume 9–18 months (per parent ranking). Falsifiable by: faster repricing (e.g., a single Kazatomprom guide-down triggering >40% spot move within 3 months). Faster recognition is upside; failure mode is *slower* recognition extending beyond outcome window.

## Graph references

Pulled from snapshot 2026-05-08T09:00Z (sibling-inquiry hand-snapshots layered onto graph snapshot 2026-05-08T05:30Z; FRED gap, EDGAR stub, no flows feed, no broker feed).

**Strategy / parent context.**

- `graph/strategies.md#strategy.type-b.current_candidates[rank=2]` — uranium / HALEU candidate, vehicles `["SRUUF", "U.UN", "LEU", "CCJ"]`, recognition window 9–18mo, asymmetry ~5:2, drawdown bound −55% (worst leg), drawdown floor "Sprott Physical NAV ~ spot uranium; Centrus operationally levered". Provenance: `inquiry.2026-05-08-type-b-screen`.
- `graph/strategies.md#strategy.portfolio-architecture` — framings in use, scenario set S1–S8, hole H2 (AI-capex factor over-concentration), proposed adjustment A6 (tighten Type B sizing discipline; sequence + concentration cap). This inquiry is one of the three coordinated under A6 (alongside `2026-05-09-lynas-sizing`, `2026-05-09-silver-sizing`).

**Themes.**

- `graph/themes.md#themes.ai-capex-cycle` — peak-timing distribution {peak_within_18mo: 0.45, peak_18_to_36mo: 0.35, no_peak_36mo: 0.20}, confidence 0.55. Powers the demand-deduction chain via hyperscaler PPA leg. *Brittle upstream node per portfolio-architecture sensitivity §7.*
- `themes.capital_framework_overhaul`, `themes.payments_infrastructure_expansion` — not load-bearing here; noted.

**Politics / sanctions.**

- `graph/politics.md#politics.fomc_rate_path_may2026` — hold_through_june 0.55, cut_25 0.20, hold_then_cut_h2 0.15. Conditions equity multiple on LEU / CCJ (rate-cut path → growth-equity friendly).
- `graph/politics.md#politics.regulatory_deregulation_posture` — moderate_easing 0.50; secondary impact on nuclear permitting cadence (NRC).
- *Missing graph node:* `politics.russia-uranium-import-ban` — promoted to assumption 3 (load-bearing). Should be added to `politics.md` on next news-summarizer pass; flagged as graph-update candidate.
- *Missing graph node:* `politics.doe-haleu-availability-program` — promoted to assumption 5; same flag.

**Macro (proxy only — FRED gap).**

- `graph/macro.md#macro.cfx_uup` — DXY proxy 27.41, low realised vol 5.9%; weak-USD tailwind absent.
- `graph/macro.md#macro.cfx_tlt` — duration proxy 85.65, vol 8.55%; rate-cut path expressed here.
- `graph/macro.md#macro.cfx_dbc` — broad commodity proxy 30.25, vol 23.1%; supports commodities-friendly tape.
- `graph/macro.md#macro.cfx_eurusd_x` — 1.174; EUR firmer; supports U.UN (TSX/CAD) indirectly via USD softness.

**Technicals.**

- `graph/technicals.md#technicals.gld` — 431.68, vol 28.0% (informs gold/uranium real-asset cluster correlation).
- `graph/technicals.md#technicals.xle` — 55.95, vol 27.3%; energy correlation reference.
- `graph/technicals.md#technicals.dbc` — 30.25, vol 23.1%; broad commodity tape.
- *Missing direct node:* uranium spot, CCJ, LEU, SRUUF, U.UN, URNM, URA technicals not in current graph (yfinance feed pulls SPY-cluster + sector ETFs + mega-caps + crypto + macro proxies). Single-name uranium technicals are web_search / external; flagged as feed-extension candidate.

**Sentiment.**

- `graph/sentiment.md#sentiment.fed_policy_stance` — mean 0.05 (neutral-slight-hawkish), sd 0.25, fuzz_halo HIGH. Treat as low-information.
- *No uranium-specific sentiment node.* Web_search + Type B screen prose is the only signal; flag.

**Flows.**

- `graph/flows.md` — *empty.* Per assumption 12, this is a structural blind spot; the parent portfolio-architecture A3 proposes registering a flows feed. **Cannot probe crowding on URNM / URA / CCJ / LEU.**

**Fundamentals.**

- `graph/fundamentals.md` — *EDGAR stub.* Per assumption 13, single-name fundamentals not directly readable. CCJ Q4 2025 fuel-services backlog, LEU DOE contract values, Kazatomprom 2025 production print — all from web_search prose, not graph.

**Edges.**

- `graph/edges.md#edge.crowding-to-drawdown` — illustrative; reflexive edge with strength mean 0.25, conditions "positioning percentile > 70" + "vol mid-elevated or higher". Walked but **not directly applicable** to single-name uranium miners (per portfolio-architecture §6 caveat). Used by inversion: Type B recognition-window theses benefit from positioning building pre-recognition, suffer post-recognition; we cannot locate ourselves on the curve without flows feed.
- *Implied edge (not in graph):* `edge.haleu-supply-to-leu-equity` — HALEU sole-source duration → LEU realised price/EBITDA; latency 6–12 months on contract awards; would be belief-Collapse candidate.
- *Implied edge:* `edge.spot-u3o8-to-sruuf-nav` — direct, near-zero latency, strength near 1.0 minus premium/discount drift. Implicit in vehicle choice.

**Portfolio.**

- `graph/portfolio.md#portfolio.current` — schema only; broker feed not wired (assumption: no current uranium exposure in book). Sleeve sizing therefore additive, not adjustment.

## Intent

Output sizing recommendation in NAV %, E[R]/E[risk], brittle assumption, vehicle mix.

## Self

- `self.capability` — Convergent capital-sizing inquiry. Can build per-vehicle return distributions from parent screen asymmetry bounds + sober adjustments; can compute drawdown distributions and E[R]/E[risk]; can apply the Type B mandate caps proposed in portfolio-architecture A6/A7. *Cannot* run a live HALEU fuel-cycle DCF (EDGAR stub), cannot price option overlays (no CBOE feed), cannot probe crowding (no flows feed). All three gaps are encoded as confidence haircuts (assumptions 12, 13, 15).

- `self.calibration` — No prior closed uranium / Type B inquiries on this instance. Industry prior on Type B disciplined-screen hit rate ~0.30–0.40; payoff multiple on hits ~3–8x (per parent screen self.calibration). Treat point estimates as priors; report distributions, not point sizing recommendations. Use ±1 quantile band on every return / risk number.

- `self.taste` — Bias toward (a) physical / spot proxy (SRUUF, U.UN) over operational equities for the *core* of a Type B real-asset thesis, because mining and enrichment equities carry idiosyncratic operational risk uncorrelated with the demand thesis; (b) treating recognition-window theses as "core spot + small torque" rather than concentrating in the highest-multiplier name; (c) drawing the drawdown bound from physical / NAV floors rather than equity-cycle floors where available. Counter-bias: I tend to *under*-weight the operational-leverage upside on names like LEU when the thesis is right — sober-case modelling should not collapse the upper tail.

- **Bias probes for this run.**
  - *Narrative seduction* — would I size this if the AI / hyperscaler PPA story were boring? Probed: Western utility refill cycle (assumption 4) and HALEU sole-source (assumption 5) are independent legs that pre-date and survive without the AI narrative. Sleeve survives the boring-story test, but at the *lower* end of the size band (because two legs not three).
  - *Recency bias* — uranium had a strong 2023–2024 then compressed 2025–2026. Am I anchoring on the prior peak as the upside target? Probed: upside in Prediction is built bottom-up from term-contracting price + utility refill volumes, not from "return to prior peak". Compressed enough.
  - *Tail neglect* — am I Gaussian-shaping a fat-tailed outcome? Probed: drawdown distribution is explicitly bimodal (NAV floor scenario vs operational-leverage blow-out for LEU), not single-mode.
  - *Crowding blindness* — without flows feed, am I assuming positioning is light because price is compressed? Probed: confidence haircut −25% applied; sleeve sized at the *lower* end of mandate cap to absorb a forced-unwind shock that we cannot detect.
  - *Implicit factor bet* — sleeve adds to the "supply-bottleneck industrial" cluster (REE + uranium + silver + grid). Probed: cluster cap (per portfolio-architecture A6) bounds total Type B at 6–10% NAV; this inquiry sized within that envelope.

## M-nodes (sequence)

1. **`m.probe.scope`** — sharpened from "size uranium" to "size a uranium / HALEU sleeve, split between spot proxy (SRUUF / U.UN) as core and operational torque (LEU and/or CCJ), within the Type B cluster cap of 6–10% NAV proposed by portfolio-architecture A6". Outcome window 12 months (sizing decision judged at 12mo) with secondary 24mo distribution because thesis recognition window is 9–18mo.

2. **`m.probe.prior-art`** — consulted:
   - `methods.md` — Kelly (haircut for fat-tail distribution), drawdown bound (hard stop), scenario stress (per portfolio-architecture S1–S8), factor exposure (implicit AI-capex + supply-bottleneck industrial).
   - `blind-spots.md` — narrative seduction, recency, tail neglect, implicit factor bets, crowding risk (flagged structurally per assumption 12).
   - `strategies.md` — Type B criteria (deductive demand, supply bottleneck, narrow window, asymmetric payoff, drawdown-bounded sizing).
   - parent `2026-05-08-type-b-screen.md` rank-2 entry — asymmetry 5:2, drawdown −30 to −55%, vehicle preferences.
   - sibling `2026-05-08-portfolio-architecture.md` — scenario distribution S1–S8, hole H2 (AI-capex over-concentration), A6 (Type B sizing discipline).

3. **`m.probe.world`** — graph snapshot read; gaps confirmed (FRED, EDGAR, flows, CBOE, broker, single-name uranium technicals). Web_search supplements for: Kazatomprom 2025 production print, Cameco Q4 2025 fuel-services contracts, Centrus DOE HALEU contract status, term-contracting volumes (UxC / TradeTech), spot U3O8 level, hyperscaler PPA progress.

4. **`m.probe.edges` — factor-coverage walk** (per amendment `2026-05-08-factor-coverage-checklist`). Each factor enumerated explicitly:

   - **macro (rates, growth, inflation, fiscal).** Per FOMC distribution `politics.fomc_rate_path_may2026`, dovish bias on cuts paths totals 0.40 — supports growth-equity multiple on LEU / CCJ marginally. Real-rate path approximated by `macro.cfx_tlt`. **FRED gap → −30% confidence haircut on macro-conditional sizing (assumption 14).** *Probed (low-resolution).*

   - **geographic (jurisdiction, sanctions, trade).** Russia / Rosatom 25% global enrichment + 40% HALEU technical capability — promoted to assumption 3. Kazakhstan (Kazatomprom) jurisdiction risk — covered by assumption 6. US permitting (NRC) — assumption 2. Canadian Cameco — operationally domestic to NA. *Probed (load-bearing on assumption 3, 5).*

   - **regime (vol, liquidity, dispersion).** Vol regime mid-elevated (per portfolio-architecture assumption 9). Single-name uranium equities likely 35–55% realised vol (CCJ probably lower mid-30s; LEU likely 60%+ given small/mid-cap operational leverage). SRUUF tracks spot — vol ≈ spot uranium vol (estimated 25–35%). *Probed.*

   - **correlation structure.** Spot uranium ↔ SRUUF/U.UN: near-1 ex-NAV-premium drift. SRUUF ↔ CCJ: high in regime moves, decoupled in idiosyncratic operational events. SRUUF ↔ LEU: moderate; LEU has its own HALEU-contract leg. Uranium-cluster ↔ broader Type B real-asset cluster (REE, silver): positive in S2/S5/S6, negative-to-flat in S3/S4. ↔ AI-capex factor: positive on demand leg (bullish if S1, S6) but susceptible if AI capex peaks (S4, 0.20). *Probed (qualitative; no real correlation matrix).*

   - **flows / crowding.** **N/A with reason: no flows feed (assumption 12).** Surfaced as material risk: Type B recognition-window theses are explicitly reflexive; we cannot tell where on the positioning curve we are. **Mitigation:** size at lower end of mandate envelope to absorb a forced-unwind shock; weighted toward physical (SRUUF / U.UN) which has structural NAV-floor support vs equities.

   - **themes.** `themes.ai-capex-cycle` peak-timing distribution conditions hyperscaler PPA leg (assumption 1). Sensitivity to this node is the dominant non-sleeve-internal risk (per portfolio-architecture §7). *Probed.*

   - **reflexivity.** Pre-recognition: positioning building → spot up → utility FOMO contract → spot up further (positive reflexivity, what we want). Post-recognition: positioning blowoff → spot reverts → equity multiples derate → forced unwind on small/mid-cap miners (negative reflexivity, what kills LEU specifically). With no flows feed, we cannot detect transition. **Mitigation:** sleeve weighted to spot (NAV-floored) over equity (multiple-floored). *Probed.*

   - **liquidity / capacity.** SRUUF ADV ~$8–15m, U.UN (TSX) ADV ~CAD 15–30m → can absorb $50k–$5m. CCJ NYSE ADV $200m+ → fully liquid. LEU NYSE ADV ~$50–100m, beta-3-ish, slippage in stress could widen — sized smaller. URNM/URA basket alternative: ADVs $10–30m, broader liquidity at cost of HALEU torque dilution. *Probed.*

5. **`m.reframe`** — Reframed once: original framing was "size uranium as a single allocation"; reframed to "core spot + small HALEU torque" two-leg structure. The reframe is forced by the bimodal drawdown distribution (parent screen drawdown −30% on SRUUF vs −55% on LEU) — a single-name allocation cannot respect both bounds simultaneously. Reframe stable.

6. **`m.test.feasibility`**:
   - *capability* ✓ — sleeve constructable in available accounts; SRUUF for US, U.UN equivalent for CAD; CCJ + LEU on NYSE.
   - *constraint* ✓ — within proposed 6–10% Type B cluster cap; respects per-name 8% cap proposed in portfolio-architecture A7.
   - *budget* ✓ — sleeve target 3–5% NAV (see Prediction).
   - *data quality* — flagged via assumptions 12, 13, 14, 15 with explicit confidence haircuts.
   - *mandate* — no leverage, no shorting, no derivatives — consistent with current loose mandate; no option overlay attempted.

7. **`m.collapse`** — capital-Collapse pending user gate. Sizing recommendation in Prediction. **Collapse is contingent on user posterior on (a) AI-capex peak timing and (b) acceptance of A6 cluster cap.** If user has not collapsed on A6, this inquiry's sizing is provisional pending the cluster envelope.

## Prediction (convergent)

All distributions reported as quantile sketches with explicit failure-path joint probabilities. Confidence haircuts (assumptions 12 −25%, 13 −20%, 14 −30%, 15 full on options) applied multiplicatively to thesis-conviction; sleeve sizing is *post-haircut*.

### Vehicle-level return distributions (12 months)

Per parent screen rank-2 entry, scaled to 12mo (parent quoted 12–24mo bands). Quantiles are subjective, derived from parent's ranges with sober adjustment.

| Vehicle | P10 | P25 | P50 | P75 | P90 | E[R] (12mo) | Tail-loss (P5) |
|---------|-----|-----|-----|-----|-----|-------------|----------------|
| SRUUF / U.UN (spot) | −28% | −10% | +18% | +55% | +110% | **+22%** | −32% |
| CCJ (liquid major) | −30% | −12% | +15% | +50% | +100% | **+18%** | −38% |
| LEU (HALEU torque) | −55% | −25% | +25% | +110% | +250% | **+38%** | −62% |

Notes:
- SRUUF P50 +18%: spot U3O8 from ~$70/lb base toward $85–90/lb on assumption-4 utility refill; bounded above by Sprott NAV-mechanic and term-vs-spot convergence.
- LEU P50 +25%: a positive but un-explosive realisation; the right tail (P75/P90) reflects the binary nature of HALEU contract awards and operational leverage to enrichment-fee uplift; left tail (P10) reflects sole-source-duration failure (assumption 5) compounded with macro (assumption 9).
- CCJ between the two: operational diversification (Cigar Lake + Inkai + fuel services + Westinghouse JV), but Inkai Kazakhstan operational risk (assumption 7) and equity-cycle exposure cap upside vs LEU.

### Vehicle-level return distributions (24 months)

| Vehicle | P10 | P25 | P50 | P75 | P90 | E[R] (24mo) |
|---------|-----|-----|-----|-----|-----|-------------|
| SRUUF / U.UN | −20% | +5%  | +45%  | +90%  | +160% | **+45%** |
| CCJ | −25% | 0%   | +35%  | +75%  | +130% | **+35%** |
| LEU | −60% | −15% | +60%  | +180% | +400% | **+75%** |

Notes:
- 24mo P50 reflects the recognition-window centre case: utility refill cycle visible in term-contracting print, first commercial HALEU contract awarded, SMR project crosses NRC milestone.
- LEU 24mo P10 stays −60%: if assumption 5 fails (Urenco USA delivers, Russia waiver re-permitting), the LEU multiple compresses sharply and stays compressed — the failure path is path-dependent, not mean-reverting inside window.

### Vehicle-level drawdown distributions (peak-to-trough inside 12 months)

| Vehicle | Median DD | P75 DD (worst quartile) | P95 DD (tail) | Hard floor (NAV / cycle) |
|---------|-----------|--------------------------|----------------|---------------------------|
| SRUUF / U.UN | −15% | −25% | −35% | NAV ≈ spot uranium; spot floor ~$45–50/lb top quartile cash-cost → ~−40% from current |
| CCJ | −18% | −30% | −45% | ~10x trough EBITDA on Cameco book → ~−45% |
| LEU | −28% | −45% | −62% | Operational option value + DOE backstop → ~−65% |

### Sleeve construction — recommended mix

**Sleeve target: 4% of NAV** (within 3–5% recommended band; centred at 4% post-haircuts).

| Vehicle | NAV % | Within-sleeve % | Rationale |
|---------|-------|------------------|-----------|
| SRUUF / U.UN | 2.4% | 60% | Core. NAV-floored spot proxy. Survives assumption 5 failure. Survives recognition-latency drift. |
| CCJ | 1.0% | 25% | Liquidity + operational diversification ballast. Lower drawdown than LEU; participates in spot move via fuel-services and Westinghouse exposure. |
| LEU | 0.6% | 15% | HALEU-specific torque. Sized to absorb its own −62% tail (LEU drawdown × 0.6% NAV ≤ 0.4% NAV book impact). |

Sleeve-level expected return (12mo, weighted): **+22.5%**.
Sleeve-level expected drawdown (median, partial-correlation adjusted): **−18%**.
Sleeve-level tail loss (P5, joint failure-path adjusted, all three vehicles down): **−40%** at sleeve = −1.6% NAV book impact.

### E[R] / E[risk] ratio (sleeve-level)

Two formulations (per `methods.md` — neither prescribed; both surfaced):

- **E[R] / median drawdown:** +22.5% / 18% = **1.25** (12mo).
- **E[R] / P5 tail-loss:** +22.5% / 40% = **0.56** (12mo, tail-conditional, conservative).

24mo equivalents:
- E[R] / median drawdown ≈ +47% / 22% = **2.13**.
- E[R] / P5 tail-loss ≈ +47% / 50% = **0.94**.

For comparison, parent screen quoted asymmetry ~5:2 = 2.5 (qualitative). Our 24mo E[R]/median-DD ≈ 2.13 lands close to that, post-haircut. The 12mo number is materially worse because recognition window is 9–18mo — the thesis is *under-incubated* at 12mo measurement.

**Optimization-target verdict:** sleeve E[R]/E[risk] is favourable on the 24mo measurement (≥2.0 on median-DD denominator) and **borderline** on the 12mo measurement (1.25). User should be aware the optimization target wants the 24mo lens, not the 12mo lens. Outcome window 12mo is a *check-in*, not the verdict horizon.

### Sensitivity — brittle assumption + threshold

Single-perturbation sweep across assumptions 1–11 and theme `ai-capex-cycle`. Surfacing the dominant brittle link.

**Brittle assumption: #5 — HALEU sole-source duration (Centrus monopoly through 2027).**

This is brittle because:
- It is the *only* assumption that maps directly to the highest-multiplier name (LEU) without macro/correlation buffering.
- Failure modes are observable in advance with a short latency (Urenco USA HALEU commercial-delivery announcement, DOE program restructuring, Russian HALEU re-import waiver), so the assumption can be monitored continuously.
- Failure path is path-dependent and not mean-reverting — once monopoly premium dissipates, LEU re-rates lower and stays lower.

**Threshold to flip:**
- *Trigger:* announcement of any of (i) Urenco USA commercial HALEU delivery within 18 months, (ii) DOE HALEU Availability Program awarding ≥40% to a non-Centrus producer, (iii) Russian HALEU import waiver covering >50% of pre-2024 import volume.
- *Action on flip:* exit LEU leg fully (estimated immediate −20–35% mark on the leg itself); rebalance into SRUUF (raise SRUUF from 2.4% → 3.0% NAV) and CCJ (raise from 1.0% → 1.5%).
- *Sleeve impact under flip:* book impact on flip ≈ −0.15% NAV; sleeve E[R] (12mo) recompresses to ~+18% (closer to spot-only profile).

**Secondary brittle assumption: #1 — hyperscaler PPA execution rate (≥60% of >5GW reach COD).**

If PPA execution rate falls below 50% inside 18 months (i.e., cancellations/renegotiations exceed 40% of announced GW), the demand-pull leg of the thesis weakens. Combined with assumption-9 macro recession, sleeve E[R] (12mo) drops from +22.5% to +5–8%. **Threshold to flip:** PPA cancellation print >40% of announced GW.

**Tertiary: theme `ai-capex-cycle` peak-timing.** Already surfaced in portfolio-architecture §7 as the broadest-leverage upstream node. A ~10–12pp shift toward "early peak" (S4 mass rises) reduces sleeve E[R] (12mo) by ~5–8pp; sleeve still positive but ratio compresses.

**Robust to:** assumption 6 (Kazatomprom upside surprise — flips spot direction by 10–20% but does not invalidate sleeve; partially compensated by HALEU leg if assumption 5 holds), assumption 7 (Cameco operational continuity — affects CCJ idiosyncratically, not sleeve-level), assumption 10 (liquidity — bounded by sizing), assumption 8 (SRUUF NAV-discount — adds ~5% downside to spot leg but bounded). 

### Sizing recommendation

**Recommend sleeve at 4% NAV, mix 60/25/15 SRUUF/CCJ/LEU.** Acceptable band 3–5% NAV depending on user's posterior on AI-capex peak-timing and acceptance of A6 cluster cap.

If user's posterior on AI-capex peak inside 18 months is **>0.55** (ie heavier than current 0.45), recommend lower bound: **3% NAV, mix 70/20/10** (SRUUF heavier, LEU lighter).

If user's posterior on early peak is **<0.30** (ie thesis runway longer than current themes-graph distribution), recommend upper bound: **5% NAV, mix 55/25/20** (more LEU torque tolerable).

Either way, **maintain SRUUF/U.UN as ≥55% of sleeve** — the spot proxy is the thesis-survival vehicle and respects the −30% drawdown bound that the parent screen quoted; the equity legs respect their own larger drawdown bounds within their own size.

**Vehicle preference rationale (explicit per parent screen).**
- *Core spot (SRUUF / U.UN, 60% of sleeve).* Reason: the demand-deduction chain rests on spot uranium price re-rating; SRUUF tracks that directly with NAV-floor protection. This is the thesis-survival vehicle. U.UN preferred over SRUUF for liquidity if accessible.
- *Liquid major ballast (CCJ, 25% of sleeve).* Reason: operational diversification (Cigar Lake + Inkai + fuel services + Westinghouse), better liquidity than SRUUF, drawdown bound −25% per parent screen. Adds equity-cycle participation without LEU's binary HALEU dependency.
- *Small HALEU torque (LEU, 15% of sleeve).* Reason: parent screen quotes 3–6x upside on Centrus under thesis. Sized so the −55–62% tail equals ≤0.4% NAV book impact — drawdown-bounded per parent assumption 10 and Type B "drawdown-bounded sizing" criterion.

### Coordination flag

Per portfolio-architecture A6, this sleeve must be *coordinated* with `2026-05-09-lynas-sizing` (rare earths) and `2026-05-09-silver-sizing` (silver). Combined Type B cluster sleeve **must not exceed 6–10% NAV**. This inquiry asks for 4% NAV; that leaves 2–6% for the other two children. Recommend the user collapse on the cluster-cap belief-Collapse (A6, child `2026-05-15-type-b-cluster-sizing`) **before** capital-collapsing this inquiry, so the cluster envelope is firm at the moment of collapse.

## Outcome

_Locked until 2027-05-09._

## Reflection

_Locked._
