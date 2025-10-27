# Systemd Service Setup

This directory contains systemd service files for the Research Intelligence Platform.

## Services

- **research-backend.service** - Backend FastAPI application
- **research-frontend.service** - Frontend React application

## Installation

To install these services for autostart on system boot:

```bash
# Copy service files
sudo cp systemd/research-backend.service /etc/systemd/system/
sudo cp systemd/research-frontend.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable services to start on boot
sudo systemctl enable research-backend.service
sudo systemctl enable research-frontend.service

# Start services
sudo systemctl start research-backend.service
sudo systemctl start research-frontend.service
```

## Managing Services

```bash
# Check status
sudo systemctl status research-backend.service
sudo systemctl status research-frontend.service

# View logs
sudo journalctl -u research-backend.service -f
sudo journalctl -u research-frontend.service -f

# Restart services
sudo systemctl restart research-backend.service
sudo systemctl restart research-frontend.service

# Stop services
sudo systemctl stop research-backend.service
sudo systemctl stop research-frontend.service
```

## Access

- **Backend API**: http://localhost:8000
- **Frontend**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs

## Notes

- Backend runs using uvicorn with Python virtual environment at `/home/claudeuser/research_venv`
- Frontend runs using npm/vite dev server
- Both services automatically restart on failure
- Redis is optional - caching is disabled if not available
- Services are configured to start after network is available
