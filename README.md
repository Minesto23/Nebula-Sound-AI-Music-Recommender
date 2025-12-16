# 🎵 Nebula Sound – AI Music Recommender
💡 “Discover the music you love without searching: intelligent AI-powered recommendations and playlists.”

## 🔹 Project Overview
Nebula Sound is a music recommendation system powered by Machine Learning.
Given a song input by the user, the application can:

- Suggest songs with similar acoustic features

- Automatically generate personalized playlists

- Deliver fast and explainable results, ready to play

This project combines Data Science, Machine Learning, and software development to create a fully functional demo

## 🔹 Features
- Search for songs by name (case-insensitive)

- Get song recommendations based on similarity

- Generate smart playlists from a seed song

- Simple and intuitive interface for demo purposes

## 🔹 Tech Stack

- Python 3.9+

- Scikit-learn: KNN & feature scaling

- Pandas & NumPy: data processing

- FastAPI + Uvicorn: lightweight backend API

- Gradio / Tkinter: interactive demo interface

## 🔹 How to Run the Demo
1. Clone the repository
```bash
git clone https://github.com/your-username/nebula-sound.git
cd nebula-sound
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Train the model (only once)
```bash
python model/train_model.py
```
5. Run the backend
```bash
uvicorn backend.main:app --reload
```
6. Open the interface and try your favorite songs

## 🔹 Demo
You can view a working demo at [HuggingFace Spaces / insert link here] (if deploying there)

## 🔹 Dataset
Dataset used: Spotify Global Music (2009–2025)
Source: Kaggle

Includes global song information such as:

- Danceability

- Energy

- Tempo

- Loudness

- Acousticness

- Valence

- Instrumentalness

- And more

## 🔹 Project Goals
- Create a realistic and functional project for your portfolio
- Showcase skills in:
    - Applied Machine Learning
    - API development
    - UI/UX for demos
- Prepare a project ready to deploy on VPS or free services

## 🔹 Roadmap
 - Improve search with partial and fuzzy matching

 - Add filters by genre, energy, or mood

 - Optional integration with official Spotify API

 -  Advanced and responsive UI

 ## 🔹 Author
 Miguel Ernesto Morales Molina – Software Engineer