# backend/recommender.py

import pickle
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from rapidfuzz import process


# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"

# -----------------------------
# Load artifacts
# -----------------------------
with open(MODEL_DIR / "knn_model.pkl", "rb") as f:
    knn = pickle.load(f)

with open(MODEL_DIR / "scaler.pkl", "rb") as f:
    scaler: StandardScaler = pickle.load(f)

with open(MODEL_DIR / "tfidf.pkl", "rb") as f:
    tfidf: TfidfVectorizer = pickle.load(f)

df = pd.read_csv(MODEL_DIR / "cleaned_spotify.csv")

# -----------------------------
# Constants
# -----------------------------
NUM_FEATURES = [
    "track_popularity",
    "artist_popularity",
    "artist_followers",
    "track_duration_min",
    "album_total_tracks",
    "explicit"
]

# -----------------------------
# Internal helpers
# -----------------------------
def _build_text_features(row: pd.Series) -> str:
    return (
        f"{row['artist_name']} "
        f"{row['artist_genres']} "
        f"{row['album_name']} "
        f"{row['album_type']}"
    )

def _vectorize_song(row: pd.Series):
    # Text vector
    text_vector = tfidf.transform([_build_text_features(row)])

    # Numeric vector
    num_vector = scaler.transform(pd.DataFrame([row[NUM_FEATURES]]))

    # Combined vector
    return hstack([text_vector, num_vector])

# -----------------------------
# Public API
# -----------------------------
def find_song(track_name: str) -> pd.Series:
    """
    Find a song by name using fuzzy matching.
    Returns the most relevant match.
    """
    choices = df["track_name"].tolist()
    match, score, idx = process.extractOne(track_name, choices)

    if score < 60:  # umbral mínimo de coincidencia
        raise ValueError(f"Song '{track_name}' not found")

    return df.iloc[idx]


def recommend_songs(track_name: str, n_recommendations: int = 5):
    """Return similar songs based on metadata similarity."""
    song = find_song(track_name)
    song_vector = _vectorize_song(song)

    distances, indices = knn.kneighbors(song_vector, n_neighbors=n_recommendations + 1)

    recommendations = (
        df.iloc[indices[0][1:]]
        .loc[:, ["track_name", "artist_name", "album_name"]]
        .reset_index(drop=True)
    )

    return recommendations

def generate_playlist(track_name: str, size: int = 10):
    """Generate a playlist based on a seed song."""
    return recommend_songs(track_name, n_recommendations=size)
