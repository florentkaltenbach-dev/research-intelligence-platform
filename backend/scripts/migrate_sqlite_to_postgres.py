#!/usr/bin/env python3
"""
Migrate data from SQLite to PostgreSQL.
Run this after initializing PostgreSQL: python backend/scripts/migrate_sqlite_to_postgres.py
"""
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from backend.models.database import Base, SessionLocal
from backend.models import models

# SQLite source database
SQLITE_URL = "sqlite:///./research.db"
sqlite_engine = create_engine(SQLITE_URL)
SqliteSession = sessionmaker(bind=sqlite_engine)

# PostgreSQL target database (from environment)
postgres_session = SessionLocal()

def migrate_data():
    """Migrate all data from SQLite to PostgreSQL."""
    print("Starting migration from SQLite to PostgreSQL...")
    print("=" * 60)

    sqlite_session = SqliteSession()

    try:
        # Define migration order (respecting foreign key dependencies)
        migrations = [
            ('events', models.Event),
            ('historical_patterns', models.HistoricalPattern),
            ('metrics', models.Metric),
            ('sources', models.Source),
            ('analyses', models.Analysis),
            ('perspectives', models.Perspective),
            ('metric_datapoints', models.MetricDataPoint),
        ]

        total_migrated = 0

        for table_name, model_class in migrations:
            # Count records in SQLite
            count = sqlite_session.query(model_class).count()

            if count == 0:
                print(f"✓ {table_name}: 0 rows (skipping)")
                continue

            print(f"Migrating {table_name}: {count} rows...", end=" ")

            # Fetch all records from SQLite
            records = sqlite_session.query(model_class).all()

            # Insert into PostgreSQL
            for record in records:
                # Create a dict of all attributes
                record_dict = {}
                for column in model_class.__table__.columns:
                    record_dict[column.name] = getattr(record, column.name)

                # Create new instance for PostgreSQL
                new_record = model_class(**record_dict)
                postgres_session.add(new_record)

            postgres_session.commit()
            print(f"✓ Done")
            total_migrated += count

        print("=" * 60)
        print(f"✓ Migration complete! Migrated {total_migrated} total rows")

        # Show summary
        print("\nPostgreSQL Database Summary:")
        print("-" * 60)
        for table_name, model_class in migrations:
            count = postgres_session.query(model_class).count()
            if count > 0:
                print(f"  {table_name}: {count} rows")

    except Exception as e:
        postgres_session.rollback()
        print(f"\n✗ Migration failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    finally:
        sqlite_session.close()
        postgres_session.close()

if __name__ == "__main__":
    migrate_data()
