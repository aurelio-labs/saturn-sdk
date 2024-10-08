# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import FileTypes

__all__ = ["DocumentProcessParams"]


class DocumentProcessParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to ingest."""

    chunk: bool

    quality: Literal["high", "low"]
