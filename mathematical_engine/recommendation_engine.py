"""
Recommendation Engine Module
============================
Uses set theory operations to generate movie recommendations.
"""

from typing import List, Dict, Set, Any, Tuple
from .set_operations import (
    jaccard_similarity,
    union_operation,
    intersection_operation,
    set_difference,
    multi_union,
    multi_intersection,
)


class RecommendationEngine:
    """
    Mathematical recommendation engine using set theory.
    
    This engine treats:
    - Movies as elements
    - Genres as sets
    - User preferences as sets
    - Recommendations as set operations
    """
    
    def __init__(self, movies_data: List[Dict[str, Any]]):
        """
        Initialize the recommendation engine with movie data.
        
        Args:
            movies_data: List of movie dictionaries with structure:
                {
                    'id': int,
                    'title': str,
                    'genres': List[str],
                    'release_year': int,
                    'rating': float
                }
        """
        self.movies = {movie['id']: movie for movie in movies_data}
        self.genre_to_movies = self._build_genre_index()
    
    def _build_genre_index(self) -> Dict[str, Set[int]]:
        """
        Build an inverted index: genre -> set of movie IDs.
        This enables efficient set operations.
        
        Returns:
            Dictionary mapping genre names to sets of movie IDs
        """
        index = {}
        for movie_id, movie in self.movies.items():
            for genre in movie.get('genres', []):
                if genre not in index:
                    index[genre] = set()
                index[genre].add(movie_id)
        return index
    
    def get_movies_by_genres_union(
        self,
        preferred_genres: List[str],
        excluded_genres: List[str] = None,
        min_rating: float = 0.0
    ) -> Set[int]:
        """
        Get movies matching ANY of the preferred genres (Union operation).
        
        Mathematical Operation:
        Result = (G₁ ∪ G₂ ∪ ... ∪ Gₙ) - (E₁ ∪ E₂ ∪ ... ∪ Eₘ)
        
        Where:
        - Gᵢ = set of movies with genre i
        - Eⱼ = set of movies with excluded genre j
        
        Args:
            preferred_genres: List of genre names (OR matching)
            excluded_genres: List of genres to exclude
            min_rating: Minimum rating threshold
        
        Returns:
            Set of movie IDs matching the criteria
        """
        if not preferred_genres:
            return set()
        
        # Union of all preferred genre sets
        genre_sets = [
            self.genre_to_movies.get(genre, set())
            for genre in preferred_genres
        ]
        result = multi_union(*genre_sets) if genre_sets else set()
        
        # Remove excluded genres
        if excluded_genres:
            excluded_sets = [
                self.genre_to_movies.get(genre, set())
                for genre in excluded_genres
            ]
            excluded = multi_union(*excluded_sets) if excluded_sets else set()
            result = set_difference(result, excluded)
        
        # Filter by minimum rating
        if min_rating > 0.0:
            result = {
                mid for mid in result
                if self.movies[mid].get('rating', 0.0) >= min_rating
            }
        
        return result
    
    def get_movies_by_genres_intersection(
        self,
        preferred_genres: List[str],
        excluded_genres: List[str] = None,
        min_rating: float = 0.0
    ) -> Set[int]:
        """
        Get movies matching ALL of the preferred genres (Intersection operation).
        
        Mathematical Operation:
        Result = (G₁ ∩ G₂ ∩ ... ∩ Gₙ) - (E₁ ∪ E₂ ∪ ... ∪ Eₘ)
        
        Args:
            preferred_genres: List of genre names (AND matching)
            excluded_genres: List of genres to exclude
            min_rating: Minimum rating threshold
        
        Returns:
            Set of movie IDs matching the criteria
        """
        if not preferred_genres:
            return set()
        
        # Intersection of all preferred genre sets
        genre_sets = [
            self.genre_to_movies.get(genre, set())
            for genre in preferred_genres
        ]
        result = multi_intersection(*genre_sets) if genre_sets else set()
        
        # Remove excluded genres
        if excluded_genres:
            excluded_sets = [
                self.genre_to_movies.get(genre, set())
                for genre in excluded_genres
            ]
            excluded = multi_union(*excluded_sets) if excluded_sets else set()
            result = set_difference(result, excluded)
        
        # Filter by minimum rating
        if min_rating > 0.0:
            result = {
                mid for mid in result
                if self.movies[mid].get('rating', 0.0) >= min_rating
            }
        
        return result
    
    def calculate_similarity_scores(
        self,
        movie_ids: Set[int],
        preferred_genres: Set[str]
    ) -> List[Tuple[int, float, Set[str]]]:
        """
        Calculate Jaccard similarity between user preferences and each movie.
        
        Mathematical Formula:
        J(User, Movie) = |User ∩ Movie| / |User ∪ Movie|
        
        Args:
            movie_ids: Set of movie IDs to score
            preferred_genres: Set of user's preferred genres
        
        Returns:
            List of tuples: (movie_id, similarity_score, matching_genres)
            Sorted by similarity score (descending), then by movie ID
        """
        results = []
        
        for movie_id in movie_ids:
            movie = self.movies[movie_id]
            movie_genres = set(movie.get('genres', []))
            
            # Calculate Jaccard similarity
            score = jaccard_similarity(preferred_genres, movie_genres)
            
            # Find matching genres
            matching = preferred_genres & movie_genres
            
            results.append((movie_id, score, matching))
        
        # Sort by score (descending), then by movie_id (for deterministic ordering)
        results.sort(key=lambda x: (-x[1], x[0]))
        
        return results
    
    def recommend(
        self,
        preferred_genres: List[str],
        match_type: str = 'OR',
        excluded_genres: List[str] = None,
        min_rating: float = 0.0,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Generate movie recommendations based on user preferences.
        
        Args:
            preferred_genres: List of preferred genre names
            match_type: 'OR' (union) or 'AND' (intersection)
            excluded_genres: List of genres to exclude
            min_rating: Minimum rating threshold
            limit: Maximum number of recommendations
        
        Returns:
            List of recommendation dictionaries with structure:
                {
                    'movie': movie_dict,
                    'similarity_score': float,
                    'matching_genres': List[str],
                    'explanation': str,
                    'operation': str
                }
        """
        if not preferred_genres:
            return []
        
        # Get matching movies based on match type
        if match_type == 'AND':
            movie_ids = self.get_movies_by_genres_intersection(
                preferred_genres, excluded_genres, min_rating
            )
            operation = 'INTERSECTION'
        else:  # OR
            movie_ids = self.get_movies_by_genres_union(
                preferred_genres, excluded_genres, min_rating
            )
            operation = 'UNION'
        
        if not movie_ids:
            return []
        
        # Calculate similarity scores
        preferred_set = set(preferred_genres)
        scored_movies = self.calculate_similarity_scores(movie_ids, preferred_set)
        
        # Build recommendations
        recommendations = []
        for movie_id, score, matching_genres in scored_movies[:limit]:
            movie = self.movies[movie_id]
            
            # Generate explanation
            explanation = self._generate_explanation(
                movie, matching_genres, preferred_genres,
                match_type, score
            )
            
            recommendations.append({
                'movie': movie,
                'similarity_score': score,
                'matching_genres': list(matching_genres),
                'explanation': explanation,
                'operation': operation,
            })
        
        return recommendations
    
    def _generate_explanation(
        self,
        movie: Dict[str, Any],
        matching_genres: Set[str],
        preferred_genres: List[str],
        match_type: str,
        score: float
    ) -> str:
        """
        Generate a human-readable explanation for a recommendation.
        
        Args:
            movie: Movie dictionary
            matching_genres: Set of genres that matched
            preferred_genres: User's preferred genres
            match_type: 'OR' or 'AND'
            score: Jaccard similarity score
        
        Returns:
            Explanation string
        """
        movie_genres = set(movie.get('genres', []))
        match_count = len(matching_genres)
        total_preferred = len(preferred_genres)
        
        if match_type == 'AND':
            if match_count == total_preferred:
                explanation = (
                    f"This movie matches all {total_preferred} of your preferred genres: "
                    f"{', '.join(sorted(matching_genres))}. "
                )
            else:
                explanation = (
                    f"This movie matches {match_count} of your preferred genres: "
                    f"{', '.join(sorted(matching_genres))}. "
                )
        else:  # OR
            if match_count == 1:
                genre = list(matching_genres)[0]
                explanation = f"This movie matches your preferred genre: {genre}. "
            else:
                explanation = (
                    f"This movie matches {match_count} of your preferred genres: "
                    f"{', '.join(sorted(matching_genres))}. "
                )
        
        # Add Jaccard similarity context
        percentage = score * 100
        explanation += f"Jaccard similarity: {percentage:.1f}%. "
        
        # Mention additional genres if present
        additional = movie_genres - matching_genres
        if additional:
            explanation += f"Also includes: {', '.join(sorted(additional))}."
        
        return explanation
    
    def get_genre_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about the movie dataset.
        
        Returns:
            Dictionary with genre statistics
        """
        stats = {
            'total_movies': len(self.movies),
            'total_genres': len(self.genre_to_movies),
            'genres': {}
        }
        
        for genre, movie_ids in self.genre_to_movies.items():
            stats['genres'][genre] = {
                'count': len(movie_ids),
                'percentage': (len(movie_ids) / len(self.movies)) * 100
            }
        
        # Sort genres by count
        stats['genres'] = dict(
            sorted(
                stats['genres'].items(),
                key=lambda x: x[1]['count'],
                reverse=True
            )
        )
        
        return stats
    
    def find_similar_movies(
        self,
        movie_id: int,
        limit: int = 10
    ) -> List[Tuple[int, float]]:
        """
        Find movies similar to a given movie based on genre overlap.
        
        Args:
            movie_id: ID of the reference movie
            limit: Maximum number of similar movies
        
        Returns:
            List of tuples: (movie_id, similarity_score)
        """
        if movie_id not in self.movies:
            return []
        
        reference_movie = self.movies[movie_id]
        reference_genres = set(reference_movie.get('genres', []))
        
        if not reference_genres:
            return []
        
        # Calculate similarity with all other movies
        similarities = []
        for mid, movie in self.movies.items():
            if mid == movie_id:
                continue
            
            movie_genres = set(movie.get('genres', []))
            score = jaccard_similarity(reference_genres, movie_genres)
            
            if score > 0:
                similarities.append((mid, score))
        
        # Sort by similarity (descending), then by movie_id
        similarities.sort(key=lambda x: (-x[1], x[0]))
        
        return similarities[:limit]
