# CineSet - Mathematical Movie Recommendation Engine

A Django-based movie recommendation platform that demonstrates how **Set Theory** principles from Discrete Mathematics can power intelligent movie recommendations using the **Jaccard Similarity Coefficient**.

---

## 🎯 Project Overview

**CineSet** is an academic project that transforms abstract mathematical concepts into a practical, beautiful web application. Users select their preferred movie genres, and the system calculates personalized recommendations using genuine set theory operations.

### Key Features

✅ **Mathematical Core**: Real Jaccard Similarity calculations  
✅ **Interactive UI**: Beautiful, colorful, modern design  
✅ **Set Theory Lab**: Interactive playground for learning set operations  
✅ **53+ Movies**: Curated dataset with real movie information  
✅ **Complete User System**: Authentication, preferences, favorites  
✅ **Visual Explanations**: See the math behind every recommendation  

---

## 🧮 Mathematical Foundation

### Jaccard Similarity Coefficient

```
J(P, M) = |P ∩ M| / |P ∪ M|
```

Where:
- **P** = Set of user's preferred genres
- **M** = Set of movie's genres
- **|P ∩ M|** = Number of matching genres (intersection)
- **|P ∪ M|** = Total unique genres (union)

### Set Operations Implemented

| Operation | Symbol | Description |
|-----------|--------|-------------|
| **Union** | P ∪ M | All unique genres from both sets |
| **Intersection** | P ∩ M | Genres present in both sets |
| **Difference** | P - M | Genres in P but not in M |
| **Symmetric Difference** | P △ M | Genres in either set but not both |

---

## 🎨 Design System

### Color Palette

```css
Primary:    #7047EB (Vibrant Purple)
Secondary:  #FF6B6B (Coral)
Accent:     #3987FF (Electric Blue)
Highlight:  #FFD166 (Yellow)
Background: #F7F5FF (Soft Lavender)
Success:    #38C99B (Mint Green)
```

### Visual Features

- Gradient backgrounds and buttons
- Rounded cards with shadows
- Smooth animations and transitions
- Interactive hover effects
- Colorful genre chips
- Responsive grid layouts
- Toast notifications

---

## 📂 Project Structure

```
MovieRecomendation/
├── movie/                      # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/                   # User authentication & preferences
│   ├── models.py              # UserPreference model
│   ├── views.py               # Auth & preference views
│   └── admin.py
├── movies/                     # Movie data management
│   ├── models.py              # Movie model
│   ├── views.py               # Explorer & detail views
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── load_movies.py # Movie data loader
├── recommendations/            # Recommendation engine
│   ├── models.py              # Favorite & History models
│   ├── views.py               # Recommendations & dashboard
│   ├── engine.py              # Jaccard similarity engine
│   └── admin.py
├── templates/                  # HTML templates
│   ├── base.html
│   ├── landing.html
│   ├── accounts/
│   ├── movies/
│   └── recommendations/
├── static/                     # CSS, JavaScript, images
│   ├── css/
│   └── js/
├── db.sqlite3                 # SQLite database
└── manage.py
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Django 5.2+
- Virtual environment (recommended)

### Installation

1. **Navigate to project directory:**
   ```bash
   cd MovieRecomendation
   ```

2. **Activate virtual environment:**
   ```bash
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Load movie data:**
   ```bash
   python manage.py load_movies
   ```

6. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server:**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser:**
   ```
   http://127.0.0.1:8000
   ```

---

## 📱 Application Pages

### 1. Landing Page (`/`)
- Hero section with mathematical formula
- "How It Works" explanation
- Featured movies
- Set theory showcase
- Call-to-action buttons

### 2. Registration & Login (`/accounts/`)
- User registration with validation
- Secure login system
- Password requirements
- Session management

### 3. Movie Explorer (`/movies/`)
- Browse all 53 movies
- Filter by genre, year, rating, language
- Search by title
- Add to favorites
- Responsive grid layout

### 4. Genre Preferences (`/accounts/preferences/`)
- Interactive genre selection
- Visual set notation display
- Colorful chip-based UI
- Save and update preferences

### 5. Recommendations (`/recommendations/`)
- Personalized movie list
- Similarity percentage for each
- Matching genres highlighted
- Mathematical analysis expansion
- Complete Jaccard calculation shown

### 6. Mathematics Lab (`/recommendations/math-lab/`)
- Interactive set input
- Real-time calculations
- All set operations displayed
- Venn diagram visualization
- Jaccard similarity calculator
- Educational explanations

### 7. User Dashboard (`/dashboard/`)
- Statistics overview
- Current preference set
- Quick action cards
- Recent recommendations
- Favorite movies gallery

### 8. Movie Detail (`/movies/<id>/`)
- Full movie information
- Large poster display
- Genre tags
- User similarity score
- Add/remove favorites
- Mathematical match explanation

---

## 🧪 Testing

### Run System Test

```bash
python test_system.py
```

**Expected Output:**
```
============================================================
CineSet - Testing Recommendation System
============================================================

Total movies in database: 53

Test user: testuser (created)
Preferences set: P = {Action,Science Fiction,Thriller}

============================================================
Testing Jaccard Similarity Calculations
============================================================

Top 10 Recommendations for user 'testuser':
------------------------------------------------------------

1. Inception (2010)
   Similarity Score: 100.0%
   Movie Genres: {Action, Science Fiction, Thriller}
   Matching Genres: {Action, Science Fiction, Thriller}
   Rating: 8.8/10

2. The Matrix (1999)
   Similarity Score: 66.67%
   Movie Genres: {Action, Science Fiction}
   Matching Genres: {Action, Science Fiction}
   Rating: 8.7/10

...
```

### Manual Testing Checklist

- [ ] Server starts without errors
- [ ] Landing page displays correctly
- [ ] User registration works
- [ ] User login/logout works
- [ ] Genre preferences save
- [ ] Movie explorer shows all movies
- [ ] Filters work correctly
- [ ] Search functionality works
- [ ] Recommendations calculate accurately
- [ ] Math Lab performs set operations
- [ ] Dashboard shows user data
- [ ] Favorites add/remove correctly
- [ ] Movie detail page displays
- [ ] Responsive on mobile devices
- [ ] No console errors

---

## 🎓 Educational Value

### Learning Outcomes

Students using this project will understand:

1. **Set Theory Applications**: How abstract mathematical concepts solve real problems
2. **Jaccard Similarity**: Practical use of similarity coefficients
3. **Algorithm Implementation**: Translating formulas into code
4. **Data Modeling**: Designing relational databases
5. **Full-Stack Development**: Building complete web applications
6. **UI/UX Design**: Creating engaging user interfaces

### Presentation Tips

- Start with a live demo showing the landing page
- Explain the mathematical foundation with examples
- Show the Math Lab to demonstrate set operations
- Walk through the recommendation process for a user
- Highlight the mathematical analysis section
- Discuss the code architecture and design decisions

---

## 🔧 Technical Details

### Database Models

**Movie**
- title, description, poster_url
- release_year, genres, rating
- language, cast

**UserPreference**
- user (OneToOne with User)
- selected_genres (comma-separated)

**Favorite**
- user, movie, created_at

**RecommendationHistory**
- user, movie, similarity_score
- matching_genres, created_at

### Key Algorithms

**Jaccard Similarity (`recommendations/engine.py`)**
```python
def calculate_jaccard_similarity(user_genres_set, movie_genres_set):
    if not user_genres_set or not movie_genres_set:
        return 0.0
    
    intersection = user_genres_set & movie_genres_set
    union = user_genres_set | movie_genres_set
    
    if len(union) == 0:
        return 0.0
    
    return (len(intersection) / len(union)) * 100
```

**Recommendation Ranking**
1. Calculate Jaccard similarity for all movies
2. Sort by similarity (descending)
3. Tie-break by rating (descending)
4. Final tie-break by title (ascending)

---

## 📊 Dataset

53 carefully curated movies including:
- Classic films (The Shawshank Redemption, The Godfather)
- Modern blockbusters (Inception, The Dark Knight)
- International cinema (Parasite, Oldboy, Amélie)
- Animated features (Spirited Away, Toy Story, Coco)
- Various genres and languages

All movies include:
- Accurate titles and years
- Real TMDB poster URLs
- Authentic ratings
- Multiple genres
- Cast information

---

## 🛠️ Customization

### Adding More Movies

Edit `movies/management/commands/load_movies.py` and add:

```python
{
    'title': 'Movie Title',
    'description': 'Movie description...',
    'poster_url': 'https://image.tmdb.org/t/p/w500/poster.jpg',
    'release_year': 2024,
    'genres': 'Genre1, Genre2',
    'rating': 8.5,
    'language': 'English',
    'cast': 'Actor 1, Actor 2'
}
```

Then run:
```bash
python manage.py load_movies
```

### Modifying Colors

Edit `static/css/base.css` and change the CSS variables:

```css
:root {
    --primary: #YourColor;
    --secondary: #YourColor;
    /* etc... */
}
```

---

## 🚨 Troubleshooting

### Common Issues

**Server won't start:**
- Check Python version: `python --version`
- Ensure virtual environment is activated
- Run `python manage.py check`

**No movies showing:**
- Run `python manage.py load_movies`
- Check database: `python manage.py dbshell`

**CSS not loading:**
- Run `python manage.py collectstatic` (if using production)
- Check STATIC_URL in settings.py
- Clear browser cache

**Recommendations not working:**
- Ensure user has preferences set
- Check that movies exist in database
- Review logs for errors

---

## 📝 License

This is an academic project created for educational purposes.

---

## 👨‍💻 Development

### Future Enhancements

- [ ] User reviews and ratings
- [ ] Social features (follow users, share recommendations)
- [ ] Advanced filtering (decade, director, actor)
- [ ] Collaborative filtering algorithm
- [ ] Machine learning integration
- [ ] Real-time notifications
- [ ] API for mobile apps
- [ ] Export recommendations to PDF

### Contributing

This is an academic project, but suggestions are welcome!

---

## 🎉 Credits

**Mathematical Concepts:** Discrete Mathematics - Set Theory  
**Design Inspiration:** Modern entertainment platforms  
**Movie Data:** The Movie Database (TMDB)  
**Framework:** Django  
**Visualization:** Chart.js, Custom SVG

---

## 📞 Support

For questions or issues:
1. Check this README
2. Review the code comments
3. Test with `python test_system.py`
4. Check Django logs

---

**Built with ❤️ and Mathematics**

*"Your interests are sets. Your next favorite movie is their intersection."*
