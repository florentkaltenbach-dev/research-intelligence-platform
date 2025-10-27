#!/usr/bin/env python3
"""
Initialize the database with tables.
Run this after starting postgres: python backend/scripts/init_db.py
"""
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.database import Base, engine
from models import models  # noqa - import to register models

def init_db():
    """Create all tables in the database."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Database initialized successfully!")
    print("\nTables created:")
    for table in Base.metadata.sorted_tables:
        print(f"  - {table.name}")

if __name__ == "__main__":
    init_db()
