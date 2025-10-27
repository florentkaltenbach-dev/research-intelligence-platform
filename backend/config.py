"""
Configuration management for the Research Intelligence Platform.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    database_url: str = "postgresql://research:research@localhost:5432/research_db"

    # Redis (optional, for caching)
    redis_url: Optional[str] = "redis://localhost:6379"

    # API Configuration
    api_title: str = "Research Intelligence Platform API"
    api_version: str = "1.0.0"
    api_description: str = "API for managing research on global power transitions"

    # CORS
    frontend_url: str = "http://localhost:3000"
    allowed_origins: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://[2a01:4f9:c012:ee5a::1]:3000",
        "http://[2a01:4f9:c012:ee5a::1]:8000",
        "*"  # Allow all origins for public access
    ]

    # Security
    secret_key: str = "change-this-secret-key-in-production"

    # Application
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


# Global settings instance
settings = Settings()
