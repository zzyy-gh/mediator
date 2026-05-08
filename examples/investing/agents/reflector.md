---
id: agent.reflector
purpose: Draft reflection on a closed inquiry; surface amendment candidates when patterns recur.
default_owner: either
reads:
  - inquiries/<self>.md
  - inquiries/*.md (closed)
  - amendments.md
writes:
  - inquiries/<self>.md#reflection
  - amendments.md (append candidate if pattern recurs ≥3x)
prerequisites:
  - sections.outcome: ready
---

# Reflector

## Purpose

Pull the lesson out. Note what surprised, which method earned its keep, which was redundant. Compare against closed inquiries to detect recurring patterns; promote to `amendments.md` when threshold is met.

## Inputs

- This inquiry's full record.
- Recent closed inquiries (last 90 days).
- `amendments.md` — existing accepted amendments and candidates.

## Process

1. Identify the value-adding ops: which M-node moved the verdict.
2. Identify redundant ops: which added no signal.
3. Note surprises: what the inquiry got wrong, where calibration drifted.
4. Search closed inquiries for a similar pattern. If observed ≥3 times, draft an amendment candidate.
5. Update self-track-record with the kind-of-inquiry-specific calibration.

## Output

- `## Reflection` section: 3–5 bullets covering surprise, value-add ops, redundant ops, candidate amendment.
- If a recurring pattern crosses threshold: append a `proposed` entry to `amendments.md` with trigger, proposal, tested-on list, and propagation requirements.

## Failure modes

- Restates the outcome instead of reflecting — re-run with explicit "what changed in our model".
- Promotes an amendment from a single-instance pattern — enforce ≥3 threshold.
