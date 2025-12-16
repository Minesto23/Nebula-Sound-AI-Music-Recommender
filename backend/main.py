# backend/main.py

from fastapi import FastAPI, HTTPException, Query
from backend.recommender import find_song, recommend_songs, generate_playlist, df
import pandas as pd
from rapidfuzz import process, fuzz

app = FastAPI(title="Nebula Sound API", version="1.0")

# -----------------------------
# Health check
# -----------------------------
@app.get("/health")
def health_check():
    return {"status": "OK", "message": "Nebula Sound API is running"}

# -----------------------------
# Recommend songs by track name
# -----------------------------
@app.get("/recommend")
def recommend(track_name: str = Query(..., description="Track name to find recommendations")):
    try:
        recs = recommend_songs(track_name)
        return {"track_name": track_name, "recommendations": recs.to_dict(orient="records")}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# -----------------------------
# Search by artist (fuzzy matching)
# -----------------------------
@app.get("/artist")
def search_by_artist(artist_name: str = Query(..., description="Artist name to search songs")):
    # Normalizar input
    search_name = artist_name.strip().lower()

    # Lista única de artistas en el dataset
    artist_list = df["artist_name"].dropna().unique()

    # Buscar mejor coincidencia fuzzy
    match, score, idx = process.extractOne(
        search_name,
        artist_list,
        scorer=fuzz.WRatio
    )

    # Threshold mínimo para considerar coincidencia
    if score < 60:
        raise HTTPException(status_code=404, detail="Artist not found")

    # Filtrar todas las canciones del artista encontrado
    matches = df[df["artist_name"] == match]

    results = matches.loc[:, ["track_name", "album_name", "track_popularity"]].reset_index(drop=True)
    return {"artist_name": match, "songs": results.to_dict(orient="records")}

# -----------------------------
# Generate playlist
# -----------------------------
@app.get("/playlist")
def playlist(track_name: str = Query(..., description="Track name to generate playlist"),
             size: int = Query(10, description="Number of songs in playlist")):
    try:
        pl = generate_playlist(track_name, size=size)
        return {"track_name": track_name, "playlist": pl.to_dict(orient="records")}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
