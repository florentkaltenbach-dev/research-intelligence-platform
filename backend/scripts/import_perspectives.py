#!/usr/bin/env python3
"""
Import all perspectives for Events 11-16 that were missing from bash script imports.
"""
import requests

API_BASE = "http://localhost:8000/api"

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
        print(f"       {response.text}")
        return False

print("=" * 80)
print("IMPORTING MISSING PERSPECTIVES FOR EVENTS 11-16")
print("=" * 80)
print()

# Event 11: Central Bank Gold Accumulation
print("Event 11: Central Bank Gold...")
add_perspective(11, "Western Mainstream",
    "Western analysis frames as safe haven demand driven by geopolitical uncertainty, inflation hedging, and portfolio diversification. World Gold Council reports emphasize purchases at double the 2010-2021 average. Generally treats as prudent monetary policy without deep geopolitical implications, highlighting Poland (67t H1 2025) and Turkey as leading buyers.",
    ["3,220 tonnes purchased 2022-2024 (3x historical average)", "2022: 1,136t (record), 2023: 1,037t, 2024: 1,044.6t", "Framed as inflation hedge and geopolitical uncertainty response", "Poland leading with 67t in H1 2025 alone", "77% of central banks plan continued purchases"],
    "English")

add_perspective(11, "Chinese State/Academic",
    "PBOC officially added 44 tonnes in 2024, resuming purchases in November 2024. However, Goldman Sachs estimates actual purchases ~40t/month, with one analysis claiming 570t covertly purchased in 2024. Chinese academic sources frame as reserve diversification consistent with yuan internationalization strategy, viewing Western reporting with suspicion. Gold represents only ~5% of China reserves vs 15% global average, suggesting room for expansion.",
    ["Official: 44t added in 2024, total 2,298.53t by Q2 2025", "Alternative estimates: 570t purchased covertly in 2024", "Goldman Sachs estimates ~40t/month actual purchases", "Gold only 5% of reserves vs 15% global average", "Consistent with yuan internationalization strategy"],
    "English/Chinese")

add_perspective(11, "Russian Perspective",
    "Most explicit narrative: directly frames as response to weaponization of dollar and Western sanctions. Russia accumulated 1,244 tonnes (40M oz) from 2014-2020 post-Crimea as prescient strategy. Gold reserves now worth $229B (34.4% of $650B total reserves), offsetting ~33% of $322B frozen assets. Gold appreciation of +$96B (+72%) since early 2022. Presents as essential financial sovereignty tool and insurance against economic warfare, with 2022 proving strategy correct.",
    ["Russia holds 75M oz (~2,330t) worth $229B", "Represents 34-35% of Russia total reserves", "Accumulated 40M oz between 2014-2020 (post-Crimea)", "$322B forex frozen by Western sanctions (2022)", "Gold gains (+$96B) offset 33% of frozen asset losses"],
    "English/Russian")

add_perspective(11, "Indian Interpretation",
    "RBI gold holdings reached 800.78 tonnes (8% of reserves) by September 2023, adding 73t in 2024. Indian analysis presents as dual dynamic where official and consumer demand reinforce each other - cultural affinity meeting monetary policy. Frames gold accumulation as consistent with India 5,000-year gold culture while modernizing reserve management. Less explicitly geopolitical than Russian narrative, emphasizing prudent diversification.",
    ["RBI holds 800.78t (8% of total reserves)", "Added 73 tonnes in 2024", "Cultural-institutional synthesis approach", "5,000-year gold cultural tradition", "Modernizing reserve management while honoring tradition"],
    "English/Hindi")

print()

# Event 12: BRICS Payment Systems
print("Event 12: BRICS Payment Systems...")
add_perspective(12, "Western Mainstream",
    "Skeptical framing: BRICS Pay not operational despite speculation, emphasizes 2030 target as unrealistic, questions feasibility given member rivalries. Notes dollar still commands 58% of global reserves. Treats as aspirational rhetoric with limited practical impact, emphasizing technical challenges and political divisions among BRICS members.",
    ["BRICS Pay prototype shown October 2024 but not operational", "Implementation now targeted for 2030 (delayed)", "Dollar still 58% of global reserves", "Emphasizes member rivalries (India-China tensions)", "Technical challenges and coordination issues highlighted"],
    "English")

add_perspective(12, "Chinese State/Academic",
    "Incrementalist success narrative: emphasizes 95% of China-Russia trade now in yuan/rubles, CIPS processing 52T yuan ($7.2T) annually - 58% of China cross-border transactions. Frames BRICS Pay delays as pragmatic approach favoring bilateral systems over premature multilateral launch. Views Western skepticism as defensive reaction to losing financial infrastructure monopoly. CIPS growth (+42.6% in 2024) demonstrates systematic progress.",
    ["95% of China-Russia trade ($245B) in yuan/rubles", "CIPS processed 175T yuan ($24.47T) in 2024, +42.6% YoY", "176 direct participants, 1,514 indirect, 189 countries coverage", "Bilateral systems preferred over premature multilateral", "Systematic infrastructure building vs rhetoric"],
    "English/Chinese")

add_perspective(12, "Russian Perspective",
    "SPFS now connects 550+ organizations including 150 from 16 foreign countries (expanded to 20 by Jan 2024). Russian analysis presents as successful sanctions circumvention - financial isolation transformed into opportunity for alternative system building. Views 90% local currency settlement as validation of strategy. Emphasizes BRICS expansion (now 47.9% of global population) as historic shift. Critical of Indian hesitation but pragmatic about separate national approaches.",
    ["SPFS: 550 organizations, 150 non-residents from 16-20 countries", "90% intra-BRICS local currency settlement (Putin statement)", "95% China-Russia bilateral trade in yuan/rubles", "Sanctions circumvention successful", "EU banned SPFS June 2024, US OFAC warned institutions Nov 2024"],
    "English/Russian")

add_perspective(12, "Indian Interpretation - CRITICAL DIVERGENCE",
    "MOST AMBIVALENT NARRATIVE and directly contradicts BRICS unity framing. Foreign Minister Jaishankar (December 2024): India has never been for de-dollarization and no proposal for BRICS currency. India pursuing bilateral rupee internationalization via RBI SRVA (Special Rupee Vostro Account) expansion instead of multilateral BRICS system. Views unified system as potential Chinese dominance; prefers Indian-controlled alternatives. US is India largest trade partner with no interest in weakening dollar.",
    ["Jaishankar: India has never been for de-dollarization", "No proposal for BRICS currency - explicit rejection", "RBI SRVA expansion for bilateral rupee settlements", "US is India largest trade partner", "Fears Chinese dominance in unified BRICS system"],
    "English/Hindi")

print()

# Event 13: CIPS Expansion
print("Event 13: CIPS Expansion...")
add_perspective(13, "Western Mainstream",
    "Acknowledges growth (175.49T yuan/$24.45T processed in 2024, +43%) but emphasizes limitations: yuan only 3% of global SWIFT payments vs 48% for dollar. Notes CIPS still relies on SWIFT messaging for many transactions. Presents as regional system lacking global scale compared to SWIFT 11,500+ institutions in 235+ countries.",
    ["175.49T yuan ($24.47T) processed in 2024, +42.6% YoY", "176 direct participants, 1,514 indirect", "Yuan only 3% of SWIFT payments vs 48% USD", "SWIFT has 11,500+ institutions in 235+ countries", "CIPS still uses SWIFT messaging for many transactions"],
    "English")

add_perspective(13, "Chinese State/Academic",
    "Testing ground narrative: PBOC Governor Pan Gongsheng called Africa partnerships key step in advancing economic ties. Emphasizes yuan stablecoin (AxCNH) in Kazakhstan, Shanghai Oil & Gas Exchange yuan pricing, and 40 bilateral settlement agreements. Views CIPS as parallel infrastructure, not SWIFT replacement - real alternative for global trade settlements operating alongside Western system.",
    ["189 countries business coverage through 4,900+ banks", "June 2025: First Africa/ME direct partnerships (6 institutions)", "Transactions/value tripled since 2020", "CAGR 2022-2024: 35% volume, 30% value", "Parallel infrastructure strategy, not SWIFT replacement"],
    "English/Chinese")

add_perspective(13, "African Perspective",
    "Most enthusiastic adoption: Afreximbank and Standard Bank joining as direct participants signals continent-wide integration. African analysis emphasizes: (1) Western banks reducing Africa presence creating vacuum, (2) CIPS offering lower transaction costs than correspondent banking (remittances average 8.5% in sub-Saharan Africa - most expensive globally), (3) BRI loans often yuan-denominated making CIPS natural repayment channel. 53 of 54 African nations in BRI with CIPS access.",
    ["Afreximbank & Standard Bank first African direct participants", "Lower costs than correspondent banking (8.5% average remittance fees)", "53 of 54 African countries in BRI", "Western bank retreat created vacuum", "Standard Bank launching CIPS for clients September 2025"],
    "English")

print()

# Event 14: El Salvador Bitcoin
print("Event 14: El Salvador Bitcoin...")
add_perspective(14, "Western Mainstream",
    "Near-universal framing as failed experiment: only 8.1% used Bitcoin, 80% never used it, 1% of remittances via crypto. IMF $1.4B loan conditional on removing Bitcoin as legal tender. Western economists emphasize volatility, lack of adoption, fiscal irresponsibility. Presents as cautionary tale against cryptocurrency hype and populist economic policies, with CAR parallel failure reinforcing narrative.",
    ["January 30, 2025: Congress voted 55-2 to repeal legal tender status", "Only 8.1% of Salvadorans used Bitcoin (down from 25.7% year 1)", "1.1% of remittances via crypto (0.87% by Dec 2024)", "IMF $1.4B loan conditional on rollback", "Central African Republic also failed after 1 year (2022-2023)"],
    "English")

add_perspective(14, "Chinese State/Academic",
    "Limited coverage but frames as validation of China CBDC (digital yuan) approach: state-controlled, centralized digital currency vs decentralized cryptocurrency. Chinese analysis presents El Salvador case as proof that unregulated crypto cannot serve monetary policy functions. Reinforces China position that digital currencies must be sovereign-issued and controlled.",
    ["Validates state-controlled CBDC approach", "Demonstrates unregulated crypto unsuitability for monetary policy", "China digital yuan model vindicated", "Decentralized crypto lacks institutional backing", "Sovereign control essential for currency function"],
    "English/Chinese")

add_perspective(14, "Russian Perspective",
    "Russian analysis sympathetic to anti-dollar intent but critical of execution. Russia exploring crypto for sanctions evasion but emphasizes need for state control. Views Bitcoin volatility as fatal flaw for reserve asset. Contrasts with Russia methodical gold accumulation and SPFS development as cautionary tale about rushing de-dollarization without proper infrastructure.",
    ["Sympathetic to de-dollarization goal", "Bitcoin volatility fatal for reserve assets", "Russia prefers gold + state-controlled systems", "Methodical infrastructure building vs rushed implementation", "Crypto useful for sanctions evasion but not monetary policy"],
    "English/Russian")

print()

# Event 15: Islamic Finance
print("Event 15: Islamic Finance...")
add_perspective(15, "Western Mainstream",
    "Generally overlooked or minimized in mainstream Western coverage despite $6T scale (larger than many G20 economies). When covered, presents as niche market or specialty finance. Acknowledges sukuk growth (+25.6% to $230.4B in 2024) but rarely contextualizes as parallel financial architecture operating at scale. Tends to emphasize exotic Shariah compliance requirements as barriers rather than features.",
    ["$6T scale rarely contextualized in Western media", "Treated as niche despite exceeding many G20 economies", "Sukuk growth acknowledged but not systemic significance", "Shariah compliance framed as exotic/complex", "Parallel financial architecture aspect ignored"],
    "English")

add_perspective(15, "Middle Eastern View - PRIMARY NARRATIVE",
    "GCC holds 50% of global Islamic finance assets ($2.5-2.7T in 2024, projected $5T+ by 2029). Middle Eastern sources present not as alternative but as authentic system aligned with civilizational values. Saudi Vision 2030 and UAE strategies explicitly prioritize Islamic finance development. Recent: PIF second sukuk, Mubadala debut sukuk (March 2024), green sukuk $4B Q1 2024 (+17% YoY). Frames as moral capitalism surpassing Western system ethical failures (2008 financial crisis).",
    ["GCC holds ~50% of $6T global assets", "Projected $9.7T by 2029 (10% CAGR)", "Iran $2.24T, Saudi $1.31T, Malaysia $761B = 72% global", "Sukuk market >$1T outstanding, $250B issuance 2024", "UAE targeting AED 2.56T banking assets by 2031"],
    "English/Arabic")

add_perspective(15, "African Perspective",
    "Growing African interest, particularly Muslim-majority North/West Africa. African sources emphasize ethics-based approach and profit-loss sharing as potentially more equitable than conventional banking. AfDB and African institutions issuing sukuk to tap Gulf liquidity. Nigeria, South Africa, Egypt issued $3.045B combined in 2024. Views as bridge to Gulf capital and alternative to Western institutions reducing Africa exposure, though capacity constraints and regulatory frameworks lag.",
    ["Nigeria, South Africa, Egypt: $3.045B sukuk 2024", "Ethics-based approach seen as more equitable", "Bridge to Gulf capital access", "Alternative to Western banks retreating from Africa", "Regulatory and capacity constraints remain"],
    "English")

print()

# Event 16: Millionaire Migration
print("Event 16: Millionaire Migration...")
add_perspective(16, "Western Mainstream",
    "Frames as wealth migration driven by personal tax optimization, political stability, business opportunities. Western coverage emphasizes brain drain from high-tax jurisdictions (UK, California, France) to UAE/Singapore. Generally presents as individual choices based on rational economic incentives. Acknowledges geopolitical instability factor but emphasizes personal financial motivations over systemic shifts.",
    ["142,000 HNWIs relocating in 2025 (record high)", "Tax optimization primary driver in Western framing", "UK losing -16,500 (largest outflow)", "High-tax jurisdictions losing to zero-tax havens", "Individual rational choice over systemic interpretation"],
    "English")

add_perspective(16, "Middle Eastern View - UAE TRIUMPHALIST",
    "Leading destination reflects successful national strategy: zero taxes, political stability, luxury infrastructure, strategic location bridging East/West. UAE sources present as validation of diversification from oil economy. Dubai positioning as Switzerland of Middle East with strong rule of law, asset protection. Dubai International Financial Centre hosts 120 family offices managing $1.2T. Emphasizes emergence as alternative to London/New York/Hong Kong with optionality (access to both Western and non-Western systems).",
    ["UAE attracting 9,800 millionaires in 2025 ($63B wealth)", "Golden Visa, zero income/capital gains tax", "DIFC: 120 family offices, $1.2T assets under management", "Strategic location bridging East and West", "Alternative to traditional financial centers"],
    "English/Arabic")

add_perspective(16, "Russian Perspective",
    "Russian oligarchs among those relocating to UAE/Dubai after sanctions. Russian analysis presents as adaptation to financial warfare - moving assets to jurisdictions less susceptible to Western sanctions. UAE refusal to sanction Russia makes it attractive safe haven. Russian sources frame as Western sanctions driving capital to non-Western financial centers, undermining Western financial influence. Real estate doubled to $500M H1 2022, 96.4t gold imported, hundreds of Russian companies created.",
    ["UAE did not impose Russia sanctions", "Russian real estate in Dubai doubled to $500M (H1 2022)", "96.4 tonnes gold imported from Russia (2022)", "Hundreds of Russian companies created since Feb 2022", "UAE on FATF grey list 2022-2024 for money laundering"],
    "English/Russian")

print()
print("=" * 80)
print("✅ ALL PERSPECTIVES IMPORTED!")
print("=" * 80)
