"""
Main FastAPI application for Research Intelligence Platform.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings
from backend.api.routes import events, metrics, sources, analyses, admin

# Create FastAPI app
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description=settings.api_description,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(events.router, prefix="/api/events", tags=["Events"])
app.include_router(metrics.router, prefix="/api/metrics", tags=["Metrics"])
app.include_router(sources.router, prefix="/api/sources", tags=["Sources"])
app.include_router(analyses.router, prefix="/api/analyses", tags=["Analyses"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint."""
    return {
        "message": "Research Intelligence Platform API",
        "version": settings.api_version,
        "docs": "/docs",
        "health": "/api/admin/health"
    }


@app.get("/api/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": settings.api_version
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )
