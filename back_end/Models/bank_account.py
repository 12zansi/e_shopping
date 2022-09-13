from pydantic import BaseModel

class BankAccount(BaseModel):
      holder_name: str
      account_no: int
      ifsc_code: str
      branch_name: str
      user_id: int
