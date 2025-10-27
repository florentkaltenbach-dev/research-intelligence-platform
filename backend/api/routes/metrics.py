"""
API routes for managing metrics and time series data.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from datetime import datetime

from backend.models import Metric, MetricDataPoint, get_db

router = APIRouter()


# Pydantic schemas
class MetricCreate(BaseModel):
    name: str
    description: str | None = None
    unit: str
    category: str | None = None


class DataPointCreate(BaseModel):
    metric_id: int
    value: float
    date: datetime
    source_id: int | None = None
    notes: str | None = None


class MetricResponse(BaseModel):
    id: int
    name: str
    description: str | None
    unit: str
    category: str | None

    class Config:
        from_attributes = True


@router.get("/", response_model=List[MetricResponse])
async def list_metrics(db: Session = Depends(get_db)):
    """List all metrics."""
    metrics = db.query(Metric).all()
    return metrics


@router.get("/{metric_id}")
async def get_metric(metric_id: int, db: Session = Depends(get_db)):
    """Get a single metric."""
    metric = db.query(Metric).filter(Metric.id == metric_id).first()
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric


@router.get("/{metric_id}/history")
async def get_metric_history(
    metric_id: int,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get time series data for a metric."""
    metric = db.query(Metric).filter(Metric.id == metric_id).first()
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")

    datapoints = (
        db.query(MetricDataPoint)
        .filter(MetricDataPoint.metric_id == metric_id)
        .order_by(MetricDataPoint.date.desc())
        .limit(limit)
        .all()
    )

    return {
        "metric": {
            "id": metric.id,
            "name": metric.name,
            "unit": metric.unit,
            "category": metric.category
        },
        "datapoints": [
            {
                "value": dp.value,
                "date": dp.date,
                "notes": dp.notes,
                "source_id": dp.source_id
            }
            for dp in reversed(datapoints)  # Chronological order
        ]
    }


@router.post("/", response_model=MetricResponse)
async def create_metric(metric: MetricCreate, db: Session = Depends(get_db)):
    """Create a new metric."""
    db_metric = Metric(
        name=metric.name,
        description=metric.description,
        unit=metric.unit,
        category=metric.category
    )
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric


@router.post("/datapoint")
async def add_datapoint(datapoint: DataPointCreate, db: Session = Depends(get_db)):
    """Add a data point to a metric."""
    # Verify metric exists
    metric = db.query(Metric).filter(Metric.id == datapoint.metric_id).first()
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")

    db_datapoint = MetricDataPoint(
        metric_id=datapoint.metric_id,
        value=datapoint.value,
        date=datapoint.date,
        source_id=datapoint.source_id,
        notes=datapoint.notes
    )
    db.add(db_datapoint)
    db.commit()
    db.refresh(db_datapoint)
    return db_datapoint
