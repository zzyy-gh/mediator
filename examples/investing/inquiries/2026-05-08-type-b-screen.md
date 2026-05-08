---
id: 2026-05-08-type-b-screen
shape: divergent
collapse_flavour: belief
status: open
scope: "Surface current Type B (Asymmetric Speculative) candidates with deductively-likely undiscovered demand across all vehicles."
parent_inquiry: null
graph_snapshot: "2026-05-08T05:15Z (yfinance + crypto + commodities-fx + news-summarizer; FRED gap)"
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
owner: agent:screener-type-b
---

# Inquiry: Type B candidates (Asymmetric Speculative)

## Scope

Generate a ranked candidate list for the **Type B — Asymmetric Speculative** archetype as of 2026-05-08. For each candidate, require an explicit first-principles demand-deduction chain, identified supply-side bottleneck, narrow recognition window, and quantified drawdown bound under thesis-failure path. Vehicles in scope: stocks, ETFs, crypto, commodities, FX, fixed income.

**Out of scope:** sizing decisions, portfolio-fit checks, capital-Collapse. This inquiry's Collapse is a belief Collapse — the artifact is the ranked candidate list landing in `graph/strategies.md`. Sizing happens in child convergent inquiries.

## Assumptions (load-bearing)

1. AI infrastructure capex remains elevated through 2026; hyperscaler power-constraint timing is 2026–2028 (per `themes.ai-capex-cycle`, p≈0.55 within 36 months). Failure → demand-pull on grid/uranium/copper resets lower.
2. China retains export controls on heavy rare earths (Sm/Tb/Dy/Gd) and tightens enforcement through 2026. Failure → REE thesis collapses near-immediately.
3. SMR commercialisation milestones (NRC certification, first concrete pour, fuel orders) accelerate from 2026Q3 onward. Failure → uranium demand-pull pushed out 2+ years; spot price drift only.
4. Solar PV installations grow at >12 % YoY 2026–2027 globally; silver loading per cell does not collapse (no thrifting breakthrough). Failure → silver industrial demand reverts to flat.
5. Houthi/Red Sea disruption + Russia-fleet sanctions enforcement persist through 2026. Failure → tanker rates normalize to 2019 baseline within 6 months.
6. US/EU LNG export capacity ramps as scheduled (Plaquemines Phase II, Rio Grande Train 1, Corpus Christi 3) through 2027. Failure → gas oversupply pulls Henry Hub below $2.50.
7. No global recession deep enough to compress base-metal demand >10 % in 2026 (recognised as macro-conditional given thin FRED graph; flag).
8. Liquidity is sufficient at small/mid-cap miner level for $50k–$5m position sizing without material slippage.
9. Recognition latency: it takes the median market participant 6–18 months to reprice a thesis once supply-bottleneck data crosses a clear threshold.
10. Drawdown bound is computed as (max plausible 12-month decline under thesis-failure path) — not historical max — and includes the probability the thesis-failure occurs.

## Graph references

Pulled from snapshot 2026-05-08T05:15Z:

- `themes.ai-capex-cycle` — power binds before chip supply by 2027 (p≈0.45 within 18 months, p≈0.35 18–36 months). Powers candidates 1, 2, 4.
- `themes.payments_infrastructure_expansion` — FedNow broadening; not a Type B driver here, noted for completeness.
- `themes.capital_framework_overhaul` — bank dereg tailwind; relevant for community-bank M&A optional add (not making the cut for top-5).
- `politics.regulatory_deregulation_posture` — moderate easing baseline (p=0.50); supports financials but recognition not narrow.
- `politics.fednow_intermediary_rule` — noted, not load-bearing.
- `sentiment.fed_policy_stance` — neutral-slight-hawkish prior, fuzz_halo HIGH; treat any rate-conditional thesis as low confidence.
- `technicals.gld` last 431.68, vol 28.0 % — gold strong; informs silver/gold ratio framing.
- `technicals.uso` last 134.97, vol 73.1 % — anomalous; flag for data-quality, not used as signal.
- `technicals.dbc` last 30.25, vol 23.1 % — broad commodity tape mid-vol, supports commodities thesis viability.
- `technicals.btc_usd` 79616, vol 28.7 % — BTC ~30 % off recent highs; weighed but excluded (see rejected list).
- `technicals.eth_usd` 2280, vol 39.5 % — same.
- `technicals.xle` 55.95, vol 27.3 % — energy still volatile, gas-vs-oil split needed at child-inquiry stage.
- `macro.cfx_uup` 27.41, vol 5.9 % — DXY proxy steady; weak USD tailwind absent.
- `macro.cfx_eurusd_x` 1.1737 — EUR firmer; supports EU defense / Lynas-Australia thesis indirectly.
- `fundamentals.*` — stub only (edgar feed empty); flag — single-name fundamental claims rest on web_search, not graph.

**Graph gaps that limit confidence:**
- FRED feed missing → no rates, CPI, IP, payrolls; macro-conditional theses flagged low-confidence per inquiry.
- EDGAR feed stub → no filings-driven supply/capacity numbers; web_search compensates but lower provenance weight.
- No flows.md hydration → cannot assess crowding for any candidate.

## Intent

Produce a ranked list of vehicles where future demand is great and likely by deduction, the masses have not yet realised it, and current price reflects little of the unfolding demand. Each candidate carries a deductive chain, supply-side bottleneck, recognition-window estimate, asymmetry quantified, and a drawdown bound under thesis-failure.

Confidence on the *list as a whole*: 0.55 (medium). Macro-conditional candidates carry their own lower confidence individually due to FRED gap.

## Self

- **self.capability** — Vehicle-agnostic screen. Web_search available; graph hydrated for technicals + sentiment + politics; thin on fundamentals/macro. Cannot run live factor regressions or DCFs from this seat — those are downstream.
- **self.calibration** — No prior closed Type B inquiries on this instance; no track record yet. Assume base-rate Type B hit-rate ≈ 0.30–0.40 for a disciplined screen, payoff multiple on hits ≈ 3–8x (industry prior, not measured here). Treat all rankings as priors awaiting outcome data.
- **self.taste** — Bias toward structurally-bottlenecked physical-supply theses over narrative/sentiment trades; bias against any candidate that fails the boring-story test (would I take this if the story were dull?). Bias against crypto for Type B because recognition is rarely narrow there.

## M-nodes (sequence)

1. `m.probe.scope` — sharpened: vehicle-agnostic, all 5 hard criteria gating, top-5 ranked.
2. `m.probe.prior-art` — methods.md (drawdown bound, scenario stress); blind-spots.md (narrative seduction, recency, tail neglect); strategies.md Type B criteria.
3. `m.probe.world` — graph snapshot read; web_search supplements for SMR orders, REE export controls, silver inventory, LNG schedules, tanker rates.
4. `m.probe.edges` — themes.ai-capex-cycle → power → uranium/grid/copper; politics.regulatory_deregulation_posture → financials (deferred).
5. `m.reframe` — None needed; scope held.
6. `m.test.feasibility` — Each candidate filtered for: deductive chain, supply bottleneck, narrow window, quantified asymmetry, quantified drawdown bound. Five candidates passed; six were rejected (logged in output).
7. `m.collapse` — belief: candidate list landed in `graph/strategies.md` under `strategy.type-b.current_candidates`.

## Output (divergent)

Status: ready. Five candidates passed all five hard-criteria gates and are ranked below. Six rejected, with reasons. Each candidate suggests a child convergent inquiry for sizing.

### Ranked candidate list

---

**#1 — Heavy Rare Earths ex-China (Lynas Rare Earths LYC.AX / MP Materials MP / REMX ETF)**

- **Demand-deduction chain.** EV traction motors (NdFeB), wind-turbine generators, F-35/precision-munition guidance, MRI machines, robotics actuators all require rare-earth permanent magnets containing dysprosium and terbium for high-temperature performance. EV motor demand alone implies ~1.5–2x current global Dy/Tb output by 2030 (deductive from 30M+ EV units × 1.5–3kg NdFeB × ~3–6 % Dy/Tb content). Defense modernisation adds independent demand floor.
- **Supply bottleneck.** China refines >85 % of light REE and >95 % of heavy REE (Dy/Tb/Sm/Gd). Lynas Kalgoorlie is the only commercial heavy-REE separation plant outside China and Lynas is the only ex-China producer with operating heavy circuit (commissioning 2025–2026). MP Materials Stage III heavy separation 2026–2027. Energy Fuels/Ucore are years from output. China expanded export-control list in 2024–2025 to include Sm, Tb, Dy, Gd. New mine-to-magnet capacity outside China requires 5–8 years lead time (permitting + cap-ex + commissioning).
- **Recognition window.** 6–15 months. The thesis is *named* in trade press but not priced — Lynas trades at single-digit EBITDA multiple on bottom-cycle realised pricing; MP Materials still primarily light-REE story for most analysts. Recognition trigger: first material China export-licence denial to a Western auto/defense customer, OR Lynas reporting Dy/Tb separation revenue at a premium realised price.
- **Asymmetry.** Upside: 2.5–4x in 12–18 months on price-realisation regime change to USD ~$1500/kg+ Dy (vs ~$300 China-internal). Downside under thesis-failure (China rolls back controls AND new ex-China supply arrives faster): -35 %.
- **Drawdown bound (thesis-failure path).** Quantified at -40 % over 12 months, capped by physical asset book value floor on Lynas (NTA ~AUD 4/share vs current ~AUD 8). Position sizing should respect this hard bound.
- **Vehicle preference.** Lynas (LYC.AX) primary, MP Materials secondary, REMX ETF for diversified exposure (lower beta to single-name disappointment).
- **Suggested child inquiry.** `2026-05-09-lynas-sizing` (convergent, capital).

---

**#2 — Uranium fuel cycle / HALEU (Sprott Physical Uranium SRUUF/U.UN, Centrus Energy LEU, Cameco CCJ)**

- **Demand-deduction chain.** Hyperscaler nuclear power-purchase agreements (Microsoft-Constellation 2024, Amazon-Talen 2024, Meta RFP 2024–2025) commit to >5 GW of nuclear off-take by 2030. Restart fleet (Palisades, Three Mile Island/Crane) plus ~15 announced SMR projects in US/Canada/UK require fresh fuel orders 2026–2029. Western utilities holding 1.5–2 years of inventory (vs 3+ years pre-2022) need to refill in tightening market. Russia/Rosatom supplies ~25 % of global enrichment + ~40 % of HALEU technically; sanctions risk forces Western de-risking.
- **Supply bottleneck.** Cameco + Kazatomprom dominate primary supply. Kazatomprom missed production guidance 2023–2024–2025 (sulphuric-acid shortage, drilling backlog); Cameco running below licensed capacity. Spot inventory drawn down to multi-year lows. HALEU specifically: Centrus is the only NRC-licensed US HALEU producer (American Centrifuge Plant); commercial scale-up requires multi-year DOE contracts. New mines need 7–10 years minimum.
- **Recognition window.** 9–18 months. Spot U3O8 ~$65–75/lb in 2026 vs term contracts $80+. Equity compression has been severe since 2024 peak — recognition retracted, not yet rebuilt. Trigger: Kazatomprom guide-down again, OR first commercial HALEU contract award, OR utility contracting cycle picking up.
- **Asymmetry.** Upside: 2–3.5x on Sprott Physical, 3–6x on Centrus, 1.8–2.5x on Cameco over 12–24 months under thesis. Downside: utility contracting stalls, spot drifts to $50/lb.
- **Drawdown bound (thesis-failure path).** -30 % on Sprott Physical (NAV-floor close to spot uranium); -55 % on Centrus (operational leverage cuts both ways); -25 % on Cameco. Use Sprott Physical as core, Centrus as the asymmetric tail bet, sized to absorb -55 %.
- **Vehicle preference.** Sprott Physical (SRUUF / U.UN) for clean exposure, Centrus (LEU) for HALEU-specific torque, Cameco (CCJ) for liquid majors exposure.
- **Suggested child inquiry.** `2026-05-09-uranium-sizing` (convergent, capital).

---

**#3 — Silver (SLV / PSLV / SIL miners ETF)**

- **Demand-deduction chain.** Solar PV is now the largest single industrial silver use (~20 % of demand, growing). Per-cell silver loading on TOPCon and HJT cells is 2–3x older PERC. Global PV installations growing ~12–18 % YoY into 2027. AI datacenter electrification, EV power electronics, and 5G base-station infrastructure each add independent industrial demand. Fourth consecutive year of structural deficit (Silver Institute 2024–2025 estimates: 150–200 Moz/yr deficit).
- **Supply bottleneck.** ~70 % of mine silver is byproduct of lead/zinc/copper/gold. Byproduct supply is capex-unresponsive to silver price — it tracks the host metal cycle. Above-ground inventory (LBMA + COMEX + ETF) drawn ~25 % from 2021 peak. Primary silver miners are few and operationally stretched (Pan American, Hecla, First Majestic). New primary mine lead-time 7–10 years.
- **Recognition window.** 3–12 months. Silver is partially recognised but the gold/silver ratio remains historically extended (gold at all-time highs while silver lags). Recognition trigger: ratio compression below 70x, OR ETF inflows breaking 2020 levels, OR LBMA delivery stress reported.
- **Asymmetry.** Upside: SLV +60–120 % over 12–18 months on a mean-reversion-plus-deficit run to $50–60/oz; SIL +120–250 % on operational leverage. Downside under thesis-failure (PV thrifting + weak host metals): -25 % on SLV, -45 % on SIL.
- **Drawdown bound (thesis-failure path).** SLV -25 % bounded by mine cash-cost floor (~$15/oz all-in for top quartile). SIL -45 % bounded by miner book value at depressed silver price. Quantified, not "high vol = asymmetric".
- **Vehicle preference.** PSLV (allocated bullion, lower counterparty risk) > SLV (liquidity); SIL for torque if drawdown bound respected.
- **Suggested child inquiry.** `2026-05-09-silver-sizing` (convergent, capital).

---

**#4 — Grid transformer / HV interconnect supply chain (Hubbell HUBB, Eaton ETN, Hitachi 6501.T, Prysmian PRY.MI)**

- **Demand-deduction chain.** AI datacenter buildouts require ~1 GW per campus; queue interconnection backlog at PJM, ERCOT, MISO grew >2x 2022–2025. Reshoring industrial load adds ~10–15 % electricity demand by 2030. Grid hardening post-Helene/Beryl mandates accelerated transformer replacement. Utility capex cycles inflecting upward, multiple visibility years.
- **Supply bottleneck.** Large-power-transformer (LPT) lead times stretched from 50 weeks (2020) to 120–210 weeks (2025) globally. Grain-oriented electrical steel (GOES) is supply-constrained — only ~12 producers globally; AK Steel/Cleveland-Cliffs is sole US supplier. HV cable manufacturers (Prysmian, Nexans, NKT) have multi-year backlogs. New transformer plant 3–5 years; new GOES capacity 5+ years.
- **Recognition window.** Tighter — 3–9 months and partial. ETN/HUBB/GEV equities have re-rated meaningfully since 2023. The undiscovered torque is in second-derivative names (transformer-component suppliers, Japanese majors lagging US peers). **Flag: this candidate is on the edge of the recognition criterion.**
- **Asymmetry.** Upside: 60–120 % over 12–24 months on continued multiple expansion + capex visibility. Downside: -30–40 % on AI-capex digestion or utility capex slowdown.
- **Drawdown bound (thesis-failure path).** -40 % over 12 months under combined AI capex pause + utility rate-case denials. Bounded by ~15x trough earnings on quality industrial names.
- **Vehicle preference.** Hitachi (6501.T) and Prysmian (PRY.MI) preferred for less-priced exposure; HUBB/ETN as US-listed liquid options if non-US access constrained.
- **Suggested child inquiry.** `2026-05-09-grid-equipment-sizing` (convergent, capital). **Flag for the architect:** test for crowding before sizing.

---

**#5 — Product-tanker shipping (Scorpio Tankers STNG, International Seaways INSW, Hafnia HAFN)**

- **Demand-deduction chain.** Red Sea/Suez disruption forces Cape-of-Good-Hope routings, adding ~30 % ton-miles. Russian sanction-evasion shadow-fleet aging out (>20 years average) with limited insurer access. Refining capacity dislocation (Atlantic deficit, Asian surplus) drives long-haul product flows. Ton-mile demand structurally higher than pre-2022.
- **Supply bottleneck.** Product-tanker orderbook is ~12–15 % of fleet (low historically); newbuilds delivered 2026–2028 but yard slots limited (LNG/container priority). 20 %+ of fleet is >20 years old and faces phase-out under IMO emissions rules. New build lead time 2–3 years from order.
- **Recognition window.** 3–9 months. Ratings compressed during 2024–2025 rate softness; trades at low single-digit P/E and below NAV. Trigger: rate spike on next geopolitical incident, OR IMO enforcement clarity.
- **Asymmetry.** Upside: 80–150 % over 12 months on rate normalisation + multiple expansion. Downside: -35–50 % on Red Sea peace + global refining slack.
- **Drawdown bound (thesis-failure path).** -50 % bounded by NAV floor on tanker scrap value + remaining fleet earnings.
- **Vehicle preference.** STNG (cleanest fleet, share-buyback engine), INSW for diversified mix, HAFN for size.
- **Macro-conditional flag:** Strongly geopolitics-conditional. Lower confidence given thin FRED graph and the binary nature of the Red Sea outcome.
- **Suggested child inquiry.** `2026-05-09-tankers-sizing` (convergent, capital).

---

### Rejected candidates (logged for traceability)

- **GLP-1 manufacturing / fill-finish (Catalent acquired, NVO, Lilly contract manufacturers)** — Recognition window already closed; thesis is widely priced.
- **Bitcoin at $79.6k drawdown** — Not pre-recognition. Sentiment is the driver, not first-principles undiscovered demand.
- **Defense primes (RTX, LMT, Rheinmetall)** — Substantially recognised post-2022; doesn't pass narrow-window gate.
- **Copper majors (FCX, SCCO)** — Strong thesis but ~50–70 % recognised; remains a candidate for Type A reframing instead.
- **Long-duration Treasuries (TLT)** — Macro-conditional and FRED graph thin; cannot quantify drawdown bound under thesis-failure path with current data.
- **Community-bank takeout candidates (KRE-driven)** — Asymmetry insufficient at index level; single-name takeouts fail the diversifiable-risk test for a systematic screen.

### Ranking summary

| Rank | Candidate | Bottleneck quality | Window narrowness | Asymmetry (up:down) | Drawdown bound | Macro-conditional? |
|------|-----------|--------------------|--------------------|---------------------|----------------|--------------------|
| 1 | Heavy REE ex-China | very high | high | ~7:2 | -40 % | low |
| 2 | Uranium / HALEU | high | high | ~5:2 | -30 % to -55 % | low-medium |
| 3 | Silver | high | medium-high | ~4:1 | -25 % | low |
| 4 | Grid transformers | medium-high | medium (partial recog) | ~3:2 | -40 % | medium |
| 5 | Product tankers | medium | medium | ~3:1 | -50 % | high (flagged) |

## Outcome

_Locked until outcome window 2026-11-08._

## Reflection

_Locked until outcome window._
