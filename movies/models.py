from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster_url = models.URLField(max_length=500)
    release_year = models.IntegerField()
    genres = models.CharField(max_length=500)  # comma-separated
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    language = models.CharField(max_length=50, default='English')
    cast = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-rating', 'title']
    
    def __str__(self):
        return self.title
    
    def get_genres_list(self):
        """Return genres as a list"""
        return [g.strip() for g in self.genres.split(',') if g.strip()]
    
    def get_genres_set(self):
        """Return genres as a set for mathematical operations"""
        return set(self.get_genres_list())
