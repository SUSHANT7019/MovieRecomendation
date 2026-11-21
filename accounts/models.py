from django.db import models
from django.contrib.auth.models import User


class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preferences')
    selected_genres = models.CharField(max_length=500, default='')  # comma-separated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s preferences"
    
    def get_genres_list(self):
        """Return selected genres as a list"""
        if not self.selected_genres:
            return []
        return [g.strip() for g in self.selected_genres.split(',') if g.strip()]
    
    def get_genres_set(self):
        """Return selected genres as a set for mathematical operations"""
        return set(self.get_genres_list())
    
    def set_genres_from_list(self, genres_list):
        """Set genres from a list"""
        self.selected_genres = ','.join(genres_list)
