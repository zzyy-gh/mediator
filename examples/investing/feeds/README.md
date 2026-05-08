# Feeds

Specs for data sources that hydrate the graph. Each feed is registered via a feed-Collapse inquiry — see `architecture.md`.

## File shape

One file per feed: `feeds/<source>.md`. Suggested sections:

```yaml
---
id: feed.<source>
status: proposed | active | deprecated
target_nodes: [graph_topic]          # which graph file(s) it writes
cadence: <interval or event>
latency: <expected lag>
quality:
  coverage: ...
  accuracy: ...
  history: ...
cost: ...
provenance:
  registered_by_inquiry: <id>
  reviewed_at: ISO8601
---
```

## Lifecycle

A feed is requested via a feed-flavour inquiry. The inquiry's feasibility-gate covers:
- access (legal, technical, account)
- cost (subscription, rate-limit, infra)
- latency (decision-relevance)
- quality (provenance, accuracy, completeness)
- quantity (history length, breadth, frequency)

On Collapse, the feed entry lands here and the runner starts hydrating its target graph nodes.

## Active feeds

_(empty — feeds register here as they are accepted.)_
