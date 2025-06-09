"""Application configuration utilities."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(slots=True)
class Settings:
    """Container for environment settings."""

    database_url: str = os.environ.get(
        "DATABASE_URL", "postgresql://user:pass@localhost/db"
    )


def get_settings() -> Settings:
    """Return current configuration settings."""

    return Settings()
