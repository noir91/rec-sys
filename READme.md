## End-to-End Content based Recommend System

This repository holds a cosine similarity TF-IDF Recommender system.

- Model trained on ~46k movies 
- Images fetched from TMDB Developers API
- Consists of dockerfile.yaml and docker-compose.yaml for the respective : 
    - Frontend (FastAPI)
    - Backend  (Streamlit)
- Holds Docker images stored as .tar for both ends.
- Repo consists of three model files under ./api/data/
    - movie_dictdf.pkl: DataFrame holding a cleaned version of movies associated with their id and name.
    - similarities.pkl: TF-IDF cosine similarity vectors used at inference for recommending 'top_n' movies.
    - movie_dict.pkl ~ ignore
    
The code present in this repo is modular and hence easier to navigate.

./api/ stores fastapi and functions requried for inference.

./streamlit_app/ stores streamlit app.py which runs the frontend of the application.

Routes used (FastAPI) :

GET
/fetch_poster : gets the posters from TMDB Developer's API for the respective movie_id's

/getdata : gets the data from .pkl files at the initial stage of FastAPI. 
To avoid redundant getdata requests using Lifespan, caching in the data early reducing server overhead.

POST
/recommend : Sends a request body of movie_name and top_n.
    where, 
        - movie_name stands for the Movie's Name associated with the id.
        - top_n for the top recommendations. 
        default set to 6.

