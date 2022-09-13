from pydantic import BaseModel

class FavoriteList(BaseModel):
    product_id:int
    user_id:int
