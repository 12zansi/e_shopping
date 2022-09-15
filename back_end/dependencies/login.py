from datetime import datetime, timedelta
from back_end.Models.login import Login
from back_end.database.connection import cursor
from back_end.database.mysql.profile import TBUser
from back_end.dependencies.users.user_info.register import UsersRegister
from jose import jwt, JWTError
from fastapi import HTTPException

class UserLogin:
    _JWT_SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    Algorithm = "HS256"

    def __verify_password(plain_password: str, hashed_password: str) -> bool:
        
        return UsersRegister.pwd_context.verify(plain_password, hashed_password)

    def __create_access_token(data: dict, expire_delta: timedelta | None = None):
        to_encode = data.copy()
        if expire_delta:
            expire = datetime.utcnow() + expire_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, UserLogin._JWT_SECRET, algorithm=UserLogin.Algorithm)
        return encoded_jwt

    def __authenticate(
        
        email: str,
        password: str,
    ):
        query = "SELECT * FROM users WHERE email = %s "
        cursor.execute(query, (email,))
       

        result = cursor.fetchone()
        print(result)
        if not result:
            return None
        if not UserLogin.__verify_password(password, result[3]):
            return None

        data = TBUser()
        data.id = result[0]
        data.name = result[1]
        data.email = result[2]
        data.password = result[3]
        data.is_admin = result[4]
        
        return data

    def login(self,form_data:Login):
        user = UserLogin.__authenticate(email = form_data.email,
                            password = form_data.password)

        if not user:
            raise HTTPException(
                status_code=400, detail="incorrect username or password")

        access_token_expires = timedelta(minutes = UserLogin.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = UserLogin.__create_access_token(
            data={"sub": user.name,"id": user.id}, expire_delta = access_token_expires
        )
        
        token_detail = { 
                "is_admin":user.is_admin,
                "access_token": access_token,
                "token_type": "bearer" 

                }

        return token_detail

