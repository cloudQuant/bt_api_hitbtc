from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class HitBtcExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "HITBTC"
        self.rest_url = "https://api.hitbtc.com/api/3"
        self.wss_url = "wss://api.hitbtc.com/api/3/ws/public"
        self.legal_currency = ["USDT", "BTC", "ETH"]
        self.kline_periods = {
            "1m": "M1",
            "3m": "M3",
            "5m": "M5",
            "15m": "M15",
            "30m": "M30",
            "1h": "H1",
            "2h": "H2",
            "4h": "H4",
            "1d": "D1",
            "1w": "D7",
            "1M": "1M",
        }
        self.rest_paths = {}
        self.wss_paths = {}

    def get_rest_path(self, key: str, **kwargs) -> str:
        path = self.rest_paths.get(key)
        if path is None:
            raise ValueError(f"Unknown REST path key: {key}")
        return path

    def get_wss_path(self, channel: str, **kwargs) -> str:
        path = self.wss_paths.get(channel)
        if path is None:
            raise ValueError(f"Unknown WSS channel: {channel}")
        return path

    def get_symbol(self, symbol: str) -> str:
        return symbol.upper().replace("/", "").replace("-", "")

    def get_period(self, period: str) -> str:
        return self.kline_periods.get(period.lower(), period.upper())


class HitBtcExchangeDataSpot(HitBtcExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"
        self.exchange_name = "HITBTC___SPOT"
        self.rest_paths = {
            "get_server_time": "GET /public/time",
            "get_exchange_info": "GET /public/symbol",
            "get_tick": "GET /public/ticker/{symbol}",
            "get_tick_all": "GET /public/ticker",
            "get_depth": "GET /public/orderbook/{symbol}",
            "get_trades": "GET /public/trades/{symbol}",
            "get_kline": "GET /public/candles/{symbol}",
            "make_order": "POST /spot/order",
            "cancel_order": "DELETE /spot/order/{client_order_id}",
            "cancel_all_orders": "DELETE /spot/order",
            "get_open_orders": "GET /spot/order",
            "query_order": "GET /spot/order/{client_order_id}",
            "get_order_history": "GET /spot/history/order",
            "get_trades_history": "GET /spot/history/trade",
            "get_balance": "GET /spot/balance",
            "get_account": "GET /spot/balance",
        }
        self.wss_paths = {
            "ticker": "ticker/1s",
            "orderbook": "orderbook/full",
            "trades": "trades",
            "candles": "candles",
        }
