from datetime import datetime, timedelta
from back_end.Models.login import Login
from back_end.database.connection import my_cursor
from back_end.dependencies.users.user_info.register import UsersRegister
from jose import jwt, JWTError
from fastapi import HTTPException

class UserLogin:
    _JWT_SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    Algorithm = "HS256"

    def __verify_password(plain_password: str, hashed_password: str) -> bool:
        
        return UsersRegister.PWD_CONTEXT.verify(plain_password, hashed_password)

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
        my_cursor.execute(query, (email,))
        

        result = my_cursor.fetchall()
        print(result[0][3])

        if not result:
            return None
        if not UserLogin.__verify_password(password, result[0][3]):
            return None

        return {"id":result[0][0],"name":result[0][1],"email":result[0][2],"password":result[0][3],"is_admin":result[0][4]}

    def login(self,form_data:Login):
        user = UserLogin.__authenticate(email = form_data.email,
                            password = form_data.password)
        if not user:
            raise HTTPException(
                status_code=400, detail="incorrect username or password")

        access_token_expires = timedelta(minutes = UserLogin.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = UserLogin.__create_access_token(
            data={"sub": user['name'],"id": user['id']}, expire_delta = access_token_expires
        )

        return {"id":user['id'], "name":user['name'], "is_admin":user['is_admin'], "access_token": access_token, "token_type": "bearer" }

