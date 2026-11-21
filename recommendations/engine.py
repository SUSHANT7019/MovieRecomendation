"""
Mathematical Movie Recommendation Engine using Set Theory
Implements Jaccard Similarity Coefficient
"""


def calculate_jaccard_similarity(user_genres_set, movie_genres_set):
    """
    Calculate Jaccard Similarity between two sets.
    
    Formula: J(P,M) = |P ∩ M| / |P ∪ M|
    
    Args:
        user_genres_set: Set of user's preferred genres
        movie_genres_set: Set of movie's genres
    
    Returns:
        Float between 0 and 100 representing similarity percentage
    """
    if not user_genres_set or not movie_genres_set:
        return 0.0
    
    intersection = user_genres_set & movie_genres_set
    union = user_genres_set | movie_genres_set
    
    if len(union) == 0:
        return 0.0
    
    jaccard_coefficient = len(intersection) / len(union)
    return round(jaccard_coefficient * 100, 2)


def get_set_operations(set_a, set_b):
    """
    Perform all set operations between two sets.
    
    Returns:
        dict with all set operations
    """
    return {
        'intersection': set_a & set_b,
        'union': set_a | set_b,
        'difference_a_b': set_a - set_b,
        'difference_b_a': set_b - set_a,
        'symmetric_difference': set_a ^ set_b,
    }


def get_recommendations(user, exclude_favorites=False, limit=None):
    """
    Get movie recommendations for a user based on their preferences.
    
    Args:
        user: Django User object
        exclude_favorites: Whether to exclude favorited movies
        limit: Maximum number of recommendations to return
    
    Returns:
        List of dicts containing movie and similarity information
    """
    from movies.models import Movie
    from accounts.models import UserPreference
    from recommendations.models import Favorite
    
    # Get user preferences
    try:
        preferences = UserPreference.objects.get(user=user)
        user_genres_set = preferences.get_genres_set()
    except UserPreference.DoesNotExist:
        return []
    
    if not user_genres_set:
        return []
    
    # Get all movies
    movies = Movie.objects.all()
    
    # Get favorited movie IDs if excluding
    favorited_ids = set()
    if exclude_favorites:
        favorited_ids = set(Favorite.objects.filter(user=user).values_list('movie_id', flat=True))
    
    recommendations = []
    
    for movie in movies:
        # Skip favorites if requested
        if exclude_favorites and movie.id in favorited_ids:
            continue
        
        movie_genres_set = movie.get_genres_set()
        
        # Calculate similarity
        similarity_score = calculate_jaccard_similarity(user_genres_set, movie_genres_set)
        
        # Get set operations
        intersection = user_genres_set & movie_genres_set
        union = user_genres_set | movie_genres_set
        missing_genres = user_genres_set - movie_genres_set
        extra_genres = movie_genres_set - user_genres_set
        
        recommendations.append({
            'movie': movie,
            'similarity_score': similarity_score,
            'matching_genres': sorted(list(intersection)),
            'all_genres': sorted(list(union)),
            'missing_genres': sorted(list(missing_genres)),
            'extra_genres': sorted(list(extra_genres)),
            'user_genres': sorted(list(user_genres_set)),
            'movie_genres': sorted(list(movie_genres_set)),
        })
    
    # Sort by similarity score (descending), then rating (descending), then title (ascending)
    recommendations.sort(key=lambda x: (-x['similarity_score'], -float(x['movie'].rating), x['movie'].title))
    
    if limit:
        recommendations = recommendations[:limit]
    
    return recommendations
