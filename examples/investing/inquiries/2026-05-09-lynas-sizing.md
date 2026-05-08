---
id: 2026-05-09-lynas-sizing
shape: convergent
collapse_flavour: capital
status: open
scope: "Sizing decision for heavy rare earths ex-China exposure (Lynas / MP / REMX) under Type B archetype."
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

# Inquiry: Heavy rare earths ex-China sizing

## Scope

Decide capital allocation to a heavy rare earths ex-China sleeve (NdFeB / Dy / Tb supply chain) — primary vehicle Lynas (LYC.AX), secondary MP Materials (MP), basket via REMX. Ranked #1 in 2026-05-08 Type B screen. Demand-deduction chain (EV motors + defense + robotics + MRI + wind), supply bottleneck (~85% Chinese refining concentration; export-control regime escalation), recognition window open, drawdown bound −40% under thesis-failure path.

In scope: vehicle selection within sleeve, sizing range with confidence interval, drawdown distribution, asymmetry distribution, sensitivity, Collapse recommendation.
Out of scope: trade execution, operational implementation, currency overlay (deferred).

## Assumptions (load-bearing)

Numbered, falsifiable. Failure of any single assumption with a "verdict-flipping" tag below collapses the recommendation.

**Demand-side**

1. **EV adoption rate.** Global plug-in vehicle production reaches 28–34M units in 2030 (base path), with PHEV+BEV NdFeB-magnet penetration ≥ 80% of traction-motor designs. Failure → demand-pull on Dy/Tb compresses materially; downside skews wider.
2. **Dy/Tb intensity per motor.** Average traction motor uses 1.5–3.0 kg of NdFeB; Dy + Tb content 3–6% by mass for high-temperature stability. Substitution research (Dy-free grain-boundary diffusion, ferrite hybrids) does not displace > 25% of high-temperature motor demand inside 36 months. Failure → 12-month upside compresses by ~half; thesis remains alive on defense + wind floor.
3. **Defense / robotics / wind demand floor.** F-35, precision-guided munitions, MRI machines, industrial robotics actuators, and offshore-wind direct-drive generators provide a Dy/Tb demand floor independent of EV path; floor magnitude ≥ 30% of base-case Dy/Tb consumption by 2028. Failure → asymmetry intact but slower realisation.

**Supply-side**

4. **China export-control posture.** China retains the 2024–2025 export-licensing regime on heavy rare earths (Sm/Tb/Dy/Gd) and tightens enforcement through outcome window (2027-05). Probability hold ≥ 0.70; rollback ≤ 0.15; further escalation ≤ 0.15. Failure (rollback) → **verdict-flipping**: thesis collapses near-immediately with -25 to -45% sleeve drawdown over 30–90 days.
5. **Lynas execution risk.** Kalgoorlie heavy-circuit reaches ≥ 60% nameplate Dy/Tb separation throughput by Q4 2026; Mt Weld feedstock grade and recovery hold to within ±15% of FY25 guidance; Malaysia LAMP licence renewed without curtailment. Failure (single severe ops miss) → -25 to -35% on LYC.AX, -10 to -20% on MP/REMX through contagion.
6. **Refining bottleneck longevity.** Western mine-to-magnet capacity outside Lynas + MP Stage III remains < 15% of global Dy/Tb supply through 2028 (Energy Fuels, Ucore, Iluka, Vital Metals all > 24 months from commercial output). Failure → upside compresses; floor preserved by Lynas first-mover position.
7. **Recognition trigger plausibility.** At least one of: (a) a publicly disclosed China export-licence denial to a Western auto/defense customer, (b) Lynas reporting Dy/Tb separation revenue at premium realised pricing, or (c) a US/EU heavy-REE strategic-stockpile contract — occurs inside 12 months. Probability ≥ 0.55. Failure → recognition window slides right; not a thesis kill, a duration mismatch.

**Liquidity / vehicle**

8. **Liquidity at sleeve size.** ASX LYC.AX and NYSE MP each clear $2–5M USD/day at < 20bps slippage; REMX ETF clears > $4M/day. Failure → cap sleeve allocation to liquidity-constrained scale; no thesis change.

**Feed-gap-promoted assumptions (per 2026-05-08 amendment "feed-gap-promotes-to-assumption")**

9. **Macro proxy (FRED missing).** Assume macro regime is approximated by `macro.cfx_uup` (DXY proxy 27.41, vol 5.9%), `macro.cfx_eurusd_x` (1.1737), `macro.cfx_dbc` (30.25), `macro.cfx_tlt` (85.65), and the news-summarizer FOMC distribution (`politics.fomc_rate_path_may2026`, hold-through-June p≈0.55). Confidence haircut **−25%** on macro-conditional sub-claims. Resolves when FRED feed hydrates (rates / CPI / IP / payrolls).
10. **Fundamentals proxy (EDGAR stub).** Assume LYC.AX and MP financial fundamentals are approximated by web-search-grade qualitative valuation (Lynas single-digit EBITDA multiple on bottom-cycle pricing; NTA ≈ AUD 4/sh) and price action. Confidence haircut **−20%** on single-name valuation gap. Resolves when EDGAR + ASX filings feed hydrates.
11. **Crowding proxy (no flows feed).** Assume positioning / crowding for the sleeve is approximated by first-principles reasoning + observable ETF AUM trends (REMX small relative to MOAT/QQQ; MP institutional ownership concentrated; LYC.AX moderate Western fund holdings). Confidence haircut **−20%** on the recognition-window narrowness claim. Resolves when a flows / 13F / ETF-flow feed registers (architect's proposed adjustment A3).
12. **No live broker feed.** Assume entry executes within ±3% of current LYC.AX (~AUD 8) and MP (~USD 25–35 area) reference levels; no slippage shock. Confidence haircut **−10%** on entry-price assumption. Resolves when broker feed wires.

**Drawdown-bound construction (per parent assumption #10)**

13. **Drawdown bound is forward thesis-failure path** = max plausible 12-month decline conditional on assumption (4) or (5) failing severely, weighted by their joint probability. Not historical max drawdown. Quantified at -40% sleeve-aggregate; -55% LYC.AX worst-case; -45% MP worst-case; -30% REMX worst-case (basket diversifies single-name execution risk).

## Graph references

Pulled from snapshot 2026-05-08T09:00Z. One-line relevance each.

**Strategy**
- `strategy.type-b.current_candidates[rank=1]` — this inquiry's parent claim; carries demand-chain, bottleneck, recognition window, asymmetry, drawdown bound from the screen.
- `strategy.portfolio-architecture.scenario_set` — sleeve win/lose mapping across S1–S8; REE wins under S2 (stagflation, p=0.18), S5 (geopolitical escalation, p=0.10), S6 (reflation, p=0.08); loses under S3 (recession + cuts, p=0.14) and S4 (AI-capex peak, p=0.20). Sleeve-weighted scenario expectation positive but macro-conditional.
- `strategy.portfolio-architecture.balance_assessment.holes[H3]` — no flows feed; reflexivity probe is structurally blind for this thesis (recognition-window theses are the most reflexive). Drives haircut #11.
- `strategy.portfolio-architecture.proposed_adjustments[A6]` — tighten Type B sizing discipline (sequence + concentration cap); cluster cap relevant when REE sizes alongside uranium + silver children.

**Themes**
- `themes.ai-capex-cycle` (p_peak_within_18mo=0.45, confidence 0.55) — second-order: AI power demand → wind/grid → REE permanent magnets via wind generators; supports demand floor independent of EV path. Power-binds-before-chips claim is consistent with REE upside.
- `themes.capital_framework_overhaul` — not load-bearing here; noted only because it sets a deregulatory tilt that supports US strategic-mineral spending.

**Politics**
- `politics.regulatory_deregulation_posture` (moderate_easing p=0.50) — supports US Defense Production Act / DoD strategic-stockpile and IRA-domestic-content disbursements that benefit MP and Lynas's US partnership.
- `politics.fomc_rate_path_may2026` (hold_through_june p=0.55, fuzz_halo VERY HIGH) — neutral for sleeve directly; matters only via USD path (assumption 9 proxy).
- `politics.us-china-tariff-regime-2026` (status-quo p=0.50, escalation p=0.35, partial-rollback p=0.15) — escalation tightens the export-control thesis; partial-rollback is the verdict-flipping path (assumption 4).

**Macro**
- `macro.cfx_uup` 27.41, vol 5.9% — DXY proxy steady; weak-USD tailwind for AUD-denominated LYC.AX is absent. Mildly negative for AUD entry timing, not thesis-altering.
- `macro.cfx_eurusd_x` 1.1737 — EUR firmer; supports EU defense + auto OEM demand for ex-China REE supply.
- `macro.cfx_dbc` 30.25, vol 23.1% — broad commodity tape mid-vol; consistent with real-asset bid backdrop.
- `macro.cfx_tlt` 85.65 — long-duration soft; consistent with no immediate recession pricing (S3 not the modal scenario).

**Sentiment**
- `sentiment.fed_policy_stance` (mean +0.05, sd 0.25, fuzz_halo HIGH) — neutral-to-slight-hawkish; treat USD/AUD-cross sub-claims as low confidence (folds into haircut #9).

**Technicals**
- `technicals.gld` 431.68, vol 28.0% — gold strong; supports the "real assets bid" backdrop reflexively favourable for REE narrative.
- `technicals.dbc` 30.25, vol 23.1% — broad commodities mid-vol; sleeve-supportive backdrop.
- `technicals.spy` 731.58, vol 15.94% — broad equity vol modest; suggests no immediate market-stress liquidation risk for the sleeve.
- `technicals.iwm` 282.26, vol 21.22% — small-cap vol elevated relative to large-cap; LYC.AX behaves more like a small/mid-cap miner; tail beta to small-cap risk-off.

**Fundamentals**
- `fundamentals.*` — stub only (EDGAR feed empty). Drives haircut #10. LYC.AX and MP fundamentals are qualitative-only at this snapshot.

**Graph gaps that limit confidence (carried from parent + amendment)**
- FRED missing — assumption #9.
- EDGAR stub — assumption #10.
- No flows feed — assumption #11.
- No CBOE / options feed — implied vol on MP / LYC unknown; option-overlay sizing deferred.

## Intent

Output a sizing recommendation in NAV % with E[R]/E[risk] ratio, brittle assumption identified, and child Collapse-ready capital decision. Confidence: medium (~0.50–0.55, weighted by feed-gap haircuts).

## Self

- **self.capability** — Vehicle-aware sizing within a Type B sleeve. Web_search and graph snapshot available; no live broker, options, or flows feed. Cannot run live factor regression or option-implied vol surfaces from this seat. Can construct a forward thesis-failure drawdown distribution and a scenario-weighted return distribution.
- **self.calibration** — **No prior closed Type B inquiries on this instance**; no track record yet. Per parent inquiry, base-rate Type B hit-rate prior ≈ 0.30–0.40 with payoff multiple on hits ≈ 3–8x (industry prior, not measured here). All numbers below are priors awaiting outcome data; treat the E[R] / E[risk] number as a *relative ranking signal*, not a precise expectation.
- **self.taste** — Per parent: structurally-bottlenecked physical-supply theses preferred over narrative trades; bias against any candidate failing the boring-story test (here: REE passes — the deductive chain is dull and physical, not narrative); bias against single-name concentration when fundamentals graph is stub-only (drives REMX inclusion in the basket); bias toward geographic / execution diversification within a thesis (LYC + MP + REMX rather than LYC alone).

## M-nodes (sequence)

1. **`m.probe.scope`** — sharpened: vehicle split (LYC primary / MP secondary / REMX basket) within a single capital-Collapse decision; sizing as NAV % range with confidence; drawdown distribution as forward thesis-failure path; brittle-assumption identification mandatory.
2. **`m.probe.prior-art`** — methods.md (Kelly with haircut, drawdown bound, scenario stress, factor exposure), blind-spots.md (narrative seduction → boring-story test passes; tail neglect → fat-tailed China-policy distribution; implicit factor bets → REE is partially a China-trade-policy factor in disguise; crowding → structurally blind, haircut applied), strategies.md Type B criteria (all five hard gates passed at parent).
3. **`m.probe.world`** — graph snapshot 2026-05-08T09:00Z; FRED gap → haircut #9; EDGAR stub → haircut #10; flows missing → haircut #11; CBOE missing → option overlay deferred. Web_search supplements: China export-licence regime status, Lynas Kalgoorlie commissioning progress, MP Stage III timeline, US DoD strategic stockpile activity.
4. **`m.probe.edges`** — factor-coverage walk (per amendment 2026-05-08 factor-coverage-checklist):
   - **macro (rates / growth / inflation / fiscal)** — proxy via `macro.cfx_*` + `politics.fomc_rate_path_may2026`. Sleeve is mildly negatively exposed to a rate-cut-driven USD-weakening regime (positive for AUD-denom LYC translation, ambiguous for MP/REMX). Net: **macro-conditional but secondary**; haircut #9 applied. Status: probed.
   - **geographic (jurisdiction / sanctions / trade)** — load-bearing. Direct exposure to China export-control regime (assumption 4); Australia (LYC), USA (MP), Malaysia (LAMP plant). EU defense + auto demand supportive. **Verdict-flipping factor sits here.** Status: probed; load-bearing.
   - **regime (vol / liquidity / dispersion)** — `technicals.iwm` vol 21.22% suggests small-cap-mining tail beta is elevated but not extreme. Sleeve will exhibit higher realised vol than IWM (single-commodity small-cap miner cluster). Status: probed.
   - **correlation structure** — REE sleeve correlates positively with: gold (real assets bid), uranium / silver / copper (Type B cluster), small-cap miners (IWM beta). Correlates negatively with: long-duration Treasuries (S3 path), AI-mega-cap (S4 path). At portfolio level, sleeve adds a *China-policy* factor not currently held in book; partial offset to Type A US-mega-cap concentration noted in `strategy.portfolio-architecture.balance_assessment.concentrations`. Status: probed.
   - **flows (positioning / crowding / fund flows)** — **structurally blind**; haircut #11 applied. First-principles reasoning: REMX AUM small (~$300M historical range), institutional ownership of MP concentrated (Pentagon, Vanguard, JPM Asset Mgmt) but not crowded retail; LYC.AX has moderate Western fund holdings post-2022 dereg shift. Crowding probability low but unmeasurable. Status: probed with structural blindness flag.
   - **themes (narrative state / recognition stage)** — thesis is *named* in trade press but not priced (parent finding). Recognition stage = early. Status: probed; consistent with narrow-window gate.
   - **reflexivity (positioning ↔ price ↔ narrative)** — high. Recognition trigger is positively reflexive (first export-licence denial → narrative cascade → flows in → price → more analyst coverage → more flows). Symmetric on the downside (rollback → cascade out). Sleeve is at the *pre-cascade* point; sizing must respect that the realised volatility through the cascade may exceed the historical sample. Status: probed; load-bearing.
   - **liquidity / capacity** — LYC.AX > $5M USD/day, MP > $50M USD/day, REMX > $5M USD/day average. Sleeve at 2–4% NAV on a small/mid-NAV book is well within capacity; assumption #8 holds. Status: probed; not load-bearing.
5. **`m.reframe`** — not invoked; scope held. (One reframe candidate considered and rejected: "treat sleeve as call option on China policy regime change" — declined because the underlying physical demand thesis stands independent of policy change; option framing under-weights the demand floor. Logged for completeness.)
6. **`m.test.feasibility`** — capability OK (within seat); constraint OK (no mandate against single-commodity sleeves at < 5% NAV); budget OK (sleeve fits within Type B cluster cap discussed in proposed adjustment A6); data quality MEDIUM (three feed-gap haircuts applied). Feasible to size.
7. **`m.collapse`** — **propose for human gate**. Recommended: capital Collapse at sleeve = 2.5% NAV (range 1.5–4.0%) split LYC.AX 1.25% / MP 0.75% / REMX 0.50%. Do NOT execute Collapse from this section; status remains `open` until human gate.

## Prediction (convergent)

Distributions are sleeve-aggregate (LYC 50% / MP 30% / REMX 20% notional weights) unless noted. All numbers are priors with feed-gap haircuts already folded in; treat as ranking signal, not precise expectation.

### Expected return — 12 month

- **Shape:** strongly right-skewed bi-modal (modes near +5–10% drift case and +60–90% recognition-cascade case); fat left tail from policy-rollback path.
- **Mean:** +18%
- **SD:** ~38%
- **Quantiles:**
  - p05: −34%
  - p25: −10%
  - p50 (median): +9%
  - p75: +42%
  - p95: +88%
- **Probability of recognition trigger inside 12mo (assumption 7):** 0.55 → conditional return given trigger ≈ +55% (sleeve-aggregate); conditional return given no trigger ≈ +6% (drift case).

### Expected return — 24 month

- **Shape:** still right-skewed, modes diverging further; tails wider.
- **Mean:** +42%
- **SD:** ~62%
- **Quantiles:**
  - p05: −48%
  - p25: −12%
  - p50: +28%
  - p75: +85%
  - p95: +165%
- **Probability of recognition trigger inside 24mo (assumption 7 cumulative):** 0.78. Conditional given trigger ≈ +75%; conditional given no trigger ≈ −5% to +12%.

### Expected risk — drawdown distribution (forward, thesis-failure-conditional)

Drawdown defined as max peak-to-trough sleeve return over the 12-month window (NOT historical realised drawdown).

- **p50 drawdown:** −18% (typical realised path includes a 15–25% pullback even on the winning thesis as recognition cascade is rarely linear)
- **p90 drawdown:** −35%
- **p95 drawdown:** −42%
- **p99 drawdown:** −58%
- **Tail behaviour:** left tail is fatter than Gaussian. Joint failure of assumption 4 (China rollback) AND assumption 5 (Lynas execution miss) inside 12 months has probability ≈ 0.04 and conditional drawdown ≈ −60 to −70% sleeve-aggregate. Drawdown bound from parent (−40%) is the p93–p94 threshold; honoured at sleeve level.
- **Single-name worst-case drawdowns under thesis-failure path:** LYC.AX −55%, MP −45%, REMX −30%. REMX basket diversifies single-name execution risk meaningfully.

### E[R] / E[risk] ratio

- **Definition used:** E[R, 12mo] / E[|drawdown|, p90] = +18% / 35% = **0.51**
- **Alternative (24mo numerator):** +42% / 35% = **1.20**
- **Kelly-style heuristic check:** with edge ≈ 0.18 and variance ≈ 0.38², full-Kelly fraction ≈ edge / variance ≈ 1.25, but Kelly assumes the distribution is well-estimated. Per methods.md Kelly cautions (fat tails, edge over-estimation): apply 0.25× Kelly haircut + an additional 0.5× haircut for first-Type-B-on-this-instance (no calibration). Result: ≈ 0.16× of NAV ≈ 16% (gross Kelly with two haircuts). This is far above the drawdown-bounded sleeve sizing below; drawdown discipline binds before Kelly.
- **Verdict:** ratio is favourable on the 24mo horizon and roughly break-even on the 12mo horizon (consistent with recognition-window 6–15 months from parent).

### Sensitivity — the SINGLE brittle assumption

**Assumption #4 — China retains heavy-REE export controls through outcome window.**

- **Threshold value:** P(China rollback or material loosening inside 12 months) > **0.25**.
- At P(rollback) = 0.15 (current prior), E[R, 12mo] ≈ +18%, sleeve sizing 2.5% NAV stands.
- At P(rollback) = 0.25, sleeve E[R, 12mo] drops to ≈ +5%, p90 drawdown widens to −44%, ratio drops below 0.15 → cut sleeve to 1.0% NAV.
- At P(rollback) = 0.40, E[R, 12mo] turns negative ≈ −10%, p90 drawdown −50%; **verdict flips → no sleeve allocation**, monitor only.
- All other assumptions (1–3, 5–8) have wider tolerance bands and degrade the recommendation gradually rather than flipping it.

**Trip-wires (close monitoring required, not waiting for outcome window):**
- Public US-China heavy-REE de-escalation joint statement → assumption 4 stress test.
- Lynas Kalgoorlie production guidance withdrawal or LAMP licence non-renewal → assumption 5 stress test.
- A Western magnet maker announcing commercial Dy-free high-temp grain-boundary diffusion product at scale → assumption 2 stress test.

### Sizing recommendation

**Recommended sleeve size: 2.5% NAV (range 1.5–4.0%, confidence ~0.55).**

Vehicle split rationale:

| Vehicle | NAV % (mid) | Range | Rationale |
|---|---|---|---|
| LYC.AX | 1.25% | 0.75–2.00% | Primary. Only operating ex-China heavy-REE separator. NTA floor (~AUD 4 vs current ~AUD 8) bounds downside. Highest torque to recognition trigger. Single-name execution risk is the binding constraint. |
| MP | 0.75% | 0.50–1.25% | Secondary. US-listed, Pentagon-backed (DoD strategic capital), Stage III heavy-circuit 2026–2027 = second-mover ex-China. Lower torque pre-Stage-III but stronger jurisdictional + capital backing. Diversifies LYC execution + Australia jurisdiction risk. |
| REMX | 0.50% | 0.25–0.75% | Basket. Diversifies single-name execution risk and adds smaller miners + Chinese REE producers (which paradoxically benefit on a price-up regime even if export controls hold). Smallest weight because its construction includes Chinese-listed names that are tail-correlated to assumption 4 in the wrong direction. |

**Confidence:** ~0.55 sleeve recommendation; ~0.50 vehicle-split mid-points (could reasonably be LYC 1.50% / MP 0.50% / REMX 0.50% if single-name execution risk is judged lower).

**Cluster constraint (per architect proposed-adjustment A6).** This sleeve plus the uranium-sizing child plus the silver-sizing child plus grid-equipment-sizing child should be capped collectively at ≤ 8–10% NAV before cluster-correlation review. This sleeve at 2.5% leaves 5.5–7.5% for the rest of Type B.

**Do NOT collapse here.** Status remains `open` until human gate. Recommendation packaged for the architect / human principal at Collapse.

## Reconciliation (deep-dive vs adversarial probe)

The probe (`2026-05-08-rare-earths-adversarial-probe.md`) lands three attacks that the sizing section above did not adequately price. This section reconciles, re-rates sizing, and updates the recommendation. Status remains `open` — no Collapse.

### A. Assumption-by-assumption reconciliation

| Deep-dive assumption | Probe attack | Original framing | Reconciled framing |
|---|---|---|---|
| **#1 EV adoption (28–34M units, ≥80% NdFeB-traction)** | 1a unit-count + motor-architecture pivot (EESM, induction, SynRM) | "Failure → upside compresses materially" (non-flipping) | **Materially more brittle.** Three independent compounding haircuts (units 22–25M, NdFeB share ~55%, per-motor Dy thrifting via GBD) are not a tail — they are partly *already shipped* (Tesla Highland, BMW Gen-5 eDrive, Renault EESM). P(≥one of the three lands inside 24mo) ≈ 0.55–0.65; P(all three compound to "EV Dy demand ≈ flat") ≈ 0.25–0.35. Reclassify from "compresses upside" to **"compresses upside AND can flip the supply-bottleneck logic on its own."** |
| **#2 Dy/Tb intensity per motor** | 1a thrifting + 1b substitution-already-happening | "Substitution does not displace > 25% of high-temp motor demand inside 36 months" | **Falsified in spirit at the 36-month frame.** GBD thrifting and EESM/induction adoption are present-tense, not 2030+. The 25% threshold is plausibly already breached on *new platform specifications* (vs installed fleet). Tighten the assumption window: the 36-month protection is roughly 0.40, not the implied ≥ 0.70. |
| **#3 Defense / robotics / wind floor** | 1c defense Dy/Tb is small in absolute terms | Floor "≥ 30% of base-case Dy/Tb consumption by 2028" | **Floor magnitude likely overstated.** Defense Dy/Tb is single-digit % of EV-driven demand at the bull case; at the demand-collapse case the *ratio* rises but the *absolute floor* under realised-price premium remains small. Floor preserves a price *level* above ex-China, not a price *multiple*. Asymmetry-shrinking, not thesis-killing. |
| **#4 China export-control posture** | 2a non-stationary + 3a detente | P(rollback) = 0.15 | **Hold the prior at 0.15 for now.** Probe's 2a/3a arguments are credible but do not change the 12-month posterior much: the May 2026 graph does not show detente signals; election-cycle pressure is real but binary. Keep 0.15 with a wider trip-wire band. |
| **#5 Lynas execution** | 2b industry slippage base rate 18–30 months / 30–60% capex overrun | P(hit ≥60% nameplate by Q4 2026) ≈ 0.70 implied | **Lower posterior to 0.50–0.55.** Probe's industry base rate is well-sourced; deep-dive was using a Lynas-specific recency rather than the cross-name base rate. Effect is to widen p90 drawdown by ~5pp. |
| **#6 Refining bottleneck longevity** | (no direct attack) | Holds | Holds. |
| **#7 Recognition trigger inside 12mo (P=0.55)** | 3b 15-year recognition cycle + 4a/4b post-2024 crowding | "Recognition window open, narrow" | **Reframe required.** The honest claim is not "market hasn't recognised it" but "market re-prices this cyclically; we are betting we are early in *this* cycle, not in *the* cycle." The probe is right that REMX AUM tripling 2023→2025 means the Type B narrow-recognition gate is partly failing in real time. Two consequences: (i) the trigger probability stands at ~0.55 but the *unwind* probability inside the same window rises ~0.10–0.15 (recognition + unwind can both happen inside outcome window); (ii) gap-risk on exit is asymmetric (forced-passive sellers). |
| **#8 Liquidity** | (no direct attack) | Holds | Holds at sleeve scale. |

**Net on (A):** the demand-deduction attack does **not** flip the verdict by itself today, but it is materially stronger than the deep-dive's implicit weighting and **promotes a second independent kill mechanism** alongside #4. The deep-dive's framing of "single brittle assumption = #4" is wrong. There are now two brittle assumptions: **#4 (China rollback)** and **#1+#2 jointly (demand-deduction collapse)**. Recognition-window claim survives in a weakened form: "early in *this* cycle" rather than "pre-recognition," with explicit acknowledgment that REMX AUM trajectory shows the gate is closing.

### B. Joint kill probability and sizing implications

Two independent kill mechanisms, treated as approximately independent (China policy and OEM motor-architecture choices have weak coupling):

- P(rollback, 12mo) ≈ **0.15** (held from deep-dive)
- P(demand-collapse, 12–24mo) ≈ **0.30** (mid of probe's 0.25–0.35; note this is a slower mechanism, mostly resolves on 24mo not 12mo, but bleeds into 12mo via expectations / forward curves on Dy/Tb)
- P(joint kill, union) = 0.15 + 0.30 − (0.15 × 0.30) = **0.405** ≈ **0.40**

This is materially higher than the ~0.15–0.20 implicit in the deep-dive's drawdown distribution. Re-rating:

- **Drawdown distribution shifts left.** p90 drawdown from −35% → **−42 to −45%**; p95 from −42% → **−50%**. Drawdown bound at parent (−40% sleeve) is now p85, not p93.
- **E[R, 12mo] re-rated.** Mean +18% → **+8 to +11%** (kill-path conditional return ≈ −35%, weighted higher).
- **Ratio E[R] / E[|p90 drawdown|]:** drops from 0.51 → ≈ **0.20–0.25** on 12mo; ~0.85 on 24mo (was 1.20).
- **Kelly-style heuristic.** With re-rated edge ≈ 0.10 and variance ≈ 0.40², full-Kelly ≈ 0.62 of NAV; same two haircuts (0.25× × 0.5×) → ≈ 7.7% gross. Drawdown discipline still binds before Kelly, but the gap narrowed.

### C. Sizing decision

**Cut sleeve to 1.5% NAV (lower edge of original range), split LYC.AX 0.75% / MP 0.50% / REMX 0.25%.**

Reasoning:
- Probe's 30–50% cut from naive Kelly on bull asymmetry maps to roughly **1.25–1.75% NAV** at our drawdown-bounded sizing. 1.5% sits near mid of that band and at the lower edge of the deep-dive's stated 1.5–4.0% range — i.e., this is *not* a re-write of the range, it is a move within the stated range driven by the joint-kill re-rating.
- Holding 2.5% would mean ignoring a credible second independent kill mechanism. Cutting below 1.25% would over-react: the demand-collapse mechanism is slower (mostly 18–30mo), and partial confirmation of the deductive chain (any one of the three demand-side haircuts failing to materialise in primary OEM data) re-rates back upward.
- Vehicle split tilts marginally away from LYC concentration: deep-dive had 50/30/20; reconciliation moves to 50/33/17 within the cut sleeve (LYC 0.75 / MP 0.50 / REMX 0.25). Rationale: REMX share is *cut hardest* because (a) crowding attack 4a/4b lands hardest there (REMX AUM tripling is itself the crowding signal), and (b) probe's exit-liquidity concern is most acute for the basket vehicle on a forced-seller event.

**#1 ranking decision: DEMOTE pending evidence.** The probe's pre-condition for holding #1 ("deep-dive must engage these or it is not worth running") was not fully met — the deep-dive sized on the strength of #4 alone and did not produce the six evidence items the probe demanded. Recommended action: **provisionally demote rare-earths from #1 to #2 or #3 in the Type B ranking**, contingent on the evidence-gathering pass below. If items E1 and E2 (top of next subsection) come back supportive of the bull deductive chain, restore to #1. If they come back ambiguous or negative, hold demotion and consider further cut to 1.0% NAV.

**Confidence on the reconciled recommendation:** ~0.50 (down from 0.55). The cut to 1.5% is itself made under feed-gap and probe-uncertainty haircuts; do not treat the new midpoint as more precise than the old one.

### D. Top 3 evidence items by E[information value]

Pulled from the probe's six requested items, ranked by how much each item moves the joint kill probability if it resolves either way:

1. **E1 — Primary OEM EV motor-architecture mix, 2024 actual + 2027 announced.** By OEM and platform: NdFeB-PMSM vs EESM vs induction vs SynRM share. This single item directly tests assumptions #1 and #2 jointly and resolves the largest component of the demand-collapse probability. If NdFeB share holds ≥ 75% in announced 2027 platforms, P(demand-collapse) drops from 0.30 toward 0.15 and the sleeve restores to 2.0–2.5%. If NdFeB share is already ≤ 60% in announced 2027 platforms, P(demand-collapse) rises toward 0.40 and sleeve cuts to 1.0% with permanent demotion. **Highest E[VOI].**

2. **E2 — Per-motor Dy/Tb content trend with primary citations** (Tesla Highland teardown, BMW Gen-5 eDrive specs, OEM-disclosed GBD adoption). Tests the second leg of #2 independently of motor-mix. Even if NdFeB share holds, per-motor thrifting alone can compound to ≥ 30% Dy/Tb haircut. Pairs cleanly with E1 to triangulate the demand chain.

3. **E3 — REMX flow data and LYC.AX thematic-ownership estimate.** Tests assumption #7 (recognition window) directly and the crowding/forced-seller risk that materially widens the p90 drawdown. If thematic + passive ownership of LYC float is < 20%, gap-risk concern is reduced and the p90 drawdown bound is closer to the deep-dive's −35% than to the reconciled −45%. If > 30%, vehicle split tilts further away from LYC toward MP. Lower E[VOI] than E1/E2 but resolves a different axis (reflexivity / exit-liquidity rather than demand chain), so non-redundant.

The remaining three probe items (Lynas execution-track-record table, detente-scenario explicit modeling, recycling break-even price) are valuable but lower-leverage at current sizing: each one shifts E[R] or drawdown by a few pp without re-rating the joint kill probability.

### Reconciled outputs

- **Reconciled sleeve sizing:** **1.5% NAV** (range 1.0–2.0%, confidence 0.50). Split: LYC.AX 0.75% / MP 0.50% / REMX 0.25%.
- **Joint kill probability (12–24mo):** **≈ 0.40** (rollback ∪ demand-collapse).
- **Ranking recommendation:** **demote from #1 pending E1+E2 evidence**; restore conditional on supportive primary OEM data.
- **Trip-wires (added to those already listed):** OEM 2027 platform announcements showing EESM/induction adoption ≥ 35% of unit volume; any major Western magnet maker announcing commercial Dy-free high-temp GBD product (already in deep-dive trip-wires, raise to higher priority); REMX AUM continuing to rise > 50% from current level without a corresponding Dy/Tb realised-price ramp (signals crowding without underlying confirmation).

Status remains `open`. No Collapse from this section. Capital decision waits on E1+E2.

## Outcome

_Locked until 2027-05-09._

## Reflection

_Locked until outcome window._
