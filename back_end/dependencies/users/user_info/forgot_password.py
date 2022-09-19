from passlib.context import CryptContext
from back_end.Models.login import ForgotPassword
from back_end.database.tables.tb_users import TBUsers
from back_end.database.session import start_session
from fastapi import Depends
from requests import Session


class UserForgotPassword:
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def change_password(self, user:ForgotPassword):
        pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")
        hashed_password = pwd_context.hash(user.password)

        query = self.db.query(TBUsers).filter(TBUsers.email == user.email).update({TBUsers.password: hashed_password})

        self.db.commit()
        
        if query == 1:
           return {"message": "Password Successfully Updated"}

        return {"message": "email does not exist"}


