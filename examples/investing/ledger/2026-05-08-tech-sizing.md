# Decision: Tech sector sizing under elevated vol

**Date:** 2026-05-08
**Status:** open
**Outcome window:** 2026-08-08 (3 months)

## S-nodes

### Intent
- `intent.tech-sizing` — Decide whether to scale tech allocation from 18% → 25% NAV. Confidence: 0.5. Fuzz: target sizing precision is fuzzy by ±3%.

### World
- `world.vol-regime` — VIX 22, 30d realized 19%. Mid-elevated, not panic. Provenance: CBOE 2026-05-07.
- `world.tech-earnings` — Q1 reported, beats 68% of names, guide-down on 22%. Provenance: FactSet 2026-05-06.
- `world.rates` — 10y at 4.6%, Fed pause ongoing. Provenance: FRED.
- `world.crowding` — HF tech net long at 75th percentile. Provenance: prime broker positioning report.

### Self
- `self.capability` — Single-stock pickers in tech: 4 names with conviction. Sizing model: confidence-haircut Kelly.
- `self.taste` — Tilt toward platforms with installed-base moats; underweight thematic momentum.
- `self.track-record` — Last 3 tech sizing calls: +1, -1, +1. Calibration on tech sizing: ~0.55.

## M-nodes

1. `m.probe.prior-art` — Consult `registry/tools.md`. Run factor exposure check. Tech tilt resolves to: HML negative, MKT +1.1, MOM +0.3. Already running an implicit factor bet.
2. `m.probe.world` — Check crowding via prime broker positioning. Result: crowded.
3. `m.reframe` — Reframe from "size up tech" to "size up two highest-conviction names within current 18% sleeve". Avoid sector-level bet given crowding + implicit factor exposure.
4. `m.test.feasibility` — Capability ✓ (research bandwidth available). Constraint ✓ (within mandate). Budget ✓ (no leverage needed). Pass.
5. `m.collapse` — Commit: rebalance within sleeve, no sector size-up. Two top names from 4% → 6%, funded from low-conviction trim.

## Predictions logged

- Tech sleeve return vs SPY over 3 months: +50bps. Confidence: 0.6.
- Top-2 names beat sleeve average: 0.55.

## Outcome

_Pending. Fill on 2026-08-08._

## Reflection note

Probe.world surfaced crowding I would have missed. The Reframe op was the actual value-add — saved a sector-level bet for a within-sleeve rebalance. In-task patch candidate: add "crowding probe" as standard pre-Collapse for any sizing decision >2% NAV. Promote to `amendments/` if pattern recurs across ≥3 entries.
