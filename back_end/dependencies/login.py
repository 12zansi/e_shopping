from datetime import datetime, timedelta
from back_end.Models.login import Login
from back_end.database.tables.tb_users import TBUsers
from back_end.dependencies.users.user_info.register import UsersRegister
from jose import jwt, JWTError
from fastapi import HTTPException
from fastapi import Depends,HTTPException
from fastapi.security import HTTPBearer 
from back_end.database.session import start_session
from requests import Session


token_auth_scheme = HTTPBearer()

class UserLogin:
    _JWT_SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ACCESS_TOKEN_EXPIRE_MINUTES = 55
    Algorithm = "HS256"

    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def __verify_password(plain_password: str, hashed_password: str):
        return UsersRegister.pwd_context.verify(plain_password, hashed_password)

    def __create_access_token(data: dict, expire_delta: timedelta | None = None):
        to_encode = data.copy()
        if expire_delta:
            expire = datetime.utcnow() + expire_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes = 55)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, UserLogin._JWT_SECRET, algorithm = UserLogin.Algorithm)
        
        return encoded_jwt

    def _get_user(token:str = Depends(token_auth_scheme)):

        try:
            payload = jwt.decode(token.credentials, UserLogin._JWT_SECRET, algorithms=['HS256'])
            username: str = payload.get("sub")
            user_id: str = payload.get("user_id")
            is_admin: str = payload.get("is_admin")
     

        except jwt.ExpiredSignatureError:
           raise HTTPException(status_code=403, detail="token has been expired")
        
        except JWTError:
           raise HTTPException(status_code=401, detail="Could Not Valid Credentials")
        
        return username,user_id,is_admin

    def __authenticate(
        self,
        email: str,
        password: str,
    ):
        user = self.db.query(TBUsers).filter(TBUsers.email == email).first()
        
        
        if not user:
            return None
        if not UserLogin.__verify_password(password, user.password):
            return None
        
        return user

    def login(self,form_data:Login):
        user = UserLogin.__authenticate(self,email = form_data.email,
                            password=form_data.password)
        if not user:
            raise HTTPException(
                status_code=400, detail="incorrect username or password")
        if user.otp != 0:
            raise HTTPException(  status_code=400,detail="please verify otp")


    
        access_token_expires = timedelta(minutes = UserLogin.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = UserLogin.__create_access_token(
            data={"sub": user.name,"user_id":user.id,"is_admin":user.is_admin}, expire_delta = access_token_expires
        )
        return { "is_admin":user.is_admin,"access_token": access_token, "token_type": "bearer"}
