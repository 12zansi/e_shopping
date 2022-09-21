
from fastapi import Depends
from requests import Session
from back_end.database.session import start_session
from back_end.database.tables.tb_brand import TBBrands


class UserBrand:
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def get_brand(self, id: int):

        query = self.db.query(TBBrands).filter(
                TBBrands.id == id).first()

        return {"data": query,"success": True}



    
