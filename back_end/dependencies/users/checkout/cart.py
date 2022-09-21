from fastapi import Depends, Query
from back_end.Models.cart import OrderItem
from back_end.database.tables.tb_cart import TBCarts
from back_end.database.tables.tb_order_item import TBOrderItems
from back_end.database.tables.tb_product import TBProducts
from back_end.database.tables.tb_product_images import TBProductImages
from back_end.dependencies.add_into_table import AddIntoTable
from back_end.dependencies.login import UserLogin,token_auth_scheme
from sqlalchemy import and_
import random
import shutil
import os

    
class UserCart(UserLogin, AddIntoTable):

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data

    def add_in_cart(self, cart: OrderItem, token:str = Depends(token_auth_scheme)):
        user = UserCart._get_user(token)
    
        query  = self.db.query(TBOrderItems).filter(and_(TBOrderItems.product_id == cart.product_id, TBOrderItems.user_id == user[1], TBOrderItems.order_id == None)).first()

        if query:
            return { "data": "item already added"}
        
        self.db.query(TBCarts.id).filter(TBCarts.user_id == user[1])\
            .update({TBCarts.status_id : 1})
        self.db.commit()

        product_query  = self.db.query(TBProducts, TBProductImages).join(TBProductImages, TBProductImages.id == TBProducts.thumbnail_id).filter(TBProducts.id == cart.product_id).first()
        cart_query = self.db.query(TBCarts.id).filter(TBCarts.user_id == user[1]).first()

        split_image_name = product_query[1].name.split(".")
       
        split_image_name[0] = 'order_items'+str(cart_query[0])+str(random.randint(0, 100000))
        image_name = '.'.join(split_image_name)
        shutil.copyfile(f'images/products/{product_query[1].name}', f'images/order_items/{image_name}')
        
        product_query =  TBOrderItems(
           product_name = product_query[0].name,
           product_price = product_query[0].price,
           product_mrp = product_query[0].mrp,
           quantity = 1,
           image_name =  image_name,
           cart_id = cart_query[0],
           product_id = cart.product_id,
           user_id = user[1]
         )

        UserCart._add_in_table(self, product_query)

        return { "data": product_query, "success": True }

    def get_cart_item(self, token:str = Depends(token_auth_scheme)):
        user = UserCart._get_user(token)

        query = self.db.query(TBOrderItems).filter(and_(TBOrderItems.user_id == user[1], TBOrderItems.order_id == None)).all()

        return { "data": query }

    def update_cart_item(self,id:int, quantity: int = Query(default = 1, gt = 0, lt = 5), token:str = Depends(token_auth_scheme)):
        user = UserCart._get_user(token)

        query = self.db.query(TBOrderItems).filter(and_(TBOrderItems.id == id, TBOrderItems.user_id == user[1], TBOrderItems.order_id == None))\
            .update({TBOrderItems.quantity : quantity })

        self.db.commit()

        if query: 
            return { "success": True }

        return { "message": "Items doesn't exist" }

    def delete_cart_item(self, id: int, token:str = Depends(token_auth_scheme)):
        user = UserCart._get_user(token)

        query = self.db.query(TBOrderItems).filter(and_(TBOrderItems.user_id == user[1], TBOrderItems.id == id, TBOrderItems.order_id == None))
        result = query.first()
        

        if result:
            if os.path.exists(f'images/order_items/{result.image_name}'):
            
              os.remove(f'images/order_items/{result.image_name}')
              query.delete()
              self.db.commit()
            return {"message": "Item Successfully removed"}
        
        return {"message": "item doesn't exist"}