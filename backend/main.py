"""
Main FastAPI application for Research Intelligence Platform.
"""
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from backend.config import settings
from backend.api.routes import events, metrics, sources, analyses, admin, historical_patterns, analysis_endpoints, source_management, pattern_matching, confidence_trends
from backend.middleware import LoggingMiddleware, UsageAnalyticsMiddleware
from backend.logging_config import setup_logging
from backend.sentry_config import init_sentry
import logging

# Setup logging
setup_logging(
    log_level="DEBUG" if settings.debug else "INFO",
    log_dir="logs"
)
logger = logging.getLogger(__name__)

# Initialize Sentry (optional - only if DSN is provided)
if settings.sentry_dsn:
    sentry_enabled = init_sentry(
        dsn=settings.sentry_dsn,
        environment=settings.environment,
        enable_tracing=not settings.debug,
        traces_sample_rate=0.1 if settings.environment == "production" else 1.0
    )
    if sentry_enabled:
        logger.info("Sentry error tracking enabled")
else:
    logger.info("Sentry error tracking disabled (no DSN provided)")

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

# Create FastAPI app
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description=settings.api_description,
)

# Add rate limiter to app state
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom middleware
app.add_middleware(LoggingMiddleware)
app.add_middleware(UsageAnalyticsMiddleware)

# Include routers
app.include_router(events.router, prefix="/api/events", tags=["Events"])
app.include_router(metrics.router, prefix="/api/metrics", tags=["Metrics"])
app.include_router(sources.router, prefix="/api/sources", tags=["Sources"])
app.include_router(analyses.router, prefix="/api/analyses", tags=["Analyses"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
app.include_router(historical_patterns.router, prefix="/api/historical-patterns", tags=["Historical Patterns"])
app.include_router(analysis_endpoints.router, prefix="/api/analysis", tags=["Analysis Tools"])
app.include_router(source_management.router, prefix="/api/source-management", tags=["Source Management"])
app.include_router(pattern_matching.router, prefix="/api/pattern-matching", tags=["Pattern Matching"])
app.include_router(confidence_trends.router, prefix="/api/confidence-trends", tags=["Confidence Trends"])

logger.info(f"Application started: environment={settings.environment}, debug={settings.debug}")


@app.get("/", tags=["Root"])
@limiter.limit("100/minute")
async def root(request: Request):
    """Root endpoint."""
    logger.debug("Root endpoint accessed")
    return {
        "message": "Research Intelligence Platform API",
        "version": settings.api_version,
        "environment": settings.environment,
        "docs": "/docs",
        "health": "/api/admin/health"
    }


@app.get("/api/health", tags=["Health"])
@limiter.limit("100/minute")
async def health_check(request: Request):
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": settings.api_version,
        "environment": settings.environment
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",  # Listen on all IPv4 interfaces
        port=8000,
        reload=settings.debug
    )
