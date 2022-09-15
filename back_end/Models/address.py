from enum import Enum
from pydantic import BaseModel, Field

class sv(Enum):
    w = "home"
    e = "office"


class Address(BaseModel):
    receiver_name: str
    mobile_no: str = Field(min_length=1, max_length=10, example = "enter only 10 digit")
    address_line1: str
    address_line2: str
    city: str
    pincode: str = Field(min_length=1, max_length=6, example="enter only 6 digit")
    state: str
    type: str = Field( example="home or office")
