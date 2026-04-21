from __future__ import annotations

from typing import Any

from bt_api_base.balance_utils import simple_balance_handler as _hitbtc_balance_handler
from bt_api_hitbtc.exchange_data import HitBtcExchangeDataSpot
from bt_api_hitbtc.feeds.live_hitbtc.spot import HitBtcSpotRequestData
from bt_api_base.registry import ExchangeRegistry


def register_hitbtc(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("HITBTC___SPOT", HitBtcSpotRequestData)
    registry.register_exchange_data("HITBTC___SPOT", HitBtcExchangeDataSpot)
    registry.register_balance_handler("HITBTC___SPOT", _hitbtc_balance_handler)
