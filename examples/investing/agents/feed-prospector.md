---
id: agent.feed-prospector
purpose: When a data gap surfaces, draft a feed-flavour inquiry with feasibility analysis.
default_owner: agent
reads:
  - feeds/*.md
  - graph/*.md
writes:
  - inquiries/<new>.md (creates a new feed-flavour inquiry)
prerequisites:
  - triggered by probe-world or any agent flagging a data gap
spawns:
  - feed-inquiry
---

# Feed Prospector

## Purpose

Convert a data gap into a feed-flavour inquiry that can be evaluated through the standard lifecycle. Stays cheap, free-first, and explicit about quality vs cost.

## Inputs

- The triggering gap description (which graph node, what kind of data, why needed).
- Existing `feeds/*.md` to avoid duplication.

## Process

1. Identify candidate data sources. Free-first: yfinance, FRED, EDGAR, CoinGecko, RSS, public APIs, scraped LLM-summarised text.
2. For each candidate, assess:
   - Access (legal, technical, account requirements).
   - Cost (subscription, rate-limit, infra).
   - Latency (decision-relevance).
   - Quality (provenance, accuracy, completeness).
   - Quantity (history length, breadth, frequency).
3. Recommend the cheapest source meeting the inquiry need; flag if no free source qualifies.
4. Draft a new feed-flavour inquiry file with a populated feasibility section.

## Output

A new `inquiries/<date>-feed-<source>.md` file ready for human Collapse. The new inquiry references the gap-triggering inquiry as parent.

## Failure modes

- Defaults to paid sources — re-run with free-first constraint.
- Recommends without evaluating quality or coverage — fields must be filled.
