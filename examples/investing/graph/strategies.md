# Strategy Nodes

Standing graph-resident nodes for the two archetypes plus the live portfolio architecture. Updated by screener and architect inquiries.

## Type A — standing node

```yaml
- id: strategy.type-a
  topic: themes
  content: "Resilient compounder archetype"
  criteria_summary:
    - "ecosystem moat"
    - "multi-year FCF compounding under sober assumptions"
    - "optionality preserved"
    - "low obsolescence risk across futures"
    - "sober-case valuation gap"
  current_candidates:
    - rank: 1
      symbol: GOOG
      vehicle: stock
      durability: "Multi-product ecosystem; AI-shift survivable via Cloud + Gemini + Waymo optionality."
      valuation: "Fair-to-modestly-undervalued under sober DCF; Cloud + Waymo near-free."
      macro_conditional: false
      child_inquiry: 2026-05-15-goog-deep-dive
      provenance:
        source: inquiry.2026-05-08-type-a-screen
        timestamp: 2026-05-08T05:15:27Z
    - rank: 2
      symbol: BRK-B
      vehicle: stock
      durability: "Diversified holding-co; cash + insurance float = anti-fragile; lowest realised vol in universe."
      valuation: "Fair; book compounds 8-10%; cash pile is dry-powder optionality."
      macro_conditional: false
      child_inquiry: 2026-05-15-brk-b-sober-case
      provenance:
        source: inquiry.2026-05-08-type-a-screen
        timestamp: 2026-05-08T05:15:27Z
    - rank: 3
      symbol: COST
      vehicle: stock
      durability: "Membership flywheel + scale; AI-shift insulated; taste-resilient."
      valuation: "Persistent premium multiple; admitted as fair, not undervalued. Multiple-compression risk."
      macro_conditional: false
      child_inquiry: 2026-05-15-cost-multiple-risk
      provenance:
        source: inquiry.2026-05-08-type-a-screen
        timestamp: 2026-05-08T05:15:27Z
    - rank: 4
      symbol: MOAT
      vehicle: etf
      durability: "Rules-based wide-moat basket; embeds Type A archetype by construction."
      valuation: "Methodology over-weights names below Morningstar fair value — valuation gap embedded."
      macro_conditional: false
      child_inquiry: 2026-05-15-moat-as-core-allocation
      provenance:
        source: inquiry.2026-05-08-type-a-screen
        timestamp: 2026-05-08T05:15:27Z
    - rank: 5
      symbol: GLD
      vehicle: commodity
      durability: "Monetary asset with millennial track record; durable across all stress dimensions."
      valuation: "Macro-driven; entry-timing low-confidence given FRED feed gap; underlying durability high-confidence."
      macro_conditional: true
      child_inquiry: 2026-05-15-gld-entry-timing
      provenance:
        source: inquiry.2026-05-08-type-a-screen
        timestamp: 2026-05-08T05:15:27Z
    - rank: 6
      symbol: BTC
      vehicle: crypto
      durability: "Censorship-resistant monetary network; 17-year track record; structurally tailwinded by deglobalization."
      valuation: "Adoption-S-curve framing, no DCF; high fuzz_halo on framework. Vol-haircut sizing."
      macro_conditional: partial
      child_inquiry: 2026-05-15-btc-as-type-a
      provenance:
        source: inquiry.2026-05-08-type-a-screen
        timestamp: 2026-05-08T05:15:27Z
    - rank: 7
      symbol: V
      vehicle: stock
      durability: "Two-sided network; FedNow / stablecoin displacement is the genuine threat."
      valuation: "Premium multiple, fair not undervalued; sober-case 7-9% top-line CAGR."
      macro_conditional: partial
      child_inquiry: 2026-05-15-v-rails-displacement-risk
      provenance:
        source: inquiry.2026-05-08-type-a-screen
        timestamp: 2026-05-08T05:15:27Z
    - rank: 8
      symbol: TSM
      vehicle: stock
      durability: "Leading-edge foundry monopoly; business durability high; jurisdictional tail is the discriminator."
      valuation: "Undervalued ex-tail; the discount IS the geopolitical option premium."
      macro_conditional: false
      child_inquiry: 2026-05-15-tsm-tail-bounded-sizing
      provenance:
        source: inquiry.2026-05-08-type-a-screen
        timestamp: 2026-05-08T05:15:27Z
  hit_rate: null                # filled by outcome-recorder over time
  calibration: null
  provenance:
    source: strategies.md
    timestamp: 2026-05-08T00:00:00Z
  last_screened:
    inquiry: 2026-05-08-type-a-screen
    timestamp: 2026-05-08T05:15:27Z
  fuzz_halo: "criteria are illustrative; not gating; current_candidates carry low-resolution flag — fundamentals graph is stub, FRED macro thin."
```

## Type B — standing node

```yaml
- id: strategy.type-b
  topic: themes
  content: "Asymmetric speculative archetype"
  criteria_summary:
    - "explicit demand-deduction chain"
    - "supply-side bottleneck"
    - "narrow window before realisation"
    - "asymmetric payoff"
    - "drawdown-bounded sizing"
  current_candidates:
    - rank: 1
      label: "Heavy rare earths ex-China"
      vehicles: ["LYC.AX", "MP", "REMX"]
      demand_chain: >
        EV traction motors + wind generators + defense PMA + robotics actuators
        require NdFeB magnets containing Dy/Tb for high-temp performance. EV motor
        demand alone implies ~1.5-2x current Dy/Tb output by 2030.
      bottleneck: "Lynas only ex-China heavy-REE separator operating; China >95% Dy/Tb refining; new mine-to-magnet 5-8yr"
      recognition_window_months: [6, 15]
      asymmetry_up_down: "~7:2"
      drawdown_bound_pct: -40
      drawdown_floor: "Lynas NTA ~AUD 4/sh"
      macro_conditional: false
      child_inquiry: "2026-05-09-lynas-sizing"
    - rank: 2
      label: "Uranium / HALEU"
      vehicles: ["SRUUF", "U.UN", "LEU", "CCJ"]
      demand_chain: >
        Hyperscaler nuclear PPAs + restart fleet + ~15 SMR projects need fuel
        2026-2029. Western utilities at multi-yr inventory lows. Russia/Rosatom
        risk forces Western enrichment de-risking.
      bottleneck: "Kazatomprom guidance misses 3yr running; Centrus sole NRC-licensed HALEU; new mines 7-10yr"
      recognition_window_months: [9, 18]
      asymmetry_up_down: "~5:2"
      drawdown_bound_pct: -55
      drawdown_floor: "Sprott Physical NAV ~ spot uranium; Centrus operationally levered"
      macro_conditional: false
      child_inquiry: "2026-05-09-uranium-sizing"
    - rank: 3
      label: "Silver"
      vehicles: ["PSLV", "SLV", "SIL"]
      demand_chain: >
        Solar PV (TOPCon/HJT 2-3x silver loading vs PERC) + EV power electronics +
        AI datacenter + 5G + record industrial demand. 4yr structural deficit
        150-200 Moz/yr.
      bottleneck: "70% mine supply is byproduct of Pb/Zn/Cu/Au — capex-unresponsive to silver price; primary miners few"
      recognition_window_months: [3, 12]
      asymmetry_up_down: "~4:1"
      drawdown_bound_pct: -45
      drawdown_floor: "All-in cash cost ~$15/oz top quartile"
      macro_conditional: false
      child_inquiry: "2026-05-09-silver-sizing"
    - rank: 4
      label: "Grid transformer / HV interconnect"
      vehicles: ["6501.T", "PRY.MI", "HUBB", "ETN"]
      demand_chain: >
        AI datacenter ~1GW per campus; queue interconnect backlog 2x at PJM/ERCOT/MISO.
        Reshoring +10-15% electricity demand by 2030. Grid hardening accelerates
        transformer replacement.
      bottleneck: "LPT lead times 120-210wk (vs 50wk in 2020); GOES electrical-steel ~12 producers globally; HV cable backlog multi-yr"
      recognition_window_months: [3, 9]
      asymmetry_up_down: "~3:2"
      drawdown_bound_pct: -40
      drawdown_floor: "~15x trough EPS on quality industrials"
      macro_conditional: true
      flag: "edge of recognition criterion; check crowding before sizing"
      child_inquiry: "2026-05-09-grid-equipment-sizing"
    - rank: 5
      label: "Product tankers"
      vehicles: ["STNG", "INSW", "HAFN"]
      demand_chain: >
        Red Sea/Suez disruption -> Cape routings +30% ton-miles. Russian shadow-fleet
        aging out. Refining-capacity dislocation drives long-haul product flows.
      bottleneck: "Orderbook 12-15% of fleet (low historically); >20% fleet >20yrs facing IMO phase-out; yard slots scarce"
      recognition_window_months: [3, 9]
      asymmetry_up_down: "~3:1"
      drawdown_bound_pct: -50
      drawdown_floor: "NAV = scrap value + remaining earnings"
      macro_conditional: true
      flag: "geopolitics-conditional and binary; thin FRED graph caps confidence"
      child_inquiry: "2026-05-09-tankers-sizing"
  rejected_in_screen:
    - { label: "GLP-1 manufacturing", reason: "recognition window closed" }
    - { label: "BTC at drawdown", reason: "not pre-recognition; sentiment-driven not first-principles" }
    - { label: "Defense primes", reason: "substantially recognised post-2022" }
    - { label: "Copper majors", reason: "50-70% recognised; consider for Type A reframing" }
    - { label: "Long-duration USTs (TLT)", reason: "macro-conditional; FRED gap precludes drawdown bound" }
    - { label: "Community-bank takeouts", reason: "asymmetry insufficient at index level; single-name diversifiable" }
  current_candidates_v2:
    - rank: 1
      label: "Phosphate fertilizer"
      vehicles: ["MOS", "ICL", "NTR"]
      geography: "Morocco / US / Israel"
      demand_chain: >
        Phosphate is non-substitutable macronutrient; calorie demand floor; India + Brazil + SEA
        seaborne import demand ~35% global; China DAP/MAP export quotas structural through 2026-2028.
      bottleneck: "Reserves >70% Morocco (OCP); China grades declining + export-restricted; Russia sanctioned; new mine 7-12yr"
      recognition_window_months: [12, 24]
      asymmetry_up_down: "~3:1"
      drawdown_bound_pct: -35
      drawdown_floor: "Replacement-cost-of-asset on Florida + Saskatchewan; ICL potash+bromine floor"
      macro_conditional: false
      demand_floor_recession: true
      child_inquiry: "2026-05-15-phosphate-sizing"
    - rank: 2
      label: "EU defense second-tier supply chain"
      vehicles: ["HAG.DE", "KOG.OL", "LDO.MI", "SAAB-B.ST", "HO.PA"]
      geography: "Europe"
      demand_chain: >
        German Sondervermogen >EUR90bn through 2028; Polish defense 4.5% GDP; Nordic NATO refresh.
        EDIS channels EU-domiciled procurement preference. Second-tier electronics/sensors/seekers
        recognition has not propagated; primes already re-rated.
      bottleneck: "Skilled-labour + classified-clearance + ASIC fab access; backlog 2.8-4.5x revenue; multi-year qualification"
      recognition_window_months: [12, 24]
      asymmetry_up_down: "~3:1"
      drawdown_bound_pct: -35
      drawdown_floor: "12x trough EBIT on multi-year backlog with cancellation penalties"
      macro_conditional: false
      demand_floor_recession: true
      child_inquiry: "2026-05-15-eu-defense-tier2-sizing"
    - rank: 3
      label: "India infrastructure mid-caps"
      vehicles: ["LT.NS", "SIEMENS.NS", "ABB.NS", "CUMMINSIND.NS", "SMIN", "INDA"]
      geography: "India"
      demand_chain: >
        Electricity demand 7-9% YoY; T&D capex tripled 2020-2025; data-centers 5-7GW by 2030;
        rail electrification + Jal Jeevan fiscal commitments. Demographic urbanization 36->50%.
        Foreign holding share at 15yr low — under-owned recognition gap.
      bottleneck: "L&T duopoly at scale; Siemens/ABB India HV automation IP; Cummins genset; skilled-engineer constraint; 3-5yr HV capacity"
      recognition_window_months: [18, 36]
      asymmetry_up_down: "~5:2"
      drawdown_bound_pct: -40
      drawdown_floor: "~18x sober earnings on confirmed backlog; ETF caps single-name risk"
      macro_conditional: true
      flag: "INR depreciation could mute USD returns 5-10%"
      demand_floor_recession: true
      child_inquiry: "2026-05-15-india-infra-sizing"
    - rank: 4
      label: "Tin"
      vehicles: ["AFM.V", "MLX.AX", "SM.KL"]
      geography: "DRC / Indonesia / Australia / Malaysia"
      demand_chain: >
        ~50% demand electronics solder (lead-free RoHS expanded loading); AI server miniaturization
        + EV power-electronics + 5G + PV ribbon. Non-substitutable for high-density electronics.
      bottleneck: "Top-3 = DRC (Bisie militia risk) + Indonesia (export-ore ban) + Myanmar (Wa State suspended). LME inv multi-year low. New mine 7-10yr."
      recognition_window_months: [12, 24]
      asymmetry_up_down: "~3:1"
      drawdown_bound_pct: -55
      drawdown_floor: "Alphamin cash-cost ~$18k/t + net cash; MLX book"
      macro_conditional: true
      demand_floor_recession: partial
      child_inquiry: "2026-05-15-tin-sizing"
    - rank: 5
      label: "Frontier hard-currency sovereign basket"
      vehicles: ["EGY USD'31/'33", "PAK USD'27/'29", "ARG USD'30/'35", "SRILAN USD'28"]
      geography: "EM Frontier (Egypt / Pakistan / Argentina / Sri Lanka)"
      demand_chain: >
        Each name has active IMF program + bilateral support (UAE Ras El-Hekma for Egypt;
        IMF EFF for Pakistan; Milei stabilization for Argentina; post-restructure compliance for SL).
        Pricing 50-70 cents on dollar with 8-11% USD coupons implies default probability arguably
        contradicted by multilateral backstop.
      bottleneck: "Frontier-sov USD issuance window minimal post-2022; aggregate stock shrinking; dedicated EM funds raised cash 2022-2024"
      recognition_window_months: [18, 36]
      asymmetry_up_down: "~2:1 + 8-11% carry"
      drawdown_bound_pct: -35
      drawdown_floor: "Historical post-default recovery 40-55c (Moody's 1983-2023); basket diversification"
      macro_conditional: true
      flag: "USD-cycle and DM-rate path matter; confidence-haircut 0.20"
      demand_floor_recession: false
      child_inquiry: "2026-05-15-frontier-sov-basket-sizing"
    - rank: 6
      label: "Lithium reframe at depressed prices"
      vehicles: ["ALB", "SQM", "PLS.AX", "ALTM", "LIT"]
      geography: "Chile / Australia / China"
      demand_chain: >
        EV demand decel but not reversed (BNEF base 2x by 2030); ESS deployment +65% YoY 2025
        and ~25% lithium demand independent of EV cycle. >35% brownfield capacity loss-making
        at <$10/kg LCE; capex destruction visible (Mt Cattlin, Greenbushes T3, Liontown ramp).
      bottleneck: "Brownfield response 2-4yr; lepidolite high-cost+ESG-fragile; Chilean Atacama state-participation overhang; producer discipline emerged 2025"
      recognition_window_months: [18, 30]
      asymmetry_up_down: "~4:1"
      drawdown_bound_pct: -55
      drawdown_floor: "ALB NAV at $9/kg + bromine/catalysts; PLS spodumene cash-cost $550/t + net cash"
      macro_conditional: true
      demand_floor_recession: partial
      child_inquiry: "2026-05-15-lithium-reframe-sizing"
    - rank: 7
      label: "Helium pure-plays"
      vehicles: ["PLSR.V", "DME.V", "HE.V", "APD"]
      geography: "Global (US / Canada / Tanzania exploration; anchor APD)"
      demand_chain: >
        ~30% MRI cryogenics (price-inelastic medical); ~30% semi dry-etch + lithography (AI driver);
        ~15% fiber draw. Zero substitute for super-cold cryogenics + electron-microscopy.
        Demand floor in S3: medical does not cycle.
      bottleneck: "Geological (atmosphere 5ppm); commercial extraction = specific N2-He gas fields. US BLM Federal Reserve sold 2024. Russia Amur 2 ramp issues. Qatar capacity-constrained. New project 5-10yr."
      recognition_window_months: [18, 30]
      asymmetry_up_down: "~5:1"
      drawdown_bound_pct: -65
      drawdown_floor: "Drilled-resource value at $200/Mcf vs spot $400+; basket sizing absorbs -65%"
      macro_conditional: false
      demand_floor_recession: true
      flag: "microcap basket; position-size discipline gating"
      child_inquiry: "2026-05-15-helium-basket-sizing"
    - rank: 8
      label: "JGB short / yen carry unwind"
      vehicles: ["USDJPY puts 12-24mo", "JGBS inverse-JGB ETF", "EWJ + USDJPY-hedge pair"]
      geography: "Japan"
      demand_chain: >
        BOJ ended NIRP Apr 2024, +0.50% by Jan 2026; CPI >2% for 4yrs; shunto wage +5%/yr 2024-2025.
        Real policy rate deeply negative. USDJPY 156 reflects extreme carry. BOJ tightening reflexive:
        rates rise + yen strengthens, compressing carry flows. Aging savers demand domestic yield.
      bottleneck: "BOJ owns ~50% JGB stock; MoF issuance constrained; marginal buyer (banks/insurers/foreign) yield-sensitive; lifers repatriate as USDJPY-hedged USTs turn negative"
      recognition_window_months: [18, 36]
      asymmetry_up_down: "options-defined (5-15x on puts)"
      drawdown_bound_pct: "premium-only on options; -25% on JGBS ETF"
      drawdown_floor: "Premium at risk on options structure; size <1.5% NAV per leg"
      macro_conditional: true
      flag: "FX/rates pair; timing-sensitive; called too early since 2022"
      demand_floor_recession: false
      child_inquiry: "2026-05-15-yen-carry-unwind-sizing"
  rejected_in_screen_v2:
    - { label: "Argentina equity (YPF/GGAL/BMA/ARGT)", reason: "pre-recognition substantially closed; up 2-4x from 2023 lows" }
    - { label: "Brazil iron-ore (VALE)", reason: "high recognition; trades on China headlines; consider Type A" }
    - { label: "Indonesian nickel (INCO/ANTM)", reason: "supply bottleneck reversed; Indonesia flooding market" }
    - { label: "Copper-substitute aluminum (AA/NHY.OL)", reason: "substitution probabilistic not deductive; partial recognition" }
    - { label: "African mining juniors (EDV/IVN)", reason: "narrow-window fails — EDV up materially; IVN partially recognised" }
    - { label: "Nat-gas infra ex-US (SRG.MI/ENG.MC/Petronet)", reason: "merged-with-original adj #4 grid; midstream regulated returns insufficient asym" }
    - { label: "Kazakh tenge / KAP.IL", reason: "merged-with-original (v1 #2 uranium)" }
    - { label: "EM local-currency debt (EMLC)", reason: "window too wide; asymmetry mostly carry; recognition trigger ill-defined" }
  current_candidates_v2_provenance:
    source: inquiry.2026-05-08-type-b-screen-v2
    timestamp: 2026-05-08T07:00:00Z
    snapshot: "2026-05-08T05:15Z (same as v1 parent; FRED + EM-debt + commodities-curve gaps)"
    parent_inquiry: 2026-05-08-type-b-screen
  current_candidates_provenance:
    source: inquiry.2026-05-08-type-b-screen
    timestamp: 2026-05-08T05:30:00Z
    snapshot: "2026-05-08T05:15Z (yfinance + crypto + commodities-fx + news-summarizer; FRED gap)"
  last_screened:
    inquiry: 2026-05-08-type-b-screen
    timestamp: 2026-05-08T05:30:00Z
  hit_rate: null
  calibration: null
  provenance:
    source: strategies.md
    timestamp: 2026-05-08T00:00:00Z
  fuzz_halo: "criteria are illustrative; not gating; current_candidates carry low-resolution flag on macro-conditional ranks (4,5) — FRED feed missing; fundamentals graph is stub."
```

## Type B — post-reconciliation portfolio digest

Concise current state. Source-of-truth is the per-candidate child inquiry; this is the read-out.

```yaml
- id: strategy.type-b.portfolio-digest
  topic: themes
  content: "Type B current sizing post deep-dive + adversarial probe + reconciliation"
  as_of: 2026-05-08
  candidates:
    - rank: 1
      label: "Heavy rare earths"
      sleeve_pct: 1.5    # reconciled down from 2.5
      vehicles: { LYC.AX: 0.75, MP: 0.50, REMX: 0.25 }
      brittle: "demand-deduction collapse OR China rollback (joint kill p~0.40)"
      cluster: supply-bottleneck
      horizon_mo: 18
      e_r_over_e_risk_24mo: 0.20-0.25
      status: open; demoted from #1 pending evidence (E1 OEM motor mix, E2 Dy/Tb intensity, E3 REMX flows)
      child_inquiry: 2026-05-09-lynas-sizing
    - rank: 2
      label: "Uranium / HALEU"
      sleeve_pct: 4.0
      vehicles: { SRUUF_or_U.UN: 2.4, CCJ: 1.0, LEU: 0.6 }    # 60/25/15
      brittle: "HALEU sole-source duration"
      flip_triggers: ["Urenco USA HALEU commercial delivery", "DOE >=40% non-Centrus award", "Russian HALEU waiver >50% pre-2024"]
      cluster: supply-bottleneck
      horizon_mo: 24
      e_r_over_e_risk: { 12mo: 1.25, 24mo: 2.13 }
      status: open
      child_inquiry: 2026-05-09-uranium-sizing
    - rank: 3
      label: "Silver"
      sleeve_pct: 4.0
      vehicles: { PSLV: 2.8, SIL: 1.2 }    # 70/30 bullion/miner
      brittle: "gold-correlation regime stability"
      auto_resize_triggers: ["GLD vol >35% AND off >10% peak -> halve", "Si/Au corr <0.50 sustained 30d -> close miner", "copper-plating commercial -> halve miner"]
      cluster: supply-bottleneck
      horizon_mo: 12
      e_r_over_e_risk_blended: 2.75
      status: open
      child_inquiry: 2026-05-09-silver-sizing
    - rank: 4
      label: "Phosphate fertilizer"
      sleeve_pct: 2.0    # Track A baseline; Track B 3.0 if cluster cap raised
      vehicles: { MOS: 1.2, ICL: 0.5, NTR: 0.3 }    # 60/25/15
      brittle: "recession demand-floor robustness"
      flip_triggers: ["corn <$3.80 sustained 2Q AND diesel/gas spike >40% AND DAP -15%"]
      cluster: supply-bottleneck (zero AI-capex coupling — diversifies cluster)
      horizon_mo: 18
      e_r_over_e_risk_24mo: ~1.5
      status: open; cluster cap collision flagged for architect Collapse
      child_inquiry: 2026-05-15-phosphate-sizing
    - rank: 5
      label: "EU defense second-tier"
      sleeve_pct: 3.0
      vehicles: { HAG.DE: 0.90, KOG.OL: 0.75, SAAB-B.ST: 0.75, HO.PA: 0.60 }    # LDO excluded
      brittle: "German Sondervermögen continuation"
      flip_triggers: ["P(non-continuation) >= 0.45 -> drop HAG, cap <=1.0%"]
      cluster: aggregate (not supply-bottleneck)
      horizon_mo: 24
      e_r_over_e_risk: { 12mo: 0.57, 24mo: 1.25 }
      fx: unhedged EUR
      status: open
      child_inquiry: 2026-05-15-eu-defense-tier2-sizing
    - rank: 6
      label: "India infra mid-caps"
      sleeve_pct: 4.0
      vehicles: { SMIN: 2.4, LT.NS: 0.8, SIEMENS.NS: 0.5, ABB.NS: 0.3 }    # 60/40 ETF/single-name
      brittle: "FII flow turn (foreign-holding mean-reversion)"
      flip_triggers: ["12mo net FII <$0bn -> halve", "<-$10bn AND USDINR>92 -> close"]
      cluster: aggregate-only (geographically + mechanically uncorrelated to bottleneck cluster)
      horizon_mo: 36
      e_r_over_e_risk: { 24mo: 0.60, 36mo: 1.05 }
      fx: unhedged INR; conditional NDF if USDINR>92 sustained 30d
      status: open
      child_inquiry: 2026-05-15-india-infra-sizing
    - rank: 7
      label: "Helium"
      sleeve_pct: 1.75    # reconciled down from 4.5; staged scale-up gated
      vehicles: { APD: 1.5, PLSR.V: 0.10, DME.V: 0.10, HE.V: 0.05 }    # placebo basket + anchor
      brittle: "P(2027 supply glut) ~0.35-0.40 × microcap-conversion-without-binding-signals"
      scale_up_gates: ["binding offtake (not MOU)", "NI 51-101 reserves at production scale", "non-dilutive financing closed"]
      cluster: supply-bottleneck
      horizon_mo: 24
      e_r_over_e_risk_blended: 1.0
      status: open; placebo only until evidence emerges
      child_inquiry: 2026-05-15-helium-basket-sizing
  cluster_totals:
    supply_bottleneck: 13.25    # REE 1.5 + U 4.0 + Ag 4.0 + phosphate 2.0 + helium 1.75
    aggregate_total: 20.25       # + EU defense 3.0 + India infra 4.0
  cluster_caps_status:
    supply_bottleneck_cap_8_to_10pct: BREACHED (13.25 vs 8-10 architect target — requires belief-Collapse on A6 to formalise raise OR sibling trims)
    aggregate_type_b_cap: not formalised — A7 (mandate caps) is pending
  cross_cutting_evidence_gates:
    - { id: E1, item: "Primary OEM EV motor architecture mix (NdFeB-PMSM vs EESM vs induction vs SynRM)", gates: ["rare earths"] }
    - { id: E2, item: "Per-motor Dy/Tb content trend (Tesla Highland teardown, BMW Gen-5)", gates: ["rare earths"] }
    - { id: E3, item: "REMX flow data + LYC.AX thematic-ownership %", gates: ["rare earths"] }
    - { id: E4, item: "Helium spot price path Q2-Q4 2026 (industry-press + earnings calls)", gates: ["helium"] }
    - { id: E5, item: "Qatar Helium 3 actual utilisation vs ~425 mmcf/yr nameplate", gates: ["helium"] }
    - { id: E6, item: "PLSR/DME binding offtake or NI 51-101 booking through Q4 2026", gates: ["helium"] }
    - { id: E7, item: "FII flow direction (NSDL/SEBI proxy)", gates: ["india infra"] }
    - { id: E8, item: "FRED hydration (real rates path)", gates: ["all macro-conditional"] }
    - { id: E9, item: "Flows feed registration (architect A3)", gates: ["all (reflexivity)"] }
  v2_remaining_unsized: ["tin", "frontier sov basket", "lithium reframe", "yen carry unwind"]
  open_human_decisions:
    - "Collapse on cluster cap (raise to 13-15% to fit existing or trim siblings to fit 10%)"
    - "Collapse on architect A1-A7 adjustments"
    - "Collapse on tech-sizing inquiry"
    - "Trigger evidence-gathering for E1-E9 (assign owners or feed-inquiries)"
  provenance:
    source: ["inquiries/2026-05-09-{lynas,uranium,silver}-sizing.md", "inquiries/2026-05-15-{phosphate,eu-defense-tier2,india-infra,helium-basket}-sizing.md", "inquiries/2026-05-08-{rare-earths,helium}-adversarial-probe.md", "inquiries/2026-05-08-portfolio-architecture.md"]
    timestamp: 2026-05-08T12:00:00Z
  fuzz_halo: "all sizing pre-Collapse; reconciliations applied where probe-vs-deep-dive gap was material (rare earths, helium); cluster cap status load-bearing for any capital Collapse."
```

## Portfolio architecture — open snapshot

```yaml
- id: strategy.portfolio-architecture
  topic: themes
  content: "Current architecture snapshot — framings in use, scenario set, balance assessment"
  framings_in_use:
    - { framing: "scenario distribution", weight: load-bearing,  rationale: "candidate pool spans macro-conditional and macro-insensitive vehicles" }
    - { framing: "macro regime",          weight: low-resolution, rationale: "Type B cands 4-5 + Type A GLD macro-conditional; FRED gap caps confidence" }
    - { framing: "game-theoretic flow",   weight: load-bearing,  rationale: "rate-cut path + dereg posture point to specific flow recipients" }
    - { framing: "correlation structure", weight: load-bearing,  rationale: "Type A US-mega-cap correlation under stress vs Type B real-asset cluster" }
    - { framing: "tail-hedge availability", weight: load-bearing, rationale: "implicit hedges (GLD, BRK-B cash) but no explicit hedges; CBOE feed missing" }
    - { framing: "reflexivity",           weight: load-bearing,  rationale: "Type B recognition-window theses are explicitly reflexive" }
    - { framing: "mandate / time-horizon mix", weight: partial,  rationale: "Type A multi-year vs Type B 3-18mo; mandate loose" }
    - { framing: "liquidity / capacity",  weight: partial,        rationale: "Type B small/mid-cap miners; carried from Type B screen" }
  scenario_set:
    scenarios:
      - { id: S1, label: "Soft landing + dereg + AI capex extends", p: 0.22, wins: ["GOOG","V","MOAT","COST","grid","BRK-B"], loses: ["tankers","GLD entry-timing"], flows: "growth megacap + regional banks + infra industrials + credit tightens" }
      - { id: S2, label: "Stagflation lite",                        p: 0.18, wins: ["GLD","BTC","silver","REE","uranium","BRK-B cash"], loses: ["TLT-equivalents","V","COST margin"], flows: "real assets + gold + commodities; multiples compress" }
      - { id: S3, label: "Recession + Fed cuts faster than priced", p: 0.14, wins: ["BRK-B cash","TLT (not in book)","MOAT","GLD"], loses: ["tankers","grid","REE","silver","uranium","V","GOOG"], flows: "duration + defensives + gold; cyclicals dump" }
      - { id: S4, label: "AI capex peak inside 18 months",          p: 0.20, wins: ["BRK-B","COST","V","GLD"], loses: ["grid","uranium","GOOG","TSM"], flows: "defensives + value rotation; semis derate; power-thesis hit" }
      - { id: S5, label: "Geopolitical escalation",                 p: 0.10, wins: ["GLD","BTC","REE","uranium","tankers"], loses: ["TSM","GOOG","V"], flows: "safe havens + energy + commodities + defense" }
      - { id: S6, label: "Reflation surprise",                      p: 0.08, wins: ["silver","REE","uranium","grid","tankers","TSM"], loses: ["TLT-equivalents","GLD","V multiple"], flows: "cyclicals + commodities + value; growth derates" }
      - { id: S7, label: "Status quo drift",                        p: 0.06, wins: ["MOAT","BRK-B","COST","V"], loses: ["Type B (no recognition trigger)"], flows: "carry trades; distribution flat" }
      - { id: S8, label: "Tail / fat-left",                         p: 0.02, wins: ["GLD","BTC partial","BRK-B cash"], loses: ["everything risk; Type B small-caps gap 30-50%"], flows: "dollars + gold; everything else dumps" }
    probabilities: { S1: 0.22, S2: 0.18, S3: 0.14, S4: 0.20, S5: 0.10, S6: 0.08, S7: 0.06, S8: 0.02 }
    calibration_band_per_scenario_pp: 10
  balance_assessment:
    concentrations:
      - "AI-capex factor across 5-6 candidates + existing 18% tech sleeve (dominant implicit factor bet)"
      - "US-mega-cap factor across 5 of 8 Type A candidates (book MKT already +1.1)"
      - "Supply-bottleneck industrial cluster across 4 of 5 Type B candidates"
    holes:
      - { id: H1, label: "no explicit tail hedge", load_bearing: high, scenarios_uncovered: ["S3","S8"] }
      - { id: H2, label: "AI-capex factor over-concentration", load_bearing: high, scenarios_uncovered: ["S4"] }
      - { id: H3, label: "no flows / positioning feed (reflexivity probe is structurally blind)", load_bearing: high, scenarios_uncovered: "all (cross-cutting)" }
      - { id: H4, label: "no duration exposure (passive omission, not active rejection)", load_bearing: medium, scenarios_uncovered: ["S3"] }
      - { id: H5, label: "EDGAR stub - single-name valuation gaps qualitative", load_bearing: medium, scenarios_uncovered: "all (cross-cutting)" }
      - { id: H6, label: "no copper / industrial-metal convex exposure", load_bearing: medium, scenarios_uncovered: ["S6"] }
      - { id: H7, label: "no FX / USD-funding-shock exposure", load_bearing: low, scenarios_uncovered: ["S8"] }
      - { id: H8, label: "mandate caps not formalised (sector/name/max-DD)", load_bearing: medium, scenarios_uncovered: "all (governance)" }
      - { id: H9, label: "portfolio.current outside tech sleeve unknown to this inquiry (broker feed not wired)", load_bearing: medium, scenarios_uncovered: "all (data)" }
    proposed_adjustments:
      - { id: A1, action: "add explicit tail hedge sleeve, 1-3% NAV", closes: ["H1"], child_inquiry: "2026-05-15-tail-hedge-vehicle-selection" }
      - { id: A2, action: "cap AI-capex factor before adding GOOG/TSM/grid", closes: ["H2"], child_inquiry: "2026-05-15-ai-capex-factor-cap" }
      - { id: A3, action: "register flows / positioning feed", closes: ["H3"], child_inquiry: "2026-05-15-flows-feed-registration", collapse_flavour: feed }
      - { id: A4, action: "open duration ballast (TLT or barbell)", closes: ["H4"], child_inquiry: "2026-05-15-duration-ballast-sizing" }
      - { id: A5, action: "reframe copper from Type B rejected to Type A candidate", closes: ["H6"], child_inquiry: "2026-05-15-copper-as-type-a" }
      - { id: A6, action: "tighten Type B sizing discipline (sequence + concentration cap)", closes: ["partial H2","cluster risk on H3"], child_inquiry: "2026-05-15-type-b-cluster-sizing" }
      - { id: A7, action: "formalise mandate caps (sector/name/max-DD)", closes: ["H8"], child_inquiry: "2026-05-15-mandate-caps-formalisation", collapse_flavour: belief }
    second_order_cross_check:
      reflexive_edges_walked: ["edge.crowding-to-drawdown"]
      finding: >
        Type B recognition-window theses (REE, uranium, silver) are positively reflexive pre-recognition,
        negatively reflexive post-recognition. With flows feed missing (H3) we cannot locate the position on
        the curve. A3 is the highest-value structural adjustment regardless of capital adjustments selected.
  feed_gaps_promoted_to_assumptions:
    - { gap: "FRED feed missing", proxy: "ETF/FX commodities-fx + news-summarizer FOMC", confidence_haircut: 0.30 }
    - { gap: "EDGAR feed stub-only", proxy: "qualitative valuation + price action", confidence_haircut: 0.20 }
    - { gap: "no flows / positioning feed", proxy: "first-principles reasoning", confidence_haircut: 0.25 }
    - { gap: "no live broker feed", proxy: "hand-snapshot from sibling inquiries", confidence_haircut: 0.15 }
  provenance:
    source: inquiry.2026-05-08-portfolio-architecture
    timestamp: 2026-05-08T06:00:00Z
  fuzz_halo: >
    snapshot only; reframable per inquiry. Three proposed amendments today (factor-coverage-checklist,
    feed-gap-promotes-to-assumption, world-frame-first) applied here pre-ratification; subject to revision
    on amendment status change. Confidence on architecture as a whole ~0.55; on hole identification ~0.7;
    on probability weights ~0.45 (per-scenario calibration band +/-10pp).
```
