#!/usr/bin/env python3
"""
Export research.db content to GitHub Pages markdown structure
"""

import sqlite3
import os
import re
from datetime import datetime

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def export_events(conn):
    """Export all events to docs/events/"""
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, date, description, region, impact_level
        FROM events
        ORDER BY date DESC
    ''')
    events = cursor.fetchall()

    print(f"Exporting {len(events)} events...")

    for event in events:
        event_id, title, date, description, region, impact = event
        slug = slugify(title)

        # Get perspectives for this event
        cursor.execute('''
            SELECT region, summary, key_points
            FROM perspectives
            WHERE event_id = ?
            ORDER BY region
        ''', (event_id,))
        perspectives = cursor.fetchall()

        # Create markdown content
        content = f"""---
layout: default
title: "{title}"
date: {str(date).split()[0] if date else '2025-01-01'}
region: "{region or 'Global'}"
impact: "{impact or 'high'}"
---

# {title}

**Date**: {str(date).split()[0] if date else 'Ongoing'}
**Region**: {region or 'Global'}
**Impact Level**: {impact or 'High'}

---

## Overview

{description or 'Detailed analysis of this strategic development.'}

---

## Regional Perspectives

"""

        # Add perspectives
        for persp_region, summary, key_points in perspectives:
            content += f"""### {persp_region} Perspective

{summary or 'Analysis of event from regional standpoint'}

**Key Points**: {key_points or 'Strategic implications and regional priorities'}

---

"""

        # Add footer
        content += f"""
## Related Content

- [View All Events](/events/)
- [Explore Perspectives](/perspectives/)
- [Historical Patterns](/historical-patterns/)

---

**Event ID**: {event_id}
**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

[← Back to Events](/events/)
"""

        # Write file
        filename = f"docs/events/{slug}.md"
        with open(filename, 'w') as f:
            f.write(content)
        print(f"  ✓ {filename}")

    return events

def export_perspectives(conn):
    """Export all perspectives to docs/perspectives/"""
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, event_id, region, summary, key_points, language
        FROM perspectives
        ORDER BY region, event_id
    ''')
    perspectives = cursor.fetchall()

    print(f"\nExporting {len(perspectives)} perspectives...")

    # Group by region
    by_region = {}
    for p in perspectives:
        region = p[2]
        if region not in by_region:
            by_region[region] = []
        by_region[region].append(p)

    # Export each region
    for region, persp_list in by_region.items():
        region_slug = slugify(region)
        os.makedirs(f"docs/perspectives/{region_slug}", exist_ok=True)

        # Create region index
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
            p_id, event_id, region, summary, key_points, language = p

            # Get event title
            cursor.execute('SELECT title FROM events WHERE id = ?', (event_id,))
            event_result = cursor.fetchone()
            event_title = event_result[0] if event_result else f"Event {event_id}"
            event_slug = slugify(event_title)

            content += f"""### [{event_title}](/events/{event_slug})

{summary or 'Regional analysis of strategic implications'}

**Key Points**: {key_points or 'Strategic priorities and regional concerns'}

---

"""

        content += f"""

[← Back to All Perspectives](/perspectives/)
"""

        # Write region index
        filename = f"docs/perspectives/{region_slug}/index.md"
        with open(filename, 'w') as f:
            f.write(content)
        print(f"  ✓ {filename}")

    return perspectives

def export_analyses(conn):
    """Export all analyses to docs/analyses/"""
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, content, confidence_level, research_approach, created_at
        FROM analyses
        ORDER BY created_at DESC
    ''')
    analyses = cursor.fetchall()

    print(f"\nExporting {len(analyses)} analyses...")

    os.makedirs("docs/analyses", exist_ok=True)

    for analysis in analyses:
        a_id, title, content, confidence, methodology, created = analysis
        slug = slugify(title)

        md_content = f"""---
layout: default
title: "{title}"
date: {str(created).split()[0] if created else '2025-10-27'}
confidence: {confidence or 4}
---

# {title}

**Date**: {str(created).split()[0] if created else '2025-10-27'}
**Confidence**: {'⭐' * (confidence or 4)} ({confidence or 4}/5)
**Research Approach**: {methodology or 'Multi-perspective synthesis'}

---

## Full Analysis

{content or 'Detailed synthesis of regional perspectives and historical patterns'}

---

**Analysis ID**: {a_id}

[← Back to Home](/) | [View Events](/events/) | [Perspectives](/perspectives/)
"""

        filename = f"docs/analyses/{slug}.md"
        with open(filename, 'w') as f:
            f.write(md_content)
        print(f"  ✓ {filename}")

    return analyses

def export_historical_patterns(conn):
    """Export historical patterns to docs/historical-patterns/"""
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, name, time_period, description, relevance_score, key_characteristics
        FROM historical_patterns
        ORDER BY relevance_score DESC
    ''')
    patterns = cursor.fetchall()

    print(f"\nExporting {len(patterns)} historical patterns...")

    for pattern in patterns:
        p_id, name, period, description, relevance, characteristics = pattern
        slug = slugify(name)

        content = f"""---
layout: default
title: "{name}"
time_period: "{period or 'Historical'}"
relevance: {relevance or 0.9}
---

# {name}

**Time Period**: {period or 'Historical analysis'}
**Relevance Score**: {relevance or 0.9} {'⭐' * int((relevance or 0.9) * 5)}

---

## Historical Context

{description or 'Analysis of historical power transition pattern'}

---

## Key Characteristics

{characteristics or 'Core patterns and strategic dynamics'}

---

## Applications to Current Events

See how this pattern applies to:
- [Browse Events](/events/)
- [View Perspectives](/perspectives/)

---

**Pattern ID**: {p_id}

[← Back to Historical Patterns](/historical-patterns/)
"""

        filename = f"docs/historical-patterns/{slug}.md"
        with open(filename, 'w') as f:
            f.write(content)
        print(f"  ✓ {filename}")

    return patterns

def main():
    """Main export function"""
    print("=" * 60)
    print("EXPORTING RESEARCH DATABASE TO GITHUB PAGES")
    print("=" * 60)

    # Connect to database
    conn = sqlite3.connect('research.db')

    # Export all content
    events = export_events(conn)
    perspectives = export_perspectives(conn)
    analyses = export_analyses(conn)
    patterns = export_historical_patterns(conn)

    # Summary
    print("\n" + "=" * 60)
    print("EXPORT COMPLETE")
    print("=" * 60)
    print(f"✓ {len(events)} events exported to docs/events/")
    print(f"✓ {len(perspectives)} perspectives exported to docs/perspectives/")
    print(f"✓ {len(analyses)} analyses exported to docs/analyses/")
    print(f"✓ {len(patterns)} historical patterns exported to docs/historical-patterns/")
    print("\nNext: Update navigation indices and commit to git")

    conn.close()

if __name__ == "__main__":
    main()
