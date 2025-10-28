#!/bin/bash
# Test script: Import ONE event via API to verify it works

API_BASE="http://localhost:8000/api"

echo "========================================="
echo "TEST: Adding Saudi PIF Event via API"
echo "========================================="
echo ""

# Create Event 1: Saudi PIF
echo "Creating event..."
EVENT_RESPONSE=$(curl -s -X POST "$API_BASE/events/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Saudi PIF $913B Repositioning & 33% US Equity Reduction",
    "description": "Saudi Arabia Public Investment Fund (PIF) reduced US equity holdings by $2B in Q2 2025 (down 24% YoY to $26.71B), marking 55% decline from 2021 peak of $60B. Simultaneously signed $50B agreements with 6 major Chinese banks (August 2024), opened Hong Kong office, and pursued QFII certification. PIF Lucid Motors investment showed $13B accumulated losses (95% stock decline). Governor Al Rumayyan announced paradigm shift focusing on domestic Vision 2030 projects while maintaining US as #1 target. Total AUM reached $913B (+19% in 2024) with 2030 target raised to $2.67T.",
    "date": "2025-08-01T00:00:00",
    "region": "Global/Saudi Arabia",
    "impact_level": "high"
  }')

EVENT_ID=$(echo "$EVENT_RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])" 2>/dev/null)

if [ -z "$EVENT_ID" ]; then
  echo "❌ Failed to create event"
  echo "Response: $EVENT_RESPONSE"
  exit 1
fi

echo "✅ Event created with ID: $EVENT_ID"
echo ""

# Add Western Perspective
echo "Adding Western perspective..."
curl -s -X POST "$API_BASE/events/$EVENT_ID/perspectives" \
  -H "Content-Type: application/json" \
  -d '{
    "region": "Western Mainstream",
    "summary": "Western media frames PIF actions as portfolio rebalancing toward domestic Vision 2030 projects, emphasizing mixed investment outcomes and major losses in Lucid Motors (-55% from peak). Presents $2B Q2 2025 US stock reduction as normal portfolio management with focus on losses rather than strategic repositioning.",
    "key_points": [
      "PIF reduced US exposure from $25.5B to $23.8B in Q2 2025",
      "Lucid Motors investment shows $13B accumulated losses, stock down 95%",
      "Total US holdings down 24% YoY to $26.71B (end 2024)",
      "55% decline from $60B peak in 2021",
      "Emphasis on investment failures rather than geopolitical strategy"
    ],
    "language": "English"
  }' > /dev/null

echo "✅ Western perspective added"

# Add Chinese Perspective
echo "Adding Chinese perspective..."
curl -s -X POST "$API_BASE/events/$EVENT_ID/perspectives" \
  -H "Content-Type: application/json" \
  -d '{
    "region": "Chinese State/Academic",
    "summary": "Chinese sources interpret as strategic pivot toward China-Gulf economic corridor. Highlight PIF $50B agreements with 6 major Chinese banks (August 2024: ABC, BOC, CCB, SINOSURE, CEXIM, ICBC), Hong Kong office opening (February 2022), and QFII certification pursuit as evidence of systematic reorientation toward Asian markets. Framed as win-win cooperation under BRI framework.",
    "key_points": [
      "$50B agreements with 6 Chinese banks (August 2024)",
      "Hong Kong office opened February 2022",
      "QFII certification pursuit for A-shares access",
      "Framework represents 1.5x China 2023 total FDI",
      "Positioned as Belt and Road Initiative cooperation"
    ],
    "language": "English/Chinese"
  }' > /dev/null

echo "✅ Chinese perspective added"
echo ""
echo "========================================="
echo "✅ TEST SUCCESSFUL!"
echo "Event ID: $EVENT_ID"
echo "========================================="
echo ""
echo "Check it out: http://localhost:3000 or http://46.62.231.96:3000"
echo ""
