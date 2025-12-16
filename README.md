# 🎵 Nebula Sound – AI Music Recommender
💡 “Discover the music you love without searching: intelligent AI-powered recommendations and playlists.”

## 🔹 Project Overview
Nebula Sound is a metadata-based music recommendation system that allows users to:

- Search songs by name

- Search songs by artist

- Get similar song recommendations

- Generate playlists

This project uses Spotify metadata (without audio features) and demonstrates a full pipeline: preprocessing, model training, backend API, interactive UI, and Docker deployment.

## 🔹 Tech Stack

- Python 3.9+

- Scikit-learn: KNN & feature scaling

- Pandas & NumPy: data processing

- FastAPI + Uvicorn: lightweight backend API

- Gradio: interactive demo interface

## 📂 Dataset
Dataset used: [Spotify Global Music Dataset 2009-2025 (Kaggle)](https://www.kaggle.com/datasets/wardabilal/spotify-global-music-dataset-20092025)

This project focuses on metadata-based features to recommend songs, without analyzing audio directly.

## 🧠 Model

- **TF-IDF** for text features (artist_name, artist_genres, album_name, album_type)

- **StandardScaler** for numeric features (track_popularity, artist_popularity, artist_followers, track_duration_min, album_total_tracks, explicit)

- K-Nearest Neighbors (Cosine similarity) for recommendations

Artifacts stored in model/:
- knn_model.pkl
- scaler.pkl
- tfidf.pkl
- cleaned_spotify.csv


## ⚙️ Installation
1. Clone the repository
```bash
    git clone https://github.com/your-username/nebula-sound.git
    cd nebula-sound
```
2. Python Environment (optional but recommended)
```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
```
3. Install dependencies
```bash
    pip install -r requirements.txt
```
## 🖥️ Run Locally
**Gradio UI** (Interactive Demo)

```bash
    python ui/app.py
```
- Open your browser at http://127.0.0.1:7860

- Tabs available:

    1. Song Recommendations

    2. Playlist Generator

    3. Search by Artist

**FastAPI** Backend (Optional)
```bash
    uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```
Endpoints:

- /health → Check API status

- /recommend?track_name=<song> → Recommend songs

- /artist?artist_name=<artist> → Search songs by artist

- /playlist?track_name=<song>&size=<n> → Generate playlist

## 🐳 Docker Deployment
1. Build Docker image
```bash
    podman build -t nebula-sound:latest .
    # or using docker
    # docker build -t nebula-sound:latest .
```
2. Run Docker container
```bash
    podman run -p 7860:7860 nebula-sound:latest
    # Gradio UI available at http://127.0.0.1:7860
```
**Notes**
- Gradio listens on 0.0.0.0 to expose the interface outside the container.

- FastAPI can also be run in Docker by changing CMD in Dockerfile.

## 📦 Project Structure
```bash
nebula-sound/
│── data/                  # Original dataset
│── model/                 # Trained model and artifacts
│── backend/
│    ├── __init__.py
│    ├── recommender.py    # Recommendation engine
│    └── main.py           # FastAPI backend
│── ui/
│    ├── __init__.py
│    └── app.py            # Gradio interface
│── Dockerfile
│── requirements.txt
│── README.md
```
## 📈 Features
 - Search by song or artist

- Recommend similar tracks

- Generate playlists of configurable size

- Fully reproducible pipeline

- Docker-ready for deployment
 ## 🔹 Author
 Miguel Ernesto Morales Molina – Software Engineer