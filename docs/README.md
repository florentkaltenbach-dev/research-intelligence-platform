# Research Intelligence Platform - GitHub Pages

This directory contains the GitHub Pages site for the Research Intelligence Platform.

## Structure

```
docs/
├── _config.yml              # Jekyll configuration
├── index.md                 # Homepage with timeline
├── events/
│   ├── index.md            # Events catalog
│   ├── saudi-pif-repositioning.md
│   ├── central-bank-gold-2024.md
│   ├── brics-payment-systems.md
│   ├── china-cips-expansion.md
│   ├── el-salvador-bitcoin-reversal.md
│   ├── islamic-finance-growth.md
│   └── capital-flight-uae-singapore.md
├── perspectives/
│   ├── index.md            # Perspectives overview
│   └── indian/
│       └── index.md        # Sample perspective
├── historical-patterns/
│   └── index.md            # Historical patterns catalog
└── sources.md              # Credibility-tiered source library
```

## Deployment to GitHub Pages

### Option 1: From Repository Settings (Recommended)

1. **Push to GitHub**:
   ```bash
   git add docs/
   git commit -m "feat: add GitHub Pages structure with events, perspectives, and sources"
   git push origin master
   ```

2. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `master`
   - Folder: `/docs`
   - Click Save

3. **Wait for build** (1-2 minutes)
   - GitHub Actions will build Jekyll site automatically
   - Site will be available at: `https://username.github.io/research-intelligence-platform/`

### Option 2: Local Testing (Optional)

To test Jekyll locally before pushing:

```bash
# Install Jekyll (requires Ruby)
gem install jekyll bundler

# Navigate to docs directory
cd docs/

# Create Gemfile
cat > Gemfile << 'EOF'
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
gem "jekyll-seo-tag"
gem "jekyll-sitemap"
EOF

# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Visit http://localhost:4000
```

## Content Overview

### Events (7 Major Developments)
1. **Saudi PIF Repositioning** - $913B fund reducing US equity 61%
2. **Central Bank Gold** - 3,220 tonnes accumulated (2022-2024)
3. **BRICS Payment Systems** - Fragmentation NOT unity
4. **China's CIPS** - 189 countries, yuan payment infrastructure
5. **El Salvador Bitcoin** - Legal tender reversal after 3.5 years
6. **Islamic Finance** - $6T → $9.7T projected growth
7. **Capital Flight** - 142,000 millionaires relocating to UAE/Singapore

### Perspectives (Multi-Regional Analysis)
- Chinese: Infrastructure development, yuan internationalization
- Russian: Sanctions circumvention, gold reserves
- Middle Eastern: Multi-alignment, Islamic finance
- **Indian: Explicit rejection of de-dollarization** (critical perspective)
- Western: Dollar dominance analysis, threat assessment
- African: Alternative development finance

### Historical Patterns (8 Transitions)
- Mamluk-Ottoman (1517) - Technology gap
- Ming-Qing (1644) - Defection over conquest
- Mongol Fragmentation - Competing successors
- British-American (1914-1944) - 30-year infrastructure transition
- Soviet Collapse - Internal contradictions
- British Slave Trade Abolition - Strategic retreat as moral progress

### Sources (100+ Verified)
- **Tier 1**: Official government sources, central banks, system operators
- **Tier 2**: Established media (Bloomberg, Arab News, SCMP, Al Jazeera)
- **Tier 3**: Academic/think tank publications
- **Tier 4**: Social media/unverified (rarely used, explicitly noted)

## Confidence Levels

All research uses explicit confidence ratings:
- ⭐⭐⭐⭐⭐ (5/5): Multiple Tier 1 sources, cross-regional verification
- ⭐⭐⭐⭐ (4/5): Tier 1-2 sources with corroboration
- ⭐⭐⭐ (3/5): Tier 2 sources or single Tier 1
- ⭐⭐ (2/5): Tier 3 sources or uncorroborated
- ⭐ (1/5): Speculation or Tier 4 sources

## Theme Customization

Current theme: `jekyll-theme-cayman`

To change theme, edit `_config.yml`:

```yaml
theme: jekyll-theme-minimal
# Options: minimal, slate, modernist, architect, tactile, time-machine
```

Or use remote theme for more options:

```yaml
remote_theme: pages-themes/slate@v0.2.0
plugins:
  - jekyll-remote-theme
```

## Adding New Content

### New Event
1. Create `docs/events/event-name.md`
2. Add front matter:
   ```yaml
   ---
   layout: default
   title: "Event Title"
   date: YYYY-MM-DD
   confidence: 1-5
   regions: ["Region1", "Region2"]
   ---
   ```
3. Add to `docs/events/index.md`
4. Update `docs/index.md` timeline if recent

### New Perspective
1. Create `docs/perspectives/region/topic.md`
2. Use front matter with `region` tag
3. Link from `docs/perspectives/index.md`

### New Historical Pattern
1. Create `docs/historical-patterns/pattern-name.md`
2. Include relevance score (0.00-1.00)
3. Add to `docs/historical-patterns/index.md`

## SEO & Metadata

Jekyll SEO plugin automatically generates:
- Meta descriptions
- Open Graph tags
- Twitter cards
- Sitemap

To customize for event pages, add to front matter:

```yaml
description: "Brief event summary for search results"
image: /assets/images/event-image.jpg  # Optional
```

## Navigation

Site uses simple markdown links:
- `[Text](/path/)` for internal links
- `[Text](https://external.com)` for external

All pages have footer navigation:
```
[← Back to Home](/) | [View Events](/events/) | [Perspectives](/perspectives/)
```

## Maintenance

### Updating Research
When Claude Code adds new research:
1. Add new markdown file to appropriate section
2. Update index pages
3. Update timeline on homepage if recent
4. Commit with descriptive message

### Monitoring
- Check GitHub Actions for build failures
- Test links periodically
- Update sources library with new research

## Next Steps

1. **Immediate**: Push to GitHub, enable Pages
2. **Short-term**: Add remaining perspective pages
3. **Medium-term**: Create detailed historical pattern pages
4. **Ongoing**: Update with new research sessions

---

**Last Updated**: October 27, 2025
**Status**: Ready for deployment
**Content**: 7 events, 1 perspective, 8 pattern summaries, 100+ sources
