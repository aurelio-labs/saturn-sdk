# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from saturn_sdk import SaturnSDK, AsyncSaturnSDK
from tests.utils import assert_matches_type
from saturn_sdk.types import ResponsePayload

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocument:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_process(self, client: SaturnSDK) -> None:
        document = client.ingest.document.process(
            file=b"raw file contents",
        )
        assert_matches_type(ResponsePayload, document, path=["response"])

    @parametrize
    def test_method_process_with_all_params(self, client: SaturnSDK) -> None:
        document = client.ingest.document.process(
            file=b"raw file contents",
            chunk=True,
            quality="high",
        )
        assert_matches_type(ResponsePayload, document, path=["response"])

    @parametrize
    def test_raw_response_process(self, client: SaturnSDK) -> None:
        response = client.ingest.document.with_raw_response.process(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(ResponsePayload, document, path=["response"])

    @parametrize
    def test_streaming_response_process(self, client: SaturnSDK) -> None:
        with client.ingest.document.with_streaming_response.process(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(ResponsePayload, document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocument:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_process(self, async_client: AsyncSaturnSDK) -> None:
        document = await async_client.ingest.document.process(
            file=b"raw file contents",
        )
        assert_matches_type(ResponsePayload, document, path=["response"])

    @parametrize
    async def test_method_process_with_all_params(self, async_client: AsyncSaturnSDK) -> None:
        document = await async_client.ingest.document.process(
            file=b"raw file contents",
            chunk=True,
            quality="high",
        )
        assert_matches_type(ResponsePayload, document, path=["response"])

    @parametrize
    async def test_raw_response_process(self, async_client: AsyncSaturnSDK) -> None:
        response = await async_client.ingest.document.with_raw_response.process(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(ResponsePayload, document, path=["response"])

    @parametrize
    async def test_streaming_response_process(self, async_client: AsyncSaturnSDK) -> None:
        async with async_client.ingest.document.with_streaming_response.process(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(ResponsePayload, document, path=["response"])

        assert cast(Any, response.is_closed) is True
