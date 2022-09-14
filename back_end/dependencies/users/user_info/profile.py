from jose import jwt
from back_end.database.connection import my_cursor
from fastapi import Depends

from back_end.dependencies.login import UserLogin
from fastapi.security import HTTPBearer 


token_auth_scheme = HTTPBearer()


class UserProfile(UserLogin):
    def get_profile(self,token:str = Depends(token_auth_scheme)):
        print(token)
        payload = jwt.decode(token.credentials, UserProfile._JWT_SECRET, algorithms=['HS256'])
        username: str = payload.get("sub")
        
        query = "SELECT name,email, is_admin FROM users WHERE name = %s"
        my_cursor.execute(query, (username,))
        
        result = my_cursor.fetchone()
        print(result[0])
        result_dict = {"name": result[0], "email": result[1], "is_admin": result[0] }
        return result_dict
    