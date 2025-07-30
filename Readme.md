
# 🎬 Recommendation Engine

This project implements a **movie recommendation system** using two popular approaches:
1. **Content-Based Filtering** — recommends similar items based on genre/content
2. **Collaborative Filtering** — recommends items based on user behavior (ratings)

The system is modular and ready to be extended for books, music, jobs, products, etc.

---

## 🚀 Features

- ✅ Recommend similar movies using **TF-IDF + cosine similarity**
- ✅ Recommend movies to a user based on **SVD matrix factorization**
- ✅ Easily swappable datasets (movies, users, ratings)
- ✅ Pure Python, no heavy frameworks
- ✅ Ready for extension into APIs or UIs

---

## 🗂️ Project Structure

```
recommendation_engine/
│
├── data/
│   ├── movies.csv                  # Movie metadata: id, title, genres
│   └── ratings.csv                 # User ratings: userId, movieId, rating
│
├── recommender/
│   ├── content_recommender.py      # TF-IDF-based recommender
│   ├── collaborative_recommender.py # SVD-based user recommender
│   └── utils.py                    # Common data loading helpers
│
├── main.py                         # Run both recommenders
├── requirements.txt                # Project dependencies
└── README.md                       # You're reading it
```

---

## 📊 Data Format

### `movies.csv`

| movieId | title              | genres                       |
|---------|--------------------|------------------------------|
| 1       | Toy Story (1995)   | Adventure|Animation|Children |
| 2       | Jumanji (1995)     | Adventure|Children|Fantasy   |
| 3       | Grumpier Old Men   | Comedy|Romance               |

### `ratings.csv`

| userId | movieId | rating |
|--------|---------|--------|
| 1      | 1       | 4.0    |
| 1      | 2       | 5.0    |
| 2      | 2       | 3.0    |
| 2      | 3       | 2.5    |

---

## 📌 Recommendation Techniques

### 1️⃣ Content-Based Filtering (`content_recommender.py`)

- Uses `TfidfVectorizer` on the movie genres.
- Computes **cosine similarity** between movies.
- Recommends top-N most similar movies to a given title.

### 2️⃣ Collaborative Filtering (`collaborative_recommender.py`)

- Uses a **User × Movie ratings matrix**.
- Applies **SVD** (Singular Value Decomposition) to factorize the matrix.
- Predicts unseen ratings for a user.
- Recommends top-N movies the user hasn't rated yet.

---

## 🔧 Setup Instructions

### ✅ Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ Add sample data

Download MovieLens sample data (e.g., from https://grouplens.org/datasets/movielens/)  
or use your own CSVs in `data/`.

Make sure you have:
- `data/movies.csv`
- `data/ratings.csv`

---

## ▶️ How to Run

Run the main script:

```bash
python main.py
```

Expected output:
```
📌 Content-Based Recommendations:
['Jumanji (1995)', 'Grumpier Old Men (1995)', 'Some Other Title']

📌 Collaborative Filtering Recommendations:
['Movie A', 'Movie B', 'Movie C']
```

---

## 📈 How It Works

### TF-IDF Content Flow:
```
Movie → Genre Text → TF-IDF Matrix → Cosine Similarity Matrix → Top-N Similar Movies
```

### Collaborative Flow:
```
User-Rating Matrix → SVD → Rating Predictions → Top-N Unseen Recommendations
```

---

## 🧩 Easily Extensible

You can adapt this project for:
- 🛍️ Product Recommendations
- 🎵 Music or Playlist Suggestions
- 📚 Book or Course Recommendations
- 🧠 Personalized Learning Paths

---

## 🛠️ Future Improvements

- ✅ Hybrid model: content + collaborative weighting
- ✅ Web interface (e.g., Streamlit or Flask)
- ✅ Real-time API recommendations
- ✅ Implicit feedback integration (e.g., clicks, views)
- ✅ Add user/item metadata (e.g., age, tags)

---

## 📚 Dependencies

```
pandas
scikit-learn
numpy
scipy
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

Built by SRI VIDHYA — feel free to use, fork, and extend!

---

## 📄 License

MIT License — free for personal and commercial use.
