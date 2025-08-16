import pandas as pd
from fastapi import FastAPI
from contextlib import asynccontextmanager
import requests as r
from api.routes import recommend
from api.logic.load_data import data


def add(a,b):
    return a + b
# caching the data on startup for 
@asynccontextmanager
async def lifespan(app: FastAPI):
    movies, sim_mat = data()
    app.state.movies = movies
    app.state.sim_mat = sim_mat
    yield

# Recommend and getdata routes
app = FastAPI(title = 'Content Based Recommender System', lifespan= lifespan)
app.include_router(recommend.apirouter)





