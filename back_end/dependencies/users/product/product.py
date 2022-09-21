from fastapi import Depends
from requests import Session
from back_end.Models.product_return import ProductReturn
from back_end.database.session import start_session
from back_end.database.tables.tb_brand import TBBrands
from back_end.database.tables.tb_category import TBCategories
from back_end.database.tables.tb_product import TBProducts
from back_end.database.tables.tb_product_detail import TBProductDetails
from back_end.database.tables.tb_product_images import TBProductImages
# from back_end.database.mysql.product import TBProduct
from sqlalchemy import or_

from back_end.dependencies.login import UserLogin
class UserProduct(UserLogin):
     
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db  

    def search_product(self, q: str):
        
        query = self.db.query(TBProducts, TBBrands).outerjoin(TBCategories, TBCategories.id == TBProducts.category_id).outerjoin(TBBrands, TBBrands.id == TBProducts.brand_id).filter(or_(TBBrands.name == q, TBCategories.name == q, TBProducts.name == q)).all()
        data_list = []
        # for data in result:
        #     product = TBProduct()
        #     product.id = data[0]
        #     product.name = data[1]
        #     product.mrp = data[3]
        #     product.price = data[2]
        #     product.category_name = data[5]
        #     product.brand_name = data[6]
        #     product.return_policy_in_days = data[4]
        #     data_list.append(product)

        return query

    def get_product_detail(self, id: int):

        query = self.db.query(TBProducts, TBProductImages, TBProductDetails)\
                .join(TBProductImages, TBProductImages.product_id == TBProducts.id)\
                .join(TBProductDetails, TBProductDetails.product_id == TBProducts.id)\
                .filter(TBProducts.id == id).all()
            
        return { "data": query,"success":True }

    # def return_request(self, id:int,item_id:int,product:ProductReturn,token: str = Depends(token_auth_scheme)):
        

