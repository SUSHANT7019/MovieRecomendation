# CineSet - Mathematical Movie Recommendation System

A movie recommendation system built entirely on **Discrete Mathematics** and **Set Theory** principles, not AI/ML algorithms.

## 🎯 Project Overview

CineSet demonstrates practical applications of discrete mathematics concepts through a functional movie recommendation system. It uses set operations, Jaccard similarity, and mathematical laws to generate deterministic, transparent recommendations.

## 📚 Mathematical Concepts Implemented

1. **Universal Set** - All movies in the database
2. **Subsets** - Genre-based movie collections
3. **Union (∪)** - OR matching for recommendations
4. **Intersection (∩)** - AND matching for recommendations
5. **Set Difference (−)** - Genre exclusions
6. **Complement (')** - Movies outside a genre
7. **Cartesian Product (×)** - User-movie pairs
8. **Power Set (𝒫)** - All possible genre combinations
9. **Jaccard Similarity** - Preference matching score
10. **De Morgan's Laws** - Mathematical verification
11. **Set Cardinality** - Size calculations

## 🛠️ Technology Stack

### Backend
- Python 3.14
- Django 5.2.19
- Django REST Framework 3.18.3
- SQLite3 database

### Frontend
- HTML5
- CSS3 (Custom styling)
- Vanilla JavaScript (No frameworks)
- Fetch API

### Mathematics
- Custom mathematical engine (`mathematical_engine/`)
- Set operations module
- Recommendation algorithm engine

## 📂 Project Structure

```
MovieRecomendation/
├── movie/                      # Main Django project
├── accounts/                   # User authentication
├── movies/                     # Movie and genre management
├── recommendations/            # Recommendation engine
├── mathematical_engine/        # Core math operations
│   ├── set_operations.py      # Set theory operations
│   └── recommendation_engine.py
├── templates/                  # HTML templates
│   ├── base.html
│   ├── accounts/
│   ├── movies/
│   └── recommendations/
├── static/                     # CSS and JavaScript
│   ├── css/main.css
│   └── js/main.js
├── dataset/                    # Movie data files
├── DM.md                       # Mathematical documentation
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.14+
- pip
- Virtual environment

### Steps

1. **Navigate to the project directory:**
   ```bash
   cd c:\Users\thadg\OneDrive\Desktop\MovieRecomendation
   ```

2. **Activate virtual environment:**
   ```bash
   .\.venv\Scripts\Activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create sample data:**
   ```bash
   python manage.py create_sample_data
   ```

6. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   - Username: admin
   - Password: admin123 (or your choice)

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Web: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📖 Features

### 1. User Authentication
- Registration with email validation
- Login/Logout
- User dashboard

### 2. Movie Discovery
- Browse all movies
- Search by title
- View movie details with genres and ratings

### 3. Preferences Management
- Select preferred genres (preference set)
- Exclude unwanted genres (exclusion set)
- Choose matching strategy (OR/AND)
- Set minimum rating threshold

### 4. Recommendations
- **Union-based (OR):** Movies matching ANY preferred genre
- **Intersection-based (AND):** Movies matching ALL preferred genres
- Jaccard similarity scoring (0-100%)
- Detailed explanations for each recommendation
- Ranked results with matching genres

### 5. Mathematical Lab
- Interactive experiments with real movie data
- Union operation
- Intersection operation
- Set difference
- Complement
- Jaccard similarity calculator
- De Morgan's laws verification
- Real-time results with mathematical formulas

### 6. Recommendation History
- Track all past recommendations
- View similarity scores
- Access explanations

## 🧮 How the Mathematical Engine Works

### Jaccard Similarity Formula

```
J(User, Movie) = |User ∩ Movie| / |User ∪ Movie|
```

Where:
- `User` = Set of user's preferred genres
- `Movie` = Set of movie's genres
- `∩` = Intersection (common genres)
- `∪` = Union (all unique genres)
- `| |` = Cardinality (set size)

### Example

User preferences: `{Action, Sci-Fi, Thriller}`  
Movie genres: `{Action, Thriller, Drama}`

```
Intersection = {Action, Thriller}  (2 elements)
Union = {Action, Sci-Fi, Thriller, Drama}  (4 elements)

J(User, Movie) = 2 / 4 = 0.5 = 50% similarity
```

### Recommendation Algorithm

1. **Build genre sets** from user preferences
2. **Apply set operations** (union for OR, intersection for AND)
3. **Remove exclusions** using set difference
4. **Filter by rating** threshold
5. **Calculate Jaccard similarity** for each movie
6. **Sort by similarity score** (descending)
7. **Generate explanations** for each recommendation

## 📊 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout

### Movies
- `GET /api/movies/` - List all movies
- `GET /api/movies/{id}/` - Movie details
- `GET /api/genres/` - List all genres
- `GET /api/genres/statistics/` - Genre statistics

### Recommendations
- `GET/POST /api/preferences/` - Get/Update user preferences
- `POST /api/recommendations/` - Generate recommendations
- `GET /api/recommendations/history/` - View history

### Mathematical Lab
- `POST /api/math/union/` - Union operation
- `POST /api/math/intersection/` - Intersection operation
- `POST /api/math/difference/` - Set difference
- `POST /api/math/complement/` - Complement
- `POST /api/math/jaccard/` - Jaccard similarity
- `POST /api/math/verify-de-morgan/` - Verify De Morgan's laws

## 🧪 Testing

Run the mathematical engine tests:

```bash
python test_mathematical_engine.py
```

This verifies:
- Basic set operations
- Advanced operations
- De Morgan's laws
- Inclusion-exclusion principle
- Recommendation engine

## 📝 Mathematical Documentation

See `DM.md` for comprehensive mathematical documentation including:
- All formulas with explanations
- Proofs and verifications
- Implementation examples
- Mathematical properties

## 👥 Team Responsibilities

### Member 1: Mathematical Engine & Documentation
- Implement set_operations.py
- Implement recommendation_engine.py
- Write DM.md
- Create test_mathematical_engine.py

### Member 2: Backend & Database
- Configure Django settings
- Create all models (User, Movie, Genre, etc.)
- Implement admin interfaces
- Create API serializers and views

### Member 3: Frontend & UI
- Design HTML templates
- Write CSS styling
- Implement JavaScript for API integration
- Create responsive layouts

### Member 4: Testing & Integration
- Test all mathematical operations
- Test API endpoints
- Create sample data
- Write final documentation

## 🎓 Educational Value

This project demonstrates:

1. **Practical application** of discrete mathematics
2. **Set theory** in real-world problems
3. **Deterministic algorithms** vs. ML approaches
4. **Mathematical rigor** in software engineering
5. **Full-stack development** with mathematical foundation

## 📄 License

This is an educational university project.

## 🙏 Acknowledgments

- MovieLens dataset for sample movie data
- Discrete Mathematics course materials
- Django and Django REST Framework documentation

## 📞 Support

For issues or questions:
1. Check `DM.md` for mathematical concepts
2. Review API documentation above
3. Test with `test_mathematical_engine.py`
4. Check Django admin panel for data

---

**Built with ❤️ and Mathematics**
