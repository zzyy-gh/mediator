# Methods — Available, Not Required

Toolbox for Probe and Collapse, framed as available components. Pull what serves the objective; drop what is redundant. None of these are prescribed; all are situational.

For each method: when it helps, when it misleads.

## Sizing

- **Kelly** — sizes to maximize log-wealth growth given known edge and odds. Helps when edge and variance are decently estimated. Misleads when edge is overestimated or distribution is fat-tailed; haircut accordingly.
- **Vol-targeting** — sizes inversely to realized vol. Helps for steady risk budget; misleads on regime breaks.
- **Fixed fractional** — sizes by fraction of NAV. Helps for simplicity; ignores edge variation.
- **Risk-parity** — equal risk contribution across positions. Helps diversify; misleads when correlations break.

## Risk measurement

- **VaR / CVaR** — quantile / tail-conditional loss. Helps frame tails; misleads under non-stationary tails.
- **Drawdown bound** — maximum acceptable peak-to-trough. Helps as hard stop.
- **Stress scenarios** — handpicked regime shocks. Helps when history is thin or biased.
- **Factor exposure** — implicit-bet detection. Helps reveal what you are *actually* betting on.

## Return modelling

- **Bayesian shrinkage** (James-Stein, Ledoit-Wolf) — pulls noisy estimates toward a prior. Helps when sample is small.
- **Black-Litterman** — blends equilibrium prior with explicit views. Helps when views are well-articulated.
- **Factor models** (Fama-French, Carhart, Barra) — decompose returns. Helps with attribution and exposure.
- **Cointegration** — stationary spread between non-stationary series. Helps for pair / basket trades.
- **HMM regime detection** — Markov-switching for regime classification. Helps when regimes are real and persistent.

## Frameworks worth knowing

- **Multi-manager pod** (Citadel, Millennium, Point72) — central risk, decentralized PMs.
- **Bridgewater Pure Alpha** — systematic with discretionary regime overrides.
- **Renaissance Medallion** — short-horizon statistical arbitrage.
- **AQR / DFA** — academic-factor systematic.

## Data sources

- Bloomberg, Refinitiv, FactSet — institutional terminals.
- IEX, Polygon, Alpaca — retail / dev APIs.
- SEC EDGAR — filings.
- FRED — macro series.
- CBOE — options and vol.

## Behavioral lenses

- Kahneman / Tversky biases: anchoring, recency, narrative, disposition, loss aversion.
- Soros reflexivity — feedback between beliefs and prices.
