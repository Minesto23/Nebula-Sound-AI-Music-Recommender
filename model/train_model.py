# model/train_model.py

import pandas as pd
import pickle
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "spotify.csv"
MODEL_DIR = BASE_DIR / "model"

# -----------------------------
# Load dataset
# -----------------------------
print("Loading dataset...")
df = pd.read_csv(DATA_PATH)

# -----------------------------
# Cleaning
# -----------------------------
df = df.drop_duplicates(subset=["track_name", "artist_name"])
df = df.dropna()

# -----------------------------
# Text feature engineering
# -----------------------------
df["text_features"] = (
    df["artist_name"].astype(str) + " " +
    df["artist_genres"].astype(str) + " " +
    df["album_name"].astype(str) + " " +
    df["album_type"].astype(str)
)

# -----------------------------
# TF-IDF
# -----------------------------
tfidf = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)
X_text = tfidf.fit_transform(df["text_features"])

# -----------------------------
# Numeric features
# -----------------------------
NUM_FEATURES = [
    "track_popularity",
    "artist_popularity",
    "artist_followers",
    "track_duration_min",
    "album_total_tracks",
    "explicit"
]

scaler = StandardScaler()
X_num = scaler.fit_transform(df[NUM_FEATURES])

# -----------------------------
# Combine features
# -----------------------------
X = hstack([X_text, X_num])

# -----------------------------
# Train KNN
# -----------------------------

print("Training the model....")
knn = NearestNeighbors(
    n_neighbors=11,
    metric="cosine",
    algorithm="brute"
)
knn.fit(X)

# -----------------------------
# Save artifacts
# -----------------------------
with open(MODEL_DIR / "knn_model.pkl", "wb") as f:
    pickle.dump(knn, f)

with open(MODEL_DIR / "scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open(MODEL_DIR / "tfidf.pkl", "wb") as f:
    pickle.dump(tfidf, f)

df.to_csv(MODEL_DIR / "cleaned_spotify.csv", index=False)

print("✅ Metadata-based model trained successfully")
