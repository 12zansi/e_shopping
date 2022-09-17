
from passlib.context import CryptContext
from back_end.Models.login import ForgotPassword
from back_end.database.connection import cursor, connection



class UserForgotPassword:

    def change_password(self,user:ForgotPassword):
        pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")
        hashed_password = pwd_context.hash(user.password)
        query = "UPDATE users SET password = %s WHERE email = %s "

        cursor.execute(query, (hashed_password, user.email ))
        connection.commit()
        if cursor.rowcount == 0:
            return {"message": "please enter right email"}

        return {"message": "password successfully updated"}
