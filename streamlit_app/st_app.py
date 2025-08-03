import sys
import os

# modifying sys.path for modular code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import streamlit as st
import requests as r
import json

# Functions
def fetch_movie_title():
    res_data = r.get('http://backend:8000/getdata')
    return res_data.json()['title']

def get_response_data(): # frontend gets json
    payload = {"movie_name": selected_movie_name, "top_n" : 6}
    response = r.post( url = "http://backend:8000/recommend", json = payload)
    return response.json()

# -- STREAMLIT (UI) --

st.title('Content-Based Movie Recommender system')
titles = fetch_movie_title()
selected_movie_name = st.selectbox('', titles)

# - When user clicks on button, we will fetch it from the API

data = get_response_data()
if st.button('Recommend'):
    # titles and posters being extracted from RecommendationResponse made into json
    names = data['titles']
    posters = data['posters']

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            title = names[i]
            st.subheader(names[i])
            st.image(posters[i])