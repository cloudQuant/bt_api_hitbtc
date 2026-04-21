"""Tests for HitbtcExchangeData container."""

from __future__ import annotations

from bt_api_hitbtc.exchange_data import HitBtcExchangeData


class TestHitBtcExchangeData:
    """Tests for HitBtcExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = HitBtcExchangeData()

        assert exchange.exchange_name == "HITBTC"
