# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.ingest import url_process_params
from ...types.response_payload import ResponsePayload

__all__ = ["URLResource", "AsyncURLResource"]


class URLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLResourceWithRawResponse:
        return URLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLResourceWithStreamingResponse:
        return URLResourceWithStreamingResponse(self)

    def process(
        self,
        *,
        url: str,
        chunk: bool | NotGiven = NOT_GIVEN,
        quality: Literal["high", "low"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponsePayload:
        """
        Process a file from a URL.

        Args:
          url: The URLs of the document files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/ingest/url",
            body=maybe_transform({"url": url}, url_process_params.URLProcessParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "chunk": chunk,
                        "quality": quality,
                    },
                    url_process_params.URLProcessParams,
                ),
            ),
            cast_to=ResponsePayload,
        )


class AsyncURLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLResourceWithRawResponse:
        return AsyncURLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLResourceWithStreamingResponse:
        return AsyncURLResourceWithStreamingResponse(self)

    async def process(
        self,
        *,
        url: str,
        chunk: bool | NotGiven = NOT_GIVEN,
        quality: Literal["high", "low"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponsePayload:
        """
        Process a file from a URL.

        Args:
          url: The URLs of the document files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/ingest/url",
            body=await async_maybe_transform({"url": url}, url_process_params.URLProcessParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "chunk": chunk,
                        "quality": quality,
                    },
                    url_process_params.URLProcessParams,
                ),
            ),
            cast_to=ResponsePayload,
        )


class URLResourceWithRawResponse:
    def __init__(self, url: URLResource) -> None:
        self._url = url

        self.process = to_raw_response_wrapper(
            url.process,
        )


class AsyncURLResourceWithRawResponse:
    def __init__(self, url: AsyncURLResource) -> None:
        self._url = url

        self.process = async_to_raw_response_wrapper(
            url.process,
        )


class URLResourceWithStreamingResponse:
    def __init__(self, url: URLResource) -> None:
        self._url = url

        self.process = to_streamed_response_wrapper(
            url.process,
        )


class AsyncURLResourceWithStreamingResponse:
    def __init__(self, url: AsyncURLResource) -> None:
        self._url = url

        self.process = async_to_streamed_response_wrapper(
            url.process,
        )
