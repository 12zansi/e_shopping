from pydantic import BaseModel

class Review(BaseModel):
    rating: int
    comment: str
    like: int
