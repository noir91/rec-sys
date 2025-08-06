import requests

def fetch_poster(movie_id):
    API_key = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NGU0ZmNiOTYzMzQxYTQ3ODUwYTU5N2E3MmUwNjBmNCIsIm5iZiI6MTc0MTM4NTA1NC4xOTM5OTk4LCJzdWIiOiI2N2NiNmQ1ZTgyMzBiMjU2ZjRmNTg0NWMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.TkN8TsrUT8rnkQBzRVEb_vSZLSsK6la0e6IlkcCqP58'
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NGU0ZmNiOTYzMzQxYTQ3ODUwYTU5N2E3MmUwNjBmNCIsIm5iZiI6MTc0MTM4NTA1NC4xOTM5OTk4LCJzdWIiOiI2N2NiNmQ1ZTgyMzBiMjU2ZjRmNTg0NWMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.TkN8TsrUT8rnkQBzRVEb_vSZLSsK6la0e6IlkcCqP58"}

    response = requests.get(url, headers=headers)
    poster = response.json()['poster_path']
    print(poster)
    return "https://image.tmdb.org/t/p/original/" + poster