from django.contrib import admin
from .models import Genre, Movie, MovieRating


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Admin interface for Genre model.
    """
    list_display = ['name', 'movie_count', 'created_at']
    search_fields = ['name']
    ordering = ['name']
    
    def movie_count(self, obj):
        return obj.movies.count()
    movie_count.short_description = 'Number of Movies'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    Admin interface for Movie model.
    """
    list_display = ['title', 'release_year', 'get_genres', 'created_at']
    list_filter = ['release_year', 'genres']
    search_fields = ['title', 'imdb_id', 'tmdb_id']
    filter_horizontal = ['genres']
    ordering = ['-release_year', 'title']
    
    def get_genres(self, obj):
        return ', '.join([g.name for g in obj.genres.all()[:3]])
    get_genres.short_description = 'Genres'


@admin.register(MovieRating)
class MovieRatingAdmin(admin.ModelAdmin):
    """
    Admin interface for MovieRating model.
    """
    list_display = ['movie', 'source', 'rating', 'vote_count', 'created_at']
    list_filter = ['source', 'rating']
    search_fields = ['movie__title']
    ordering = ['-rating']
