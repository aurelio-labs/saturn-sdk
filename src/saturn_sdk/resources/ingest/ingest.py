# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .url import (
    URLResource,
    AsyncURLResource,
    URLResourceWithRawResponse,
    AsyncURLResourceWithRawResponse,
    URLResourceWithStreamingResponse,
    AsyncURLResourceWithStreamingResponse,
)
from .document import (
    DocumentResource,
    AsyncDocumentResource,
    DocumentResourceWithRawResponse,
    AsyncDocumentResourceWithRawResponse,
    DocumentResourceWithStreamingResponse,
    AsyncDocumentResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["IngestResource", "AsyncIngestResource"]


class IngestResource(SyncAPIResource):
    @cached_property
    def document(self) -> DocumentResource:
        return DocumentResource(self._client)

    @cached_property
    def url(self) -> URLResource:
        return URLResource(self._client)

    @cached_property
    def with_raw_response(self) -> IngestResourceWithRawResponse:
        return IngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IngestResourceWithStreamingResponse:
        return IngestResourceWithStreamingResponse(self)


class AsyncIngestResource(AsyncAPIResource):
    @cached_property
    def document(self) -> AsyncDocumentResource:
        return AsyncDocumentResource(self._client)

    @cached_property
    def url(self) -> AsyncURLResource:
        return AsyncURLResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIngestResourceWithRawResponse:
        return AsyncIngestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIngestResourceWithStreamingResponse:
        return AsyncIngestResourceWithStreamingResponse(self)


class IngestResourceWithRawResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

    @cached_property
    def document(self) -> DocumentResourceWithRawResponse:
        return DocumentResourceWithRawResponse(self._ingest.document)

    @cached_property
    def url(self) -> URLResourceWithRawResponse:
        return URLResourceWithRawResponse(self._ingest.url)


class AsyncIngestResourceWithRawResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

    @cached_property
    def document(self) -> AsyncDocumentResourceWithRawResponse:
        return AsyncDocumentResourceWithRawResponse(self._ingest.document)

    @cached_property
    def url(self) -> AsyncURLResourceWithRawResponse:
        return AsyncURLResourceWithRawResponse(self._ingest.url)


class IngestResourceWithStreamingResponse:
    def __init__(self, ingest: IngestResource) -> None:
        self._ingest = ingest

    @cached_property
    def document(self) -> DocumentResourceWithStreamingResponse:
        return DocumentResourceWithStreamingResponse(self._ingest.document)

    @cached_property
    def url(self) -> URLResourceWithStreamingResponse:
        return URLResourceWithStreamingResponse(self._ingest.url)


class AsyncIngestResourceWithStreamingResponse:
    def __init__(self, ingest: AsyncIngestResource) -> None:
        self._ingest = ingest

    @cached_property
    def document(self) -> AsyncDocumentResourceWithStreamingResponse:
        return AsyncDocumentResourceWithStreamingResponse(self._ingest.document)

    @cached_property
    def url(self) -> AsyncURLResourceWithStreamingResponse:
        return AsyncURLResourceWithStreamingResponse(self._ingest.url)
