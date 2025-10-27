"""
API routes for managing sources.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from backend.models import Source, get_db, CredibilityTier

router = APIRouter()


class SourceCreate(BaseModel):
    url: str
    title: str
    credibility_tier: str = "tier_3"
    region: str | None = None
    language: str | None = None
    publisher: str | None = None


class SourceResponse(BaseModel):
    id: int
    url: str
    title: str
    credibility_tier: str
    region: str | None
    language: str | None
    publisher: str | None

    class Config:
        from_attributes = True


@router.get("/", response_model=List[SourceResponse])
async def list_sources(
    region: str | None = None,
    tier: str | None = None,
    db: Session = Depends(get_db)
):
    """List all sources with optional filtering."""
    query = db.query(Source)

    if region:
        query = query.filter(Source.region == region)
    if tier:
        query = query.filter(Source.credibility_tier == CredibilityTier[tier.upper()])

    sources = query.all()
    return sources


@router.get("/{source_id}", response_model=SourceResponse)
async def get_source(source_id: int, db: Session = Depends(get_db)):
    """Get a single source."""
    source = db.query(Source).filter(Source.id == source_id).first()
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    return source


@router.post("/", response_model=SourceResponse)
async def create_source(source: SourceCreate, db: Session = Depends(get_db)):
    """Create a new source."""
    db_source = Source(
        url=source.url,
        title=source.title,
        credibility_tier=CredibilityTier[source.credibility_tier.upper()],
        region=source.region,
        language=source.language,
        publisher=source.publisher
    )
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source
