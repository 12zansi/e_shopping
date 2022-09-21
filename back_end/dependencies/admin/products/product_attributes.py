
from back_end.Models.product import ProductAttribute, ProductDetail
from back_end.database.session import start_session
from requests import Session
from fastapi import Depends
from back_end.database.tables.tb_product_detail import TBProductDetails
from back_end.dependencies.admin.products.product import AdminProducts
from back_end.dependencies.login import UserLogin, token_auth_scheme

class AdminProductAttributes(AdminProducts, UserLogin):
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data

    
    def  add_product_attribute(self,id:int, attribute: ProductDetail, token: str = Depends(token_auth_scheme)):
        
        user = AdminProductAttributes._get_user(token)

        if user[2] == 1:
            
            for i, k in attribute.detail.items():
                query = TBProductDetails(
                    attribute_name = i,
                    attribute_value = k,
                    product_id = id,
                    user_id = user[1])


                AdminProductAttributes._add_in_table(self, query)
                
                
            return { "message": "detail successfully added" }

        return { "message":"Could Not Valid Credentials" }
        
    def view_product_attribute(self,id: int, token: str = Depends(token_auth_scheme)):
        user = AdminProductAttributes._get_user(token)
       
        if user[2] == 1:
            
            query = self.db.query(TBProductDetails).filter(TBProductDetails.id == id).first()
            
            return { "data": query,"success":True }

        return { "data":"Could Not Valid Credentials" }

    def change_product_attribute(self, id:int, attribute: ProductAttribute, token: str = Depends(token_auth_scheme)):
        user = AdminProductAttributes._get_user(token)

        if user[2] == 1:
            
            query = self.db.query(TBProductDetails).filter(TBProductDetails.id == id).update({
               
                TBProductDetails.attribute_name: attribute.attribute_name,
                TBProductDetails.attribute_value: attribute.attribute_value,
                TBProductDetails.product_id: attribute.product_id,
                TBProductDetails.user_id: user[1] })
           
        
            self.db.commit()
            if not query:
                return { "message": "product attribute doesn't exist" }

            return { "message": "product attribute successfully updated" }
           
        return { "message": "Could Not Valid Credentials" }
