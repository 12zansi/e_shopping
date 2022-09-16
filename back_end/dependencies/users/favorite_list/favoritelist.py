from back_end.Models.favorite_list import FavoriteList
from back_end.database.connection import cursor, connection
from fastapi import Depends
from back_end.dependencies.login import UserLogin,token_auth_scheme


class UserFavorite(UserLogin):

    def  get_favorite_list(self,token:str = Depends(token_auth_scheme)):
        username, user_id = UserFavorite._get_user(token)
    
        query = """SELECT product.id,product.name, product.price,product.mrp FROM product LEFT JOIN favorite ON favorite.product_id = product.id  WHERE  favorite.user_id = %s"""
        cursor.execute(query,(user_id, ))
        result = cursor.fetchall()
        return result   

    def add_into_favorite_list(self,favorite_list: FavoriteList, token:str = Depends(token_auth_scheme)):
        username, user_id = UserFavorite._get_user(token)
        query = """INSERT INTO favorite (product_id,user_id) VALUES(%s, %s)"""
        val = (favorite_list.product_id,user_id)
        cursor.execute(query, val)
        connection.commit()

        return "product  successfully add in favoritelist"

    def delete_into_favorite_list(self,id:int, token:str = Depends(token_auth_scheme)):
        query = """DELETE FROM favorite WHERE id = %s"""
        value = (id,)
        cursor.execute(query, value)
        connection.commit()

        return "product removed from the favorite list"
