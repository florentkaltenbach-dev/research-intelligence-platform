"""
Confidence trends tracking - Monitor how analysis confidence changes over time.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from datetime import datetime, timedelta

from backend.models.database import get_db
from backend.models.models import Analysis
from pydantic import BaseModel

router = APIRouter()


class ConfidenceTrend(BaseModel):
    """Confidence trend data point."""
    date: str
    avg_confidence: float
    count: int


class ConfidenceTrendResponse(BaseModel):
    """Response containing confidence trends over time."""
    trends: List[ConfidenceTrend]
    overall_average: float
    total_analyses: int


class AnalysisConfidenceHistory(BaseModel):
    """Historical confidence for a single analysis topic."""
    title: str
    confidence_history: List[dict]


@router.get("/trends", response_model=ConfidenceTrendResponse)
async def get_confidence_trends(
    days: int = 30,
    db: Session = Depends(get_db)
):
    """
    Get confidence level trends over time.

    Args:
        days: Number of days to look back (default 30)
        db: Database session

    Returns:
        Confidence trends aggregated by day
    """
    cutoff_date = datetime.now() - timedelta(days=days)

    # Get analyses from the specified time period
    analyses = db.query(Analysis).filter(
        Analysis.created_at >= cutoff_date
    ).order_by(Analysis.created_at).all()

    if not analyses:
        return ConfidenceTrendResponse(
            trends=[],
            overall_average=0.0,
            total_analyses=0
        )

    # Group by date and calculate average confidence
    trends_by_date = {}
    for analysis in analyses:
        date_str = analysis.created_at.strftime('%Y-%m-%d')
        if date_str not in trends_by_date:
            trends_by_date[date_str] = {
                'confidence_sum': 0,
                'count': 0
            }
        if analysis.confidence_level:
            trends_by_date[date_str]['confidence_sum'] += analysis.confidence_level
            trends_by_date[date_str]['count'] += 1

    # Convert to list of trends
    trends = []
    total_confidence = 0
    total_count = 0

    for date_str in sorted(trends_by_date.keys()):
        data = trends_by_date[date_str]
        if data['count'] > 0:
            avg_conf = data['confidence_sum'] / data['count']
            trends.append(ConfidenceTrend(
                date=date_str,
                avg_confidence=round(avg_conf, 2),
                count=data['count']
            ))
            total_confidence += data['confidence_sum']
            total_count += data['count']

    overall_avg = round(total_confidence / total_count, 2) if total_count > 0 else 0.0

    return ConfidenceTrendResponse(
        trends=trends,
        overall_average=overall_avg,
        total_analyses=len(analyses)
    )


@router.get("/by-approach", response_model=List[dict])
async def get_confidence_by_approach(
    db: Session = Depends(get_db)
):
    """
    Get average confidence grouped by research approach.

    Returns:
        List of approaches with their average confidence and count
    """
    # Query analyses grouped by research approach
    results = db.query(
        Analysis.research_approach,
        func.avg(Analysis.confidence_level).label('avg_confidence'),
        func.count(Analysis.id).label('count')
    ).filter(
        Analysis.research_approach.isnot(None),
        Analysis.confidence_level.isnot(None)
    ).group_by(Analysis.research_approach).all()

    return [
        {
            'approach': result.research_approach,
            'avg_confidence': round(float(result.avg_confidence), 2),
            'count': result.count
        }
        for result in results
    ]


@router.get("/distribution", response_model=dict)
async def get_confidence_distribution(
    db: Session = Depends(get_db)
):
    """
    Get distribution of confidence levels (1-5 stars).

    Returns:
        Count of analyses for each confidence level
    """
    # Query all analyses with confidence levels
    analyses = db.query(Analysis).filter(
        Analysis.confidence_level.isnot(None)
    ).all()

    # Count by confidence level
    distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for analysis in analyses:
        if 1 <= analysis.confidence_level <= 5:
            distribution[analysis.confidence_level] += 1

    total = sum(distribution.values())

    return {
        'distribution': distribution,
        'total': total,
        'percentages': {
            level: round((count / total * 100), 1) if total > 0 else 0
            for level, count in distribution.items()
        }
    }


@router.get("/recent", response_model=List[dict])
async def get_recent_confidence_changes(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    Get recent analyses ordered by creation date to show confidence trends.

    Args:
        limit: Number of recent analyses to return (default 10)
        db: Database session

    Returns:
        List of recent analyses with confidence levels
    """
    analyses = db.query(Analysis).filter(
        Analysis.confidence_level.isnot(None)
    ).order_by(Analysis.created_at.desc()).limit(limit).all()

    return [
        {
            'id': analysis.id,
            'title': analysis.title,
            'confidence_level': analysis.confidence_level,
            'research_approach': analysis.research_approach,
            'created_at': analysis.created_at.isoformat() if analysis.created_at else None
        }
        for analysis in analyses
    ]


@router.get("/stats", response_model=dict)
async def get_confidence_stats(
    db: Session = Depends(get_db)
):
    """
    Get overall confidence statistics.

    Returns:
        Statistical summary of confidence levels
    """
    analyses = db.query(Analysis).filter(
        Analysis.confidence_level.isnot(None)
    ).all()

    if not analyses:
        return {
            'total_analyses': 0,
            'average_confidence': 0.0,
            'min_confidence': 0,
            'max_confidence': 0,
            'std_deviation': 0.0
        }

    confidence_levels = [a.confidence_level for a in analyses]
    avg = sum(confidence_levels) / len(confidence_levels)

    # Calculate standard deviation
    variance = sum((x - avg) ** 2 for x in confidence_levels) / len(confidence_levels)
    std_dev = variance ** 0.5

    return {
        'total_analyses': len(analyses),
        'average_confidence': round(avg, 2),
        'min_confidence': min(confidence_levels),
        'max_confidence': max(confidence_levels),
        'std_deviation': round(std_dev, 2)
    }
