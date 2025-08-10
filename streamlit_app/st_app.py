import sys
import os

# modifying sys.path for modular code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import streamlit as st
import requests 

# Functions
def fetch_movie_title():
    res_data = requests.get('http://backend:8000/getdata')
    return res_data.json()['title']

def post_response_data(title): # frontend gets json
    payload = {"movie_name": title, "top_n" : 6}
    response = requests.post( url = "http://backend:8000/recommend", json = payload)
    return response.json()       

def main():
    # -- STREAMLIT (UI) --

    st.title('Content-Based Movie Recommender system')
    titles = fetch_movie_title()
    selected_movie_name = st.selectbox('', titles)

    # - When user clicks on button, we will fetch it from the API

    data = post_response_data(selected_movie_name)
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

    