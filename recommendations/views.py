from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Favorite, RecommendationHistory
from movies.models import Movie
from accounts.models import UserPreference
from .engine import get_recommendations


@login_required
def recommendations_view(request):
    """Display personalized movie recommendations"""
    # Check if user has preferences
    try:
        preferences = UserPreference.objects.get(user=request.user)
        if not preferences.selected_genres:
            messages.warning(request, 'Please select your genre preferences first.')
            return redirect('preferences')
    except UserPreference.DoesNotExist:
        messages.warning(request, 'Please select your genre preferences first.')
        return redirect('preferences')
    
    # Get recommendations
    exclude_favorites = request.GET.get('exclude_favorites') == 'true'
    recommendations = get_recommendations(request.user, exclude_favorites=exclude_favorites)
    
    # Save top recommendations to history
    for rec in recommendations[:10]:  # Save top 10
        RecommendationHistory.objects.update_or_create(
            user=request.user,
            movie=rec['movie'],
            defaults={
                'similarity_score': rec['similarity_score'],
                'matching_genres': ','.join(rec['matching_genres']),
            }
        )
    
    context = {
        'recommendations': recommendations,
        'preferences': preferences,
        'exclude_favorites': exclude_favorites,
    }
    
    return render(request, 'recommendations/results.html', context)


@login_required
def dashboard_view(request):
    """User dashboard"""
    # Get statistics
    total_movies = Movie.objects.count()
    favorites_count = Favorite.objects.filter(user=request.user).count()
    
    try:
        preferences = UserPreference.objects.get(user=request.user)
        selected_genres_count = len(preferences.get_genres_list())
    except UserPreference.DoesNotExist:
        preferences = None
        selected_genres_count = 0
    
    # Get recent recommendations
    recent_recommendations = RecommendationHistory.objects.filter(
        user=request.user
    ).select_related('movie').order_by('-created_at')[:5]
    
    # Get favorite movies
    favorite_movies = Favorite.objects.filter(
        user=request.user
    ).select_related('movie').order_by('-created_at')[:5]
    
    context = {
        'total_movies': total_movies,
        'favorites_count': favorites_count,
        'selected_genres_count': selected_genres_count,
        'preferences': preferences,
        'recent_recommendations': recent_recommendations,
        'favorite_movies': favorite_movies,
    }
    
    return render(request, 'recommendations/dashboard.html', context)


@login_required
@require_POST
def add_favorite_view(request, movie_id):
    """Add a movie to favorites"""
    movie = get_object_or_404(Movie, id=movie_id)
    
    favorite, created = Favorite.objects.get_or_create(user=request.user, movie=movie)
    
    # Check if AJAX request
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if is_ajax:
        return JsonResponse({
            'success': True,
            'action': 'added',
            'message': f'{movie.title} added to favorites!' if created else f'{movie.title} is already in your favorites.'
        })
    
    if created:
        messages.success(request, f'{movie.title} added to favorites!')
    else:
        messages.info(request, f'{movie.title} is already in your favorites.')
    
    # Redirect back to the referring page
    return redirect(request.META.get('HTTP_REFERER', 'movie_explorer'))


@login_required
@require_POST
def remove_favorite_view(request, movie_id):
    """Remove a movie from favorites"""
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Check if AJAX request
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    try:
        favorite = Favorite.objects.get(user=request.user, movie=movie)
        favorite.delete()
        success = True
        message = f'{movie.title} removed from favorites.'
    except Favorite.DoesNotExist:
        success = False
        message = 'Movie not in favorites.'
    
    if is_ajax:
        return JsonResponse({
            'success': success,
            'action': 'removed',
            'message': message
        })
    
    if success:
        messages.success(request, message)
    else:
        messages.error(request, message)
    
    # Redirect back to the referring page
    return redirect(request.META.get('HTTP_REFERER', 'movie_explorer'))


def landing_view(request):
    """Landing page"""
    # Get some featured movies
    featured_movies = Movie.objects.all().order_by('-rating')[:6]
    
    context = {
        'featured_movies': featured_movies,
    }
    
    return render(request, 'landing.html', context)
