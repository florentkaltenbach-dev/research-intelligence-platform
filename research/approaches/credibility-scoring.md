# Credibility Scoring Research Approach

## Overview
This approach provides a systematic framework for rating sources and assigning confidence levels to claims. It helps maintain transparency about information quality and enables readers to assess the reliability of research findings.

## Purpose
- Rate source credibility on a consistent scale (Tier 1-4)
- Assign confidence levels to specific claims (1-5 stars)
- Track source reliability over time
- Maintain transparency about information quality
- Help readers evaluate research trustworthiness

## Two-Dimensional Rating System

### Dimension 1: Source Credibility Tiers
Rates the **source type** itself (static rating)

### Dimension 2: Claim Confidence Levels
Rates the **specific claim's** evidence strength (claim-specific)

## Source Credibility Tiers

### Tier 1: Primary/Official Data
**Characteristics**:
- Government statistical agencies (Bureau of Labor Statistics, Eurostat, etc.)
- Central banks (Federal Reserve, ECB, PBOC official data)
- International organizations (IMF, World Bank, UN datasets)
- Academic peer-reviewed research
- Official government documents/releases

**Examples**:
- Federal Reserve Economic Data (FRED)
- Chinese National Bureau of Statistics
- IMF World Economic Outlook database
- Peer-reviewed journal articles
- Official treaty texts, policy documents

**Use For**:
- Economic indicators
- Trade statistics
- Financial data
- Official policy positions

**Limitations**:
- May reflect political priorities in data collection
- Delayed publication (not for breaking news)
- Methodology may favor certain narratives

**Badge Display**: `🟢 Tier 1: Official Data`

---

### Tier 2: Investigative/Specialized Journalism
**Characteristics**:
- Major investigative journalism (NYT, Reuters, Bloomberg, FT)
- Specialized regional media (Al Jazeera, SCMP, Kommersant, The Hindu)
- Think tanks with transparent methodology (Brookings, Chatham House, Carnegie)
- Independent researchers with track records
- Expert analysis from credentialed specialists

**Examples**:
- Reuters investigative reports
- Financial Times analysis
- Al Jazeera English documentaries
- RAND Corporation research
- South China Morning Post business coverage

**Use For**:
- Breaking news with context
- In-depth analysis
- Regional perspectives
- Expert commentary

**Limitations**:
- Editorial bias varies by outlet
- Analysis quality varies by journalist
- Regional focus may miss broader context

**Badge Display**: `🟡 Tier 2: Expert Analysis`

---

### Tier 3: Standard News Reporting
**Characteristics**:
- Mainstream media news reporting (not opinion)
- Wire services (AP, AFP)
- Regional newspapers
- Industry publications
- Academic commentary (non-peer-reviewed)

**Examples**:
- Associated Press news articles
- BBC World News reporting
- Regional newspaper coverage
- Industry trade publications

**Use For**:
- Event reporting
- Official statements
- General news coverage

**Limitations**:
- May lack verification
- Often relies on single sources
- Limited investigative depth

**Badge Display**: `🟠 Tier 3: News Reporting`

---

### Tier 4: Opinion/Social Sources
**Characteristics**:
- Opinion pieces and editorials
- Social media posts (even from experts)
- Blogs and personal commentary
- Unverified eyewitness accounts
- Activist organization claims

**Examples**:
- Twitter/X posts from experts
- Medium articles
- Opinion columns
- Activist press releases
- Reddit discussions

**Use For**:
- Gauging public sentiment
- Expert speculation
- Emerging narratives
- Grassroots perspectives

**Limitations**:
- Often unverified
- High bias potential
- No editorial review

**Badge Display**: `🔴 Tier 4: Opinion/Social`

---

## Confidence Levels (1-5 Stars)

Rate individual **claims**, not entire sources. A Tier 1 source can contain ⭐⭐ claims if data is preliminary.

### ⭐ Very Low Confidence
**Characteristics**:
- Single unverified source
- Speculation or prediction
- Contradicted by other evidence
- No supporting data

**Example Claims**:
- "Markets will crash next month" (prediction)
- "Anonymous sources say..." (single unverified)
- Rumor or unconfirmed report

**Use When**:
- Including early breaking news
- Noting speculation for context
- Presenting contested claims

---

### ⭐⭐ Low Confidence
**Characteristics**:
- Limited supporting evidence
- Single credible source
- Preliminary data
- Plausible but unconfirmed

**Example Claims**:
- "Early estimates suggest..." (preliminary data)
- "One analysis indicates..." (single source)
- "Unconfirmed reports from..." (limited verification)

**Use When**:
- Citing preliminary findings
- Noting emerging patterns
- Including claims needing verification

---

### ⭐⭐⭐ Moderate Confidence
**Characteristics**:
- Multiple credible sources
- Some contradicting evidence exists
- Standard methodology
- Generally accepted but debated

**Example Claims**:
- "Several reports indicate..." (multiple sources)
- "Data shows X, though some dispute methodology"
- "Most analysts agree, but Y remains uncertain"

**Use When**:
- Presenting mainstream views
- Citing standard analysis
- Noting majority consensus

---

### ⭐⭐⭐⭐ High Confidence
**Characteristics**:
- Strong evidence from diverse sources
- Multiple Tier 1-2 sources agree
- Robust methodology
- Limited contradicting evidence

**Example Claims**:
- "Official data confirms X, corroborated by independent analysis"
- "Multiple investigations verify..."
- "Peer-reviewed studies demonstrate..."

**Use When**:
- Citing well-established facts
- Presenting verified findings
- Relying on strong evidence

---

### ⭐⭐⭐⭐⭐ Very High Confidence
**Characteristics**:
- Overwhelming evidence
- Consensus across stakeholders
- Multiple Tier 1 sources
- No credible contradicting evidence
- Replicable findings

**Example Claims**:
- "Official statistics confirm, verified by international observers"
- "Broad academic consensus based on decades of research"
- "Documented historical fact with extensive evidence"

**Use When**:
- Stating core facts
- Presenting established knowledge
- Citing uncontested data

---

## Application Guidelines

### How to Score a Claim

1. **Identify the Source Tier** (1-4)
2. **Assess the Claim's Evidence**:
   - How many sources support it?
   - Do sources agree or contradict?
   - Is evidence direct or circumstantial?
   - Is methodology sound?
3. **Assign Confidence Level** (1-5 stars)
4. **Document in Database**

### Example Scoring Process

**Claim**: "China purchased 200 tons of gold in Q3 2024"

**Step 1 - Source Tier**:
- Source: People's Bank of China official report
- Tier: **Tier 1** (official government data)

**Step 2 - Evidence Assessment**:
- Official PBOC quarterly report (primary source)
- Corroborated by IMF data
- Matches independent analyst estimates
- Methodology transparent

**Step 3 - Confidence Level**:
- Multiple Tier 1 sources agree
- Robust official data
- No contradicting evidence
- **Rating: ⭐⭐⭐⭐⭐ (Very High Confidence)**

**Step 4 - Database Entry**:
```json
{
  "claim": "China purchased 200 tons of gold in Q3 2024",
  "source_tier": 1,
  "confidence": 5,
  "sources": [
    {
      "url": "pboc.gov.cn/...",
      "title": "PBOC Q3 2024 Reserve Report",
      "tier": 1
    },
    {
      "url": "imf.org/...",
      "title": "IMF COFER Database",
      "tier": 1
    }
  ]
}
```

---

## Database Structure

### Source Model
```python
class Source(Base):
    id: int
    url: str  # Unique URL
    title: str
    credibility_tier: int  # 1-4
    region: str  # Geographic origin
    language: str  # Source language
    source_type: str  # "government", "media", "academic", etc.
    verified_date: datetime  # When tier was assigned
    notes: str  # Why this tier was assigned
```

### Perspective/Analysis with Confidence
```python
class Perspective(Base):
    # ... other fields
    confidence_level: int  # 1-5 stars
    sources: relationship  # Many-to-many with Source

class Analysis(Base):
    # ... other fields
    confidence_level: int  # Overall analysis confidence
    source_breakdown: dict  # {"tier1": 3, "tier2": 5, "tier3": 2, "tier4": 1}
```

---

## Tracking Source Reliability Over Time

### Historical Accuracy Tracking
Monitor how sources perform over time:

**Methodology**:
1. Record predictions/claims with timestamps
2. Later verify outcomes
3. Track accuracy rate

**Example**:
- Source: "Economist X predicted Y"
- Prediction date: 2024-01-15
- Outcome date: 2024-06-01
- Result: Correct/Incorrect/Partially Correct
- Track: Economist X's accuracy rate over time

### Adjusting Tiers
Sources can move between tiers based on track record:
- Tier 2 → Tier 1: Consistently verified, transparent methodology
- Tier 3 → Tier 2: Strong investigative track record
- Any Tier → Lower: Pattern of inaccuracy, lack of transparency

**Document Tier Changes**:
```json
{
  "source_id": 123,
  "tier_history": [
    {"date": "2024-01-01", "tier": 3, "reason": "Initial assessment"},
    {"date": "2024-06-01", "tier": 2, "reason": "Consistent accuracy, strong methodology"}
  ]
}
```

---

## Frontend Display Guidelines

### Source Badges
Display tier clearly on all citations:
- 🟢 **Tier 1**: Official Data
- 🟡 **Tier 2**: Expert Analysis
- 🟠 **Tier 3**: News Reporting
- 🔴 **Tier 4**: Opinion/Social

### Confidence Stars
Show confidence level for each claim:
- ⭐⭐⭐⭐⭐ Very High Confidence
- ⭐⭐⭐⭐ High Confidence
- ⭐⭐⭐ Moderate Confidence
- ⭐⭐ Low Confidence
- ⭐ Very Low Confidence

### Aggregate Metrics
On event/analysis pages, show:
- **Source Diversity**: "Based on 3 Tier 1, 5 Tier 2, 2 Tier 3 sources"
- **Overall Confidence**: Average confidence across claims
- **Regional Breakdown**: Sources by region

---

## Best Practices

### Do's
✅ Rate sources based on category, not individual articles
✅ Rate claims separately from source tier
✅ Document why you assigned specific tiers/confidence
✅ Update confidence as new evidence emerges
✅ Include Tier 4 sources when they provide unique perspectives
✅ Be transparent about limitations of all tiers

### Don'ts
❌ Don't dismiss Tier 4 sources automatically
❌ Don't assume Tier 1 = 5 stars (rate claims independently)
❌ Don't let personal bias affect tier assignment
❌ Don't fail to update ratings as evidence changes
❌ Don't hide low-confidence claims - present with appropriate caveats
❌ Don't use tiers to exclude opposing viewpoints

---

## Integration with Other Approaches

**Works Well With**:
- **Counter-Narrative**: Rate credibility of opposing views fairly
- **Source Diversification**: Ensure mix across tiers and regions
- **Historical Matcher**: Higher confidence for well-documented patterns
- **Data Collection**: Tier 1 sources for hard numbers

**Enhances**:
- All research approaches benefit from explicit credibility tracking

---

## Examples

### Example 1: Economic Data
**Claim**: "US unemployment rate was 3.8% in September 2024"
- **Source**: Bureau of Labor Statistics
- **Tier**: 1 (official government data)
- **Confidence**: ⭐⭐⭐⭐⭐ (official statistic, verified)

### Example 2: Policy Analysis
**Claim**: "New tariffs will reduce inflation"
- **Source**: Think tank analysis
- **Tier**: 2 (expert analysis)
- **Confidence**: ⭐⭐⭐ (plausible but debated, models vary)

### Example 3: Breaking News
**Claim**: "Protests erupted in city X"
- **Source**: Wire service report + social media videos
- **Tier**: 3 (news reporting) + 4 (social media)
- **Confidence**: ⭐⭐⭐⭐ (multiple sources, video evidence)

### Example 4: Speculation
**Claim**: "Central bank will raise rates next month"
- **Source**: Financial analyst opinion
- **Tier**: 4 (opinion)
- **Confidence**: ⭐⭐ (educated guess, no official indication)

---

## Output Checklist

Before considering credibility scoring complete:
- [ ] All sources assigned tier (1-4)
- [ ] All major claims assigned confidence (1-5 stars)
- [ ] Tier assignment reasoning documented
- [ ] Confidence based on evidence, not source tier alone
- [ ] Source diversity tracked (not all Tier 1 or all Tier 4)
- [ ] Regional diversity in sources
- [ ] Low-confidence claims included with caveats
- [ ] Source metadata complete (URL, region, language, type)

---

## Notes

**Remember**:
- A Tier 1 source can make low-confidence claims (preliminary data)
- A Tier 4 source can be right (social media often breaks news first)
- Confidence reflects evidence strength, not source prestige
- Transparency is more valuable than false certainty

This system helps readers evaluate research quality themselves rather than taking claims at face value.
