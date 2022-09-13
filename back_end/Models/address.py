from pydantic import BaseModel

class Address(BaseModel):
    receiver_name: str
    address_line1: str
    address_line2: str
    mobile_no: str
    city: str
    pincode: str
    state: str
    address_type: str
    user_id: int