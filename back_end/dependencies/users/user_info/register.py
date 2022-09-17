from passlib.context import CryptContext
from fastapi import HTTPException
import random
from back_end.Models.register import Register, Verification
from email_validator import validate_email, EmailNotValidError
from back_end.database.connection import cursor, connection




class UsersRegister:
    pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

    def register(self, user:Register):
        try:
         valid = validate_email(email = user.email)
         email = valid.email
        except EmailNotValidError:
          raise HTTPException(
            status_code=404, 
            detail="please enter a valid email")

        db_user = "select * from users where name = %s or email = %s"
        cursor.execute(db_user, (user.name,email))
        result = cursor.fetchone()
  
        if result:
          raise HTTPException(status_code=400, detail="username or email already exists")
        
        otp = random.randint(100000,999999)
        
        query = "insert into users (name,email,password,otp) values(%s, %s, %s, %s)"

        hashed_password = UsersRegister.pwd_context.hash(user.password)
        val = (user.name, email, hashed_password, otp)

        cursor.execute(query, val)
        connection.commit()

        user_id = cursor.lastrowid
        query1 = "insert into cart (user_id) values (%s)"
        cursor.execute(query1, (user_id, ))
        connection.commit()
         
        return otp

    def verify_otp(self,verification:Verification):
      query = "SELECT * FROM users WHERE email = %s and otp = %s"
      cursor.execute(query, (verification.email,verification.otp ))
      result = cursor.fetchone()
      if result:
         query = "UPDATE users SET otp = 0 WHERE email = %s "

         cursor.execute(query, (verification.email, ))
         connection.commit()
         return {"data":"You are successfully registered"}

      return {"data":"otp is incorrect"}
