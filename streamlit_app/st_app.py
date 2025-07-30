import sys
import os

# modifying sys.path for modular code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import streamlit as st
import requests as r
import json

# Streamlit
st.title('Content-Based Movie Recommender system')

res_data = r.get('http://backend:8000/getdata')
movies_titles = res_data.json()['title']

selected_movie_name = st.selectbox(
    '',
    movies_titles)
#name = {'movie_name': selected_movie_name}

# - When user clicks on button, we will fetch it from the API
if st.button('Recommend'):
    # Front End sending json
    payload = {"movie_name": selected_movie_name, "top_n" : 6}
    response = r.post( url = "http://backend:8000/recommend",
                    json = payload)
    # Response json
    data = response.json()

    # titles and posters being extracted from RecommendationResponse made into json
    names = data['titles']
    posters = data['posters']

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            title = names[i]
            st.subheader(names[i])
            st.image(posters[i])