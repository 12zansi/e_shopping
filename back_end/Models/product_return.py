from pydantic import BaseModel

class ProductReturn(BaseModel):
    reason: str
    bank_id: int