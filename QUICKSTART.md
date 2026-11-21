# 🚀 Quick Start Guide - CineSet

Get CineSet up and running in under 5 minutes!

---

## Step 1: Start the Server

```bash
cd MovieRecomendation
.venv\Scripts\activate
python manage.py runserver
```

Open your browser to: **http://127.0.0.1:8000**

---

## Step 2: Create Your Account

1. Click **"Sign Up"** in the navigation
2. Enter a username and password
3. Submit the form

---

## Step 3: Select Your Preferences

1. You'll be redirected to the preferences page
2. Click on genres you enjoy (e.g., Action, Science Fiction, Thriller)
3. Click **"Save Preferences"**

---

## Step 4: Get Recommendations!

1. Click **"Get My Recommendations"** or navigate to **Recommendations**
2. See your personalized movie list ranked by similarity
3. Click **"View Mathematical Analysis"** to see the Jaccard calculation

---

## 🎮 Try the Math Lab

1. Navigate to **"Math Lab"** in the menu
2. Enter two sets (e.g., "Action, Comedy, Drama" and "Action, Thriller, Horror")
3. Click **"Calculate Operations"**
4. See all set operations and Jaccard similarity instantly!

---

## 🎬 Explore Movies

1. Click **"Explore"** in the navigation
2. Browse all 53 movies
3. Use filters to narrow down by genre, year, rating, or language
4. Click any movie to see details
5. Add movies to your favorites with the heart button

---

## 📊 View Your Dashboard

1. Click **"Dashboard"** in the navigation
2. See your statistics, recent recommendations, and favorites
3. Use quick action cards to navigate

---

## 🧪 Test the System

Run the verification script:

```bash
python test_system.py
```

Expected output: Perfect 100% match for Inception with Action+SciFi+Thriller preferences!

---

## 📝 Test Accounts

**Admin Account:**
- Username: `admin`
- Password: `admin123`
- Admin Panel: http://127.0.0.1:8000/admin/

**Test User:**
- Username: `testuser`
- Password: `testpass123`
- Preferences: Action, Science Fiction, Thriller

---

## 🎯 What to Show in Your Demo

### 1. Start with the Landing Page
- Beautiful hero section
- Mathematical formula display
- "How It Works" explanation

### 2. Show the Math Lab
- Enter two sets
- Calculate all operations
- Explain Jaccard similarity
- Show Venn diagram

### 3. Create a Live Demo User
- Register a new account
- Select preferences (e.g., Comedy, Romance, Drama)
- Get recommendations
- Show mathematical analysis

### 4. Explore a Movie
- Click on a recommended movie
- Show the similarity score
- Explain the matching genres
- Add to favorites

### 5. Show the Dashboard
- Statistics overview
- Recent recommendations
- Favorite movies

---

## 💡 Demo Tips

**Best User Preference Combinations:**

1. **Action + Science Fiction + Thriller**
   - 100% match: Inception
   - 66% match: The Matrix

2. **Animation + Adventure + Comedy**
   - High matches: Toy Story, Finding Nemo, Coco

3. **Drama + Crime + Thriller**
   - High matches: The Dark Knight, Pulp Fiction, Se7en

4. **Romance + Drama**
   - High matches: Titanic, The Notebook, La La Land

---

## 🐛 Quick Troubleshooting

**No movies showing?**
```bash
python manage.py load_movies
```

**CSS not loading?**
- Clear your browser cache (Ctrl+Shift+Delete)
- Refresh the page (Ctrl+F5)

**Server won't start?**
```bash
python manage.py check
```

**Need to reset?**
```bash
# Delete database
rm db.sqlite3

# Recreate
python manage.py migrate
python manage.py load_movies
```

---

## 📸 Screenshot Opportunities

Take screenshots of:
1. Landing page hero section
2. Genre preference selection
3. Recommendation list with similarity scores
4. Mathematical analysis expanded
5. Math Lab with results
6. Venn diagram visualization
7. Movie detail page
8. Dashboard overview

---

## ✅ Feature Checklist for Demo

- [ ] Landing page loads
- [ ] Registration works
- [ ] Login works
- [ ] Preferences save
- [ ] Recommendations calculate
- [ ] Math Lab works
- [ ] Filters work
- [ ] Search works
- [ ] Favorites work
- [ ] Dashboard displays
- [ ] Movie details show
- [ ] Mathematical explanations visible

---

## 🎓 Talking Points

### Mathematical Accuracy
"The system uses genuine Jaccard Similarity. For example, if my preferences are {Action, SciFi, Thriller} and a movie has {Action, SciFi, Thriller}, that's 3 matching genres out of 3 total unique genres, giving us 3/3 = 100% match."

### Set Theory
"Every recommendation is calculated using real set operations - intersection, union, and the Jaccard coefficient. Nothing is hardcoded."

### Educational Value
"The Math Lab lets anyone experiment with set theory interactively. Students can see how changing elements affects the similarity score."

### Design Philosophy
"We wanted to show that mathematical applications don't have to be boring. Clean, colorful design makes the concepts more approachable."

---

## 🚀 Ready to Present!

You now have:
- ✅ A fully functional movie recommendation system
- ✅ 53 curated movies with real data
- ✅ Beautiful, modern UI
- ✅ Mathematically accurate calculations
- ✅ Interactive educational tools
- ✅ Complete documentation

**Good luck with your presentation!** 🎉

---

*Average setup time: 3-5 minutes*
*Recommended browsers: Chrome, Firefox, Edge*
*Minimum screen resolution: 1024x768*
