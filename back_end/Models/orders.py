from pydantic import BaseModel

class Orders(BaseModel):

  address_id: int
  cart_id: int
  

