"""
CineSet Mathematical Engine
===========================
This module implements discrete mathematics concepts using Python sets
for movie recommendations.
"""

from .set_operations import *
from .recommendation_engine import *

__all__ = [
    'universal_set',
    'genre_subset',
    'union_operation',
    'intersection_operation',
    'set_difference',
    'complement_operation',
    'cartesian_product',
    'power_set',
    'jaccard_similarity',
    'verify_de_morgans_laws',
    'set_cardinality',
    'RecommendationEngine',
]
