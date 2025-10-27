"""
Database connection and session management.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.config import settings

# Create database engine with SQLite-specific configuration
if settings.database_url.startswith('sqlite'):
    # SQLite doesn't support pool_size/max_overflow
    engine = create_engine(
        settings.database_url,
        connect_args={"check_same_thread": False}  # Allow SQLite to be used with FastAPI
    )
else:
    # PostgreSQL and other databases
    engine = create_engine(
        settings.database_url,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20
    )

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db():
    """
    Dependency function to get database session.

    Yields:
        Database session that automatically closes after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
