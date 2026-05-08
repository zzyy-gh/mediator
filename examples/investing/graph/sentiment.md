# Sentiment Nodes

Surveys, news tone, social signal, analyst tone, narrative momentum. Updated by sentiment feeds (LLM summarization or scored feeds).

## Example

```yaml
- id: sentiment.tech-narrative
  topic: sentiment
  content: "AI capex enthusiasm cooling but still positive net"
  distribution:
    shape: bounded
    params:
      range: [-1, 1]
      mean: 0.3
      sd: 0.2
  confidence: 0.5
  provenance:
    source: feed.news-summarizer
    timestamp: 2026-05-08T00:00:00Z
  fuzz_halo: "narrative-shift risk on next print"
```

_(Hydrate as feeds come online.)_
