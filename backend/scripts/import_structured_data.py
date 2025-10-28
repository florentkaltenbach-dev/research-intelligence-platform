#!/usr/bin/env python3
"""
Import structured data from Global Capital Flows 2025 research:
- Metrics with time-series data points
- Historical patterns with relevance scores
- Sources with credibility tiers
"""
import requests
from datetime import datetime

API_BASE = "http://localhost:8000/api"

def create_metric(name, description, unit, category):
    """Create a metric and return its ID."""
    response = requests.post(
        f"{API_BASE}/metrics/",
        json={
            "name": name,
            "description": description,
            "unit": unit,
            "category": category
        }
    )
    if response.status_code in [200, 201]:
        result = response.json()
        print(f"  ✅ Created metric: {name} (ID: {result['id']})")
        return result['id']
    else:
        print(f"  ❌ Failed to create metric: {name}")
        print(f"     {response.text}")
        return None

def add_datapoint(metric_id, value, date_str, notes=None):
    """Add a data point to a metric."""
    response = requests.post(
        f"{API_BASE}/metrics/datapoint",
        json={
            "metric_id": metric_id,
            "value": value,
            "date": date_str,
            "notes": notes
        }
    )
    if response.status_code not in [200, 201]:
        print(f"    ❌ Failed to add datapoint: {response.text}")

def create_historical_pattern(name, description, time_period, key_characteristics, relevance_score):
    """Create a historical pattern."""
    response = requests.post(
        f"{API_BASE}/historical-patterns/",
        json={
            "name": name,
            "description": description,
            "time_period": time_period,
            "key_characteristics": key_characteristics,
            "relevance_score": relevance_score
        }
    )
    if response.status_code in [200, 201]:
        result = response.json()
        print(f"  ✅ Created pattern: {name} (relevance: {relevance_score})")
        return result['id']
    else:
        print(f"  ❌ Failed to create pattern: {name}")
        print(f"     {response.text}")
        return None

def create_source(url, title, tier, region, language, publisher):
    """Create a source."""
    response = requests.post(
        f"{API_BASE}/sources/",
        json={
            "url": url,
            "title": title,
            "credibility_tier": tier,
            "region": region,
            "language": language,
            "publisher": publisher
        }
    )
    if response.status_code in [200, 201]:
        result = response.json()
        print(f"  ✅ Created source: {title}")
        return result['id']
    else:
        # Source might already exist (unique URL constraint)
        if "duplicate" in response.text.lower() or "unique" in response.text.lower():
            print(f"  ⚠️  Source already exists: {title}")
        else:
            print(f"  ❌ Failed to create source: {title}")
            print(f"     {response.text}")
        return None

def main():
    print("=" * 70)
    print("IMPORTING STRUCTURED DATA: METRICS, PATTERNS, SOURCES")
    print("=" * 70)
    print()

    # =========================================================================
    # METRICS WITH TIME-SERIES DATA
    # =========================================================================
    print("📊 CREATING METRICS WITH TIME-SERIES DATA")
    print("-" * 70)

    # Metric 1: Central Bank Gold Purchases
    metric_id = create_metric(
        name="Central Bank Gold Purchases",
        description="Annual gold purchases by central banks worldwide (tonnes)",
        unit="tonnes",
        category="reserves"
    )
    if metric_id:
        add_datapoint(metric_id, 473, "2021-12-31T00:00:00", "2010-2021 average")
        add_datapoint(metric_id, 1136, "2022-12-31T00:00:00", "Record purchases")
        add_datapoint(metric_id, 1037, "2023-12-31T00:00:00")
        add_datapoint(metric_id, 1044.6, "2024-12-31T00:00:00")

    # Metric 2: Dollar Share of Global Reserves
    metric_id = create_metric(
        name="Dollar Share of Global Reserves",
        description="US Dollar percentage of global central bank reserves",
        unit="percentage",
        category="currency"
    )
    if metric_id:
        add_datapoint(metric_id, 71, "2000-01-01T00:00:00", "Peak dollar dominance")
        add_datapoint(metric_id, 58, "2024-12-31T00:00:00", "Current share")

    # Metric 3: Yuan Share of Global Payments (SWIFT)
    metric_id = create_metric(
        name="Yuan Share of Global Payments",
        description="Chinese Yuan (RMB) percentage of SWIFT global payments",
        unit="percentage",
        category="currency"
    )
    if metric_id:
        add_datapoint(metric_id, 3, "2025-06-30T00:00:00", "vs 48% for USD")

    # Metric 4: CIPS Transaction Volume
    metric_id = create_metric(
        name="CIPS Transaction Volume",
        description="China Cross-Border Interbank Payment System annual volume",
        unit="trillion yuan",
        category="trade"
    )
    if metric_id:
        add_datapoint(metric_id, 58.33, "2020-12-31T00:00:00", "Baseline year")
        add_datapoint(metric_id, 123.01, "2023-12-31T00:00:00", "+42.6% YoY")
        add_datapoint(metric_id, 175.49, "2024-12-31T00:00:00", "Tripled since 2020")

    # Metric 5: Islamic Finance Assets
    metric_id = create_metric(
        name="Islamic Finance Global Assets",
        description="Total Islamic finance assets globally",
        unit="trillion USD",
        category="trade"
    )
    if metric_id:
        add_datapoint(metric_id, 5.98, "2024-12-31T00:00:00")

    # Metric 6: HNWI Migration
    metric_id = create_metric(
        name="High Net Worth Individual Migration",
        description="Number of millionaires (liquid wealth $1M+) relocating annually",
        unit="individuals",
        category="capital_flows"
    )
    if metric_id:
        add_datapoint(metric_id, 134000, "2024-12-31T00:00:00")
        add_datapoint(metric_id, 142000, "2025-12-31T00:00:00", "Record high")

    # Metric 7: China-Russia Local Currency Trade
    metric_id = create_metric(
        name="China-Russia Local Currency Settlement",
        description="Percentage of China-Russia bilateral trade in yuan/rubles",
        unit="percentage",
        category="trade"
    )
    if metric_id:
        add_datapoint(metric_id, 25, "2021-12-31T00:00:00")
        add_datapoint(metric_id, 95, "2024-12-31T00:00:00", "On $245B volume")

    # Metric 8: Russia Gold Reserves
    metric_id = create_metric(
        name="Russia Gold Reserves",
        description="Russian central bank gold holdings",
        unit="million troy ounces",
        category="reserves"
    )
    if metric_id:
        add_datapoint(metric_id, 35, "2014-01-01T00:00:00", "Pre-Crimea")
        add_datapoint(metric_id, 75, "2022-01-01T00:00:00", "Worth $229B, 35% of reserves")

    # Metric 9: Saudi PIF US Equity Exposure
    metric_id = create_metric(
        name="Saudi PIF US Equity Holdings",
        description="Saudi Arabia Public Investment Fund US equity exposure",
        unit="billion USD",
        category="capital_flows"
    )
    if metric_id:
        add_datapoint(metric_id, 60, "2021-12-31T00:00:00", "Peak exposure")
        add_datapoint(metric_id, 26.71, "2024-12-31T00:00:00", "-24% YoY")
        add_datapoint(metric_id, 23.8, "2025-06-30T00:00:00", "55% decline from peak")

    print()

    # =========================================================================
    # HISTORICAL PATTERNS
    # =========================================================================
    print("🏛️  CREATING HISTORICAL PATTERNS")
    print("-" * 70)

    create_historical_pattern(
        name="Mamluk-Ottoman Transition (1517)",
        description="Technology gap determines outcomes. CIPS/digital payments/CBDC infrastructure = modern 'cannons and firearms'. Mamluks (Western financial system) have historical dominance. Ottomans (BRICS/emerging systems) have technological dynamism in payment infrastructure.",
        time_period="1517",
        key_characteristics=[
            "Military technology advantage (Ottoman cannons)",
            "Institutional rigidity of incumbent (Mamluk cavalry)",
            "Swift decisive transition",
            "Infrastructure superiority over traditional dominance"
        ],
        relevance_score=0.85
    )

    create_historical_pattern(
        name="Ming-Qing Transition (1644)",
        description="Defection over conquest. Countries joining BRICS/CIPS not conquered - choosing alternative systems voluntarily. Ming (dollar system) hollowing from within through deficits and debt crises. Qing (alternative systems) offering continuity plus optionality.",
        time_period="1644",
        key_characteristics=[
            "Internal system collapse",
            "Voluntary defection of elites",
            "Gradual hollowing before sudden collapse",
            "Continuity offered by successor"
        ],
        relevance_score=0.82
    )

    create_historical_pattern(
        name="Mongol Empire Fragmentation (post-1259)",
        description="Succession crisis pattern. No single dollar alternative emerges - multiple regional systems (yuan, rupee, BRICS mechanisms, Islamic finance). Competing claims under common banner ('de-dollarization') without unified strategy. Similar to post-Mongke fragmentation into competing khanates.",
        time_period="1259-1300",
        key_characteristics=[
            "Succession disputes",
            "Fragmentation into regional powers",
            "Competing claims to legitimacy",
            "No unified alternative emerges"
        ],
        relevance_score=0.78
    )

    create_historical_pattern(
        name="British Slave Trade Abolition (1807)",
        description="'Moral advances' masking strategic retreats. Western 'promoting democracy/human rights' in sanctions regime masks declining ability to enforce financial dominance. British positioned abolition as moral victory when economic model was shifting to industrial capitalism.",
        time_period="1807",
        key_characteristics=[
            "Moral narrative masking strategic shift",
            "Economic model transition",
            "Reframing decline as progress",
            "Ideological justification for policy change"
        ],
        relevance_score=0.75
    )

    create_historical_pattern(
        name="Soviet Collapse: Managed Decline (1991)",
        description="Internal system failure presented differently. US fiscal dominance, debt ceiling crises = internal contradictions. Dollar system decline presented by West as 'strength' (reserve currency status). Similar to how Soviet maintained appearance of strength until sudden collapse.",
        time_period="1985-1991",
        key_characteristics=[
            "Internal contradictions masked",
            "Appearance of strength maintained",
            "Sudden collapse after gradual decline",
            "Elite denial until crisis"
        ],
        relevance_score=0.70
    )

    print()

    # =========================================================================
    # SOURCES (TIER 1-2 MAJOR SOURCES)
    # =========================================================================
    print("📚 CREATING MAJOR SOURCES")
    print("-" * 70)

    # Tier 1: Government/Official
    create_source(
        url="http://www.pbc.gov.cn/",
        title="People's Bank of China (PBOC) Official",
        tier="tier_1",
        region="China",
        language="Chinese/English",
        publisher="PBOC"
    )

    create_source(
        url="https://www.rbi.org.in/",
        title="Reserve Bank of India (RBI) Official",
        tier="tier_1",
        region="India",
        language="English/Hindi",
        publisher="RBI"
    )

    create_source(
        url="https://www.gold.org/",
        title="World Gold Council",
        tier="tier_1",
        region="Global",
        language="English",
        publisher="World Gold Council"
    )

    create_source(
        url="https://www.en.cips.com.cn/",
        title="China Cross-Border Interbank Payment System (CIPS) Official",
        tier="tier_1",
        region="China",
        language="English/Chinese",
        publisher="CIPS"
    )

    create_source(
        url="https://www.pif.gov.sa/",
        title="Saudi Arabia Public Investment Fund (PIF) Official",
        tier="tier_1",
        region="Saudi Arabia",
        language="English/Arabic",
        publisher="PIF"
    )

    create_source(
        url="https://www.imf.org/",
        title="International Monetary Fund",
        tier="tier_1",
        region="Global",
        language="English",
        publisher="IMF"
    )

    # Tier 2: Established Media
    create_source(
        url="https://www.bloomberg.com/",
        title="Bloomberg News",
        tier="tier_2",
        region="Western",
        language="English",
        publisher="Bloomberg LP"
    )

    create_source(
        url="https://www.arabnews.com/",
        title="Arab News",
        tier="tier_2",
        region="Middle East",
        language="English/Arabic",
        publisher="Saudi Research & Marketing Group"
    )

    create_source(
        url="https://www.al-monitor.com/",
        title="Al-Monitor: Middle East News",
        tier="tier_2",
        region="Middle East",
        language="English",
        publisher="Al-Monitor"
    )

    create_source(
        url="https://www.globaltimes.cn/",
        title="Global Times",
        tier="tier_2",
        region="China",
        language="English/Chinese",
        publisher="People's Daily"
    )

    create_source(
        url="https://www.interfax.ru/",
        title="Interfax Russia",
        tier="tier_2",
        region="Russia",
        language="English/Russian",
        publisher="Interfax"
    )

    create_source(
        url="https://gulfnews.com/",
        title="Gulf News",
        tier="tier_2",
        region="Middle East",
        language="English",
        publisher="Al Nisr Publishing"
    )

    create_source(
        url="https://www.thenationalnews.com/",
        title="The National (UAE)",
        tier="tier_2",
        region="Middle East",
        language="English",
        publisher="Abu Dhabi Media"
    )

    create_source(
        url="https://www.aljazeera.com/",
        title="Al Jazeera",
        tier="tier_2",
        region="Middle East",
        language="English/Arabic",
        publisher="Al Jazeera Media Network"
    )

    create_source(
        url="https://www.scmp.com/",
        title="South China Morning Post",
        tier="tier_2",
        region="China",
        language="English",
        publisher="Alibaba Group"
    )

    create_source(
        url="https://www.cnbc.com/",
        title="CNBC",
        tier="tier_2",
        region="Western",
        language="English",
        publisher="NBCUniversal"
    )

    create_source(
        url="https://www.henleyglobal.com/",
        title="Henley & Partners Private Wealth Migration Report",
        tier="tier_2",
        region="Global",
        language="English",
        publisher="Henley & Partners"
    )

    create_source(
        url="https://www.lseg.com/",
        title="London Stock Exchange Group (LSEG) / ICD Islamic Finance Development Indicator",
        tier="tier_2",
        region="Global",
        language="English",
        publisher="LSEG"
    )

    print()
    print("=" * 70)
    print("✅ STRUCTURED DATA IMPORT COMPLETE!")
    print("=" * 70)
    print()
    print("📊 View metrics at: http://46.62.231.96:3000")
    print("🏛️  View patterns at: http://46.62.231.96:3000")
    print("📚 View sources at: http://46.62.231.96:3000")
    print()

if __name__ == "__main__":
    main()
