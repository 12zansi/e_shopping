from fastapi import Depends
from back_end.database.mysql.profile import Profile
from back_end.database.tables.tb_users import TBUsers
from back_end.dependencies.login import UserLogin,token_auth_scheme
from back_end.database.session import start_session
from requests import Session


class UserProfile(UserLogin):
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def get_profile(self, token:str = Depends(token_auth_scheme)):
    
        user = UserProfile._get_user(token)

        query = self.db.query(TBUsers.id, TBUsers.name, TBUsers.email, TBUsers.is_admin).filter(TBUsers.id == user[1]).first()
        result = Profile()
        result.id = query[0]
        result.name = query[1]
        result.email = query[2]
        result.is_admin = query[3]
       
        return result
    