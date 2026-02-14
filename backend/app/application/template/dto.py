"""
Template Application DTO
"""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class ImportFromGoogleSlidesDTO(BaseModel):
    presentation_url: str


class UpdateTemplateDTO(BaseModel):
    title: Optional[str] = None
    contents: Optional[Any] = None


# ── Response ──────────────────────────────────────────


class TemplateResponseDTO(BaseModel):
    id: str
    owner_id: str
    title: str
    contents: Any
    thumbnail_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class TemplateListItemDTO(BaseModel):
    id: str
    title: str
    thumbnail_url: Optional[str] = None
    created_at: datetime
