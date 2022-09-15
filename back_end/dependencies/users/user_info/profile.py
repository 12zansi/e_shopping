from jose import jwt,JWTError
from back_end.database.connection import cursor
from fastapi import Depends,HTTPException
from back_end.database.mysql.profile import TBUser
from back_end.dependencies.login import UserLogin
from fastapi.security import HTTPBearer 



token_auth_scheme = HTTPBearer()


class UserProfile(UserLogin):
    def get_profile(self,token:str = Depends(token_auth_scheme)):
    
        try:
            payload = jwt.decode(token.credentials, UserProfile._JWT_SECRET, algorithms=['HS256'])
            username: str = payload.get("sub")
        
        except jwt.ExpiredSignatureError:
           raise HTTPException(status_code=403, detail="token has been expired")
        
        except JWTError:
           raise HTTPException(status_code=401, detail="Could Not Valid Credentials")
        
        query = "SELECT id,name,email, is_admin FROM users WHERE name = %s"
        cursor.execute(query, (username,))
        
        result = cursor.fetchone()

        data = TBUser()
        data.id = result[0]
        data.name = result[1]
        data.email = result[2]
        data.is_admin = result[3]
    
        return data
    