from django.db import models
from django.conf import settings
from movies.models import Genre, Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class UserPreference(models.Model):
    """
    Stores user's movie preferences for set-based recommendations.
    Preferred genres form the user's preference set.
    Excluded genres form the exclusion set.
    """
    MATCH_CHOICES = [
        ('OR', 'Match Any Genre (Union)'),
        ('AND', 'Match All Genres (Intersection)'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='preferences')
    preferred_genres = models.ManyToManyField(Genre, related_name='preferred_by', blank=True)
    excluded_genres = models.ManyToManyField(Genre, related_name='excluded_by', blank=True)
    match_type = models.CharField(max_length=3, choices=MATCH_CHOICES, default='OR')
    min_rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s preferences"

    @property
    def preferred_genre_names(self):
        """Returns set of preferred genre names."""
        return set(self.preferred_genres.values_list('name', flat=True))

    @property
    def excluded_genre_names(self):
        """Returns set of excluded genre names."""
        return set(self.excluded_genres.values_list('name', flat=True))

    class Meta:
        db_table = 'user_preferences'


class RecommendationHistory(models.Model):
    """
    Stores history of recommendations generated for users.
    Tracks which mathematical operations were used and their results.
    """
    OPERATION_CHOICES = [
        ('UNION', 'Union (OR matching)'),
        ('INTERSECTION', 'Intersection (AND matching)'),
        ('DIFFERENCE', 'Set Difference'),
        ('COMPLEMENT', 'Complement'),
        ('JACCARD', 'Jaccard Similarity'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recommendation_history')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='recommendations')
    operation_used = models.CharField(max_length=20, choices=OPERATION_CHOICES)
    similarity_score = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
    )
    matching_genres = models.JSONField(default=list)  # List of genres that matched
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.similarity_score})"

    class Meta:
        db_table = 'recommendation_history'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['user', '-similarity_score']),
        ]
