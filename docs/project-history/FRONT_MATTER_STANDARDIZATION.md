# Event Front Matter Standardization Guide

**Created**: October 28, 2025
**Status**: Documentation for future standardization

---

## Current State

Event files have **two different front matter formats**:

### Format A: Standard (Preferred) ✅
Used by 7 files including: `saudi-pif-repositioning.md`, `brics-payment-systems.md`, `china-cips-expansion.md`

```yaml
---
layout: default
title: "Event Title"
date: YYYY-MM-DD
event_type: "Category"
confidence: 1-5
regions: ["Region1", "Region2"]
---
```

**Fields**:
- `event_type`: Categorical (e.g., "Sovereign Wealth Reallocation", "Payment Infrastructure")
- `confidence`: Numeric 1-5 rating
- `regions`: Array of affected regions

### Format B: Non-Standard (Needs Updating) ⚠️
Used by 22 files including: `dollar-weaponization...`, `indias-strategic-autonomy...`

```yaml
---
layout: default
title: "Event Title"
date: YYYY-MM-DD
region: "Single Region/Global"
impact: "critical|high|medium"
---
```

**Fields**:
- `region`: String (singular)
- `impact`: Text-based severity

---

## Recommended Standard

All event files should use **Format A**:

```yaml
---
layout: default
title: "Event Title (No Inconsistent Punctuation)"
date: YYYY-MM-DD
event_type: "Category"
confidence: 1-5
regions: ["Region1", "Region2", "Region3"]
---
```

### Field Definitions

**`event_type`** (required):
- Sovereign Wealth Reallocation
- Payment Infrastructure
- Reserve Diversification
- Monetary Policy Experiment
- Financial Sector Growth
- Wealth Migration
- Geopolitical Realignment
- Technology/Infrastructure
- Trade Policy

**`confidence`** (required): 1-5 stars
- 5: Very high - multiple Tier 1 sources
- 4: High - Tier 1-2 sources with corroboration
- 3: Medium - Tier 2 sources or single Tier 1
- 2: Low - Tier 3 sources or uncorroborated
- 1: Speculation - Tier 4 or no verification

**`regions`** (required): Array of strings
- Use specific regions: ["China", "Russia", "Middle East", "India", "United States", "Europe", "Africa", "Latin America", "Global"]
- Multiple regions OK: ["Middle East", "China", "United States"]
- "Global" when truly worldwide impact

---

## Files Needing Standardization (22 files)

### Files with `impact` field instead of `confidence`:

1. `dollar-weaponization-accelerates-global-de-dollarization-trends.md`
   - Current: `region: "Global"`, `impact: "critical"`
   - Should be: `confidence: 4`, `regions: ["Global", "Russia", "China", "Middle East"]`

2. `indias-strategic-autonomy-multi-alignment-between-quad-russia-and-china.md`
   - Current: `region: "India/Global"`, `impact: "high"`
   - Should be: `event_type: "Geopolitical Realignment"`, `confidence: 4`, `regions: ["India", "United States", "China", "Russia"]`

3. `us-sovereign-wealth-fund-state-capitalism-emerges-in-market-economy.md`
   - Current: `region: "United States"`, `impact: "high"`
   - Should be: `event_type: "Sovereign Wealth Creation"`, `confidence: 3`, `regions: ["United States"]`

4. `china-brokered-saudi-iran-rapprochement-middle-east-realignment.md`
   - Current: `region: "Middle East"`, `impact: "critical"`
   - Should be: `event_type: "Geopolitical Realignment"`, `confidence: 5`, `regions: ["Middle East", "China", "Saudi Arabia", "Iran"]`

5. `supply-chain-regionalization-23-trillion-semiconductor-fragmentation.md`
   - Current: `region: "Global"`, `impact: "critical"`
   - Should be: `event_type: "Technology/Infrastructure"`, `confidence: 5`, `regions: ["Global", "United States", "China", "Taiwan"]`

6. `el-salvador-bitcoin-experiment-reversal-imf-mandated-rollback.md`
   - Current: `region: "Latin America/Global"`, `impact: "medium"`
   - Should be: Already has `event_type: "Monetary Policy Experiment"` - just needs `confidence: 5`, `regions: ["Latin America", "El Salvador"]`

7. `ai-infrastructure-arms-race-325-billion-big-tech-investment-in-2025.md`
   - Current: `region: "Global"`, `impact: "critical"`
   - Should be: `event_type: "Technology/Infrastructure"`, `confidence: 4`, `regions: ["Global", "United States", "China"]`

8. `european-strategic-autonomy-trumps-return-forces-defense-reckoning.md`
   - Current: `region: "Europe/Transatlantic"`, `impact: "critical"`
   - Should be: `event_type: "Geopolitical Realignment"`, `confidence: 4`, `regions: ["Europe", "United States"]`

9. `indo-pacific-military-realignments-aukus-quad-and-rising-china.md`
   - Current: `region: "Indo-Pacific"`, `impact: "critical"`
   - Should be: `event_type: "Geopolitical Realignment"`, `confidence: 5`, `regions: ["Indo-Pacific", "United States", "China", "Australia", "India"]`

10. `us-china-semiconductor-war-export-control-reversals-and-escalation.md`
    - Current: `region: "US-China"`, `impact: "critical"`
    - Should be: `event_type: "Technology/Trade Policy"`, `confidence: 5`, `regions: ["United States", "China", "Global"]`

11. `china-weaponizes-rare-earth-supply-chain-with-export-controls.md`
    - Current: `region: "Global/China"`, `impact: "high"`
    - Should be: `event_type: "Trade Policy"`, `confidence: 5`, `regions: ["China", "Global", "United States"]`

12. `china-cips-expansion-to-185-countries-176-direct-participants.md`
    - Current: `region: "Global/China"`, `impact: "high"`
    - Should be: Already has proper structure, verify only

13. `capital-flight-to-uaesingapore-142000-millionaires-relocating-in-2025.md`
    - Current: `region: "Global"`, `impact: "high"`
    - Should be: Already has `event_type: "Wealth Migration"` in some versions

14. `brics-17th-summit-expansion-and-payment-system-development.md`
    - Current: `region: "Global/BRICS"`, `impact: "high"`
    - Should be: `event_type: "Payment Infrastructure"`, `confidence: 4`, `regions: ["Global", "BRICS", "China", "Russia", "India"]`

15. `islamic-finance-growth-to-6-trillion-projected-97t-by-2029.md`
    - Current: `region: "Global/Middle East"`, `impact: "high"`
    - Should be: Already has `event_type: "Financial Sector Growth"`

16. `africa-in-multipolar-order-30-critical-minerals-us-china-competition.md`
    - Current: `region: "Africa"`, `impact: "critical"`
    - Should be: `event_type: "Geopolitical Realignment"`, `confidence: 4`, `regions: ["Africa", "China", "United States"]`

17. `energy-transition-geopolitics-critical-minerals-competition-intensifies.md`
    - Current: `region: "Global"`, `impact: "critical"`
    - Should be: `event_type: "Resource Competition"`, `confidence: 5`, `regions: ["Global", "China", "United States"]`

18. `nato-5-gdp-defense-spending-29-trillion-by-2035-rearmament.md`
    - Current: `region: "Global/NATO"`, `impact: "critical"`
    - Should be: `event_type: "Military Policy"`, `confidence: 4`, `regions: ["Europe", "United States", "NATO"]`

19. `brics-payment-systems-de-dollarization-90-intra-brics-local-currency-trade.md`
    - Current: Unknown - needs checking

20. `geographical-determinism-the-same-strategic-locations-for-millennia.md`
    - Current: Unknown - needs checking

21. `saudi-pif-913b-repositioning-33-us-equity-reduction.md`
    - Note: Duplicate of `saudi-pif-repositioning.md`? Check if should be deleted.

22. Various others - complete audit needed

---

## Conversion Script (Future)

```bash
# Template for bulk conversion
for file in docs/events/*.md; do
  # Check if has 'impact:' instead of 'confidence:'
  if grep -q "^impact:" "$file"; then
    echo "Needs conversion: $file"
    # Manual review and conversion required
  fi
done
```

---

## Standardization Process

1. **Phase 1**: Identify all files with non-standard front matter (DONE - see list above)
2. **Phase 2**: For each file:
   - Read content to determine appropriate `event_type`
   - Convert `impact` to numeric `confidence` (critical=5/4, high=4/3, medium=3/2)
   - Convert `region` string to `regions` array
   - Add any missing regions based on content
3. **Phase 3**: Update docs/README.md with front matter standards
4. **Phase 4**: Create template for new events

---

## Impact Mapping Guide

When converting `impact` to `confidence`:

- `impact: "critical"` + Tier 1 sources → `confidence: 5`
- `impact: "critical"` + Tier 2 sources → `confidence: 4`
- `impact: "high"` + Tier 1-2 sources → `confidence: 4`
- `impact: "high"` + Tier 3 sources → `confidence: 3`
- `impact: "medium"` → `confidence: 3` or `2` (assess sources)

Note: `impact` measures event significance, `confidence` measures source quality. They're different dimensions - conversion requires reading the "Source Credibility" section of each event.

---

## Benefits of Standardization

1. **Consistency**: All events use same metadata structure
2. **Filtering**: Can filter/sort by confidence level programmatically
3. **Clarity**: `confidence: 4` clearer than `impact: "high"`
4. **Multi-region**: Array supports multiple regions properly
5. **Jekyll**: Potential future use of Jekyll collections/filters

---

**Next Step**: Systematically update all 22 files using this guide.
**Estimated Time**: 2-3 hours (careful review required for each file)
**Priority**: Medium (functional impact low, quality impact high)
