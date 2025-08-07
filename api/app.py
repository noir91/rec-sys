
from fastapi import FastAPI
from api.routes import recommend

# Recommend and getdata routes
app = FastAPI(title = 'Content Based Recommender System')
app.include_router(recommend.apirouter)


# caching the data on startup for streamlit
#async def lifespan(app: FastAPI):
    #movies, sim_mat = data()
    #app.state.movies = movies
    #app.state.sim_mat = sim_mat
    #yield


