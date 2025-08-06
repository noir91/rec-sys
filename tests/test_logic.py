from api.logic.load_data import data
import pandas as pd
import torch as t
from unittest.mock import Mock, patch
import unittest
from api.models.schemas import MovieRequest
from api.logic.recommender import recommend

class Test_logicfunc(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.movies, self.sim_mat = data()
    
    def test_loading_data(self):
        # Testing datatype
        assert isinstance(self.movies, pd.DataFrame)
        assert isinstance(self.sim_mat, t.Tensor)

        # Testing structure
        assert 'title' in self.movies.columns
        assert self.sim_mat.shape[0] == self.movies.shape[0]
    
    @patch('api.models.schemas.MovieRequest')
    def test_recommend(self, mock_movierequest):

        mock_movierequest = Mock()
        mock_movierequest.movie_name = 'Iron Man'
        mock_movierequest.top_n = 6

        result = {'titles':[], 'posters': []}

        assert isinstance(recommend(mock_movierequest) , dict)
        assert result.keys() == recommend(mock_movierequest).keys()
    

            
