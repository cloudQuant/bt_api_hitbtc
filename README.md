# bt_api_hitbtc

HitBTC exchange plugin for `bt_api`, supporting Spot trading.

## Installation

```bash
pip install bt_api_hitbtc
```

## Usage

```python
from bt_api_hitbtc import HitBtcSpotRequestData

feed = HitBtcSpotRequestData(public_key="your_key", private_key="your_secret")
ticker = feed.get_ticker("BTCUSDT")
```

## Architecture

```
bt_api_hitbtc/
├── exchange_data/         # Exchange configuration and REST/WSS paths
├── errors/               # Error translator
├── tickers/              # Ticker data container
├── feeds/live_hitbtc/    # REST API implementation
└── plugin.py             # PluginInfo registration
```