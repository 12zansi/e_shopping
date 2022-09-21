from back_end.Models.favorite_list import FavoriteList
from fastapi import Depends
from back_end.database.mysql.favoritlist import UserFavoriteList
from back_end.database.tables.tb_favorite import TBFavorites
from back_end.database.tables.tb_product import TBProducts
from back_end.database.tables.tb_product_images import TBProductImages
from back_end.dependencies.login import UserLogin,token_auth_scheme
from back_end.database.session import start_session
from requests import Session
from sqlalchemy import and_

class UserFavorite(UserLogin):
    def __init__(self,db: Session = Depends(start_session)):
      self.db = db   

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data


    def  get_favorite_list(self,token:str = Depends(token_auth_scheme)):
        user = UserFavorite._get_user(token)

        query = self.db.query(TBFavorites.id,TBProducts.id,TBProducts.name,TBProducts.price,TBProducts.mrp,TBProductImages.name, TBFavorites.user_id)\
            .outerjoin(TBFavorites, TBProducts.id == TBFavorites.product_id)\
            .outerjoin(TBProductImages, TBProducts.thumbnail_id == TBProductImages.id)\
            .filter(TBFavorites.user_id == user[1]).all()
        
        favorite_list = []
        for data in query:
            favorite = UserFavoriteList()

            favorite.id = data[0]
            favorite.product_id = data[1]
            favorite.name = data[2]
            favorite.price = data[3]
            favorite.mrp = data[4]
            favorite.image_name = data[5]
            favorite.user_id = data[6]

            favorite_list.append(favorite)
        return favorite_list
        
        # return query 

    def add_into_favorite_list(self,favorite_list: FavoriteList, token:str = Depends(token_auth_scheme)):
        user = UserFavorite._get_user(token)
    
        query  = self.db.query(TBFavorites).filter(and_(TBFavorites.product_id == favorite_list.product_id, TBFavorites.user_id == user[1])).first()
    
        if query:
            return {"message":"product already added"}
        
        product_query =  TBFavorites(product_id = favorite_list.product_id,
          user_id = user[1]
         )

        UserFavorite._add_in_table(self, product_query)

        return { "data": product_query, "success": True }

    def delete_into_favorite_list(self,id:int, token:str = Depends(token_auth_scheme)):
        
        user = UserFavorite._get_user(token)
        
        query = self.db.query(TBFavorites).filter(and_(TBFavorites.user_id == user[1], TBFavorites.id == id))\
          .delete()
        self.db.commit()

        if not query:
            return { "success": False }
            
        return { "success": True }
