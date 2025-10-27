"""
SQLAlchemy models for the Research Intelligence Platform.
"""
from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, DateTime, ForeignKey,
    Float, JSON, Enum as SQLEnum
)
from sqlalchemy.orm import relationship
from backend.models.database import Base
import enum


class CredibilityTier(enum.Enum):
    """Source credibility tiers."""
    TIER_1 = "tier_1"  # Government data, academic papers
    TIER_2 = "tier_2"  # Established news organizations
    TIER_3 = "tier_3"  # Independent journalists, blogs
    TIER_4 = "tier_4"  # Social media, unverified sources


class ImpactLevel(enum.Enum):
    """Event impact levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Event(Base):
    """Major events in global power transitions."""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    description = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    region = Column(String(100), nullable=False)
    impact_level = Column(SQLEnum(ImpactLevel), default=ImpactLevel.MEDIUM)

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_edited_by = Column(String(200), default="claude-code")

    # Relationships
    perspectives = relationship("Perspective", back_populates="event", cascade="all, delete-orphan")


class Perspective(Base):
    """Different regional viewpoints on events."""

    __tablename__ = "perspectives"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    region = Column(String(100), nullable=False)  # e.g., "Chinese", "Russian", "Western"
    summary = Column(Text, nullable=False)
    key_points = Column(JSON)  # List of key points
    language = Column(String(50))  # Original language of sources

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    event = relationship("Event", back_populates="perspectives")
    sources = relationship("Source", secondary="perspective_sources", back_populates="perspectives")


class Metric(Base):
    """Trackable financial/economic indicators."""

    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, unique=True)
    description = Column(Text)
    unit = Column(String(50))  # e.g., "USD billions", "percentage"
    category = Column(String(100))  # e.g., "reserves", "trade", "currency"

    # Relationships
    datapoints = relationship("MetricDataPoint", back_populates="metric", cascade="all, delete-orphan")


class MetricDataPoint(Base):
    """Time series data for metrics."""

    __tablename__ = "metric_datapoints"

    id = Column(Integer, primary_key=True, index=True)
    metric_id = Column(Integer, ForeignKey("metrics.id"), nullable=False)
    value = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)
    source_id = Column(Integer, ForeignKey("sources.id"))

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)

    # Relationships
    metric = relationship("Metric", back_populates="datapoints")
    source = relationship("Source")


class HistoricalPattern(Base):
    """Historical power transition patterns for comparison."""

    __tablename__ = "historical_patterns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    time_period = Column(String(100))  # e.g., "1870-1914"
    key_characteristics = Column(JSON)  # List of characteristics
    relevance_score = Column(Float)  # How relevant to current situation

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)


class Source(Base):
    """URLs and documents with credibility ratings."""

    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(1000), nullable=False)
    title = Column(String(500), nullable=False)
    credibility_tier = Column(SQLEnum(CredibilityTier), default=CredibilityTier.TIER_3)
    region = Column(String(100))  # Geographic/cultural origin
    language = Column(String(50))
    publisher = Column(String(200))

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    accessed_at = Column(DateTime)

    # Relationships
    perspectives = relationship("Perspective", secondary="perspective_sources", back_populates="sources")


class Analysis(Base):
    """Research findings and synthesis."""

    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)  # Markdown format
    confidence_level = Column(Integer, default=3)  # 1-5 stars
    research_approach = Column(String(100))  # Which approach was used

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(String(200), default="claude-code")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# Association table for many-to-many relationship
from sqlalchemy import Table

perspective_sources = Table(
    'perspective_sources',
    Base.metadata,
    Column('perspective_id', Integer, ForeignKey('perspectives.id'), primary_key=True),
    Column('source_id', Integer, ForeignKey('sources.id'), primary_key=True)
)
