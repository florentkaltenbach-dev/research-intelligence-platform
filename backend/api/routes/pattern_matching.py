"""
Pattern matching endpoints to link events with relevant historical patterns.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from typing import List
from datetime import datetime

from backend.models.database import get_db
from backend.models.models import Event, HistoricalPattern
from pydantic import BaseModel

router = APIRouter()


class PatternMatch(BaseModel):
    """Pattern match result with similarity score."""
    pattern_id: int
    pattern_name: str
    pattern_description: str
    time_period: str
    relevance_score: float
    similarity_score: float
    matching_reasons: List[str]


class EventPatternMatches(BaseModel):
    """Event with matched historical patterns."""
    event_id: int
    event_title: str
    matched_patterns: List[PatternMatch]


def calculate_similarity(event: Event, pattern: HistoricalPattern) -> tuple[float, List[str]]:
    """
    Calculate similarity between an event and historical pattern.

    Returns:
        tuple: (similarity_score, matching_reasons)
    """
    reasons = []
    score = 0.0
    max_score = 100.0

    # Region/geographic similarity (weight: 20%)
    event_region_lower = event.region.lower()
    pattern_desc_lower = pattern.description.lower()

    regional_keywords = {
        'middle east': ['middle east', 'arab', 'gulf', 'levant'],
        'europe': ['europe', 'european', 'eu'],
        'asia': ['asia', 'asian', 'east asia', 'southeast asia'],
        'africa': ['africa', 'african'],
        'americas': ['america', 'americas', 'latin america']
    }

    for region, keywords in regional_keywords.items():
        if region in event_region_lower or any(k in event_region_lower for k in keywords):
            if any(k in pattern_desc_lower for k in keywords):
                score += 20.0
                reasons.append(f"Geographic similarity: {region}")
                break

    # Title/description keyword matching (weight: 40%)
    event_keywords = set(event.title.lower().split() + event.description.lower().split())
    # Remove common words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'as'}
    event_keywords = {w for w in event_keywords if len(w) > 3 and w not in stop_words}

    pattern_text = (pattern.name + ' ' + pattern.description).lower()
    matching_keywords = [k for k in event_keywords if k in pattern_text]

    if matching_keywords:
        keyword_score = min(40.0, len(matching_keywords) * 5)
        score += keyword_score
        reasons.append(f"Keyword matches: {', '.join(matching_keywords[:5])}")

    # Characteristics matching (weight: 30%)
    if pattern.key_characteristics:
        for characteristic in pattern.key_characteristics:
            char_lower = characteristic.lower()
            if any(k in char_lower for k in event_keywords):
                score += 10.0
                reasons.append(f"Characteristic match: {characteristic}")
                if score >= 30.0:  # Cap at 30 points
                    break

    # Impact level consideration (weight: 10%)
    impact_keywords = {
        'CRITICAL': ['crisis', 'collapse', 'war', 'revolution', 'catastroph'],
        'HIGH': ['major', 'significant', 'important', 'critical'],
        'MEDIUM': ['notable', 'considerable'],
        'LOW': ['minor', 'small']
    }

    if event.impact_level:
        impact_words = impact_keywords.get(event.impact_level.value, [])
        if any(word in pattern_desc_lower for word in impact_words):
            score += 10.0
            reasons.append(f"Impact level alignment: {event.impact_level.value}")

    # Normalize score to 0-1 range
    similarity_score = min(score / max_score, 1.0)

    return similarity_score, reasons


@router.get("/events/{event_id}/patterns", response_model=EventPatternMatches)
async def get_event_pattern_matches(
    event_id: int,
    min_similarity: float = 0.2,
    limit: int = 5,
    db: Session = Depends(get_db)
):
    """
    Find historical patterns that match a given event.

    Args:
        event_id: Event ID to find matches for
        min_similarity: Minimum similarity score (0-1, default 0.2)
        limit: Maximum number of patterns to return (default 5)
        db: Database session

    Returns:
        EventPatternMatches with ranked pattern matches
    """
    # Get event
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Get all historical patterns
    patterns = db.query(HistoricalPattern).all()

    if not patterns:
        return EventPatternMatches(
            event_id=event.id,
            event_title=event.title,
            matched_patterns=[]
        )

    # Calculate similarity for each pattern
    matches = []
    for pattern in patterns:
        similarity_score, reasons = calculate_similarity(event, pattern)

        if similarity_score >= min_similarity:
            matches.append(PatternMatch(
                pattern_id=pattern.id,
                pattern_name=pattern.name,
                pattern_description=pattern.description,
                time_period=pattern.time_period or "Unknown period",
                relevance_score=pattern.relevance_score or 0.0,
                similarity_score=similarity_score,
                matching_reasons=reasons
            ))

    # Sort by similarity score descending
    matches.sort(key=lambda x: x.similarity_score, reverse=True)

    # Limit results
    matches = matches[:limit]

    return EventPatternMatches(
        event_id=event.id,
        event_title=event.title,
        matched_patterns=matches
    )


@router.get("/patterns/{pattern_id}/events", response_model=List[dict])
async def get_pattern_matching_events(
    pattern_id: int,
    min_similarity: float = 0.2,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    Find events that match a given historical pattern.

    Args:
        pattern_id: Historical pattern ID
        min_similarity: Minimum similarity score (0-1, default 0.2)
        limit: Maximum number of events to return (default 10)
        db: Database session

    Returns:
        List of matching events with similarity scores
    """
    # Get pattern
    pattern = db.query(HistoricalPattern).filter(HistoricalPattern.id == pattern_id).first()
    if not pattern:
        raise HTTPException(status_code=404, detail="Pattern not found")

    # Get all events
    events = db.query(Event).all()

    if not events:
        return []

    # Calculate similarity for each event
    matches = []
    for event in events:
        similarity_score, reasons = calculate_similarity(event, pattern)

        if similarity_score >= min_similarity:
            matches.append({
                "event_id": event.id,
                "event_title": event.title,
                "event_date": event.date.isoformat() if event.date else None,
                "event_region": event.region,
                "impact_level": event.impact_level.value if event.impact_level else None,
                "similarity_score": similarity_score,
                "matching_reasons": reasons
            })

    # Sort by similarity score descending
    matches.sort(key=lambda x: x["similarity_score"], reverse=True)

    # Limit results
    return matches[:limit]


@router.get("/batch-match", response_model=List[EventPatternMatches])
async def batch_match_events(
    min_similarity: float = 0.3,
    limit_per_event: int = 3,
    db: Session = Depends(get_db)
):
    """
    Match all events to historical patterns in batch.

    Args:
        min_similarity: Minimum similarity score (0-1, default 0.3)
        limit_per_event: Maximum patterns per event (default 3)
        db: Database session

    Returns:
        List of EventPatternMatches for all events
    """
    events = db.query(Event).all()
    patterns = db.query(HistoricalPattern).all()

    if not events or not patterns:
        return []

    results = []

    for event in events:
        matches = []
        for pattern in patterns:
            similarity_score, reasons = calculate_similarity(event, pattern)

            if similarity_score >= min_similarity:
                matches.append(PatternMatch(
                    pattern_id=pattern.id,
                    pattern_name=pattern.name,
                    pattern_description=pattern.description,
                    time_period=pattern.time_period or "Unknown period",
                    relevance_score=pattern.relevance_score or 0.0,
                    similarity_score=similarity_score,
                    matching_reasons=reasons
                ))

        # Sort and limit
        matches.sort(key=lambda x: x.similarity_score, reverse=True)
        matches = matches[:limit_per_event]

        if matches:  # Only include events with matches
            results.append(EventPatternMatches(
                event_id=event.id,
                event_title=event.title,
                matched_patterns=matches
            ))

    return results
