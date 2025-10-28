#!/bin/bash
# Import final 4 events (4-7) from Global Capital Flows 2025 research

API_BASE="http://localhost:8000/api"
SUCCESS_COUNT=0

echo "========================================================================"
echo "IMPORTING FINAL 4 EVENTS (CIPS, El Salvador, Islamic Finance, Migration)"
echo "========================================================================"
echo ""

create_event() {
    RESPONSE=$(curl -s -X POST "$API_BASE/events/" -H "Content-Type: application/json" -d "$1")
    EVENT_ID=$(echo "$RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null)
    if [ ! -z "$EVENT_ID" ]; then
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        echo "  ✅ Created (ID: $EVENT_ID)"
    fi
    echo "$EVENT_ID"
}

add_perspective() {
    curl -s -X POST "$API_BASE/events/$1/perspectives" -H "Content-Type: application/json" -d "$2" > /dev/null
    REGION=$(echo "$2" | python3 -c "import sys, json; print(json.load(sys.stdin)['region'])")
    echo "    + $REGION"
}

# EVENT 4: CIPS EXPANSION
echo "Event 4: China CIPS Expansion..."
E4='{
  "title": "China CIPS Expansion to 185+ Countries (176 Direct Participants)",
  "description": "China Cross-Border Interbank Payment System (CIPS) reached 176 direct participants and 1,514 indirect participants across 121 countries, with business coverage extending to 189 countries and 4,900+ banking institutions. Processed 175.49 trillion yuan ($24.47T) in 2024 (+42.6% YoY), tripling since 2020. June 2025 marked first direct partnerships with 6 institutions in Africa/Middle East: Afreximbank, Standard Bank (South Africa), First Abu Dhabi Bank, UOB Singapore, Eldik Bank (Kyrgyzstan), and Chongwa Macau. Despite growth, yuan represents only 3% of global SWIFT payments vs 48% USD.",
  "date": "2025-06-15T00:00:00",
  "region": "Global/China",
  "impact_level": "high"
}'
EID=$(create_event "$E4")
if [ ! -z "$EID" ]; then
    add_perspective "$EID" '{"region":"Western Mainstream","summary":"Acknowledges growth (175.49T yuan/$24.45T processed in 2024, +43%) but emphasizes limitations: yuan only 3% of global SWIFT payments vs 48% for dollar. Notes CIPS still relies on SWIFT messaging for many transactions. Presents as regional system lacking global scale compared to SWIFT 11,500+ institutions in 235+ countries.","key_points":["175.49T yuan ($24.47T) processed in 2024, +42.6% YoY","176 direct participants, 1,514 indirect","Yuan only 3% of SWIFT payments vs 48% USD","SWIFT has 11,500+ institutions in 235+ countries","CIPS still uses SWIFT messaging for many transactions"],"language":"English"}'
    add_perspective "$EID" '{"region":"Chinese State/Academic","summary":"Testing ground narrative: PBOC Governor Pan Gongsheng called Africa partnerships key step in advancing economic ties. Emphasizes yuan stablecoin (AxCNH) in Kazakhstan, Shanghai Oil & Gas Exchange yuan pricing, and 40 bilateral settlement agreements. Views CIPS as parallel infrastructure, not SWIFT replacement - real alternative for global trade settlements operating alongside Western system.","key_points":["189 countries business coverage through 4,900+ banks","June 2025: First Africa/ME direct partnerships (6 institutions)","Transactions/value tripled since 2020","CAGR 2022-2024: 35% volume, 30% value","Parallel infrastructure strategy, not SWIFT replacement"],"language":"English/Chinese"}'
    add_perspective "$EID" '{"region":"African Perspective","summary":"Most enthusiastic adoption: Afreximbank and Standard Bank joining as direct participants signals continent-wide integration. African analysis emphasizes: (1) Western banks reducing Africa presence creating vacuum, (2) CIPS offering lower transaction costs than correspondent banking (remittances average 8.5% in sub-Saharan Africa - most expensive globally), (3) BRI loans often yuan-denominated making CIPS natural repayment channel. 53 of 54 African nations in BRI with CIPS access.","key_points":["Afreximbank & Standard Bank first African direct participants","Lower costs than correspondent banking (8.5% average remittance fees)","53 of 54 African countries in BRI","Western bank retreat created vacuum","Standard Bank launching CIPS for clients September 2025"],"language":"English"}'
fi
echo ""

# EVENT 5: EL SALVADOR BITCOIN
echo "Event 5: El Salvador Bitcoin Reversal..."
E5='{
  "title": "El Salvador Bitcoin Experiment Reversal: IMF-Mandated Rollback",
  "description": "El Salvador repealed Bitcoin as legal tender (January 30, 2025) to secure IMF $1.4B loan, making acceptance voluntary for private businesses and prohibiting use for taxes/government debts. Only 8.1% of Salvadorans used Bitcoin for payments (down from 25.7% first year), with 80% never using it. Remittances via crypto were 1.1% of $5.46B (Jan-Aug 2024), declining to 0.87% by December. IMF imposed continuous performance criteria with ceiling of 0 on new public sector Bitcoin acquisitions. Despite rollback, El Salvador purchased 12 more BTC in February 2025 (total 6,068+ BTC). Central African Republic parallel Bitcoin experiment (April 2022-2023) also failed with 85%+ lacking electricity and ~10% internet access.",
  "date": "2025-01-30T00:00:00",
  "region": "Latin America/Global",
  "impact_level": "medium"
}'
EID=$(create_event "$E5")
if [ ! -z "$EID" ]; then
    add_perspective "$EID" '{"region":"Western Mainstream","summary":"Near-universal framing as failed experiment: only 8.1% used Bitcoin, 80% never used it, 1% of remittances via crypto. IMF $1.4B loan conditional on removing Bitcoin as legal tender. Western economists emphasize volatility, lack of adoption, fiscal irresponsibility. Presents as cautionary tale against cryptocurrency hype and populist economic policies, with CAR parallel failure reinforcing narrative.","key_points":["January 30, 2025: Congress voted 55-2 to repeal legal tender status","Only 8.1% of Salvadorans used Bitcoin (down from 25.7% year 1)","1.1% of remittances via crypto (0.87% by Dec 2024)","IMF $1.4B loan conditional on rollback","Central African Republic also failed after 1 year (2022-2023)"],"language":"English"}'
    add_perspective "$EID" '{"region":"Chinese State/Academic","summary":"Limited coverage but frames as validation of China CBDC (digital yuan) approach: state-controlled, centralized digital currency vs decentralized cryptocurrency. Chinese analysis presents El Salvador case as proof that unregulated crypto cannot serve monetary policy functions. Reinforces China position that digital currencies must be sovereign-issued and controlled.","key_points":["Validates state-controlled CBDC approach","Demonstrates unregulated crypto unsuitability for monetary policy","China digital yuan model vindicated","Decentralized crypto lacks institutional backing","Sovereign control essential for currency function"],"language":"English/Chinese"}'
    add_perspective "$EID" '{"region":"Russian Perspective","summary":"Russian analysis sympathetic to anti-dollar intent but critical of execution. Russia exploring crypto for sanctions evasion but emphasizes need for state control. Views Bitcoin volatility as fatal flaw for reserve asset. Contrasts with Russia methodical gold accumulation and SPFS development as cautionary tale about rushing de-dollarization without proper infrastructure.","key_points":["Sympathetic to de-dollarization goal","Bitcoin volatility fatal for reserve assets","Russia prefers gold + state-controlled systems","Methodical infrastructure building vs rushed implementation","Crypto useful for sanctions evasion but not monetary policy"],"language":"English/Russian"}'
fi
echo ""

# EVENT 6: ISLAMIC FINANCE
echo "Event 6: Islamic Finance Growth..."
E6='{
  "title": "Islamic Finance Growth to $6 Trillion (Projected $9.7T by 2029)",
  "description": "Global Islamic finance assets reached $5.98T (end 2024) with LSEG/ICD projecting $9.7T by 2029 (10% CAGR). GCC holds ~50% of global assets ($2.5-2.7T in 2024, projected $5T+ by 2029). Iran leads with $2.24T, Saudi Arabia $1.31T, Malaysia $761B (these three = 72% of global). Sukuk market surpassed $1T outstanding with $250B issuance in 2024 (+16% YoY). Green/ESG sukuk reached $15.2B (+14% YoY), representing 6.1% of total sukuk. Nigeria, South Africa, Egypt issued $3.045B combined in 2024. Saudi Vision 2030 and UAE strategies explicitly prioritize Islamic finance, with UAE targeting AED 2.56T banking assets by 2031.",
  "date": "2024-12-31T00:00:00",
  "region": "Global/Middle East",
  "impact_level": "high"
}'
EID=$(create_event "$E6")
if [ ! -z "$EID" ]; then
    add_perspective "$EID" '{"region":"Western Mainstream","summary":"Generally overlooked or minimized in mainstream Western coverage despite $6T scale (larger than many G20 economies). When covered, presents as niche market or specialty finance. Acknowledges sukuk growth (+25.6% to $230.4B in 2024) but rarely contextualizes as parallel financial architecture operating at scale. Tends to emphasize exotic Shariah compliance requirements as barriers rather than features.","key_points":["$6T scale rarely contextualized in Western media","Treated as niche despite exceeding many G20 economies","Sukuk growth acknowledged but not systemic significance","Shariah compliance framed as exotic/complex","Parallel financial architecture aspect ignored"],"language":"English"}'
    add_perspective "$EID" '{"region":"Middle Eastern View - PRIMARY NARRATIVE","summary":"GCC holds 50% of global Islamic finance assets ($2.5-2.7T in 2024, projected $5T+ by 2029). Middle Eastern sources present not as alternative but as authentic system aligned with civilizational values. Saudi Vision 2030 and UAE strategies explicitly prioritize Islamic finance development. Recent: PIF second sukuk, Mubadala debut sukuk (March 2024), green sukuk $4B Q1 2024 (+17% YoY). Frames as moral capitalism surpassing Western system ethical failures (2008 financial crisis).","key_points":["GCC holds ~50% of $6T global assets","Projected $9.7T by 2029 (10% CAGR)","Iran $2.24T, Saudi $1.31T, Malaysia $761B = 72% global","Sukuk market >$1T outstanding, $250B issuance 2024","UAE targeting AED 2.56T banking assets by 2031"],"language":"English/Arabic"}'
    add_perspective "$EID" '{"region":"African Perspective","summary":"Growing African interest, particularly Muslim-majority North/West Africa. African sources emphasize ethics-based approach and profit-loss sharing as potentially more equitable than conventional banking. AfDB and African institutions issuing sukuk to tap Gulf liquidity. Nigeria, South Africa, Egypt issued $3.045B combined in 2024. Views as bridge to Gulf capital and alternative to Western institutions reducing Africa exposure, though capacity constraints and regulatory frameworks lag.","key_points":["Nigeria, South Africa, Egypt: $3.045B sukuk 2024","Ethics-based approach seen as more equitable","Bridge to Gulf capital access","Alternative to Western banks retreating from Africa","Regulatory and capacity constraints remain"],"language":"English"}'
fi
echo ""

# EVENT 7: MILLIONAIRE MIGRATION
echo "Event 7: Millionaire Migration..."
E7='{
  "title": "Capital Flight to UAE/Singapore: 142,000 Millionaires Relocating in 2025",
  "description": "Record 142,000 HNWIs (liquid wealth $1M+) projected to relocate in 2025, up from 134,000 in 2024 - largest voluntary transfer of private capital in modern history per Henley & Partners. UAE leads with 9,800 millionaire inflow ($63B wealth), driven by Golden Visa, zero income/capital gains tax, political stability. Singapore expects 1,600 (down from 3,500 in 2024) due to raised Global Investor Programme (S$10M from S$2.5M) and high property prices. USA 7,500 inflow. UK sees largest outflow: -16,500 (double China -7,800). Dubai hosts 120 family offices managing $1.2T. Russian wealth fled to UAE post-sanctions: real estate doubled to $500M H1 2022, 96.4t gold imported, hundreds of companies created.",
  "date": "2025-01-01T00:00:00",
  "region": "Global",
  "impact_level": "high"
}'
EID=$(create_event "$E7")
if [ ! -z "$EID" ]; then
    add_perspective "$EID" '{"region":"Western Mainstream","summary":"Frames as wealth migration driven by personal tax optimization, political stability, business opportunities. Western coverage emphasizes brain drain from high-tax jurisdictions (UK, California, France) to UAE/Singapore. Generally presents as individual choices based on rational economic incentives. Acknowledges geopolitical instability factor but emphasizes personal financial motivations over systemic shifts.","key_points":["142,000 HNWIs relocating in 2025 (record high)","Tax optimization primary driver in Western framing","UK losing -16,500 (largest outflow)","High-tax jurisdictions losing to zero-tax havens","Individual rational choice over systemic interpretation"],"language":"English"}'
    add_perspective "$EID" '{"region":"Middle Eastern View - UAE TRIUMPHALIST","summary":"Leading destination reflects successful national strategy: zero taxes, political stability, luxury infrastructure, strategic location bridging East/West. UAE sources present as validation of diversification from oil economy. Dubai positioning as Switzerland of Middle East with strong rule of law, asset protection. Dubai International Financial Centre hosts 120 family offices managing $1.2T. Emphasizes emergence as alternative to London/New York/Hong Kong with optionality (access to both Western and non-Western systems).","key_points":["UAE attracting 9,800 millionaires in 2025 ($63B wealth)","Golden Visa, zero income/capital gains tax","DIFC: 120 family offices, $1.2T assets under management","Strategic location bridging East and West","Alternative to traditional financial centers"],"language":"English/Arabic"}'
    add_perspective "$EID" '{"region":"Russian Perspective","summary":"Russian oligarchs among those relocating to UAE/Dubai after sanctions. Russian analysis presents as adaptation to financial warfare - moving assets to jurisdictions less susceptible to Western sanctions. UAE refusal to sanction Russia makes it attractive safe haven. Russian sources frame as Western sanctions driving capital to non-Western financial centers, undermining Western financial influence. Real estate doubled to $500M H1 2022, 96.4t gold imported, hundreds of Russian companies created.","key_points":["UAE did not impose Russia sanctions","Russian real estate in Dubai doubled to $500M (H1 2022)","96.4 tonnes gold imported from Russia (2022)","Hundreds of Russian companies created since Feb 2022","UAE on FATF grey list 2022-2024 for money laundering"],"language":"English/Russian"}'
fi
echo ""

echo "========================================================================"
echo "✅ ALL EVENTS IMPORTED!"
echo "========================================================================"
echo "Successfully imported: $SUCCESS_COUNT events"
echo "Total events in database: $(curl -s "$API_BASE/events/" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))")"
echo ""
echo "🎉 View your research at: http://46.62.231.96:3000"
echo "========================================================================"
