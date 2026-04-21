from unittest.mock import AsyncMock
import pytest
from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_hitbtc.feeds.live_hitbtc.request_base import HitBtcRequestData


async def test_hitbtc_async_request_allows_missing_extra_data(monkeypatch) -> None:
    request_data = HitBtcRequestData(
        public_key="public-key",
        private_key="secret-key",
        exchange_name="HITBTC___SPOT",
    )

    async_request_mock = AsyncMock(return_value={"timestamp": "2024-01-01T00:00:00.000Z"})
    monkeypatch.setattr(request_data, "async_http_request", async_request_mock)

    result = await request_data.async_request("GET /api/3/public/time")

    assert isinstance(result, RequestData)
    assert result.get_extra_data() == {}
    assert result.get_input_data() == {"timestamp": "2024-01-01T00:00:00.000Z"}
