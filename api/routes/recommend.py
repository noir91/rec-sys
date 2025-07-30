from api.models.schemas import RecommendationsResponse, MovieRequest
from api.logic.recommender import recommend
from fastapi import APIRouter, Request
import requests as r
from api.logic.load_data import data
apirouter = APIRouter()

@apirouter.post('/recommend', response_model= RecommendationsResponse)
def recommend_fastapi(request: MovieRequest):
    return recommend(request)

@apirouter.get('/getdata')
def getdata(request: Request):
    movies = request.app.state.movies
    return {'title': movies['title'].tolist()}
