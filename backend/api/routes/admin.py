"""
Admin API routes for platform management.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
import logging

from backend.models import Event, Perspective, Source, Analysis, Metric, get_db
from backend.cache import cache

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "Research Intelligence Platform API"
    }


@router.get("/stats")
async def get_stats(db: Session = Depends(get_db)):
    """Get platform statistics."""
    # Try to get from cache first
    cache_key = "stats:platform"
    cached_stats = cache.get(cache_key)
    if cached_stats:
        logger.debug("Returning cached stats")
        return cached_stats

    # Query database
    stats = {
        "events": db.query(func.count(Event.id)).scalar(),
        "perspectives": db.query(func.count(Perspective.id)).scalar(),
        "sources": db.query(func.count(Source.id)).scalar(),
        "analyses": db.query(func.count(Analysis.id)).scalar(),
        "metrics": db.query(func.count(Metric.id)).scalar(),
    }

    # Source diversity
    sources_by_region = (
        db.query(Source.region, func.count(Source.id))
        .group_by(Source.region)
        .all()
    )
    stats["sources_by_region"] = {region: count for region, count in sources_by_region if region}

    # Cache for 5 minutes
    cache.set(cache_key, stats, ttl=300)
    logger.info("Stats computed and cached")

    return stats
