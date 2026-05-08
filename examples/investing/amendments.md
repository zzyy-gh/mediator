# Amendments

Flat log of proposed and accepted changes to `objective.md`, `architecture.md`, `primitives.md`, `methods.md`, `template-inquiry.md`, `blind-spots.md`, or graph schemas. Append-only. Each entry is one block.

## Entry shape

```
### YYYY-MM-DD — short name
- **Trigger** — what surfaced this (calibration drift, repeated miss, new context, taste shift, regime change).
- **Proposal** — exactly what changes.
- **Tested on** — historical entries in `inquiries/` re-evaluated under the proposal.
- **Calibration delta** — measured improvement or regression.
- **Status** — proposed | tested | accepted | rejected | deferred.
- **Propagation** — files updated if accepted.
```

## Promotion rule

In-task reflection notes that recur across ≥3 inquiries become candidates. `objective.md` and `architecture.md` changes additionally require explicit user input plus a propagation pass across all dependent files.

## Log

### 2026-05-08 — factor-coverage checklist on m.probe.edges
- **Trigger** — 2026-05-08 type-a + type-b screens. FRED feed missing → macro probe shallow; no flows feed → crowding probe blind. Agents flagged candidates as "macro-conditional" but coverage of factor classes was uneven and not enforced. Single cycle, not yet ≥3, but proposing early because gap is structural not incidental.
- **Proposal** — extend `template-inquiry.md` `m.probe.edges` step with an explicit factor-coverage checklist that every inquiry must address (or explicitly mark not-applicable with reason):
  - macro (rates, growth, inflation, fiscal)
  - geographic (jurisdiction, sanctions, trade)
  - regime (vol, liquidity, dispersion)
  - correlation structure (what moves together / breaks)
  - flows (positioning, crowding, fund flows)
  - themes (narrative state, recognition stage)
  - reflexivity (positioning ↔ price ↔ narrative)
  - liquidity / capacity (size, exit cost)
- **Tested on** — pending; will re-evaluate against 2026-05-08-type-a-screen and 2026-05-08-type-b-screen on close.
- **Calibration delta** — n/a until tested.
- **Status** — proposed.
- **Propagation** — `template-inquiry.md` (extend m.probe.edges); `blind-spots.md` (add "factor-blindness" as named bias); agent specs in `agents/` (acknowledge checklist).

### 2026-05-08 — feed-gap promotes to assumption
- **Trigger** — same cycle as above. When FRED was missing, agents silently flagged candidates as macro-conditional rather than promoting the data gap to a load-bearing assumption with explicit confidence haircut. This makes the gap invisible at Collapse.
- **Proposal** — when a feed required by a factor probe is missing or stub-only, the agent MUST add an entry to the inquiry's `Assumptions (load-bearing)` block of the form: `Assume <factor> is approximated by <proxy / prior>; confidence haircut <X%>; resolves when <feed> hydrates.` This forces the gap into the Collapse decision.
- **Tested on** — pending.
- **Calibration delta** — n/a until tested.
- **Status** — proposed.
- **Propagation** — `template-inquiry.md` (Assumptions section guidance); `methods.md` (confidence-haircut convention); agent specs (require assumption-promotion on feed gap).

### 2026-05-08 — story-stock / fraud / overinflation screen on Type B candidates
- **Trigger** — user flagged: "did we consider possible scams or overinflated valuation and promises?" Helium adversarial probe (2026-05-08) confirmed gap: junior helium cohort 2017-2025 has ~0% commercial-success base rate (12 named explorers, all −80 to −95%), capex-to-cap 1.5-5x, recurring dilution pattern. Same risk pattern across other v2 candidates: tin juniors (Alphamin DRC), REE microcaps in REMX, lithium juniors (PLS.AX), uranium-LEU at small market cap, India infra mid-caps with local-accounting risk. Type B archetype as written did not require this screen.
- **Proposal** — extend `m.probe.feasibility` (or new step `m.probe.adversarial-base-rate`) on every Type B child convergent inquiry to require explicit screen for: (a) population base-rate of similar candidates reaching commercial state, (b) capex-to-market-cap ratio with implied dilution forecast, (c) free-float USD + insider concentration, (d) story-stock pattern markers (MOU vs binding contract, KPI redefinitions, founder turnover, retail-podcast promotion), (e) implied bull-case terminal multiple at current price vs comp 60th-pct (priced-in test).
- **Treatment is Bayesian, not gating.** Base rate is the prior. The screen does NOT auto-reject — strong signals can overpower a poor base rate: binding offtake contracts (not MOUs), audited reserves with primary-source independence, insider buying with $$$ commitment, financing covenants funded, multi-year operational track record on prior assets. If posterior materially exceeds base rate, candidate retains rank and sizing.
- **Hedge mechanics when concern is material but signals are mixed.** Pull from menu: (i) cohort basket (3-5 names) vs single-name to cap single-name fraud risk, (ii) index ETF vehicle (REMX, LIT, URA, SIL) over microcap pure-play to diversify execution risk while keeping thesis exposure, (iii) anchor-plus-satellite (large-cap with thesis exposure as anchor + microcap basket as satellite, e.g. APD + helium juniors), (iv) defined-risk options wrapper if/when CBOE feed registers, (v) pair-trade short of clearly-fraudulent comp to hedge cohort risk (high friction, asymmetric short cost), (vi) staged sizing — placebo first, scale on milestone hits.
- **Failure handling.** Failure on ≥2 dimensions WITHOUT compensating signals demotes ranking by ≥1 tier and caps sizing at placebo (<0.5% NAV) UNTIL evidence emerges OR a hedge mechanic above is applied. With a hedge in place, sizing band may be restored proportional to residual risk.
- **Tread-carefully clause.** This screen is a discipline, not an automatic disqualifier. Some Type B asymmetries are large enough that a 10% commercial-success rate at 30x payoff still clears a 2.5x E[R]/E[risk]. Reject only when hedge unavailable AND base rate × asymmetry fails to clear.
- **Tested on** — partially tested via helium probe on 2026-05-08; will retroactively re-rate v1 + v2 candidates against this screen on next pass before any capital Collapse.
- **Calibration delta** — n/a until tested. Helium probe alone shifted recommended sizing from "1-2% basket" to "<0.5% placebo or skip" — that's the screen earning its keep on first application.
- **Status** — proposed.
- **Propagation** — `blind-spots.md` (story-stock, valuation-bubble, microcap-fraud entries added 2026-05-08); `template-inquiry.md` (extend m.probe.feasibility); `agents/screener-type-b.md` (require base-rate cohort estimate per candidate); `agents/sensitivity-analyzer.md` (consider pricing-in test as named sensitivity dimension).

### 2026-05-08 — world-frame-first as available pattern (not prescribed)
- **Trigger** — user flagged that running screen-a / screen-b before any world-state framing produces a candidate pile the architect must then re-frame. Architect's open-considerations menu (regime, scenarios, correlation, reflexivity, ...) is the world frame; doing it last makes the screens upstream-blind. User explicitly clarified this is *not* a mandate — framework deliberately under-prescribes (objective.md treats portfolio architecture as open consideration, never prescribed).
- **Proposal** — register `world-frame-first` as an available cycle ordering, not a required one. Pattern: `feeds → world-state inquiry (divergent, belief) → screens conditioned on frame → architect`. Document it in `strategies.md` open-considerations menu (or a `methods.md` "cycle patterns" section if added) so a user or orchestrator can pull it situationally. Vehicle-first remains valid; choice is per-cycle.
- **Tested on** — pending; will re-evaluate after a cycle that adopts the pattern, vs the 2026-05-08 vehicle-first cycle.
- **Calibration delta** — n/a until tested.
- **Status** — proposed.
- **Propagation** — `strategies.md` open-considerations menu and/or a new `methods.md` cycle-patterns section; no orchestrator hard-wiring.
