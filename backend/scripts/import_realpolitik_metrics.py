#!/usr/bin/env python3
"""
Import metrics and additional event related to Realpolitik research
"""
import requests

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
        print(f"  ✅ Created metric: {name}")
        return result['id']
    else:
        print(f"  ❌ Failed: {name} - {response.text}")
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
        print(f"    ❌ Failed datapoint: {response.text}")

def create_event(title, description, date, region, impact_level):
    """Create an event and return its ID."""
    response = requests.post(
        f"{API_BASE}/events/",
        json={
            "title": title,
            "description": description,
            "date": date,
            "region": region,
            "impact_level": impact_level
        }
    )
    if response.status_code in [200, 201]:
        result = response.json()
        print(f"  ✅ Created Event {result['id']}: {title[:60]}...")
        return result['id']
    else:
        print(f"  ❌ Failed: {title} - {response.text}")
        return None

def add_perspective(event_id, region, summary, key_points, language):
    """Add a perspective to an event."""
    response = requests.post(
        f"{API_BASE}/events/{event_id}/perspectives",
        json={
            "region": region,
            "summary": summary,
            "key_points": key_points,
            "language": language
        }
    )
    if response.status_code in [200, 201]:
        print(f"    ✅ {region}")
    else:
        print(f"    ❌ Failed: {region}")

print("=" * 80)
print("IMPORTING REALPOLITIK METRICS & AFRICA EVENT")
print("=" * 80)
print()

# ============================================================================
# METRICS
# ============================================================================
print("📊 CREATING METRICS")
print("-" * 80)

# Metric: AI Infrastructure Spending
metric_id = create_metric(
    name="Big Tech AI Infrastructure Spending",
    description="Combined annual capital expenditure on AI infrastructure by Google, Meta, Microsoft, Amazon",
    unit="billion USD",
    category="technology"
)
if metric_id:
    add_datapoint(metric_id, 223, "2024-12-31T00:00:00", "Combined spending by Big 4")
    add_datapoint(metric_id, 325, "2025-12-31T00:00:00", "+46% increase")

# Metric: US AI Compute Share
metric_id = create_metric(
    name="US Share of Global AI Compute",
    description="US percentage of global high-end AI compute capacity",
    unit="percentage",
    category="technology"
)
if metric_id:
    add_datapoint(metric_id, 74, "2025-01-01T00:00:00", "US 74%, China 14%, EU 4.8%")

# Metric: NATO Defense Spending
metric_id = create_metric(
    name="NATO Combined Defense Spending",
    description="Total military expenditure by all NATO member states",
    unit="trillion USD",
    category="defense"
)
if metric_id:
    add_datapoint(metric_id, 1.506, "2024-12-31T00:00:00", "55% of global military spending")
    add_datapoint(metric_id, 2.9, "2035-12-31T00:00:00", "Projected if 5% GDP target met")

# Metric: Global Military Expenditure
metric_id = create_metric(
    name="Global Military Expenditure",
    description="Total worldwide military spending",
    unit="trillion USD",
    category="defense"
)
if metric_id:
    add_datapoint(metric_id, 2.718, "2024-12-31T00:00:00", "+9.4% YoY, steepest since 1988")

# Metric: India Arms Imports from Russia
metric_id = create_metric(
    name="India Weapons Imports from Russia",
    description="Percentage of India's weapons imports from Russia",
    unit="percentage",
    category="defense"
)
if metric_id:
    add_datapoint(metric_id, 72, "2014-01-01T00:00:00", "2010-2014 average")
    add_datapoint(metric_id, 55, "2019-12-31T00:00:00", "2015-2019 average")
    add_datapoint(metric_id, 36, "2024-12-31T00:00:00", "2020-2024, diversifying suppliers")

# Metric: Semiconductor Capital Expenditure
metric_id = create_metric(
    name="Global Semiconductor Capital Expenditure",
    description="Worldwide capital investment in semiconductor fabrication facilities",
    unit="trillion USD",
    category="technology"
)
if metric_id:
    add_datapoint(metric_id, 2.3, "2024-01-01T00:00:00", "2024-2032 projected investment wave")

print()

# ============================================================================
# EVENT: AFRICA IN MULTIPOLAR ORDER
# ============================================================================
print("🌍 CREATING AFRICA EVENT")
print("-" * 80)

event_id = create_event(
    title="Africa in Multipolar Order: 30% Critical Minerals & US-China Competition",
    description="Africa holds ~30% of global critical mineral deposits. DRC produces 75% of global cobalt output. China invested $4.5B in lithium projects (Zimbabwe, DRC, Mali, Namibia), dominates refining and supply chains. US/EU seek access through partnerships to break Chinese dominance. BRICS expansion includes Egypt, Ethiopia - network now 50% global GDP (PPP) and >50% world population. Africa's importance rising: UN voting power (54 nations), critical minerals for green transition, young demographics (median age 19 vs 43 Europe), migration concerns for Europe. Chinese-led South-South cooperation competing with Western development models. Strategic autonomy allows African states to play rivals against each other for better deals.",
    date="2025-01-01T00:00:00",
    region="Africa",
    impact_level="high"
)

if event_id:
    add_perspective(event_id, "Western/US Perspective",
        "Africa seen as critical battleground in great power competition, particularly for minerals essential to green energy transition. US/EU recognize late start vs China's decade-plus infrastructure/mining investments. Approach: Partnerships and 'values-based' investment emphasizing governance, transparency, labor standards vs Chinese model. Concerned about losing influence - China doesn't demand political reforms, making it attractive partner for African governments. Migration pressure from Africa to Europe adds urgency to engagement. Sees Africa's 54 UN votes as geopolitically significant. Strategy: Build Better World, Prosper Africa initiatives to counter BRI.",
        ["Africa critical for green transition minerals", "Late start vs China decade-plus investments", "Partnership approach emphasizing governance/transparency", "China no-strings approach more attractive to African govts", "Migration concerns drive European engagement", "54 UN votes geopolitically significant"],
        "English")

    add_perspective(event_id, "Chinese Perspective",
        "Frames Africa engagement as South-South cooperation and anti-colonial solidarity, contrasting with Western 'neo-imperialism.' China's $4.5B lithium investments and infrastructure projects presented as win-win development. No political conditionality seen as respecting sovereignty vs Western imposing values. BRI in Africa: Roads, rails, ports, energy projects addressing infrastructure gap Western countries failed to fill. BRICS expansion including Egypt, Ethiopia strengthens Global South bloc. Long-term: Africa's young population (1.3B now, 2.5B by 2050) represents future consumer market and geopolitical weight. China positioning early for African century.",
        ["South-South cooperation vs Western neo-imperialism", "$4.5B lithium + infrastructure = win-win development", "No political conditions respects sovereignty", "BRI fills infrastructure gap West neglected", "BRICS expansion (Egypt, Ethiopia) strengthens Global South", "Africa's young population = future market and power"],
        "English/Chinese")

    add_perspective(event_id, "African Perspective",
        "African states increasingly asserting strategic autonomy, playing great powers against each other for better deals. Frustrated with Western conditionality and lectures while China delivers infrastructure. Resource nationalism rising: African states demanding more value capture - processing, refining locally vs exporting raw materials. DRC pushing to process cobalt domestically. BRICS membership (South Africa, Egypt, Ethiopia) seen as diversifying options beyond West-dominated institutions. Concerns about Chinese debt, labor practices, but pragmatic about needing investment. Youth bulge offers demographic dividend if jobs created, crisis if not. Climate change disproportionately affecting Africa despite minimal contribution to emissions.",
        ["Strategic autonomy: Playing powers against each other", "China delivers infrastructure, West lectures", "Resource nationalism rising: Local processing demanded", "BRICS diversifies options beyond Western institutions", "Chinese debt concerns but need investment", "Youth bulge: Dividend if jobs, crisis if not"],
        "English/Swahili/French/Arabic")

print()
print("=" * 80)
print("✅ METRICS & AFRICA EVENT IMPORT COMPLETE!")
print("=" * 80)
print("🌐 View at: http://46.62.231.96:3000")
print("=" * 80)
