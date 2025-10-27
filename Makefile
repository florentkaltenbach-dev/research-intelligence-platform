# Research Intelligence Platform - Makefile
# Common development commands

.PHONY: help setup dev clean lint format test migrations migrate backend frontend install-backend install-frontend

# Default target
help:
	@echo "Research Intelligence Platform - Available Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make setup              - Complete project setup (backend + frontend)"
	@echo "  make install-backend    - Install backend dependencies"
	@echo "  make install-frontend   - Install frontend dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make dev                - Start both backend and frontend dev servers"
	@echo "  make backend            - Start backend only (port 8000)"
	@echo "  make frontend           - Start frontend only (port 3000)"
	@echo ""
	@echo "Database:"
	@echo "  make migrations msg=\"description\"  - Create new Alembic migration"
	@echo "  make migrate            - Apply pending migrations"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint               - Run all linters (Python + TypeScript)"
	@echo "  make format             - Format all code (Black + Prettier)"
	@echo "  make test               - Run test suites"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean              - Remove build artifacts and cache files"
	@echo ""

# Setup
setup: install-backend install-frontend
	@echo "✅ Setup complete! Use 'make dev' to start development servers."

install-backend:
	@echo "📦 Installing backend dependencies..."
	cd backend && pip install -r requirements.txt
	@echo "✅ Backend dependencies installed"

install-frontend:
	@echo "📦 Installing frontend dependencies..."
	cd frontend && npm install
	@echo "✅ Frontend dependencies installed"

# Development
dev:
	@echo "🚀 Starting development servers..."
	@echo "Backend: http://localhost:8000"
	@echo "Frontend: http://localhost:3000"
	@echo "API Docs: http://localhost:8000/docs"
	@echo ""
	@echo "Press Ctrl+C to stop all servers"
	@$(MAKE) -j 2 backend frontend

backend:
	@echo "🐍 Starting FastAPI backend on port 8000..."
	cd /home/claudeuser/research-intelligence-platform && \
	PYTHONPATH=/home/claudeuser/research-intelligence-platform python3 backend/main.py

frontend:
	@echo "⚛️  Starting React frontend on port 3000..."
	cd frontend && npm run dev

# Database
migrations:
	@echo "📝 Creating new migration: $(msg)"
	@if [ -z "$(msg)" ]; then \
		echo "❌ Error: Please provide a migration message with msg=\"description\""; \
		exit 1; \
	fi
	cd backend && alembic revision --autogenerate -m "$(msg)"
	@echo "✅ Migration created"

migrate:
	@echo "🔄 Applying database migrations..."
	cd backend && alembic upgrade head
	@echo "✅ Migrations applied"

# Code Quality
lint:
	@echo "🔍 Running linters..."
	@echo "Backend (Python)..."
	cd backend && python3 -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	@echo "Frontend (TypeScript)..."
	cd frontend && npm run lint
	@echo "✅ Linting complete"

format:
	@echo "✨ Formatting code..."
	@echo "Backend (Black + isort)..."
	cd backend && python3 -m black . --line-length 100
	cd backend && python3 -m isort .
	@echo "Frontend (Prettier)..."
	cd frontend && npm run format || npx prettier --write "src/**/*.{ts,tsx}"
	@echo "✅ Formatting complete"

test:
	@echo "🧪 Running tests..."
	@echo "Backend tests..."
	cd backend && python3 -m pytest tests/ -v
	@echo "Frontend tests..."
	cd frontend && npm test
	@echo "✅ Tests complete"

# Maintenance
clean:
	@echo "🧹 Cleaning build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "node_modules" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Clean complete"
