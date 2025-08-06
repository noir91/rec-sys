from fastapi.testclient import TestClient
import unittest
from api.app import app


client = TestClient(app)

@app.post('/recommend')
def test_route():    
    payload = {'movie_name': 'Iron Man',
                'top_n': 5}
    headers = {'Content-Type': 'application/json'}
    # Testing FastAPI
    response = client.post('/recommend',
                            json = payload,
                            headers = headers)
    assert response.status_code == 200
    return response.json()
        
class Test_fastapi(unittest.TestCase):
    def test_recommend_route_assertion(self):
        result = test_route()

        # Assertions
        self.assertIsInstance(result, dict)
        self.assertIn("titles", result)
        self.assertIn("posters", result)
        self.assertIsInstance(result["titles"], list)
        self.assertIsInstance(result["posters"], list)
