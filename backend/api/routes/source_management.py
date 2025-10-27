"""
Source management utilities for populating and validating sources.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from pydantic import BaseModel, HttpUrl, validator
import logging
from urllib.parse import urlparse

from backend.models import get_db, Source, Perspective, Event
from backend.models.models import CredibilityTier
from backend.cache import invalidate_cache

logger = logging.getLogger(__name__)
router = APIRouter()


class SourceCreate(BaseModel):
    """Schema for creating a source with validation."""
    url: HttpUrl
    title: str
    credibility_tier: str = "tier_3"
    region: str | None = None
    language: str | None = None
    publisher: str | None = None

    @validator('url')
    def validate_url(cls, v):
        """Validate URL format."""
        parsed = urlparse(str(v))
        if not parsed.scheme or not parsed.netloc:
            raise ValueError('Invalid URL format')
        return str(v)

    @validator('credibility_tier')
    def validate_tier(cls, v):
        """Validate credibility tier."""
        valid_tiers = ['tier_1', 'tier_2', 'tier_3', 'tier_4']
        if v not in valid_tiers:
            raise ValueError(f'Invalid tier. Must be one of: {valid_tiers}')
        return v


@router.post("/extract-from-perspectives")
async def extract_sources_from_perspectives(db: Session = Depends(get_db)):
    """
    Extract source URLs from existing perspective data and create Source records.

    This is a utility endpoint to populate the source library from existing data.
    """
    logger.info("Starting source extraction from perspectives")

    # Get all perspectives
    perspectives = db.query(Perspective).all()

    created_sources = []
    skipped_count = 0

    for perspective in perspectives:
        # Check if perspective has sources already linked
        if perspective.sources:
            logger.debug(f"Perspective {perspective.id} already has sources linked")
            continue

        # Try to extract source info from perspective data
        # This is a placeholder - in real usage, you'd parse from summary/key_points
        # or have source data stored separately

        # For now, create a placeholder source for each perspective
        # You should modify this to match your actual data structure
        if perspective.summary:
            # Generate a source URL based on region (placeholder)
            source_url = f"https://example.com/source/{perspective.region.lower().replace(' ', '-')}"

            # Check if source already exists
            existing = db.query(Source).filter(Source.url == source_url).first()
            if existing:
                logger.debug(f"Source already exists: {source_url}")
                skipped_count += 1
                continue

            # Create source
            source = Source(
                url=source_url,
                title=f"{perspective.region} Source - {perspective.event.title[:50]}",
                credibility_tier=CredibilityTier.TIER_2,
                region=perspective.region,
                language=perspective.language
            )
            db.add(source)
            db.flush()  # Get the source ID

            # Link to perspective
            perspective.sources.append(source)

            created_sources.append({
                'source_id': source.id,
                'url': source.url,
                'perspective_id': perspective.id
            })

    db.commit()

    # Invalidate cache
    invalidate_cache("stats:*")

    logger.info(f"Source extraction complete: {len(created_sources)} created, {skipped_count} skipped")

    return {
        'created_count': len(created_sources),
        'skipped_count': skipped_count,
        'sources': created_sources
    }


@router.post("/validate-sources")
async def validate_all_sources(db: Session = Depends(get_db)):
    """
    Validate all sources in the database.

    Returns list of invalid or duplicate sources.
    """
    logger.info("Starting source validation")

    sources = db.query(Source).all()

    issues = []
    seen_urls = {}

    for source in sources:
        # Check for duplicates
        if source.url in seen_urls:
            issues.append({
                'source_id': source.id,
                'url': source.url,
                'issue': 'duplicate',
                'duplicate_of': seen_urls[source.url]
            })
        else:
            seen_urls[source.url] = source.id

        # Validate URL format
        try:
            parsed = urlparse(source.url)
            if not parsed.scheme or not parsed.netloc:
                issues.append({
                    'source_id': source.id,
                    'url': source.url,
                    'issue': 'invalid_url_format'
                })
        except Exception as e:
            issues.append({
                'source_id': source.id,
                'url': source.url,
                'issue': 'parse_error',
                'error': str(e)
            })

    logger.info(f"Source validation complete: {len(issues)} issues found")

    return {
        'total_sources': len(sources),
        'issues_found': len(issues),
        'issues': issues
    }


@router.delete("/remove-duplicates")
async def remove_duplicate_sources(db: Session = Depends(get_db)):
    """
    Remove duplicate sources, keeping the oldest one.
    """
    logger.info("Starting duplicate source removal")

    # Find duplicates
    from sqlalchemy import func
    duplicates = db.query(
        Source.url,
        func.count(Source.id).label('count'),
        func.min(Source.id).label('keep_id')
    ).group_by(Source.url).having(func.count(Source.id) > 1).all()

    removed_count = 0

    for url, count, keep_id in duplicates:
        # Get all sources with this URL
        sources = db.query(Source).filter(Source.url == url).all()

        # Remove all except the one to keep
        for source in sources:
            if source.id != keep_id:
                db.delete(source)
                removed_count += 1
                logger.debug(f"Removed duplicate source {source.id}: {url}")

    db.commit()

    # Invalidate cache
    invalidate_cache("stats:*")

    logger.info(f"Duplicate removal complete: {removed_count} duplicates removed")

    return {
        'removed_count': removed_count,
        'duplicate_urls': [url for url, _, _ in duplicates]
    }
