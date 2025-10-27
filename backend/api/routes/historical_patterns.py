"""
API routes for historical patterns management.
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.models.database import get_db
from backend.models.models import HistoricalPattern
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


# Pydantic schemas
class HistoricalPatternCreate(BaseModel):
    """Schema for creating a historical pattern."""
    name: str
    description: str
    time_period: Optional[str] = None
    key_characteristics: Optional[List[str]] = None
    relevance_score: Optional[float] = None


class HistoricalPatternUpdate(BaseModel):
    """Schema for updating a historical pattern."""
    name: Optional[str] = None
    description: Optional[str] = None
    time_period: Optional[str] = None
    key_characteristics: Optional[List[str]] = None
    relevance_score: Optional[float] = None


class HistoricalPatternResponse(BaseModel):
    """Schema for historical pattern response."""
    id: int
    name: str
    description: str
    time_period: Optional[str]
    key_characteristics: Optional[List[str]]
    relevance_score: Optional[float]
    created_at: str

    class Config:
        from_attributes = True


@router.get("/", response_model=List[HistoricalPatternResponse])
async def get_historical_patterns(
    skip: int = 0,
    limit: int = 100,
    min_relevance: Optional[float] = None,
    db: Session = Depends(get_db)
):
    """
    Get all historical patterns with optional filtering.

    Args:
        skip: Number of records to skip (pagination)
        limit: Maximum number of records to return
        min_relevance: Filter by minimum relevance score
        db: Database session
    """
    logger.info(f"Fetching historical patterns: skip={skip}, limit={limit}, min_relevance={min_relevance}")

    query = db.query(HistoricalPattern)

    if min_relevance is not None:
        query = query.filter(HistoricalPattern.relevance_score >= min_relevance)

    patterns = query.order_by(HistoricalPattern.relevance_score.desc()).offset(skip).limit(limit).all()
    logger.info(f"Found {len(patterns)} historical patterns")

    return patterns


@router.get("/{pattern_id}", response_model=HistoricalPatternResponse)
async def get_historical_pattern(
    pattern_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific historical pattern by ID.

    Args:
        pattern_id: The ID of the historical pattern
        db: Database session
    """
    logger.info(f"Fetching historical pattern: id={pattern_id}")

    pattern = db.query(HistoricalPattern).filter(HistoricalPattern.id == pattern_id).first()

    if not pattern:
        logger.warning(f"Historical pattern not found: id={pattern_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Historical pattern with ID {pattern_id} not found"
        )

    return pattern


@router.post("/", response_model=HistoricalPatternResponse, status_code=status.HTTP_201_CREATED)
async def create_historical_pattern(
    pattern_data: HistoricalPatternCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new historical pattern.

    Args:
        pattern_data: Historical pattern data
        db: Database session
    """
    logger.info(f"Creating historical pattern: name={pattern_data.name}")

    # Create pattern
    pattern = HistoricalPattern(
        name=pattern_data.name,
        description=pattern_data.description,
        time_period=pattern_data.time_period,
        key_characteristics=pattern_data.key_characteristics or [],
        relevance_score=pattern_data.relevance_score
    )

    db.add(pattern)
    db.commit()
    db.refresh(pattern)

    logger.info(f"Historical pattern created: id={pattern.id}, name={pattern.name}")

    return pattern


@router.put("/{pattern_id}", response_model=HistoricalPatternResponse)
async def update_historical_pattern(
    pattern_id: int,
    pattern_data: HistoricalPatternUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing historical pattern.

    Args:
        pattern_id: The ID of the historical pattern
        pattern_data: Updated pattern data
        db: Database session
    """
    logger.info(f"Updating historical pattern: id={pattern_id}")

    pattern = db.query(HistoricalPattern).filter(HistoricalPattern.id == pattern_id).first()

    if not pattern:
        logger.warning(f"Historical pattern not found: id={pattern_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Historical pattern with ID {pattern_id} not found"
        )

    # Update fields if provided
    update_data = pattern_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(pattern, field, value)

    db.commit()
    db.refresh(pattern)

    logger.info(f"Historical pattern updated: id={pattern.id}")

    return pattern


@router.delete("/{pattern_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_historical_pattern(
    pattern_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a historical pattern.

    Args:
        pattern_id: The ID of the historical pattern
        db: Database session
    """
    logger.info(f"Deleting historical pattern: id={pattern_id}")

    pattern = db.query(HistoricalPattern).filter(HistoricalPattern.id == pattern_id).first()

    if not pattern:
        logger.warning(f"Historical pattern not found: id={pattern_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Historical pattern with ID {pattern_id} not found"
        )

    db.delete(pattern)
    db.commit()

    logger.info(f"Historical pattern deleted: id={pattern_id}")
