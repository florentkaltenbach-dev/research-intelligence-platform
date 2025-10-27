#!/usr/bin/env python3
"""
Export PostgreSQL content via API to GitHub Pages markdown structure
"""

import requests
import os
import re
import json
from datetime import datetime

API_BASE = "http://localhost:8000/api"

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def export_events():
    """Export all events from API"""
    print("\n" + "=" * 60)
    print("EXPORTING EVENTS")
    print("=" * 60)

    response = requests.get(f"{API_BASE}/events/?limit=100")
    events = response.json()

    print(f"Found {len(events)} events")

    for event in events:
        title = event['title']
        slug = slugify(title)

        # Get full event details with embedded perspectives
        event_detail = requests.get(f"{API_BASE}/events/{event['id']}").json()
        perspectives = event_detail.get('perspectives', [])

        content = f"""---
layout: default
title: "{title}"
date: {event.get('date', '2025-01-01').split('T')[0]}
region: "{event.get('region', 'Global')}"
impact: "{event.get('impact_level', 'high')}"
---

# {title}

**Date**: {event.get('date', 'Ongoing').split('T')[0]}
**Region**: {event.get('region', 'Global')}
**Impact Level**: {event.get('impact_level', 'High')}

---

## Overview

{event.get('description', 'Detailed analysis of this strategic development.')}

---

## Regional Perspectives

"""

        for persp in perspectives:
            content += f"""### {persp.get('region', 'Unknown')} Perspective

{persp.get('summary', 'Regional analysis')}

"""
            if persp.get('key_points'):
                try:
                    key_points = json.loads(persp['key_points']) if isinstance(persp['key_points'], str) else persp['key_points']
                    if key_points:
                        content += "**Key Points**:\n"
                        for point in key_points:
                            content += f"- {point}\n"
                except:
                    pass

            content += "\n---\n\n"

        content += f"""
## Related Content

- [View All Events](/events/)
- [Explore Perspectives](/perspectives/)
- [Historical Patterns](/historical-patterns/)

---

**Event ID**: {event['id']}
**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

[← Back to Events](/events/)
"""

        filename = f"docs/events/{slug}.md"
        with open(filename, 'w') as f:
            f.write(content)
        print(f"  ✓ {slug}")

    return len(events)

def export_perspectives():
    """Export all perspectives organized by region"""
    print("\n" + "=" * 60)
    print("EXPORTING PERSPECTIVES")
    print("=" * 60)

    # Get all events with embedded perspectives
    events_response = requests.get(f"{API_BASE}/events/?limit=100")
    events_list = events_response.json()

    # Collect all perspectives
    all_perspectives = []
    for event in events_list:
        # Get full event details with perspectives
        event_detail = requests.get(f"{API_BASE}/events/{event['id']}").json()
        perspectives = event_detail.get('perspectives', [])
        for p in perspectives:
            p['event'] = event
            all_perspectives.append(p)

    print(f"Found {len(all_perspectives)} perspectives")

    # Group by region
    by_region = {}
    for p in all_perspectives:
        region = p.get('region', 'Unknown')
        if region not in by_region:
            by_region[region] = []
        by_region[region].append(p)

    # Export each region
    for region, persp_list in by_region.items():
        region_slug = slugify(region)
        os.makedirs(f"docs/perspectives/{region_slug}", exist_ok=True)

        content = f"""---
layout: default
title: "{region} Perspectives"
region: "{region}"
---

# {region} Perspectives on Global Power Transitions

**Total Perspectives**: {len(persp_list)}

---

## Overview

This section presents {region}'s viewpoints on major global strategic developments.

---

## Perspectives by Event

"""

        for p in persp_list:
            event = p['event']
            event_slug = slugify(event['title'])

            content += f"""### [{event['title']}](/events/{event_slug})

{p.get('summary', 'Regional analysis')}

"""
            if p.get('key_points'):
                try:
                    key_points = json.loads(p['key_points']) if isinstance(p['key_points'], str) else p['key_points']
                    if key_points:
                        content += "**Key Points**:\n"
                        for point in key_points:
                            content += f"- {point}\n"
                except:
                    pass

            content += "\n---\n\n"

        content += "\n[← Back to All Perspectives](/perspectives/)\n"

        filename = f"docs/perspectives/{region_slug}/index.md"
        with open(filename, 'w') as f:
            f.write(content)
        print(f"  ✓ {region_slug}")

    return len(all_perspectives)

def export_analyses():
    """Export all analyses"""
    print("\n" + "=" * 60)
    print("EXPORTING ANALYSES")
    print("=" * 60)

    response = requests.get(f"{API_BASE}/analyses/?limit=100")
    analyses = response.json()

    print(f"Found {len(analyses)} analyses")

    os.makedirs("docs/analyses", exist_ok=True)

    for analysis in analyses:
        slug = slugify(analysis['title'])

        content = f"""---
layout: default
title: "{analysis['title']}"
date: {analysis.get('created_at', '2025-10-27').split('T')[0]}
confidence: {analysis.get('confidence_level', 4)}
---

# {analysis['title']}

**Date**: {analysis.get('created_at', '2025-10-27').split('T')[0]}
**Confidence**: {'⭐' * analysis.get('confidence_level', 4)} ({analysis.get('confidence_level', 4)}/5)
**Research Approach**: {analysis.get('research_approach', 'Multi-perspective synthesis')}

---

## Full Analysis

{analysis.get('content', 'Comprehensive analysis of global power transition patterns.')}

---

**Analysis ID**: {analysis['id']}

[← Back to Home](/) | [View Events](/events/) | [Perspectives](/perspectives/)
"""

        filename = f"docs/analyses/{slug}.md"
        with open(filename, 'w') as f:
            f.write(content)
        print(f"  ✓ {slug}")

    return len(analyses)

def export_sources():
    """Export all sources"""
    print("\n" + "=" * 60)
    print("EXPORTING SOURCES")
    print("=" * 60)

    response = requests.get(f"{API_BASE}/sources/?limit=100")
    sources = response.json()

    print(f"Found {len(sources)} sources")

    # Group by region
    by_region = {}
    for source in sources:
        region = source.get('region', 'Global')
        if region not in by_region:
            by_region[region] = []
        by_region[region].append(source)

    # Create comprehensive sources page
    content = f"""---
layout: default
title: "Source Library"
---

# Source Library: Credibility-Tiered Sources

All research uses {len(sources)} credibility-tiered sources organized by region.

---

## Sources by Region

"""

    for region, sources_list in sorted(by_region.items()):
        content += f"""### {region} ({len(sources_list)} sources)

"""
        for source in sources_list:
            tier = source.get('credibility_tier', 'Unknown')
            content += f"""**{source.get('title', source.get('name', 'Unknown Source'))}**
- **Credibility Tier**: {tier}
- **URL**: {source.get('url', 'N/A')}
- **Publisher**: {source.get('publisher', 'Unknown')}
- **Language**: {source.get('language', 'Unknown')}

"""
        content += "---\n\n"

    content += """
## Credibility Tier Definitions

- **Tier 1**: Government/Official sources
- **Tier 2**: Established media outlets
- **Tier 3**: Academic/think tank publications
- **Tier 4**: Social media/unverified sources

---

[← Back to Home](/)
"""

    with open("docs/sources.md", 'w') as f:
        f.write(content)
    print(f"  ✓ sources.md (comprehensive source library)")

    return len(sources)

def main():
    """Main export function"""
    print("\n" + "=" * 70)
    print("EXPORTING ALL CONTENT FROM POSTGRESQL API TO GITHUB PAGES")
    print("=" * 70)

    # Export all content
    events_count = export_events()
    perspectives_count = export_perspectives()
    analyses_count = export_analyses()
    sources_count = export_sources()

    # Summary
    print("\n" + "=" * 70)
    print("EXPORT COMPLETE")
    print("=" * 70)
    print(f"✓ {events_count} events exported")
    print(f"✓ {perspectives_count} perspectives exported")
    print(f"✓ {analyses_count} analyses exported")
    print(f"✓ {sources_count} sources exported")
    print("\nAll content now in docs/ ready for GitHub Pages!")

if __name__ == "__main__":
    main()
