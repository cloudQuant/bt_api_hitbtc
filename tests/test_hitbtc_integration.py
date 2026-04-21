"""
HitBTC Integration Tests

This module provides basic tests for HitBTC exchange integration.
Tests basic functionality without requiring API keys.
"""

from __future__ import annotations

import pytest

from bt_api_hitbtc.exchange_data import HitBtcExchangeDataSpot
from bt_api_hitbtc.tickers import HitBtcRequestTickerData
from bt_api_hitbtc.registry_registration import register_hitbtc


class TestHitBtcFeedRegistration:
    """Test HitBTC feed registration"""

    def test_register_hitbtc(self):
        """Test that HitBTC feeds are registered correctly"""
        from bt_api_base.registry import ExchangeRegistry

        register_hitbtc(ExchangeRegistry)

        assert ExchangeRegistry.has_exchange("HITBTC___SPOT")


class TestHitBtcExchangeData:
    """Test HitBTC exchange data container"""

    def test_exchange_data_initialization(self):
        """Test exchange data initialization"""
        data = HitBtcExchangeDataSpot()

        assert data.exchange_name == "HITBTC___SPOT"
        assert data.asset_type == "SPOT"
        assert data.rest_url == "https://api.hitbtc.com/api/3"
        assert data.wss_url == "wss://api.hitbtc.com/api/3/ws/public"

    def test_get_rest_path(self):
        """Test REST path generation"""
        data = HitBtcExchangeDataSpot()

        path = data.get_rest_path("get_tick")
        assert "/public/ticker/" in path

        path = data.get_rest_path("make_order")
        assert "/spot/order" in path

        assert data.get_symbol("BTC/USDT") == "BTCUSDT"
        assert data.get_symbol("btcusdt") == "BTCUSDT"

    def test_get_period_conversion(self):
        """Test period conversion"""
        data = HitBtcExchangeDataSpot()

        assert data.get_period("1m") == "M1"
        assert data.get_period("5m") == "M5"
        assert data.get_period("1h") == "H1"
        assert data.get_period("1d") == "D1"


class TestHitBtcDataContainers:
    """Test HitBTC data containers"""

    @pytest.mark.ticker
    def test_ticker_data(self):
        """Test ticker data container"""
        ticker_info = {
            "symbol": "BTCUSDT",
            "last": "50000.0",
            "bid": "49900.0",
            "ask": "50100.0",
            "volume": "1.5",
            "high": "51000.0",
            "low": "48000.0",
            "open": "49000.0",
            "timestamp": 1640995200000,
            "count": 100,
        }

        ticker = HitBtcRequestTickerData(ticker_info, "BTC/USDT", "SPOT")
        ticker.init_data()

        assert ticker.symbol_name == "BTC/USDT"
        assert ticker.last_price == 50000.0
        assert ticker.bid_price == 49900.0
        assert ticker.ask_price == 50100.0
        assert ticker.high_price == 51000.0
        assert ticker.low_price == 48000.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
