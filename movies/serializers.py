from rest_framework import serializers
from .models import Genre, Movie, MovieRating


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for Genre model.
    """
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['id', 'name', 'movie_count']
        read_only_fields = ['id']

    def get_movie_count(self, obj):
        return obj.movies.count()


class MovieRatingSerializer(serializers.ModelSerializer):
    """
    Serializer for MovieRating model.
    """
    class Meta:
        model = MovieRating
        fields = ['id', 'source', 'rating', 'vote_count']
        read_only_fields = ['id']


class MovieListSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie list view (lightweight).
    """
    genres = serializers.StringRelatedField(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'release_year', 'genres',
            'poster_url', 'average_rating'
        ]
        read_only_fields = ['id']

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            avg = sum(r.rating for r in ratings) / len(ratings)
            return round(float(avg), 1)
        return None


class MovieDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie detail view (comprehensive).
    """
    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        write_only=True,
        source='genres'
    )
    ratings = MovieRatingSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    genre_list = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'release_year', 'genres', 'genre_ids',
            'genre_list', 'poster_url', 'poster_image', 'tmdb_id',
            'imdb_id', 'overview', 'ratings', 'average_rating',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            avg = sum(r.rating for r in ratings) / len(ratings)
            return round(float(avg), 1)
        return None


class MovieCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating movies.
    """
    genre_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        source='genres'
    )

    class Meta:
        model = Movie
        fields = [
            'title', 'release_year', 'genre_ids', 'poster_url',
            'tmdb_id', 'imdb_id', 'overview'
        ]
