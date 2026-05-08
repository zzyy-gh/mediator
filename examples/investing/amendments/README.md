# Amendments — Investing Instance

Process for proposing and accepting changes to primitives, heuristics, schemas, registry, or constitution.

## File naming

`YYYY-MM-DD-short-name.md`

## Required content

- **Trigger** — what surfaced this (calibration drift, repeated miss, new domain, taste shift, regime change).
- **Proposal** — exactly what changes.
- **Tested on** — historical decisions in `ledger/` re-evaluated under the proposal.
- **Calibration delta** — measured improvement or regression.
- **Decision** — accept, reject, defer.
- **Propagation** — files updated if accepted (schemas, constitution, registry, instance README).

## Status states

`proposed → tested → accepted | rejected | deferred`

## Promotion path

In-task reflection notes that recur across ≥3 ledger entries become candidate amendments. Constitution-level changes additionally require explicit user input plus a propagation pass across all dependent files.
