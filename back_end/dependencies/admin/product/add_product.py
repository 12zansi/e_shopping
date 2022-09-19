from back_end.Models.product import Product
from back_end.database.tables.tb_product import TBProducts
from back_end.dependencies.add_into_table import AddIntoTable
from back_end.dependencies.login import UserLogin, token_auth_scheme
from fastapi import Depends
from back_end.database.session import start_session
from requests import Session


class AdminProducts(UserLogin,AddIntoTable):
      

    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data

    
    def  publish_product(self, product:Product, token: str = Depends(token_auth_scheme)):
        
        user = AdminProducts._get_user(token)
        print(user[2])
        if user[2] == 1:
            
            query  = self.db.query(TBProducts).filter(TBProducts.name == product.name  and TBProducts.user_id == user[1]).first()
    
            if not query:
           
                new_product_query = TBProducts(name = product.name,
                                    description = product.description,
                                    mrp = product.mrp,
                                    price = product.price,
                                    brand_id = product.brand_id,
                                    category_id = product.category_id,
                                    return_policy_in_days = product.return_policy_in_days,
                                    user_id = user[1])


                AdminProducts._add_in_table(self,new_product_query)

                return {"message":new_product_query}

            return {"message":"Product Already Added"}

        return {"message":"Could Not Valid Credentials"}
        
    def view_product(self,id: int, token: str = Depends(token_auth_scheme)):
        user = AdminProducts._get_user(token)

        if user[2] == 1:
            
            query = self.db.query(TBProducts).filter(TBProducts.id == id).first()
            
            return {"data": query,"success":True}

        return {"data":"Could Not Valid Credentials"}

    def change_product(self, id:int, product:Product, token: str = Depends(token_auth_scheme)):
        user = AdminProducts._get_user(token)
        
        if user[2] == 1:
            
            query = self.db.query(TBProducts).filter(TBProducts.id == id, TBProducts.user_id == user[1]).update({
               
                TBProducts.name: product.name,
                TBProducts.description: product.description,
                TBProducts.mrp: product.mrp,
                TBProducts.price: product.price,
                TBProducts.brand_id: product.brand_id,
                TBProducts.category_id: product.category_id,
                TBProducts.return_policy_in_days: product.return_policy_in_days,
                TBProducts.user_id: user[1] })
           
        
            self.db.commit()
            if not query:
                return { "message": "product doesn't exist" }

            return { "message": "product successfully updated" }
           
        return { "message":"Could Not Valid Credentials" }
