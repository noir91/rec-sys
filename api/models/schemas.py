from pydantic import BaseModel
from typing import List
class MovieRequest(BaseModel):
    movie_name: str
    top_n: int
class RecommendationsResponse(BaseModel):
    titles: List[str]
    posters: List[str]    