from pydantic import BaseModel

class ProductReturn(BaseModel):
    reason: str
    user_id: int
    order_id: int
    order_item_id: int
    bank_id: int