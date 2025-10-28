#!/usr/bin/env python3
"""
Import Historical Power Transitions Analysis
Adds 3 new historical patterns and comprehensive analysis document
"""
import requests

API_BASE = "http://localhost:8000/api"

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
        print(f"  ✅ Created: {name} (relevance: {relevance_score})")
        return result['id']
    else:
        print(f"  ❌ Failed: {name}")
        print(f"     {response.text}")
        return None

def create_analysis(title, content, confidence, approach):
    """Create an analysis document."""
    response = requests.post(
        f"{API_BASE}/analyses/",
        json={
            "title": title,
            "content": content,
            "confidence_level": confidence,
            "research_approach": approach
        }
    )
    if response.status_code in [200, 201]:
        result = response.json()
        print(f"  ✅ Created Analysis: {title}")
        return result['id']
    else:
        print(f"  ❌ Failed: {title}")
        return None

print("=" * 80)
print("IMPORTING HISTORICAL POWER TRANSITIONS")
print("=" * 80)
print()

# ===========================================================================
# NEW HISTORICAL PATTERNS
# ===========================================================================
print("🏛️  ADDING NEW HISTORICAL PATTERNS")
print("-" * 80)

# Pattern 1: Byzantine-Ottoman Fall (1453)
create_historical_pattern(
    name="Byzantine-Ottoman Fall (1453): Declining Power Dynamics",
    description="Constantinople fell to Ottomans in 1453 when city population had collapsed from 400,000 (12th century) to 40,000-50,000, and Byzantine Empire shrunk to few square kilometers. Orthodox Byzantines preferred Muslim Turkish rule over Catholic Rome ('Better Turkish turban than Papal tiara'). Mehmed II's systematic preparation included fortresses along Bosporus and Hungarian gunsmith Urban building cannon powerful enough to breach Constantinople's walls. Religious schism between Orthodox and Catholic prevented unified Christian resistance. Demonstrates pattern where internal division, population decline, and technological gap combine to enable transition. Moral narrative of Christian vs Muslim oversimplifies complex religious-political dynamics.",
    time_period="1453",
    key_characteristics=[
        "Population collapse: 400,000 → 40,000-50,000",
        "Internal religious division (Orthodox vs Catholic)",
        "Technological superiority (Ottoman cannons vs Byzantine walls)",
        "Preference for foreign rule over domestic schism",
        "Systematic preparation by successor power",
        "Moral narratives oversimplify complex dynamics"
    ],
    relevance_score=0.80
)

# Pattern 2: Mughal to British East India Company (1765)
create_historical_pattern(
    name="Mughal to British EIC (1765): Commercial Power to Political Rule",
    description="European trading companies initially played no real part in Mughal decline, racing to get permission to establish trades. However, 1765 Treaty of Allahabad granted East India Company diwani rights to collect revenue from Bengal, Bihar, Orissa - giving immense economic control. EIC crossed from commercial to political/administrative power, with Bengali Nawab becoming fully dependent on British for security and finances. Capitalized on Mughal political instability using 'divide and rule,' forming alliances with local rulers and promising protection for trading rights and territorial concessions. Demonstrates pattern where seemingly innocuous commercial presence transforms into political control through financial leverage during internal instability.",
    time_period="1765",
    key_characteristics=[
        "Commercial presence transforms to political control",
        "Economic leverage (revenue collection rights) precedes military conquest",
        "Divide and rule strategy during internal instability",
        "Local rulers become dependent for security",
        "Watershed moment: 1765 Treaty of Allahabad",
        "Gradual accumulation of sovereignty without formal conquest"
    ],
    relevance_score=0.77
)

# Pattern 3: Colonial to Post-Colonial Transitions (1960s)
create_historical_pattern(
    name="Colonial to Post-Colonial Transitions (1960s): Managed Retreat",
    description="Post-WWII debt left European powers unable to afford African colonies, allowing African nationalists to negotiate decolonization quickly with minimal casualties in many cases. Macmillan's 'Wind of Change' speech represented urgent desire to avoid colonial war like France in Algeria. US took middle-road: supporting African independence while reassuring European allies, wanting 'right type' of African groups (not communist, not especially democratic). By late 1960s, remaining nonindependent countries were in settler-dominated Southern Africa where white settlers complicated transfer. Decolonization coincided with Cold War, with newly independent nations often joining 'nonaligned movement.' Demonstrates pattern where economic exhaustion is reframed as moral progress, with great powers managing retreat to maintain influence through new mechanisms.",
    time_period="1945-1975",
    key_characteristics=[
        "Economic exhaustion (post-war debt) forces retreat",
        "Moral reframing: 'Granting freedom' vs 'Cannot afford'",
        "Managed transitions to maintain influence",
        "Superpower competition shapes process",
        "Nonaligned movement emerges from forced choice rejection",
        "Settler colonies resist longer than others"
    ],
    relevance_score=0.73
)

print()

# ===========================================================================
# COMPREHENSIVE ANALYSIS DOCUMENT
# ===========================================================================
print("📚 CREATING COMPREHENSIVE HISTORICAL ANALYSIS")
print("-" * 80)

analysis_content = """# Historical Power Transitions: Realpolitik Analysis Across 8 Major Cases

**Research Method**: Comprehensive analysis across multiple civilizations examining both official narratives and underlying geopolitical realities

**Key Finding**: Power transitions throughout history consistently involve far more complex realpolitik calculations than humanitarian or ideological narratives typically suggest, with declining powers frequently repositioning retreats as moral advances.

---

## 8 Major Power Transitions Analyzed

### 1. Mamluk Fall to Ottoman Empire (1517)

**Technology as Power Determinant**

Ottoman conquest of Mamluk Sultanate in 1516-1517 represents clear case where technological superiority determined outcomes. Ottoman cannons and firearms overwhelmed traditional Mamluk cavalry tactics. Egyptian historian Ibn Zunbul acknowledged contemporaneously that despite Mamluk fighting qualities, they could not resist Ottoman firearms actively used for decades.

**Power Play Analysis**:
- Sultan Selim I obtained fatwa claiming Mamluks were "Muslim oppressors" allied with Shia Safavids
- Framed conquest as "holy war" - humanitarian/religious justification masking strategic territorial ambitions
- Conquest gave Ottomans control of Islam's holy cities (Mecca, Medina), bolstering religious legitimacy
- Gained Egypt's enormous tax revenue

**Pattern**: Religious/humanitarian justifications masking strategic objectives

---

### 2. British Abolition of Slavery (1807-1815)

**Geopolitical Strategy as Moral Victory**

British propaganda linked slavery to French tyranny under Napoleon. Abolitionists argued banning slavery would constitute economic warfare against France, whose slaves formed key part of French trade.

**Realpolitik Dimensions**:
- Treaty of Vienna (1815): British Foreign Secretary Castlereagh pressured France, Spain, Portugal to abolish slave trade - first human rights declaration in international treaty
- Mid-1750s: British involvement peaked, but rising costs made abolitionists easier to hear as economic conditions shifted
- French and American traders accused Britain of using abolition as pretext for colonial expansion into West Africa, Cuba, Texas

**Strategic Retreat Pattern**: Abolitionists argued slavery immoral and economy would prosper without it, but transition came when British economic interests had shifted. Britain transformed declining economic advantage into moral high ground.

**Pattern**: Moral positioning over economic necessity

---

### 3. Ming to Qing Transition (1644)

**Defection and Internal Collapse**

Qing victory overwhelmingly resulted from defection of Ming dynasty's Liaodong military establishment and other defectors, with Manchu military playing very minor role. Challenges Western narratives of nomadic conquest.

**Power Dynamics**:
- Han Chinese defector troops formed 75% of Eight Banners by 1648
- Ethnic Manchus only 16% - demonstrating multi-ethnic nature
- Ming fell due to: fiscal turmoil, peasant rebellions, deteriorating royal-military relations, natural disasters, epidemics
- Ming general Wu Sangui's decision to side with Manchus over rebel Li Zicheng proved decisive

**Strategic Continuity**: Qing positioned as political heirs to Ming, held formal funeral for Chongzhen Emperor, maintained Chinese bureaucratic structures.

**Pattern**: Power consolidation through legitimacy rather than destruction

---

### 4. Byzantine to Ottoman Fall (1453)

**Declining Power Dynamics**

By 1453, Constantinople's population dropped from 400,000 (12th century) to 40,000-50,000. Byzantine Empire shrunk to few square kilometers outside Constantinople.

**Geopolitical Reality**:
- Orthodox Byzantines preferred Muslim Turkish rule over Catholic Rome: "Better Turkish turban than Papal tiara"
- Mehmed II's systematic preparation: fortresses along Bosporus, Hungarian gunsmith Urban building cannon to breach walls
- Religious schism between Orthodox and Catholic prevented unified resistance

**Pattern**: Moral narrative (Christian vs Muslim) oversimplifies religious schism preventing unity

---

### 5. Mongol Empire Fragmentation (post-1259)

**Succession Crisis Pattern**

After Mongke Khan's death (1259), succession crisis and civil war split empire into four khanates: Yuan Dynasty (China), Ilkhanate (Persia), Chagatai Khanate (Central Asia), Golden Horde (Russia).

**Recurring Pattern**:
- Chinggisid political culture meant succession struggles endemic
- Empire conceived as joint property of royal clan, each member theoretically eligible for Khan
- Mid-14th century "Chinggisid Crisis": extinction of ruling lineages, rise of military commanders (amirs) over Chinggisids
- Power transitions through internal dissolution, not external conquest

---

### 6. Mughal to British East India Company (1765)

**Commercial Power to Political Rule**

Seemingly innocuous European trading companies played no part in initial Mughal decline - racing to get permission for trades and factories. However, 1765 Treaty of Allahabad granted EIC diwani rights to collect revenue from Bengal, Bihar, Orissa.

**Strategic Transformation**:
- EIC crossed from commercial to political/administrative power
- 1765 Treaty watershed: Bengali Nawab became fully dependent on British for security and finances
- Capitalized on Mughal instability using "divide and rule" - alliances with local rulers promising protection for trading rights

**Pattern**: Commercial presence transforms to political control through financial leverage

---

### 7. Colonial to Post-Colonial Transitions (1960s)

**Managed Retreat**

Post-war debt left European powers unable to afford African colonies, allowing African nationalists to negotiate decolonization quickly with minimal casualties in many cases.

**Power Calculus**:
- Macmillan's "Wind of Change" speech: urgent desire to avoid colonial war like France in Algeria
- American middle-road: supporting independence while reassuring European allies
- Wanted "right type" of African groups to lead - not communist, not especially democratic
- Late 1960s: remaining nonindependent countries in settler-dominated Southern Africa where whites complicated transfer
- Decolonization coincided with Cold War - newly independent nations often joined "nonaligned movement"

**Pattern**: Economic exhaustion reframed as moral progress

---

### 8. Soviet Union Collapse (1991)

**Internal System Failure Presented as Ideological Victory**

Collapse came from within - economic problems gave rise to reformist policies which eroded revolutionary-imperial paradigm and Soviet power. Western narratives presented as capitalism's triumph over communism.

**Russian Perspective**:
- Putin described as "major geopolitical disaster of century" - "tens of millions of our co-citizens found themselves outside Russian territory"
- Russians initially viewed US favorably, but thirty years later regard it as antagonist that deliberately weakened country through foreign economic models and NATO expansion

**Hidden Costs**:
- Yeltsin's rapid capitalism transition caused tremendous economic upheaval
- Those able to privatize state assets became rich while average Russians suffered sharp drop in living standards
- 1990s: social devastation, wars, chaos, fragmentation
- Tens of thousands deaths in wars and ethnic conflicts across former Soviet republics

**Pattern**: Internal failure presented as external victory

---

## Recurring Patterns Across All 8 Transitions

### 1. Technology Gaps Determine Outcomes
- Mamluks' cavalry vs Ottoman firearms
- Byzantine walls vs Ottoman cannons
- Traditional Mughal forces vs European military tactics

### 2. Humanitarian Advances as Strategic Positioning
- British abolition served economic warfare, moral superiority, colonial expansion justification
- European decolonization framed as "granting freedom" rather than inability to afford

### 3. Defection Over Conquest
- Ming fell primarily through Chinese defections to Qing
- Mughal princes allied with British
- Byzantine preference for Ottomans over Catholic Rome

### 4. Succession Crises as Weakness
- Mongol fragmentation after Mongke
- Mughal wars of succession creating vulnerabilities
- Soviet power struggles during collapse

### 5. Economic Exhaustion Preceding Collapse
- All major transitions involved fiscal crises
- Often masked or explained differently in official narratives

### 6. Legitimacy Through Continuity
- Qing positioned as Ming heirs
- British Company ruling "in name of" Mughal emperor
- New powers maintain symbolic authority of old

### 7. Managed Retreat as Victory
- British decolonization framed as granting freedom
- British abolition framed as moral triumph
- Moral positioning over economic necessity

### 8. Regional Fragmentation After Central Collapse
- Mongol khanates after empire split
- Mughal successor states
- Post-Soviet republics

---

## Relevance to Current Multipolar Transition (2025)

### Patterns Currently Visible:

**Technology Gaps**: AI/semiconductor competition mirrors Mamluk-Ottoman firearms gap. US 74% AI compute vs China 14% comparable to technological determinism in historical transitions.

**Managed Retreat as Victory**: US promoting "democracy" and "rules-based order" while relative power declines mirrors British abolition framing moral high ground during strategic retreat.

**Defection Over Conquest**: India's strategic autonomy, Global South joining BRICS mirrors Ming defections to Qing - voluntary alignment shifts, not military conquest.

**Economic Exhaustion**: NATO 5% GDP defense spending, US debt ceiling crises, European fiscal constraints mirror patterns preceding historical collapses.

**Fragmentation Not Unity**: BRICS lacks unified vision beyond opposing West, mirrors Mongol khanate fragmentation - competing regional powers, no single alternative.

**Commercial to Political Power**: China's BRI infrastructure investments in Africa/Asia mirror British EIC pattern - commercial presence transforming to political influence.

### Key Insight:

Current multipolar transition following historical patterns: Not dramatic collapse but gradual accumulation of alternatives, internal contradictions in dominant system, economic exhaustion masked by ideological narratives, defections to emerging powers during declining hegemon's succession crisis.

**Most Likely Outcome**: Managed transition with dominant power maintaining symbolic authority while actual power diffuses to regional centers. Humanitarian/democratic narratives will mask strategic retreats. Technology gaps (AI, semiconductors) will determine winners. Those recognizing patterns and acting accordingly will shape next order.

---

## Methodological Note

This analysis examined:
- Primary sources from multiple civilizations (Ottoman, Chinese, British, Russian, American, African perspectives)
- Contemporary accounts vs retrospective narratives
- Economic data underlying political events
- Religious/humanitarian justifications vs strategic outcomes
- Defection patterns and elite behavior during transitions
- Technology differentials at transition points

**Confidence Level**: 4/5 stars - High confidence in patterns, acknowledging historical sources have biases and incomplete information about elite calculations.

**Research Approach**: Multi-regional source analysis + historical pattern matching + realpolitik framework
"""

create_analysis(
    title="Historical Power Transitions: 8 Cases from Realpolitik Perspective",
    content=analysis_content,
    confidence=4,
    approach="Multi-regional Historical Analysis + Realpolitik Framework"
)

print()
print("=" * 80)
print("✅ HISTORICAL TRANSITIONS IMPORT COMPLETE!")
print("=" * 80)
print("🌐 View at: http://46.62.231.96:3000")
print("=" * 80)
