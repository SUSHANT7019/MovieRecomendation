from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'rating', 'language', 'genres')
    list_filter = ('release_year', 'language', 'rating')
    search_fields = ('title', 'description', 'genres')
    ordering = ('-rating', 'title')
