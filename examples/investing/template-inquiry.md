# Inquiry Template

Each entry in `inquiries/` follows this shape. Sections are independently fillable — agent or human can populate any block. Status fields drive orchestration.

---

```yaml
---
id: YYYY-MM-DD-name
shape: convergent | divergent
collapse_flavour: capital | belief | feed
status: open
scope: <one-line>
parent_inquiry: <id or null>
graph_snapshot: <snapshot ref>
outcome_window: YYYY-MM-DD
sections:
  scope: ready
  assumptions: pending
  graph_refs: pending
  intent: pending
  self: pending
  m_nodes: pending
  prediction: pending
  outcome: locked
  reflection: locked
owner: either
---
```

# Inquiry: [name]

## Scope

Sharp framing. What this inquiry is, what it is not. In-scope vs deliberately deferred.

## Assumptions (load-bearing)

Numbered, falsifiable claims that must hold for the analysis to be valid.

1. ...
2. ...

## Graph references

Nodes pulled from the snapshot, by id, that this inquiry reasons over. Add or remove during probe.

- `macro.<id>` — ...
- `flows.<id>` — ...
- `themes.<id>` — ...

## Intent

Goal in one sentence, with confidence or distribution.

## Self

- `self.capability` — what we can actually execute.
- `self.calibration` — track record on this kind of inquiry.
- `self.taste` — known leanings relevant here.

## M-nodes (sequence)

1. `m.probe.scope` — sharpen scope.
2. `m.probe.prior-art` — consult `methods.md`, `blind-spots.md`, related closed inquiries.
3. `m.probe.world` — fill graph gaps via feeds; spawn a feed-inquiry if data is missing.
4. `m.probe.edges` — walk relevant edges; flag implicit dependencies.
5. `m.reframe` — only if scope or assumptions need it.
6. `m.test.feasibility` — capability × constraint × budget × data-quality.
7. `m.collapse` — commit one of: capital | belief | feed.

## Output

**Convergent:**
- **Expected return** — distribution sketch (shape + key params or quantiles).
- **Expected risk** — loss distribution, drawdown bound, tail behaviour.
- **E[R] / E[risk] ratio** — explicit number, the optimization target.
- **Sensitivity** — which assumption or edge, if violated, breaks the verdict.

**Divergent:**
- **Output artifact** — ranked list, scenario tree, or candidate set, written to `graph/<topic>.md` with provenance pointing back to this inquiry.
- **Per-candidate** — short rationale, sensitivity, suggested child inquiry id.

## Outcome

Filled at outcome window.

- Realized state:
- Calibration delta:
- Edges affected:

## Reflection

What surprised. Which method earned its keep. Which was redundant. Candidate amendment if a pattern is forming.
