---
id: 2026-05-08-portfolio-architecture
shape: convergent
collapse_flavour: belief
status: open
scope: "Architect (or evaluate) the current portfolio against the open considerations menu in strategies.md, maximising E[R]/E[risk] across plausible futures."
parent_inquiry: null
graph_snapshot: "2026-05-08T05:30Z (yfinance + crypto + commodities-fx + news-summarizer; FRED gap; EDGAR stub; broker feed not wired)"
outcome_window: 2026-08-08
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
owner: agent:portfolio-architect
---

# Inquiry: Portfolio architecture as of 2026-05-08

## Scope

Use the open-considerations menu in `strategies.md` (game-theoretic, macro regime, scenario distribution, correlation structure, liquidity, mandate, time-horizon mix, tail-hedge availability, reflexivity, ...) to architect — or evaluate the current — portfolio for maximising E[R]/E[risk]. Surface holes. Propose adjustments. Stay creative and critical; do not default to a single framing.

In scope: framing selection, scenario set, coverage assessment, hole identification, adjustment proposals.
Out of scope: execution sizing of individual capital trades (handled by child convergent capital-flavour inquiries on accepted adjustments).

## Assumptions (load-bearing)

Note: per proposed amendment `2026-05-08-feed-gap-promotes-to-assumption`, feed gaps are promoted from silent flags into named load-bearing assumptions with explicit confidence haircuts.

1. **Type A and Type B candidate pools as of 2026-05-08T05:30Z are usable as the architect's working universe.** They are screen output, not commitments; current portfolio book may also include legacy positions (per `2026-05-08-tech-sizing` snapshot: 18% tech sleeve, factor exposure HML −0.4, MKT +1.1, MOM +0.3). Falsifiable by a refreshed screen run with materially different rankings.
2. **FRED feed missing — macro probe is approximated by ETF/FX proxies (TLT, HYG, LQD, UUP, GLD, DBC, USO) plus news-summarizer FOMC inferences.** Confidence haircut on any macro-conditional claim: −30%. Resolves when FRED hydrates. (Promoted from feed gap.)
3. **EDGAR feed stub-only — single-name fundamentals are not directly readable.** Valuation framing is qualitative + price-action. Confidence haircut on single-name valuation: −20%. Resolves when EDGAR hydrates. (Promoted from feed gap.)
4. **No flows / positioning / crowding feed exists in this instance.** The `flows.tech-positioning` reference in the tech-sizing inquiry was a snapshot value carried in by hand; there is no live source. Confidence haircut on any reflexivity / crowding-driven scenario: −25%. Resolves when a positioning feed (prime-broker proxy, CFTC COT, ETF-flow tracker, or option-skew) is registered. (Promoted from feed gap.)
5. **No live broker feed — `portfolio.current` is partly hand-snapshotted from the sibling tech-sizing inquiry.** The book outside the tech sleeve is unknown to this inquiry. Confidence haircut on coverage and concentration claims: −15%. Resolves when broker feed is wired up.
6. **Outcome window 3 months (to 2026-08-08).** Type A theses are years-long; Type B theses are 3–18 months. The architecture this inquiry blesses is judged on whether the book *moved correctly* over 3 months, not whether theses *played out* over 3 months.
7. **Reflexivity edges are sparse but real.** The standing graph has only the example `edge.crowding-to-drawdown` marked reflexive. We treat that as illustrative — the architect must reason about reflexivity from first principles (not skip it because there is one edge in the graph).
8. **Mandate constraints are loose.** Per tech-sizing assumption 4, sector concentration up to 30% is permissible. No leverage, no shorting, no derivatives explicitly forbidden but none currently used. Single-name caps: not formalised.
9. **Vol regime is mid-elevated.** SPY 30d realised ≈16%, QQQ ≈20%, single-name mega-cap tech 39–44% — implies dispersion is up. Forward implieds unknown (no CBOE feed) so fat-tail probability is structurally underestimated.
10. **The user is the principal at Collapse.** This inquiry's belief-Collapse will be gated by the user; the architect surfaces options, does not decide.

## Graph references

Pulled from snapshot 2026-05-08T05:30Z:

- `graph/strategies.md#strategy.type-a.current_candidates` — 8 entries (GOOG, BRK-B, COST, MOAT, GLD, BTC, V, TSM); top 3 GOOG, BRK-B, COST. Provenance: `inquiry.2026-05-08-type-a-screen`.
- `graph/strategies.md#strategy.type-b.current_candidates` — 5 entries (heavy rare earths ex-China, uranium/HALEU, silver, grid transformer/HV interconnect, product tankers); top 3 the first three. Provenance: `inquiry.2026-05-08-type-b-screen`.
- `graph/strategies.md#strategy.type-b.rejected_in_screen` — copper, GLP-1 mfg, defense primes, BTC at drawdown, TLT, community-bank takeouts. Useful as negative space for hole-checking.
- `inquiries/2026-05-08-tech-sizing.md` — `portfolio.current` snapshot (18% tech sleeve, factor exposure HML −0.4, MKT +1.1, MOM +0.3) and `edges.crowding-to-drawdown` reference.
- `graph/themes.md` — `themes.ai-capex-cycle` (peak-timing distribution: 0.45/0.35/0.20); `themes.payments_infrastructure_expansion` (FedNow); `themes.capital_framework_overhaul` (Basel III); `themes.enforcement_normalization`.
- `graph/politics.md` — `politics.fomc_rate_path_may2026` (hold_through_june 0.55, cut_25 0.20, hold_then_cut_h2 0.15); `politics.regulatory_deregulation_posture` (moderate_easing 0.50); `politics.fednow_intermediary_rule`.
- `graph/macro.md` — only commodities-fx ETF proxies (GLD 431.68, USO 134.97, DBC 30.25, UUP 27.41, TLT 85.65, HYG 79.86, LQD 108.74, EURUSD 1.174, USDJPY 156.87, GBPUSD 1.357). FRED gap.
- `graph/edges.md` — `edge.crowding-to-drawdown` (illustrative, only reflexive edge currently in graph).
- `graph/portfolio.md` — schema only; live state empty pending broker feed wiring.

## Intent

Output a structured architecture proposal: framings used, scenario set with explicit probabilities, per-scenario book performance against the candidate pool + portfolio.current, coverage assessment, holes surfaced, proposed adjustments with rationale. Update `graph/strategies.md` → `strategy.portfolio-architecture` with the snapshot. Confidence: 0.55 on the architecture proposal as a whole (haircut from FRED + EDGAR + flows gaps). Higher confidence on hole identification (~0.7) than on probability weights (~0.45).

## Self

- `self.capability` — architect agent can pull framings situationally, build scenarios, surface holes, propose adjustments. Cannot execute trades, cannot decide. Cannot generate single-name DCFs (EDGAR stub).
- `self.calibration` — first portfolio-architecture inquiry in this instance. No closed prior. Calibration prior is uninformative; treat all probability weights as preliminary, ±10pp band each.
- `self.taste` — biased toward (a) explicit hole-surfacing over polished allocation grids, (b) reflexivity / crowding probes, (c) tail-hedge cheapness checks, (d) treating "fairly valued + premium-multiple" as a hidden short-vol bet. Counter-bias: I tend to over-weight tail scenarios and under-weight base-case carry.
- **Bias probes for this run.**
  - Narrative seduction: would I propose silver / uranium / REE if the AI capex story were boring? Probed — the supply-bottleneck arguments are vehicle-agnostic and pre-date the AI narrative; survives.
  - Anchoring on Type A/Type B framing: am I treating the menu as exhaustive? No — game-theoretic flow framing forces me to consider vehicles outside both archetypes (e.g. cash, vol-as-asset, FX).
  - Confirmation: have I read the rejected list (Type B screen) as adversarial input? Yes — copper rejection on "50–70% recognised" is a candidate hole flag (might be missing convex copper exposure).

## M-nodes (sequence)

1. `m.probe.scope` — sharpened from "evaluate portfolio" to "assess whether candidate pool + portfolio.current covers the scenario distribution, given today's gaps". The gap-promoted assumptions reframe what "evaluate" can mean under thin macro / fundamentals / flows.
2. `m.probe.prior-art` — consulted `strategies.md` open-considerations menu; `methods.md` (factor exposure, scenario stress, tail-hedge availability); `blind-spots.md` (implicit factor bets, crowding, tail neglect, narrative seduction).
3. `m.probe.world` — pulled candidate pools + portfolio.current snapshot + macro/themes/politics nodes; confirmed FRED, EDGAR, flows, broker feeds are gapped (assumptions 2–5).
4. `m.probe.edges` — applied the proposed `factor-coverage-checklist` (amendment `2026-05-08-factor-coverage-checklist`). Per-factor:
   - **macro** — probed via news-summarizer FOMC distribution + ETF proxies. Confidence-haircut. *Probed (low-resolution).*
   - **geographic** — probed via Type A TSM Taiwan-tail and Type B REE ex-China bottleneck; US-domestic concentration explicit (BRK-B, COST). *Probed.*
   - **regime (vol/dispersion)** — probed via 30d realised vols across universe (mega-cap tech 39–44%, broad market 16–20%). *Probed.*
   - **correlation** — probed by mapping each candidate to factor exposure direction (see Output). Real correlation matrix unavailable. *Probed (qualitative only).*
   - **flows / crowding** — *N/A with reason: no flows feed registered.* Promoted to assumption 4. Surfaced as hole.
   - **themes** — pulled `themes.ai-capex-cycle`, FedNow, Basel III, enforcement normalization. *Probed.*
   - **reflexivity** — probed via `edge.crowding-to-drawdown` and first-principles on Type B recognition windows (positioning ↔ price ↔ narrative on REE, uranium, silver). *Probed.*
   - **liquidity / capacity** — probed qualitatively: Type A names all large-cap; Type B Lynas / Centrus / silver miners are small/mid-cap, sized accordingly per Type B screen assumption 8. *Probed.*
5. `m.reframe` — reframed from "find the right allocation" to "identify the holes the candidate pool + portfolio leaves uncovered, and propose convergent capital-flavour child inquiries to close each".
6. `m.test.feasibility` — capability ✓ (architect surfaces options); constraint ✓ (no allocations committed here); data-quality flagged in assumptions; budget N/A (belief-Collapse, not capital).
7. `m.collapse` — belief-Collapse pending user gate. Output written; status remains `open` until user collapses.

## Output (convergent)

### 1. Framings used (from open-considerations menu)

Pulled situationally. Five earned their keep; three are partial / data-blocked.

- **Scenario distribution** *(load-bearing)* — relevant because the candidate pool spans macro-conditional and macro-insensitive vehicles; we need explicit scenarios to see which subset is bet on.
- **Macro regime** *(low-resolution)* — relevant because Type B candidates 4–5 (grid, tankers) and Type A GLD are macro-conditional; FRED gap caps confidence (assumption 2).
- **Game-theoretic flow** *(load-bearing)* — relevant because most-probable-future analysis ignores where capital *has to go*; rate-cut path and dereg posture point to specific flow recipients (banks, duration, real assets).
- **Correlation structure** *(load-bearing)* — relevant because the Type A pool is heavy on US-mega-cap (correlated under stress) and Type B pool is heavy on commodities/industrials (correlated under reflation); cross-bucket correlation in a recession is the discriminator.
- **Tail-hedge availability** *(load-bearing)* — relevant because the candidate pool has *implicit* tail hedges (GLD, BTC, BRK-B cash) but no *explicit* tail hedges (puts, vol, OTM hedges); we cannot afford to skip this when CBOE feed is missing (assumption 9).
- **Reflexivity** *(load-bearing)* — relevant because Type B recognition-window theses (REE, uranium, silver) are explicitly reflexive: positioning ↔ price ↔ recognition. Cross-checked vs `edge.crowding-to-drawdown` as the only reflexive edge currently in the graph.
- **Mandate / time-horizon mix** *(partial)* — relevant because Type A is multi-year, Type B is 3–18 months; the book needs a stated mix even if mandate is loose. Used qualitatively.
- **Liquidity / capacity** *(partial)* — relevant for Type B small/mid-cap miners. Already flagged in Type B screen assumption 8; carried forward without re-derivation.

### 2. Scenario set

Open-ended; not limited to base/bull/bear/tail. Probabilities sum to 1.00 and carry ±10pp confidence band (self.calibration). Per scenario: P, what wins, what loses, where flows accumulate.

| ID | Scenario | P | What wins (from pool + book) | What loses | Where flows go |
|----|----------|---|------------------------------|------------|----------------|
| S1 | **Soft landing + dereg + AI capex extends** | 0.22 | GOOG, V, MOAT, COST, grid (4), BRK-B | tankers (5), GLD entry-timing | growth megacap, regional banks, infra industrials, credit spreads tighten (HYG↑) |
| S2 | **Stagflation lite (sticky inflation, growth weak)** | 0.18 | GLD, BTC, silver (3), REE (1), uranium (2), BRK-B (cash) | duration (TLT not in book), V (consumer), COST margin | real assets, gold, commodities; equity multiples compress |
| S3 | **Recession + Fed cuts faster than priced** | 0.14 | BRK-B (cash deploys), TLT (not in book), MOAT (defensives rotate up), GLD | tankers, grid, REE/silver/uranium (all demand-cyclical), V, GOOG (ad cycle) | duration, defensives, gold; cyclicals dump |
| S4 | **AI capex peak inside 18 months** | 0.20 | BRK-B, COST, V, GLD, silver (mixed) | grid (4), uranium (2), GOOG (multiple compresses), TSM (sentiment) | defensives + value rotation; semis derate; power-thesis names hit hard |
| S5 | **Geopolitical escalation (Taiwan / ME / sanctions widen)** | 0.10 | GLD, BTC, REE (1), uranium (2), tankers (5), defense (not in pool) | TSM (50–80% impair), GOOG (China/cloud), V (cross-border), broad equity | safe havens, energy, commodities, defense; risk assets dump |
| S6 | **Reflation surprise (growth re-accelerates, inflation re-accelerates)** | 0.08 | silver (3), REE (1), uranium (2), grid (4), tankers (5), TSM | TLT-equivalents, GLD (real-rate up), V multiple | cyclicals, commodities, value; growth derates |
| S7 | **Status quo drift (none of the above clearly)** | 0.06 | MOAT, BRK-B, COST, V — slow compounders | Type B (no recognition trigger fires) | distribution flat; carry-trades win |
| S8 | **Tail / fat-left (credit event, USD funding shock, sovereign stress)** | 0.02 | GLD, BTC partial, BRK-B cash | everything risk; Type B small-caps gap down 30–50% | dollars and gold; everything else dumps |

Sum = 1.00. **Note** — S1+S4 jointly = 0.42 (the AI-capex axis in both directions). S2+S6 = 0.26 (commodities-friendly, real-asset friendly axis). S3+S5+S8 = 0.26 (risk-off cluster). Calibration band ±10pp per scenario.

### 3. Coverage assessment

**Where the candidate pool + portfolio.current is concentrated.**

- **AI-capex factor:** GOOG, TSM, V (partial), grid (4), uranium (2 — power-thesis indirect), silver (3 — partial). 5–6 of 13 candidates carry AI-capex exposure. The portfolio's existing 18% tech sleeve adds to this. *This is the dominant implicit factor bet.*
- **US-mega-cap factor (MKT +1.1 already from book):** GOOG, BRK-B, COST, V, MOAT — 5 of 8 Type A candidates. Plus the existing tech sleeve. Adding any 2–3 Type A names raises MKT exposure further.
- **Real-asset / monetary-debasement factor:** GLD, BTC, silver (3) — 3 candidates. Decent coverage *if* sized; under-sized in current book (book has zero per snapshot).
- **Supply-bottleneck industrial factor:** REE (1), uranium (2), grid (4), tankers (5) — 4 of 5 Type B candidates. Concentrated bet on physical-supply scarcity.
- **Commodities-conditional / macro-conditional:** GLD, grid, tankers, V (partial), TSM (geopolitical option) — meaningful exposure but masked by the FRED gap (we cannot rate the macro driver).

**Coverage by scenario:**

- S1 (soft landing): well covered by Type A + grid.
- S2 (stagflation): well covered by Type B real-asset cluster + GLD/BTC.
- S3 (recession): **thin** — BRK-B cash is the only real ballast; no duration position; no explicit tail hedge.
- S4 (AI peak): **thin** — most of the candidate pool is the *opposite* bet; only BRK-B, COST, GLD survive.
- S5 (geopolitical): partial — REE/uranium/tankers + GLD; offset by TSM impairment.
- S6 (reflation): well covered by Type B.
- S7 (drift): MOAT, BRK-B, COST cover.
- S8 (tail): GLD + BRK-B cash partial; **no explicit tail hedge** (puts, OTM, long vol).

### 4. Holes surfaced

Ordered by load-bearing weight.

1. **No explicit tail hedge.** S3 (recession 0.14) + S8 (tail 0.02) jointly carry 0.16 probability, and the book has only implicit hedges (GLD, BRK-B cash, BTC partial). With the CBOE / options feed missing (assumption 9), forward-implied tail probability is *underestimated* — the gap goes the wrong way. Real probability of tail-protective payoff being needed could be 0.20+.
2. **AI-capex factor over-concentration.** The candidate pool + existing 18% tech sleeve makes the book a directional AI-capex bet. S4 (0.20) is uncovered. The tech-sizing inquiry already flagged factor MKT +1.1; adding GOOG or TSM widens this further.
3. **Flows feed gap is structural, not incidental.** Without crowding / positioning data we *cannot* probe reflexivity on Type B candidates (REE, uranium, silver) properly. The Type B recognition-window thesis *is* a reflexive thesis. Currently we are flying blind on the variable that determines whether the thesis path is monotone or oscillatory.
4. **No duration exposure.** TLT was rejected by Type B screen (macro-conditional, FRED-gap precludes drawdown bound) and not promoted by Type A (it's a macro instrument). But S3 (recession 0.14) and the FOMC distribution (cut paths total 0.40) suggest duration is a *natural* long-only ballast and we have *zero* exposure. This is a passive omission, not an active rejection.
5. **EDGAR stub means single-name valuation gaps are qualitative.** GOOG, BRK-B, COST, V, TSM valuations are soft; sober-case DCFs do not exist in this instance. Architect cannot rank within the Type A pool with confidence.
6. **Copper / industrial-metal convex exposure missing.** Copper was rejected by Type B screen as "50–70% recognised" but the *call option* on a reflation surprise (S6, 0.08) plus electrification + AI capex makes it a candidate hole. Rejected on "recognition" criterion, not on demand thesis — that's a borderline call worth re-probing.
7. **No FX or USD-funding-shock exposure.** S8 tail features USD funding shock; UUP rejected by both screens; no FX hedge in book. ETF-proxy macro graph cannot tell us where DXY is in regime terms.
8. **Mandate caps not formalised.** Sector caps, single-name caps, max drawdown — none are written. The 30% sector cap (per tech-sizing assumption 4) is informal. As more positions accumulate from child inquiries this becomes binding.
9. **`portfolio.current` is partly hand-snapshotted.** The book outside the tech sleeve is unknown to this inquiry. Assumption 5 confidence haircut applies.

**Known-thin (data) vs unknown (gap):**
- Known-thin: macro driver rating (FRED), single-name valuation (EDGAR), forward-implied vol (CBOE).
- Unknown: positioning / crowding (no feed at all), full book outside tech sleeve, real correlation matrix.

### 5. Proposed adjustments

Each adjustment surfaces a candidate convergent capital-flavour child inquiry id. **None are recommendations; all are options for user collapse.**

- **A1 — Add explicit tail hedge sleeve, 1–3% NAV.**
  *Rationale:* closes hole 1. Options: long-dated SPY/QQQ OTM puts, VIX call ladder, or constant-mix gold/long-vol. Cheapest under current vol regime is unknown without CBOE feed — that is the first child question.
  *Alternatives:* (i) lean harder on GLD as implicit hedge (cheaper, less convex); (ii) increase BRK-B weight (cash optionality at cost of return drag); (iii) do nothing and accept the tail.
  *Child inquiry:* `2026-05-15-tail-hedge-vehicle-selection` (convergent, capital-Collapse contingent on belief-Collapse on cost-effectiveness).

- **A2 — Cap AI-capex factor exposure before adding GOOG / TSM / grid.**
  *Rationale:* closes hole 2. Tech-sizing already kept tech sleeve at 18% with MKT +1.1, MOM +0.3. Adding 2 of {GOOG, TSM, grid} pushes implicit AI-capex factor toward concentration limit.
  *Alternatives:* (i) swap GOOG for MOAT (broader basket, lower idiosyncratic AI exposure); (ii) pair GOOG with explicit tail hedge or short basket; (iii) skip TSM, prioritise BRK-B + COST for ballast.
  *Child inquiry:* `2026-05-15-ai-capex-factor-cap` (convergent, belief-Collapse — sets the cap before any further single-name capital-Collapses).

- **A3 — Register a flows / positioning feed.**
  *Rationale:* closes hole 3 structurally. Without it, reflexivity probes on Type B are uncorroborated. Options: CFTC COT (free, lagged), prime-broker proxy via ETF flows, options skew / put-call ratio, sector ETF creation/redemption.
  *Alternatives:* (i) accept the gap and apply confidence haircut permanently; (ii) hand-snapshot at each inquiry (current de facto state).
  *Child inquiry:* `2026-05-15-flows-feed-registration` (convergent, **feed-Collapse** — not capital).

- **A4 — Open duration ballast position (TLT or barbell).**
  *Rationale:* closes hole 4. S3 (0.14) + dovish FOMC tail (cuts paths 0.40) make duration a natural ballast. Even FRED gap does not invalidate the directional bet — it caps confidence in size.
  *Alternatives:* (i) intermediate IEF instead of TLT (lower convexity, lower drawdown bound risk); (ii) credit spread proxy (LQD); (iii) skip duration, accept S3 vulnerability.
  *Child inquiry:* `2026-05-15-duration-ballast-sizing` (convergent, capital-Collapse).

- **A5 — Reframe copper from Type B "rejected" to Type A "industrial real-asset compounder".**
  *Rationale:* closes hole 6. Copper was rejected from Type B on "50–70% recognised" but durability + electrification + reflation-call-option make it a Type A candidate. The Type B screen `rejected_in_screen` line literally suggests this: "consider for Type A reframing".
  *Alternatives:* (i) buy a copper-miner basket (COPX) instead of single-name; (ii) skip and rely on grid (4) for indirect electrification exposure; (iii) wait for a pullback.
  *Child inquiry:* `2026-05-15-copper-as-type-a` (convergent, belief-Collapse first; capital downstream).

- **A6 — Tighten Type B sizing discipline (sequence + concentration cap).**
  *Rationale:* Type B candidates 1–5 are all reflexive, all small/mid-cap, all flows-blind. Without flows data, sizing all three of REE + uranium + silver simultaneously creates an implicit "supply-bottleneck commodities" factor concentration that S3 (recession 0.14) and S4 (AI-peak 0.20) jointly punish (0.34 of distribution).
  *Alternatives:* (i) sequence: pick highest-asymmetry one (REE 7:2) first, observe, then add; (ii) basket via REMX + URNM + SIL with smaller per-position size; (iii) full pool, but drawdown-cap each at smaller-than-screen-recommended size.
  *Child inquiry:* `2026-05-15-type-b-cluster-sizing` (convergent, capital-Collapse — coordinates across the three Type B sizing children rather than treating them independently).

- **A7 — Formalise mandate caps (sector, single-name, max drawdown).**
  *Rationale:* closes hole 8. Cheap to do; binding before, not after, child inquiries land.
  *Alternatives:* (i) write minimal caps now (per sector 30%, per name 8%, max book DD 25%); (ii) defer until first cap is approached.
  *Child inquiry:* `2026-05-15-mandate-caps-formalisation` (convergent, **belief-Collapse** — encodes constraint).

### 6. Reflexivity / second-order cross-check

Per architect spec failure mode 3, cross-check against edges marked `reflexive`. The graph currently has only `edge.crowding-to-drawdown` (illustrative). Walking it:
- `edge.crowding-to-drawdown` says P(forced unwind in 3mo | sector dd >5%) ≈ 0.25 conditional on positioning percentile >70 and vol mid-elevated or higher.
- This already informed the tech-sizing decision (reframe to within-sleeve concentration).
- **For Type B candidates, this same edge is *not* directly applicable** (small/mid-caps, not sector-level positioning data). But the *type* of edge applies in reverse: Type B recognition-window theses *benefit* from positioning building before recognition (positive reflexivity) and *suffer* from positioning blowing off after recognition (negative reflexivity at the late end). With the flows feed missing (hole 3) we cannot tell where on the curve we are. **This is the single biggest unsurfaced risk** in the proposed adjustments.

Recommend treating A3 (register flows feed) as the highest-value structural adjustment regardless of which capital adjustments the user collapses on.

### 7. Sensitivity

Single-perturbation sweep over load-bearing assumptions (1–10), walked edges (`edge.crowding-to-drawdown`), and scenario probabilities (S1–S8 within ±10pp calibration band). Pair-perturbation used where single-perturbation is non-informative. Surfacing the dominant brittle link per top adjustment, plus the broadest-leverage assumption.

**Brittle assumption for A1 (tail hedge sleeve 1–3% NAV).** Assumption 9 (vol regime mid-elevated, forward-implied tail probability *structurally underestimated* due to missing CBOE feed). A1's load-bearing claim is that explicit hedges are systematically cheaper than their fair value because IV does not reflect the true tail. **Threshold to flip:** if forward-implied vol on SPY/QQQ 3–6mo OTM puts is in the >65th percentile of its 5y range (i.e., tail is *richly* priced, not cheap), the implicit-hedge alternative (lean on GLD + BRK-B cash; A1 alternative i) dominates A1 on cost-adjusted convexity. This single perturbation does not require any change in S3+S8 probability mass — it flips on the *price* of the hedge alone. Pair-perturbation with S8 dropping from 0.02 → 0.00 (within band) accelerates the flip but is not necessary. **Verdict on A1 is robust** to perturbations in assumptions 1, 5, 6, 7, 8, 10 and to weakening of `edge.crowding-to-drawdown` strength from 0.25 → 0.10.

**Brittle assumption for A3 (register flows feed).** Assumption 7 (reflexivity edges sparse but real) — specifically the claim that reflexivity is load-bearing for the Type B universe at currently-contemplated sizes. A3's value rests on flows data being decision-relevant for sizing/timing of REE, uranium, silver. **Threshold to flip:** if reflexivity is refuted *as load-bearing for this universe at these sizes* — i.e., if Type B positions are small enough (<2% NAV each per A6 sequencing) that crowding cannot mechanically force-unwind the names, *and* `edge.crowding-to-drawdown.strength.mean` weakens from 0.25 to <0.10 with sector-ETF positioning shown to not map onto single-name miner flows — then A3 demotes from "structural priority" to alternative (i): "accept the gap and apply permanent confidence haircut." The architect's own §6 caveat ("for Type B this same edge is *not* directly applicable") is the seed of this flip. Pair-perturbation: assumption 7 refuted *and* A6 (Type B sizing discipline) accepted is what makes A3 deferrable; either alone is insufficient. **Verdict on A3 is robust** to perturbations in scenario probabilities, assumptions 2/3/5/9, and macro regime swings — A3 is structural, not scenario-conditional.

**Broadest-leverage assumption (inverts rank of A1–A5).** `themes.ai-capex-cycle` peak-timing distribution (currently 0.45/0.35/0.20 for late/mid/early peak). It is the single upstream node that conditions S1 (0.22) and S4 (0.20) jointly — 0.42 of the distribution — and indirectly modulates S6 (reflation surprise) and the Type B power-thesis derivatives (uranium rank 2, grid rank 4). **Threshold to flip rank:** a ~10–12pp shift of mass from "late peak" toward "early peak" (i.e., S4 rises from 0.20 → ~0.32 and S1 falls from 0.22 → ~0.12, both within ±10pp calibration band) inverts the A1–A5 ranking as follows:
- A2 (cap AI-capex factor) rises from rank 2 → rank 1 — becomes urgent before any further single-name AI capital-Collapses.
- A5 (reframe copper as Type A) drops from rank 5 → rank 6+ — copper's electrification leg is dampened if AI capex is rolling over.
- A4 (duration ballast) rises — recession-adjacency to AI peak strengthens.
- A1 stays high (tail mass rises) but A2 leapfrogs it.
- A3 (flows feed) is *unaffected by this perturbation* — confirming it as a structural, scenario-invariant adjustment (consistent with §6 finding).

The mirror perturbation (peak-timing shifts *later*: S4 → ~0.10, S1 → ~0.30) demotes A2 to rank 5+ and promotes A5 toward rank 2–3. No other single load-bearing assumption produces this magnitude of cross-adjustment reordering within its plausible range. Assumption 2 (FRED gap) and assumption 4 (flows gap) condition *confidence* uniformly but do not reorder rank. Assumption 6 (3-month outcome window) reorders A4 vs A5 modestly but does not touch A1/A2/A3.

**Dominant sensitivity surfaced.** The peak-timing distribution on `themes.ai-capex-cycle` is the brittle node for the proposal *as a whole*. Within-band drift on it reorders the top 5. Recommend the user, at Collapse, weight conviction on A2 vs A5 by their personal posterior on AI-capex peak timing, and treat A3 as the one adjustment whose value does not depend on resolving that posterior.

*Section status: ready.*

## Outcome

_Locked until outcome window (2026-08-08)._

- Realized state:
- Calibration delta (per-scenario probability vs realized + per-adjustment outcome if collapsed):
- Edges affected:

## Reflection

_Locked until outcome window._
