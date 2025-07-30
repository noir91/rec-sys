# End-to-End Content-based Recommender System

This repository holds a cosine similarity TF-IDF Recommender system.

Model trained on ~46k movies.  
Images are fetched from the TMDB Developers API.

Includes Docker support using `dockerfile` and `docker-compose.yaml` for:

- **Backend** (FastAPI)
- **Frontend** (Streamlit)

---

###  Model Artifacts (under `./api/data/`):

- `movie_dictdf.pkl`: Cleaned DataFrame mapping movie names to their IDs
- `similarities.pkl`: Cosine similarity vectors used during inference
- `movie_dict.pkl`: (temporary, can be ignored)

---

###  Code Structure

- `./api/` — FastAPI backend, core logic, routing, data handling
- `./streamlit_app/` — Streamlit frontend (UI)

---

###  API Routes (FastAPI)

#### `GET` routes:

- `/fetch_poster`: Fetches posters from TMDB API using `movie_id`
- `/getdata`: Preloads `.pkl` files on startup using lifespan caching to avoid redundant loading

#### `POST` route:

- `/recommend`: 
    - Accepts: `movie_name` and `top_n`
    - Returns: list of top-N similar movie recommendations

---

###  Note

This repo uses a modular structure for readability and maintainability.
