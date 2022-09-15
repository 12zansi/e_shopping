from passlib.context import CryptContext
from fastapi import HTTPException

from back_end.Models.register import Register
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
      
        query = "insert into users (name,email,password) values(%s,%s,%s)"

        hashed_password = UsersRegister.pwd_context.hash(user.password)
        val = (user.name, email, hashed_password)

        cursor.execute(query, val)
        connection.commit()

        user_id = cursor.lastrowid
        query1 = "insert into cart (user_id) values (%s)"
        cursor.execute(query1, (user_id, ))
        connection.commit()

        return "You are successfully registered"