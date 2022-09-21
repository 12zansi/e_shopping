from passlib.context import CryptContext
from back_end.Models.login import ForgotPassword
from back_end.Models.register import Verification
from back_end.database.tables.tb_users import TBUsers
from back_end.database.session import start_session
from fastapi import Depends
from back_end.dependencies.users.user_info.register import conf
import random
from fastapi_mail import FastMail, MessageSchema
from sqlalchemy import and_
from requests import Session


class UserForgotPassword:
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    async def change_password(self, user:ForgotPassword):
        pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")
        global hashed_password 
        hashed_password  = pwd_context.hash(user.password)
        otp_no = random.randint(100000,999999)

        query = self.db.query(TBUsers).filter(TBUsers.email == user.email)\
          .update({TBUsers.otp: otp_no })
        self.db.commit()
        
        if query == 1:
            message = MessageSchema(
              subject="Fastapi-Mail module",
              recipients = [user.email],
              body = "Verify your account otp no: " + str(otp_no),
              )

            fm = FastMail(conf)

            await fm.send_message(message)
            return {"message": "Otp send your mail"}

        return {"message": "Email does not exist"}

    def verify_otp(self, verification: Verification):
      
      query = self.db.query(TBUsers).filter(and_(TBUsers.email == verification.email, TBUsers.otp == verification.otp))\
        .update({TBUsers.otp : 0, TBUsers.password : hashed_password })

      self.db.commit()
        
      if query:
        return {"message": "Password updated successfully" }

      return {"message": "Incorrect Otp"}
      




