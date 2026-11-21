from django.urls import path
from . import views

urlpatterns = [
    # Template views
    path('discovery/', views.movie_discovery, name='movie_discovery'),
    
    # API endpoints
    path('api/movies/', views.MovieListView.as_view(), name='api_movie_list'),
    path('api/movies/<int:pk>/', views.MovieDetailView.as_view(), name='api_movie_detail'),
    path('api/movies/search/', views.movie_search, name='api_movie_search'),
    path('api/genres/', views.GenreListView.as_view(), name='api_genre_list'),
    path('api/genres/statistics/', views.genre_statistics, name='api_genre_statistics'),
]
