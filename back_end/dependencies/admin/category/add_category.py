from email.policy import default
from typing import Optional
import random
from back_end.database.connection import cursor, connection
from fastapi import Depends, UploadFile, File, Form
from back_end.database.tables.tb_category import TBCategories
from back_end.dependencies.add_into_table import AddIntoTable
from back_end.dependencies.login import UserLogin,token_auth_scheme
from back_end.database.session import start_session
from requests import Session
import os  

class AdminCategories(UserLogin, AddIntoTable):
    
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data

    def __rename_image_name(image, name: str):

        txt = image.filename
        split_image_name = txt.split(".")
       
        split_image_name[0] = name+str(random.randint(0, 100000))
        image_name = '.'.join(split_image_name)
        print(image_name)
        with open(f'images/{name}/{image_name}', "wb") as buffer:
            buffer.write(image.file.read())
        
        return image_name

    def  publish_category(self, name: str = Form(...), image_name : UploadFile = File(...), parent_id: str= Form(default = 0) , token: str = Depends(token_auth_scheme)):
        
        user = AdminCategories._get_user(token)

        if user[2] == 1:
            query  = self.db.query(TBCategories).filter(TBCategories.name == name).first()
    
            if not query:
                image = AdminCategories.__rename_image_name(image_name, "categories")

                query = TBCategories(
                    name = name,
                    image_name = image,
                    parent_id = parent_id)

                AdminCategories._add_in_table(self, query)

                return {"data":query,"success":True}

            return {"message":"category Already Added"}

        return "Could Not Valid Credentials"
        
    def view_category(self,id: int, token: str = Depends(token_auth_scheme)):
        user = AdminCategories._get_user(token)

        if user[2] == 1:
        
            query  = self.db.query(TBCategories).filter(TBCategories.id == id).first()

            return {"data": query,"success":True}

        return {"data":"Could Not Valid Credentials"}

    def change_category(self,id: int, name: str  = Form(...), image_name : UploadFile = File(default = None), parent_id: str = Form(default = 0) , token: str = Depends(token_auth_scheme)):
        user = AdminCategories._get_user(token)
        

        if user[2] == 1:
            query = self.db.query(TBCategories).filter(TBCategories.id == id)\
                .update({ TBCategories.name : name, TBCategories.parent_id : parent_id })
    
            self.db.commit()
        
            if query:
                if image_name != None:
                    image = self.db.query(TBCategories).get(id)
                    with open(f'images/categories/{image.image_name}', "wb") as buffer:
                       buffer.write(image_name.file.read())
                return { "message": "category successfully updated" }
    
            return { "message": "category doesn't exist" }

        return { "message": "Could Not Valid Credentials" }
