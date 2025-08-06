import unittest
from unittest.mock import patch, MagicMock, Mock
from api.utils.posters import fetch_poster


class Test_utilsfunc(unittest.TestCase):

    @patch('api.utils.posters.requests')
    def test_fetch_poster(self, mock_request):

        self.movie_id = 192
        mock_response = MagicMock()  
        mock_response.json.return_value = {'poster_path' : ""}
        mock_request.get.return_value = mock_response

        result = fetch_poster(self.movie_id)

        self.assertIsInstance(result, str)
        self.assertIn(result, "https://image.tmdb.org/t/p/original/")
        mock_request.get.assert_called_with(f"https://api.themoviedb.org/3/movie/{self.movie_id}?language=en-US", headers = {"accept": "application/json","Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NGU0ZmNiOTYzMzQxYTQ3ODUwYTU5N2E3MmUwNjBmNCIsIm5iZiI6MTc0MTM4NTA1NC4xOTM5OTk4LCJzdWIiOiI2N2NiNmQ1ZTgyMzBiMjU2ZjRmNTg0NWMiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.TkN8TsrUT8rnkQBzRVEb_vSZLSsK6la0e6IlkcCqP58"})
        

    