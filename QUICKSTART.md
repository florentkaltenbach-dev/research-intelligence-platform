# Quick Start Guide

## Start Backend
```bash
cd /home/claudeuser/research-intelligence-platform
PYTHONPATH=/home/claudeuser/research-intelligence-platform python3 backend/main.py
```

## Start Frontend
```bash
cd /home/claudeuser/research-intelligence-platform/frontend
npm run dev
```

## Access
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Database Fixed
SQLite connection now works properly (no more PostgreSQL connection errors).

## New Features Available
- Event Timeline (`/timeline`)
- Historical Patterns (`/historical-patterns`)
- Metrics Visualization with charts (`/metrics/{id}`)
- Geographic distribution chart on homepage
- Advanced analysis APIs for contradictions, consensus, conflict prediction

## Logs
Check `logs/` directory for application logs.
