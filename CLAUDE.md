# Research Intelligence Platform

## Project Overview
This is a multi-agent research platform for analyzing global power transitions and capital flows. The system automates research, synthesis, and presentation through specialized AI agents, integrating with the Anthropic API and presenting findings in a Wikipedia-quality web interface.

## Core Mission
Build a production-grade research platform that:
- Automates 20 predefined research tasks through specialized agents
- Searches non-Western sources (Chinese, Russian, Arabic, Hindi, Middle Eastern)
- Tracks financial metrics across multiple currencies and regions
- Maps current events to historical power transition patterns
- Presents multi-perspective analysis in an interactive web interface
- Continuously updates with new data and maintains source credibility tracking

## Technology Stack

### Backend
- **Framework**: Python 3.12+ with FastAPI
- **Database**: PostgreSQL 16+ for structured data
- **Cache**: Redis 7.4+ (optional, for web caching only)
- **ORM**: SQLAlchemy with Alembic for migrations
- **Note**: NO automated API calls or background workers

### Frontend
- **Framework**: React 19 with TypeScript 5+
- **Build Tool**: Vite 6 (requires Node.js 20.19+ or 22.12+)
- **UI Components**: shadcn/ui (built on Radix UI)
- **Styling**: Tailwind CSS
- **Charts**: Recharts for data visualization
- **State Management**: React Query for server state

### Development Workflow
- **AI Assistant**: Claude Code (via CLI or https://claude.ai/code web interface)
- **Version Control**: Git with GitHub integration
- **CI/CD**: GitHub Actions for deployment
- **Deployment**: Vercel/Netlify (frontend), Railway/Fly.io (backend)

## Project Structure

```
research-intelligence-platform/
├── .github/                    # GitHub Actions workflows
│   └── workflows/              # Deployment automation
├── backend/
│   ├── api/
│   │   └── routes/            # FastAPI route handlers
│   ├── models/                # SQLAlchemy models
│   ├── services/              # Business logic layer
│   ├── scripts/               # Data import/maintenance scripts
│   ├── main.py                # FastAPI application
│   └── config.py              # Configuration management
├── frontend/
│   └── src/
│       ├── components/        # React components
│       ├── pages/            # Page-level components
│       ├── hooks/            # Custom React hooks
│       └── services/         # API client
├── research/                  # Research templates & notes
│   ├── approaches/           # Different research methodologies
│   └── findings/             # Session outputs
├── docs/                      # Project documentation
├── tests/                     # Test suites
├── docker-compose.yml         # Development environment
└── Makefile                   # Common development tasks
```

## Development Commands

### Setup
```bash
make setup              # Initial project setup
docker-compose up -d    # Start development environment
```

### Development
```bash
make dev               # Start dev servers
make lint              # Run all linters
make format            # Format code
```

### Database
```bash
make migrations msg="description"  # Create migration
make migrate                       # Apply migrations
```

## Code Style & Conventions

### Python
- Use **Black** for formatting (line length: 100)
- Use **isort** for import sorting
- Type hints are REQUIRED for all functions
- Docstrings using Google style
- Async/await for I/O operations
- Pydantic models for data validation

### TypeScript/React
- Use **Prettier** for formatting
- **ESLint** with TypeScript rules
- Functional components with hooks (no class components)
- Use TypeScript strict mode
- Descriptive component and variable names
- Extract reusable logic into custom hooks

### General Principles
- **DRY** (Don't Repeat Yourself)
- **SOLID** principles
- Explicit is better than implicit
- Fail fast with clear error messages
- Log extensively but meaningfully

## Research Methodology Templates

These are structured approaches you guide Claude Code through (not automated agents):

### How It Works
1. You describe research goal to Claude Code
2. Specify which approach to use (or let Claude suggest)
3. Claude Code uses web search, analysis, and structured output
4. Results are saved to database with proper citations
5. Changes committed to git with descriptive messages

### Available Research Approaches

**Source Diversification**
- Find perspectives from Chinese, Russian, Arabic, Hindi, Middle Eastern sources
- Compare Western vs non-Western framing of events
- Track which regions emphasize which aspects

**Data Collection**
- Track financial metrics over time (gold purchases, reserve %, currency flows)
- Gather data in multiple currencies (Yuan, Rupee, Ruble, Dirham, not just USD/EUR)
- Cite all data sources with credibility tiers

**Historical Matcher**
- Map current events to 8 historical power transition patterns
- Identify similarities and differences
- Assess which historical parallels are most relevant

**Counter Narrative**
- Find opposing viewpoints on same event
- Analyze different stakeholder perspectives
- Present balanced view without false equivalence

**Credibility Scorer**
- Rate sources Tier 1-4 (government data → social media)
- Assign confidence levels (1-5 stars) to claims
- Track source reliability over time

**Synthesis**
- Combine findings from multiple research sessions
- Create cohesive narratives from diverse perspectives
- Identify consensus points and genuine disagreements

## Database Schema Highlights

**Core Entities**:
- `ResearchTask`: 20 predefined tasks with status tracking
- `Event`: Major developments (e.g., "Saudi PIF pivot")
- `Perspective`: Regional views on each event
- `Metric`: Trackable indicators (gold purchases, reserve %)
- `HistoricalPattern`: 8 patterns from historical analysis
- `Source`: URLs with credibility tier and region
- `Analysis`: Agent outputs and synthesis results

## API Patterns

### Endpoints

#### Public Read Access (for Wikipedia-style viewing)
- `GET /api/events` - List all events with pagination
- `GET /api/events/{id}` - Get single event with perspectives
- `GET /api/metrics` - List tracked metrics
- `GET /api/metrics/{id}/history` - Time series data
- `GET /api/analysis/{id}` - Get analysis with sources
- `GET /api/sources` - Browse source library with credibility tiers

#### Content Management (used by you via Claude Code)
- `POST /api/events` - Add new event
- `PUT /api/events/{id}` - Update event
- `DELETE /api/events/{id}` - Remove event
- `POST /api/perspectives` - Add perspective to event
- `POST /api/metrics/datapoint` - Add metric data point
- `POST /api/analysis` - Save research analysis
- `POST /api/sources` - Register new source

#### Admin/Maintenance
- `GET /api/stats` - Platform statistics
- `POST /api/admin/rebuild-cache` - Rebuild Redis cache
- `GET /api/health` - Health check

### Response Format
All API responses follow:
```json
{
  "success": boolean,
  "data": {...},
  "error": string | null,
  "metadata": {
    "timestamp": string,
    "request_id": string
  }
}
```

### Usage Pattern
During a Claude Code research session:
1. Claude Code searches web for information
2. Analyzes and structures findings
3. Makes POST/PUT requests to API to save data
4. Or directly inserts to database via SQLAlchemy scripts
5. Commits changes to git when complete

## Environment Variables

Required in `.env`:
```
DATABASE_URL=postgresql://user:pass@localhost/research_db
REDIS_URL=redis://localhost:6379  # Optional, for web caching
SECRET_KEY=your_secret_key_for_sessions
FRONTEND_URL=http://localhost:3000
```

**Note**: No ANTHROPIC_API_KEY needed - you're using Claude Code via Max subscription

## Research Methodology

The platform follows these principles:
1. **Multi-perspective**: Always search non-Western sources
2. **Currency diversity**: Check data in Yuan, Rupee, Ruble, Dirham, not just Dollar/Euro
3. **Historical context**: Map current events to historical patterns
4. **Source credibility**: Track and rate all sources (Tier 1-4)
5. **Explicit uncertainty**: Use confidence levels for all claims

## Git Workflow

- **main**: Production-ready code (protected)
- **develop**: Integration branch (protected)
- **feature/\***: Feature development
- **hotfix/\***: Urgent fixes

Conventional commits:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Maintenance tasks

## GitHub Integration & Deployment

### Repository Setup
1. Create GitHub repository for the project
2. Push initial code: `git remote add origin <url> && git push -u origin main`
3. Set up branch protection rules for `main`

### Claude Code Web Interface
- Access at: https://claude.ai/code
- Connect your GitHub account for seamless integration
- Claude Code can read and edit files via GitHub
- Changes are committed with proper attribution
- Works great for reviewing code and making updates from anywhere

### Deployment Strategy

**Frontend (React)**
- **Vercel** (recommended): Connect GitHub repo, auto-deploy on push
- **Netlify**: Similar GitHub integration, excellent CDN
- **GitHub Pages**: Free for public repos

**Backend (FastAPI)**
- **Railway**: Easy Python deployment, auto-detects FastAPI
- **Fly.io**: Great for containers, free tier available
- **DigitalOcean App Platform**: Simple deployment from GitHub

**Database**
- Use managed PostgreSQL from your hosting provider
- Or: Supabase (free tier with 500MB)
- Or: Neon (serverless Postgres)

### GitHub Actions Workflows

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy Frontend
        # Vercel/Netlify auto-deploys via webhook
      - name: Deploy Backend
        # Railway/Fly.io auto-deploys via webhook
```

**Note**: Most modern platforms auto-deploy from GitHub without complex CI/CD

## Working with Claude Code

### How You'll Work
You have a **Claude Max subscription** and will use Claude Code manually (not automated API calls):
- **CLI**: Run `claude` in your project directory
- **Web Interface**: Use https://claude.ai/code with GitHub integration
- **No API costs**: You're using your Max subscription, not programmatic API calls

### Claude Code Capabilities

#### File Operations
- **Read**: View files with line numbers
- **Edit**: Make precise string replacements
- **Write**: Create new files (prefers Edit for existing files)
- **Glob**: Fast file pattern matching (`**/*.py`, `src/**/*.ts`)
- **Grep**: Search code content with regex

#### Execution & Planning
- **Bash**: Run terminal commands (git, npm, docker, etc.)
- **Plan Mode**: Claude presents implementation plans before executing
- **TodoWrite**: Proactive task tracking and progress updates
- **Task (Sub-agents)**: Delegate complex tasks to specialized agents:
  - **Explore**: Fast codebase exploration and analysis
  - **general-purpose**: Complex multi-step research and implementation

#### Git Workflows
- Automated commit creation with conventional commits
- Pull request creation via `gh` CLI
- Only commits when explicitly requested
- Never skips hooks or uses `--no-verify`
- Includes co-author attribution: `Co-Authored-By: Claude <noreply@anthropic.com>`

### Typical Research Session

1. **Start Claude Code**
   ```bash
   cd research-intelligence-platform
   claude  # Or use https://claude.ai/code
   ```

2. **Request Research**
   ```
   "Research Chinese and Russian perspectives on the Saudi PIF pivot away from
   the dollar. Use web search to find sources, analyze the findings, and update
   the database with a new Event and associated Perspectives."
   ```

3. **Claude Code Will:**
   - Present a plan in Plan Mode
   - Use web search (included in Max subscription)
   - Analyze and synthesize information
   - Generate SQL inserts or API calls
   - Update database via backend API or scripts
   - Commit changes with descriptive message

4. **You Review & Deploy**
   - Review the changes
   - Push to GitHub
   - Auto-deploy via GitHub Actions

### Research Approaches (Not Automated Agents)

These are methodologies you can ask Claude Code to follow:

- **Source Diversification**: Find non-Western perspectives (Chinese, Russian, Arabic, Hindi sources)
- **Historical Matcher**: Map current events to historical power transition patterns
- **Counter Narrative**: Find and analyze opposing viewpoints
- **Data Collection**: Track financial metrics over time with citations
- **Credibility Scorer**: Rate sources and assign confidence levels
- **Synthesis**: Combine multiple analyses into cohesive findings

Example request: *"Use the Source Diversification approach to research BRICS currency proposals"*

### When Making Changes

1. **Plan First**: Claude Code uses Plan Mode - review before execution
2. **Read Before Edit**: Always reads files before editing (required by Edit tool)
3. **Commit Frequently**: With descriptive conventional commit messages
4. **Update Documentation**: Keep this CLAUDE.md current with learnings
5. **Test Critical Paths**: Verify database operations and API endpoints

## Claude Max Usage Best Practices

Since you're using your Max subscription (not paying per API call):

### Efficient Usage
- **Web Search**: Included but use judiciously (comes with context costs)
- **Context Management**: Use sub-agents (Task tool) for complex explorations to avoid filling context
- **Iterative Approach**: Break large research into sessions to stay within rate limits
- **Caching**: Let Claude Code cache file reads automatically

### What to Watch
- **Rate Limits**: Max has generous limits but they exist
- **Session Length**: Very long sessions may hit context limits
- **Web Search**: Each search adds context - be specific in queries

### Cost-Free Advantages
- No per-token anxiety - iterate freely
- Experiment with approaches without cost concerns
- Use web search liberally for current information
- Leverage Claude Sonnet 4.5 (best coding model) included in Max

## Security Notes

- Never commit `.env` file
- Use environment variables for all secrets
- Sanitize all user inputs
- Rate limit public APIs
- Follow OWASP top 10 guidelines

## Testing Philosophy

- Write tests for critical paths (not everything)
- Mock external API calls (Anthropic, web searches)
- Use fixtures for complex test data
- Focus on integration tests for key workflows
- Practical testing over dogmatic TDD

## Documentation Standards

- Update README.md for user-facing changes
- Update this CLAUDE.md for development guidance
- Document complex algorithms inline
- Keep API documentation in sync (OpenAPI)
- Add ADRs (Architecture Decision Records) for major decisions

## Current Focus

This is a new project being initialized. The immediate priorities are:
1. Set up project structure and dependencies
2. Create database schema and migrations
3. Build RESTful API with FastAPI
4. Create React 19 frontend with Vite 6
5. Build Wikipedia-style UI for displaying research
6. Create research approach templates
7. Conduct first research session with Claude Code

## Notes for Claude Code

### Key Principles
- This project values **clarity over cleverness**
- We prioritize **working code over perfect code** initially
- **Iterate and refine** rather than trying to build everything at once
- **Ask questions** when requirements are ambiguous using AskUserQuestion tool
- **Suggest improvements** to architecture or patterns

### Working with This Project
- Use **Plan Mode** to present plans before executing
- Use **TodoWrite** to track progress on multi-step tasks
- Use **Read before Edit** (required by Edit tool)
- Use **web search** liberally for current information (included in Max)
- **Commit frequently** with conventional commit messages
- Include **co-author attribution** in commits
- Update this CLAUDE.md as you learn project patterns

### What Makes This Project Unique
- **No automated agents** - manual research via Claude Code sessions
- **No API costs** - using Max subscription, not programmatic API
- **Wikipedia-style** - public-facing content platform
- **Manual curation** - quality over automation
- **Git as history** - every research session is documented in commits

### Tools to Emphasize
- **Web Search**: For finding diverse sources
- **Structured Output**: For populating database properly
- **Git Workflows**: For tracking research history
- **API Calls**: Using requests/httpx to populate backend

---

*This file is a living document. Update it via Edit tool as the project evolves.*
