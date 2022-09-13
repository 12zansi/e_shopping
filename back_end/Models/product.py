from pydantic import BaseModel

class Product(BaseModel):

    name: str
    description: str
    mrp: int
    price: int
    brand_id: int
    category_id: int
    return_policy_in_days: int
    
class ProductImage(BaseModel):
    name: str
    product_id: int

class ProductDetail(BaseModel):
    detail: dict
    product_id: int
