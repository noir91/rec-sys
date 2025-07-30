import pickle
import requests as r
import torch
from api.models.schemas import MovieRequest, RecommendationsResponse
from api.logic.load_data import data
from api.utils.posters import fetch_poster

def recommend(request: MovieRequest): # movie_dict = movies, sim_mat = sim_matx,
    movies, sim_mat = data()
    movie_name = request.movie_name
    top_n = request.top_n

    movie_index = movies[movies['title'] == movie_name].index[0]
    #movie_index = next((k for k, v in movie_dict.items() if v == movie_name), None)
    distances = sim_mat[movie_index]
    top_indices = torch.argsort(distances, descending=True)
    top_similiar_indices = top_indices[1: top_n + 1]
    #print(movie_dict.iloc[top_similiar_indices].title)
    print(movies.iloc[top_similiar_indices].title)

    recommend_movies = []
    recommend_movies_posters = []

    for i in top_similiar_indices:
        movie_id = movies.iloc[i.item()]['id']
        recommend_movies.append(movies[movies['id'] == movie_id]['title'].values[0])
        recommend_movies_posters.append(fetch_poster(movie_id))
    return {"titles":recommend_movies, 
            "posters":recommend_movies_posters}