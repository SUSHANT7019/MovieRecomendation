from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Movie
from recommendations.models import Favorite
from recommendations.engine import calculate_jaccard_similarity
from accounts.models import UserPreference


def movie_explorer_view(request):
    """Movie explorer with filtering and search"""
    movies = Movie.objects.all()
    
    # Get all unique genres for filter
    all_genres = set()
    for movie in Movie.objects.all():
        all_genres.update(movie.get_genres_list())
    all_genres = sorted(list(all_genres))
    
    # Get filter parameters
    search_query = request.GET.get('search', '').strip()
    genre_filter = request.GET.get('genre', '').strip()
    year_filter = request.GET.get('year', '').strip()
    rating_filter = request.GET.get('rating', '').strip()
    language_filter = request.GET.get('language', '').strip()
    
    # Apply filters
    if search_query:
        movies = movies.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    
    if genre_filter:
        movies = movies.filter(genres__icontains=genre_filter)
    
    if year_filter:
        try:
            movies = movies.filter(release_year=int(year_filter))
        except ValueError:
            pass
    
    if rating_filter:
        try:
            movies = movies.filter(rating__gte=float(rating_filter))
        except ValueError:
            pass
    
    if language_filter:
        movies = movies.filter(language__iexact=language_filter)
    
    # Get unique years and languages for filters
    years = Movie.objects.values_list('release_year', flat=True).distinct().order_by('-release_year')
    languages = Movie.objects.values_list('language', flat=True).distinct().order_by('language')
    
    # Get favorited movie IDs if user is authenticated
    favorited_ids = set()
    if request.user.is_authenticated:
        favorited_ids = set(Favorite.objects.filter(user=request.user).values_list('movie_id', flat=True))
    
    context = {
        'movies': movies,
        'all_genres': all_genres,
        'years': years,
        'languages': languages,
        'favorited_ids': favorited_ids,
        'search_query': search_query,
        'genre_filter': genre_filter,
        'year_filter': year_filter,
        'rating_filter': rating_filter,
        'language_filter': language_filter,
    }
    
    return render(request, 'movies/explorer.html', context)


def movie_detail_view(request, movie_id):
    """Movie detail page"""
    movie = get_object_or_404(Movie, id=movie_id)
    
    is_favorited = False
    user_similarity = None
    matching_genres = []
    user_preferences = None
    
    if request.user.is_authenticated:
        # Check if favorited
        is_favorited = Favorite.objects.filter(user=request.user, movie=movie).exists()
        
        # Calculate similarity if user has preferences
        try:
            user_preferences = UserPreference.objects.get(user=request.user)
            user_genres_set = user_preferences.get_genres_set()
            movie_genres_set = movie.get_genres_set()
            
            if user_genres_set:
                user_similarity = calculate_jaccard_similarity(user_genres_set, movie_genres_set)
                matching_genres = sorted(list(user_genres_set & movie_genres_set))
        except UserPreference.DoesNotExist:
            pass
    
    context = {
        'movie': movie,
        'is_favorited': is_favorited,
        'user_similarity': user_similarity,
        'matching_genres': matching_genres,
        'user_preferences': user_preferences,
    }
    
    return render(request, 'movies/detail.html', context)
