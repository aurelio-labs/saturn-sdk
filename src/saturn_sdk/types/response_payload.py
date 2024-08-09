# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ResponsePayload", "Data", "DataChunk", "DataDocument"]


class DataChunk(BaseModel):
    id: str

    content: str

    document_id: str

    chunk_index: Optional[int] = None

    doc_url: Optional[str] = None

    metadata: Optional[object] = None

    source: Optional[str] = None

    source_type: Optional[str] = None

    token_count: Optional[int] = None


class DataDocument(BaseModel):
    id: str

    content: str

    doc_url: Optional[str] = None

    metadata: Optional[object] = None

    source: Optional[str] = None

    source_type: Optional[str] = None

    title: Optional[str] = None


class Data(BaseModel):
    chunks: List[DataChunk]

    document: DataDocument


class ResponsePayload(BaseModel):
    success: bool

    data: Optional[Data] = None

    message: Optional[str] = None
