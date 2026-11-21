from rest_framework import serializers
from .models import UserPreference, RecommendationHistory
from movies.serializers import GenreSerializer, MovieListSerializer
from movies.models import Genre


class UserPreferenceSerializer(serializers.ModelSerializer):
    """
    Serializer for UserPreference model.
    """
    preferred_genres = GenreSerializer(many=True, read_only=True)
    excluded_genres = GenreSerializer(many=True, read_only=True)
    preferred_genre_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        write_only=True,
        source='preferred_genres',
        required=False
    )
    excluded_genre_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        write_only=True,
        source='excluded_genres',
        required=False
    )

    class Meta:
        model = UserPreference
        fields = [
            'id', 'user', 'preferred_genres', 'excluded_genres',
            'preferred_genre_ids', 'excluded_genre_ids',
            'match_type', 'min_rating', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']


class RecommendationHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for RecommendationHistory model.
    """
    movie = MovieListSerializer(read_only=True)
    similarity_percentage = serializers.SerializerMethodField()

    class Meta:
        model = RecommendationHistory
        fields = [
            'id', 'user', 'movie', 'operation_used',
            'similarity_score', 'similarity_percentage',
            'matching_genres', 'explanation', 'created_at'
        ]
        read_only_fields = ['id', 'user', 'created_at']

    def get_similarity_percentage(self, obj):
        return round(float(obj.similarity_score) * 100, 1)


class RecommendationRequestSerializer(serializers.Serializer):
    """
    Serializer for recommendation request.
    """
    preferred_genre_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        allow_empty=True
    )
    excluded_genre_ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        allow_empty=True
    )
    match_type = serializers.ChoiceField(
        choices=['OR', 'AND'],
        default='OR',
        required=False
    )
    min_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        required=False
    )
    limit = serializers.IntegerField(
        default=20,
        min_value=1,
        max_value=100,
        required=False
    )
    save_history = serializers.BooleanField(
        default=True,
        required=False
    )


class RecommendationResponseSerializer(serializers.Serializer):
    """
    Serializer for recommendation response.
    """
    movie = MovieListSerializer()
    similarity_score = serializers.FloatField()
    similarity_percentage = serializers.FloatField()
    matching_genres = serializers.ListField(child=serializers.CharField())
    explanation = serializers.CharField()
    operation = serializers.CharField()
