# Data Collection Research Approach

## Goal
Track financial and economic metrics over time with proper citations, focusing on multi-currency data collection.

## Steps

### 1. Define the Metric
- Clear name (e.g., "Chinese Gold Reserves")
- Unit (e.g., "tonnes", "USD billions", "percentage")
- Category (e.g., "reserves", "trade", "currency")

### 2. Gather Historical Data
Search for data points with:
- Specific dates
- Exact values
- Primary sources (government data, central banks, IMF, World Bank)

### 3. Track in Multiple Currencies
When relevant, collect data in:
- Chinese Yuan (CNY)
- Russian Ruble (RUB)
- Indian Rupee (INR)
- UAE Dirham (AED)
- Not just USD/EUR

### 4. Document Sources
- Link each data point to its source
- Rate source credibility (Tier 1 for government data)
- Note any discrepancies between sources

### 5. Add to Database
- Create Metric if it doesn't exist
- Add MetricDataPoint for each value
- Link to Source records

## Example Prompt for Claude Code

```
Track "Russian foreign exchange reserves" using the Data Collection approach.

Search for monthly data from 2020 to present from:
1. Central Bank of Russia official data
2. IMF statistics
3. Bloomberg/Reuters data

For each data point:
- Date
- Value in USD
- Value in Rubles (if available)
- Source URL

Create the Metric in the database and add all data points with proper source attribution.
```

## Tips
- Government sources are Tier 1
- Cross-reference multiple sources when possible
- Note data revisions or corrections
- Track data in the native currency when possible
- Document calculation methodology if provided
