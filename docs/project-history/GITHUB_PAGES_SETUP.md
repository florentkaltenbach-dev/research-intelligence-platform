# GitHub Pages Setup - Todo List

**Created**: 2025-10-27
**Goal**: Set up GitHub Pages with markdown content that Claude Code can directly read/edit

## Status: Ready to Start (waiting for claudeuser)

## Todos

- [ ] **Fix git repository ownership permissions for claudeuser**
  - Run: `git config --global --add safe.directory /home/claudeuser/research-intelligence-platform`

- [ ] **Explore existing research content**
  - Check research.db structure
  - Review markdown files in research/findings/
  - Understand current content organization

- [ ] **Design GitHub Pages content structure**
  - events/ directory for major developments
  - perspectives/ by region/event
  - metrics/ for time-series data
  - timeline.md for chronological view
  - sources.md for source library

- [ ] **Set up GitHub Pages configuration**
  - Create docs/_config.yml
  - Choose Jekyll theme
  - Create docs/index.md homepage

- [ ] **Export existing database content to markdown**
  - Extract events from research.db
  - Create markdown files in docs/events/
  - Preserve existing research findings

- [ ] **Study existing research and create content pages**
  - Review global_capital_flows_2025_verified.md
  - Break into individual event pages
  - Create perspective pages by region

- [ ] **Create navigation structure**
  - Timeline view
  - Events index
  - Sources library
  - Cross-linking between pages

- [ ] **Test GitHub Pages locally and prepare for push**
  - Test Jekyll build locally
  - Verify all markdown renders correctly
  - Ready for git push

## Target Structure

```
docs/                          # GitHub Pages root
├── _config.yml               # Jekyll config
├── index.md                  # Homepage/timeline
├── events/
│   ├── index.md             # Events catalog
│   ├── saudi-pif-pivot.md
│   ├── central-bank-gold.md
│   ├── brics-payments.md
│   ├── china-cips.md
│   ├── islamic-finance.md
│   └── capital-flight-uae.md
├── perspectives/
│   ├── chinese/
│   ├── russian/
│   ├── middle-eastern/
│   ├── indian/
│   └── western/
├── metrics/
│   └── [CSV or markdown tables]
└── sources.md               # Source credibility library
```

## Workflow After Setup

1. Claude Code reads markdown files directly
2. When doing research: Claude edits markdown → commits
3. Push to GitHub → Pages updates automatically
4. No database queries needed - all content in git
