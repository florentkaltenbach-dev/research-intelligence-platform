# Counter-Narrative Research Approach

## Overview
This approach identifies and analyzes opposing viewpoints on the same event or issue. The goal is to present a balanced, multi-perspective analysis without false equivalence, understanding how different stakeholders frame and interpret the same situation.

## Purpose
- Find genuinely opposing interpretations of events
- Analyze different stakeholder perspectives and motivations
- Understand regional/cultural framing differences
- Present balanced views that acknowledge disagreements
- Avoid false equivalence while maintaining objectivity

## When to Use
- Analyzing controversial or politically sensitive events
- Understanding geopolitical tensions
- Comparing Western vs non-Western narratives
- Researching events with clear opposing factions
- Events where official narratives contradict grassroots perspectives

## Research Process

### 1. Identify the Main Narrative
First, establish the dominant or most visible narrative:
- What is the mainstream Western media portrayal?
- What are official government statements?
- What narrative appears most frequently in search results?

**Example**: "Western sanctions are crippling Russia's economy"

### 2. Find Opposition Sources
Search for sources that explicitly contradict or challenge the main narrative:

**Geographic Opposition**
- If main narrative is Western → search Chinese, Russian, Arabic, Hindi sources
- If main narrative is government → search independent media, academic analysis
- If main narrative is corporate → search labor/activist perspectives

**Search Strategies**
- Use negation keywords: "sanctions NOT working", "economy resilient"
- Search in other languages and regions
- Look for analysis from opposing political factions
- Check specialized/regional news sources

### 3. Categorize Perspectives
Organize findings into stakeholder categories:

**Common Stakeholder Categories**
- Government (different countries/regions)
- Corporate/Business
- Academic/Expert
- Civil society/NGO
- Media (by region/political leaning)
- Grassroots/Social movements

### 4. Analyze Key Differences
For each opposing perspective, identify:

**Framing Differences**
- What aspects do they emphasize vs downplay?
- What language/terminology do they use?
- What evidence do they cite?

**Factual Disagreements**
- Where do they agree on facts but disagree on interpretation?
- Where do they dispute the underlying facts themselves?
- What data/metrics do they highlight differently?

**Motivation/Interest**
- What are the stakeholder's interests?
- How might their position serve their goals?
- Are there economic/political incentives for their narrative?

### 5. Identify Consensus Points
Even among opposing views, find areas of agreement:
- Facts that all sides acknowledge
- Shared concerns despite different solutions
- Common baseline data (even if interpreted differently)

### 6. Assess Credibility Without Bias
Rate each narrative's support:

**Evidence Quality**
- Tier 1: Official data, peer-reviewed research
- Tier 2: Investigative journalism, expert analysis
- Tier 3: Standard news reporting
- Tier 4: Opinion pieces, social media

**Confidence Level** (1-5 stars)
- ⭐: Speculation/unverified claims
- ⭐⭐: Some supporting evidence
- ⭐⭐⭐: Multiple credible sources
- ⭐⭐⭐⭐: Strong evidence from diverse sources
- ⭐⭐⭐⭐⭐: Overwhelming consensus across stakeholders

### 7. Present Balanced Analysis
Create a synthesis that:
- Presents all major perspectives fairly
- Notes strength of evidence for each view
- Identifies genuine factual disputes vs interpretation differences
- Avoids false equivalence (don't equate speculation with verified facts)
- Acknowledges uncertainty where it exists

## Database Structure

### Event
Create the main event record:
```json
{
  "title": "Impact of Western Sanctions on Russian Economy (2024)",
  "date": "2024-01-15",
  "region": "Europe/Russia",
  "impact_level": "high"
}
```

### Perspectives
Add multiple perspectives with clear regional/stakeholder attribution:

**Perspective 1: Western Government**
```json
{
  "region": "North America/Europe",
  "stakeholder": "Government",
  "summary": "Sanctions significantly degrading Russian economic capacity",
  "key_points": [
    "GDP contraction of 2.1% in 2023",
    "Import restrictions limiting tech access",
    "Capital flight exceeding $200 billion"
  ],
  "sources": [/* Tier 1-2 sources */],
  "confidence": 4
}
```

**Perspective 2: Russian Government**
```json
{
  "region": "Russia",
  "stakeholder": "Government",
  "summary": "Economy adapting successfully, sanctions creating new opportunities",
  "key_points": [
    "Growth in domestic manufacturing",
    "New trade partnerships with BRICS nations",
    "Ruble stabilization through commodity exports"
  ],
  "sources": [/* Tier 1-2 sources */],
  "confidence": 3
}
```

**Perspective 3: Independent Economists**
```json
{
  "region": "Global",
  "stakeholder": "Academic",
  "summary": "Mixed impact - short-term pain but long-term adaptation likely",
  "key_points": [
    "Initial shock absorbed through central bank interventions",
    "Structural vulnerabilities remain but sanctions less effective than projected",
    "Import substitution occurring but with quality/efficiency trade-offs"
  ],
  "sources": [/* Tier 1-2 sources */],
  "confidence": 4
}
```

### Analysis Record
Create synthesis analysis:
```json
{
  "title": "Counter-Narrative Analysis: Russian Sanctions Impact",
  "content": "## Synthesis\n\nWestern governments emphasize...\n\nRussian official sources counter...\n\nIndependent analysts suggest...\n\n## Consensus Points\n- All sides agree sanctions were unprecedented\n- GDP impact occurred but magnitude disputed\n\n## Key Disagreements\n- Sustainability of current trajectory\n- Effectiveness of import substitution\n- Long-term economic outlook",
  "confidence_level": 4,
  "related_events": [/* IDs */]
}
```

## Examples

### Example 1: Climate Policy
**Main Narrative**: "Rapid transition to renewables necessary to prevent climate catastrophe"
**Counter-Narratives**:
- Developing nations: "Unfair burden on countries still industrializing"
- Fossil fuel sector: "Transition too rapid, energy security at risk"
- Green activists: "Transition not happening fast enough"

### Example 2: Trade Policy
**Main Narrative**: "Free trade benefits all economies"
**Counter-Narratives**:
- Labor unions: "Outsourcing destroys domestic jobs"
- Developing countries: "Unequal trade terms perpetuate dependency"
- Protectionists: "National industries need protection"

### Example 3: Monetary Policy
**Main Narrative**: "Central bank independence crucial for stability"
**Counter-Narratives**:
- MMT economists: "Excessive focus on inflation vs employment"
- Populist movements: "Unelected technocrats serving financial elites"
- Austrian economists: "Intervention causes boom-bust cycles"

## Best Practices

### Do's
✅ Search across multiple languages and regions
✅ Consider stakeholder interests and motivations
✅ Present evidence strength for each perspective
✅ Acknowledge areas of genuine uncertainty
✅ Note when disagreements are factual vs interpretive
✅ Include grassroots/civil society views alongside official narratives

### Don'ts
❌ Don't equate speculation with verified facts (no false equivalence)
❌ Don't dismiss perspectives simply because they're minority views
❌ Don't only include government/official sources
❌ Don't ignore evidence that contradicts your initial hypothesis
❌ Don't present narratives without attribution/sourcing
❌ Don't fail to acknowledge your own potential biases

## Integration with Other Approaches

**Works Well With**:
- **Source Diversification**: Find non-Western sources for counter-narratives
- **Credibility Scoring**: Rate evidence quality for each narrative
- **Historical Matcher**: Compare to past instances of narrative divergence
- **Synthesis**: Combine multiple counter-narratives into cohesive analysis

**Complements**:
- Data collection (hard numbers can cut through narrative spin)
- Consensus identification (find rare agreement points)

## Output Checklist

Before considering counter-narrative research complete:
- [ ] At least 3 distinct perspectives identified
- [ ] Each perspective attributed to clear stakeholder category
- [ ] Sources cited for each narrative (with credibility tiers)
- [ ] Key differences explicitly analyzed (framing, facts, interests)
- [ ] Consensus points identified (if any exist)
- [ ] Confidence levels assigned based on evidence
- [ ] Synthesis analysis created avoiding false equivalence
- [ ] Related events linked (if historical patterns exist)

## Notes

This approach is particularly valuable for:
- Geopolitically sensitive events
- Economic policy debates
- Historical events with competing interpretations
- Situations where official narratives face credible challenges

Remember: The goal is understanding different perspectives, not picking "winners" or declaring one narrative "correct." Present the evidence and let readers evaluate.
