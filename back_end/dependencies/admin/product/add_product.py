from back_end.Models.product import Product
from back_end.database.connection import cursor, connection
from back_end.dependencies.login import UserLogin, token_auth_scheme


class AdminProduct(UserLogin):
      
    def  publish_product(self, product:Product, token: str = Depends(token_auth_scheme)):
        
        user = Adminproduct._get_user(token)

        if user[2] == 1:
            
            query = """INSERT INTO product(name, description, mrp, price, category_id, brand_id, return_policy_in_days, user_id) VALUES (%s, %s, %s, %s, %s, %s,%s, %s)"""
            value = (product.name, product.description, product.mrp, product.price, product.category_id, product.brand_id, product.return_policy_in_days, user[2])
            cursor.execute(query, value)
            connection.commit()

            return "product added successfully"

        return "Could Not Valid Credentials"
        
    def view_product(self,id: int, token: str = Depends(token_auth_scheme)):
        user = Adminproduct._get_user(token)

        if user[2] == 1:
            query = """SELECT * FROM product WHERE id = %s"""
          
            cursor.execute(query, (id,))
            result = cursor.fetchone()

            return {"data":result,"success":True}

        return {"data":"Could Not Valid Credentials"}

    def change_product(self, id:int, product:Product, token: str = Depends(token_auth_scheme)):
        user = Adminproduct._get_user(token)
        
        if user[2] == 1:
            
            query = """UPDATE product SET name = %s, description = %s, price = %s, mrp = %s , category_id = %s , brand_id = %s , return_policy_in_days = %s ,  WHERE id = %s"""
            value = (product.name, product.description, product.mrp, product.price, product.category_id, product.brand_id, product.return_policy_in_days,id)
            cursor.execute(query, value)
            connection.commit()
            return "product Updated successfully"

        return "Could Not Valid Credentials"
