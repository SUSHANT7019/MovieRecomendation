from django.contrib import admin
from .models import UserPreference


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'selected_genres', 'updated_at')
    search_fields = ('user__username', 'selected_genres')
    list_filter = ('updated_at',)
