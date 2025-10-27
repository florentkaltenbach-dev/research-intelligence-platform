"""
Analysis tools for advanced intelligence features.
"""
from typing import List, Dict, Tuple, Set
from collections import Counter
import logging
import re

logger = logging.getLogger(__name__)


class PerspectiveAnalyzer:
    """Analyzes perspectives to find contradictions, consensus, and conflicts."""

    @staticmethod
    def extract_keywords(text: str) -> Set[str]:
        """
        Extract meaningful keywords from text.

        Args:
            text: Text to analyze

        Returns:
            Set of keywords
        """
        # Simple keyword extraction (could be enhanced with NLP)
        words = re.findall(r'\b[a-z]{4,}\b', text.lower())
        # Filter common stop words
        stop_words = {'that', 'this', 'with', 'from', 'have', 'will', 'would', 'could',
                      'should', 'about', 'their', 'there', 'were', 'been', 'which', 'when'}
        return set(w for w in words if w not in stop_words)

    @classmethod
    def find_contradictions(cls, perspectives: List[Dict]) -> List[Dict]:
        """
        Find contradictions between perspectives on the same event.

        Args:
            perspectives: List of perspective dictionaries

        Returns:
            List of contradiction objects
        """
        contradictions = []

        for i, p1 in enumerate(perspectives):
            for p2 in perspectives[i+1:]:
                # Extract key points
                points1 = set(p1.get('key_points', []))
                points2 = set(p2.get('key_points', []))

                # Look for opposing statements
                # (This is simplified - real implementation would use semantic analysis)
                for point1 in points1:
                    for point2 in points2:
                        # Check for negation patterns
                        if cls._are_contradictory(point1, point2):
                            contradictions.append({
                                'region1': p1['region'],
                                'region2': p2['region'],
                                'point1': point1,
                                'point2': point2,
                                'type': 'direct_contradiction'
                            })

        logger.info(f"Found {len(contradictions)} contradictions")
        return contradictions

    @staticmethod
    def _are_contradictory(text1: str, text2: str) -> bool:
        """
        Check if two statements are contradictory.

        This is a simplified heuristic. Real implementation would use NLP.
        """
        text1_lower = text1.lower()
        text2_lower = text2.lower()

        # Check for negation patterns
        negation_indicators = [
            ('support', 'oppose'),
            ('agree', 'disagree'),
            ('accept', 'reject'),
            ('increase', 'decrease'),
            ('strengthen', 'weaken'),
            ('expand', 'reduce'),
            ('peaceful', 'aggressive'),
            ('cooperation', 'confrontation'),
            ('benefit', 'harm'),
        ]

        for pos, neg in negation_indicators:
            if (pos in text1_lower and neg in text2_lower) or \
               (neg in text1_lower and pos in text2_lower):
                return True

        return False

    @classmethod
    def find_consensus(cls, perspectives: List[Dict]) -> List[Dict]:
        """
        Find points of agreement across perspectives.

        Args:
            perspectives: List of perspective dictionaries

        Returns:
            List of consensus objects
        """
        consensus_items = []

        # Extract all key points
        all_points = []
        for p in perspectives:
            points = p.get('key_points', [])
            for point in points:
                all_points.append({
                    'region': p['region'],
                    'point': point
                })

        # Find similar points across regions using keyword matching
        keyword_groups = {}
        for item in all_points:
            keywords = cls.extract_keywords(item['point'])
            key = tuple(sorted(keywords)[:3])  # Use top 3 keywords as key

            if key not in keyword_groups:
                keyword_groups[key] = []
            keyword_groups[key].append(item)

        # Consensus requires agreement from at least 2 different regions
        for keyword_tuple, items in keyword_groups.items():
            regions = set(item['region'] for item in items)
            if len(regions) >= 2:
                consensus_items.append({
                    'regions': list(regions),
                    'points': [item['point'] for item in items],
                    'agreement_level': len(regions) / len(perspectives) if perspectives else 0
                })

        logger.info(f"Found {len(consensus_items)} consensus items")
        return consensus_items

    @staticmethod
    def predict_conflict_zones(perspectives: List[Dict]) -> List[Dict]:
        """
        Identify areas where conflicting trajectories suggest future conflict.

        Args:
            perspectives: List of perspective dictionaries

        Returns:
            List of conflict prediction objects
        """
        predictions = []

        # Keywords that suggest escalation
        escalation_keywords = {
            'military', 'weapon', 'sanction', 'blockade', 'threaten', 'retaliate',
            'war', 'conflict', 'attack', 'defense', 'alliance', 'deterrence'
        }

        # Keywords that suggest de-escalation
        deescalation_keywords = {
            'negotiate', 'diplomacy', 'cooperation', 'agreement', 'peace', 'dialogue',
            'compromise', 'mediate', 'resolution', 'treaty'
        }

        # Analyze each perspective's trajectory
        region_trajectories = {}
        for p in perspectives:
            summary = p.get('summary', '')
            points = ' '.join(p.get('key_points', []))
            full_text = f"{summary} {points}".lower()

            escalation_count = sum(1 for kw in escalation_keywords if kw in full_text)
            deescalation_count = sum(1 for kw in deescalation_keywords if kw in full_text)

            region_trajectories[p['region']] = {
                'escalation_score': escalation_count,
                'deescalation_score': deescalation_count,
                'net_score': escalation_count - deescalation_count
            }

        # Find regions with opposing trajectories
        regions = list(region_trajectories.keys())
        for i, r1 in enumerate(regions):
            for r2 in regions[i+1:]:
                t1 = region_trajectories[r1]
                t2 = region_trajectories[r2]

                # If one is escalating and one is de-escalating, potential conflict
                if t1['net_score'] > 2 and t2['net_score'] > 2:
                    predictions.append({
                        'region1': r1,
                        'region2': r2,
                        'risk_level': min(t1['net_score'], t2['net_score']),
                        'type': 'mutual_escalation',
                        'description': f'Both {r1} and {r2} show escalatory trajectories'
                    })
                elif (t1['net_score'] > 2 and t2['net_score'] < -2) or \
                     (t1['net_score'] < -2 and t2['net_score'] > 2):
                    predictions.append({
                        'region1': r1,
                        'region2': r2,
                        'risk_level': abs(t1['net_score'] - t2['net_score']) / 2,
                        'type': 'asymmetric_trajectory',
                        'description': f'Opposing trajectories between {r1} and {r2}'
                    })

        logger.info(f"Identified {len(predictions)} potential conflict zones")
        return predictions

    @staticmethod
    def find_related_themes(event1: Dict, event2: Dict) -> Dict:
        """
        Analyze if two events share common themes or impacts.

        Args:
            event1: First event dictionary
            event2: Second event dictionary

        Returns:
            Relationship analysis
        """
        # Extract text from both events
        text1 = f"{event1.get('title', '')} {event1.get('description', '')}".lower()
        text2 = f"{event2.get('title', '')} {event2.get('description', '')}".lower()

        # Check for shared keywords
        keywords1 = PerspectiveAnalyzer.extract_keywords(text1)
        keywords2 = PerspectiveAnalyzer.extract_keywords(text2)
        shared_keywords = keywords1 & keywords2

        # Calculate similarity score
        if keywords1 and keywords2:
            similarity = len(shared_keywords) / min(len(keywords1), len(keywords2))
        else:
            similarity = 0

        # Check if same region
        same_region = event1.get('region') == event2.get('region')

        # Check if same impact level
        same_impact = event1.get('impact_level') == event2.get('impact_level')

        return {
            'similarity_score': similarity,
            'shared_keywords': list(shared_keywords),
            'same_region': same_region,
            'same_impact': same_impact,
            'is_related': similarity > 0.3 or same_region
        }
