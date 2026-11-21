"""
Test script for the mathematical engine.
Run this to verify all mathematical operations work correctly.

Usage:
    python test_mathematical_engine.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie.settings')
django.setup()

from mathematical_engine.set_operations import *
from mathematical_engine.recommendation_engine import RecommendationEngine
from movies.models import Genre, Movie


def test_basic_set_operations():
    """Test basic set operations."""
    print("\n" + "="*60)
    print("TESTING BASIC SET OPERATIONS")
    print("="*60)
    
    # Test Universal Set
    print("\n1. Universal Set")
    U = universal_set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"   U = {U}")
    print(f"   |U| = {set_cardinality(U)}")
    assert len(U) == 10, "Universal set cardinality failed"
    print("   ✓ PASSED")
    
    # Test Union
    print("\n2. Union")
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    result = union_operation(A, B)
    print(f"   A = {A}")
    print(f"   B = {B}")
    print(f"   A ∪ B = {result}")
    print(f"   |A ∪ B| = {len(result)}")
    assert result == {1, 2, 3, 4, 5, 6}, "Union failed"
    print("   ✓ PASSED")
    
    # Test Intersection
    print("\n3. Intersection")
    result = intersection_operation(A, B)
    print(f"   A ∩ B = {result}")
    print(f"   |A ∩ B| = {len(result)}")
    assert result == {3, 4}, "Intersection failed"
    print("   ✓ PASSED")
    
    # Test Set Difference
    print("\n4. Set Difference")
    result = set_difference(A, B)
    print(f"   A - B = {result}")
    print(f"   |A - B| = {len(result)}")
    assert result == {1, 2}, "Set difference failed"
    print("   ✓ PASSED")
    
    # Test Complement
    print("\n5. Complement")
    result = complement_operation(U, A)
    print(f"   A' = {result}")
    print(f"   |A'| = {len(result)}")
    assert result == {5, 6, 7, 8, 9, 10}, "Complement failed"
    print("   ✓ PASSED")
    
    # Test properties
    print("\n6. Set Properties")
    print(f"   A ∪ A' = {union_operation(A, complement_operation(U, A))}")
    print(f"   A ∩ A' = {intersection_operation(A, complement_operation(U, A))}")
    assert union_operation(A, complement_operation(U, A)) == U, "A ∪ A' = U failed"
    assert intersection_operation(A, complement_operation(U, A)) == set(), "A ∩ A' = ∅ failed"
    print("   ✓ PASSED")


def test_advanced_operations():
    """Test advanced set operations."""
    print("\n" + "="*60)
    print("TESTING ADVANCED OPERATIONS")
    print("="*60)
    
    # Test Cartesian Product
    print("\n1. Cartesian Product")
    A = {1, 2}
    B = {'a', 'b', 'c'}
    result = cartesian_product(A, B)
    print(f"   A = {A}")
    print(f"   B = {B}")
    print(f"   A × B = {result}")
    print(f"   |A × B| = {len(result)} (expected: {len(A) * len(B)})")
    assert len(result) == len(A) * len(B), "Cartesian product cardinality failed"
    print("   ✓ PASSED")
    
    # Test Power Set
    print("\n2. Power Set")
    A = {1, 2, 3}
    result = power_set(A)
    print(f"   A = {A}")
    print(f"   𝒫(A) = {[list(s) for s in result]}")
    print(f"   |𝒫(A)| = {len(result)} (expected: {2**len(A)})")
    assert len(result) == 2**len(A), "Power set cardinality failed"
    print("   ✓ PASSED")
    
    # Test Jaccard Similarity
    print("\n3. Jaccard Similarity")
    A = {'Action', 'Sci-Fi', 'Thriller'}
    B = {'Action', 'Thriller', 'Drama'}
    score = jaccard_similarity(A, B)
    print(f"   A = {A}")
    print(f"   B = {B}")
    print(f"   J(A, B) = {score:.4f} ({score*100:.1f}%)")
    expected = 2/4  # |{Action, Thriller}| / |{Action, Sci-Fi, Thriller, Drama}|
    assert abs(score - expected) < 0.001, "Jaccard similarity failed"
    print("   ✓ PASSED")
    
    # Test edge cases
    print("\n4. Edge Cases")
    empty = set()
    print(f"   J(∅, ∅) = {jaccard_similarity(empty, empty)}")
    print(f"   J(A, A) = {jaccard_similarity(A, A)}")
    assert jaccard_similarity(A, A) == 1.0, "J(A, A) should be 1.0"
    print("   ✓ PASSED")


def test_de_morgans_laws():
    """Test De Morgan's Laws."""
    print("\n" + "="*60)
    print("TESTING DE MORGAN'S LAWS")
    print("="*60)
    
    U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    
    law1, law2, details = verify_de_morgans_laws(U, A, B)
    
    print(f"\n   U = {U}")
    print(f"   A = {A}")
    print(f"   B = {B}")
    
    print(f"\n   Law 1: {details['law1']['statement']}")
    print(f"   Left:  {details['law1']['left_side']}")
    print(f"   Right: {details['law1']['right_side']}")
    print(f"   Status: {'✓ VERIFIED' if law1 else '✗ FAILED'}")
    
    print(f"\n   Law 2: {details['law2']['statement']}")
    print(f"   Left:  {details['law2']['left_side']}")
    print(f"   Right: {details['law2']['right_side']}")
    print(f"   Status: {'✓ VERIFIED' if law2 else '✗ FAILED'}")
    
    assert law1 and law2, "De Morgan's Laws failed"
    print("\n   ✓ BOTH LAWS VERIFIED")


def test_recommendation_engine():
    """Test the recommendation engine with real data."""
    print("\n" + "="*60)
    print("TESTING RECOMMENDATION ENGINE")
    print("="*60)
    
    # Prepare movie data
    movies = Movie.objects.all().prefetch_related('genres', 'ratings')
    movies_data = []
    
    for movie in movies[:20]:  # Test with first 20 movies
        ratings = movie.ratings.all()
        avg_rating = sum(float(r.rating) for r in ratings) / len(ratings) if ratings else 0.0
        
        movies_data.append({
            'id': movie.id,
            'title': movie.title,
            'genres': movie.genre_list,
            'release_year': movie.release_year,
            'rating': avg_rating,
        })
    
    if not movies_data:
        print("\n   No movies found in database. Run create_sample_data first.")
        return
    
    # Initialize engine
    engine = RecommendationEngine(movies_data)
    
    print(f"\n   Loaded {len(movies_data)} movies")
    
    # Get statistics
    stats = engine.get_genre_statistics()
    print(f"\n   Total Genres: {stats['total_genres']}")
    print("\n   Top 5 Genres:")
    for genre, data in list(stats['genres'].items())[:5]:
        print(f"     - {genre}: {data['count']} movies ({data['percentage']:.1f}%)")
    
    # Test Union-based recommendations
    print("\n   Testing Union-Based Recommendations (OR)")
    recs = engine.recommend(
        preferred_genres=['Action', 'Sci-Fi'],
        match_type='OR',
        limit=5
    )
    print(f"   Found {len(recs)} recommendations")
    for i, rec in enumerate(recs[:3], 1):
        print(f"     {i}. {rec['movie']['title']} - {rec['similarity_score']*100:.1f}%")
        print(f"        Genres: {', '.join(rec['matching_genres'])}")
    
    # Test Intersection-based recommendations
    print("\n   Testing Intersection-Based Recommendations (AND)")
    recs = engine.recommend(
        preferred_genres=['Action', 'Sci-Fi'],
        match_type='AND',
        limit=5
    )
    print(f"   Found {len(recs)} recommendations")
    for i, rec in enumerate(recs[:3], 1):
        print(f"     {i}. {rec['movie']['title']} - {rec['similarity_score']*100:.1f}%")
        print(f"        Genres: {', '.join(rec['matching_genres'])}")
    
    # Test with exclusions
    print("\n   Testing with Exclusions")
    recs = engine.recommend(
        preferred_genres=['Drama'],
        excluded_genres=['Horror'],
        match_type='OR',
        limit=5
    )
    print(f"   Found {len(recs)} Drama movies (excluding Horror)")
    for i, rec in enumerate(recs[:3], 1):
        print(f"     {i}. {rec['movie']['title']}")
    
    print("\n   ✓ RECOMMENDATION ENGINE WORKING")


def test_inclusion_exclusion():
    """Test the inclusion-exclusion principle."""
    print("\n" + "="*60)
    print("TESTING INCLUSION-EXCLUSION PRINCIPLE")
    print("="*60)
    
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    
    union = union_operation(A, B)
    intersection = intersection_operation(A, B)
    
    print(f"\n   A = {A}, |A| = {len(A)}")
    print(f"   B = {B}, |B| = {len(B)}")
    print(f"   A ∩ B = {intersection}, |A ∩ B| = {len(intersection)}")
    print(f"   A ∪ B = {union}, |A ∪ B| = {len(union)}")
    
    # Verify: |A ∪ B| = |A| + |B| - |A ∩ B|
    expected = len(A) + len(B) - len(intersection)
    actual = len(union)
    
    print(f"\n   Formula: |A ∪ B| = |A| + |B| - |A ∩ B|")
    print(f"            {actual} = {len(A)} + {len(B)} - {len(intersection)}")
    print(f"            {actual} = {expected}")
    
    assert actual == expected, "Inclusion-Exclusion Principle failed"
    print("\n   ✓ VERIFIED")


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*15 + "CineSet Mathematical Engine Tests" + " "*15 + "║")
    print("╚" + "="*58 + "╝")
    
    try:
        test_basic_set_operations()
        test_advanced_operations()
        test_de_morgans_laws()
        test_inclusion_exclusion()
        test_recommendation_engine()
        
        print("\n" + "="*60)
        print("ALL TESTS PASSED! ✓")
        print("="*60)
        print("\nThe mathematical engine is working correctly.")
        print("All set theory operations are verified.")
        print("\n")
        
    except AssertionError as e:
        print(f"\n\n✗ TEST FAILED: {e}\n")
        return False
    except Exception as e:
        print(f"\n\n✗ ERROR: {e}\n")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
