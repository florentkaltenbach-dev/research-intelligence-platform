#!/bin/bash
# Quick Start Script for Research Intelligence Platform

set -e

echo "🚀 Research Intelligence Platform - Quick Start"
echo "=============================================="
echo ""

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if PostgreSQL is installed
if command -v psql &> /dev/null; then
    echo -e "${GREEN}✓${NC} PostgreSQL is installed"
else
    echo -e "${YELLOW}⚠${NC}  PostgreSQL is not installed"
    echo "  Install it with: sudo apt install postgresql-16"
    echo ""
fi

# Check if Node.js is installed
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓${NC} Node.js is installed (${NODE_VERSION})"
else
    echo -e "${YELLOW}⚠${NC}  Node.js is not installed"
    echo "  Install it from: https://nodejs.org/"
    echo ""
fi

# Check if Python 3 is installed
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓${NC} Python is installed (${PYTHON_VERSION})"
else
    echo -e "${YELLOW}⚠${NC}  Python 3 is not installed"
    echo ""
fi

echo ""
echo -e "${BLUE}📋 Next Steps:${NC}"
echo ""
echo "1. Read SETUP.md for detailed instructions"
echo "2. Install PostgreSQL if not already installed"
echo "3. Create database: sudo -u postgres psql < setup-db.sql"
echo "4. Set up backend: cd backend && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
echo "5. Initialize DB: python scripts/init_db.py"
echo "6. Set up frontend: cd frontend && npm install"
echo "7. Start backend: cd backend && python main.py"
echo "8. Start frontend: cd frontend && npm run dev"
echo ""
echo -e "${GREEN}🌐 Access URLs:${NC}"
echo "   Frontend: http://46.62.231.96:3000"
echo "   API: http://46.62.231.96:8000"
echo "   API Docs: http://46.62.231.96:8000/docs"
echo ""
