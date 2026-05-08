---
id: 2026-05-15-phosphate-sizing
shape: convergent
collapse_flavour: capital
status: open
scope: "Sizing decision for phosphate fertilizer sleeve under Type B archetype."
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

# Inquiry: Phosphate fertilizer sizing

## Scope

Decide capital allocation to phosphate fertilizer sleeve. Vehicles: MOS (US-listed liquid), ICL (potash + phosphate hybrid, lower beta), NTR (potash-heavy reference). Ranked #1 in v2 Type B screen. Demand drivers: non-substitutable macronutrient, food-security demand floor surviving recession. Supply bottleneck: Morocco-OCP + China export-quota regime. Recognition window 12-24mo. Drawdown bound −35%.

In scope: vehicle mix, sizing, drawdown, asymmetry, sensitivity.
Out of scope: full ag-cycle macro overlay, urea/potash standalone (referenced as adjacent only).

## Assumptions (load-bearing)

Per amendment `2026-05-08-feed-gap-promotes-to-assumption`, feed gaps are promoted to named assumptions with explicit confidence haircuts. Per amendment `2026-05-08-factor-coverage-checklist`, factor coverage is enumerated explicitly in m.probe.edges.

**Demand-side assumptions.**

1. **Food-security demand floor (calorie-driven, biological).** Global phosphate consumption tracks calorie demand at ~1.5–2% YoY structurally; phosphorus is one of three macronutrients with no substitute; soil-P drawdown without re-application reduces yields within 1–3 crop cycles. Indian fertilizer subsidy (~1.5% of central budget) and Brazilian/SEA seaborne import volumes (~35% of seaborne trade combined) are politically protected. Falsifiable by: a structural per-capita demand drop >5% YoY across India + Brazil + SEA inside outcome window (no precedent ex-1980s structural-adjustment shocks). Failure → demand floor narrative weakens; not invalidated. p(holds within 24mo) ≈ 0.85.

2. **China phosphate export-quota persistence.** China DAP/MAP export quota regime, in place since 2023–2024, persists through 2026–2028 (Q1 2026 export print already −20% YoY). Falsifiable by: explicit MOFCOM rescission of quota OR sustained quarterly export volume restoration to >90% of 2022 baseline. Failure (downside) → seaborne supply rebalances faster, DAP price compresses 10–15% from current ~$580. Failure (upside, less likely): quota broadens to urea + fluorspar (per parent v2 assumption 1, p≈0.45 within 18mo) — bullish reflexive catalyst. p(quota holds in current band) ≈ 0.65; p(broadens) ≈ 0.20; p(rolled back) ≈ 0.15.

3. **Morocco / OCP supply discipline.** OCP (~70% global reserves, state-owned, sole rational marginal swing producer) does not flood the seaborne market; targets price-realisation over volume; capex pace continues at announced ~6 Mtpa over 2025–2028 build-out (incremental, not disruptive). Falsifiable by: an OCP volume guide-up >15% inside 12 months OR a disclosed Saudi Ma'aden + OCP price-war episode. Failure → DAP price floor breaks toward $480–520; thesis still partially intact via depleted-reserve framing on Florida and China. p ≈ 0.75.

4. **Ag-cycle / corn–soybean linkage.** Farmer affordability is set by corn × yield − input cost. CBOT corn holds within $4.20–5.80/bu band through 2026–2027 (current ~$4.90); soybean holds $9.50–12.50/bu (current ~$10.50); USDA stocks-to-use ratios stay below long-term average, supporting application demand. Falsifiable by: a sustained corn print <$3.80 for >2 quarters (kills application affordability) OR >$6.50 for >2 quarters (compresses fertilizer margin via input-cost spike). Failure (downside) → North American application volume compresses 8–12% (2014–2016 analogue); MOS most exposed. p(within band) ≈ 0.65.

5. **US natural-gas-input cost path (ammonia–phosphate cost stack).** US Henry Hub stays in $2.80–4.50 band through 2026–2027 (current ~$3.20–3.50). Ammonia is direct nat-gas input; ammonium-phosphate (DAP/MAP) requires ammonia. If gas spikes, US producer margin compresses; if gas collapses, US producer cost-curve advantage widens vs Saudi/Moroccan but DAP price-floor weakens via lower cost-of-marginal-supply. Falsifiable by: HH sustained <$2.50 (parent v2 assumption 6 LNG-export ramp risk) OR >$5.50 (winter-shock or LNG-export overshoot). Failure → MOS US-asset margin shifts ±15% from current; ICL less exposed (Israeli gas + Dead-Sea cost-curve insulation). p(within band) ≈ 0.65.

6. **Recession demand-floor robustness (Type B's recession-survival claim).** In a global recession scenario (S3 in portfolio-architecture, p≈0.14), phosphate application volume compresses ≤8% peak-to-trough vs typical industrial-commodity 20–35% compression. Demand floor is real because (a) farmers cannot skip P-application for >1 cycle without yield loss, (b) Indian + Brazilian + SEA fiscal subsidies hold, (c) destocking on the agricultural side is bounded by the biological cycle. Falsifiable by: a 2026–2027 recession in which DAP demand prints down >12% YoY for 2 consecutive quarters. Failure → recession-survival claim broken; phosphate behaves like cyclical commodity; sleeve drawdown bound widens from −35% toward −50%. p(holds in S3) ≈ 0.70; *this is the central Type B differentiator for this candidate.*

**Supply-side / structural assumptions.**

7. **Saudi Ma'aden marginal cost is the implicit price floor.** Ma'aden + OCP set an implicit DAP price floor at ~$520–550/t via cost-curve discipline. Falsifiable by: Ma'aden expansion announcement that floods market OR Chinese low-grade rock re-entering at <$450 cif. p ≈ 0.75.

8. **Mosaic / ICL operational continuity.** No major operational disruption inside outcome window (Florida wetlands litigation, Saskatchewan potash flooding, Israeli geopolitical disruption to Rotem/Sdom operations). MOS Florida permits already secured for 2026–2028 mining. ICL Israeli operations resilient (operating through 2023–2025 conflict). Falsifiable by: production halt or downgrade >15% of guidance on either name. p ≈ 0.85.

9. **Recognition latency.** Median market participant takes 6–18 months to reprice phosphate equities once supply-bottleneck data crosses a clear threshold. Recognition triggers per parent screen: India tender clears at >$650 DAP, OR China announces extended quota. For phosphate specifically: recognition is *slower* than uranium/REE because the demand chain is undramatic (food, not AI/defense) — story-narrative deficit cuts both ways (less crowding risk, slower repricing). p (recognition inside 12–24mo) ≈ 0.60.

10. **Drawdown bound is computed as max-plausible 12-month decline under thesis-failure path** (joint: recession + China relaxes quota + Saudi ramp). Per parent screen, MOS −35%, ICL −40%; here we sober to MOS −38% / ICL −42% / NTR −30% reflecting NTR's potash-heavy mix as a partial diversifier.

**Promoted from feed gaps (per amendment).**

11. **No flows / positioning feed available.** Crowding probe on phosphate equities (MOS short interest, ICL ADR flows, agribusiness ETF positioning, MOO/COW ETF flows) is *first-principles only*. **Confidence haircut on reflexivity / crowding-driven sizing: −20%.** Lower haircut than uranium/REE sleeves because phosphate has *lower* narrative crowding (no AI-narrative coupling); first-principles likely closer to truth. Resolves when flows feed registered (parent A3).

12. **EDGAR feed stub-only.** MOS Q4 2025 phosphate-segment realised pricing, NTR potash + phosphate breakout, ICL bromine-segment optionality value — all qualitative + web_search rather than primary filings. **Confidence haircut on single-name fundamentals: −20%.** Resolves when EDGAR hydrates.

13. **FRED feed missing.** Macro regime conditioning (real rates → ag-credit availability; DXY → EM-buyer affordability; CPI components → fertilizer subsidy fiscal pressure) approximated via TLT/UUP/DBC ETF proxies and news-summarizer FOMC distribution. **Confidence haircut on macro-conditional ranking: −20%** (lower than uranium sleeve because phosphate is less rate-sensitive — utility-style demand floor vs growth-equity multiple). Resolves when FRED hydrates.

14. **No CBOE / options feed.** Forward-implied vol on MOS, NTR, ICL unobserved. Cannot price call spreads or protective puts. **Confidence haircut on options-overlay alternatives: full (excluded from this inquiry).** Resolves when CBOE feed registered.

15. **No commodities futures-curve feed.** DAP / MAP / phosphate-rock / ammonia term structure inferred not measured. **Confidence haircut on price-target precision: −15%.** Web_search compensates with spot prints; curve shape (contango/backwardation) is the recognition tell and we are blind to it. Resolves when commodities-curve feed registered.

16. **No EM-debt / FX-stress feed.** India-rupee, Brazilian real, Egyptian pound under stress would compress affordability and subsidy fiscal capacity. Web_search-derived only. **Confidence haircut on EM-buyer demand assumption (1): −10%.**

## Graph references

Pulled from snapshot 2026-05-08T09:00Z (sibling-inquiry hand-snapshots layered onto graph snapshot 2026-05-08T05:30Z; FRED gap, EDGAR stub, no flows feed, no commodities-curve feed, no broker feed).

**Strategy / parent context.**

- `graph/strategies.md#strategy.type-b.current_candidates_v2[rank=1]` — phosphate fertilizer candidate, vehicles `["MOS", "ICL", "NTR"]`, geography "Morocco/US/Israel", recognition window 12–24mo, asymmetry ~3:1, drawdown bound −35%, drawdown floor "replacement-cost-of-asset on Florida + Saskatchewan; ICL potash+bromine floor", `demand_floor_recession: true`. Provenance: `inquiry.2026-05-08-type-b-screen-v2`.
- `graph/strategies.md#strategy.portfolio-architecture` — scenario set S1–S8, hole H2 (AI-capex factor over-concentration), proposed adjustment A6 (tighten Type B sizing discipline; cluster cap 6–10% NAV). Phosphate is a *diversifier within the Type B cluster* because its demand chain is independent of AI-capex (food vs power). This is the strongest argument for phosphate consuming Type B cluster headroom over an additional uranium/REE/silver add-on.

**Themes.**

- `graph/themes.md#themes.ai-capex-cycle` — *not load-bearing on demand chain* (food-security demand is independent). Indirectly relevant: if AI-capex peaks (S4, p=0.20), the supply-bottleneck industrial cluster that includes phosphate could derate via factor-rotation contagion even though fundamentals don't change. *Probed; flagged as reflexive risk not fundamental risk.*
- *Implied theme node (not in graph):* `themes.food-security-bifurcation` — would capture protein-transition, climate-driven yield variance, fertilizer-as-strategic-stockpile narrative. Belief-Collapse candidate; not load-bearing for sizing today but useful for outcome-window calibration.

**Politics / sanctions.**

- `graph/politics.md#politics.us-china-tariff-regime-2026` — status_quo 0.50, escalation 0.35, partial_rollback 0.15. Phosphate is a *China retaliation lever* (per parent v2 assumption 1): if escalation, China extends quota / adds urea / adds fluorspar — direct upside catalyst. Conditions assumption 2.
- `graph/politics.md#politics.fomc_rate_path_may2026` — hold_through_june 0.55, cut_25 0.20, hold_then_cut_h2 0.15. Lower load-bearing here than for uranium (phosphate is less rate-sensitive); affects MOS multiple at the margin (~5–8% multiple sensitivity per 50bp).
- *Missing graph node:* `politics.india-fertilizer-subsidy-regime` — promoted to assumption 1 (load-bearing). Should be added to `politics.md` on next news-summarizer pass.
- *Missing graph node:* `politics.morocco-ocp-ipo-timeline` — promoted to assumption 3; explicit catalyst risk (positive) in 2026–2027.
- *Missing graph node:* `politics.china-phosphate-export-quota` — promoted to assumption 2; central catalyst.

**Macro (proxy only — FRED gap).**

- `graph/macro.md#macro.cfx_dbc` — broad commodity proxy 30.25, vol 23.1%; supports commodities-friendly tape, includes ag.
- `graph/macro.md#macro.cfx_uup` — DXY proxy 27.41, low realised vol 5.9%; weak-USD tailwind absent. EM-buyer affordability bounded — supports caution on EM-demand pace.
- `graph/macro.md#macro.cfx_uso` — 134.97, vol 73.1% (data-quality flagged in v1 screen, not used as signal).
- `graph/macro.md#macro.cfx_eurusd_x` — 1.174; ICL.TA quoted in ILS; EUR firmer = USD softer indirectly supports ICL on USD-investor returns.
- *Missing graph node:* `macro.us-henry-hub` — promoted to assumption 5 (ammonia-phosphate cost stack); ETF proxy unavailable.
- *Missing graph node:* `macro.cbot-corn` and `macro.cbot-soybean` — promoted to assumption 4. Web_search only.
- *Missing graph node:* `macro.dap-price` — promoted as the central observable; web_search only.

**Technicals.**

- `graph/technicals.md#technicals.dbc` — 30.25, vol 23.1%; ag/commodity tape mid-vol.
- `graph/technicals.md#technicals.gld` — 431.68, vol 28.0%; real-asset cluster correlation reference.
- *Missing direct nodes:* MOS, NTR, ICL, ICL.TA, MOO (ag ETF), VEGI (agribusiness ETF) technicals not in current graph (yfinance feed pulls SPY-cluster + sector ETFs + mega-caps + crypto + macro proxies). Single-name phosphate technicals via web_search; flagged as feed-extension candidate.

**Sentiment.**

- `graph/sentiment.md#sentiment.fed_policy_stance` — mean 0.05, sd 0.25, fuzz_halo HIGH. Low-information.
- *No phosphate-specific sentiment node.* Web_search prose only. Flagged. (Note: low narrative coverage is *thesis-positive* for phosphate — pre-recognition signal.)

**Flows.**

- `graph/flows.md` — *empty.* Per assumption 11, structural blind spot. **Cannot probe crowding on MOS/NTR/ICL or MOO/VEGI ETFs.**

**Fundamentals.**

- `graph/fundamentals.md` — *EDGAR stub.* Per assumption 12, single-name fundamentals not directly readable. MOS Q4 2025 segment data, ICL bromine segment, NTR potash–phosphate split — all from web_search prose.

**Edges.**

- `graph/edges.md#edge.crowding-to-drawdown` — illustrative reflexive edge; *less applicable* to phosphate than to uranium/REE because narrative crowding is structurally lower.
- *Implied edge (not in graph):* `edge.china-quota-to-dap-price` — direct, ~3–6 month latency, strength mean ~0.6. Belief-Collapse candidate.
- *Implied edge:* `edge.dap-price-to-mos-realisation` — direct, near-zero latency on realised pricing, multi-quarter latency on equity-multiple expansion (~6–12 months). Strength mean ~0.7. Implicit in vehicle choice.
- *Implied edge:* `edge.henry-hub-to-mos-margin` — direct, ~1 quarter latency, strength mean ~0.4 (partial — MOS Florida + Saskatchewan are integrated; not pure-play ammonia).

**Portfolio.**

- `graph/portfolio.md#portfolio.current` — schema only; broker feed not wired (assumption: no current phosphate exposure). Sleeve sizing additive, not adjustment.

**Cluster context (load-bearing for sizing).**

- Sibling open Type B sleeves with tentative sizing: Lynas/REE (1.5%), uranium (4%), silver (4%). Combined existing target = **9.5% NAV**. Architect's proposed Type B cluster cap (A6): **6–10% NAV**. Phosphate at any size pushes the cluster *above 10%*. **This is the binding constraint of this inquiry.**

## Intent

Output sizing recommendation in NAV %, vehicle mix, E[R]/E[risk], brittle assumption — *conditional on cluster-cap resolution*. Two-track recommendation:
- **Track A (cluster cap firm at 10%):** trim a sibling sleeve OR fund phosphate inside a tightened envelope.
- **Track B (cluster cap raised by user to 12% on diversification argument):** size phosphate fully on its own merits.

Confidence on sizing recommendation: 0.55 (medium). Higher than a uranium-class candidate on thesis-conviction (food-security demand floor is more deductively-tight than AI-capex demand floor), lower on price-discovery precision (no curve feed, no flows feed). Macro-conditional features carry their own haircuts.

## Self

- `self.capability` — Convergent capital-sizing inquiry. Can build per-vehicle return distributions from parent screen asymmetry bounds + sober adjustments; can compute drawdown distributions and E[R]/E[risk]; can apply cluster cap. *Cannot* run live MOS/ICL/NTR DCF (EDGAR stub), cannot price option overlays (no CBOE feed), cannot read DAP futures curve (no commodities-curve feed), cannot probe crowding (no flows feed). All four gaps encoded as confidence haircuts (assumptions 11–15).

- `self.calibration` — No prior closed phosphate / Type B inquiries on this instance. Industry prior on Type B disciplined-screen hit rate ~0.30–0.40; payoff multiple on hits ~3–8x (per parent screen). For ag-commodity-cycle equities specifically, industry prior on cycle-return is asymmetric: peak-to-trough median drawdown −45 to −60% (MOS 2014–2020), peak-to-trough median upside +250 to +400% (MOS 2020–2022). The current set-up resembles 2020 entry — bottoming with first supply-side discipline visible. Treat point estimates as priors; report distributions.

- `self.taste` — Bias toward (a) demand-floor theses that survive S3 (recession) — phosphate is the cleanest demand-floor candidate in v2; (b) supply bottlenecks where the marginal producer is rational (OCP, Ma'aden) over those where it is fragmented; (c) "boring story" theses that lack narrative crowding — phosphate passes the boring-story test cleanly. Counter-bias: I tend to under-weight ag-affordability downside (assumption 4) because the deductive demand floor is so prominent; sober-case modelling should reflect that affordability *can* compress application even when biological demand stands. Counter-bias 2: I tend to over-weight cluster diversification arguments and may push phosphate sizing above what cluster-cap discipline supports — surface this explicitly to user.

- **Bias probes for this run.**
  - *Narrative seduction* — would I size this if the China-tariff retaliation story were boring? Probed: even without the China-quota catalyst, OCP supply discipline + ag-cycle bottoming + recognition-latency math support the thesis at 60% of current conviction. Survives the boring-story test, at lower-end size band.
  - *Recency bias* — DAP recovered from $400 (2024) to $580 (Q1 2026); am I extrapolating to $700+? Probed: upside in Prediction is bounded by Saudi Ma'aden cost-curve and OCP capacity discipline, not extrapolation. Bounded.
  - *Tail neglect* — am I Gaussian-shaping phosphate? Probed: drawdown distribution is bounded by replacement-cost-of-asset (MOS Florida + Saskatchewan integrated mining infrastructure not easily reproduced; ICL Dead Sea concession is structurally unique). Tail is bounded *more tightly* than uranium/REE because both companies have hard physical-asset floors. Less bimodal than uranium (no Centrus-style HALEU monopoly to lose).
  - *Implicit factor bet* — phosphate sleeve adds to the "supply-bottleneck industrial" cluster. *But* its demand chain is uncorrelated with AI-capex, partially decorrelated with recession (assumption 6). Probed: phosphate is the *least* implicit-factor-coupled candidate in the v2 set. This is the diversification-within-cluster argument for raising cluster cap.
  - *Cluster-cap discipline* — am I motivated-reasoning toward "phosphate is special, raise the cap"? Probed: argument is structurally sound (independent demand chain, S3-survival) but Track A (trim a sibling) is the disciplined path. Both tracks reported.

## M-nodes (sequence)

1. **`m.probe.scope`** — sharpened from "size phosphate" to "size a phosphate sleeve, three-vehicle mix (MOS/ICL/NTR), within or beyond the Type B cluster cap proposed by portfolio-architecture A6, with the diversification-within-cluster argument as a separate first-principles consideration". Outcome window 12 months (sizing decision judged at 12mo) with 24mo overlay because thesis recognition window is 12–24mo.

2. **`m.probe.prior-art`** — consulted:
   - `methods.md` — Kelly (haircut for fat-tail), drawdown bound (hard stop), scenario stress (S1–S8), factor exposure (food-security cluster vs supply-bottleneck industrial cluster).
   - `blind-spots.md` — narrative seduction, recency, tail neglect, implicit factor bets, crowding risk, regime-change blindness (ag-cycle 2014–2020 vs 2020–2022 regime).
   - `strategies.md` — Type B criteria, all five gates passed by parent v2.
   - parent `2026-05-08-type-b-screen-v2.md` rank-1 entry — asymmetry 3:1, drawdown −35%, vehicle mix.
   - sibling `2026-05-09-uranium-sizing.md` — sleeve-construction template (core spot + torque), drawdown-bounded sizing math, cluster-cap coordination flag.
   - sibling `2026-05-08-portfolio-architecture.md` — scenario distribution, cluster cap A6, hole H2.

3. **`m.probe.world`** — graph snapshot read; gaps confirmed (FRED, EDGAR, flows, CBOE, commodities-curve, single-name technicals). Web_search supplements for: Q1 2026 China DAP/MAP export print, OCP capex schedule + IPO timeline, MOS Q4 2025 phosphate-segment realised pricing, ICL Q4 2025 results, India 2025–2026 DAP tender clearing prices, Brazilian fertilizer import volumes, Saudi Ma'aden capacity announcements, US Henry Hub strip, CBOT corn/soybean strip.

4. **`m.probe.edges` — factor-coverage walk** (per amendment `2026-05-08-factor-coverage-checklist`).

   - **macro (rates, growth, inflation, fiscal).** Per FOMC distribution, dovish bias on cuts paths totals 0.40 — supports MOS multiple at the margin (~5–8% per 50bp). Real-rate path approximated by `macro.cfx_tlt`. Inflation re-acceleration (assumption 5 gas spike scenario) is the more material macro variable than rates. **FRED gap → −20% confidence haircut (assumption 13);** lower than uranium because phosphate is less rate-sensitive. *Probed (low-resolution).*

   - **geographic (jurisdiction, sanctions, trade).** Morocco (OCP, supply-discipline, IPO catalyst), Israel (ICL, Dead Sea concession + 2023–2025 conflict-resilient operations), US (MOS Florida + Saskatchewan integration), Canada (NTR potash-heavy), China (export-quota lever — assumption 2), Russia (sanctioned, removed from market — implicit supply-side support). India + Brazil + SEA on demand side (assumption 1). **Geographic factor is the *primary* bottleneck** — load-bearing on assumptions 2, 3, 7. *Probed.*

   - **regime (vol, liquidity, dispersion).** Vol regime mid-elevated. MOS realised vol estimated 30–38% (commodity-cyclical name); NTR 25–32% (more diversified, potash-heavy); ICL 28–35%. Lower than uranium small/mid-caps; more retail/passive participation via DBA/MOO/VEGI ETFs. Dispersion within fertilizer space: phosphate vs potash vs nitrogen has been tightly cointegrated historically; current divergence (potash recovered first, phosphate lagging on equity multiples despite price recovery) is a positive signal for mean reversion. *Probed.*

   - **correlation structure.** DAP price ↔ MOS realisation: near-1 ex multiple drift. MOS ↔ NTR: high (~0.7) in regime moves; decoupled idiosyncratically (NTR potash + Brazil retail). MOS ↔ ICL: moderate (~0.5); ICL has bromine + specialty optionality. ICL ↔ Israel-equity factor: high (USD-investor returns dampened by ILS volatility under conflict scenarios). Phosphate cluster ↔ AI-capex factor: ~0 (this is the diversification argument). Phosphate cluster ↔ Type B real-asset cluster (REE/uranium/silver): low-to-moderate (~0.2–0.4) — different demand chains. Phosphate ↔ broad market in S3: less negative than industrial cyclicals (food-security demand floor); historical 2008–2009 MOS −60% vs broad XLB −45% — *worse* than market in deep recession via input-cost spike + farmer destocking. **Counter to the recession-survival narrative**: 2008 MOS *did* drawdown more than market because ag-affordability collapsed via corn at $3 + diesel spike. Assumption 6 must respect this historical case. *Probed; informed sober-case model.*

   - **flows / crowding.** **N/A with reason: no flows feed (assumption 11).** *But* — phosphate has low narrative coverage and low retail crowding (no AI/defense story); first-principles confidence is higher than for uranium/REE. Probed: agribusiness ETF (MOO/VEGI) flows have been net-outflow 2022–2025 per public ETF tracker references; positioning likely *light*, not crowded. **Mitigation:** size at *middle* of mandate envelope (vs lower-end for uranium) because crowding risk is structurally smaller. Lower haircut applied (assumption 11).

   - **themes.** `themes.ai-capex-cycle` — *not load-bearing*; this is the diversification argument. Implicit `themes.food-security-bifurcation` (not yet a graph node) is the relevant theme. *Probed; flagged for graph-update.*

   - **reflexivity.** Pre-recognition: positioning building → DAP price up via term-contracting → equity multiples expand → more positioning. Post-recognition: positioning blowoff → DAP reverts → equity multiples derate. Lower current positioning means the reflexive *upside* path has more runway and the reflexive *downside* path has less risk than for uranium/REE. *This is a structural advantage for phosphate sizing within Type B.* *Probed.*

   - **liquidity / capacity.** MOS NYSE ADV ~$200–300m → fully liquid for $50k–$5m. NTR NYSE ADV ~$250m → fully liquid. ICL NYSE ADR ADV ~$30–60m → liquid for $50k–$2m, slightly slippage-sensitive at upper end. ICL.TA local ADV ~ILS 80m → liquid via ADR for USD investor. All three vehicles materially more liquid than uranium small/mid-caps or REE single-names. *Probed; liquidity is not a gating constraint.*

5. **`m.reframe`** — Reframed twice:
   - First reframe: original framing was "size MOS as primary, ICL/NTR as secondary". Reframed to *three-vehicle balanced sleeve* because the diversification argument across Morocco-OCP exposure (none of these names hold OCP equity directly — OCP IPO is a future catalyst affecting all three via reference valuation), US/Florida (MOS), Israel/Dead-Sea (ICL bromine optionality), and Canada/Saskatchewan-potash (NTR) gives jurisdictional + product-mix diversification within sleeve.
   - Second reframe: "size phosphate within cluster cap" reframed to "size phosphate while explicitly surfacing the cluster-cap binding constraint and presenting both Track A (trim sibling) and Track B (raise cap on diversification argument) for user collapse". Forced by the parent inquiry observation that REE + uranium + silver = 9.5% NAV — phosphate at any size pushes above the upper cap bound.

6. **`m.test.feasibility`**:
   - *capability* ✓ — sleeve constructable in available accounts; MOS + NTR on NYSE, ICL ADR on NYSE.
   - *constraint* ✗→⚠ — *binding cluster-cap conflict.* Existing tentative cluster sizing 9.5% + any phosphate >0.5% breaches A6 upper bound 10%. This inquiry must surface to user before capital-Collapse.
   - *budget* ✓ — sleeve target 2.5–4% NAV gross (see Prediction); Track A trims a sibling; Track B requires user belief-Collapse on cluster-cap raise.
   - *data quality* — flagged via assumptions 11–16 with explicit confidence haircuts.
   - *mandate* — no leverage, no shorting, no derivatives — consistent.

7. **`m.collapse`** — capital-Collapse pending user gate. **Collapse is contingent on:**
   (a) user posterior on China-tariff escalation (politics.us-china-tariff-regime-2026) — nudges target sizing within the band;
   (b) user posterior on recession-survival robustness for phosphate (assumption 6) — central to whether this earns Type B cluster headroom;
   (c) user resolution of cluster-cap conflict — Track A (trim) or Track B (raise to 12%) or Track C (defer phosphate to post-recognition Type A reframe);
   (d) user acceptance of A6 cluster cap itself — if A6 not yet collapsed, this inquiry's sizing is provisional.

## Prediction (convergent)

All distributions reported as quantile sketches with explicit failure-path joint probabilities. Confidence haircuts (assumptions 11 −20%, 12 −20%, 13 −20%, 14 full on options, 15 −15%, 16 −10%) applied multiplicatively to thesis-conviction; sleeve sizing is *post-haircut*.

### Vehicle-level return distributions (12 months)

Per parent v2 screen rank-1 entry, scaled to 12mo (parent quoted 18–24mo bands; 12mo represents under-incubation). Quantiles subjective, derived from parent's ranges with sober adjustment for recognition-latency on a 12mo lens.

| Vehicle | P10 | P25 | P50 | P75 | P90 | E[R] (12mo) | Tail-loss (P5) |
|---------|-----|-----|-----|-----|-----|-------------|----------------|
| MOS | −30% | −12% | +12% | +45% | +90% | **+18%** | −38% |
| ICL | −28% | −10% | +10% | +35% | +65% | **+13%** | −35% |
| NTR | −22% | −7%  | +8%  | +28% | +50% | **+10%** | −28% |

Notes:
- MOS P50 +12%: DAP price drift to $620–650 + multiple expansion partial; bounded above by 12mo recognition incomplete.
- ICL P50 +10%: phosphate + potash + bromine optionality; bromine contributes asymmetric upside on EV-battery flame-retardant demand (bonus optionality, not load-bearing).
- NTR P50 +8%: potash-heavy mix dampens phosphate upside; provides recession ballast and liquidity.

### Vehicle-level return distributions (24 months)

Per parent v2 screen native horizon.

| Vehicle | P10 | P25 | P50 | P75 | P90 | E[R] (24mo) |
|---------|-----|-----|-----|-----|-----|-------------|
| MOS | −22% | +5%  | +45%  | +95%  | +160% | **+50%** |
| ICL | −20% | +5%  | +35%  | +75%  | +120% | **+38%** |
| NTR | −15% | +5%  | +25%  | +55%  | +90%  | **+28%** |

Notes:
- 24mo P50 reflects recognition-window centre: India tender at >$650, China extends quota, OCP IPO valuation reference unlocks comparable multiples, MOS multiple expands to 9–10x EBITDA from current ~7x.
- MOS 24mo P10 stays −22% bounded by replacement-cost-of-asset; downside is *less deep* than uranium LEU because no monopoly to lose, but *more frequent* than spot-uranium SRUUF because equity-multiple subject to ag-cycle.

### Vehicle-level drawdown distributions (peak-to-trough inside 12 months)

| Vehicle | Median DD | P75 DD | P95 DD (tail) | Hard floor |
|---------|-----------|--------|----------------|-----------|
| MOS | −18% | −30% | −42% | Replacement-cost-of-asset Florida + Saskatchewan ~$22/sh vs current ~$30 → ~−40% |
| ICL | −15% | −28% | −40% | Potash + bromine asset floor ~$4.5/sh vs current ~$6 → ~−35% |
| NTR | −12% | −22% | −32% | Saskatchewan potash franchise ~$45/sh vs current ~$58 → ~−28% |

### Sleeve construction — recommended mix

**Two tracks per the cluster-cap conflict:**

#### Track A — Cluster cap firm at 10%; phosphate funded by trimming a sibling

Net new sleeve target: **2.5% NAV** (within 2–3.5% band; centred at 2.5% post-haircuts), funded by trimming uranium 4% → 3.0% and silver 4% → 3.5% (combined trim 1.5%) AND adding 1.0% from incremental NAV. Net cluster: REE 1.5 + uranium 3.0 + silver 3.5 + phosphate 2.5 = **10.5%**. *Still slightly over upper cap;* tighten further or accept marginal breach. Recommended trim path: uranium 3.0 + silver 3.5 + phosphate 2.0 = 10.0% on the nose.

| Vehicle | NAV % (Track A) | Within-sleeve % | Rationale |
|---------|-----------------|------------------|-----------|
| MOS | 1.2% | 60% | Highest-torque pure-play. Liquidity ample. Bounded drawdown via Florida + Saskatchewan asset floor. |
| ICL | 0.5% | 25% | Diversification within sleeve (potash + bromine + Israeli concession). Lower beta than MOS. |
| NTR | 0.3% | 15% | Recession ballast (potash-heavy). Liquid. Lowest expected return but lowest drawdown. |

Sleeve-level expected return (12mo, weighted): **+15%**.
Sleeve-level expected drawdown (median, partial-correlation adjusted): **−16%**.
Sleeve-level tail loss (P5): **−37%** at sleeve = −0.74% NAV book impact.

#### Track B — Cluster cap raised to 12% on the diversification-within-cluster argument

Sleeve target: **3.5% NAV** (within 3–4% band), additive to existing cluster. Cluster: REE 1.5 + uranium 4 + silver 4 + phosphate 3.5 = **13%**, *which breaches 12%* — Track B realistically caps phosphate at **2.5%** to reach 12% exact, OR requires further marginal trims.

| Vehicle | NAV % (Track B) | Within-sleeve % | Rationale |
|---------|-----------------|------------------|-----------|
| MOS | 1.5% | 60% | Same as Track A, slightly larger. |
| ICL | 0.6% | 25% | Same. |
| NTR | 0.4% | 15% | Same. |

Sleeve-level expected return (12mo): **+15%**. Sleeve-level expected drawdown: **−16%**.

#### Track C — Defer phosphate; reframe as Type A "resilient real-asset compounder"

If user is unwilling to (a) trim siblings or (b) raise cap, defer phosphate to a Type A reframing inquiry — phosphate has many resilient-compounder characteristics (multi-decade asset base, reserves-life multi-generational, dividend-paying, non-substitutable demand). Suggested inquiry: `2026-05-22-phosphate-as-type-a` (divergent, belief). This is the conservative path; sacrifices the recognition-window asymmetry but preserves optionality.

### E[R] / E[risk] ratio (sleeve-level, Track A or Track B equivalent at 2.5% NAV)

Two formulations (per `methods.md`):

- **E[R] / median drawdown:** +15% / 16% = **0.94** (12mo).
- **E[R] / P5 tail-loss:** +15% / 37% = **0.41** (12mo, conservative).

24mo equivalents (E[R] +40%, median DD ~22%, P5 tail ~45%):
- E[R] / median drawdown ≈ +40% / 22% = **1.82**.
- E[R] / P5 tail-loss ≈ +40% / 45% = **0.89**.

For comparison, parent v2 screen quoted asymmetry ~3:1 = 3.0 (qualitative). Our 24mo E[R]/median-DD ≈ 1.82 lands somewhat below that headline, post-haircut — consistent with the haircuts compounding (assumptions 11–16 cumulative drag ~25–30% on conviction). The 12mo number is materially worse because recognition window is 12–24mo and 12mo measurement under-incubates the thesis.

**Optimization-target verdict:** sleeve E[R]/E[risk] is **favourable on the 24mo measurement** (≥1.5 on median-DD denominator) and **borderline on the 12mo** (0.94). User should be aware the optimization target wants the 24mo lens. Outcome window 12mo is a *check-in*, not the verdict horizon.

**Comparison vs sibling sleeves at same horizon (24mo, median-DD):**
- Uranium sleeve: 2.13
- Phosphate sleeve: 1.82
- (Lynas/REE sleeve: not yet computed at this depth)
- (Silver sleeve: not yet computed at this depth)

Phosphate underperforms uranium on raw E[R]/E[risk] but offers cluster-diversification value (zero AI-capex coupling). Net portfolio-level contribution under H2 (AI-capex over-concentration) is potentially *higher* than uranium's marginal contribution despite lower absolute ratio. **This is the load-bearing argument for Track B.**

### Sensitivity — brittle assumption + threshold

Single-perturbation sweep across assumptions 1–10. Surfacing the dominant brittle link.

**Brittle assumption: #6 — Recession demand-floor robustness (S3 phosphate behaves utility-like, ≤8% volume compression).**

This is brittle because:
- It is the *only* assumption that directly load-bears the cluster-cap raise argument (Track B). Without S3-survival, phosphate is not a diversifier — it is just another cyclical-commodity exposure.
- Historical 2008–2009 case (MOS −60%) demonstrates the failure mode: ag-affordability collapse via corn-price crash + diesel spike triggers farmer destocking even when biological demand stands. Phosphate *can* drawdown >35% in a deep affordability shock.
- Failure path is path-dependent: once farmer destocking starts, application volumes can lag biological demand by 2–3 quarters (lag absorbed by soil-P stocks).

**Threshold to flip:**
- *Trigger:* CBOT corn print sustained <$3.80 for >2 quarters AND CBOT diesel/Henry Hub gas spike >40% in same window AND DAP price compresses >15% from $580.
- *Action on flip:* exit MOS leg fully (estimated immediate −18–30% mark on the leg); rebalance to ICL (potash + bromine ballast, less ag-affordability sensitive) at 50% of original phosphate weight; defer NTR (potash drawdown likely correlated). Sleeve cuts from 2.5% NAV to ~0.6% NAV.
- *Sleeve impact under flip:* book impact on flip ≈ −0.45% NAV; sleeve E[R] (24mo) recompresses to ~+15% on residual ICL position alone.

**Secondary brittle assumption: #2 — China phosphate export-quota persistence.**

If China rolls back DAP/MAP quota (p≈0.15), seaborne supply rebalances faster, DAP compresses 10–15% from $580. Combined with assumption-6 partial weakening, sleeve E[R] (24mo) drops from +40% to +12–18%. **Threshold to flip:** explicit MOFCOM rescission OR sustained quarterly export volume restoration to >90% of 2022 baseline.

**Tertiary: assumption #4 — corn–soybean band.**

If corn prints <$3.80 sustained, ag-affordability compresses; assumption 6 secondary trigger; sleeve E[R] (24mo) drops 8–12pp.

**Robust to:** assumption 8 (operational continuity — affects single names idiosyncratically, not sleeve), assumption 5 partial (gas spike — bounded by ICL/NTR diversification away from US gas exposure), assumption 9 (recognition latency — affects timing not magnitude inside 24mo window), assumption 7 (Saudi Ma'aden cost-floor — bounded by OCP discipline).

### Cluster-cap flag

Per portfolio-architecture A6, this sleeve must be *coordinated* with `2026-05-09-lynas-sizing` (REE), `2026-05-09-uranium-sizing` (uranium), `2026-05-09-silver-sizing` (silver). Combined Type B cluster sleeve **must not exceed 6–10% NAV**.

**Current cluster math:**
- REE / Lynas: 1.5% (tentative)
- Uranium: 4.0% (tentative)
- Silver: 4.0% (tentative)
- **Subtotal: 9.5% NAV**
- Phosphate (this inquiry): 2.5% recommended → cluster = 12.0% → **breach of upper cap by 200bp**.

**Resolution paths for user collapse:**
- **Track A (recommended baseline):** trim uranium 4 → 3.0 and silver 4 → 3.5 to make room; phosphate at 2.0% NAV; cluster lands at 10.0% exact. Justification: phosphate's recession-survival demand floor (assumption 6) is *more* robust than uranium's hyperscaler-PPA demand chain or silver's solar-PV demand chain in S3; the trim improves cluster S3-survival.
- **Track B (acceptable on diversification argument):** raise cluster cap from 10% to 12% on the basis that phosphate's demand chain is uncorrelated with AI-capex; phosphate at 2.5% NAV; cluster lands at 12.0%. Justification: A6's 10% cap was written before phosphate candidate emerged in v2 screen; phosphate materially changes the cluster's factor profile; cap should reflect post-v2 reality.
- **Track C (conservative):** defer phosphate; reframe as Type A. Surrenders recognition-window asymmetry; preserves cluster discipline.

**Recommendation:** Track A as baseline (preserves cluster discipline; trims overlapping AI-capex-coupled siblings; phosphate enters as decorrelation-adding sleeve at cluster-equivalent weight). Track B if user is comfortable explicitly amending A6.

### Sizing recommendation

**Track A baseline: phosphate sleeve at 2.0% NAV, mix 60/25/15 MOS/ICL/NTR, with companion trims of uranium (4 → 3.0%) and silver (4 → 3.5%). Cluster lands at 10.0%.**

If user posterior on recession-survival (assumption 6) is **>0.80** (confident phosphate is utility-like in S3), recommend Track B upper bound: **3.0% NAV (no companion trims), cluster cap raised to 12.5%.**

If user posterior on recession-survival is **<0.55** (skeptical), recommend Track C: **defer phosphate; reframe as Type A** in subsequent inquiry; preserves optionality without consuming cluster headroom.

Either way, **maintain MOS as ≥55% of sleeve** — MOS is the highest-torque pure-play and aligns the sleeve with the central recognition trigger (DAP price + India tender). ICL provides bromine/potash optionality. NTR provides recession ballast and liquidity.

**Vehicle preference rationale (explicit per parent screen).**
- *MOS (60% of sleeve).* US-listed liquidity; pure-play DAP/MAP exposure with Saskatchewan potash as secondary; replacement-cost asset floor on Florida + Saskatchewan integration; highest 24mo upside.
- *ICL (25% of sleeve).* Hybrid potash + phosphate + bromine + magnesium; Israeli Dead Sea concession unique and durable; bromine optionality on EV-battery flame-retardant. Lower-beta sleeve component.
- *NTR (15% of sleeve).* Saskatchewan potash franchise as ballast; 26% phosphate exposure; high liquidity, dividend-paying. Provides recession-protection inside sleeve; lowest expected return but lowest drawdown.

### Coordination flag

Per portfolio-architecture A6, this sleeve must be coordinated with siblings. **The cluster-cap conflict is the central unresolved item for user collapse.** Recommend the user:

1. Collapse `2026-05-15-type-b-cluster-sizing` (the A6 belief-Collapse) explicitly, choosing Track A vs Track B vs Track C.
2. Then capital-collapse this phosphate inquiry plus the companion sleeves (uranium, silver) at the chosen cluster envelope.

If A6 is not yet collapsed, this inquiry's sizing is provisional pending the cluster envelope.

## Outcome

_Locked until 2027-05-15._

## Reflection

_Locked._
