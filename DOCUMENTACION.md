# 📘 Documentación del Proyecto: Nebula Sound

## 📋 Descripción General

**Nebula Sound** es un sistema inteligente de recomendación musical basado en metadatos. Su objetivo es sugerir canciones y generar playlists personalizadas sin necesidad de analizar el audio directamente, utilizando en su lugar características acústicas y metadatos textuales extraídos de un dataset de Spotify.

### ¿Qué hace?
- Encuentra canciones similares a una "canción semilla".
- Genera playlists automáticas de tamaño configurable.
- Permite la búsqueda de artistas y sus discografías.
- Ofrece una interfaz visual interactiva y una API backend robusta.

### ¿Para qué sirve?
Sirve como motor de descubrimiento musical y demostración técnica de un pipeline completo de Machine Learning, desde la ingeniería de características hasta el despliegue en producción con Docker.

### Público Objetivo
- **Usuarios finales**: Amantes de la música que desean descubrir nuevas canciones.
- **Desarrolladores y Data Scientists**: Interesados en sistemas de recomendación, procesamiento de lenguaje natural (NLP) aplicado a metadatos y arquitectura de software modular.

---

## 🏗️ Arquitectura del Proyecto

El proyecto sigue una arquitectura modular desacoplada, separando la lógica de entrenamiento, el backend de servicio y la interfaz de usuario.

### Estructura de Carpetas

```bash
Nebula-Sound-AI-Music-Recommender/
│── backend/                 # Lógica del servidor y API
│    ├── main.py             # Definición de endpoints (FastAPI)
│    └── recommender.py      # Lógica de inferencia y carga de modelos
│
│── model/                   # Entrenamiento y artefactos del modelo
│    ├── train_model.py      # Script de entrenamiento y limpieza de datos
│    ├── cleaned_spotify.csv # Dataset procesado
│    └── *.pkl               # Modelos serializados (KNN, Scaler, TF-IDF)
│
│── ui/                      # Interfaz de usuario
│    └── app.py              # Aplicación interactiva (Gradio)
│
│── data/                    # Datos crudos (entrada)
│── Dockerfile               # Configuración para contenedorización
│── requirements.txt         # Dependencias del proyecto
└── README.md                # Información básica
```

### Flujo General del Sistema
1.  **Entrenamiento (Offline)**:
    - Se carga el dataset de Spotify (`data/`).
    - Se limpian los datos y se crean características híbridas (texto + numéricas).
    - Se entrena un modelo KNN y se serializan los artefactos en `model/`.
2.  **Inferencia (Online)**:
    - Al iniciar, el backend carga los modelos `.pkl` en memoria.
    - El usuario envía una consulta (nombre de canción) vía UI o API.
    - El sistema vectoriza la consulta y busca los vecinos más cercanos usando similitud coseno.
    - Se devuelven los resultados enriquecidos con metadatos.

### Componentes Principales

| Componente | Responsabilidad |
| :--- | :--- |
| **`model/train_model.py`** | Pipeline ETL: limpieza, vectorización (TF-IDF), escalado (StandardScaler) y entrenamiento del modelo KNN. |
| **`backend/recommender.py`** | Carga los modelos entrenados y expone funciones core (`recommend_songs`, `generate_playlist`) para ser usadas por la API o la UI. Maneja la lógica de búsqueda fuzzy. |
| **`backend/main.py`** | Servidor API REST que expone la funcionalidad al mundo exterior. |
| **`ui/app.py`** | Interfaz gráfica amigable construida con Gradio para interactuar con el sistema visualmente. |

---

## 🛠️ Tecnologías Utilizadas

### Lenguajes
- **Python 3.9+**: Lenguaje principal para todo el desarrollo.

### Frameworks y Librerías
- **FastAPI**: Para la creación del backend API REST de alto rendimiento.
- **Gradio**: Para la construcción rápida de la interfaz de usuario de demostración.
- **Scikit-learn**: Para los algoritmos de ML (KNN, StandardScaler, TF-IDF).
- **Pandas & NumPy**: Para manipulación y análisis eficiente de datos estructurados.
- **RapidFuzz**: Para búsqueda difusa (fuzzy search) de nombres de canciones y artistas.
- **Uvicorn**: Servidor ASGI para ejecutar FastAPI.

### Herramientas
- **Docker / Podman**: Para empaquetado y despliegue consistente.

---

## ⚙️ Instalación y Configuración

### Requisitos Previos
- Python 3.9 o superior instalado.
- (Opcional) Docker o Podman si se prefiere ejecución en contenedor.

### Pasos para Instalar

1.  **Clonar el repositorio:**
    ```bash
    git clone <url-del-repo>
    cd Nebula-Sound-AI-Music-Recommender
    ```

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    # venv\Scripts\activate   # En Windows
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Entrenar el modelo (inicialización):**
    Antes de ejecutar la app, es necesario generar los artefactos del modelo si no existen.
    ```bash
    python model/train_model.py
    ```

### Variables de Entorno
El proyecto actualmente no requiere configuración compleja mediante variables de entorno `.env` para su funcionamiento básico local.

---

## 🚀 Uso del Proyecto

### Cómo ejecutarlo

Hay dos formas principales de usar el sistema: a través de la **Interfaz Gráfica (UI)** o mediante la **API Backend**.

#### Opción A: Interfaz Gráfica (Gradio)
Es la forma más fácil de probar el sistema.
```bash
python ui/app.py
```
- Abrir navegador tras la ejecución (usualmente `http://127.0.0.1:7860`).
- Navegar entre pestañas: "Song Recommendations", "Playlist Generator", "Search by Artist".

#### Opción B: API Backend (FastAPI)
Para integraciones o pruebas técnicas.
```bash
uvicorn backend.main:app --reload
```
- Documentación interactiva disponible en `http://127.0.0.1:8000/docs`.

### Comandos Importantes

| Acción | Comando |
| :--- | :--- |
| **Entrenar Modelo** | `python model/train_model.py` |
| **Lanzar UI** | `python ui/app.py` |
| **Lanzar API** | `uvicorn backend.main:app --reload` |
| **Construir Docker** | `docker build -t nebula-sound .` |
| **Correr Docker** | `docker run -p 7860:7860 nebula-sound` |

---

## 🧠 Detalles Técnicos Relevantes

### Lógica Clave
El núcleo de la recomendación se basa en la **similitud de cosenos** sobre un espacio vectorial híbrido:
1.  **Características de Texto**: Se concatenan `artist_name`, `artist_genres`, `album_name` y `album_type`. Se procesan con **TF-IDF** (Term Frequency-Inverse Document Frequency) para capturar la esencia semántica.
2.  **Características Numéricas**: Se usan atributos como popularidad, duración, explícito, y número de tracks. Se normalizan con **StandardScaler** para que tengan el mismo peso que el texto.
3.  **Búsqueda KNN**: Cuando llega una canción, se vectoriza igual que el set de entrenamiento y se buscan los $N$ vectores más cercanos (vecinos).

### Decisiones de Diseño
- **Sin API de Spotify en tiempo real**: Se decidió usar un dataset estático (CSV) para garantizar que el proyecto sea autónomo, reproducible y no dependa de credenciales externas o límites de API.
- **Frontend en el Backend (Gradio)**: Para el MVP, se integró la UI directamente con el código de lógica (`recommender.py`) en lugar de consumir la API HTTP. Esto simplifica el despliegue local.
- **Búsqueda Fuzzy**: Se implementó `RapidFuzz` para mejorar la experiencia de usuario, permitiendo encontrar canciones incluso con errores tipográficos leves.

### Consideraciones de Rendimiento
- **Carga en Memoria**: Los modelos `.pkl` y el DataFrame se cargan completos en RAM al inicio. Esto hace que las consultas sean muy rápidas (<100ms), pero requiere memoria suficiente (aprox. 1GB recomendado).
- **Escalabilidad**: El uso de `scikit-learn` `NearestNeighbors` con algoritmo `brute` es eficiente para datasets medianos (miles de canciones), pero para millones de registros se recomendaría un índice aproximado como **Faiss** o **Annoy**.

---

## ✅ Buenas Prácticas y Recomendaciones

### Cómo extender el proyecto
1.  **Añadir nuevas características**:
    - Editar `model/train_model.py` para incluir columnas como `danceability`, `energy`, etc. (si estuvieran en el dataset original).
    - Re-entrenar el modelo con `python model/train_model.py`.
2.  **Integrar Spotify Web API**:
    - Crear un módulo adaptador en `backend/` para obtener metadatos frescos o carátulas de álbumes en tiempo real.

### Posibles Mejoras
- **Persistencia**: Guardar las playlists generadas en una base de datos (SQLite/PostgreSQL).
- **Feedback de Usuario**: Permitir al usuario dar "Like" a recomendaciones para re-entrenar o ajustar el modelo en el futuro.
- **Frontend Moderno**: Migrar la UI de Gradio a React o Vue.js consumiendo la FastAPI para una experiencia más personalizada.

### Advertencias
- **Reiniciar tras entrenar**: Si ejecutas `train_model.py`, debes reiniciar el servidor (API o UI) para que cargue los nuevos archivos `.pkl`.
- **Datos Estáticos**: Las recomendaciones están limitadas a la música existente en el dataset `data/spotify.csv`. Canciones muy nuevas podrían no aparecer.
