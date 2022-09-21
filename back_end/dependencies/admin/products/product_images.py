from fastapi import Depends, UploadFile, File
import random
from back_end.database.tables.tb_product import TBProducts
from back_end.database.tables.tb_product_images import TBProductImages
from back_end.dependencies.admin.products.product import AdminProducts
from back_end.dependencies.login import UserLogin, token_auth_scheme


class AdminProductImages(AdminProducts, UserLogin):
      
    def __rename_image_name(image, name: str):

        txt = image.filename
        split_image_name = txt.split(".")
       
        split_image_name[0] = name+str(random.randint(0, 100000))
        image_name = '.'.join(split_image_name)
        print(image_name)
        with open(f'images/{name}/{image_name}', "wb") as buffer:
            buffer.write(image.file.read())
        
        return image_name

    def  upload_product_images(self,id: int, images_list: list[UploadFile] = File(...), token: str = Depends(token_auth_scheme)):
        
        user = AdminProductImages._get_user(token)

        if user[2] == 1:
        
            for image in images_list:

                image_name = AdminProductImages.__rename_image_name(image, "products")

                images = TBProductImages(
                    name = image_name,
                    product_id = id,
                    user_id = user[1])

                AdminProductImages._add_in_table(self, images)

            get_data = self.db.query(TBProductImages).filter(TBProductImages.product_id == id).limit(1).all()
        
            self.db.query(TBProducts).filter(TBProducts.id == id).update({
                TBProducts.thumbnail_id : get_data[0].id
            })
            self.db.commit()
            return {"message":"Product Images added successfully"}

        return {"message":"Could Not Valid Credentials"}
        
    def view_product_images(self,id: int, token: str = Depends(token_auth_scheme)):
        user = AdminProductImages._get_user(token)

        if user[2] == 1:
            query  = self.db.query(TBProductImages).filter(TBProductImages.id == id).first()
            
            return {"data": query,"success":True}

        return {"data":"Could Not Valid Credentials"}

    def change_product_images(self, id:int, name: UploadFile, token: str = Depends(token_auth_scheme)):
        user = AdminProductImages._get_user(token)
        
        if user[2] == 1:
            
            query = self.db.query(TBProductImages).get(id)
            
            if query:
                with open(f'images/products/{query.name}', "wb") as buffer:
                    buffer.write(name.file.read())
            
                return { "message": "Product Images Updated successfully" }

            return { "message": "Images doesn't exist" }

        return { "message":"Could Not Valid Credentials" }
