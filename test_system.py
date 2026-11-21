import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserPreference
from recommendations.engine import get_recommendations
from movies.models import Movie

print("="*60)
print("CineSet - Testing Recommendation System")
print("="*60)

# Check movie count
movie_count = Movie.objects.count()
print(f"\nTotal movies in database: {movie_count}")

# Create test user
user, created = User.objects.get_or_create(
    username='testuser',
    defaults={'email': 'test@test.com'}
)
user.set_password('testpass123')
user.save()
print(f"\nTest user: {user.username} ({'created' if created else 'exists'})")

# Create preferences
prefs, created = UserPreference.objects.get_or_create(user=user)
prefs.selected_genres = 'Action,Science Fiction,Thriller'
prefs.save()
print(f"Preferences set: P = {{{prefs.selected_genres}}}")

# Get recommendations
print("\n" + "="*60)
print("Testing Jaccard Similarity Calculations")
print("="*60)

recs = get_recommendations(user, limit=10)
print(f"\nTop 10 Recommendations for user '{user.username}':")
print("-"*60)

for i, rec in enumerate(recs, 1):
    movie = rec['movie']
    score = rec['similarity_score']
    matching = rec['matching_genres']
    
    print(f"\n{i}. {movie.title} ({movie.release_year})")
    print(f"   Similarity Score: {score}%")
    print(f"   Movie Genres: {{{', '.join(rec['movie_genres'])}}}")
    print(f"   Matching Genres: {{{', '.join(matching)}}}")
    print(f"   Rating: {movie.rating}/10")

print("\n" + "="*60)
print("System Test Complete!")
print("="*60)
