# Research Intelligence Platform

Multi-perspective analysis of global power transitions and capital flows, published as Wikipedia-style research on GitHub Pages.

**Live Site**: `https://[username].github.io/research-intelligence-platform/` (configure in repo settings)

## Overview

This platform curates research on financial architecture shifts through verified sources from Western, Chinese, Russian, Middle Eastern, Indian, and African perspectives. All content lives as markdown files in `docs/` and is published via GitHub Pages with Jekyll.

**Key Principle**: This is a **manually curated research platform**, not an automated system. Research is conducted using Claude Code, synthesized into structured markdown, and published via git commits.

## Current Research Content

### 📌 19+ Major Events (2022-2025)
- Saudi PIF $913B repositioning (61% US equity reduction)
- Central bank gold accumulation (3,220 tonnes over 3 years)
- BRICS payment systems (fragmented, not unified)
- China's CIPS expansion (185+ countries, $24.47T processed)
- El Salvador Bitcoin reversal (IMF-mandated rollback)
- Islamic Finance growth ($6T → $9.7T projected)
- Capital flight to UAE/Singapore (142,000 millionaires)
- Plus: US-China semiconductor war, India's strategic autonomy, dollar weaponization, etc.

### 🌍 50+ Regional Perspectives
Multi-angle analysis on each event from:
- **Western** (US, European)
- **Chinese** (state media, academic, official sources)
- **Russian** (sanctions circumvention focus)
- **Middle Eastern** (Gulf finance, Islamic banking)
- **Indian** (multi-alignment strategy)
- **African** (resource competition, alternative systems)
- **Global South** (non-aligned perspective)

### 📊 4 Comprehensive Synthesis Reports
- Global Capital Flows October 2025 Update
- Historical Power Transitions (8 cases)
- Emerging Patterns 2023-2025
- Multi-perspective thematic analysis

### 📚 Source Library
18+ credibility-tiered sources (Tier 1-4) from government data, established media, think tanks, and regional outlets.

## Technology Stack

### Published Content
- **Static Site**: Jekyll on GitHub Pages
- **Theme**: Cayman (configurable in `docs/_config.yml`)
- **Content**: Markdown files in `docs/` directory
- **Deployment**: Auto-deploy on push to main

### Optional Backend/Frontend (Development Phase)
- **Backend**: Python 3.12+ with FastAPI, PostgreSQL, SQLAlchemy
- **Frontend**: React 19 with TypeScript 5+, Vite 6, TailwindCSS
- **Note**: Backend/frontend are for content management during research. Public output is static GitHub Pages.

## Quick Start for Contributors

### 1. Clone Repository
```bash
git clone <repo-url>
cd research-intelligence-platform
```

### 2. View Content
All research is in `docs/`:
```
docs/
├── index.md                    # Homepage with timeline
├── events/                     # 19+ event files
├── perspectives/               # 50+ regional perspectives
├── analyses/                   # 4 synthesis reports
├── historical-patterns/        # Power transition parallels
└── sources.md                  # Credibility-tiered source library
```

### 3. Enable GitHub Pages
- Go to repo **Settings → Pages**
- Source: **Deploy from a branch**
- Branch: **main** → Folder: **/docs**
- Wait 1-2 minutes for build

### 4. Conduct Research with Claude Code
```bash
claude  # or use https://claude.ai/code
```

Example request:
```
Research "Central bank digital currencies Q4 2025" using Source Diversification approach.
Find Chinese, Russian, and Middle Eastern perspectives. Create an event file in docs/events/
with proper front matter, regional perspectives, and citations.
```

Claude Code will:
- Search web for multi-regional sources
- Synthesize findings into structured markdown
- Create/update files in `docs/`
- Commit with descriptive message

### 5. Push to Publish
```bash
git add docs/
git commit -m "feat: add CBDC analysis with Chinese/Russian perspectives"
git push origin main
```

GitHub Pages auto-rebuilds within 1-2 minutes.

## Project Structure

```
research-intelligence-platform/
├── docs/                        # GitHub Pages content (public)
│   ├── _config.yml             # Jekyll configuration
│   ├── index.md                # Homepage
│   ├── events/                 # Major developments
│   ├── perspectives/           # Regional viewpoints
│   ├── analyses/               # Synthesis reports
│   ├── historical-patterns/    # Historical parallels
│   └── sources.md              # Source library
├── backend/                     # Optional: FastAPI backend
│   ├── api/routes/             # API endpoints
│   ├── models/                 # Database models
│   └── scripts/                # Data management
├── frontend/                    # Optional: React UI
│   └── src/                    # React components
├── research/                    # Research templates
│   └── approaches/             # Methodologies
├── docker-compose.yml           # Dev environment
├── README.md                    # This file
└── CLAUDE.md                    # Developer instructions
```

## Research Methodology

### Multi-Perspective Analysis
✅ Always search non-Western sources (Chinese, Russian, Arabic, Hindi, Middle Eastern)
✅ Compare how different regions frame the same events
✅ Track source credibility with 4-tier system

### Currency Diversity
✅ Data in Yuan, Rupee, Ruble, Dirham (not just USD/EUR)
✅ Track financial metrics in original currencies
✅ Note exchange rate assumptions

### Historical Context
✅ Map current events to 8 historical power transition patterns
✅ Assign relevance scores (0.00-1.00) to historical parallels
✅ Identify similarities and differences

### Explicit Uncertainty
✅ Confidence levels (1-5 stars) on all claims
✅ Source credibility tiers (Tier 1-4)
✅ Clear distinction between facts and analysis

## Content Templates

### Event File Template
```yaml
---
layout: default
title: "Event Title"
date: YYYY-MM-DD
event_type: "Category"
confidence: 1-5
regions: ["Region1", "Region2"]
---

# Event Title

**Executive Summary**: 2-3 sentences

## Verified Facts
- Bullet list with sources

## Regional Perspectives

### Chinese View
**Source**: Outlet names
- Framing
- Emphasis
- Quote

### Western View
...

## Historical Parallels
Pattern name (relevance: 0.XX)

## Data & Metrics
| Metric | 2023 | 2024 | 2025 |
|--------|------|------|------|

## Related Events
- [Event 1](/events/slug)

[← Back to Events](/events/)
```

### Source Credibility Tiers
- **Tier 1**: Government/official sources, central banks, system operators
- **Tier 2**: Established media (Bloomberg, SCMP, Arab News, Al Jazeera)
- **Tier 3**: Academic publications, think tanks
- **Tier 4**: Social media, unverified sources (rarely used, explicitly noted)

### Confidence Levels
- ⭐⭐⭐⭐⭐ (5/5): Multiple Tier 1 sources, cross-regional verification
- ⭐⭐⭐⭐ (4/5): Tier 1-2 sources with corroboration
- ⭐⭐⭐ (3/5): Tier 2 sources or single Tier 1
- ⭐⭐ (2/5): Tier 3 sources or uncorroborated
- ⭐ (1/5): Speculation or Tier 4 sources

## Key Findings (October 2025)

### What Western Analysis Systematically Misses
1. **Scale Blindness** - Islamic finance ($6T) exceeds many G20 economies
2. **Infrastructure Determinism** - Payment systems built before currency adoption
3. **Optionality Over Replacement** - Countries building alternatives for OPTIONS, not replacement
4. **False Unity Narratives** - "BRICS de-dollarization" is Western construct; reality is fragmented systems
5. **Incrementalism vs Revolution** - No dramatic collapse; systematic erosion through thousand cuts

### Most Likely Outcome: Hybrid Multipolar System by 2030
**Projected:**
- Dollar: 58% → 40-45% of reserves (dominant but not monopolistic)
- Yuan zone: Asia, Africa, parts of Middle East
- Gold: 15% → 20-25% of reserves
- Islamic finance: $10T+ by 2035

**NOT Happening:**
- ❌ Dollar collapse (too binary)
- ❌ BRICS triumph (too fragmented)
- ❌ Status quo maintained (ignores structural shifts)

## Development Setup (Optional)

If you want to run the backend/frontend for content management:

### Prerequisites
- Python 3.12+, Node.js 20.19+, Docker & Docker Compose
- PostgreSQL 16+ (via Docker or local)

### Setup
```bash
# Start database
docker-compose up -d

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
python main.py  # Runs on :8000

# Frontend
cd frontend
npm install
npm run dev  # Runs on :3000
```

**Note**: Most contributors won't need the backend/frontend. Research is added directly as markdown files in `docs/`.

## Testing Locally with Jekyll (Optional)

```bash
cd docs/
gem install jekyll bundler
bundle exec jekyll serve
# Visit http://localhost:4000
```

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/topic-name`
3. Add research to `docs/` following templates
4. Commit: `git commit -m "feat: add analysis of [topic]"`
5. Push and create Pull Request
6. Merge → auto-deploys to GitHub Pages

## Documentation

- **`README.md`** (this file): Project overview and quick start
- **`CLAUDE.md`**: Detailed development instructions for Claude Code
- **`TODO.md`**: Current priorities and active tasks
- **`docs/README.md`**: GitHub Pages structure and deployment guide
- **`docs/project-history/`**: Archived project status documents

## License

MIT License - See LICENSE file for details

## Acknowledgments

Research conducted with **Claude Code** using Claude Max subscription.
All analysis commits include: `Co-Authored-By: Claude <noreply@anthropic.com>`

---

**Current Status**: Active research platform with 19+ events, 50+ perspectives, 100+ verified sources
**Last Major Update**: October 27, 2025
**Confidence**: ⭐⭐⭐⭐ (4/5 - High confidence with noted uncertainties)
