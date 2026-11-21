from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db.models import Q, Avg
from .models import Genre, Movie, MovieRating
from .serializers import (
    GenreSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieCreateSerializer
)


# ========== Template Views ==========

@login_required
def movie_discovery(request):
    """Movie discovery page."""
    return render(request, 'movies/discovery.html')


# ========== API Views ==========

class GenreListView(generics.ListAPIView):
    """
    API endpoint to list all genres.
    GET /api/genres/
    """
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieListView(generics.ListAPIView):
    """
    API endpoint to list and search movies.
    GET /api/movies/
    
    Query parameters:
    - search: Search in title
    - genre: Filter by genre ID (can be multiple)
    - year: Filter by release year
    - min_rating: Minimum average rating
    - ordering: Sort by field (title, release_year, -release_year)
    """
    serializer_class = MovieListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'release_year']
    ordering = ['-release_year', 'title']

    def get_queryset(self):
        queryset = Movie.objects.all().prefetch_related('genres', 'ratings')
        
        # Filter by genre
        genre_ids = self.request.query_params.getlist('genre')
        if genre_ids:
            for genre_id in genre_ids:
                queryset = queryset.filter(genres__id=genre_id)
        
        # Filter by year
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(release_year=year)
        
        # Filter by minimum rating
        min_rating = self.request.query_params.get('min_rating')
        if min_rating:
            # This is a simplified filter; for production, use annotations
            movie_ids = []
            for movie in queryset:
                ratings = movie.ratings.all()
                if ratings.exists():
                    avg = sum(r.rating for r in ratings) / len(ratings)
                    if avg >= float(min_rating):
                        movie_ids.append(movie.id)
            queryset = queryset.filter(id__in=movie_ids)
        
        return queryset.distinct()


class MovieDetailView(generics.RetrieveAPIView):
    """
    API endpoint to get movie details.
    GET /api/movies/{id}/
    """
    queryset = Movie.objects.all().prefetch_related('genres', 'ratings')
    serializer_class = MovieDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def movie_search(request):
    """
    Advanced movie search endpoint.
    GET /api/movies/search/
    
    Query parameters:
    - q: Search query
    - genres: Comma-separated genre IDs
    - min_year: Minimum release year
    - max_year: Maximum release year
    - min_rating: Minimum rating
    - limit: Number of results (default 20)
    """
    query = request.query_params.get('q', '')
    genre_ids = request.query_params.get('genres', '')
    min_year = request.query_params.get('min_year')
    max_year = request.query_params.get('max_year')
    min_rating = request.query_params.get('min_rating')
    limit = int(request.query_params.get('limit', 20))
    
    # Start with all movies
    queryset = Movie.objects.all().prefetch_related('genres', 'ratings')
    
    # Search by title
    if query:
        queryset = queryset.filter(title__icontains=query)
    
    # Filter by genres
    if genre_ids:
        genre_id_list = [int(gid) for gid in genre_ids.split(',') if gid.strip()]
        for gid in genre_id_list:
            queryset = queryset.filter(genres__id=gid)
    
    # Filter by year range
    if min_year:
        queryset = queryset.filter(release_year__gte=int(min_year))
    if max_year:
        queryset = queryset.filter(release_year__lte=int(max_year))
    
    # Filter by minimum rating (simplified)
    if min_rating:
        movie_ids = []
        for movie in queryset:
            ratings = movie.ratings.all()
            if ratings.exists():
                avg = sum(r.rating for r in ratings) / len(ratings)
                if avg >= float(min_rating):
                    movie_ids.append(movie.id)
        queryset = queryset.filter(id__in=movie_ids)
    
    # Apply limit
    queryset = queryset.distinct()[:limit]
    
    serializer = MovieListSerializer(queryset, many=True)
    return Response({
        'count': len(serializer.data),
        'results': serializer.data
    })


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def genre_statistics(request):
    """
    Get statistics about genres.
    GET /api/genres/statistics/
    """
    genres = Genre.objects.all()
    total_movies = Movie.objects.count()
    
    stats = []
    for genre in genres:
        movie_count = genre.movies.count()
        stats.append({
            'id': genre.id,
            'name': genre.name,
            'movie_count': movie_count,
            'percentage': round((movie_count / total_movies * 100), 2) if total_movies > 0 else 0
        })
    
    # Sort by movie count descending
    stats.sort(key=lambda x: x['movie_count'], reverse=True)
    
    return Response({
        'total_movies': total_movies,
        'total_genres': len(stats),
        'genres': stats
    })
