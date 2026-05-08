---
id: feed.news-summarizer
status: proposed
target_nodes:
  - graph/sentiment.md
  - graph/themes.md
  - graph/politics.md
cadence: hourly
latency: minutes
quality:
  coverage: configurable RSS / curated URL list — broad if list is broad
  accuracy: medium — LLM summarisation; tag with confidence and provenance
  history: rolling window (last 7d default; archive optional)
cost: free for sources; LLM-token cost for summarisation
provenance:
  registered_by_inquiry: <pending>
  reviewed_at: null
---

# Feed — News Summarizer

LLM-based feed that ingests RSS and curated URL lists, summarises into structured graph nodes, and tags themes / sentiment / political-news.

## Reads

- Configurable RSS feed list (top-tier business and macro outlets, sector specialists, central bank sites, regulatory sources).
- Curated URL list for one-off scrapes.

## Writes

- `graph/sentiment.md` — bounded-distribution sentiment nodes per topic.
- `graph/themes.md` — theme nodes when narrative momentum or new arc is detected.
- `graph/politics.md` — discrete-distribution event nodes.

## Implementation

`orchestrator/feeds/news_summarizer.py`. Uses the Claude Agent SDK as the summarisation engine. Writes only structured nodes; raw text not persisted in graph (links retained in provenance).

## Caveats

- LLM summarisation introduces fuzz; record `fuzz_halo` and provenance per node.
- Sources should be diverse enough to avoid single-outlet bias.
- Re-summarisation policy: do not overwrite a node within a configured window unless material change is detected; instead append.
