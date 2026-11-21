from django.contrib import admin
from .models import UserPreference, RecommendationHistory


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    """
    Admin interface for UserPreference model.
    """
    list_display = ['user', 'match_type', 'min_rating', 'get_preferred_genres', 'updated_at']
    list_filter = ['match_type', 'min_rating']
    search_fields = ['user__username']
    filter_horizontal = ['preferred_genres', 'excluded_genres']
    ordering = ['-updated_at']
    
    def get_preferred_genres(self, obj):
        genres = obj.preferred_genres.all()[:5]
        return ', '.join([g.name for g in genres]) if genres else 'None'
    get_preferred_genres.short_description = 'Preferred Genres'


@admin.register(RecommendationHistory)
class RecommendationHistoryAdmin(admin.ModelAdmin):
    """
    Admin interface for RecommendationHistory model.
    """
    list_display = ['user', 'movie', 'operation_used', 'similarity_score', 'created_at']
    list_filter = ['operation_used', 'created_at']
    search_fields = ['user__username', 'movie__title']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
