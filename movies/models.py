from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    """
    Represents a movie genre.
    Each genre forms a subset of the universal movie set.
    """
    name = models.CharField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genres'
        ordering = ['name']


class Movie(models.Model):
    """
    Represents a movie in the universal set.
    Each movie can belong to multiple genres (many-to-many relationship).
    """
    title = models.CharField(max_length=500, db_index=True)
    release_year = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1800), MaxValueValidator(2100)]
    )
    genres = models.ManyToManyField(Genre, related_name='movies')
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    poster_image = models.ImageField(upload_to='posters/', blank=True, null=True)
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)
    imdb_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    overview = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        year = f" ({self.release_year})" if self.release_year else ""
        return f"{self.title}{year}"

    @property
    def genre_list(self):
        """Returns a list of genre names for this movie."""
        return list(self.genres.values_list('name', flat=True))

    class Meta:
        db_table = 'movies'
        ordering = ['-release_year', 'title']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['release_year']),
        ]


class MovieRating(models.Model):
    """
    Stores movie ratings from various sources.
    Used for filtering recommendations by minimum rating.
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    source = models.CharField(max_length=50, default='user')  # 'user', 'imdb', 'tmdb', etc.
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )
    vote_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie.title} - {self.source}: {self.rating}"

    class Meta:
        db_table = 'movie_ratings'
        unique_together = ['movie', 'source']
        ordering = ['-rating']
