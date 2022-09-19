from passlib.context import CryptContext
from fastapi import HTTPException, Depends
import random
from back_end.Models.register import Register, Verification
from email_validator import validate_email, EmailNotValidError
from back_end.database.connection import cursor, connection
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from back_end.database.session import start_session
from requests import Session
from sqlalchemy import and_
from back_end.database.tables.tb_cart import TBCarts

from back_end.database.tables.tb_users import TBUsers

conf = ConnectionConfig(
      MAIL_USERNAME = "zansiviradiya2002@gmail.com",
      MAIL_PASSWORD = "pcjxjktxygriwiev",
      MAIL_FROM = "zansiviradiya2002@gmail.com",
      MAIL_PORT = 587,
      MAIL_SERVER="smtp.gmail.com",
      MAIL_TLS=True,
      MAIL_SSL=False,
      USE_CREDENTIALS = True,
      VALIDATE_CERTS = True
    )


class UsersRegister:
    pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)
        
        return add_new_data

    async def register(self, user:Register):
        try:
         valid = validate_email(email = user.email)
         email = valid.email
        except EmailNotValidError:
          raise HTTPException(
            status_code=404, 
            detail="please enter a valid email")

        
        query = self.db.query(TBUsers).filter(TBUsers.name == user.name or TBUsers.email == user.email).first()
        if query:
          raise HTTPException(status_code=400, detail="username or email already exists")
        
        otp_no = random.randint(100000,999999)
        hashed_password = UsersRegister.pwd_context.hash(user.password)
        new_user_query = TBUsers(name = user.name, 
           email = email,
           password = hashed_password, 
           otp = otp_no)

        new_user = UsersRegister._add_in_table(self,new_user_query)

        cart_query = TBCarts(user_id = new_user.id)
        UsersRegister._add_in_table(self,cart_query)
        
        message = MessageSchema(
         subject="Fastapi-Mail module",
         recipients = [user.email],
         body = "verify your account otp no: " + str(otp_no),
        )

        fm = FastMail(conf)

        await fm.send_message(message)
         
        return {"data": "email sent successfully "+ user.email }
        

    def verify_otp(self,verification:Verification):
      query = self.db.query(TBUsers).filter(and_(TBUsers.email == verification.email, TBUsers.otp == verification.otp)).first()
  
     
      if query:
         update_query = self.db.query(TBUsers).filter(TBUsers.email == verification.email)
           
         update_query.update({TBUsers.otp : 0 })
         self.db.commit()  
        
         return {"data":"You are successfully registered"}

      return {"data":"otp is incorrect"}
