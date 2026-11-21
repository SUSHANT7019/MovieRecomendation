from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from decimal import Decimal

from .models import UserPreference, RecommendationHistory
from movies.models import Genre, Movie
from .serializers import (
    UserPreferenceSerializer,
    RecommendationHistorySerializer,
    RecommendationRequestSerializer,
    RecommendationResponseSerializer
)
from mathematical_engine.recommendation_engine import RecommendationEngine
from mathematical_engine.set_operations import (
    jaccard_similarity,
    union_operation,
    intersection_operation,
    set_difference,
    complement_operation,
    cartesian_product,
    power_set,
    verify_de_morgans_laws,
    universal_set,
)


# ========== Template Views ==========

@login_required
def preferences_view(request):
    """User preferences page."""
    return render(request, 'recommendations/preferences.html')


@login_required
def recommendations_view(request):
    """Recommendations page."""
    return render(request, 'recommendations/recommendations.html')


@login_required
def history_view(request):
    """Recommendation history page."""
    return render(request, 'recommendations/history.html')


@login_required
def math_lab_view(request):
    """Mathematical Lab page."""
    return render(request, 'recommendations/math_lab.html')


# ========== API Views ==========

@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def user_preferences_api(request):
    """
    Get or update user preferences.
    GET /api/preferences/
    POST /api/preferences/
    PUT /api/preferences/
    """
    # Get or create user preference
    preference, created = UserPreference.objects.get_or_create(user=request.user)
    
    if request.method == 'GET':
        serializer = UserPreferenceSerializer(preference)
        return Response(serializer.data)
    
    elif request.method in ['POST', 'PUT']:
        serializer = UserPreferenceSerializer(preference, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_recommendations(request):
    """
    Generate movie recommendations based on user preferences.
    POST /api/recommendations/
    
    Request body:
    {
        "preferred_genre_ids": [1, 2, 3],
        "excluded_genre_ids": [4],
        "match_type": "OR",  // or "AND"
        "min_rating": 7.0,
        "limit": 20,
        "save_history": true
    }
    """
    # Validate request
    request_serializer = RecommendationRequestSerializer(data=request.data)
    if not request_serializer.is_valid():
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = request_serializer.validated_data
    
    # Get preferred genres
    preferred_genre_ids = data.get('preferred_genre_ids', [])
    excluded_genre_ids = data.get('excluded_genre_ids', [])
    match_type = data.get('match_type', 'OR')
    min_rating = float(data.get('min_rating', 0.0))
    limit = data.get('limit', 20)
    save_history = data.get('save_history', True)
    
    # If no preferences provided, get from user's saved preferences
    if not preferred_genre_ids:
        try:
            user_pref = UserPreference.objects.get(user=request.user)
            preferred_genre_ids = list(user_pref.preferred_genres.values_list('id', flat=True))
            if not excluded_genre_ids:
                excluded_genre_ids = list(user_pref.excluded_genres.values_list('id', flat=True))
            match_type = user_pref.match_type
            min_rating = float(user_pref.min_rating)
        except UserPreference.DoesNotExist:
            return Response({
                'error': 'No preferences found. Please set your preferences first.'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    if not preferred_genre_ids:
        return Response({
            'error': 'Please select at least one preferred genre.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Get genre names
    preferred_genres = Genre.objects.filter(id__in=preferred_genre_ids)
    excluded_genres = Genre.objects.filter(id__in=excluded_genre_ids)
    
    preferred_genre_names = [g.name for g in preferred_genres]
    excluded_genre_names = [g.name for g in excluded_genres]
    
    # Prepare movie data for recommendation engine
    movies = Movie.objects.all().prefetch_related('genres', 'ratings')
    movies_data = []
    
    for movie in movies:
        # Calculate average rating
        ratings = movie.ratings.all()
        if ratings.exists():
            avg_rating = sum(float(r.rating) for r in ratings) / len(ratings)
        else:
            avg_rating = 0.0
        
        movies_data.append({
            'id': movie.id,
            'title': movie.title,
            'genres': movie.genre_list,
            'release_year': movie.release_year,
            'rating': avg_rating,
            'poster_url': movie.poster_url,
        })
    
    # Initialize recommendation engine
    engine = RecommendationEngine(movies_data)
    
    # Generate recommendations
    recommendations = engine.recommend(
        preferred_genres=preferred_genre_names,
        match_type=match_type,
        excluded_genres=excluded_genre_names,
        min_rating=min_rating,
        limit=limit
    )
    
    # Format response
    results = []
    for rec in recommendations:
        movie_obj = Movie.objects.get(id=rec['movie']['id'])
        movie_data = {
            'id': movie_obj.id,
            'title': movie_obj.title,
            'release_year': movie_obj.release_year,
            'genres': list(movie_obj.genres.values_list('name', flat=True)),
            'poster_url': movie_obj.poster_url,
            'average_rating': rec['movie']['rating'],
        }
        
        result = {
            'movie': movie_data,
            'similarity_score': rec['similarity_score'],
            'similarity_percentage': round(rec['similarity_score'] * 100, 1),
            'matching_genres': rec['matching_genres'],
            'explanation': rec['explanation'],
            'operation': rec['operation'],
        }
        results.append(result)
        
        # Save to history
        if save_history:
            RecommendationHistory.objects.create(
                user=request.user,
                movie=movie_obj,
                operation_used=rec['operation'],
                similarity_score=Decimal(str(rec['similarity_score'])),
                matching_genres=rec['matching_genres'],
                explanation=rec['explanation']
            )
    
    return Response({
        'count': len(results),
        'preferred_genres': preferred_genre_names,
        'excluded_genres': excluded_genre_names,
        'match_type': match_type,
        'min_rating': min_rating,
        'recommendations': results
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommendation_history(request):
    """
    Get user's recommendation history.
    GET /api/recommendations/history/
    """
    history = RecommendationHistory.objects.filter(user=request.user).select_related('movie')
    limit = int(request.query_params.get('limit', 50))
    history = history[:limit]
    
    serializer = RecommendationHistorySerializer(history, many=True)
    return Response({
        'count': len(serializer.data),
        'results': serializer.data
    })


# ========== Mathematical Lab API Views ==========

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def math_operation_union(request):
    """
    Perform union operation on movie sets.
    POST /api/math/union/
    """
    genre_ids = request.data.get('genre_ids', [])
    
    if not genre_ids or len(genre_ids) < 2:
        return Response({
            'error': 'Please provide at least 2 genres'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    genres = Genre.objects.filter(id__in=genre_ids)
    
    # Build sets
    sets_data = []
    for genre in genres:
        movie_ids = set(genre.movies.values_list('id', flat=True))
        sets_data.append({
            'genre': genre.name,
            'movies': list(movie_ids),
            'cardinality': len(movie_ids)
        })
    
    # Compute union
    result_set = set()
    for data in sets_data:
        result_set = union_operation(result_set, set(data['movies']))
    
    result_movies = Movie.objects.filter(id__in=result_set)
    
    return Response({
        'operation': 'Union (∪)',
        'formula': ' ∪ '.join([d['genre'] for d in sets_data]),
        'input_sets': sets_data,
        'result': {
            'movie_ids': list(result_set),
            'movies': [{'id': m.id, 'title': m.title} for m in result_movies],
            'cardinality': len(result_set)
        }
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def math_operation_intersection(request):
    """
    Perform intersection operation on movie sets.
    POST /api/math/intersection/
    """
    genre_ids = request.data.get('genre_ids', [])
    
    if not genre_ids or len(genre_ids) < 2:
        return Response({
            'error': 'Please provide at least 2 genres'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    genres = Genre.objects.filter(id__in=genre_ids)
    
    # Build sets
    sets_data = []
    for genre in genres:
        movie_ids = set(genre.movies.values_list('id', flat=True))
        sets_data.append({
            'genre': genre.name,
            'movies': list(movie_ids),
            'cardinality': len(movie_ids)
        })
    
    # Compute intersection
    result_set = set(sets_data[0]['movies']) if sets_data else set()
    for data in sets_data[1:]:
        result_set = intersection_operation(result_set, set(data['movies']))
    
    result_movies = Movie.objects.filter(id__in=result_set)
    
    return Response({
        'operation': 'Intersection (∩)',
        'formula': ' ∩ '.join([d['genre'] for d in sets_data]),
        'input_sets': sets_data,
        'result': {
            'movie_ids': list(result_set),
            'movies': [{'id': m.id, 'title': m.title} for m in result_movies],
            'cardinality': len(result_set)
        }
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def math_operation_difference(request):
    """
    Perform set difference operation.
    POST /api/math/difference/
    """
    genre_a_id = request.data.get('genre_a_id')
    genre_b_id = request.data.get('genre_b_id')
    
    if not genre_a_id or not genre_b_id:
        return Response({
            'error': 'Please provide both genre_a_id and genre_b_id'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    genre_a = get_object_or_404(Genre, id=genre_a_id)
    genre_b = get_object_or_404(Genre, id=genre_b_id)
    
    set_a = set(genre_a.movies.values_list('id', flat=True))
    set_b = set(genre_b.movies.values_list('id', flat=True))
    
    result_set = set_difference(set_a, set_b)
    result_movies = Movie.objects.filter(id__in=result_set)
    
    return Response({
        'operation': 'Set Difference (−)',
        'formula': f'{genre_a.name} − {genre_b.name}',
        'set_a': {
            'genre': genre_a.name,
            'cardinality': len(set_a)
        },
        'set_b': {
            'genre': genre_b.name,
            'cardinality': len(set_b)
        },
        'result': {
            'movie_ids': list(result_set),
            'movies': [{'id': m.id, 'title': m.title} for m in result_movies],
            'cardinality': len(result_set),
            'explanation': f'Movies in {genre_a.name} but not in {genre_b.name}'
        }
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def math_operation_complement(request):
    """
    Perform complement operation.
    POST /api/math/complement/
    """
    genre_id = request.data.get('genre_id')
    
    if not genre_id:
        return Response({
            'error': 'Please provide genre_id'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    genre = get_object_or_404(Genre, id=genre_id)
    
    universal = set(Movie.objects.values_list('id', flat=True))
    genre_set = set(genre.movies.values_list('id', flat=True))
    
    result_set = complement_operation(universal, genre_set)
    result_movies = Movie.objects.filter(id__in=result_set)[:100]  # Limit for display
    
    return Response({
        'operation': 'Complement (′)',
        'formula': f'{genre.name}′',
        'universal_set': {
            'cardinality': len(universal)
        },
        'input_set': {
            'genre': genre.name,
            'cardinality': len(genre_set)
        },
        'result': {
            'movie_ids': list(result_set)[:100],
            'movies': [{'id': m.id, 'title': m.title} for m in result_movies],
            'cardinality': len(result_set),
            'explanation': f'All movies that are NOT {genre.name}'
        }
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def math_jaccard_similarity(request):
    """
    Calculate Jaccard similarity between two genre sets.
    POST /api/math/jaccard/
    """
    genre_a_id = request.data.get('genre_a_id')
    genre_b_id = request.data.get('genre_b_id')
    
    if not genre_a_id or not genre_b_id:
        return Response({
            'error': 'Please provide both genre_a_id and genre_b_id'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    genre_a = get_object_or_404(Genre, id=genre_a_id)
    genre_b = get_object_or_404(Genre, id=genre_b_id)
    
    set_a = set(genre_a.movies.values_list('id', flat=True))
    set_b = set(genre_b.movies.values_list('id', flat=True))
    
    score = jaccard_similarity(set_a, set_b)
    intersection = set_a & set_b
    union = set_a | set_b
    
    return Response({
        'operation': 'Jaccard Similarity',
        'formula': 'J(A, B) = |A ∩ B| / |A ∪ B|',
        'set_a': {
            'genre': genre_a.name,
            'cardinality': len(set_a)
        },
        'set_b': {
            'genre': genre_b.name,
            'cardinality': len(set_b)
        },
        'intersection': {
            'cardinality': len(intersection)
        },
        'union': {
            'cardinality': len(union)
        },
        'similarity_score': score,
        'similarity_percentage': round(score * 100, 2),
        'explanation': f'The similarity between {genre_a.name} and {genre_b.name} is {round(score * 100, 1)}%'
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def math_cartesian_product(request):
    """
    Demonstrate Cartesian product.
    POST /api/math/cartesian-product/
    """
    genre_a_id = request.data.get('genre_a_id')
    genre_b_id = request.data.get('genre_b_id')
    limit = int(request.data.get('limit', 20))
    
    if not genre_a_id or not genre_b_id:
        return Response({
            'error': 'Please provide both genre_a_id and genre_b_id'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    genre_a = get_object_or_404(Genre, id=genre_a_id)
    genre_b = get_object_or_404(Genre, id=genre_b_id)
    
    set_a = set(genre_a.movies.values_list('id', flat=True))
    set_b = set(genre_b.movies.values_list('id', flat=True))
    
    result = cartesian_product(set_a, set_b, limit=limit)
    total_size = len(set_a) * len(set_b)
    
    return Response({
        'operation': 'Cartesian Product (×)',
        'formula': f'{genre_a.name} × {genre_b.name}',
        'set_a': {
            'genre': genre_a.name,
            'cardinality': len(set_a)
        },
        'set_b': {
            'genre': genre_b.name,
            'cardinality': len(set_b)
        },
        'result': {
            'pairs': [[a, b] for a, b in result],
            'displayed_count': len(result),
            'total_cardinality': total_size,
            'formula_check': f'|A × B| = |A| × |B| = {len(set_a)} × {len(set_b)} = {total_size}'
        }
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def math_power_set(request):
    """
    Generate power set of a genre.
    POST /api/math/power-set/
    """
    genre_id = request.data.get('genre_id')
    limit = int(request.data.get('limit', 20))
    
    if not genre_id:
        return Response({
            'error': 'Please provide genre_id'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    genre = get_object_or_404(Genre, id=genre_id)
    genre_set = set(genre.movies.values_list('id', flat=True)[:10])  # Limit input to prevent explosion
    
    result = power_set(genre_set, limit=limit)
    total_size = 2 ** len(genre_set)
    
    return Response({
        'operation': 'Power Set (𝒫)',
        'formula': f'𝒫({genre.name})',
        'input_set': {
            'genre': genre.name,
            'cardinality': len(genre_set)
        },
        'result': {
            'subsets': [list(s) for s in result],
            'displayed_count': len(result),
            'total_cardinality': total_size,
            'formula_check': f'|𝒫(A)| = 2^|A| = 2^{len(genre_set)} = {total_size}'
        },
        'warning': 'Power sets grow exponentially. Only showing first {} subsets.'.format(limit) if total_size > limit else None
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def math_verify_de_morgan(request):
    """
    Verify De Morgan's laws.
    POST /api/math/verify-de-morgan/
    """
    genre_a_id = request.data.get('genre_a_id')
    genre_b_id = request.data.get('genre_b_id')
    
    if not genre_a_id or not genre_b_id:
        return Response({
            'error': 'Please provide both genre_a_id and genre_b_id'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    genre_a = get_object_or_404(Genre, id=genre_a_id)
    genre_b = get_object_or_404(Genre, id=genre_b_id)
    
    universal = set(Movie.objects.values_list('id', flat=True))
    set_a = set(genre_a.movies.values_list('id', flat=True))
    set_b = set(genre_b.movies.values_list('id', flat=True))
    
    law1, law2, details = verify_de_morgans_laws(universal, set_a, set_b)
    
    return Response({
        'operation': "De Morgan's Laws Verification",
        'universal_set_cardinality': len(universal),
        'set_a': {
            'genre': genre_a.name,
            'cardinality': len(set_a)
        },
        'set_b': {
            'genre': genre_b.name,
            'cardinality': len(set_b)
        },
        'law1': {
            'statement': "(A ∪ B)' = A' ∩ B'",
            'holds': law1,
            'left_cardinality': len(details['law1']['left_side']),
            'right_cardinality': len(details['law1']['right_side'])
        },
        'law2': {
            'statement': "(A ∩ B)' = A' ∪ B'",
            'holds': law2,
            'left_cardinality': len(details['law2']['left_side']),
            'right_cardinality': len(details['law2']['right_side'])
        },
        'both_laws_verified': law1 and law2
    })
