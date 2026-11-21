# CineSet - Quick Start Guide

## 🚀 5-Minute Setup

### 1. Start the Server
```bash
cd c:\Users\thadg\OneDrive\Desktop\MovieRecomendation
.\.venv\Scripts\Activate
python manage.py runserver
```

### 2. Open Your Browser
Go to: **http://127.0.0.1:8000/**

### 3. Login
- Username: `admin`
- Password: `admin123`

---

## 🎯 Quick Tour

### Step 1: Dashboard
After login, you'll see your dashboard with quick action cards.

### Step 2: Set Preferences
1. Click **"Set Preferences"**
2. Select genres you like (e.g., Action, Sci-Fi)
3. Select genres to exclude (e.g., Horror)
4. Choose **OR matching** (Union) or **AND matching** (Intersection)
5. Click **"Save Preferences"**

### Step 3: Get Recommendations
1. Click **"Get Recommendations"**
2. Click **"Generate Recommendations"** button
3. See your personalized movie list with:
   - Similarity scores (Jaccard coefficient)
   - Matching genres highlighted
   - Mathematical explanations

### Step 4: Try Mathematical Lab
1. Click **"Math Lab"** in navigation
2. Click any operation card (e.g., **Union**)
3. Select 2+ genres
4. Click **"Calculate"**
5. See the mathematical result with formula

---

## 📖 Key URLs

| Page | URL |
|------|-----|
| Landing Page | http://127.0.0.1:8000/ |
| Login | http://127.0.0.1:8000/login/ |
| Dashboard | http://127.0.0.1:8000/dashboard/ |
| Preferences | http://127.0.0.1:8000/preferences/ |
| Recommendations | http://127.0.0.1:8000/recommendations/ |
| Discovery | http://127.0.0.1:8000/movies/discovery/ |
| Math Lab | http://127.0.0.1:8000/math-lab/ |
| History | http://127.0.0.1:8000/history/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## 🧮 Mathematical Operations

### Available in Math Lab:

1. **Union (∪)** - Combine genre sets
   - Formula: `A ∪ B = {x | x ∈ A or x ∈ B}`
   - Example: Action ∪ Comedy = All action OR comedy movies

2. **Intersection (∩)** - Find common movies
   - Formula: `A ∩ B = {x | x ∈ A and x ∈ B}`
   - Example: Action ∩ Sci-Fi = Movies that are BOTH action AND sci-fi

3. **Difference (−)** - Subtract one set from another
   - Formula: `A − B = {x | x ∈ A and x ∉ B}`
   - Example: Action − Horror = Action movies that are NOT horror

4. **Complement (')** - All movies NOT in a genre
   - Formula: `A' = U − A`
   - Example: Action' = All non-action movies

5. **Jaccard Similarity** - Measure genre similarity
   - Formula: `J(A, B) = |A ∩ B| / |A ∪ B|`
   - Range: 0% (no overlap) to 100% (identical)

6. **De Morgan's Laws** - Verify mathematical laws
   - Law 1: `(A ∪ B)' = A' ∩ B'`
   - Law 2: `(A ∩ B)' = A' ∪ B'`

---

## 💡 Tips

### For Best Recommendations:
- Select 2-4 preferred genres
- Use **OR matching** for variety
- Use **AND matching** for precision
- Set minimum rating (e.g., 7.0) for quality

### For Mathematical Lab:
- Try different genre combinations
- Compare Union vs Intersection results
- Check Jaccard similarity between related genres
- Verify De Morgan's laws with any 2 genres

### Troubleshooting:
- If no recommendations appear, check your preferences
- If server won't start, make sure port 8000 is free
- If styles look broken, hard refresh (Ctrl+F5)

---

## 🧪 Test the Math

Quick test to verify everything works:

### Test 1: Union
1. Math Lab → Union
2. Select: Action, Sci-Fi
3. Result should include The Matrix, Inception, Interstellar

### Test 2: Intersection
1. Math Lab → Intersection
2. Select: Action, Sci-Fi, Thriller
3. Result should be a smaller set (movies with ALL three genres)

### Test 3: Jaccard
1. Math Lab → Jaccard Similarity
2. Genre A: Action, Genre B: Adventure
3. Should show % similarity based on common movies

---

## 📊 Sample Data

The database includes:
- **51 movies** (classics and recent films)
- **17 genres** (Action, Sci-Fi, Drama, Comedy, etc.)
- **Ratings** from IMDb

Sample movies:
- The Shawshank Redemption (Drama, Crime)
- Inception (Action, Sci-Fi, Thriller)
- The Matrix (Action, Sci-Fi)
- Toy Story (Animation, Adventure, Children, Comedy)
- The Dark Knight (Action, Crime, Drama)

---

## 🔧 Admin Panel

Access: **http://127.0.0.1:8000/admin/**

You can:
- View all users
- Browse all movies
- Check genres
- See recommendation history
- Edit movie data
- Add new movies manually

---

## 📝 For Your Presentation

### Key Talking Points:

1. **Mathematical Foundation**
   - "We use set theory, not AI"
   - "Every recommendation has a mathematical explanation"
   - "Deterministic and verifiable"

2. **Jaccard Similarity**
   - "Measures overlap between user preferences and movie genres"
   - "Range: 0% (no match) to 100% (perfect match)"
   - "Formula: |A ∩ B| / |A ∪ B|"

3. **Union vs Intersection**
   - "Union (OR): More variety, broader results"
   - "Intersection (AND): More precise, narrower results"
   - "User chooses strategy based on needs"

4. **Interactive Lab**
   - "Users can experiment with real movie data"
   - "See mathematical operations in action"
   - "Educational and functional"

### Demo Script:
1. Show landing page (30 sec)
2. Register/Login (30 sec)
3. Set preferences (1 min)
4. Generate recommendations (1 min)
5. Explain Jaccard score (1 min)
6. Try Math Lab operation (1 min)
7. Show verification (De Morgan's) (1 min)

**Total: ~6 minutes**

---

## ✅ Quick Checks

Before presentation:
- [ ] Server runs without errors
- [ ] Can login with admin/admin123
- [ ] Preferences save successfully
- [ ] Recommendations generate correctly
- [ ] Math Lab operations work
- [ ] All pages load properly
- [ ] No console errors in browser

---

## 🆘 Emergency Commands

### Reset Everything:
```bash
python manage.py flush
python manage.py create_sample_data
```

### Check if Server is Running:
```bash
netstat -ano | findstr :8000
```

### Stop Server:
- Press `Ctrl+C` in the terminal

### Restart Server:
```bash
python manage.py runserver
```

---

## 📞 Quick Reference

| Need | Command/URL |
|------|-------------|
| Start server | `python manage.py runserver` |
| Run tests | `python test_mathematical_engine.py` |
| Create data | `python manage.py create_sample_data` |
| Shell access | `python manage.py shell` |
| Admin | http://127.0.0.1:8000/admin/ |
| API docs | See README.md |

---

**You're all set! Enjoy exploring CineSet! 🎬**
