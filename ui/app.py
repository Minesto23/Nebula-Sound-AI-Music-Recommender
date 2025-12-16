# ui/app.py

import gradio as gr
import pandas as pd
from backend.recommender import recommend_songs, generate_playlist, df
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

# -----------------------------
# Helper functions
# -----------------------------
def recommend_track_ui(track_name):
    try:
        recs = recommend_songs(track_name)
        return recs  # recs ya es un DataFrame
    except ValueError:
        return pd.DataFrame(columns=["track_name", "artist_name", "album_name"])


def playlist_ui(track_name, size):
    try:
        pl = generate_playlist(track_name, size=size)
        return pl
    except ValueError:
        return pd.DataFrame(columns=["track_name", "artist_name", "album_name"])


def search_artist_ui(artist_name):
    matches = df[df["artist_name"].str.lower() == artist_name.lower()]
    if matches.empty:
        return pd.DataFrame(columns=["track_name", "album_name", "track_popularity"])
    results = matches.loc[:, ["track_name", "album_name", "track_popularity"]].reset_index(drop=True)
    return results


# -----------------------------
# Gradio Interface
# -----------------------------
with gr.Blocks(title="Nebula Sound Demo") as demo:

    gr.Markdown("## 🎵 Nebula Sound — AI Music Recommender")
    gr.Markdown("Search for a song or an artist and get recommendations or playlists!")

    with gr.Tab("Song Recommendations"):
        track_input = gr.Textbox(label="Enter Track Name")
        rec_btn = gr.Button("Get Recommendations")
        rec_output = gr.Dataframe(headers=["track_name", "artist_name", "album_name"])
        rec_btn.click(fn=recommend_track_ui, inputs=track_input, outputs=rec_output)

    with gr.Tab("Playlist Generator"):
        track_input_pl = gr.Textbox(label="Enter Track Name")
        size_input = gr.Slider(minimum=1, maximum=20, step=1, label="Playlist Size")
        pl_btn = gr.Button("Generate Playlist")
        pl_output = gr.Dataframe(headers=["track_name", "artist_name", "album_name"])
        pl_btn.click(fn=playlist_ui, inputs=[track_input_pl, size_input], outputs=pl_output)

    with gr.Tab("Search by Artist"):
        artist_input = gr.Textbox(label="Enter Artist Name")
        artist_btn = gr.Button("Search Songs")
        artist_output = gr.Dataframe(headers=["track_name", "album_name", "track_popularity"])
        artist_btn.click(fn=search_artist_ui, inputs=artist_input, outputs=artist_output)

# -----------------------------
# Launch
# -----------------------------
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
