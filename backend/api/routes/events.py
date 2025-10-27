"""
API routes for managing events.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from datetime import datetime

from backend.models import Event, Perspective, get_db, ImpactLevel

router = APIRouter()


# Pydantic schemas
class PerspectiveCreate(BaseModel):
    region: str
    summary: str
    key_points: list[str]
    language: str | None = None


class EventCreate(BaseModel):
    title: str
    description: str
    date: datetime
    region: str
    impact_level: str = "medium"


class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    date: datetime
    region: str
    impact_level: str
    created_at: datetime
    updated_at: datetime
    last_edited_by: str

    class Config:
        from_attributes = True


@router.get("/", response_model=List[EventResponse])
async def list_events(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """List all events with pagination."""
    events = db.query(Event).order_by(Event.date.desc()).offset(skip).limit(limit).all()
    return events


@router.get("/{event_id}")
async def get_event(event_id: int, db: Session = Depends(get_db)):
    """Get a single event with all perspectives."""
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return {
        "id": event.id,
        "title": event.title,
        "description": event.description,
        "date": event.date,
        "region": event.region,
        "impact_level": event.impact_level.value,
        "created_at": event.created_at,
        "updated_at": event.updated_at,
        "last_edited_by": event.last_edited_by,
        "perspectives": [
            {
                "id": p.id,
                "region": p.region,
                "summary": p.summary,
                "key_points": p.key_points,
                "language": p.language,
                "sources": [{"id": s.id, "title": s.title, "url": s.url} for s in p.sources]
            }
            for p in event.perspectives
        ]
    }


@router.post("/", response_model=EventResponse)
async def create_event(event: EventCreate, db: Session = Depends(get_db)):
    """Create a new event."""
    db_event = Event(
        title=event.title,
        description=event.description,
        date=event.date,
        region=event.region,
        impact_level=ImpactLevel[event.impact_level.upper()]
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


@router.put("/{event_id}", response_model=EventResponse)
async def update_event(
    event_id: int,
    event: EventCreate,
    db: Session = Depends(get_db)
):
    """Update an existing event."""
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")

    db_event.title = event.title
    db_event.description = event.description
    db_event.date = event.date
    db_event.region = event.region
    db_event.impact_level = ImpactLevel[event.impact_level.upper()]
    db_event.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(db_event)
    return db_event


@router.delete("/{event_id}")
async def delete_event(event_id: int, db: Session = Depends(get_db)):
    """Delete an event."""
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(db_event)
    db.commit()
    return {"message": "Event deleted successfully"}


@router.post("/{event_id}/perspectives")
async def add_perspective(
    event_id: int,
    perspective: PerspectiveCreate,
    db: Session = Depends(get_db)
):
    """Add a perspective to an event."""
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db_perspective = Perspective(
        event_id=event_id,
        region=perspective.region,
        summary=perspective.summary,
        key_points=perspective.key_points,
        language=perspective.language
    )
    db.add(db_perspective)
    db.commit()
    db.refresh(db_perspective)
    return db_perspective
