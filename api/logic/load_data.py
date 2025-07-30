import pickle
import os

def data():
    CURRENT_DIR = os.path.dirname(__file__)
    movie_path = os.path.abspath(os.path.join(CURRENT_DIR, '..', 'data', "movie_dictdf.pkl"))
    sim_path = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "similarities.pkl"))

    with open(movie_path,'rb') as f:
        movies = pickle.load(f)
    with open(sim_path, 'rb') as f:
        sim_matx = pickle.load(f)
    return movies, sim_matx