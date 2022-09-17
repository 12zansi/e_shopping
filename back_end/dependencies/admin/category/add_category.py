from typing import Optional
from back_end.database.connection import cursor, connection
from fastapi import Depends, UploadFile, File
from back_end.dependencies.login import UserLogin,token_auth_scheme


class AdminCategories(UserLogin):
      
    def  add_brand(self, name: str, image_name : UploadFile = File(...), parent_id: Optional[str] = 0 , token: str = Depends(token_auth_scheme)):
        
        user = AdminCategories._get_user(token)

        if user[2] == 1:
            
            query = """INSERT INTO category(name,image_name,parent_id) VALUES (%s,%s,%s)"""
            value = (name, image_name, parent_id)
            cursor.execute(query, value)
            connection.commit()

            return "Category add successfully"

        return "Could Not Valid Credentials"
        
    def view_category(self,id: int, token: str = Depends(token_auth_scheme)):
        user = AdminCategories._get_user(token)

        if user[2] == 1:
            query = """SELECT * FROM category WHERE id = %s"""
          
            cursor.execute(query, id)
            result = cursor.fetchone()

            return {"data":result,"success":True}

        return {"data":"Could Not Valid Credentials"}

    def change_category(self,id: int, name: str, image_name : UploadFile = File(...), parent_id: Optional[str] = 0 , token: str = Depends(token_auth_scheme)):
        user = AdminCategories._get_user(token)
        

        if user[2] == 1:
            
            query = """UPDATE category SET name = %s, image = %s, parent_id = %s WHERE id = %s"""
            value = (name,image_name,parent_id, id)
            cursor.execute(query, value)
            connection.commit()
            return "category Update successfully"

        return "Could Not Valid Credentials"
