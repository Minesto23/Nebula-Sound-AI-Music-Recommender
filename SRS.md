# 🎧 NEBULA SOUND
### AI-Powered Music Recommendation & Playlist Generator

> A music recommendation system that generates intelligent song suggestions and playlists based on a seed track, using Spotify's global dataset (2009–2025).

**Nebula Sound** is a music recommendation app that allows users to input a song and receive:

- Similar songs based on acoustic features  
- Automatically generated playlists  
- Fast, explainable results  
- A simple and intuitive interface  

The system leverages **unsupervised Machine Learning** (KNN + cosine similarity) using real Spotify data.


## 📌 Project Description
Nebula Sound is a music recommendation app that allows users to input a song and receive:

- Similar songs based on acoustic features

- Automatically generated playlists

- Fast, explainable results

- A simple and intuitive interface

The system leverages unsupervised Machine Learning (KNN + cosine similarity) using real Spotify data.

## 🎯 Objectives

- Build a realistic music recommendation system

- Showcase skills in:

    - Data Science & Machine Learning

    - Backend development with FastAPI

    - Software architecture & modular design

- Create a deployable demo for portfolio purposes

## 🧾 Software Requirements Specification (SRS)

### 1️⃣ Functional Requirements

| ID    | Requirement                                          |
| ----- | ---------------------------------------------------- |
| FR-01 | Users can search for songs by name                   |
| FR-02 | The system recommends similar songs for a given song |
| FR-03 | The system generates a playlist of 5–10 songs        |
| FR-04 | Searches are case-insensitive                        |
| FR-05 | Recommendations are returned within 1 second         |
| FR-06 | The system works without Spotify API access          |

### 2️⃣ Non-Functional Requirements
| ID     | Requirement                                           |
| ------ | ----------------------------------------------------- |
| NFR-01 | System runs on 1 GB RAM                               |
| NFR-02 | Model is loaded once at startup                       |
| NFR-03 | Architecture supports VPS or free deployment services |
| NFR-04 | Modular and documented code                           |
| NFR-05 | Compatible with Python 3.9+                           |

### 3️⃣ Users
- Technical recruiters

-  Software engineers

- Data scientists

- End users (demo)

## 🧠 System Architecture
```
User
   ↓
Interface (Web / Gradio / Desktop)
   ↓
FastAPI Backend
   ↓
ML Model (KNN + Cosine Similarity)
   ↓
Spotify Dataset (CSV)
```

## 🤖 Machine Learning Model

### Approach
- Type: **Unsupervised**  
- Algorithm: **K-Nearest Neighbors (KNN)**  
- Metric: **Cosine Similarity**

### Features Used
- danceability  
- energy  
- loudness  
- speechiness  
- acousticness  
- instrumentalness  
- liveness  
- valence  
- tempo

## 🧪 Data Pipeline

1. Load Spotify dataset  
2. Clean missing values  
3. Select acoustic features  
4. Scale features using `StandardScaler`  
5. Train KNN model  
6. Serialize model (`.pkl`)

## 🖥 User Interface (MVP)

### Features
- Text input for song name  
- “Recommend” button  
- List of suggested songs  
- Option to generate playlist  

*(Can be implemented using Gradio, HTML/CSS, or Tkinter)*

## ⚙️ Technology Stack

### Backend
- Python 3.9+  
- FastAPI  
- Uvicorn  
- Scikit-learn  
- Pandas  
- NumPy  

### ML
- NearestNeighbors (KNN)  
- StandardScaler  
- Pickle  

### Frontend (Demo)
- Gradio **(recommended)**  
- or HTML/CSS/JS

## 🏗 Project Structure

```
nebula-sound/
│── data/
│ └── spotify.csv
│
│── model/
│ ├── train_model.py
│ ├── knn_model.pkl
│ └── scaler.pkl
│
│── backend/
│ ├── main.py
│ └── recommender.py
│
│── ui/
│ └── app.py
│
│── requirements.txt
│── README.md
└── .gitignore
```
## 🚀 Installation & Running

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/nebula-sound.git
cd nebula-sound
```
### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Train the model
```bash
python model/train_model.py
```
### 5️⃣ Run the backend
```bash
uvicorn backend.main:app --reload
```
## 🧪 Example Usage
Input:
```nginx
Blinding Lights
```
Output:
```
- Save Your Tears – The Weeknd
- Take My Breath – The Weeknd
- Don't Start Now – Dua Lipa
- Physical – Dua Lipa
- Levitating – Dua Lipa
```

## ☁️ Deployment Requirements (Demo)
| Resource | Minimum        |
| -------- | -------------- |
| CPU      | 1 vCPU         |
| RAM      | 1 GB           |
| Disk     | 5 GB           |
| GPU      | ❌ Not required |

## 🛣 Roadmap

- Dynamic playlist generation

- Partial / fuzzy search

- Filter by energy / mood

- Optional Spotify API integration

- Advanced UI

## 👨‍💻 Author

Miguel Ernesto Morales Molina
Software Engineer