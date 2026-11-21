# CineSet: Discrete Mathematics Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Set Theory Fundamentals](#set-theory-fundamentals)
3. [Mathematical Operations](#mathematical-operations)
4. [Recommendation Algorithms](#recommendation-algorithms)
5. [Formulas and Proofs](#formulas-and-proofs)
6. [Implementation Examples](#implementation-examples)

---

## Introduction

**CineSet** is a movie recommendation system built entirely on **Discrete Mathematics** principles, specifically **Set Theory**. Unlike AI/ML-based recommenders, CineSet uses deterministic mathematical operations to generate recommendations based on user preferences.

### Core Concept

- **Movies** = Elements
- **Genres** = Sets
- **Database** = Universal Set
- **Preferences** = User-defined Sets
- **Recommendations** = Results of Set Operations

---

## Set Theory Fundamentals

### 1. Universal Set (U)

The universal set contains all movies in our database.

**Definition:**
```
U = {m₁, m₂, m₃, ..., mₙ}
```

Where:
- `U` = Universal set of all movies
- `mᵢ` = Individual movie
- `n` = Total number of movies

**Cardinality:**
```
|U| = n
```

**Example:**
```
U = {Inception, Interstellar, The Matrix, Titanic, The Godfather}
|U| = 5
```

---

### 2. Genre Subsets

Each genre represents a subset of the universal set.

**Definition:**
```
Gᵢ = {m ∈ U | m has genre i}
```

**Example:**
```
Action = {Inception, The Matrix, Interstellar}
Drama = {Titanic, The Godfather}
Sci-Fi = {Inception, The Matrix, Interstellar}
```

**Properties:**
- `Gᵢ ⊆ U` for all genres i
- A movie can belong to multiple genre subsets
- `⋃ᵢ Gᵢ ⊆ U` (union of all genres is a subset of U)

---

## Mathematical Operations

### 3. Union (∪) - OR Operation

**Definition:**
```
A ∪ B = {x | x ∈ A or x ∈ B}
```

**Formula:**
```
|A ∪ B| = |A| + |B| - |A ∩ B|
```

**Application in CineSet:**
Recommend movies matching **at least one** preferred genre.

```
Result = G₁ ∪ G₂ ∪ ... ∪ Gₙ
```

Where `Gᵢ` are preferred genres.

**Properties:**
1. **Commutative:** `A ∪ B = B ∪ A`
2. **Associative:** `(A ∪ B) ∪ C = A ∪ (B ∪ C)`
3. **Idempotent:** `A ∪ A = A`
4. **Identity:** `A ∪ ∅ = A`
5. **Domination:** `A ∪ U = U`

**Example:**
```
User prefers: Action OR Sci-Fi
Action = {Inception, The Matrix, John Wick}
Sci-Fi = {Inception, The Matrix, Interstellar}
Result = Action ∪ Sci-Fi = {Inception, The Matrix, John Wick, Interstellar}
```

---

### 4. Intersection (∩) - AND Operation

**Definition:**
```
A ∩ B = {x | x ∈ A and x ∈ B}
```

**Formula:**
```
|A ∩ B| ≤ min(|A|, |B|)
```

**Application in CineSet:**
Recommend movies matching **all** preferred genres.

```
Result = G₁ ∩ G₂ ∩ ... ∩ Gₙ
```

**Properties:**
1. **Commutative:** `A ∩ B = B ∩ A`
2. **Associative:** `(A ∩ B) ∩ C = A ∩ (B ∩ C)`
3. **Idempotent:** `A ∩ A = A`
4. **Identity:** `A ∩ U = A`
5. **Domination:** `A ∩ ∅ = ∅`

**Example:**
```
User prefers: Action AND Sci-Fi
Action = {Inception, The Matrix, John Wick}
Sci-Fi = {Inception, The Matrix, Interstellar}
Result = Action ∩ Sci-Fi = {Inception, The Matrix}
```

---

### 5. Set Difference (−) - Exclusion

**Definition:**
```
A − B = {x | x ∈ A and x ∉ B}
```

**Alternative Notation:**
```
A \ B  or  A - B
```

**Formula:**
```
|A − B| = |A| - |A ∩ B|
```

**Application in CineSet:**
Remove movies with excluded genres.

```
Result = (Preferred Movies) − (Excluded Movies)
```

**Properties:**
1. **NOT Commutative:** `A − B ≠ B − A` (in general)
2. `A − ∅ = A`
3. `A − A = ∅`
4. `A − B = A ∩ B'` (using complement)

**Example:**
```
User prefers: Action
User excludes: Horror
Action = {Inception, The Matrix, Resident Evil}
Horror = {Resident Evil, The Conjuring}
Result = Action − Horror = {Inception, The Matrix}
```

---

### 6. Complement (') - Opposite Set

**Definition:**
```
A' = U − A = {x ∈ U | x ∉ A}
```

**Alternative Notation:**
```
Ā  or  Aᶜ  or  ¬A
```

**Formula:**
```
|A'| = |U| - |A|
```

**Application in CineSet:**
Find movies that don't belong to a specific genre.

**Properties:**
1. `(A')' = A` (double complement)
2. `A ∪ A' = U`
3. `A ∩ A' = ∅`
4. `U' = ∅`
5. `∅' = U`

**Example:**
```
U = {Inception, The Matrix, Titanic, The Godfather, Toy Story}
Action = {Inception, The Matrix}
Action' = {Titanic, The Godfather, Toy Story}
```

---

### 7. Cartesian Product (×)

**Definition:**
```
A × B = {(a, b) | a ∈ A and b ∈ B}
```

**Formula:**
```
|A × B| = |A| × |B|
```

**Application in CineSet:**
Create user-movie pairs for recommendation tracking.

```
Users × Movies = {(u, m) | u is a user, m is a movie}
```

**Properties:**
1. **NOT Commutative:** `A × B ≠ B × A` (in general)
2. `A × ∅ = ∅`
3. `|A × B × C| = |A| × |B| × |C|`

**Example:**
```
Users = {Alice, Bob}
Movies = {Inception, The Matrix}
Users × Movies = {
    (Alice, Inception),
    (Alice, The Matrix),
    (Bob, Inception),
    (Bob, The Matrix)
}
|Users × Movies| = 2 × 2 = 4
```

---

### 8. Power Set (𝒫)

**Definition:**
```
𝒫(A) = {S | S ⊆ A}
```

The power set is the set of all possible subsets of A.

**Formula:**
```
|𝒫(A)| = 2^|A|
```

**Application in CineSet:**
Generate all possible genre combinations.

**Properties:**
1. `∅ ∈ 𝒫(A)` (empty set is always a subset)
2. `A ∈ 𝒫(A)` (set is a subset of itself)
3. If `|A| = n`, then `𝒫(A)` has `2ⁿ` elements

**Example:**
```
Genres = {Action, Comedy, Drama}
𝒫(Genres) = {
    ∅,
    {Action},
    {Comedy},
    {Drama},
    {Action, Comedy},
    {Action, Drama},
    {Comedy, Drama},
    {Action, Comedy, Drama}
}
|𝒫(Genres)| = 2³ = 8
```

**Warning:** Power sets grow exponentially!
- 10 elements → 1,024 subsets
- 20 elements → 1,048,576 subsets
- 30 elements → 1,073,741,824 subsets

---

### 9. Jaccard Similarity

**Definition:**
```
J(A, B) = |A ∩ B| / |A ∪ B|
```

**Range:**
```
0 ≤ J(A, B) ≤ 1
```

**Interpretation:**
- `J(A, B) = 0` → Sets are completely disjoint (no overlap)
- `J(A, B) = 1` → Sets are identical
- `J(A, B) = 0.5` → Sets are 50% similar

**Application in CineSet:**
Measure similarity between user preferences and movie genres.

**Properties:**
1. **Symmetric:** `J(A, B) = J(B, A)`
2. `J(A, A) = 1`
3. `J(A, ∅) = 0` (if `A ≠ ∅`)
4. `J(∅, ∅) = 0` (by convention)

**Example:**
```
User Preferences = {Action, Sci-Fi, Thriller}
Movie Genres = {Action, Thriller, Drama}

A ∩ B = {Action, Thriller}
A ∪ B = {Action, Sci-Fi, Thriller, Drama}

J(User, Movie) = |{Action, Thriller}| / |{Action, Sci-Fi, Thriller, Drama}|
               = 2 / 4
               = 0.5
               = 50% similarity
```

**Ranking Movies:**
Movies are ranked by Jaccard similarity score in descending order.

---

### 10. De Morgan's Laws

Two fundamental laws relating complement, union, and intersection.

**Law 1:**
```
(A ∪ B)' = A' ∩ B'
```

**Interpretation:** The complement of a union equals the intersection of complements.

**Law 2:**
```
(A ∩ B)' = A' ∪ B'
```

**Interpretation:** The complement of an intersection equals the union of complements.

**Verification Example:**

Given:
```
U = {1, 2, 3, 4, 5, 6}
A = {1, 2, 3}
B = {3, 4, 5}
```

**Verify Law 1:**
```
A ∪ B = {1, 2, 3, 4, 5}
(A ∪ B)' = {6}

A' = {4, 5, 6}
B' = {1, 2, 6}
A' ∩ B' = {6}

Therefore: (A ∪ B)' = A' ∩ B' ✓
```

**Verify Law 2:**
```
A ∩ B = {3}
(A ∩ B)' = {1, 2, 4, 5, 6}

A' = {4, 5, 6}
B' = {1, 2, 6}
A' ∪ B' = {1, 2, 4, 5, 6}

Therefore: (A ∩ B)' = A' ∪ B' ✓
```

**Application in CineSet:**
Validate logical consistency of recommendation filters.

---

### 11. Set Cardinality

**Definition:**
```
|A| = number of elements in set A
```

**Cardinality Formulas:**

1. **Union (Inclusion-Exclusion Principle):**
   ```
   |A ∪ B| = |A| + |B| - |A ∩ B|
   ```

2. **Three Sets:**
   ```
   |A ∪ B ∪ C| = |A| + |B| + |C| 
                 - |A ∩ B| - |A ∩ C| - |B ∩ C| 
                 + |A ∩ B ∩ C|
   ```

3. **Difference:**
   ```
   |A − B| = |A| - |A ∩ B|
   ```

4. **Complement:**
   ```
   |A'| = |U| - |A|
   ```

5. **Cartesian Product:**
   ```
   |A × B| = |A| × |B|
   ```

6. **Power Set:**
   ```
   |𝒫(A)| = 2^|A|
   ```

**Application in CineSet:**
Display statistics about recommendation results.

---

## Recommendation Algorithms

### Algorithm 1: Union-Based Recommendations (OR Matching)

**Input:**
- `P = {g₁, g₂, ..., gₙ}` (preferred genres)
- `E = {e₁, e₂, ..., eₘ}` (excluded genres)
- `min_rating` (minimum rating threshold)

**Steps:**

1. **Build Genre Sets:**
   ```
   Gᵢ = {m ∈ U | m has genre gᵢ}
   ```

2. **Compute Union:**
   ```
   Candidates = G₁ ∪ G₂ ∪ ... ∪ Gₙ
   ```

3. **Apply Exclusions:**
   ```
   Excluded = E₁ ∪ E₂ ∪ ... ∪ Eₘ
   Result = Candidates − Excluded
   ```

4. **Filter by Rating:**
   ```
   Result = {m ∈ Result | rating(m) ≥ min_rating}
   ```

5. **Calculate Jaccard Similarity:**
   ```
   For each m in Result:
       score(m) = J(P, genres(m))
   ```

6. **Sort and Return:**
   ```
   Sort Result by score (descending), then by movie_id
   Return top k movies
   ```

**Time Complexity:** O(|U| + k log k)

---

### Algorithm 2: Intersection-Based Recommendations (AND Matching)

**Input:** Same as Algorithm 1

**Steps:**

1. **Build Genre Sets:**
   ```
   Gᵢ = {m ∈ U | m has genre gᵢ}
   ```

2. **Compute Intersection:**
   ```
   Candidates = G₁ ∩ G₂ ∩ ... ∩ Gₙ
   ```

3. **Apply Exclusions:**
   ```
   Excluded = E₁ ∪ E₂ ∪ ... ∪ Eₘ
   Result = Candidates − Excluded
   ```

4. **Filter by Rating:**
   ```
   Result = {m ∈ Result | rating(m) ≥ min_rating}
   ```

5. **Calculate Jaccard Similarity:**
   ```
   For each m in Result:
       score(m) = J(P, genres(m))
   ```

6. **Sort and Return:**
   ```
   Sort Result by score (descending), then by movie_id
   Return top k movies
   ```

**Time Complexity:** O(|U| + k log k)

**Note:** Intersection typically produces fewer results than union.

---

### Algorithm 3: Jaccard-Based Ranking

For each movie `m` in the candidate set:

1. **Extract Genre Sets:**
   ```
   User_Genres = P = {g₁, g₂, ..., gₙ}
   Movie_Genres = M = genres(m)
   ```

2. **Calculate Intersection:**
   ```
   Matching = P ∩ M
   ```

3. **Calculate Union:**
   ```
   Total = P ∪ M
   ```

4. **Compute Jaccard Similarity:**
   ```
   J(P, M) = |Matching| / |Total|
   ```

5. **Handle Edge Cases:**
   ```
   If |Total| = 0:
       J(P, M) = 0
   ```

6. **Convert to Percentage:**
   ```
   Similarity_Percentage = J(P, M) × 100%
   ```

**Ranking Rule:**
```
Rank movies by:
    1. Jaccard similarity (descending)
    2. Movie ID (ascending, for determinism)
```

---

## Formulas and Proofs

### Proof: Inclusion-Exclusion Principle

**Theorem:**
```
|A ∪ B| = |A| + |B| - |A ∩ B|
```

**Proof:**

Let:
- `x` = number of elements only in A
- `y` = number of elements in both A and B
- `z` = number of elements only in B

Then:
```
|A| = x + y
|B| = y + z
|A ∩ B| = y
|A ∪ B| = x + y + z
```

Calculate:
```
|A| + |B| - |A ∩ B| = (x + y) + (y + z) - y
                      = x + y + z
                      = |A ∪ B|
```

**QED** ∎

---

### Proof: De Morgan's Law 1

**Theorem:**
```
(A ∪ B)' = A' ∩ B'
```

**Proof:**

**Part 1:** Show `(A ∪ B)' ⊆ A' ∩ B'`

Let `x ∈ (A ∪ B)'`
```
⟹ x ∉ (A ∪ B)
⟹ x ∉ A and x ∉ B
⟹ x ∈ A' and x ∈ B'
⟹ x ∈ A' ∩ B'
```

**Part 2:** Show `A' ∩ B' ⊆ (A ∪ B)'`

Let `x ∈ A' ∩ B'`
```
⟹ x ∈ A' and x ∈ B'
⟹ x ∉ A and x ∉ B
⟹ x ∉ (A ∪ B)
⟹ x ∈ (A ∪ B)'
```

Since both inclusions hold, `(A ∪ B)' = A' ∩ B'`

**QED** ∎

---

### Jaccard Similarity Properties

**Property 1: Symmetry**
```
J(A, B) = J(B, A)
```

**Proof:**
```
J(A, B) = |A ∩ B| / |A ∪ B|
        = |B ∩ A| / |B ∪ A|    (intersection and union are commutative)
        = J(B, A)
```

**Property 2: Reflexivity**
```
J(A, A) = 1
```

**Proof:**
```
J(A, A) = |A ∩ A| / |A ∪ A|
        = |A| / |A|
        = 1
```

**Property 3: Bounds**
```
0 ≤ J(A, B) ≤ 1
```

**Proof:**

Lower bound:
```
|A ∩ B| ≥ 0  (intersection is always non-negative)
|A ∪ B| > 0  (assuming non-empty sets)
⟹ J(A, B) ≥ 0
```

Upper bound:
```
|A ∩ B| ≤ |A ∪ B|  (intersection is always a subset of union)
⟹ J(A, B) = |A ∩ B| / |A ∪ B| ≤ 1
```

**QED** ∎

---

## Implementation Examples

### Example 1: Simple Recommendation

**Given:**
```
Database: 5 movies
User prefers: Action OR Sci-Fi
User excludes: Horror
Minimum rating: 7.0
```

**Data:**
```
Movie1: {Action, Sci-Fi}, rating=8.5
Movie2: {Action, Horror}, rating=7.2
Movie3: {Drama}, rating=8.0
Movie4: {Sci-Fi, Thriller}, rating=7.8
Movie5: {Action, Sci-Fi, Thriller}, rating=9.0
```

**Step 1: Build Sets**
```
Action = {Movie1, Movie2, Movie5}
Sci-Fi = {Movie1, Movie4, Movie5}
Horror = {Movie2}
```

**Step 2: Union**
```
Candidates = Action ∪ Sci-Fi = {Movie1, Movie2, Movie4, Movie5}
```

**Step 3: Exclude Horror**
```
Result = Candidates − Horror = {Movie1, Movie4, Movie5}
```

**Step 4: Filter by Rating**
```
Movie1: 8.5 ≥ 7.0 ✓
Movie4: 7.8 ≥ 7.0 ✓
Movie5: 9.0 ≥ 7.0 ✓
Result = {Movie1, Movie4, Movie5}
```

**Step 5: Calculate Jaccard Similarity**
```
User = {Action, Sci-Fi}

Movie1 = {Action, Sci-Fi}
J(User, Movie1) = |{Action, Sci-Fi}| / |{Action, Sci-Fi}| = 2/2 = 1.00

Movie4 = {Sci-Fi, Thriller}
J(User, Movie4) = |{Sci-Fi}| / |{Action, Sci-Fi, Thriller}| = 1/3 = 0.33

Movie5 = {Action, Sci-Fi, Thriller}
J(User, Movie5) = |{Action, Sci-Fi}| / |{Action, Sci-Fi, Thriller}| = 2/3 = 0.67
```

**Step 6: Rank**
```
1. Movie1: 1.00 (100% match)
2. Movie5: 0.67 (67% match)
3. Movie4: 0.33 (33% match)
```

**Final Recommendations:**
1. Movie1 (Action, Sci-Fi) - 100% similarity
2. Movie5 (Action, Sci-Fi, Thriller) - 67% similarity
3. Movie4 (Sci-Fi, Thriller) - 33% similarity

---

### Example 2: Intersection Matching

**Given:**
```
User prefers: Action AND Sci-Fi AND Thriller
```

**Data:**
```
Movie1: {Action, Sci-Fi}
Movie2: {Action, Sci-Fi, Thriller}
Movie3: {Sci-Fi, Thriller}
Movie4: {Action, Thriller}
```

**Build Sets:**
```
Action = {Movie1, Movie2, Movie4}
Sci-Fi = {Movie1, Movie2, Movie3}
Thriller = {Movie2, Movie3, Movie4}
```

**Compute Intersection:**
```
Result = Action ∩ Sci-Fi ∩ Thriller
       = {Movie1, Movie2, Movie4} ∩ {Movie1, Movie2, Movie3} ∩ {Movie2, Movie3, Movie4}
       = {Movie2}
```

**Only Movie2 has all three genres!**

---

### Example 3: De Morgan's Verification

**Given:**
```
U = {M1, M2, M3, M4, M5, M6}
Action = {M1, M2, M3}
Comedy = {M3, M4, M5}
```

**Verify Law 1: (A ∪ B)' = A' ∩ B'**

**Left Side:**
```
Action ∪ Comedy = {M1, M2, M3, M4, M5}
(Action ∪ Comedy)' = {M6}
```

**Right Side:**
```
Action' = {M4, M5, M6}
Comedy' = {M1, M2, M6}
Action' ∩ Comedy' = {M6}
```

**Result:** `{M6} = {M6}` ✓ Law holds!

**Verify Law 2: (A ∩ B)' = A' ∪ B'**

**Left Side:**
```
Action ∩ Comedy = {M3}
(Action ∩ Comedy)' = {M1, M2, M4, M5, M6}
```

**Right Side:**
```
Action' = {M4, M5, M6}
Comedy' = {M1, M2, M6}
Action' ∪ Comedy' = {M1, M2, M4, M5, M6}
```

**Result:** `{M1, M2, M4, M5, M6} = {M1, M2, M4, M5, M6}` ✓ Law holds!

---

## Summary

CineSet implements the following discrete mathematics concepts:

| Concept | Mathematical Symbol | Application |
|---------|---------------------|-------------|
| Universal Set | U | All movies in database |
| Subset | ⊆ | Genre collections |
| Union | ∪ | OR matching |
| Intersection | ∩ | AND matching |
| Difference | − | Exclusions |
| Complement | ' | Opposite genres |
| Cartesian Product | × | User-movie pairs |
| Power Set | 𝒫 | All genre combinations |
| Jaccard Similarity | J(A,B) | Similarity scoring |
| De Morgan's Laws | (A∪B)'=A'∩B' | Logical validation |
| Cardinality | \|A\| | Set sizes |

All recommendations are **mathematically verifiable** and **deterministic** - the same preferences always produce the same results.

---

**End of Documentation**
