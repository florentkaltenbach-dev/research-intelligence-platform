# Research Intelligence Platform - Initialization Prompt

Build a Wikipedia-style research platform for analyzing global power transitions and capital flows. You'll manually update it using Claude Code (via your Max subscription) - no automated API calls or agents.

## Phase 1: Project Foundation

### 1.1 Initial Setup
Create the project structure:
```
research-intelligence-platform/
├── .github/workflows/         # Deployment automation
├── backend/
│   ├── api/
│   │   └── routes/
│   ├── models/
│   ├── services/
│   ├── scripts/               # Data import/maintenance
│   ├── main.py
│   ├── config.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── services/
│   ├── package.json
│   └── tsconfig.json
├── research/                  # Research templates & session notes
│   ├── approaches/
│   └── findings/
├── docs/
├── tests/
├── docker-compose.yml
├── .env.example
├── .gitignore
├── Makefile
├── README.md
└── CLAUDE.md (already exists)
```

### 1.2 Backend Setup
1. Create Python virtual environment
2. Set up FastAPI with basic structure:
   - Health check endpoint
   - CORS configuration
   - Basic error handling
3. Configure PostgreSQL connection with SQLAlchemy
4. Optional: Set up Redis for web caching (NOT task queues)

**Key files to create**:
- `backend/main.py` - FastAPI app
- `backend/config.py` - Environment variable management
- `backend/models/database.py` - Database connection
- `backend/requirements.txt` - Python dependencies
  - FastAPI, SQLAlchemy, Alembic, psycopg2-binary
  - NO Celery, NO anthropic SDK

### 1.3 Frontend Setup
1. Initialize React 19 + TypeScript with Vite 6
   ```bash
   npm create vite@latest frontend -- --template react-ts
   npm install react@19 react-dom@19 @types/react@^19.0.0 @types/react-dom@^19.0.0
   ```
2. Set up Tailwind CSS and shadcn/ui
3. Create basic routing structure
4. Set up API client with proper typing
5. Create layout components (Header, Sidebar, Footer)

**Key files to create**:
- `frontend/src/App.tsx` - Main app component
- `frontend/src/main.tsx` - Entry point
- `frontend/src/services/api.ts` - API client
- `frontend/package.json` - Dependencies
- `frontend/tailwind.config.js` - Tailwind configuration

### 1.4 Docker Setup
Create `docker-compose.yml` with services:
- PostgreSQL 16
- Redis (optional, for caching)
- Backend (FastAPI)
- Frontend (React dev server)

**Note**: NO Celery workers or task queues - this is for local development only

### 1.5 Development Tools
1. Create `Makefile` with common commands
2. Set up `.gitignore` for Python and Node
3. Create `.env.example` template
4. Write initial README.md with setup instructions

## Phase 2: Core Backend Implementation

### 2.1 Database Models
Create SQLAlchemy models for:
- `Event` - Major events (e.g., policy changes, market movements)
  - Fields: title, description, date, region, impact_level
  - Timestamps: created_at, updated_at, last_edited_by
- `Perspective` - Different regional viewpoints on events
  - Fields: event_id (FK), region, summary, key_points (JSON)
  - Links to sources
- `Metric` - Trackable financial/economic indicators
  - Fields: name, unit, category
- `MetricDataPoint` - Time series data
  - Fields: metric_id (FK), value, date, source_id (FK)
- `HistoricalPattern` - Patterns from historical analysis
  - Fields: name, description, time_period, relevance_score
- `Source` - URLs and documents with credibility ratings
  - Fields: url, title, credibility_tier (1-4), region, language
- `Analysis` - Research findings and synthesis
  - Fields: title, content (markdown), confidence_level, created_by

**Note**: Remove any task queue or automation fields - this is a content management system

### 2.2 Database Migrations
1. Set up Alembic for migrations
2. Create initial migration with all models
3. Optional: Add sample seed data for testing

### 2.3 API Endpoints
Create RESTful routes:

**Public Read Access**:
- `GET /api/events` - List events with pagination
- `GET /api/events/{id}` - Get event with perspectives
- `GET /api/metrics/{id}/history` - Time series data
- `GET /api/analysis/{id}` - Get analysis
- `GET /api/sources` - Browse sources

**Content Management** (you'll use via Claude Code):
- `POST /api/events` - Create event
- `PUT /api/events/{id}` - Update event
- `POST /api/perspectives` - Add perspective
- `POST /api/metrics/datapoint` - Add data point
- `POST /api/analysis` - Save analysis

**Admin**:
- `GET /api/health` - Health check
- `GET /api/stats` - Platform statistics

### 2.4 Helper Scripts
Create `backend/scripts/` utilities:
- `import_research.py` - Import research from JSON/markdown
- `add_event.py` - Quick event creation script
- `export_data.py` - Export to different formats

## Phase 3: Frontend Implementation

### 3.1 Core Pages
Create these main pages (Wikipedia-style):
- **Home/Dashboard** - Overview of recent research and key metrics
- **Events** - Timeline of power transition events
- **Event Detail** - Single event with multiple regional perspectives
- **Metrics** - Dashboard of tracked indicators
- **Metric Detail** - Time series with citations
- **Analysis Library** - Browse research findings
- **Sources** - Source library with credibility tiers
- **About** - Methodology and research principles

### 3.2 Dashboard Components
Build the home dashboard showing:
- Recent events added
- Key metrics (latest values)
- Featured analyses
- Source diversity statistics (% by region/language)

### 3.3 Event Detail View
Create UI for:
- Event overview (title, date, region, impact level)
- Multiple perspectives tabs (Western, Chinese, Russian, Arabic, etc.)
- Related metrics charts
- Source citations with credibility badges
- Related events (similar historical patterns)

### 3.4 Data Visualization
Implement components for:
- Time series charts (Recharts) for metric tracking
- Credibility badges (Tier 1-4 visual indicators)
- Confidence stars (⭐-⭐⭐⭐⭐⭐)
- Region/language diversity indicators
- Interactive timeline

## Phase 4: Research Templates & Initial Content

### 4.1 Create Research Approach Templates
In `research/approaches/`, create markdown templates:
- `source-diversification.md` - How to find non-Western sources
- `historical-matcher.md` - Mapping to historical patterns
- `counter-narrative.md` - Finding opposing viewpoints
- `data-collection.md` - Tracking metrics over time
- `credibility-scoring.md` - Rating sources and confidence levels
- `synthesis.md` - Combining multiple analyses

### 4.2 Initial Content (Optional)
Add 1-2 sample events to demonstrate the platform:
- Choose a current event (e.g., "BRICS currency discussions 2024")
- Use Claude Code to research it following Source Diversification approach
- Populate database with event, perspectives, sources

## Phase 5: Integration & Deployment

### 5.1 Integration Testing
1. Start all services with docker-compose
2. Verify database connection
3. Test API endpoints with Postman or curl
4. Verify frontend connects to backend
5. Test adding data via helper scripts

### 5.2 Documentation
1. Complete README.md with:
   - Quick start guide
   - Architecture overview
   - How to use Claude Code to add research
   - Deployment instructions
2. Add inline code documentation
3. Create API documentation (OpenAPI/Swagger auto-generated by FastAPI)

### 5.3 GitHub & Deployment
1. Push to GitHub repository
2. Set up deployment (Vercel for frontend, Railway/Fly.io for backend)
3. Configure environment variables in deployment platforms
4. Test live deployment

### 5.4 First Research Session with Claude Code
1. Start Claude Code: `claude`
2. Request research on a current event
3. Guide Claude Code through populating the database
4. Review and commit changes
5. Push to GitHub and verify auto-deployment

## Implementation Notes

### Development Approach
- Start with simplest working version
- Add complexity incrementally
- Test each component before moving on
- Commit frequently with clear messages via Claude Code
- Keep CLAUDE.md updated with learnings

### Priority Order
1. Get basic structure running (Phase 1)
2. Build database and API (Phase 2)
3. Create public-facing UI (Phase 3)
4. Add initial content via Claude Code research session (Phase 4)
5. Deploy to production (Phase 5)

### What NOT to Do
- ❌ Don't build automated agents or task queues
- ❌ Don't add Anthropic SDK or programmatic API calls
- ❌ Don't add Celery or background workers
- ❌ Don't over-engineer - keep it simple and working
- ❌ Don't worry about comprehensive test suites initially

### How You'll Use This
- **Development**: Claude Code CLI for building features
- **Research**: Claude Code (CLI or web) to add content
- **Updates**: Git commits pushed to GitHub → auto-deploy
- **Collaboration**: GitHub as source of truth

## Success Criteria

The initialization is successful when:
- ✅ All services start with `docker-compose up`
- ✅ Health check endpoint returns 200
- ✅ Frontend loads in browser and looks good
- ✅ Can view sample data in the UI
- ✅ API endpoints work (test with curl/Postman)
- ✅ Can use Claude Code to research and add new event
- ✅ Data persists in database
- ✅ Changes deploy to production automatically

---

**Remember**: You're building a content platform that YOU will update using Claude Code. Think of it like building Wikipedia, not like building an autonomous research robot.
