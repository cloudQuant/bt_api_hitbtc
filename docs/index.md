# HITBTC Documentation

## English

Welcome to the HITBTC documentation for bt_api.

### Quick Start

```bash
pip install bt_api_hitbtc
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "HITBTC___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("HITBTC___SPOT", "BTCUSDT")
print(ticker)
```

## 中文

欢迎使用 bt_api 的 HITBTC 文档。

### 快速开始

```bash
pip install bt_api_hitbtc
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "HITBTC___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("HITBTC___SPOT", "BTCUSDT")
print(ticker)
```

## API Reference

See source code in `src/bt_api_hitbtc/` for detailed API documentation.
