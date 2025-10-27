"""
API routes for advanced analysis features.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import logging

from backend.models import Event, Perspective, get_db
from backend.analysis_tools import PerspectiveAnalyzer

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/events/{event_id}/contradictions")
async def get_event_contradictions(event_id: int, db: Session = Depends(get_db)):
    """
    Find contradictions between perspectives on an event.

    Args:
        event_id: Event ID
        db: Database session
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Convert perspectives to dicts
    perspectives = [
        {
            'id': p.id,
            'region': p.region,
            'summary': p.summary,
            'key_points': p.key_points or []
        }
        for p in event.perspectives
    ]

    contradictions = PerspectiveAnalyzer.find_contradictions(perspectives)

    logger.info(f"Found {len(contradictions)} contradictions for event {event_id}")

    return {
        'event_id': event_id,
        'event_title': event.title,
        'contradictions': contradictions
    }


@router.get("/events/{event_id}/consensus")
async def get_event_consensus(event_id: int, db: Session = Depends(get_db)):
    """
    Find consensus points between perspectives on an event.

    Args:
        event_id: Event ID
        db: Database session
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Convert perspectives to dicts
    perspectives = [
        {
            'id': p.id,
            'region': p.region,
            'summary': p.summary,
            'key_points': p.key_points or []
        }
        for p in event.perspectives
    ]

    consensus = PerspectiveAnalyzer.find_consensus(perspectives)

    logger.info(f"Found {len(consensus)} consensus items for event {event_id}")

    return {
        'event_id': event_id,
        'event_title': event.title,
        'consensus_items': consensus
    }


@router.get("/events/{event_id}/conflict-prediction")
async def get_conflict_predictions(event_id: int, db: Session = Depends(get_db)):
    """
    Predict potential conflicts based on opposing trajectories.

    Args:
        event_id: Event ID
        db: Database session
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Convert perspectives to dicts
    perspectives = [
        {
            'id': p.id,
            'region': p.region,
            'summary': p.summary,
            'key_points': p.key_points or []
        }
        for p in event.perspectives
    ]

    predictions = PerspectiveAnalyzer.predict_conflict_zones(perspectives)

    logger.info(f"Generated {len(predictions)} conflict predictions for event {event_id}")

    return {
        'event_id': event_id,
        'event_title': event.title,
        'predictions': predictions
    }


@router.get("/events/{event_id}/related")
async def get_related_events(
    event_id: int,
    limit: int = 5,
    db: Session = Depends(get_db)
):
    """
    Find events related to the given event by theme or impact.

    Args:
        event_id: Event ID
        limit: Maximum number of related events to return
        db: Database session
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    event_dict = {
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'region': event.region,
        'impact_level': event.impact_level.value if event.impact_level else None
    }

    # Get all other events
    other_events = db.query(Event).filter(Event.id != event_id).all()

    # Analyze relationships
    related = []
    for other in other_events:
        other_dict = {
            'id': other.id,
            'title': other.title,
            'description': other.description,
            'region': other.region,
            'impact_level': other.impact_level.value if other.impact_level else None
        }

        relationship = PerspectiveAnalyzer.find_related_themes(event_dict, other_dict)

        if relationship['is_related']:
            related.append({
                'event_id': other.id,
                'event_title': other.title,
                'event_date': other.date.isoformat(),
                'region': other.region,
                'similarity_score': relationship['similarity_score'],
                'shared_themes': relationship['shared_keywords'][:5],  # Top 5
                'same_region': relationship['same_region']
            })

    # Sort by similarity score
    related.sort(key=lambda x: x['similarity_score'], reverse=True)
    related = related[:limit]

    logger.info(f"Found {len(related)} related events for event {event_id}")

    return {
        'event_id': event_id,
        'event_title': event.title,
        'related_events': related
    }
