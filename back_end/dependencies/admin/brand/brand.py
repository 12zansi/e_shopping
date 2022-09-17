from back_end.Models.brand import Brand
from back_end.database.connection import cursor, connection
from fastapi import Depends
from back_end.dependencies.login import UserLogin,token_auth_scheme


class AdminBrand(UserLogin):
      
    def  add_brand(self, brand: Brand , token: str = Depends(token_auth_scheme)):
        
        user = AdminBrand._get_user(token)

        if user[2] == 1:
            
            query = """INSERT INTO brand(name) VALUES (%s)"""
            value = (brand.name)
            cursor.execute(query, value)
            connection.commit()

            return "Brand add successfully"

        return "Could Not Valid Credentials"
        
    def get_brand(self,id: int, token: str = Depends(token_auth_scheme)):
        user = AdminBrand._get_user(token)

        if user[2] == 1:
            query = """SELECT * FROM brand WHERE id = %s"""
          
            cursor.execute(query, id)
            result = cursor.fetchone()

            return {"data":result,"success":True}

        return {"data":"Could Not Valid Credentials"}

    def update_brand(self,id: int, brand: Brand , token: str = Depends(token_auth_scheme)):
        user = AdminBrand._get_user(token)

        if user[2] == 1:
            
            query = """UPDATE  brand SET name = %s WHERE id = %s"""
            value = (brand.name, id)
            cursor.execute(query, value)
            connection.commit()

            return "Brand Update successfully"

        return "Could Not Valid Credentials"
     
