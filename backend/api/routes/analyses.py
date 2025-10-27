"""
API routes for managing research analyses.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from backend.models import Analysis, get_db

router = APIRouter()


class AnalysisCreate(BaseModel):
    title: str
    content: str  # Markdown format
    confidence_level: int = 3  # 1-5
    research_approach: str | None = None


class AnalysisResponse(BaseModel):
    id: int
    title: str
    content: str
    confidence_level: int
    research_approach: str | None
    created_by: str
    created_at: str

    class Config:
        from_attributes = True


@router.get("/", response_model=List[AnalysisResponse])
async def list_analyses(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """List all analyses."""
    analyses = (
        db.query(Analysis)
        .order_by(Analysis.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return analyses


@router.get("/{analysis_id}", response_model=AnalysisResponse)
async def get_analysis(analysis_id: int, db: Session = Depends(get_db)):
    """Get a single analysis."""
    analysis = db.query(Analysis).filter(Analysis.id == analysis_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return analysis


@router.post("/", response_model=AnalysisResponse)
async def create_analysis(analysis: AnalysisCreate, db: Session = Depends(get_db)):
    """Create a new analysis."""
    db_analysis = Analysis(
        title=analysis.title,
        content=analysis.content,
        confidence_level=analysis.confidence_level,
        research_approach=analysis.research_approach
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis
