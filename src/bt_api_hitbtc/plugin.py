from __future__ import annotations

from bt_api_base.plugins.protocol import PluginInfo
from bt_api_base.registry import ExchangeRegistry

from bt_api_hitbtc import __version__
from bt_api_hitbtc.registry_registration import register_hitbtc


def register_plugin(registry: type[ExchangeRegistry], runtime_factory=None) -> PluginInfo:
    register_hitbtc(registry)

    return PluginInfo(
        name="bt_api_hitbtc",
        version=__version__,
        core_requires=">=0.15,<1.0",
        supported_exchanges=("HITBTC___SPOT",),
        supported_asset_types=("SPOT",),
    )
