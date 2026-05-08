---
id: 2026-05-08-type-b-screen-v2
shape: divergent
collapse_flavour: belief
status: open
scope: "Second-pass Type B screen — wider geographies, longer recognition windows, underexplored vehicle types, demand-floor candidates. Non-duplicating with v1."
parent_inquiry: 2026-05-08-type-b-screen
graph_snapshot: "2026-05-08T05:15Z (yfinance + crypto + commodities-fx + news-summarizer; FRED gap; same as v1 parent)"
outcome_window: 2027-05-08
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

# Inquiry: Type B candidates v2 (wider geo / longer window / new vehicle types)

## Scope

Second pass over the Type B candidate space. Parent inquiry `2026-05-08-type-b-screen` produced 5 US-listed equity-and-commodity candidates clustered around AI-power, defense, and shipping. This pass deliberately probes:

- **Wider geographies** — Asia ex-Japan (India infra, Indonesia tin), LATAM commodity producers (Argentina, Brazil), African mining (DRC copper, Mali lithium), European defense second-tier supply chain.
- **Longer recognition windows** — 18-36mo theses the first pass may have rejected as "too far."
- **Underexplored vehicle types** — frontier-market hard-currency sovereigns, EM local-currency debt, FX pairs with structural drivers, JGB short / yen carry unwind.
- **Adjacent themes** — fertilizer / phosphate (food security + China export controls), helium (semis + medical), lithium reframe at depressed prices, natural gas infrastructure ex-US, copper-substitute aluminum.
- **Demand-floor candidates** — things with deductively-likely demand even in S3 (recession) scenario.

Same five hard criteria still gate every candidate: demand-deduction chain, supply bottleneck, narrow recognition window, quantified asymmetry, quantified drawdown bound under thesis-failure path.

**Out of scope:** sizing, portfolio fit, capital-Collapse. Belief Collapse only.

**Duplicate handling:** any candidate that overlaps the v1 list (heavy REE, uranium/HALEU, silver, grid transformers, product tankers) is logged as `merged-with-original` in the rejected section and excluded from rank.

## Assumptions (load-bearing)

1. China export-control regime broadens from REE/Sb/Ga to phosphate, urea, and possibly fluorspar through 2026 (p≈0.45 within 18mo). Failure → fertilizer thesis loses near-term catalyst; demand-floor still partially holds.
2. India fiscal trajectory holds — capex push (rail, power T&D, water) sustained at current GDP-share through 2026-2028 election cycle (p≈0.65). Failure → mid-cap infra de-rates 25-35%.
3. European defense budgets stay above 2.5% NATO-target average through 2027 with German fiscal-rule special-fund continuing (p≈0.70). Failure → backlog growth slows but does not reverse.
4. Lithium price has overshot to the downside vs marginal cost; >35% of brownfield capacity is loss-making at sub-$10/kg LCE (p≈0.60 that price recovers to >$15 within 24mo). Failure → capex destruction continues; equities double-bottom.
5. Helium real demand is price-inelastic for the marginal user (semis dry-etch, MRI quench gas, fiber-draw cooling). Failure → if substitution accelerates (no observed signal yet) demand floor weakens.
6. Tin demand from electronics solder + AI-server miniaturization grows 2-4% per year; supply remains DRC-Indonesia-Myanmar concentrated with Indonesia continuing export-ore ban (p≈0.65). Failure → Wa-state/Bisie restart accelerates supply.
7. IMF + multilateral support continues for frontier sovereigns mid-restructuring (Egypt, Pakistan, Sri Lanka, Argentina); no second-wave default cluster (p≈0.65). Failure → cascading default re-prices recovery curves down 30-50%.
8. BOJ exits ZIRP fully — policy rate above 1.0% within 24mo (p≈0.55). Failure → JGB short loses carry; yen weakens further.
9. Recognition latency is asymmetric by vehicle: equities 6-18mo, sovereign hard-currency 12-24mo, FX 18-36mo, EM local-currency 18-36mo.
10. Drawdown bound is quantified per thesis-failure path; macro-conditional theses are flagged and confidence-haircut by 0.20 against the FRED feed gap.

## Graph references

Same snapshot as v1 (2026-05-08T05:15Z). New nodes touched:

- `themes.ai-capex-cycle` — supports tin (server miniaturization solder), helium (semi etch).
- `politics.regulatory_deregulation_posture` — neutral; not load-bearing here.
- `politics.us-china-tariff-regime-2026` — escalation 0.35; supports phosphate (China retaliation lever).
- `macro.cfx_eurusd_x` 1.1737 — EUR firmer; tailwind EU-defense USD-investor returns.
- `macro.cfx_usdjpy_x` 156.87 — extreme yen weakness; sets up BOJ-normalization asymmetry.
- `macro.cfx_dbc` 30.25 — broad commodity tape mid-vol.
- `technicals.eem` last 66.59, vol 28.7% — EM equity tape live; supports India / LATAM theses are tradeable.
- `technicals.tlt` last 85.65, vol 8.55% — duration cheap; supports frontier-sov USD bond thesis indirectly.
- `technicals.hyg` last 79.86, vol 5.37% — HY spreads tight; ironic backdrop for distressed-sovereign thesis (no contagion priced).

**Graph gaps that limit confidence (carried from v1 + new):**
- FRED feed missing → no DM rates, EM-DM real-rate differential, Indian CPI/IIP, Brazilian Selic; macro-conditional theses haircut.
- No EM-debt feed → frontier-sov spreads / yields rest on web_search.
- EDGAR stub → ex-US filings unavailable; LSE/ASX/B3/JSE filings rest on web_search.
- No commodities futures-curve feed → tin/lithium/phosphate term structure inferred not measured.

## Intent

Produce a ranked v2 candidate set (5-8 candidates) for Type B that is structurally non-overlapping with v1 along geography, recognition window, and vehicle type axes. Each carries the full hard-criteria gate. Confidence on the *list as a whole*: 0.50 (medium-low, lower than v1 due to wider geo / data-thinner candidates). Macro-conditional candidates carry their own lower confidence individually.

## Self

- **self.capability** — Vehicle-agnostic; web_search available. EM-debt and EM-FX candidates are at the edge of executable knowledge; quotes/spreads come from web_search rather than live feed. Cannot compute live curves or factor decompositions.
- **self.calibration** — No prior closed Type B inquiries on this instance. Industry prior on diversified Type B screens: hit-rate 0.30-0.40, payoff multiple on hits 3-8x. v2 candidates carry an extra calibration haircut (call it 0.10) for geographic data thinness.
- **self.taste** — Bias toward demand-floor theses that survive the recession scenario (S3 in v1 architecture); bias toward bottlenecks that take 5+ years to remediate; bias against story-stocks that lack physical-supply structure; bias against any pair trade where carry is the entire return.

## M-nodes (sequence)

1. `m.probe.scope` — sharpened: explicitly orthogonal to v1 along geography, window, vehicle type.
2. `m.probe.prior-art` — v1 inquiry, strategies.md Type B, blind-spots (narrative seduction, recency, tail neglect, EM-data thinness, FX-carry-as-return).
3. `m.probe.world` — graph snapshot read; web_search for fertilizer market, IMF programs (Egypt/Pakistan/Argentina), EU defense backlogs, lithium spot, helium contract pricing, tin LME inventory, BOJ policy path.
4. `m.probe.edges` — themes.ai-capex-cycle → helium + tin; politics.us-china-tariff-regime → phosphate retaliation; politics.regulatory_deregulation_posture → not load-bearing here; macro.cfx_usdjpy_x → JGB short.
5. `m.reframe` — None; scope held.
6. `m.test.feasibility` — Each candidate filtered for the 5 hard criteria. Eight passed; six rejected (logged below). Two of those rejected for `merged-with-original` (uranium-adjacent and grid-equipment second-derivatives) — surfaced but not double-counted.
7. `m.collapse` — belief: candidate list landed in `graph/strategies.md` under `strategy.type-b.current_candidates_v2`.

## Output (divergent)

Status: ready. Eight candidates passed all five hard-criteria gates and are ranked below. Six rejected (with reasons including two merged-with-original). Each candidate suggests a child convergent inquiry for sizing.

### Ranked candidate list (v2)

---

**#1 — Phosphate fertilizer / Mosaic MOS, OCP (private/MAD), Nutrien NTR, ICL ICL.TA**

- **Demand-deduction chain.** Global phosphate consumption tracks calorie demand at ~1.5-2% YoY structurally; demand floor is biological (P is one of three macronutrients with no substitute). Indian fertilizer subsidy is 1.5% of central budget — politically protected. China became net phosphate-export-restricter in 2023-2024 (DAP/MAP quota), with Q1 2026 export drop of >20% YoY. India + Brazil + SE Asia together import ~35% of seaborne phosphate. Food-security demand floor survives recession scenario S3.
- **Supply bottleneck.** Phosphate rock reserves are heavily concentrated: Morocco (~70% global reserves, OCP), China (declining grades, export-restricted), Russia (sanctioned), US (depleted, Mosaic legacy). New mine permitting 7-12 years; Florida mine permits face wetlands litigation. China DAP export cap is structural through 2026-2028. Marginal cost producer is Saudi Ma'aden; price floor implicit at >$550/t DAP.
- **Recognition window.** 12-24 months. DAP price recovered from $400 (2024) to $580 (Q1 2026) but equities lag — MOS trades at ~7x trough EBITDA, ICL near 5-year low. Recognition trigger: India tender clears at >$650 DAP, OR China announces extended quota.
- **Asymmetry.** Upside: MOS +80-150% over 18-24mo on price normalization to $700+ DAP; OCP IPO (Morocco signaled 2026-2027) unlocks valuation reference; ICL +60-100%. Downside (recession + China relaxes quota + Saudi ramp): -30-40%.
- **Drawdown bound (thesis-failure path).** -35% on MOS bounded by replacement-cost-of-asset floor (Florida mines + Saskatchewan potash); -40% on ICL bounded by potash + bromine optionality. Quantified, not vol-based.
- **Vehicle preference.** MOS (US-listed liquidity), ICL.TA / ICL (potash + phosphate hybrid, lower beta), Nutrien (potash-heavy reference). Non-listed OCP exposure via watching IPO timeline.
- **Suggested child inquiry.** `2026-05-15-phosphate-sizing` (convergent, capital).

---

**#2 — European defense second-tier (Hensoldt HAG.DE, Kongsberg KOG.OL, Leonardo LDO.MI, Saab SAAB-B.ST, Thales HO.PA)**

- **Demand-deduction chain.** German Sondervermögen (€100bn special fund) commits >€90bn through 2028; Polish defense at 4.5% GDP; Nordic accession to NATO drove sustained equipment refresh. Primes (Rheinmetall, BAE, RTX) have re-rated; *electronics, sensors, missiles seekers, EW, undersea sonar* are second-derivative names where the recognition has not fully propagated. EU defense industrial strategy (EDIS) channels procurement preference toward EU-domiciled suppliers — explicit demand floor independent of US politics.
- **Supply bottleneck.** EU defense electronics capacity (Hensoldt radar, Saab AESA, Thales sensors) bottlenecked by skilled-labour, classified-clearance staffing, and specific ASIC fab access. Backlog-to-revenue at Hensoldt 2.8x, Kongsberg 4.5x, multi-year visibility. New entrants face decade-long qualification cycles.
- **Recognition window.** 12-24 months. Primes already re-rated 3-5x off 2022 base. Second-tier is up but trades at 14-18x forward earnings vs primes 22-28x — a clear gap driven by liquidity and US-investor unfamiliarity.
- **Asymmetry.** Upside: Hensoldt +70-130% on multiple convergence + backlog conversion; Kongsberg +60-100%; Saab +50-90%. Downside (Ukraine ceasefire + budget pause + EUR weakness): -25-35%.
- **Drawdown bound (thesis-failure path).** -35% bounded by 12x trough EBIT on backlog burn; lower beta to peace-trigger than primes because backlog is multi-year and contracts include cancellation penalties.
- **Vehicle preference.** Hensoldt (cleanest pure-play sensors), Kongsberg (NSM missile + maritime), Saab (Gripen + AESA), Leonardo (more conglomerate but cheap). EUR exposure tailwind for USD investors.
- **Suggested child inquiry.** `2026-05-15-eu-defense-tier2-sizing` (convergent, capital).

---

**#3 — India infrastructure mid-caps (L&T LT.NS, Siemens India SIEMENS.NS, ABB India ABB.NS, Cummins India CUMMINSIND.NS; ETF SMIN/INDA/EPI)**

- **Demand-deduction chain.** Indian electricity demand growing 7-9% YoY; T&D capex tripled 2020-2025 and capex-to-GDP at multi-decade high. Data-center buildout (Mumbai-Hyderabad-Chennai) adds 5-7 GW of demand by 2030. Rail electrification + dedicated freight corridors + water-sanitation under Jal Jeevan are explicit fiscal commitments. Demographic demand floor: 1.45bn population, urbanization 36% headed to 50% — independent of global cycle.
- **Supply bottleneck.** Indian engineering/EPC (L&T) is duopolistic at scale; Siemens / ABB India hold the high-voltage automation IP with multi-year backlogs; Cummins India dominates standby gensets (data-center critical). Skilled-engineer constraint biting 2024-2026; capacity-expansion lead times 3-5 years for HV equipment.
- **Recognition window.** 18-36 months. Indian large-caps are well known; the recognition gap is in *foreign-investor allocation* — India under-owned in EM ex-China benchmarks, with foreign holding share at 15-year low after 2024-2025 FII outflows. Recognition trigger: re-acceleration of Indian GDP guide above 7% + FII inflow turn + RBI rate cuts.
- **Asymmetry.** Upside: L&T +60-100% over 24-36mo on backlog conversion + multiple stability; Siemens India +80-130% on premium-execution multiple; SMIN ETF +40-70%. Downside (election-cycle fiscal pause + global recession): -30-40%.
- **Drawdown bound (thesis-failure path).** -35% on L&T bounded by ~18x sober earnings on confirmed backlog; -40% on small/mid-cap basket. ETF route caps single-name risk.
- **Macro-conditional flag:** medium — INR depreciation under USD strength would mute USD returns 5-10%.
- **Vehicle preference.** SMIN (small/mid-cap ETF) for diversified exposure; L&T ADR or local for liquid single-name; Siemens India for execution premium.
- **Suggested child inquiry.** `2026-05-15-india-infra-sizing` (convergent, capital).

---

**#4 — Tin (Alphamin AFM.V, Metals X MLX.AX, MSC SM.KL, ITRI/iShares no clean ETF; physical via LME-tracking notes)**

- **Demand-deduction chain.** ~50% of tin demand is electronics solder; lead-free (RoHS) demand grew tin loading per board ~25% over decade. AI server miniaturization + EV power-electronics + 5G/data-center backplanes increase tin per unit. Photovoltaic ribbon (+8% of demand and growing) ties tin to solar buildout. Demand floor in S3: solder is non-substitutable for high-density electronics.
- **Supply bottleneck.** Top-3 producers are DRC (Alphamin Bisie, periodic militia disruption), Indonesia (export-ore ban + smelter consolidation), Myanmar (Wa State, suspended 2023-2024). LME inventory at multi-year lows in 2025-2026. New mine lead time 7-10 years; major projects (Achmmach Morocco, Cleveland Tasmania) years from production. China is a net importer.
- **Recognition window.** 12-24 months. Tin is partly recognised — LME price ran from $20k to $35k 2023-2024 — but equities have not kept pace; Alphamin trades at <4x EBITDA, Metals X near book. Recognition trigger: LME inventory cover below 5 days, OR Wa State outage extension.
- **Asymmetry.** Upside: Alphamin +120-200% over 18-24mo at $40-50k tin; Metals X +80-150%. Downside (Myanmar restart + Indonesia relaxation + electronics recession): -45-55%.
- **Drawdown bound (thesis-failure path).** -50% bounded by Alphamin operating cash-cost (~$18k/t) and net-cash balance sheet. -55% on MLX. Sized accordingly.
- **Vehicle preference.** Alphamin (purest play, Canadian-listed), Metals X (Australian, diversified), MSC (Malaysian smelter for non-mining angle).
- **Suggested child inquiry.** `2026-05-15-tin-sizing` (convergent, capital).

---

**#5 — Frontier hard-currency sovereign basket (Egypt EGY USD'31/'33, Pakistan PAK USD'27/'29, Argentina ARG USD'30/'35, Sri Lanka SRILAN USD'28 post-restructure)**

- **Demand-deduction chain.** Each name has an active IMF program with explicit reform conditionality and disbursement schedule. Egypt: $8bn IMF program + UAE $35bn Ras El-Hekma deal + EU/EBRD support — debt-service liquidity for 2026-2028 secured. Pakistan: $7bn EFF approved 2024, second review on track. Argentina: Milei reform locked in stabilization; net-FX reserves rebuilding; Treasury bond curve flattening. Sri Lanka: post-restructure, IMF compliant. Pricing of these bonds is at 50-70 cents on the dollar with coupons 8-11% — implies large default probabilities the IMF backstop arguably contradicts.
- **Supply bottleneck.** Frontier-sov USD bond issuance has been minimal post-2022 (window closed); aggregate stock is shrinking (debt buy-backs in Egypt, Argentina). Crowding out has reversed — dedicated EM-frontier funds raised cash 2022-2024. Recognition trigger: ratings upgrade (single-step from current B-/CCC), OR successful tap issue at sub-9% yield.
- **Recognition window.** 18-36 months. Carry is intrinsic (8-11% USD yield); price upside is recognition-driven. The slowness is the reason the asymmetry exists.
- **Asymmetry.** Upside: total return 30-60% over 24-36mo on price recovery to 80-90 + accrued coupons. Downside (default cluster, US-rate spike, IMF program collapse): -30-45% on price + lost coupons.
- **Drawdown bound (thesis-failure path).** Basket -35% bounded by historical post-default recovery rates (40-55 cents per Moody's sovereign-recovery data 1983-2023). Diversified across 4 names + maturities to bound idiosyncratic risk. Single-name -50%.
- **Vehicle preference.** Direct USD-bond holdings via broker (institutional-only typically); NEXTGEN ETF or T. Rowe EM Bond / PIMCO EM Bond as proxies; Argentina via GGAL/BMA/YPF equity adjacencies.
- **Macro-conditional flag:** high — USD-cycle and DM-rate path matter. Confidence-haircut 0.20.
- **Suggested child inquiry.** `2026-05-15-frontier-sov-basket-sizing` (convergent, capital).

---

**#6 — Lithium reframe at depressed prices (Albemarle ALB, SQM, Pilbara Minerals PLS.AX, Arcadium ALTM, Ganfeng 1772.HK)**

- **Demand-deduction chain.** EV adoption decelerated but did not reverse; BNEF 2026 base case still implies 2x lithium demand by 2030. Energy-storage system (ESS) deployment grew 65% YoY 2025 and is now ~25% of lithium demand independent of EV cycle. Spodumene spot at $750-900/t (vs $7000 peak); LCE at ~$9/kg vs marginal cost stack ~$11-13/kg for sub-quartile producers. >35% of brownfield capacity loss-making; capex destruction visible (2024-2025 mothballed: Mt Cattlin, Greenbushes Train 3 deferral, Liontown ramp slowed). Demand floor from ESS even in S3.
- **Supply bottleneck.** Brownfield response time 2-4 years even from current stretched price; new lepidolite (China) is high-cost and ESG-fragile. SQM/Albemarle Atacama brine expansions face Chilean state-participation overhang. Producer discipline has emerged: 2025 saw first coordinated capex cuts since 2018.
- **Recognition window.** 18-30 months. Counter-positioning: lithium is the most widely-disliked commodity sub-sector; sentiment is at 2018-bottom levels. Recognition trigger: spodumene above $1,200/t for two consecutive quarters, OR meaningful ESS-only contract awarded at premium price, OR ALB/SQM dividend coverage restoration.
- **Asymmetry.** Upside: ALB +120-220% over 24-30mo on $20+/kg LCE; PLS +150-300% on operational leverage; SQM +60-120% (more diversified). Downside (BEV slowdown + China Yichun cheap supply persists): -35-50%.
- **Drawdown bound (thesis-failure path).** -45% on ALB bounded by net-asset-value at $9/kg LCE plus bromine + catalysts businesses. -55% on PLS bounded by spodumene cash-cost ($550/t for top quartile) and net cash. ETF (LIT) caps single-name risk at -40%.
- **Vehicle preference.** SQM (diversified, Chilean, dividend-paying) for core; PLS.AX for torque; ALB for US-listed liquidity; LIT ETF for diversified.
- **Suggested child inquiry.** `2026-05-15-lithium-reframe-sizing` (convergent, capital).

---

**#7 — Helium pure-plays (Pulsar Helium PLSR.V, Desert Mountain Energy DME.V, Total Helium HE.V; broader: Air Products APD as anchor)**

- **Demand-deduction chain.** Helium demand splits ~30% MRI cryogenics (price-inelastic medical), ~30% semiconductor dry-etch and lithography (AI capex driver), ~15% fiber-optic draw, ~10% lifting/leak detection, balance industrial. Semi demand grows with leading-edge node count (every node needs more helium). Helium has zero substitute for super-cold cryogenics and electron-microscopy. Demand floor in S3: medical MRI does not cycle.
- **Supply bottleneck.** Helium is geological — Earth's atmosphere has only 5 ppm; commercial extraction requires specific deep-source nitrogen-helium gas fields (Texas-Hugoton depleting; Algeria, Qatar, Russia Amur dominant). US BLM Federal Helium Reserve sold 2024 — reserve buffer eliminated. Russian Amur 2 plant ramp problems in 2024-2025. Qatar extension secure but capacity-constrained. New helium project lead time 5-10 years from discovery; Pulsar Topaz Minnesota is one of very few new ex-Russia/ex-Qatar projects. Spot helium prices have risen 2-3x in 2024-2025 with little visibility.
- **Recognition window.** 18-30 months. Pure-play universe is microcap and illiquid; recognition will follow first-major-contract awards. Trigger: Pulsar enters production with a Praxair / Linde / APD off-take, OR Russia / Qatar supply disruption.
- **Asymmetry.** Upside: PLSR / DME +200-500% on first-production cashflow; APD anchor +20-40% from helium re-pricing of contracts. Downside (Qatar ramp + Algeria expansion + demand softening): -50-70% on micro-caps; -15% on APD.
- **Drawdown bound (thesis-failure path).** Microcap basket -65% bounded by drilled-resource value at $200/Mcf (vs spot $400+); position-size in the basket to absorb -65%. APD -15% bounded by diversified industrial-gas earnings.
- **Vehicle preference.** Basket of PLSR/DME/HE.V (small position size, e.g., 1-2% NAV total); APD as larger anchor for institutional-grade exposure.
- **Suggested child inquiry.** `2026-05-15-helium-basket-sizing` (convergent, capital).

---

**#8 — JGB short / yen carry unwind (TBT-style Japan ETF JGBS, FX direct USDJPY puts, EWJ-hedge pair)**

- **Demand-deduction chain.** BOJ ended NIRP April 2024, raised to 0.50% by January 2026; CPI persistently above 2% target for 4 years; wage growth (2024 shunto +5.1%, 2025 +5.2%) above productivity. Real policy rate still deeply negative. Yen at 156 vs USD reflects extreme carry; unwind is reflexive — once BOJ commits to >1%, both rates rise *and* yen strengthens, compressing carry-trade flows. Aging Japanese household savers demand higher domestic yields. Structural demand is for more BOJ tightening relative to consensus.
- **Supply bottleneck.** Of JGB outstanding, BOJ owns ~50%; ministry-of-finance issuance schedule constrained politically. As BOJ tapers, marginal buyer must be bank/insurance/foreign — all yield-sensitive. JGB curve has steepened but 10y still well below model (2.5-3% fair vs 1.5% spot). Marginal seller of carry is Japanese life-insurer FX-hedged USTs, who will repatriate as USDJPY-hedged yields turn negative.
- **Recognition window.** 18-36 months. Vehicle is asymmetric: short JGB futures or USDJPY puts have defined max-loss = premium. The carry-unwind narrative has been called too early multiple times since 2022 — this is *why* the recognition window persists.
- **Asymmetry.** Upside: 10y JGB to 2.5% from 1.5% = ~9% bond-price decline = 4-6x on JGBS notional; USDJPY puts struck 140 with 18-24mo expiry could 5-15x on a move to 130-135. Downside: bonds drift, yen weakens further to 165, premium burns.
- **Drawdown bound (thesis-failure path).** Options structure: pure premium-at-risk; size at <1.5% NAV per leg. JGBS / inverse JGB ETF: -25% over 12mo bounded by curve flattening rather than collapse.
- **Macro-conditional flag:** high. FX/rates pair, structurally driven but timing-sensitive.
- **Vehicle preference.** USDJPY put options 12-24mo as the cleanest defined-risk vehicle; JGBS / inverse-JGB ETF as a second leg; EWJ + USDJPY hedge as third (long Japan equity, short yen-currency-exposure within EWJ).
- **Suggested child inquiry.** `2026-05-15-yen-carry-unwind-sizing` (convergent, capital).

---

### Rejected candidates v2 (logged for traceability)

- **Argentina equity (YPF, GGAL, BMA, ARGT ETF)** — Strong thesis but already up 2-4x from 2023 lows; pre-recognition has substantially closed. Logged as adjacency to candidate #5 (frontier sovereigns) for sizing-stage consideration.
- **Brazil iron-ore (Vale VALE)** — Demand-floor argument exists (China steel + Indian infra + grid steel) but recognition is high; trades on China headlines. Asymmetry insufficient at index level; consider for Type A reframing.
- **Indonesian nickel (INCO, ANTM)** — Supply bottleneck reversed (Indonesia is now flooding the market). Fails supply-bottleneck gate. Reject.
- **Copper-substitute aluminum (Alcoa AA, Norsk Hydro NHY.OL)** — Substitution thesis depends on copper > $5.50/lb persistently; partial recognition; demand chain probabilistic rather than deductive. Pass for now; revisit if copper breaks higher.
- **African mining juniors (Endeavour EDV, Ivanhoe IVN.TO)** — Endeavour fails narrow-window (already up materially); Ivanhoe is large-cap copper-DRC story partially recognised. Reject for narrow-window failure on this pass.
- **Natural gas infra ex-US (Snam SRG.MI, Enagas ENG.MC, Petronet LNG)** — `merged-with-original` adjacency to #4 grid transformers thesis; midstream economics dominated by regulated returns; asymmetry insufficient. Reject as merged.
- **Kazakh tenge / Kazatomprom KAP.IL** — `merged-with-original` (uranium thesis #2 in v1). Logged.
- **EM local-currency debt (EMLC ETF)** — Strong carry but window too wide and asymmetry mostly carry rather than recognition-driven price; recognition trigger ill-defined. Reject — fails narrow-window gate cleanly.

### Ranking summary v2

| Rank | Candidate | Geography | Window (mo) | Bottleneck | Asym (up:down) | DD bound | Macro-cond? | Demand-floor in S3? |
|------|-----------|-----------|-------------|------------|----------------|----------|-------------|--------------------|
| 1 | Phosphate fertilizer | Morocco/US/Israel | 12-24 | high | ~3:1 | -35% | low | yes (food) |
| 2 | EU defense tier-2 | Europe | 12-24 | medium-high | ~3:1 | -35% | low-med | yes (budget) |
| 3 | India infra mid-caps | India | 18-36 | medium | ~5:2 | -40% | medium | yes (demographic) |
| 4 | Tin | DRC/Indonesia/Aus | 12-24 | very high | ~3:1 | -50% | medium | partial |
| 5 | Frontier hard-cur sov | EM/Frontier | 18-36 | medium (issuance) | ~2:1 + carry | -35% basket | high | n/a (carry) |
| 6 | Lithium reframe | Chile/Aus/China | 18-30 | medium-high (capex destr) | ~4:1 | -45% | medium | partial (ESS) |
| 7 | Helium pure-plays | Global | 18-30 | very high (geological) | ~5:1 | -65% basket | low | yes (medical+semis) |
| 8 | JGB short / yen carry | Japan | 18-36 | high (BOJ ownership) | options-defined | premium-only | high | n/a (rates) |

**Surprise candidate:** Helium. Initially expected to fail recognition-window or supply-bottleneck on closer inspection; the 2024 BLM reserve sale + Amur 2 ramp issues + zero-substitution medical floor combine into one of the cleanest demand-floor / geological-bottleneck stacks in the candidate set. Position-size discipline (microcap basket) is the gating constraint, not thesis quality.

**Blockers:**
- FRED feed gap continues to limit confidence on macro-conditional candidates (5, 6, 8 most affected).
- No EM-debt / sovereign-spread feed → frontier-sov candidate (#5) rests on web_search-derived prices; provenance weight lower.
- No commodities futures-curve feed → tin / lithium / phosphate term structure inferred not measured.
- Liquidity at microcap helium / DRC tin level requires position-size discipline; sizer must respect.

## Outcome

_Locked until outcome window 2027-05-08._

## Reflection

_Locked until outcome window._
