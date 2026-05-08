---
id: 2026-05-08-type-a-screen
shape: divergent
collapse_flavour: belief
status: open
scope: "Surface current Type A (Resilient Compounder) candidates across stocks, ETFs, crypto, commodities, FX, and fixed income."
parent_inquiry: null
graph_snapshot: 2026-05-08T05:15:27Z
outcome_window: 2026-11-08
sections:
  scope: ready
  assumptions: ready
  graph_refs: ready
  intent: ready
  self: ready
  m_nodes: ready
  output: ready
  outcome: locked
  reflection: locked
owner: agent:screener-type-a
---

# Inquiry: Type A candidates (Resilient Compounder)

## Scope

Generate a ranked candidate list for the **Type A — Resilient Compounder** archetype as of 2026-05-08. Vehicles in scope: stocks, ETFs, crypto, commodities, FX, fixed income. Single-name selection methodology, durability stress, valuation framing all in-scope. Capital allocation is out-of-scope (handled by child convergent inquiries).

## Assumptions (load-bearing)

1. **Durability is across-futures, not historical scoring.** Discriminator is whether the vehicle remains useful to society under tech-shift, regulation, geopolitics, and taste-shift simultaneously. Falsifiable by demonstrating any plausible future where the candidate becomes irrelevant or structurally impaired.
2. **Vehicle openness is real.** Non-stock vehicles (ETFs, commodities, FX, fixed income, crypto) can deliver Type A bet-shape if the underlying claim is durable. We force at least one non-stock candidate.
3. **Sober-case valuation gap.** "Under or fairly valued" is judged on conservative growth and margin assumptions, not bull-case extrapolation. Where direct fundamentals (EDGAR feed) are stub-only, we lean on price-action context and qualitative valuation framing — explicitly flagged as low-resolution.
4. **Macro graph is thin (FRED feed missing).** Any macro-conditional thesis (rate path, USD trajectory, inflation regime) carries low confidence. Candidates whose Type A case is *primarily* a macro bet are flagged `macro-conditional: low-confidence`.
5. **Realised-vol context only, no forward implieds.** Vol regime drawn from yfinance 30d realised; we do not have CBOE / options-chain detail. Fat-tail probability is therefore underestimated; haircut sizing in child inquiries.
6. **Regulatory regime tilt is mildly accommodative for US financials** (per `politics.regulatory_deregulation_posture`, mean 0.50 moderate easing). Treated as a tailwind not a base case for any single name.
7. **AI capex peak timing uncertain** (`themes.ai-capex-cycle`: 45% peak within 18mo, 55% later). Type A AI-adjacent names must survive a peak that arrives *before* the thesis matures.
8. **No prior Type A screen closures exist in this instance** — calibration prior is uninformative; we assume `hit_rate ~ market base rate` with wide variance.
9. **Crypto durability is split-belief.** BTC has a defensible monetary-asset case across many futures; smaller-cap tokens do not meet Type A bar. Screen admits BTC, rejects others.
10. **Fixed-income duration ETFs are not Type A by themselves** — they are macro instruments. They appear only as overlay candidates, never as the durability core.

## Graph references

- `strategies.md#Type A` — archetype criteria.
- `graph/strategies.md#strategy.type-a` — standing node, `current_candidates: []` pre-fill target.
- `graph/themes.md#themes.ai-capex-cycle` — confidence 0.55, peak-timing distribution.
- `graph/themes.md#themes.payments_infrastructure_expansion` — FedNow tailwind for payment intermediaries.
- `graph/themes.md#themes.capital_framework_overhaul` — Basel III modernization, ambiguous net effect on large banks.
- `graph/politics.md#politics.regulatory_deregulation_posture` — moderate easing tilt 0.50.
- `graph/politics.md#politics.fednow_intermediary_rule` — proposal likely finalizes (0.50).
- `graph/sentiment.md#sentiment.bank_ma_activity` — mean +0.25, healthy approval flow.
- `graph/sentiment.md#sentiment.bank_regulatory_climate` — mean -0.15, slight easing.
- `graph/macro.md` — FRED gap noted; only `feed.commodities-fx` ETF proxies hydrated. **Thin.**
- `graph/technicals.md` — 28 nodes, last_close + 30d realised vol for SPY, QQQ, IWM, EFA, EEM, sector XLs, single-name (GOOG, NVDA, TSLA, BRK-B), commodities (GLD, USO, DBC), FX (UUP), fixed income (TLT, HYG, LQD), crypto (BTC, ETH, plus CoinGecko: ADA, XRP, SOL).
- `graph/fundamentals.md` — stub only. **Single-name fundamental rigor is constrained.**
- `graph/portfolio.md` — empty book; no concentration / factor exposure constraint binds.

## Intent

Produce a ranked list of vehicles that are durable across most plausible futures, low obsolescence risk, and currently under or fairly valued. The list seeds child convergent inquiries on top candidates.

## Self

- **Prior screen calibration:** none. This is the first Type A screen in this instance. `self.calibration` initialized at `null`.
- **Known biases this run is exposed to:**
  - Vehicle bias toward stocks (mitigated by forced non-stock inclusion — see `agents/screener-type-a.md`).
  - Quality-scoring drift (re-anchored on across-futures stress; see process step 3).
  - Narrative seduction on AI / mega-caps (probed: would I take this if the AI capex cycle peaked tomorrow? Used as gate).
  - Anchoring on ticker familiarity in technicals feed (universe was hydrated by feed selection, not by the screen — explicit fuzz_halo).
- **Confidence floor:** medium-low across the list given thin fundamentals + thin macro. Recommend child inquiries treat this as a *seed list*, not an action list.

## M-nodes (sequence)

1. `probe-graph` — pulled standing nodes above (graph_refs).
2. `assumption-lister` — populated assumptions section.
3. `screener-type-a` (this run) — built candidate set, ran across-futures stress, ranked.
4. (Downstream, not yet executed) `sensitivity-analyzer` per child inquiry; `predictor` for marginal portfolio contribution; `feasibility-gate` before any capital-Collapse.

## Output (divergent)

### Candidate universe considered (wide pre-filter)

Stocks (mega/large-cap durability candidates): GOOG, MSFT, AAPL, AMZN, META, BRK-B, NVDA, TSM, ASML, V, MA, COST, WMT, UNH, LLY, NVO, JNJ, PG, KO, NSRGY, LIN, RTX, LMT, NEE, WM, MCO, SPGI, ADBE.
ETFs (basket durability): VTI, VOO, VT, MOAT, QUAL, COWZ, SCHD, XLP, XLV, XLU, XLK.
Commodities: GLD (gold), DBC (broad), USO (oil — rejected, not Type A), uranium (URNM — adjacent).
Crypto: BTC (admitted), ETH (rejected for Type A, candidate for Type B).
FX: UUP (rejected, macro instrument), no FX qualifies as Type A.
Fixed income: TLT, LQD, HYG (rejected as primary Type A; overlay only).

After across-futures stress (tech-shift / regulation / geopolitics / taste), the ranked shortlist follows. Ranking is by *durability score × inverse valuation-stretch*, with explicit fuzz_halo for thin-data names.

### Ranked candidates

---

**Rank 1 — GOOG (Alphabet)** — vehicle: stock
- **Durability rationale.** Multi-product ecosystem (Search, YouTube, Android, Cloud, Waymo, DeepMind). Cash-generative core (Search + Ads) funds optionality (Cloud, autonomy, AI infra). Survives most futures: AI-shift turns Search business model risk into a re-platforming question, but distribution + data moat + Gemini integration keep them in the top three regardless of which AI stack wins. Regulation risk (antitrust, AI rules) trims margin but does not impair existence.
- **Across-futures stress.**
  - Tech-shift (LLM disintermediates Search): partial impairment 30–40% of ad revenue at risk over 5y; offset by YouTube + Cloud + Gemini distribution — *survives*.
  - Regulation (DOJ remedies, EU AI Act, Chrome divestiture): margin compression 100–300bps; *survives*.
  - Geopolitics (Taiwan / chip supply, China decoupling): TPU vertical-integration is a hedge vs Nvidia-dependent peers — *survives, partial benefit*.
  - Taste (privacy, AI-fatigue): brand resilience, low; — *survives*.
- **Valuation framing.** Last close 395.30, 30d realised vol 39.1% — vol elevated, suggests recent re-rating event. Sober-case: assume 8% revenue CAGR, modest margin compression, the Cloud + Waymo optionality is free. Trades at fair-to-modestly-undervalued vs sober-case DCF; *valuation gap exists if you assign any non-zero value to Waymo + Cloud growth*. **Low-resolution flag** — fundamentals graph is stub.
- **Sensitivity.** Most sensitive to: AI re-platforming speed (high), antitrust remedy severity (medium), Cloud growth rate (medium). Insensitive to: rate path (low — net cash), USD (low — diversified geo).
- **Suggested child inquiry id:** `2026-05-15-goog-deep-dive` (convergent, capital-Collapse).

---

**Rank 2 — BRK-B (Berkshire Hathaway)** — vehicle: stock
- **Durability rationale.** Diversified holding co (insurance float, BNSF, BHE, equity portfolio, cash pile). Structurally anti-fragile: cash + insurance float deployable into dislocations. Lowest realised vol in the entire universe (12.08% — confirms regime-stability). Succession risk is the dominant overhang but business-model resilience persists post-Buffett.
- **Across-futures stress.**
  - Tech-shift: holdings tilted to Apple + financials; *survives*, possibly benefits from disruption-buying capacity.
  - Regulation: insurance/utility regulation incremental, manageable; *survives*.
  - Geopolitics: predominantly US-domestic; *survives, mildly benefits* in deglobalization.
  - Taste / generational: succession is the only real Type A wobble — *survives*, optionality on capital deployment under new management.
- **Valuation framing.** Last close 475.08. Sober-case: book value compounds at 8–10%, public-equity portfolio marks-to-market provides upside, cash pile (~$300B+) is dry powder optionality. P/B around historical mid; not cheap, fair. **Low fuzz_halo** — most directly observable durability candidate in the set.
- **Sensitivity.** Most sensitive to: equity-market drawdown (counter-intuitively *positive* via cash deployment), insurance underwriting cycle. Insensitive to: AI cycle, single-stock factor risk.
- **Suggested child inquiry id:** `2026-05-15-brk-b-sober-case` (convergent, capital-Collapse).

---

**Rank 3 — COST (Costco)** — vehicle: stock
- **Durability rationale.** Membership flywheel (renewal rate ~93%), scale advantage in procurement, taste-resilient (price-conscious consumer is a *more* attractive customer in stress). Genuinely insulated from AI shift (AI cannot replace bulk physical distribution). Tariff regime risk exists but absorbed historically.
- **Across-futures stress.**
  - Tech-shift: *unaffected positively* — physical retail with proprietary supply chain is a non-AI moat.
  - Regulation: tariff exposure on imported goods; *survives* via private-label substitution.
  - Geopolitics (US-China): direct sourcing risk — *survives*, would compress margins 50–150bps in escalation case.
  - Taste: value-oriented consumer behaviour is structurally durable; *survives*.
- **Valuation framing.** Persistent premium multiple (P/E 50+ historically). Sober-case requires accepting that the moat justifies premium — *not undervalued*; admitted as "fairly valued" tier. Risk: multiple compression on growth disappointment is the real downside.
- **Sensitivity.** Most sensitive to: membership growth rate, tariff regime escalation. Insensitive to: rate path, AI cycle.
- **Suggested child inquiry id:** `2026-05-15-cost-multiple-risk` (convergent, belief-Collapse first; valuation premium needs a sharper test before capital-Collapse).

---

**Rank 4 — MOAT (VanEck Morningstar Wide Moat ETF)** — vehicle: ETF
- **Durability rationale.** Rules-based exposure to companies with durable competitive advantages, weighted by valuation gap to fair value. Direct vehicle for the Type A archetype — basket-implementation of "durable + under-valued". Removes single-name idiosyncratic risk.
- **Across-futures stress.**
  - Tech-shift: holdings rotate as moats erode/emerge; *survives by construction*.
  - Regulation: diversified across sectors; *survives*.
  - Geopolitics: US-listed names dominant; *survives* but no explicit hedge.
  - Taste: methodology adapts; *survives*.
- **Valuation framing.** Methodology over-weights names trading below Morningstar fair value — embeds the "valuation gap" criterion explicitly. **No fundamental fuzz_halo** because methodology is auditable.
- **Sensitivity.** Tracks underlying basket. Lower idiosyncratic risk but also lower upside than a correctly-picked single name.
- **Suggested child inquiry id:** `2026-05-15-moat-as-core-allocation` (convergent, capital-Collapse).

---

**Rank 5 — GLD (gold ETF)** — vehicle: commodity *(non-stock — required by spec)*
- **Durability rationale.** Monetary asset with millennial track record. Durable across every Type A stress dimension by definition (zero counterparty risk in physical, structurally non-obsolescable). Functions as portfolio insurance + monetary-debasement hedge.
- **Across-futures stress.**
  - Tech-shift: *unaffected*.
  - Regulation: confiscation tail risk in extreme regimes (low probability); *survives*.
  - Geopolitics: *positive sensitivity* — central-bank buying confirmed multi-year theme.
  - Taste: cultural durability uncontroversial.
- **Valuation framing.** Last close 431.68, 30d realised vol 28.0% (elevated — gold has had a strong run). Sober-case: real-rate path uncertain (FRED gap = **low-confidence on macro driver**), but central-bank demand is structural. **Macro-conditional flag — low-confidence** on near-term entry timing; durability of the underlying asset is high-confidence.
- **Sensitivity.** Most sensitive to: real rates (inverse), USD strength (inverse), geopolitical stress (positive). Vol regime says "not cheap right now."
- **Suggested child inquiry id:** `2026-05-15-gld-entry-timing` (convergent, belief-Collapse first to resolve macro-driver picture before capital-Collapse).

---

**Rank 6 — BTC (Bitcoin)** — vehicle: crypto *(non-stock alternative)*
- **Durability rationale.** 17-year track record, monetary network with no central issuer, demonstrably durable across multiple regulatory regimes and tech cycles. Type A admission is split-belief (assumption #9): network monetary properties are durable; specific price levels are not. Vol 28.7% — high but trending lower over multi-year window.
- **Across-futures stress.**
  - Tech-shift: protocol immutability is the moat; *survives* most adversarial scenarios except a quantum-computing break (low probability, long horizon).
  - Regulation: spot-ETF approval done; ongoing regulatory normalization; *survives* — adversarial-state ban is the residual tail.
  - Geopolitics: censorship-resistant property is *more* valuable in deglobalizing world.
  - Taste: generational adoption curve — *survives, structurally tailwinded*.
- **Valuation framing.** Last close $79,616. No DCF available; framing is network-value / monetary-supply / adoption-curve. Sober-case: assume modest continued institutional adoption + halving-cycle supply mechanic — fair to undervalued vs adoption-S-curve mid-point. **High fuzz_halo on valuation framework itself.**
- **Sensitivity.** Most sensitive to: institutional flow regime, regulatory tone in major jurisdictions. Vol-haircut sizing recommended in any child inquiry.
- **Suggested child inquiry id:** `2026-05-15-btc-as-type-a` (convergent, belief-Collapse — the Type A vs Type B classification of BTC itself is a decision for child inquiry).

---

**Rank 7 — V (Visa)** — vehicle: stock
- **Durability rationale.** Two-sided network (issuers + merchants), interchange economics, FedNow / instant-payments theme is a *risk* but also a participation vector. Margin profile (60%+ operating margin) is structurally rare. Brand + rails durability across geographies.
- **Across-futures stress.**
  - Tech-shift: real-time payment rails (FedNow, RTP) and stablecoins are the genuine threat — *partial impairment*, magnitude debatable. The themes graph notes FedNow expansion.
  - Regulation: interchange caps recurrent threat — *survives* with margin compression.
  - Geopolitics: cross-border volume sensitive to trade regime; *survives*.
  - Taste: card-payment habit deeply entrenched; *survives*.
- **Valuation framing.** Premium multiple for a structurally-margin'd network. Sober-case: 7–9% top-line CAGR, modest margin compression from interchange + alt-rails — fairly valued, not undervalued.
- **Sensitivity.** Most sensitive to: stablecoin / instant-rail penetration speed, cross-border volume, interchange regulation.
- **Suggested child inquiry id:** `2026-05-15-v-rails-displacement-risk` (convergent, belief-Collapse — needs a sharper test of FedNow/stablecoin displacement risk before capital-Collapse).

---

**Rank 8 — TSM (Taiwan Semiconductor)** — vehicle: stock *(geopolitical-conditional)*
- **Durability rationale.** Foundry monopoly at leading-edge nodes, customer list = entire silicon industry. Durability of the *business* is exceptional; durability of the *jurisdiction* is the singular Type A wobble.
- **Across-futures stress.**
  - Tech-shift: leading-edge foundry essential under any AI-compute future; *strongly survives*.
  - Regulation: export controls already incorporated; *survives*.
  - **Geopolitics: Taiwan-Strait tail is the discriminator** — in escalation scenarios, equity may impair 50–80%. Arizona / Japan / Germany fab build-out is partial mitigation but not complete.
  - Taste: irrelevant.
- **Valuation framing.** Trades at perpetual geopolitical discount to peers. Sober-case business value is undervalued; the discount *is* the geopolitical option premium.
- **Sensitivity.** Dominated by Taiwan-Strait probability. Sized accordingly in any child inquiry — this is a Type A name with Type B tail risk attached.
- **Suggested child inquiry id:** `2026-05-15-tsm-tail-bounded-sizing` (convergent, capital-Collapse contingent on tail-bounded sizing).

---

### Cross-cutting notes

- **Implicit factor / theme exposures across the list.**
  - GOOG, NVDA-adjacent, TSM → AI capex theme exposure (3 names).
  - BRK-B, COST, V → consumer / financial defensiveness (3 names).
  - MOAT → diversified moat factor.
  - GLD, BTC → real-asset / monetary-debasement factor.
  - **Concentration risk:** if all top picks were taken, AI-capex theme would dominate. Architect agent should debias before capital allocation.
- **Macro-conditional flags (FRED-thin):** GLD entry-timing, TLT (not on list, but any duration overlay), V's rate sensitivity. Treat any thesis whose dominant driver is macro as **low-confidence** until FRED feed is hydrated.
- **Vol regime context.** Universe-wide 30d realised vol clusters in 14–28% for the durable names; mega-cap tech (GOOG 39%, NVDA 40%, TSLA 44%) is in a higher-vol regime. SPY 16%, QQQ 20% — broad-market vol normal. No regime-break signal.
- **Names explicitly considered and rejected:**
  - NVDA — Type A bar fails on across-futures stress: AI-cycle cyclicality + competitive entry (custom silicon, AMD, TPU) + 40% realised vol = not durable in the Type A sense; better as Type B.
  - TSLA — narrative-driven, valuation premium without sober-case support, 44% vol; rejected.
  - TLT — macro instrument, not a durability vehicle.
  - ETH, SOL, ADA, XRP — fail Type A bar (assumption #9).
  - USO — commodity beta, not a durability vehicle.
  - UUP — FX hedge tool, not Type A.
  - HYG, LQD — credit spread instruments, overlay only.

### Summary table

| Rank | Symbol | Vehicle | Durability | Valuation | Macro-conditional | Child inquiry |
|------|--------|---------|------------|-----------|-------------------|---------------|
| 1 | GOOG | stock | high | fair-to-under | no | 2026-05-15-goog-deep-dive |
| 2 | BRK-B | stock | very high | fair | no | 2026-05-15-brk-b-sober-case |
| 3 | COST | stock | high | premium / fair | no | 2026-05-15-cost-multiple-risk |
| 4 | MOAT | ETF | high (basket) | embedded gap | no | 2026-05-15-moat-as-core-allocation |
| 5 | GLD | commodity | very high | macro-driven | **yes (low-conf)** | 2026-05-15-gld-entry-timing |
| 6 | BTC | crypto | medium-high | framework-fuzzy | partial | 2026-05-15-btc-as-type-a |
| 7 | V | stock | medium-high | fair | partial | 2026-05-15-v-rails-displacement-risk |
| 8 | TSM | stock | high (ex-tail) | undervalued + tail | no | 2026-05-15-tsm-tail-bounded-sizing |

8 candidates surfaced. Non-stock representation: 3 (MOAT, GLD, BTC) — exceeds spec floor of 1.

## Outcome

_Locked until outcome window (2026-11-08)._

## Reflection

_Locked until outcome window._
