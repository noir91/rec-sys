import unittest
from streamlit_app.st_app import fetch_movie_title, post_response_data
from unittest.mock import MagicMock
from unittest.mock import patch

class Test_stapp(unittest.TestCase):
    
    @patch('streamlit_app.st_app.requests')
    def test_fetch_movie_title(self, mock_fetch_movie_title):

        # Response
        mock_response = MagicMock() 
        mock_response.json.return_value = {'title': ['Hulk']}

        # Return
        mock_fetch_movie_title.get.return_value = mock_response
        return self.assertEqual(fetch_movie_title(), ['Hulk'])
    
    @patch('streamlit_app.st_app.requests')
    def test_post_response_data(self, mock_post_response_data):

        # variables
        title = 'Hulk'
        mock_payload = {'movie_name': title, 'top_n': 6}

        # Response
        mock_response = MagicMock()
        mock_response.json.return_value = {'titles': [], 'posters': []}

        # Return
        mock_post_response_data.post.return_value = mock_response
        self.assertEqual(post_response_data(title), {'titles': [], 'posters': []})
        mock_post_response_data.post.assert_called_with(url = 'http://backend:8000/recommend', json = mock_payload)