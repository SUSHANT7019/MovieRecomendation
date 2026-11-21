from django.contrib import admin
from .models import Favorite, RecommendationHistory


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'movie__title')


@admin.register(RecommendationHistory)
class RecommendationHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'similarity_score', 'created_at')
    list_filter = ('created_at', 'similarity_score')
    search_fields = ('user__username', 'movie__title')
