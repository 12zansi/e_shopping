from typing import Optional,Union
from fastapi import FastAPI, Path
from back_end.Models.brand import Brand
from back_end.Models.category import Category
from back_end.Models.login import Login
from back_end.Models.product import Product, ProductDetail
from back_end.Models.product_return import ProductReturn

from back_end.Models.register import Register
from back_end.Models.review import Review
from back_end.enum.search import ModelName



app = FastAPI(
    title="e-Shopping",
    description="This is online shopping site for customer."
)

@app.post('/api/auth/register', tags = ['auth'])
def register(user:Register):
    return { "success": True }

@app.post('/api/auth/login', tags = ['auth'])
def login(user:Login):
   return { "success": True }

@app.get('/api/admin/dashboard', tags = ['admin'])
def  get_all_report():
    return { "success": True }

@app.get('/api/admin/{search}', tags = ['admin'])
def  get_all_detail(search: ModelName):
    return { "success": True }

@app.post('/api/admin/brands', tags = ['admin'])
def add_brand(brand:Brand):
    return { "success": True }

@app.put('/api/admin/brands/{id}', tags = ['admin'])
def update_brand(brand:Brand, id:int ):
    return { "success": True }

@app.post('/api/admin/categories', tags = ['admin'])
def add_category(category:Category):
    return { "success": True }

@app.put('/api/admin/categories/{id}', tags = ['admin'])
def update_category(id:int,category:Category):
    return { "success": True }

@app.post('/api/admin/products', tags = ['admin'])
def add_product(product:Product):
    return { "success": True }

@app.put('/api/admin/products/{id}', tags = ['admin'])
def update_product(id:int):
    return { "success": True }

@app.post('/api/admin/product/images', tags = ['admin'])
def add_images():
    return { "success": True }

@app.put('/api/admin/product/images', tags = ['admin'])
def update_images():
    return { "success": True }

@app.post('/api/admin/product/detail', tags = ['admin'])
def add_detail(detail:ProductDetail):
    return { "success": True }

@app.put('/api/admin/product/detail', tags = ['admin'])
def update_detail():
    return { "success": True }

@app.get('/api/admin/product/detail', tags = ['admin'])
def view_product_detail():
    return { "success": True }

@app.get('/api/admin/orders', tags = ['admin'])
def view_orders():
    return { "success": True }

@app.post('/api/admin/orders/status', tags = ['admin'])
def change_order_status():
    return { "success": True }

@app.get('/api/admin/product/return', tags = ['admin'])
def view_returned_product():
    return { "success": True }

@app.post('/api/admin/return/status', tags = ['admin'])
def change_return_status():
    return { "success": True }

@app.get('/api/admin/product/review', tags = ['admin'])
def view_product_review():
    return { "success": True }

@app.post('/api/address', tags = ['addressbook'])
def add_address():
    return { "success": True }

@app.put('/api/address', tags = ['addressbook'])
def update_address():
    return { "success": True }

@app.get('/api/address', tags = ['addressbook'])
def get_address():
    return { "success": True }

@app.delete('/api/address', tags = ['addressbook'])
def remove_address():
    return { "success": True }

@app.post('/api/user/forgotpassword', tags = ['users'])
def forgot_password():
    return { "success": True }

@app.get('/api/user/{id}/profile', tags = ['users'])
def get_user_profile(id:int):
    return {"success": True}

@app.post('/api/favoritelist', tags = ['favoritelist'])
def add_into_favorite_list():
    return { "success": True }

@app.get('/api/favoritelist', tags = ['favoritelist'])
def view_favorite_products():
    return { "success": True }

@app.delete('/api/favoritelist', tags = ['favoritelist'])
def remove_from_favorite_list(product_id:int):
    return { "success": True }

@app.post('/api/bank/accounts', tags = ['accounts'])
def add_bank_account_detail():
    return { "success": True }

@app.put('/api/bank/accounts/{id}', tags = ['accounts'])
def update_bank_account_detail():
    return { "success": True }

@app.get('/api/bank/accounts/{id}', tags = ['accounts'])
def add_bank_account_detail(id:int):
    return { "success": True }

@app.get('/api/user/return', tags = ['users'])
def get_returned_product():
    return {"success": True}

@app.get('/api/category', tags = ['category'])
def view_category(q : str):
    return {"success": True}

@app.get('/api/category/{id}/child', tags = ['category'])
def view_child_category(id:int):
    return {"success": True}

@app.get('/api/category/{id}/parent', tags = ['category'])
def view_parent_category(id:int):
    return {"success": True}

@app.get('/api/brand/{id}', tags = ['brand'])
def view_brand(id:int):
    return {"success": True}


@app.get('/api/search', tags = ['products'])
def view_product(q: str):
    return {"success": True}

@app.get('/api/product/{id}', tags = ['products'])
def view_product_detail(id:int):
    return {"success": True}

@app.post('/api/product/{id}/review', tags = ['products'])
def add_review(id:int, product:Review):
    return {"success": True}

@app.get('/api/product/{id}/review', tags = ['products'])
def get_review(id:int):
    return {"success": True}

@app.post('/api/product/return', tags = ['products'])
def create_return_request(product:ProductReturn):
    return {"success": True}


@app.post('/api/carts', tags = ['carts'])
def add_into_cart(product_name: str, product_price: int, product_mrp: int, user_id: int):
    return {"success": True}

@app.get('/api/users/{id}/carts', tags = ['carts'])
def view_cart():
   return {"success": True}

@app.put('/api/carts/{id}', tags = ['carts'])
def update_quantity(id:int,qauntity:int):
    return {"success": True}

@app.delete('/api/carts/{id}', tags = ['carts'])
def remove_item(id: Optional[int] = None):
    return {"success": True}


@app.post('/api/orders', tags = ['orders'])
def place_an_order():
   return {"success": True}

@app.post('/api/orders/{id}/cancel', tags = ['orders'])
def cancel_order(id:int):
    return {"success": True}

@app.get('/api/orders/{id}', tags = ['orders'])
def get_order_detail(id:Optional[int] = None):
    return {"success": True}



