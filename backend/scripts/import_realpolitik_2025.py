#!/usr/bin/env python3
"""
Import Realpolitik & Power Transitions 2025 Research
Based on comprehensive multi-perspective analysis of global power dynamics
"""
import requests

API_BASE = "http://localhost:8000/api"
SUCCESS_COUNT = 0

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
        global SUCCESS_COUNT
        SUCCESS_COUNT += 1
        print(f"  ✅ Created Event {result['id']}: {title[:60]}...")
        return result['id']
    else:
        print(f"  ❌ Failed to create event: {title}")
        print(f"     {response.text}")
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
        return True
    else:
        print(f"    ❌ Failed: {region}")
        return False

print("=" * 80)
print("IMPORTING REALPOLITIK & POWER TRANSITIONS 2025 RESEARCH")
print("=" * 80)
print()

# ============================================================================
# EVENT 1: INDIA'S STRATEGIC AUTONOMY
# ============================================================================
print("Event 1: India's Strategic Autonomy & Multi-Alignment...")

event_id = create_event(
    title="India's Strategic Autonomy: Multi-Alignment Between Quad, Russia, and China",
    description="India maintains strategic autonomy through multi-alignment policy, participating in Quad with US/Japan/Australia while importing 36% of weapons from Russia (down from 55% in 2015-19) and maintaining $140B trade with China despite 2020 Galwan clash. Took delivery of 3 Russian S-400 systems in 2023, expects 2 more by 2025. Refused to condemn Russia-Ukraine war despite Quad pressure. October 2024 border agreement with China shows functional relations with rivals. Strategic autonomy faces strain as US-China decoupling intensifies, with both being India's largest trading partners.",
    date="2024-10-01T00:00:00",
    region="India/Global",
    impact_level="high"
)

if event_id:
    add_perspective(event_id, "Western/US Perspective",
        "US views India as vital to counter China's rise in Indo-Pacific, making India cornerstone of Quad strategy. Frustrated by India's refusal to condemn Russia over Ukraine and continued arms imports. Recognizes India needs 'strategic autonomy' but pushes for closer alignment. Sees India as future great power that could balance China if properly aligned. Concerned about India-China rapprochement undermining containment strategy. US defense cooperation with India growing but Russia remains 36% of India's weapons imports.",
        ["India vital to Indo-Pacific strategy and Quad", "Frustrated by India neutrality on Russia-Ukraine", "US-India defense cooperation growing", "Concerns about India-China border agreement Oct 2024", "India strategic autonomy complicates US alliance structure"],
        "English")

    add_perspective(event_id, "Indian Perspective",
        "India frames strategic autonomy as core principle of post-Cold War foreign policy. Refuses binding alliances, instead maintains flexible partnerships across rivals. Views Quad as security cooperation, not military alliance. Russia relationship valued for defense technology transfer and energy (35-40% crude imports). China relationship managed pragmatically despite border tensions - $140B trade and Oct 2024 agreement shows functional ties. India positioning as leader of Global South, bridging East-West divide. Sees multi-alignment as maximizing options in multipolar world.",
        ["Strategic autonomy = core foreign policy principle", "Multi-alignment maximizes options in multipolar world", "Quad is cooperation, not alliance", "Russia valued for defense tech and energy", "China tensions managed, trade functional", "Positioning as Global South leader"],
        "English/Hindi")

    add_perspective(event_id, "Russian Perspective",
        "Russia views India as critical partner for evading Western sanctions. India-Russia trade reached $66B, largely settled in local currencies. Energy exports to India offset Western market losses. Defense relationship remains strong despite India diversifying suppliers (36% from Russia vs 55% previously). Concerned about India's Quad participation and growing US ties, but pragmatic about India's multi-alignment. Sees India as proof that non-Western powers can resist US pressure. Views India-Russia-China triangle as ideal but accepts India-China tensions limit full alignment.",
        ["India critical for sanctions evasion, $66B trade", "Energy exports to India offset Western losses", "Defense relationship strong but declining share", "Accepts India's multi-alignment pragmatically", "India proves non-Western can resist US pressure", "Ideal: Russia-India-China triangle, reality: complications"],
        "English/Russian")

    add_perspective(event_id, "Chinese Perspective",
        "China sees India as both partner and rival. Trade at $140B makes India major economic partner despite border tensions. October 2024 border agreement shows both sides prefer functional relations. Concerned about India's Quad participation as containment effort. Views India's strategic autonomy as preventing full US alignment, which benefits China. Recognizes India as emerging competitor for Global South leadership. Long-term: China expects India to be major power center in multipolar world, prefers managed competition to confrontation.",
        ["$140B trade despite border tensions", "Oct 2024 agreement shows preference for functional relations", "Quad concerns but India autonomy prevents full US alignment", "Competition for Global South leadership", "Long-term: India emerging power center", "Prefer managed competition to confrontation"],
        "English/Chinese")

print()

# ============================================================================
# EVENT 2: AI INFRASTRUCTURE ARMS RACE
# ============================================================================
print("Event 2: AI Infrastructure Arms Race...")

event_id = create_event(
    title="AI Infrastructure Arms Race: $325 Billion Big Tech Investment in 2025",
    description="Big Tech spending $320-325B combined in 2025 on AI infrastructure (+46% from $223B in 2024). Google: $75B, Meta: $60-65B (Zuckerberg: '2025 = defining year for AI'), Microsoft: $80B fiscal 2025 (data centers), Amazon: ~$105B. Nvidia dominates GPU supply, bought 4% Intel stake for $5B (Sept 2025) + $100B OpenAI investment in GPUs. US controls 74% global high-end AI compute vs China 14%, EU 4.8%. Cumulative US private AI investment 2013-2024: $470B vs EU $50B. China's DeepSeek challenge (Jan 2025) questions if massive spending necessary. CHIPS Act + related policies catalyzed $2.3T semiconductor investment 2024-2032, US projected 28% global capex by 2032.",
    date="2025-01-01T00:00:00",
    region="Global/US-China",
    impact_level="critical"
)

if event_id:
    add_perspective(event_id, "Western/US Perspective",
        "Frames as existential competition for technological leadership. Big Tech spending seen as necessary to maintain US dominance in AI - 'whoever wins AI wins everything' narrative. CHIPS Act and semiconductor investments framed as national security imperative. US controls 74% high-end AI compute, wants to maintain lead. DeepSeek shock (Jan 2025) caused investor panic but industry argues US approach necessary for frontier models. Views China as closing gap despite export controls. Semiconductor fragmentation necessary even if costly. Sees AI as defining 21st century like oil defined 20th.",
        ["Big Tech $325B spending framed as necessary for leadership", "US 74% global AI compute, must maintain dominance", "DeepSeek raised efficiency questions but dismissed", "China closing gap despite export controls", "CHIPS Act: $2.3T investment as national security", "AI = 21st century oil analogy"],
        "English")

    add_perspective(event_id, "Chinese Perspective",
        "DeepSeek (Jan 2025) presented as proof China can do more with less - efficiency over brute force. Framed as validation of alternative approach to AI development. China controls 14% high-end compute but argues constraints force innovation. Views US export controls as failing - China advancing despite restrictions. Semiconductor investment focuses on self-sufficiency and catching up in key nodes. Sees AI race as marathon, not sprint. Notes US spending may be inefficient and unsustainable. Long-term: China expects to close gap through indigenous innovation and state coordination.",
        ["DeepSeek proves efficiency over brute force approach", "Constraints forcing Chinese innovation", "US export controls failing to prevent advances", "Self-sufficiency focus in semiconductors", "AI race is marathon, US lead not permanent", "State coordination advantage over market chaos"],
        "English/Chinese")

    add_perspective(event_id, "European Perspective",
        "EU deeply concerned about falling behind in AI race - only 4.8% global high-end compute, $50B investment vs US $470B. Recognizes strategic vulnerability in both AI and semiconductors. Debate between supporting European champions vs partnering with US/Asian firms. Regulatory approach (AI Act) seen domestically as necessary but criticized internationally as handicapping EU competitiveness. ASML (Netherlands) controls extreme UV lithography, giving EU leverage in semiconductor supply chain. Struggles with fragmentation - no EU-wide tech champion comparable to US Big Tech. Growing recognition that digital sovereignty requires massive state investment.",
        ["EU only 4.8% AI compute, $50B vs US $470B", "Strategic vulnerability recognized", "Regulatory approach may handicap competitiveness", "ASML gives leverage in semiconductor chain", "Fragmentation prevents EU champions", "Digital sovereignty requires state investment"],
        "English")

print()

# ============================================================================
# EVENT 3: NATO 5% DEFENSE SPENDING
# ============================================================================
print("Event 3: NATO 5% Defense Spending Target...")

event_id = create_event(
    title="NATO 5% GDP Defense Spending: $2.9 Trillion by 2035 Rearmament",
    description="June 2025 NATO Summit in The Hague: Allies committed to 5% GDP defense spending by 2035, split as 3.5% core defense + 1.5% infrastructure/cyber/resilience/industrial base. More than doubles from 2% target. Global military spending reached $2.718T in 2024 (+9.4% YoY, steepest rise since 1988), with NATO $1.506T (55% global). European NATO $454B (30% of alliance). Projected impact: If all NATO allies meet 2035 target, need $1.4T more annually than 2024, putting NATO total at $2.9T. Decade of consecutive increases: +37% from 2015-2024. European spending rose from 1.43% GDP (2014) to 2.02% (2024), now targeting 5% by 2035.",
    date="2025-06-25T00:00:00",
    region="Global/NATO",
    impact_level="critical"
)

if event_id:
    add_perspective(event_id, "Western/NATO Perspective",
        "Framed as necessary response to Russian aggression and Chinese assertiveness. 5% target driven by Trump administration pressure and European recognition that US security guarantee not permanent. Ukraine war proves Europe must defend itself. European leaders emphasize sacrifice necessary - defense vs healthcare/welfare trade-offs explicit. Baltic states, Poland see existential threat from Russia. Western Europe slower to embrace but gradually accepting necessity. Sees decade-long rearmament as reversing post-Cold War 'peace dividend' cuts. Industrial base atrophied during peacetime, must rebuild.",
        ["Response to Russian threat and Chinese rise", "Trump pressure + European self-defense recognition", "Ukraine proves Europe must defend itself", "Defense vs welfare explicit trade-offs", "Reversing post-Cold War peace dividend", "Industrial base rebuild necessary"],
        "English")

    add_perspective(event_id, "Russian Perspective",
        "Views NATO expansion and rearmament as proof of Western hostility. Frames 5% spending as preparation for eventual confrontation with Russia. Argues NATO outspends Russia already ($1.506T vs Russia's lower spending), making claims of defensive nature implausible. Sees Ukraine as proxy war and NATO expansion as existential threat. Notes Europe's economic struggles make 5% unsustainable long-term. Emphasizes Russia's asymmetric advantages: nuclear arsenal, resource self-sufficiency, tested defense industry. Views NATO cohesion as fragile - US-Europe tensions, Turkey's independence, Hungary's resistance show cracks.",
        ["NATO expansion + rearmament proves Western hostility", "5% preparing for confrontation with Russia", "Already massive spending gap: NATO $1.5T vs Russia", "Ukraine = proxy war, expansion = threat", "Europe's 5% economically unsustainable", "Russia has asymmetric advantages: nuclear, resources, industry"],
        "English/Russian")

    add_perspective(event_id, "Chinese Perspective",
        "China notes NATO's Indo-Pacific focus beyond traditional Atlantic area. Sees 5% spending as part of broader US strategy to contain China. Questions NATO's defensive claims given expansion into Asia-Pacific through Japan, South Korea, Australia partnerships. Views massive defense spending as sign of Western economic militarization and declining competitiveness. Argues China's lower defense spending as percentage of GDP (estimated 1.5-2%) shows peaceful intentions. Frames NATO rearmament as diverting resources from economic competition where China excels. Expects European fiscal limits to constrain actual spending.",
        ["NATO expanding to Indo-Pacific = China containment", "5% spending shows Western militarization", "Questions 'defensive' claims given Asia-Pacific expansion", "China 1.5-2% GDP shows peaceful intentions", "Diverts resources from economic competition", "European fiscal reality will constrain spending"],
        "English/Chinese")

print()

# ============================================================================
# EVENT 4: US SOVEREIGN WEALTH FUND
# ============================================================================
print("Event 4: US Sovereign Wealth Fund & State Capitalism...")

event_id = create_event(
    title="US Sovereign Wealth Fund: State Capitalism Emerges in Market Economy",
    description="February 2025: Trump announced US sovereign wealth fund, taking 'bottom-up, ad hoc, industrial strategy-driven' approach. CHIPS Act equity-for-grants: US received 10% stake in Intel (Aug 2025, $8.9B awards). Pentagon invested $400M in MP Materials (rare earths), becoming largest shareholder with potential 15% stake - only US rare earth producer. TikTok deal includes US 'golden shares' for veto power. Strategic Bitcoin reserve created March 2025: $5B+ seized BTC (~200,000 coins). Foreign funding component: Japan's $550B investment package tied to tariff deal. White House: 'Government's stake in Intel part of broader SWF strategy for more companies.' Marks shift to state capitalism even in traditional free-market economy.",
    date="2025-02-01T00:00:00",
    region="United States",
    impact_level="high"
)

if event_id:
    add_perspective(event_id, "US Domestic Perspective",
        "Mixed reactions across political spectrum. Industrial policy advocates see validation of state role in strategic sectors. Free-market conservatives uncomfortable with government equity stakes but accept national security justification. CHIPS Act positioned as response to China's state capitalism - 'if they do it, we must.' Intel stake framed as protecting vital semiconductor capacity. MP Materials investment seen as breaking Chinese rare earth monopoly. Tech industry divided: Some welcome state backing, others fear government control. Bitcoin reserve criticized by fiscal conservatives, praised by crypto advocates. Overall: Pragmatic acceptance that market alone insufficient for strategic competition.",
        ["Industrial policy advocates validated", "Free-market discomfort but national security accepts", "Response to China state capitalism", "Intel stake protects semiconductor capacity", "MP Materials breaks Chinese rare earth monopoly", "Pragmatic shift: market alone insufficient"],
        "English")

    add_perspective(event_id, "Chinese Perspective",
        "Frames as vindication of China's state-led development model. US adopting Chinese approach after decades of criticizing it proves state capitalism superiority. Sees hypocrisy in US maintaining 'free market' rhetoric while implementing dirigisme. Views Intel stake as admission that market failed to compete with Chinese industrial policy. Notes US starting from weaker position - China's state capacity more developed. Expects US political system to constrain effectiveness compared to China's coordinated approach. Sees opportunity: While US debates, China executes. Long-term: Validates multipolar model where each system competes on results, not ideology.",
        ["Vindication of China state-led model", "US adopting Chinese approach after criticizing it", "Proves state capitalism superiority", "Intel stake = market failed vs Chinese policy", "US state capacity weaker, politics constrain", "China executes while US debates"],
        "English/Chinese")

    add_perspective(event_id, "European Perspective",
        "Europe recognizes own version of state capitalism (Airbus model) vindicated. US shift reduces pressure on European industrial policy. Sees US-China convergence on state role while Europe maintains hybrid model. Concerned about being squeezed between US and Chinese state champions. Intel case shows US now competitor for European semiconductor ambitions (ASML dependence remains). MP Materials investment threatens European rare earth strategies. Views US approach as improvised vs Europe's institutional frameworks (EIB, national development banks). Questions US sustainability - political cycles may reverse policy. Europe's patient capital model may prove more durable.",
        ["European state capitalism (Airbus) vindicated", "US shift reduces pressure on EU industrial policy", "US-China convergence, Europe maintains hybrid", "Squeezed between US-China state champions", "US improvised vs EU institutional frameworks", "Questions US sustainability across political cycles"],
        "English")

print()

# ============================================================================
# EVENT 5: SUPPLY CHAIN REGIONALIZATION
# ============================================================================
print("Event 5: Supply Chain Regionalization & Friend-Shoring...")

event_id = create_event(
    title="Supply Chain Regionalization: $2.3 Trillion Semiconductor Fragmentation",
    description="Semiconductor supply chains fragmenting into regionalized blocs driven by 'techno-nationalism.' Era of integrated global supply chain over, replaced by strategic rivalries and 'technological iron curtain.' Friend-shoring: Companies building allied-centric supply chains (TSMC Arizona, Vietnam, Europe facilities). CHIPS Act catalyzed $2.3T wafer fab investment 2024-2032, US projected 28% global semiconductor capex by 2032. Critical minerals: US 100% import-reliant on 12+ of 50 critical minerals, China dominates supply. China export controls: Gallium/germanium (July 2023), rare earths expansion (Oct 2025). US strategy: Multilateral friend-shoring, substitute suppliers, stockpiles. Inevitable result: Higher costs, bifurcated global semiconductor market within 3 years. Regionalization extends to batteries, rare earths, pharmaceuticals.",
    date="2025-10-01T00:00:00",
    region="Global",
    impact_level="critical"
)

if event_id:
    add_perspective(event_id, "Western/US Perspective",
        "Frames supply chain regionalization as necessary despite economic costs. Pandemic and China risks proved overdependence vulnerability. Semiconductors framed as 'new oil' - too strategic to rely on geopolitical rivals. CHIPS Act and friend-shoring seen as insurance policy even if expensive. Critical minerals dependence on China identified as strategic liability - US 100% import-reliant on 12+ minerals. Taiwan vulnerability (90% advanced chips) drives geographic diversification urgency. Economic cost accepted as national security premium. Long-term: Expects allied blocs to achieve economies of scale, offsetting efficiency losses from China decoupling.",
        ["Supply chain security worth economic cost", "Semiconductors = 'new oil', too strategic for rivals", "CHIPS Act insurance despite expense", "Critical minerals dependence = strategic liability", "Taiwan vulnerability drives diversification", "Allied blocs will achieve scale economies"],
        "English")

    add_perspective(event_id, "Chinese Perspective",
        "China views Western friend-shoring as attempted containment doomed to fail. Emphasizes China's integrated advantages: Complete supply chain, rare earth dominance (gallium, germanium controls July 2023; rare earths Oct 2025), massive domestic market. Argues friend-shoring will increase costs without eliminating China dependence - too embedded in global supply chains. Notes Western companies still investing in China despite rhetoric. 'Silicon sovereignty' push: China increasing self-sufficiency in semiconductors, though lagging in advanced nodes. Sees US-led fragmentation as opportunity: Forces China to innovate domestically, reduces Western leverage. Long-term: Expects China and Global South to form larger bloc than Western allies.",
        ["Friend-shoring = attempted containment, will fail", "China advantages: Complete chain, rare earth dominance, huge market", "Fragmentation increases costs without eliminating dependence", "Silicon sovereignty: Self-sufficiency in semiconductors", "Forces domestic innovation, reduces Western leverage", "China + Global South bloc larger than West"],
        "English/Chinese")

    add_perspective(event_id, "Neutral/Small States Perspective (Singapore, Vietnam, Mexico)",
        "Small states see opportunity and risk in regionalization. Vietnam, Mexico benefit from friend-shoring (TSMC, Apple supply chain shifts). Singapore positioned as neutral hub between blocs. Risk: Forced to choose sides could damage economic model based on serving all markets. Manufacturing capacity moves create jobs but technology transfer limited vs previous globalization era. Critical minerals producers (DRC cobalt, Chile lithium, Indonesia nickel) gain leverage but face pressure to align with blocs. Overall strategy: Maximize benefits from multiple relationships while delaying forced choice as long as possible. Sees regionalization as managed correctly could increase middle power influence.",
        ["Vietnam/Mexico benefit from friend-shoring", "Singapore aims to stay neutral hub", "Risk: Forced choice could damage open economy model", "Tech transfer more limited than previous globalization", "Mineral producers gain leverage but face bloc pressure", "Strategy: Maximize multi-alignment, delay forced choice"],
        "English")

print()

print("=" * 80)
print("✅ REALPOLITIK RESEARCH IMPORT COMPLETE!")
print("=" * 80)
print(f"Successfully imported: {SUCCESS_COUNT} events")
print()
print("🌐 View at: http://46.62.231.96:3000")
print("=" * 80)
