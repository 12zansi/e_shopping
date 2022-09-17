from pydantic import BaseModel

class Register(BaseModel):
    name:str
    email: str
    password:str

class Verification(BaseModel):
    email:str
    otp: int