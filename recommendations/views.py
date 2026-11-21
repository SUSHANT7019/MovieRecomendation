from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Favorite, RecommendationHistory
from movies.models import Movie
from accounts.models import UserPreference
from .engine import get_recommendations, calculate_math_lab_operations
import json


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
    
    try:
        favorite = Favorite.objects.get(user=request.user, movie=movie)
        favorite.delete()
        messages.success(request, f'{movie.title} removed from favorites.')
    except Favorite.DoesNotExist:
        messages.error(request, 'Movie not in favorites.')
    
    # Redirect back to the referring page
    return redirect(request.META.get('HTTP_REFERER', 'movie_explorer'))


def math_lab_view(request):
    """Interactive Set Theory mathematics lab"""
    result = None
    
    if request.method == 'POST':
        set_a_input = request.POST.get('set_a', '').strip()
        set_b_input = request.POST.get('set_b', '').strip()
        
        # Parse inputs (comma-separated)
        set_a_list = [item.strip() for item in set_a_input.split(',') if item.strip()]
        set_b_list = [item.strip() for item in set_b_input.split(',') if item.strip()]
        
        if set_a_list or set_b_list:
            result = calculate_math_lab_operations(set_a_list, set_b_list)
            result['set_a_input'] = set_a_input
            result['set_b_input'] = set_b_input
    
    return render(request, 'recommendations/math_lab.html', {'result': result})


def math_lab_api_view(request):
    """API endpoint for Math Lab calculations (AJAX)"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            set_a_list = data.get('set_a', [])
            set_b_list = data.get('set_b', [])
            
            result = calculate_math_lab_operations(set_a_list, set_b_list)
            
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def landing_view(request):
    """Landing page"""
    # Get some featured movies
    featured_movies = Movie.objects.all().order_by('-rating')[:6]
    
    context = {
        'featured_movies': featured_movies,
    }
    
    return render(request, 'landing.html', context)
