#!/bin/bash
# Import remaining 6 events from Global Capital Flows 2025 research
# Event 1 (Saudi PIF) already added as ID 10

API_BASE="http://localhost:8000/api"
SUCCESS_COUNT=0
FAIL_COUNT=0

echo "========================================================================"
echo "IMPORTING GLOBAL CAPITAL FLOWS 2025 RESEARCH (Events 2-7)"
echo "========================================================================"
echo ""

# Function to create event and add perspectives
create_event() {
    local EVENT_JSON="$1"
    local TITLE=$(echo "$EVENT_JSON" | python3 -c "import sys, json; print(json.load(sys.stdin)['title'][:60])")

    echo "Creating: $TITLE..."
    RESPONSE=$(curl -s -X POST "$API_BASE/events/" -H "Content-Type: application/json" -d "$EVENT_JSON")
    EVENT_ID=$(echo "$RESPONSE" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('id', ''))" 2>/dev/null)

    if [ -z "$EVENT_ID" ]; then
        echo "  ❌ Failed"
        FAIL_COUNT=$((FAIL_COUNT + 1))
        return 1
    fi

    echo "  ✅ Created (ID: $EVENT_ID)"
    echo "$EVENT_ID"
}

add_perspective() {
    local EVENT_ID="$1"
    local PERSP_JSON="$2"
    local REGION=$(echo "$PERSP_JSON" | python3 -c "import sys, json; print(json.load(sys.stdin)['region'])")

    curl -s -X POST "$API_BASE/events/$EVENT_ID/perspectives" -H "Content-Type: application/json" -d "$PERSP_JSON" > /dev/null
    echo "    + $REGION"
}

# ============================================================================
# EVENT 2: CENTRAL BANK GOLD (3,220 tonnes in 3 years)
# ============================================================================

EVENT_2='{
  "title": "Central Bank Gold Accumulation: 1,000+ Tonnes Annually for Three Consecutive Years",
  "description": "Central banks purchased unprecedented quantities: 1,136t (2022), 1,037t (2023), 1,044.6t (2024) - totaling 3,220 tonnes over three years, double the 2010-2021 average of 473t annually. Poland (90t in 2024, 67t H1 2025), Turkey (75t in 2024), and India (73t) led purchases. China added 44t officially in 2024 but alternative estimates suggest 570t covertly. Russia 75M oz (~2,330t) gold reserves worth $229B (35% of reserves) offset ~33% of $322B frozen forex assets. 77% of central banks surveyed plan continued accumulation through 2026.",
  "date": "2024-12-31T00:00:00",
  "region": "Global",
  "impact_level": "critical"
}'

EVENT_ID=$(create_event "$EVENT_2")
if [ ! -z "$EVENT_ID" ]; then
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))

    add_perspective "$EVENT_ID" '{
      "region": "Western Mainstream",
      "summary": "Western analysis frames as safe haven demand driven by geopolitical uncertainty, inflation hedging, and portfolio diversification. World Gold Council reports emphasize purchases at double the 2010-2021 average. Generally treats as prudent monetary policy without deep geopolitical implications, highlighting Poland (67t H1 2025) and Turkey as leading buyers.",
      "key_points": ["3,220 tonnes purchased 2022-2024 (3x historical average)", "2022: 1,136t (record), 2023: 1,037t, 2024: 1,044.6t", "Framed as inflation hedge and geopolitical uncertainty response", "Poland leading with 67t in H1 2025 alone", "77% of central banks plan continued purchases"],
      "language": "English"
    }'

    add_perspective "$EVENT_ID" '{
      "region": "Chinese State/Academic",
      "summary": "PBOC officially added 44 tonnes in 2024, resuming purchases in November 2024. However, Goldman Sachs estimates actual purchases ~40t/month, with one analysis claiming 570t covertly purchased in 2024. Chinese academic sources frame as reserve diversification consistent with yuan internationalization strategy, viewing Western reporting with suspicion. Gold represents only ~5% of China reserves vs 15% global average, suggesting room for expansion.",
      "key_points": ["Official: 44t added in 2024, total 2,298.53t by Q2 2025", "Alternative estimates: 570t purchased covertly in 2024", "Goldman Sachs estimates ~40t/month actual purchases", "Gold only 5% of reserves vs 15% global average", "Consistent with yuan internationalization strategy"],
      "language": "English/Chinese"
    }'

    add_perspective "$EVENT_ID" '{
      "region": "Russian Perspective",
      "summary": "Most explicit narrative: directly frames as response to weaponization of dollar and Western sanctions. Russia accumulated 1,244 tonnes (40M oz) from 2014-2020 post-Crimea as prescient strategy. Gold reserves now worth $229B (34.4% of $650B total reserves), offsetting ~33% of $322B frozen assets. Gold appreciation of +$96B (+72%) since early 2022. Presents as essential financial sovereignty tool and insurance against economic warfare, with 2022 proving strategy correct.",
      "key_points": ["Russia holds 75M oz (~2,330t) worth $229B", "Represents 34-35% of Russia total reserves", "Accumulated 40M oz between 2014-2020 (post-Crimea)", "$322B forex frozen by Western sanctions (2022)", "Gold gains (+$96B) offset 33% of frozen asset losses"],
      "language": "English/Russian"
    }'

    add_perspective "$EVENT_ID" '{
      "region": "Indian Interpretation",
      "summary": "RBI gold holdings reached 800.78 tonnes (8% of reserves) by September 2023, adding 73t in 2024. Indian analysis presents as dual dynamic where official and consumer demand reinforce each other - cultural affinity meeting monetary policy. Frames gold accumulation as consistent with India 5,000-year gold culture while modernizing reserve management. Less explicitly geopolitical than Russian narrative, emphasizing prudent diversification.",
      "key_points": ["RBI holds 800.78t (8% of total reserves)", "Added 73 tonnes in 2024", "Cultural-institutional synthesis approach", "5,000-year gold cultural tradition", "Modernizing reserve management while honoring tradition"],
      "language": "English/Hindi"
    }'
fi

echo ""

# ============================================================================
# EVENT 3: BRICS PAYMENT SYSTEMS (90% local currency trade)
# ============================================================================

EVENT_3='{
  "title": "BRICS Payment Systems & De-Dollarization: 90% Intra-BRICS Local Currency Trade",
  "description": "Russia reported 90% of intra-BRICS trade now settled in local currencies (up from 65% two years prior), with China-Russia bilateral trade reaching 95% yuan/ruble settlement on $245B volume (2024 record). However, no unified BRICS Pay system exists - prototype demonstrated October 2024 but implementation delayed to 2030. Russia SPFS system has 550 organizations (150 from 16 countries), while China CIPS processed 175T yuan in 2024. Critically, India Foreign Minister Jaishankar explicitly stated India has never been for de-dollarization and no proposal for BRICS currency, pursuing separate rupee internationalization via RBI SRVA system. Reality: competing national systems (CIPS, SPFS, SRVA) with coordination of convenience, not integration.",
  "date": "2024-10-23T00:00:00",
  "region": "Global/BRICS",
  "impact_level": "high"
}'

EVENT_ID=$(create_event "$EVENT_3")
if [ ! -z "$EVENT_ID" ]; then
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))

    add_perspective "$EVENT_ID" '{
      "region": "Western Mainstream",
      "summary": "Skeptical framing: BRICS Pay not operational despite speculation, emphasizes 2030 target as unrealistic, questions feasibility given member rivalries. Notes dollar still commands 58% of global reserves. Treats as aspirational rhetoric with limited practical impact, emphasizing technical challenges and political divisions among BRICS members.",
      "key_points": ["BRICS Pay prototype shown October 2024 but not operational", "Implementation now targeted for 2030 (delayed)", "Dollar still 58% of global reserves", "Emphasizes member rivalries (India-China tensions)", "Technical challenges and coordination issues highlighted"],
      "language": "English"
    }'

    add_perspective "$EVENT_ID" '{
      "region": "Chinese State/Academic",
      "summary": "Incrementalist success narrative: emphasizes 95% of China-Russia trade now in yuan/rubles, CIPS processing 52T yuan ($7.2T) annually - 58% of China cross-border transactions. Frames BRICS Pay delays as pragmatic approach favoring bilateral systems over premature multilateral launch. Views Western skepticism as defensive reaction to losing financial infrastructure monopoly. CIPS growth (+42.6% in 2024) demonstrates systematic progress.",
      "key_points": ["95% of China-Russia trade ($245B) in yuan/rubles", "CIPS processed 175T yuan ($24.47T) in 2024, +42.6% YoY", "176 direct participants, 1,514 indirect, 189 countries coverage", "Bilateral systems preferred over premature multilateral", "Systematic infrastructure building vs rhetoric"],
      "language": "English/Chinese"
    }'

    add_perspective "$EVENT_ID" '{
      "region": "Russian Perspective",
      "summary": "SPFS now connects 550+ organizations including 150 from 16 foreign countries (expanded to 20 by Jan 2024). Russian analysis presents as successful sanctions circumvention - financial isolation transformed into opportunity for alternative system building. Views 90% local currency settlement as validation of strategy. Emphasizes BRICS expansion (now 47.9% of global population) as historic shift. Critical of Indian hesitation but pragmatic about separate national approaches.",
      "key_points": ["SPFS: 550 organizations, 150 non-residents from 16-20 countries", "90% intra-BRICS local currency settlement (Putin statement)", "95% China-Russia bilateral trade in yuan/rubles", "Sanctions circumvention successful", "EU banned SPFS June 2024, US OFAC warned institutions Nov 2024"],
      "language": "English/Russian"
    }'

    add_perspective "$EVENT_ID" '{
      "region": "Indian Interpretation - CRITICAL DIVERGENCE",
      "summary": "MOST AMBIVALENT NARRATIVE and directly contradicts BRICS unity framing. Foreign Minister Jaishankar (December 2024): India has never been for de-dollarization and no proposal for BRICS currency. India pursuing bilateral rupee internationalization via RBI SRVA (Special Rupee Vostro Account) expansion instead of multilateral BRICS system. Views unified system as potential Chinese dominance; prefers Indian-controlled alternatives. US is India largest trade partner with no interest in weakening dollar.",
      "key_points": ["Jaishankar: India has never been for de-dollarization", "No proposal for BRICS currency - explicit rejection", "RBI SRVA expansion for bilateral rupee settlements", "US is India largest trade partner", "Fears Chinese dominance in unified BRICS system"],
      "language": "English/Hindi"
    }'
fi

echo ""

# Continue with remaining events...
echo "✅ Batch 1 complete (Events 2-3). Adding remaining events..."
echo ""

# I'll continue this in the next part to avoid hitting context limits

# Summary
echo ""
echo "========================================================================"
echo "IMPORT SUMMARY"
echo "========================================================================"
echo "Successfully imported: $SUCCESS_COUNT events"
echo "Failed: $FAIL_COUNT events"
echo "Total events in database: $(curl -s "$API_BASE/events/" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))")"
echo ""
echo "View at: http://46.62.231.96:3000"
echo "========================================================================"
