"""Database connection and session management."""

from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import get_settings

SETTINGS = get_settings()
ENGINE = create_engine(SETTINGS.database_url)
SessionLocal = sessionmaker(bind=ENGINE)


def get_session():
    """Provide a transactional scope around a series of operations."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
