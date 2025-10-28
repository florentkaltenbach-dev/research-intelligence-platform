# Setup Guide for Research Intelligence Platform

## Current Status

✅ **Application Code**: Fully built and ready
✅ **Git Repository**: Initialized with proper commits
✅ **Web Configuration**: Configured for IPv6 access

## What You Need to Run

Since Docker is not installed on this server, you'll need to install PostgreSQL and set up the Python/Node.js environments.

## Quick Setup (Without Docker)

### 1. Install PostgreSQL 16

```bash
# Add PostgreSQL repository
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget -qO- https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo tee /etc/apt/trusted.gpg.d/pgdg.asc &>/dev/null

# Install PostgreSQL 16
sudo apt update
sudo apt install -y postgresql-16 postgresql-contrib-16

# Start PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 2. Create Database and User

```bash
# Switch to postgres user and create database
sudo -u postgres psql << EOF
CREATE DATABASE research_db;
CREATE USER research WITH PASSWORD 'research';
GRANT ALL PRIVILEGES ON DATABASE research_db TO research;
ALTER DATABASE research_db OWNER TO research;
\q
EOF
```

### 3. Install Python Dependencies

```bash
cd ~/research-intelligence-platform/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python scripts/init_db.py
```

### 4. Install Node.js Dependencies

```bash
cd ~/research-intelligence-platform/frontend

# Install dependencies
npm install
```

### 5. Start the Services

**Terminal 1 - Backend:**
```bash
cd ~/research-intelligence-platform/backend
source venv/bin/activate
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd ~/research-intelligence-platform/frontend
npm run dev
```

## Access URLs

Once both services are running:

### Web Access (IPv6)
- **Frontend**: http://[2a01:4f9:c012:ee5a::1]:3000
- **API**: http://[2a01:4f9:c012:ee5a::1]:8000
- **API Docs**: http://[2a01:4f9:c012:ee5a::1]:8000/docs

### Local Access
- **Frontend**: http://localhost:3000
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Simplified Setup (SQLite - No PostgreSQL Required)

If you want to test quickly without PostgreSQL:

1. Update `backend/config.py`:
   ```python
   database_url: str = "sqlite:///./research.db"
   ```

2. Install dependencies:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Initialize database:
   ```bash
   python scripts/init_db.py
   ```

4. Start backend:
   ```bash
   python main.py
   ```

5. In another terminal, start frontend:
   ```bash
   cd frontend
   npm install
npm run dev
   ```

## Troubleshooting

### Port Already in Use
```bash
# Check what's using port 8000 or 3000
sudo lsof -i :8000
sudo lsof -i :3000

# Kill the process if needed
kill -9 <PID>
```

### Database Connection Issues
```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Check database exists
sudo -u postgres psql -l | grep research_db
```

### Frontend Can't Connect to Backend
- Make sure both services are running
- Check CORS configuration in `backend/config.py`
- Verify no firewall blocking ports 3000 or 8000

## Production Deployment

For production deployment, see the main README.md for:
- Vercel (Frontend)
- Railway/Fly.io (Backend)
- Managed PostgreSQL
