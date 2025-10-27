#!/bin/bash
# One-command installation and startup script
# Run this after installing system packages

set -e

echo "🚀 Research Intelligence Platform - Automated Setup"
echo "===================================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo -e "${RED}Error: Run this script from the project root directory${NC}"
    exit 1
fi

# Step 1: Install Python dependencies
echo -e "${BLUE}[1/5]${NC} Installing Python dependencies..."
cd backend
python3 -m pip install --user -r requirements.txt > /dev/null 2>&1 || {
    echo -e "${YELLOW}Trying with venv...${NC}"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
}
echo -e "${GREEN}✓${NC} Python dependencies installed"

# Step 2: Initialize database
echo -e "${BLUE}[2/5]${NC} Initializing SQLite database..."
python3 scripts/init_db.py
echo -e "${GREEN}✓${NC} Database initialized"

# Step 3: Install frontend dependencies
echo -e "${BLUE}[3/5]${NC} Installing frontend dependencies..."
cd ../frontend
npm install > /dev/null 2>&1
echo -e "${GREEN}✓${NC} Frontend dependencies installed"

# Step 4: Start backend (in background)
echo -e "${BLUE}[4/5]${NC} Starting backend API..."
cd ../backend
if [ -d "venv" ]; then
    source venv/bin/activate
fi
nohup python3 main.py > ../backend.log 2>&1 &
BACKEND_PID=$!
echo $BACKEND_PID > ../backend.pid
echo -e "${GREEN}✓${NC} Backend started (PID: $BACKEND_PID)"

# Wait for backend to be ready
echo -e "${YELLOW}Waiting for backend to be ready...${NC}"
sleep 3

# Step 5: Start frontend (in background)
echo -e "${BLUE}[5/5]${NC} Starting frontend..."
cd ../frontend
nohup npm run dev > ../frontend.log 2>&1 &
FRONTEND_PID=$!
echo $FRONTEND_PID > ../frontend.pid
echo -e "${GREEN}✓${NC} Frontend started (PID: $FRONTEND_PID)"

# Wait for frontend to be ready
echo -e "${YELLOW}Waiting for frontend to be ready...${NC}"
sleep 5

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${BLUE}📡 Access URLs:${NC}"
echo ""
echo "  Frontend:  http://[2a01:4f9:c012:ee5a::1]:3000"
echo "  API:       http://[2a01:4f9:c012:ee5a::1]:8000"
echo "  API Docs:  http://[2a01:4f9:c012:ee5a::1]:8000/docs"
echo ""
echo -e "${BLUE}📋 Process Info:${NC}"
echo "  Backend PID:  $BACKEND_PID (log: backend.log)"
echo "  Frontend PID: $FRONTEND_PID (log: frontend.log)"
echo ""
echo -e "${BLUE}🛑 To stop services:${NC}"
echo "  kill $BACKEND_PID $FRONTEND_PID"
echo "  # Or run: ./stop-services.sh"
echo ""
echo -e "${BLUE}📊 View logs:${NC}"
echo "  tail -f backend.log"
echo "  tail -f frontend.log"
echo ""
