from pydantic import BaseModel

class Review(BaseModel):
    rating: int
    comment: str
    user_id: int
    like: int
