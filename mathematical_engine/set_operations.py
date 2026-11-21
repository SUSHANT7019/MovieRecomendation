"""
Set Operations Module
=====================
Implements fundamental discrete mathematics set operations for CineSet.

All operations use Python's built-in set data structure, which provides
optimal performance for set-theoretic operations.
"""

from typing import Set, List, Tuple, Any
from itertools import combinations, product


def universal_set(elements: List[Any]) -> Set[Any]:
    """
    Create a universal set U from a list of elements.
    
    Mathematical Definition:
    U = {x | x is an element in the domain}
    
    Args:
        elements: List of elements (movies, genres, etc.)
    
    Returns:
        Set containing all unique elements
    
    Example:
        >>> movies = [1, 2, 3, 4, 5]
        >>> U = universal_set(movies)
        >>> print(U)
        {1, 2, 3, 4, 5}
    """
    return set(elements)


def genre_subset(universal: Set[Any], predicate) -> Set[Any]:
    """
    Create a subset based on a predicate function.
    
    Mathematical Definition:
    A = {x ∈ U | predicate(x) is True}
    
    Args:
        universal: Universal set
        predicate: Function that returns True/False for each element
    
    Returns:
        Subset of elements satisfying the predicate
    
    Example:
        >>> U = {1, 2, 3, 4, 5, 6}
        >>> evens = genre_subset(U, lambda x: x % 2 == 0)
        >>> print(evens)
        {2, 4, 6}
    """
    return {x for x in universal if predicate(x)}


def union_operation(set_a: Set[Any], set_b: Set[Any]) -> Set[Any]:
    """
    Compute the union of two sets (OR operation).
    
    Mathematical Definition:
    A ∪ B = {x | x ∈ A or x ∈ B}
    
    Args:
        set_a: First set
        set_b: Second set
    
    Returns:
        Union of both sets
    
    Properties:
        - Commutative: A ∪ B = B ∪ A
        - Associative: (A ∪ B) ∪ C = A ∪ (B ∪ C)
        - Idempotent: A ∪ A = A
        - Identity: A ∪ ∅ = A
    
    Example:
        >>> action = {1, 2, 3}
        >>> comedy = {3, 4, 5}
        >>> result = union_operation(action, comedy)
        >>> print(result)
        {1, 2, 3, 4, 5}
    """
    return set_a | set_b


def multi_union(*sets: Set[Any]) -> Set[Any]:
    """
    Compute the union of multiple sets.
    
    Mathematical Definition:
    ⋃ᵢ Aᵢ = A₁ ∪ A₂ ∪ ... ∪ Aₙ
    
    Args:
        *sets: Variable number of sets
    
    Returns:
        Union of all sets
    """
    result = set()
    for s in sets:
        result |= s
    return result


def intersection_operation(set_a: Set[Any], set_b: Set[Any]) -> Set[Any]:
    """
    Compute the intersection of two sets (AND operation).
    
    Mathematical Definition:
    A ∩ B = {x | x ∈ A and x ∈ B}
    
    Args:
        set_a: First set
        set_b: Second set
    
    Returns:
        Intersection of both sets
    
    Properties:
        - Commutative: A ∩ B = B ∩ A
        - Associative: (A ∩ B) ∩ C = A ∩ (B ∩ C)
        - Idempotent: A ∩ A = A
        - Identity: A ∩ U = A
    
    Example:
        >>> action = {1, 2, 3}
        >>> comedy = {3, 4, 5}
        >>> result = intersection_operation(action, comedy)
        >>> print(result)
        {3}
    """
    return set_a & set_b


def multi_intersection(*sets: Set[Any]) -> Set[Any]:
    """
    Compute the intersection of multiple sets.
    
    Mathematical Definition:
    ⋂ᵢ Aᵢ = A₁ ∩ A₂ ∩ ... ∩ Aₙ
    
    Args:
        *sets: Variable number of sets
    
    Returns:
        Intersection of all sets, or empty set if no sets provided
    """
    if not sets:
        return set()
    result = sets[0].copy()
    for s in sets[1:]:
        result &= s
    return result


def set_difference(set_a: Set[Any], set_b: Set[Any]) -> Set[Any]:
    """
    Compute the set difference (relative complement).
    
    Mathematical Definition:
    A - B = A \\ B = {x | x ∈ A and x ∉ B}
    
    Args:
        set_a: Set to subtract from
        set_b: Set to subtract
    
    Returns:
        Elements in A but not in B
    
    Properties:
        - NOT commutative: A - B ≠ B - A (generally)
        - A - ∅ = A
        - A - A = ∅
        - A - B = A ∩ B'
    
    Example:
        >>> all_movies = {1, 2, 3, 4, 5}
        >>> horror = {4, 5}
        >>> result = set_difference(all_movies, horror)
        >>> print(result)
        {1, 2, 3}
    """
    return set_a - set_b


def complement_operation(universal: Set[Any], set_a: Set[Any]) -> Set[Any]:
    """
    Compute the complement of a set with respect to the universal set.
    
    Mathematical Definition:
    A' = Ā = U - A = {x ∈ U | x ∉ A}
    
    Args:
        universal: Universal set U
        set_a: Set to complement
    
    Returns:
        Elements in U but not in A
    
    Properties:
        - (A')' = A
        - A ∪ A' = U
        - A ∩ A' = ∅
        - ∅' = U
        - U' = ∅
    
    Example:
        >>> U = {1, 2, 3, 4, 5}
        >>> A = {1, 2}
        >>> result = complement_operation(U, A)
        >>> print(result)
        {3, 4, 5}
    """
    return universal - set_a


def cartesian_product(set_a: Set[Any], set_b: Set[Any], limit: int = 100) -> List[Tuple[Any, Any]]:
    """
    Compute the Cartesian product of two sets.
    
    Mathematical Definition:
    A × B = {(a, b) | a ∈ A and b ∈ B}
    
    Args:
        set_a: First set
        set_b: Second set
        limit: Maximum number of pairs to return (prevents memory issues)
    
    Returns:
        List of ordered pairs (tuples)
    
    Properties:
        - |A × B| = |A| × |B|
        - NOT commutative: A × B ≠ B × A (generally)
        - A × ∅ = ∅
    
    Example:
        >>> users = {1, 2}
        >>> movies = {'A', 'B', 'C'}
        >>> result = cartesian_product(users, movies)
        >>> print(result)
        [(1, 'A'), (1, 'B'), (1, 'C'), (2, 'A'), (2, 'B'), (2, 'C')]
    """
    result = list(product(set_a, set_b))
    return result[:limit]


def power_set(set_a: Set[Any], limit: int = 100) -> List[Set[Any]]:
    """
    Compute the power set (set of all subsets).
    
    Mathematical Definition:
    P(A) = 𝒫(A) = {S | S ⊆ A}
    
    Args:
        set_a: Input set
        limit: Maximum number of subsets to return
    
    Returns:
        List of all subsets
    
    Properties:
        - ∅ ∈ P(A)
        - A ∈ P(A)
        - |P(A)| = 2^|A|
    
    Example:
        >>> A = {1, 2, 3}
        >>> result = power_set(A)
        >>> print(result)
        [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
    """
    elements = list(set_a)
    n = len(elements)
    
    # Power set size is 2^n, which can be huge
    # Limit to prevent memory issues
    subsets = []
    for size in range(n + 1):
        for subset in combinations(elements, size):
            if len(subsets) >= limit:
                return subsets
            subsets.append(set(subset))
    
    return subsets


def jaccard_similarity(set_a: Set[Any], set_b: Set[Any]) -> float:
    """
    Compute Jaccard similarity coefficient between two sets.
    
    Mathematical Definition:
    J(A, B) = |A ∩ B| / |A ∪ B|
    
    Range: [0, 1]
    - 0: Completely disjoint sets
    - 1: Identical sets
    
    Args:
        set_a: First set
        set_b: Second set
    
    Returns:
        Jaccard similarity score (0.0 to 1.0)
    
    Properties:
        - J(A, A) = 1
        - J(A, B) = J(B, A) (symmetric)
        - J(A, ∅) = 0 if A ≠ ∅
        - J(∅, ∅) = 0 (by convention, to avoid division by zero)
    
    Example:
        >>> user_prefs = {'Action', 'Sci-Fi', 'Thriller'}
        >>> movie_genres = {'Action', 'Thriller', 'Drama'}
        >>> score = jaccard_similarity(user_prefs, movie_genres)
        >>> print(f"{score:.4f}")
        0.5000
    """
    union = set_a | set_b
    
    # Handle empty sets
    if len(union) == 0:
        return 0.0
    
    intersection = set_a & set_b
    return len(intersection) / len(union)


def set_cardinality(set_a: Set[Any]) -> int:
    """
    Compute the cardinality (size) of a set.
    
    Mathematical Definition:
    |A| = cardinality of set A
    
    Args:
        set_a: Input set
    
    Returns:
        Number of elements in the set
    
    Example:
        >>> A = {'Action', 'Comedy', 'Drama'}
        >>> print(set_cardinality(A))
        3
    """
    return len(set_a)


def verify_de_morgans_laws(
    universal: Set[Any],
    set_a: Set[Any],
    set_b: Set[Any]
) -> Tuple[bool, bool, dict]:
    """
    Verify De Morgan's Laws for given sets.
    
    De Morgan's Laws:
    1. (A ∪ B)' = A' ∩ B'
    2. (A ∩ B)' = A' ∪ B'
    
    Args:
        universal: Universal set U
        set_a: First set A
        set_b: Second set B
    
    Returns:
        Tuple of (law1_holds, law2_holds, details_dict)
    
    Example:
        >>> U = {1, 2, 3, 4, 5}
        >>> A = {1, 2}
        >>> B = {2, 3}
        >>> law1, law2, details = verify_de_morgans_laws(U, A, B)
        >>> print(f"Law 1: {law1}, Law 2: {law2}")
        Law 1: True, Law 2: True
    """
    # Compute complements
    a_complement = complement_operation(universal, set_a)
    b_complement = complement_operation(universal, set_b)
    
    # Law 1: (A ∪ B)' = A' ∩ B'
    union_ab = union_operation(set_a, set_b)
    left_side_1 = complement_operation(universal, union_ab)
    right_side_1 = intersection_operation(a_complement, b_complement)
    law1_holds = left_side_1 == right_side_1
    
    # Law 2: (A ∩ B)' = A' ∪ B'
    intersection_ab = intersection_operation(set_a, set_b)
    left_side_2 = complement_operation(universal, intersection_ab)
    right_side_2 = union_operation(a_complement, b_complement)
    law2_holds = left_side_2 == right_side_2
    
    details = {
        'law1': {
            'statement': "(A ∪ B)' = A' ∩ B'",
            'left_side': left_side_1,
            'right_side': right_side_1,
            'holds': law1_holds,
        },
        'law2': {
            'statement': "(A ∩ B)' = A' ∪ B'",
            'left_side': left_side_2,
            'right_side': right_side_2,
            'holds': law2_holds,
        },
        'sets': {
            'U': universal,
            'A': set_a,
            'B': set_b,
            "A'": a_complement,
            "B'": b_complement,
        }
    }
    
    return law1_holds, law2_holds, details


def symmetric_difference(set_a: Set[Any], set_b: Set[Any]) -> Set[Any]:
    """
    Compute the symmetric difference of two sets.
    
    Mathematical Definition:
    A Δ B = (A - B) ∪ (B - A) = (A ∪ B) - (A ∩ B)
    
    Args:
        set_a: First set
        set_b: Second set
    
    Returns:
        Elements in either A or B but not in both
    
    Properties:
        - Commutative: A Δ B = B Δ A
        - A Δ A = ∅
        - A Δ ∅ = A
    
    Example:
        >>> A = {1, 2, 3}
        >>> B = {3, 4, 5}
        >>> result = symmetric_difference(A, B)
        >>> print(result)
        {1, 2, 4, 5}
    """
    return set_a ^ set_b


def is_subset(set_a: Set[Any], set_b: Set[Any]) -> bool:
    """
    Check if set_a is a subset of set_b.
    
    Mathematical Definition:
    A ⊆ B ⟺ ∀x (x ∈ A → x ∈ B)
    
    Args:
        set_a: Potential subset
        set_b: Potential superset
    
    Returns:
        True if A ⊆ B, False otherwise
    
    Example:
        >>> A = {1, 2}
        >>> B = {1, 2, 3, 4}
        >>> print(is_subset(A, B))
        True
    """
    return set_a <= set_b


def is_proper_subset(set_a: Set[Any], set_b: Set[Any]) -> bool:
    """
    Check if set_a is a proper subset of set_b.
    
    Mathematical Definition:
    A ⊂ B ⟺ A ⊆ B and A ≠ B
    
    Args:
        set_a: Potential proper subset
        set_b: Potential superset
    
    Returns:
        True if A ⊂ B, False otherwise
    
    Example:
        >>> A = {1, 2}
        >>> B = {1, 2, 3, 4}
        >>> print(is_proper_subset(A, B))
        True
    """
    return set_a < set_b


def are_disjoint(set_a: Set[Any], set_b: Set[Any]) -> bool:
    """
    Check if two sets are disjoint (have no common elements).
    
    Mathematical Definition:
    A and B are disjoint ⟺ A ∩ B = ∅
    
    Args:
        set_a: First set
        set_b: Second set
    
    Returns:
        True if sets are disjoint, False otherwise
    
    Example:
        >>> A = {1, 2, 3}
        >>> B = {4, 5, 6}
        >>> print(are_disjoint(A, B))
        True
    """
    return set_a.isdisjoint(set_b)
