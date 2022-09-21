from back_end.Models.brand import Brand
from fastapi import Depends
from back_end.database.session import start_session
from requests import Session
from back_end.database.tables.tb_brand import TBBrands
from back_end.dependencies.login import UserLogin, token_auth_scheme


class AdminBrands(UserLogin):
      
    def __init__(self, db: Session = Depends(start_session)):
        self.db = db

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data

    def  add_brand(self, brand: Brand , token: str = Depends(token_auth_scheme)):
        
        user = AdminBrands._get_user(token)

        if user[2] == 1:
            query  = self.db.query(TBBrands).filter(TBBrands.name == brand.name).first()
    
            if not query:
                new_brand = TBBrands(name = brand.name)
            
                AdminBrands._add_in_table(self, new_brand)
                return { "data": new_brand, "success": True }

            return {"message": "Brand already Exists"}
          
        return {"message": "Could Not Valid Credentials"}

        
        
    def get_brand(self,id: int, token: str = Depends(token_auth_scheme)):
        user = AdminBrands._get_user(token)

        if user[2] == 1:
          
                query = self.db.query(TBBrands).filter(
                        TBBrands.id == id).first()

                return {"data": query,"success": True}

        return {"message": "Could Not Valid Credentials"}


    def change_brand(self,id: int, brand: Brand , token: str = Depends(token_auth_scheme)):
        user = AdminBrands._get_user(token)

        if user[2] == 1:
             
            query = self.db.query(TBBrands).filter(TBBrands.id == id)\
                .update({TBBrands.name: brand.name})

            self.db.commit()
            if query:
                return {"detail": "Brand No "+ str(id) +" Updated successfully"}

            return {"detail": "Brand No "+ str(id) +" doesn't exists"}

        return {"message": "Could Not Valid Credentials"}

    def delete_brand(self,id: int, token: str = Depends(token_auth_scheme)):
        user = AdminBrands._get_user(token)
        
        if user[2] == 1:
            query  = self.db.query(TBBrands).filter(TBBrands.id == id)\
              .update({TBBrands.is_active : 0})

            self.db.commit()
            if query:
               return  { "message": "Brand successfully removed" }

            return { "message": "Brand doesn't exist" }
        
        return { "message": "Could Not Valid Credentials" }
     
