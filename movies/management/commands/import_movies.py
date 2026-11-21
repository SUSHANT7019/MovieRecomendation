"""
Management command to import movies from CSV files.
Supports MovieLens dataset format.

Usage:
    python manage.py import_movies <path_to_movies.csv>
    
CSV Format:
    movieId,title,genres
    1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
"""

import csv
import re
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from movies.models import Genre, Movie, MovieRating
from decimal import Decimal


class Command(BaseCommand):
    help = 'Import movies from CSV file (MovieLens format)'

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            help='Path to the movies CSV file'
        )
        parser.add_argument(
            '--ratings-file',
            type=str,
            help='Optional: Path to ratings CSV file',
            default=None
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing movies before import'
        )

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        ratings_file = options.get('ratings_file')
        clear = options.get('clear', False)

        # Clear existing data if requested
        if clear:
            self.stdout.write(self.style.WARNING('Clearing existing movies...'))
            Movie.objects.all().delete()
            Genre.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared existing data'))

        # Import movies
        try:
            self.import_movies(csv_file)
        except FileNotFoundError:
            raise CommandError(f'File not found: {csv_file}')
        except Exception as e:
            raise CommandError(f'Error importing movies: {str(e)}')

        # Import ratings if provided
        if ratings_file:
            try:
                self.import_ratings(ratings_file)
            except FileNotFoundError:
                self.stdout.write(self.style.WARNING(f'Ratings file not found: {ratings_file}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error importing ratings: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Import completed successfully!'))

    @transaction.atomic
    def import_movies(self, csv_file):
        """Import movies from CSV file."""
        self.stdout.write(f'Importing movies from {csv_file}...')

        genres_created = {}
        movies_created = 0
        movies_updated = 0

        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                movie_id = row.get('movieId')
                title = row.get('title', '').strip()
                genres_str = row.get('genres', '')

                if not title:
                    continue

                # Extract year from title (e.g., "Toy Story (1995)")
                year_match = re.search(r'\((\d{4})\)', title)
                year = int(year_match.group(1)) if year_match else None
                
                # Remove year from title
                clean_title = re.sub(r'\s*\(\d{4}\)', '', title).strip()

                # Get or create movie
                movie, created = Movie.objects.get_or_create(
                    tmdb_id=int(movie_id) if movie_id else None,
                    defaults={
                        'title': clean_title,
                        'release_year': year,
                    }
                )

                if created:
                    movies_created += 1
                else:
                    movies_updated += 1
                    movie.title = clean_title
                    if year:
                        movie.release_year = year
                    movie.save()

                # Process genres
                if genres_str and genres_str != '(no genres listed)':
                    genre_names = [g.strip() for g in genres_str.split('|')]
                    
                    for genre_name in genre_names:
                        if genre_name not in genres_created:
                            genre, _ = Genre.objects.get_or_create(name=genre_name)
                            genres_created[genre_name] = genre
                        else:
                            genre = genres_created[genre_name]
                        
                        movie.genres.add(genre)

                if movies_created % 100 == 0:
                    self.stdout.write(f'  Processed {movies_created} movies...')

        self.stdout.write(self.style.SUCCESS(
            f'Movies imported: {movies_created} created, {movies_updated} updated'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'Genres created: {len(genres_created)}'
        ))

    @transaction.atomic
    def import_ratings(self, ratings_file):
        """Import ratings from CSV file."""
        self.stdout.write(f'Importing ratings from {ratings_file}...')

        ratings_created = 0
        
        # Build movie ID mapping
        movie_map = {}
        for movie in Movie.objects.all():
            if movie.tmdb_id:
                movie_map[movie.tmdb_id] = movie

        with open(ratings_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # MovieLens ratings format: userId,movieId,rating,timestamp
            # We'll calculate average ratings per movie
            movie_ratings = {}
            
            for row in reader:
                movie_id = int(row.get('movieId', 0))
                rating = float(row.get('rating', 0))
                
                if movie_id not in movie_ratings:
                    movie_ratings[movie_id] = []
                movie_ratings[movie_id].append(rating)
            
            # Create average ratings
            for movie_id, ratings in movie_ratings.items():
                if movie_id in movie_map:
                    movie = movie_map[movie_id]
                    avg_rating = sum(ratings) / len(ratings)
                    
                    MovieRating.objects.update_or_create(
                        movie=movie,
                        source='movielens',
                        defaults={
                            'rating': Decimal(str(round(avg_rating, 1))),
                            'vote_count': len(ratings)
                        }
                    )
                    ratings_created += 1

        self.stdout.write(self.style.SUCCESS(
            f'Ratings imported: {ratings_created} movies rated'
        ))
