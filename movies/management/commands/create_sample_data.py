"""
Management command to create sample movie data for testing.

Usage:
    python manage.py create_sample_data
"""

from django.core.management.base import BaseCommand
from django.db import transaction
from movies.models import Genre, Movie, MovieRating
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Create sample movie data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        with transaction.atomic():
            # Create genres
            genre_names = [
                'Action', 'Adventure', 'Animation', 'Children', 'Comedy',
                'Crime', 'Documentary', 'Drama', 'Fantasy', 'Horror',
                'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller',
                'War', 'Western'
            ]
            
            genres = {}
            for name in genre_names:
                genre, created = Genre.objects.get_or_create(name=name)
                genres[name] = genre
                if created:
                    self.stdout.write(f'  Created genre: {name}')
            
            # Sample movies data
            movies_data = [
                ('The Shawshank Redemption', 1994, ['Drama', 'Crime'], 9.3),
                ('The Godfather', 1972, ['Crime', 'Drama'], 9.2),
                ('The Dark Knight', 2008, ['Action', 'Crime', 'Drama'], 9.0),
                ('Pulp Fiction', 1994, ['Crime', 'Drama'], 8.9),
                ('Forrest Gump', 1994, ['Drama', 'Romance'], 8.8),
                ('Inception', 2010, ['Action', 'Sci-Fi', 'Thriller'], 8.8),
                ('The Matrix', 1999, ['Action', 'Sci-Fi'], 8.7),
                ('Interstellar', 2014, ['Adventure', 'Drama', 'Sci-Fi'], 8.6),
                ('The Lion King', 1994, ['Animation', 'Adventure', 'Drama'], 8.5),
                ('The Avengers', 2012, ['Action', 'Adventure', 'Sci-Fi'], 8.0),
                ('Toy Story', 1995, ['Animation', 'Adventure', 'Children', 'Comedy'], 8.3),
                ('Finding Nemo', 2003, ['Animation', 'Adventure', 'Children', 'Comedy'], 8.1),
                ('The Conjuring', 2013, ['Horror', 'Mystery', 'Thriller'], 7.5),
                ('A Quiet Place', 2018, ['Drama', 'Horror', 'Sci-Fi'], 7.5),
                ('The Notebook', 2004, ['Drama', 'Romance'], 7.8),
                ('Titanic', 1997, ['Drama', 'Romance'], 7.9),
                ('Gladiator', 2000, ['Action', 'Adventure', 'Drama'], 8.5),
                ('Braveheart', 1995, ['Action', 'Drama', 'War'], 8.3),
                ('Saving Private Ryan', 1998, ['Drama', 'War'], 8.6),
                ('The Departed', 2006, ['Crime', 'Drama', 'Thriller'], 8.5),
                ('The Prestige', 2006, ['Drama', 'Mystery', 'Thriller'], 8.5),
                ('Memento', 2000, ['Mystery', 'Thriller'], 8.4),
                ('The Silence of the Lambs', 1991, ['Crime', 'Drama', 'Thriller'], 8.6),
                ('Se7en', 1995, ['Crime', 'Drama', 'Mystery'], 8.6),
                ('The Usual Suspects', 1995, ['Crime', 'Mystery', 'Thriller'], 8.5),
                ('Blade Runner 2049', 2017, ['Drama', 'Mystery', 'Sci-Fi', 'Thriller'], 8.0),
                ('Mad Max: Fury Road', 2015, ['Action', 'Adventure', 'Sci-Fi'], 8.1),
                ('Avatar', 2009, ['Action', 'Adventure', 'Fantasy', 'Sci-Fi'], 7.8),
                ('The Lord of the Rings: The Fellowship of the Ring', 2001, ['Action', 'Adventure', 'Drama', 'Fantasy'], 8.8),
                ('The Lord of the Rings: The Return of the King', 2003, ['Action', 'Adventure', 'Drama', 'Fantasy'], 9.0),
                ('Harry Potter and the Prisoner of Azkaban', 2004, ['Adventure', 'Family', 'Fantasy', 'Mystery'], 7.9),
                ('Spider-Man: Into the Spider-Verse', 2018, ['Action', 'Animation', 'Adventure', 'Sci-Fi'], 8.4),
                ('Coco', 2017, ['Animation', 'Adventure', 'Children', 'Comedy', 'Fantasy'], 8.4),
                ('Up', 2009, ['Animation', 'Adventure', 'Children', 'Comedy', 'Drama'], 8.3),
                ('WALL-E', 2008, ['Animation', 'Adventure', 'Children', 'Sci-Fi'], 8.4),
                ('Inside Out', 2015, ['Animation', 'Adventure', 'Children', 'Comedy', 'Drama'], 8.1),
                ('Zootopia', 2016, ['Animation', 'Adventure', 'Children', 'Comedy'], 8.0),
                ('The Grand Budapest Hotel', 2014, ['Adventure', 'Comedy', 'Drama'], 8.1),
                ('La La Land', 2016, ['Comedy', 'Drama', 'Musical', 'Romance'], 8.0),
                ('Whiplash', 2014, ['Drama', 'Musical'], 8.5),
                ('The Social Network', 2010, ['Drama'], 7.8),
                ('Good Will Hunting', 1997, ['Drama', 'Romance'], 8.3),
                ('A Beautiful Mind', 2001, ['Drama', 'Romance'], 8.2),
                ('The Truman Show', 1998, ['Comedy', 'Drama', 'Sci-Fi'], 8.2),
                ('Eternal Sunshine of the Spotless Mind', 2004, ['Drama', 'Romance', 'Sci-Fi'], 8.3),
                ('Her', 2013, ['Drama', 'Romance', 'Sci-Fi'], 8.0),
                ('Ex Machina', 2014, ['Drama', 'Sci-Fi', 'Thriller'], 7.7),
                ('Arrival', 2016, ['Drama', 'Sci-Fi'], 7.9),
                ('Edge of Tomorrow', 2014, ['Action', 'Sci-Fi'], 7.9),
                ('District 9', 2009, ['Action', 'Sci-Fi', 'Thriller'], 7.9),
                ('Moon', 2009, ['Drama', 'Mystery', 'Sci-Fi'], 7.8),
            ]
            
            movies_created = 0
            for title, year, genre_names_list, rating in movies_data:
                movie, created = Movie.objects.get_or_create(
                    title=title,
                    release_year=year,
                    defaults={
                        'overview': f'Sample movie: {title}'
                    }
                )
                
                if created:
                    movies_created += 1
                    
                    # Add genres
                    for genre_name in genre_names_list:
                        if genre_name in genres:
                            movie.genres.add(genres[genre_name])
                    
                    # Add rating
                    MovieRating.objects.create(
                        movie=movie,
                        source='imdb',
                        rating=Decimal(str(rating)),
                        vote_count=random.randint(10000, 2000000)
                    )
                    
                    self.stdout.write(f'  Created movie: {title} ({year})')
        
        self.stdout.write(self.style.SUCCESS(
            f'\nSample data created successfully!'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'  Genres: {len(genre_names)}'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'  Movies: {movies_created}'
        ))
