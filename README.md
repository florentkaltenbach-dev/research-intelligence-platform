# Research Intelligence Platform

A Wikipedia-style platform for analyzing global power transitions and capital flows through multi-perspective research.

## Overview

This platform enables you to manually curate research on power transitions, tracking events, perspectives from different regions, financial metrics, and sources—all with proper credibility ratings and citations.

**Key Principle**: This is **not** an automated system. You use Claude Code (via your Max subscription) to manually research topics and populate the platform with findings.

## Features

- 📅 **Events**: Track major developments in power transitions
- 🌍 **Multi-Perspective Analysis**: Compare Western, Chinese, Russian, Arabic, and other regional viewpoints
- 📊 **Metrics**: Track financial indicators over time (gold reserves, currency flows, etc.)
- 📚 **Source Library**: All sources rated Tier 1-4 for credibility
- 📝 **Research Analyses**: Synthesize findings with confidence ratings
- 🔍 **Wikipedia-Style UI**: Clean, accessible presentation

## Technology Stack

### Backend
- Python 3.12+ with FastAPI
- PostgreSQL 16+ for data storage
- SQLAlchemy ORM with Alembic migrations
- Redis 7.4+ (optional, for caching)

### Frontend
- React 19 with TypeScript 5+
- Vite 6 (requires Node.js 20.19+ or 22.12+)
- TailwindCSS for styling
- React Query for data fetching

### Development
- Docker Compose for local development
- Claude Code for manual research and content addition

## Quick Start

### Prerequisites
- Python 3.12+
- Node.js 20.19+ or 22.12+
- Docker and Docker Compose
- Claude Code (or Claude Max subscription)

### Installation

1. **Clone and setup**
   ```bash
   cd research-intelligence-platform
   cp .env.example .env
   ```

2. **Start services**
   ```bash
   docker-compose up -d
   ```

3. **Install Python dependencies**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   python scripts/init_db.py
   ```

5. **Install frontend dependencies**
   ```bash
   cd ../frontend
   npm install
   ```

6. **Start development servers**

   Terminal 1 (Backend):
   ```bash
   cd backend
   python main.py
   ```

   Terminal 2 (Frontend):
   ```bash
   cd frontend
   npm run dev
   ```

7. **Access the application**
   - Frontend: http://localhost:3000
   - API docs: http://localhost:8000/docs
   - Database: PostgreSQL on localhost:5432

## Usage

### Adding Research with Claude Code

1. **Start Claude Code**
   ```bash
   claude  # or use https://claude.ai/code
   ```

2. **Request research** (example):
   ```
   Research "BRICS currency discussions 2024" using the Source Diversification approach.

   Find perspectives from Chinese, Russian, Indian, and Arabic sources. Create an Event
   in the database with Perspectives for each region, properly cited with Sources.
   ```

3. **Claude Code will**:
   - Use web search to find sources
   - Analyze different regional perspectives
   - Make API calls to create Event, Perspectives, and Sources
   - Commit the changes with a descriptive message

4. **Review and push**
   ```bash
   git push origin main  # Auto-deploys if configured
   ```

### Research Approaches

See `research/approaches/` for detailed templates:
- **Source Diversification**: Find non-Western perspectives
- **Data Collection**: Track metrics over time
- **Synthesis**: Combine multiple analyses

## Project Structure

```
research-intelligence-platform/
├── backend/                  # FastAPI backend
│   ├── api/routes/          # API endpoints
│   ├── models/              # Database models
│   ├── scripts/             # Helper scripts
│   ├── alembic/             # Database migrations
│   ├── main.py              # FastAPI app
│   └── config.py            # Configuration
├── frontend/                 # React frontend
│   └── src/
│       ├── components/      # React components
│       ├── pages/           # Page components
│       └── services/        # API client
├── research/                 # Research templates
│   ├── approaches/          # Research methodologies
│   └── findings/            # Session outputs
├── docker-compose.yml        # Local development
└── README.md
```

## API Endpoints

### Public Read Access
- `GET /api/events` - List all events
- `GET /api/events/{id}` - Get event with perspectives
- `GET /api/metrics` - List metrics
- `GET /api/sources` - Browse sources
- `GET /api/analyses` - List analyses

### Content Management (via Claude Code)
- `POST /api/events` - Create event
- `POST /api/perspectives` - Add perspective
- `POST /api/metrics/datapoint` - Add data point
- `POST /api/sources` - Register source
- `POST /api/analyses` - Save analysis

### Admin
- `GET /api/admin/health` - Health check
- `GET /api/admin/stats` - Platform statistics

## Development

### Database Migrations

```bash
cd backend
# Create migration
alembic revision --autogenerate -m "description"
# Apply migrations
alembic upgrade head
```

### Testing Locally

```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm run lint
npm run build
```

## Deployment

### Frontend (Vercel)
1. Connect GitHub repository to Vercel
2. Set build command: `cd frontend && npm run build`
3. Set output directory: `frontend/dist`
4. Auto-deploys on push to main

### Backend (Railway/Fly.io)
1. Connect GitHub repository
2. Set environment variables from `.env.example`
3. Auto-deploys on push to main

### Database
- Use managed PostgreSQL from hosting provider
- Or use Supabase/Neon for serverless Postgres

## Contributing

1. Create a feature branch
2. Make changes
3. Use Claude Code to test thoroughly
4. Create pull request
5. Merge to main → auto-deploy

## Research Methodology

### Multi-Perspective Principle
Always search for non-Western sources (Chinese, Russian, Arabic, Hindi perspectives) to avoid Western-centric bias.

### Currency Diversity
Track financial data in multiple currencies (Yuan, Rupee, Ruble, Dirham), not just USD/EUR.

### Source Credibility Tiers
- **Tier 1**: Government data, academic papers
- **Tier 2**: Established news organizations
- **Tier 3**: Independent journalists, blogs
- **Tier 4**: Social media, unverified sources

### Confidence Levels
All analyses use 1-5 star confidence ratings:
- ⭐ = Speculative
- ⭐⭐ = Uncertain
- ⭐⭐⭐ = Moderate confidence
- ⭐⭐⭐⭐ = High confidence
- ⭐⭐⭐⭐⭐ = Very high confidence

## License

MIT License - See LICENSE file for details

## Acknowledgments

Built with Claude Code - AI-assisted development using Claude Max subscription.

---

**Note**: This platform is designed for manual curation, not automation. Think of it like building Wikipedia, not like building a robot researcher.
